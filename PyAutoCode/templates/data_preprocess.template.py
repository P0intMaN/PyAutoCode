# An attempt to create a tokenizer-cum-pretrainer from scratch
import os, time
from sty import fg, bg, rs

# Walk the repos directory and append all the .py files to a list
walk_dir = './resources/repos'
full_paths = []
for dirpath, dirnames, filenames in os.walk(walk_dir):
    for f in filenames:
        full_path = os.path.join(dirpath, f)
        full_paths.append(full_path)
print(f'{fg.green}Total paths: {len(full_paths)}{fg.rs}\n')

# Pick a file from the list and print its contents (codes)
print(f'{fg.cyan}Original code sample from:{fg.rs}', end='')
for fpath in full_paths:
    data = open(fpath, "r", encoding="utf-8").read()
    print(f'{fg.cyan} {fpath} {fg.rs}')
    print(f"{bg.grey}{fg.black} {data} {fg.rs}{bg.rs}")
    print(f'{fg.cyan}Total char length: {len(data)} {fg.rs}')
    break
