from pathlib import Path

p1 =  Path("files/abc.txt")
print(type(p1))

# if file exist
if p1.exists():
    with open(p1, "r") as file:
        print(file.read())

p2 = Path("files/def.txt")

# if it does not exist create it
if not p2.exists():
    with open(p2, "w") as file:
        file.write("d,e,f")
else:
    with open(p2,"r") as file:
        print(file.read())

# get the name of the file
print(p1.name)
# name without the extension
print(p1.stem)

print(p2.name)
print(p2.stem)
# the Extension
print(p2.suffix)

p3 = Path("files")

print(list(p3.iterdir()))