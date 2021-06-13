import os

cwd = os.getcwd()

print(cwd)

objects = os.listdir(cwd)

for o in objects:
  if o == "extensionCollecter.py":
    print(o)
    print("that's me")
  elif os.path.isdir(cwd+o):
    print(o)
    print("that's a dir")
  else:
    print(o)
    print("that's a file")
