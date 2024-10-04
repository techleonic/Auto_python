
with open('merge_files/merg_file.csv', "r") as file:
    content =  file.readlines()

content[0]= 'ID,AMOUNT,COST\n'

with open('merge_files/merg_file_new_title.csv', 'w') as file:
    file.writelines(content)