import os
import pathlib
import sys

cwd = os.getcwd()

objects = os.listdir(cwd)
dictionary = {}
maintainanceFiles = ["extensionCollecter.py", "filenamDict.txt"]

for o in objects:
  if not o in maintainanceFiles and not os.path.isdir(cwd+"/"+o):
    filenamewoext = pathlib.Path(o).with_suffix("")
    dictionary.update({str(filenamewoext) : o})

#with open("filenameDict.txt", "w") as f:
#  f.write(str(dictionary))

sys.stderr.write(str(dictionary))
