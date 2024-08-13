from pathlib import Path
#create the files
# for num in range(10,21):
#     with open(f"files/{num}.txt", "w") as file:
#         file.write("")

root_path = Path("files")

for path in root_path.rglob("*.txt"):
    if path.is_file():
        new_filepath = path.with_suffix(".csv")
        path.rename(new_filepath)
