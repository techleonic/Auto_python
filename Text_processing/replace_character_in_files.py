from pathlib import Path

files_dir = Path("files")

for filepath in files_dir.iterdir():
    with open(filepath, "r") as file:
        content =  file.read()
        mod_content = content.replace('amount', 'units')

    with open(f"files/new_{filepath.name}", "w") as file:
        file.write(mod_content)