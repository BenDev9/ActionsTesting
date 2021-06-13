import os

cwd = os.getcwd()

print(cwd)

objects = os.listdir(cwd)

for o in objects:
  if o == "extensionCollecter.py":
    print("that's me")
    print(o)
  elif os.path.isdir(cwd+o):
    print("that's a dir")
    print(o)
  else:
    print("that's a file")
    print(o)
