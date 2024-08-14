from pathlib import Path
import zipfile
# same directory as the script
root_dir = Path(".")
destination_path =  Path("unzip_files")

for path in root_dir.glob("*.zip"):
    with zipfile.ZipFile(path,"r") as zf:
        final_path = destination_path / Path(path.stem)
        print(final_path)
        zf.extractall(path=final_path)

