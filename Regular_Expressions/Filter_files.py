import re
from pathlib import Path

root_dir =  Path("files")
filenames =  root_dir.iterdir()
filenames_str =  [file.name for file in filenames]
print(filenames_str)

pattern = re.compile("nov[a-z]*-(?:[1-9]|[1[0-9]|2[0-9])", re.IGNORECASE)

matches = [filename for filename in filenames_str if pattern.findall(filename)]
print(matches)