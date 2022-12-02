import os
from os import path

# key = Name
# value = Copy Location
filemap = {
  ".prettierrc": "~/",
  ".rustfmt.toml": "~/",
}

thisFilePath = path.dirname(path.realpath(__file__))

def appendTrailingSlash(path):
  if path[-1] != "/":
    return path + "/"
  return path

def install():
  os.system("git pull") # Pull latest dotfiles if needed
  numberFailed = 0
  for filename, copyLocation in filemap.items():
    copyLocation = appendTrailingSlash(os.path.expanduser(copyLocation))
    result = os.system("cp " + thisFilePath + "/dotfiles/" + filename + " " + copyLocation)
    if (result != 0):
      numberFailed += 1
      print("Failed to copy " + filename + " to " + copyLocation)
    else:
      print("Copied " + filename + " to " + copyLocation)

install()