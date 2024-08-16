import pandas
import yagmail
import os
sender = os.getenv("SENDER_EMAIL")

subject = "using yagmail to send mail"


df = pandas.read_csv("emails.csv")
print(df)
yag = yagmail.SMTP(user=sender, password=os.getenv("SENDER_PASSWORD"))
for index , row in df.iterrows():
    content = f"""
    hello {row["name"]}
    this is a email test from yagmail lib
    """
    yag.send(to=row["email"], subject=subject, contents=content)