import os
import pathlib
import sys

cwd = os.getcwd()

objects = os.listdir(cwd)
dictionary = {}
maintainanceFiles = ["extensionCollecter.py", "filenamDict.txt"]
    
for o in objects:
  if o in maintainanceFiles:
    print(f"{o} is a maintainance file, Skipping!")
    print()
  elif os.paht.isdir(cwd+"/"+o):
    print(f"{o} is a dir, Skipping!")
    print()
  else:
    print(f"{o} is a file")
    filenamewoext = pathlib.Path(o).with_suffix("")
    dictionary.update({str(filenamewoext) : o})
    print(f"Added {o} to the dictionary")

with open("filenameDict.txt", "w") as f:
  f.write(str(dictionary))
