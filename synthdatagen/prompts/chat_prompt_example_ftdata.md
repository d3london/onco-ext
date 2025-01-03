# Training Data Creation From Example Letter

Create new synthetic cancer clinic letter and paired structured (json) response, based on pre-defined context including letter types, components, and styles, as well as example clinic letter. The example should be a synthetic letter that is hand-crafted to closely represent a real letter. This should be used to capture particular edge cases in language style, letter structure, and other edge cases. 

### Requirements
* blocks.md
* example letter
* output_schema_v2.json

### Prompt
```
You are a highly experienced oncology consultant with deep understanding of medical documentation. Your task is to write synthetic oncology clinic letters, based on a realistic example, with corresponding structured outputs that capture key clinical concepts. Please make careful note of the structure in output_schema_v2.json, and the example JSONs with prior paired letter / output schema outputs.

Required Inputs:
* Realistic example letter will be provided in following prompt

From the realistic example letter that has been provided:
* Please consider all the subblocks found in blocks.md. Perform a highly detailed subblock analysis, and extract these from the example letter in sequential order. You will use these subblocks in the letter you create
* Please make note of the main primary cancer diagnosis, its stage/biomarker/metastatic status, and the treatment course. Keep these the same, but substantially change the wording.
* For all other subblocks, please discard and replace the original information (for example - historical cancers, symptoms, findings, test results, comorbidities, side-effects and toxicities, etc)
* Discard all identifying, personal, and social information
* Change all dates by multiple years and months, while maintaining temporal consistency
* Keep the overall structure and language style

Planning (show this thought process):
* Document and use the main cancer diagnosis, stage/biomarker/metastatic/treatment statuses from example letter, but entirely change the wording of these subblocks. 
* Map and use the block/subblock flow (from example letter)
* Replace all other information, aside from the main cancer characteristics, with entirely new details
* New clinical information which must be clinically coherent, accurate, and temporally consistent
* New content must reflects realistic cancer presentation, symptoms, complications, signs, and temporal evolution

The letter contents should be generated following the same structure and style, and using the same subheadings as the example. However, do not use direct descriptions. Any derived content from the example letter must be reworded substantially.

Letter generation requirements:
* Single line output with formatting artifacts (\t, \n, ?, \n?\n)
* Clinical content only (no greetings/sign off/headers/footers)
* Use [redacted name] for all names
* Dates where appropriate, using varied formats (e.g., 2012-5-1, March 2013)

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

