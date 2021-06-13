import os
import pathlib

cwd = os.getcwd()
print(f"Current working directory is: {cwd}")

objects = os.listdir(cwd)
dictionary = {}
maintainanceFiles = ["extensionCollecter.py", "filenamDict.txt"]

for o in objects:
  print(cwd+"/"+o)
  if o in maintainanceFiles:
    print(f"{o} is a maintainence file, skipping!")
  elif os.path.isdir(cwd+"/"+o):
    print(f"{o} is a directory, skipping!")
  else:
    filenamewoext = pathlib.Path(o).with_suffix("")
    dictionary.update({str(filenamewoext) : filename})
    print(f"Added {o} to the dict!")
  print()

print(dictionary)

with open("filenameDict.txt", "w") as f:
  f.write(str(dictionary))
  
print()
print("Wrote dict to file")
