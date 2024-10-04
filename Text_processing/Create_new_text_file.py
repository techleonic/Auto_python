
content = """this 
    is
     a
      multyline
       text
       """
with open("file1.txt", "w") as file:
    file.write("first text\n")
    file.write("second text")

    file.write(content)