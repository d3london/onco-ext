import anthropic
import pandas as pd
import json
import re
import time
import os
from dotenv import load_dotenv

# load api key
load_dotenv()
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')

# functions
def extract_json_from_response(response):
    """
    Extract JSON from Claude's response, handle any potential output formatting variation
    """
    # claude may return a text block or a list...
    if hasattr(response, 'text'):
        response = response.text
    elif isinstance(response, list):
        response = response[0].text

    # try parse response as JSON
    try:
        return json.loads(response)
    except json.JSONDecodeError:
        # try to find JSON in a code block
        json_match = re.search(r'```json\s*(.*?)\s*```', response, re.DOTALL)
        if json_match:
            try:
                return json.loads(json_match.group(1))
            except json.JSONDecodeError:
                pass

        # If fails, try to find any JSON-like structure
        json_match = re.search(r'{[\s\S]*}', response)
        if json_match:
            try:
                return json.loads(json_match.group(0))
            except json.JSONDecodeError:
                raise Exception("Could not parse JSON from response")

        print("No valid JSON found in response")
        return None

# load context data and features array
with open('context/types.md', 'r') as f:
    types_content = f.read()

with open('context/styles.md', 'r') as f:
    styles_content = f.read()

with open('context/blocks.md', 'r') as f:
    blocks_content = f.read()

with open('context/output_schema_v2.json', 'r') as f:
    schema_content = f.read()

datagen = pd.read_csv('datagen.csv')

# system prompt providing context for synthetic letter generation
system_prompt = f"""You are an oncology specialist doctor experienced at writing cancer clinic letters, and extracting their information into structured forms. Please take note of the following documents: types.md: {types_content}; styles.md: {styles_content}; blocks.md: {blocks_content}; output_schema_v2.json: {schema_content}"""

# initialise anthropic connection
client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

for index, row in datagen.iterrows():
    print(f"Processing row {index + 1} of {len(datagen)}")

    # get array row as dict to pass into prompt
    row_data = row.to_dict()

    time.sleep(1) # API rate limit
    try:
        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=8192,
            temperature=0,
            system=system_prompt,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text":f"""You are a highly experienced and senior oncology doctor with deep understanding of medical documentation. Your task is to write synthetic oncology clinic letters, based on given parameters and context (types.md, blocks.md, styles.md), with corresponding structured outputs that capture key clinical concepts (output_schema_v2.json). Please make careful note of the structure of output_schema_v2.json.\n\nRequired Inputs:\n* An array of items to help generate a letter - these include in order: topography,morphology,stage,biomarker,extent_mets,disease_trajectory,treatment_complexity,excluded_subblocks,data_quality_issue,letter_type from types.md),structural_style from styles.md,language_style from styles.md\n\nGiven the letter type and structural style, and the other array contents, please look through the entire contents of blocks.md and select sequence of blocks/subblocks that best suits.\n\nPlanning (silent):\n* Map block/subblock flow\n* Create new clinical reasoning starting from array contents, and then based on newly generated clinical information, to be used in the new letter\n* Array contents should not be used verbatim, but should provide baseline information for letter contents\n\nLetter content should not be directly lifted from any example letters.\n\nLetter generation requirements:\n* Single line output with formatting artifacts (\\t, \\n, ?, \\n?\\n)\n* Clinical content only (no greetings/sign off/headers/footers)\n* Use [redacted name] for all names\n* Dates where appropriate, using varied formats (e.g., 2012-5-1, March 2013)\n* Logical temporal consistency between subblocks\n* Complexity-appropriate detail level per subblock\n* Professional medical terminology\n* Content reflects realistic cancer presentations and progression\n* Clinically coherent measurements and findings\n* Logical consistency in disease progression and treatment sequences and timing\n* All clinical details are robust and consistent\n* Consistency in complciations or toxicities.\n\nAs the letter is being generated, simultaneously construct its JSON output following output_schema_v2.json. Be as comprehensive as possible, particular with respect to the patient's main primary cancer timeline. Be as accurate as possible, particular with respect to main cancer facts, treatment responses, and treatment changes. \n\nJSON Output Schema process:\n* Include all extractable clinical concepts from the new letter that match the schema's field definitions.\n* Maintain perfect alignment between letter content and JSON output\n* Extract dates only where they are explicit. Do not infer dates for events where not directly connected\n* Please be as comprehensive as possible.\n* However - do not make up information that is not present in the letter you have written \n* Do not populate fields unless the context is explicit (for example - populate 'latest_treatment_toxicity' only if a symptom is explicitly described as a treatment side-effect)\n* Do not infer new information from what is present in the letter you have written\n\nFinally - double check that the cancer timeline has been comprehensively extracted all the way to the current consultation. Double check that all of the status updates have been extracted, including treatment updates and instructions to continue or change current treatment.\n\nOutput Format:\nPresent only the new letter and output schema as a JSON file, with main fields \"content\" and \"output\". Dot not provide any other information.\n\nPlease provide the final output as a JSON. \n\nArray: {json.dumps(row_data)}"""
                        }
                    ]
                }
            ]
        )
        # parse json response
        json_output = extract_json_from_response(message.content)

        if json_output is not None:
            output_filename = f"data/api/{row['topography']}_{index + 1}.json"
            try:
                with open(output_filename, 'w', encoding='utf-8') as f:
                    json.dump(json_output, f, indent=2, ensure_ascii=False)
                print(f"Successfully saved output to {output_filename}")
            except Exception as e:
                print(f"error saving JSON to file: {e}")
                print(message.content)
        else:
            print(f"Skipping file save for row {index + 1} due to JSON parsing failure")
            print(message.content)

    except Exception as e:
        print(f"Error processing row {index + 1}: {e}")
        continue

print("processing rows complete")