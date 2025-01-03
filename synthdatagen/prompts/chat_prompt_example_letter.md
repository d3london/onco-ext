# New Letter Generation From Example

Create new synthetic cancer clinic letter based on pre-defined context including letter types, components, and styles, as well as example clinic letter. The example should be a synthetic letter that is hand-crafted to closely represent a real letter. This should be used to capture particular edge cases in language style, letter structure, and other edge cases. 

### Requirements
* types.md
* blocks.md
* styles.md
* example letter

### Prompt
```
You are a highly experienced oncology consultant with deep understanding of medical documentation. You are required to create a synthetic oncology clinic letter using the following parameters and structure.

Required Inputs:
* Random seed (to systematically choose types, structure, and styles)
* Realistic example letter to be provided in following prompt

Use random seed to systematically select (use a modulo function):
* Letter type (from types.md)
* Structural style (from styles.md)

From the realistic example letter that has been provided:
* Please consider all the subblocks found in blocks.md. Perform a highly detailed subblock analysis, and extract these from the example letter in sequential order.
* You will use these subblocks in the letter you create.
* From the example letter, please extract the following information: Cancer diagnosis, biomarker status, metastatic status, treatment course.
* Please discard any other information, including symptoms, examination findings, and all identifying or personal information
* Please select the best Language style that represents the example letter contents. 

Planning (show this thought process):
* Document and use the selected letter type and structural style
* Document and use the same diagnosis, biomarker, metastatic, and treatment statuses (from example letter)
* Document and use the language style (from example letter)
* Map and use the block/subblock flow (from example letter)
* Add additional subblocks, only if required, and only if they are mandatory for the letter type. 
* Create and outline newly constructed clinical reasoning used in the new letter

The letter contents should then be generated using the type, styles, the extracted cancer details, and extracted subblock sequence. Do not use direct descriptions from the example letter, except for subheadings. Any derived content from the example letter should be reworded.

Letter generation requirements:
* Single line output with formatting artifacts (\t, \n, ?, \n?\n)
* Clinical content only (no greetings/sign off/headers/footers)
* Use [redacted name] for all names
* Dates where appropriate, using varied formats (e.g., 2012-5-1, March 2013)
* Logical temporal consistency between subblocks
* Professional medical terminology
* Content reflects realistic cancer presentation, symptoms, and signs
* Clinically coherent measurements and findings
* Logical consistency in disease progression and treatment sequences and timing
* All clinical details are robust and consistent
* Consistency in complciations or toxicities.

Output Format:
* Show planning thought process
* Present letter in code block

The letter must demonstrate clear clinical reasoning, appropriate terminology, logical information flow, and realistic decision-making while avoiding exact copying from examples. Before proceeding, please confirm that this information is understood.
```