import yagmail
import os
import pandas


sender = os.getenv("SENDER_EMAIL")
sender_password = os.getenv("SENDER_PASSWORD")
receiver = os.getenv("RECIVER_EMAIL")

yag = yagmail.SMTP(user=sender,password=sender_password)

df = pandas.read_csv("emails.csv")

def generate_file(name, content):
    with open(name,"w") as file:
        file.write(content)

for index, row in df.iterrows():
    content = f"name: {row["name"]}\nemail: {row["email"]}\nPayment: {row["amount"]}"
    file_name = row["name"] + ".txt"
    generate_file(file_name,content)
    email_content = [f"hello {row["name"]} \nthis is your bill for our service:\n{row["amount"]}$",file_name]
    yag.send(to=row["email"], subject="Service Payment",contents=email_content)



