from pathlib import Path

# december_dir = Path("December")
# November_dir = Path("November")
#
# def rename_files(dir):
#     for path in dir.iterdir():
#         new_filename = str(path.parent)+"-" + path.stem + path.suffix
#         # print(path)
#         new_filepath = path.with_name(new_filename)
#         # print(new_filepath)
#         path.rename(new_filepath)
#
# rename_files(december_dir)
# rename_files(November_dir)

# GET ALL FILES AND FOLDER
root_dir =Path("files")
file_paths =  root_dir.glob("**/*")

for path in file_paths:
    print(path)
    if path.is_file():
        print("is a file")
    if path.is_dir():
        print("is a Directory")




