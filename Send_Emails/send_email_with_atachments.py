import yagmail
import os
sender = os.getenv("SENDER_EMAIL")
receiver = os.environ.get("RECIVER_EMAIL")

subject = "using yagmail to send mail"

content = [""" 
this is better than smt library?
""","emails.csv"]

yag = yagmail.SMTP(user=sender, password=os.getenv("SENDER_PASSWORD"))
yag.send(to=receiver, subject=subject, contents=content)