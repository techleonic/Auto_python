from pathlib import Path
from datetime import datetime

path = Path("files/December/a.txt")
stats = path.stat()
second_created = stats.st_ctime
date_created = datetime.fromtimestamp(second_created)
date_created_str =  date_created.strftime("%Y-%m-%d")
print(date_created)