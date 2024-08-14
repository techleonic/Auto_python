from pathlib import Path

root_dir  =  Path(".")
search_term = "20"

for path in root_dir.rglob("*"):
    if search_term in path.stem:
        print(path.absolute())