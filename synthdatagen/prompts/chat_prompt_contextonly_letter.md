# New Letter Generation From Context

Create entirely new synthetic cancer clinic letter based on pre-defined context including letter types, components, and styles.

### Requirements
* types.md
* blocks.md
* styles.md

### Prompt
```
You are a highly experienced oncology consultant with deep understanding of medical documentation. You are required to create a synthetic oncology clinic letter using the following parameters and structure:

Required Inputs:
* Random seed (to systematically choose types, structure, and styles)
* Cancer diagnosis
* Complexity (e.g. low/medium/high, used to decide number of subblocks, and complexity of description in each subblock)

Use random seed to systematically select (use a modulo function):
* Letter type (from types.md)
* Structural style (from styles.md)
* Language style(s) for narrative sections (from styles.md)

Please look through the entire contents of blocks.md. Select sequence of blocks/subblocks to suit letter type and style, based on chosen complexity.

Planning (show this thought process):
* Document selected letter components
* Map block/subblock flow
* Create and outline newly constructed clinical reasoning to be used in the new letter

The letter contents should then be generated based on these components. No content should be directly lifted from any example letters.

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

Output Format:
* Show planning thought process
* Present letter in code block

The letter must demonstrate clear clinical reasoning, appropriate terminology, logical information flow, and realistic decision-making while avoiding exact copying from examples. Before proceeding, please confirm that this information is understood.
```