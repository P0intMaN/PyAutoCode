# removing all the non-py files
import os
from sty import fg, bg, ef, rs
from rich.progress import track

py_files = 0
warnings = 0
walk_dir = './resources/repos'

for dirpath, dirnames, filenames in os.walk(walk_dir):
    for f in filenames:
        full_path = os.path.join(dirpath, f)

        if full_path.endswith('.py'):
            print(f"{fg.green} keeping {full_path} {fg.rs}")
            py_files += 1

        else:
            if "repos" in full_path:
                print(f"{fg.red} deleting {full_path} {fg.rs}")
                os.chmod(full_path, 0o777)
                os.remove(full_path)

            else:
                print(f"{fg.yellow} something is not right!! {fg.rs}")
                warnings += 1
# checking if I am on the right track
print(f"Python files: {py_files}")
print(f"Warnings: {warnings}")
