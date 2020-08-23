# RIZE-Blockly-Generator
A generator of Google Blockly environments for RIZE

# How to compile and add new blocks:

## Step 1.-  Define new blocks 

Blocks must be defined as JSON files in the "/primitives" folder. 
The name of each primitive will be the name of the JSON file. 
For example, in "object_detected.json" the name of the primitive will be "object_detected".
Therefore, do not use special characters to define the name of these files. 
Use _ instead of space.

## Step 2.- Generate code for Google Blockly 

- run **1.- create.py** (this script transform JSON files to specification for Google Blockly)
- run **2.- files2developer.py** (this script copy and paste the needed files required to run Google Blockly to "/developer" folder)

## Step 3.- Copy and paste content of developer folder to RIZE/developer

# Format to generate new blocks (primitives)

Basic nodes that can be generated are two types:

- Condition/Events = **inputs**
- Actions = **outputs**

## Inputs

Is basically composed of 5 compulsory keys: 
- **"primitive"**: Text to display in the block to guide end users
- **"type"**: must be defined as "input"
- **"description"**: More detailed documentation of the block
- **"input"**: Will define the type of input displayed to the end users

Avaliable options for **"input"**

"string" or "dropdown"

When used "dropdown" you need to add and additional key in the JSON file denoted as "input_options", that will define the available options that users can select

Example for object detected

```javascript
{
    "primitive": "Object detected",
    "type": "output",
    "description": "Select an object that robot can detect",
    "input": "dropdown",
    "input_options":["head", "right_hand", "left_hand"]
}
```

Example for emotion

```javascript
{
    "primitive": "Emotion",
    "type": "input",
    "description": "Select some emotion",
    "input": "dropdown",
    "input_options":["happy", "angry", "sad", "surprised", "neutral"]
}
```

## Outputs

Is basically composed of 5 compulsory keys and 1 optional key: 
- **"primitive"**: Text to display in the block to guide end users
- **"type"**: must be defined as "output"
- **"description"**: More detailed documentation of the block
- **"input"**: Will define the type of input displayed to the end users
- **"options"**: This is the option key which can be composed of several keys for the parametrization of the action


Example for say

```javascript
{
    "primitive": "Say",
    "type": "output",
    "description": "Say something with the robot",
    "input": "string",
    "options":{"contextual":"bool","velocity":"percentage", "pitch":"percentage"}
}
```

When used "dropdown" you need to add and additional key in the JSON file denoted as "input_options", that will define the available options that users can select

Example for track people
```javascript
{
    "primitive": "Track people with",
    "type": "output",
    "description": "Track human",
    "input": "dropdown",
    "input_options":["WholeBody", "Head", "None"],
    "options":{"LeftArm":"bool","RightArm":"bool"}
}
```

### Advanced options

Are defined by the format "*key*":"*type*"

*NOTE: dont use spaces for defining keys*

**Avaliable types:**

bool, dropdown, seconds, minutes, hours, degrees, meters, number and percentage



