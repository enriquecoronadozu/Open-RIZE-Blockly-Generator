import rize
import os


# Color for each primitive type
color_OUTPUT = '''"#2196f3"''' 
color_INPUT = '''"#009688"'''
color_output = "#2196f3"
color_input = "#009688"

path_ = os.path.abspath(os.getcwd()) # Path of RIZE-Blockly-Generator folder
print (path_)
blockly = rize.blockly.blockly_files("primitives", path_, color_input,color_output)


rb = rize.blockly.rize_blocks(blockly,color_OUTPUT,color_INPUT)
rb.generate()
blockly.close_files()


def define_toolbox(path):
    name_toolbox = "toolbox"

    js_init = "var " + name_toolbox  + """ = '<xml id="toolbox" style="display: none">';""" + "\n" + "\n"

    blocks = []
    files = ["blocks_inputs.js","blocks_input_operators.js","blocks_actions.js","blocks_outputs.js","blocks_modules.js","blocks_behaviors.js"]

    for f in files:
        try:
            file_ct = open(path + "/" + f, "r") 
            blocks.append(file_ct.read())
        except:
            pass

    xml_text = "var " + name_toolbox  + """ = '<xml id="toolbox" style="display: none">';""" + "\n" + "\n"

    for b in blocks:
        xml_text = xml_text + b + "\n"

    xml_text = xml_text +  name_toolbox + " += '</xml>';"
    return xml_text


toolbox_xml = define_toolbox("toolbox")
path_developer = path_ + "/developer"
file_toolbox = open( path_developer + "/toolbox.js","w")
file_toolbox.write(toolbox_xml)
file_toolbox.close()
print ("Toolbox created in: " +  path_developer + "/toolbox.js")

import time
time.sleep(2)
