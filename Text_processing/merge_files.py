from pathlib import  Path

files_dir = Path("files")

merge_content = ''
for index, filepath in enumerate(files_dir.iterdir()):
    with open(filepath, 'r') as file:
        content = file.readlines()
        new_content =  content[1:]
    if index == 0:
        content =  "".join(content)
        merge_content= merge_content + content + '\n'
    else:
        new_content = "".join(new_content)
        merge_content = merge_content + new_content + '\n'


with open("merge_files/merg_file.csv", "w" ) as file:
    file.write(merge_content)