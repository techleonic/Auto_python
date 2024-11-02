import csv

import praw
import os
from datetime import datetime, timedelta

reddit = praw.Reddit(user_agent=True, client_id=os.getenv("CLIENT_ID"),
                     client_secret=os.getenv("CLIENT_SECRET"), username=os.getenv("USERNAME"), password=os.getenv("PASSWORD"))

subreddit =  reddit.subreddit("business")

post_for_24 = []

for post in subreddit.new(limit=10):
    current_time = datetime.now()
    post_date = datetime.fromtimestamp(post.created)
    deltatime = current_time - post_date

    if deltatime <= timedelta(hours=24):
        post_for_24.append([post.title.encode(encoding="ascii",errors="backslashreplace"), post.selftext.encode(encoding="ascii",errors="backslashreplace"), post_date.strftime("%Y-%m-%d")])

with open("business.csv", "w", newline="") as file:
    writer = csv.writer(file)
    columns = ["Title","Description", "Date"]
    writer.writerow(columns)
    for post in post_for_24:
        writer.writerow([post[0],post[1],post[2]])
        # print(post[0])
        # print(post[1])
        # print(post[2])




