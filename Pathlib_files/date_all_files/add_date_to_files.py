from pathlib import Path
from datetime import datetime

path = Path("files/December/a.txt")
stats = path.stat()
second_created = stats.st_ctime
date_created = datetime.fromtimestamp(second_created)
date_created_str =  date_created.strftime("%Y-%m-%d_%H_%M_%S")

root_file = Path("files")
for path in root_file.glob("**/*"):
    if path.is_file():
        print(path)
        print(path.name)
        file_newname =date_created_str+"_"+path.name

        new_filepath =  path.with_name(file_newname)
        print(new_filepath)
        path.rename(new_filepath)