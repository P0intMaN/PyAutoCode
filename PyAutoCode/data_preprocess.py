# An attempt to create a tokenizer-cum-pretrainer from scratch
import os, time
from sty import fg, rs

# globals
MAX_CHAR_LENGTH = 512
MIN_CHAR_LENGTH = 400

# decoy newline char to encode newlines in python
NEWLINECHAR = "<N>"

walk_dir = './resources/repos'
full_paths = []
for dirpath, dirnames, filenames in os.walk(walk_dir):
    for f in filenames:
        full_path = os.path.join(dirpath, f)
        full_paths.append(full_path)

print(len(full_paths))

for fpath in full_paths:
    data = open(fpath, "r", encoding="utf-8").read()
    if len(data) > 60 and len(data) <= MAX_CHAR_LENGTH:
        print(f"{data}: len {len(data)}")
        formatted_data = data.replace("\n", NEWLINECHAR)
        print(f"{formatted_data}: len {len(formatted_data)}")
        break
