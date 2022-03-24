# An attempt to create a tokenizer-cum-pretrainer from scratch
import os
from sty import fg, bg, rs

# globals
MAX_CHAR_LENGTH = 512
MIN_CHAR_LENGTH = 400

# decoy newline char to encode newlines in python
NEWLINECHAR = "<$N$>"

walk_dir = './resources/repos'
full_paths = []
for dirpath, dirnames, filenames in os.walk(walk_dir):
    for f in filenames:
        full_path = os.path.join(dirpath, f)
        full_paths.append(full_path)

# Write the formatted data to a file to create a custom dataset.
exception_hits = 0
with open('python_code_dataset.txt', 'a', encoding='utf-8') as f:
    for fpath in full_paths:
        try:
            data = open(fpath, "r", encoding="utf-8").read()
            formatted_data = data.replace("\n", NEWLINECHAR)

            print(f"{fg.yellow} Data from {fpath} {fg.rs}")
            if len(data) > 100 and len(data) <= MAX_CHAR_LENGTH:
                f.write(formatted_data+'\n')
                

            else:
                split_data = formatted_data.split(f'{NEWLINECHAR}{NEWLINECHAR}')
                buffer = ""
        
                print(f"{fg.yellow} Data from {fpath} {fg.rs}")
                for _ in split_data:
                    buffer = _+f'{NEWLINECHAR}{NEWLINECHAR}'
                    
                    if len(buffer) >= MIN_CHAR_LENGTH and len(buffer) <= MAX_CHAR_LENGTH:
                        f.write(buffer+'\n')
                        buffer = ""
        
        except (UnicodeDecodeError, UnicodeError):
            exception_hits+=1
