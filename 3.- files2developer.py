from shutil import copyfile
import os

path_blockly = os.path.abspath(os.getcwd()) + "/blockly"
print (path_blockly)
path_rize_developer = os.path.abspath(os.getcwd()) + "/developer"
print (path_rize_developer)

def copydata():
    lista = ["blocks_compressed.js","javascript_compressed.js","python_compressed.js"]

    for l in lista:
        src = path_blockly + "/" + l
        dst = path_rize_developer + "/blockly_dynamic/" + l
        
        copyfile(src, dst)


copydata()
