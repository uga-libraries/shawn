import os
import os.path
import sys
from pathlib import Path

def usage_error():
  print("""Usage: python3 ghost.py source dest
       'source' is the directory you want to make a ghost copy of.
       'dest' is the directory you want to put the ghost copy in. This directory will be created if it does not exist.""")
  exit()

if len(sys.argv) != 3:
  usage_error()

source = sys.argv[1]
dest = sys.argv[2]

if not os.path.exists(source):
  print(f'{source} does not exist')
  usage_error()

if not os.path.exists(dest):
  os.makedirs(dest)

for root, dirs, files in os.walk(source):
  for name in dirs:
    path = os.path.join(root, name).replace(f'{source}/','')
    path = os.path.join(dest,path)
    if not os.path.exists(path):
      os.makedirs(path)
  for name in files:
    part = os.path.join(root, name).replace(f'{source}/','')
    path = os.path.join(dest, part)
    Path(path).touch()
