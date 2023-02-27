import os
from os import path
from sys import argv

# key = Name
# value = Copy Location
filemap = {
  ".prettierrc": "~/",
  ".rustfmt.toml": "~/",
  "starship.toml": "~/.config/",
  ".vimrc": "~/",
}

# Commands
installCommands = ["install", "i"]
pullCommands = ["pull", "p", "copy"]

thisFilePath = path.dirname(path.realpath(__file__))

def appendTrailingSlash(path):
  if path[-1] != "/":
    return path + "/"
  return path

def install():
  numberFailed = 0
  for filename, copyLocation in filemap.items():
    copyLocation = appendTrailingSlash(os.path.expanduser(copyLocation))
    result = os.system("cp " + thisFilePath + "/dotfiles/" + filename + " " + copyLocation)
    if (result != 0):
      numberFailed += 1
      print("Failed to copy " + filename + " to " + copyLocation)
    else:
      print("Copied " + filename + " to " + copyLocation)
  if numberFailed > 0:
    print(f"Failed to copy {numberFailed} files")
    exit(1)
  
def pullFromSystem():
  # copy all files in filemap to dotfiles directory
  numFailed = 0
  for filename, copyLocation in filemap.items():
    copyLocation = appendTrailingSlash(os.path.expanduser(copyLocation))
    result = os.system("cp " + copyLocation + filename + " " + thisFilePath + "/dotfiles/")
    if (result != 0):
      numFailed += 1
      print("Failed to copy " + filename + " to " + copyLocation)
    else:
      print("Copied " + filename + " to " + copyLocation)
  if numFailed > 0:
    print(f"Failed to copy {numFailed} files")
    exit(1)
  
def main():

  # If no args, just run `install()`
  if (len(argv) <= 1):
    install();
    return;

  cmd = argv[1].lower()

  if cmd in installCommands:
    install()
  elif cmd in pullCommands:
    pullFromSystem()
  else:
    print(f"Invalid command {cmd}")
    exit(1)
  

main()