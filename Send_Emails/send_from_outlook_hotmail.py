import smtplib
import os

sender =  os.getenv("SENDER")
password = os.getenv("PASSWORD")
reciver  = "gekkogtodpnihixwko@poplk.com"
message ="""\
Subject: What's up i am the creepy old dude

hello i am a creepy old dude that uses outlook email
"""
server = smtplib.SMTP("smtp.office365.com",587)
server.starttls()
server.login(sender, password)
server.sendmail(sender,reciver,message)
server.quit()
