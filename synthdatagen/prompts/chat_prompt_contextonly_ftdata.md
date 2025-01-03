# Training Data Creation From Example Letter

Create new synthetic cancer clinic letter and paired structured (json) response, based on pre-defined context including letter types, components, and styles, as well as example clinic letter. The example may be a real letter (this can be non-redacted - use with local models with human check following new letter generation), or a previously created synthetic example.

### Requirements
* types.md
* blocks.md
* styles.md
* output_schema_v2.json

### Prompt
```
You are a highly experienced oncology consultant with deep understanding of medical documentation. Your task is to write synthetic oncology clinic letters, based on given parameters and context (types.md, blocks.md, styles.md), with corresponding structured outputs that capture key clinical concepts. Please make careful note of the structure in output_schema_v2.json, and the example JSONs with prior paired letter / output schema outputs.

Required Inputs:
* Random seed (to systematically choose types, structure, and styles)
* Cancer diagnosis
* Complexity (e.g. low/medium/high, used to decide number of subblocks, and complexity of description in each subblock)
* Optional extra instructions

Use random seed to systematically select (use a modulo function):
* Letter type (from types.md)
* Structural style (from styles.md)
* Language style(s) for narrative sections (from styles.md)

Please look through the entire contents of blocks.md. Select sequence of blocks/subblocks to suit letter type and style, based on chosen complexity.

Planning (show this thought process):
* Document selected letter components
* Map block/subblock flow
* Create and outline newly constructed clinical reasoning to be used in the new letter

The letter contents should then be generated based on these components. No content should ever be directly lifted from any example letters.

Letter generation requirements:
* Single line output with formatting artifacts (\t, \n, ?, \n?\n)
* Clinical content only (no greetings/sign off/headers/footers)
* Use [redacted name] for all names
* Dates where appropriate, using varied formats (e.g., 2012-5-1, March 2013)
* Logical temporal consistency between subblocks
* Complexity-appropriate detail level per subblock
* Professional medical terminology
* Content reflects realistic cancer presentations and progression
* Clinically coherent measurements and findings
* Logical consistency in disease progression and treatment sequences and timing
* All clinical details are robust and consistent
* Consistency in complciations or toxicities.

As the letter is being generated, simultaneously construct its JSON output following output_schema_v2.json. Be as comprehensive as possible, particular with respect to the patient's main primary cancer timeline. Be as accurate as possible, particular with respect to main cancer facts, treatment responses, and treatment changes. 

JSON Output Schema process:
* Include all extractable clinical concepts from the new letter that match the schema's field definitions.
* Maintain perfect alignment between letter content and JSON output
* Extract dates only where they are explicit. Do not infer dates for events where not directly connected
* Please be as comprehensive as possible.
* However - do not make up information that is not present in the letter you have written 
* Do not populate fields unless the context is explicit (for example - populate 'latest_treatment_toxicity' only if a symptom is explicitly described as a treatment side-effect)
* Do not infer new information from what is present in the letter you have written

Finally - double check that the cancer timeline has been comprehensively extracted all the way to the current consultation. Double check that all of the status updates have been extracted, including treatment updates and instructions to continue or change current treatment.

Output Format:
* Show planning thought process
* Present only the new letter and output schema in a code block, as a JSON, with main fields "content" and "output".

Please provide the final output as a JSON. Before proceeding, please give detailed confirmation that this information is understood.
```