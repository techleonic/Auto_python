import praw
import os
from datetime import datetime, timedelta
reddit = praw.Reddit(user_agent=True, client_id=os.getenv("CLIENT_ID"),
                     client_secret=os.getenv("CLIENT_SECRET"), username=os.getenv("USERNAME"), password=os.getenv("PASSWORD"))

subreddit = reddit.subreddit("glassblowing")

for post in subreddit.hot(limit=25):
    current_time = datetime.now()
    post_date = datetime.fromtimestamp(post.created)
    deltatime = current_time - post_date

    print(post.title)
    if "whiskey" in post.title.lower():
        post.reply("That's beautiful")
        for comment in post.comments:
            if "beautiful" in comment.body.lower():
                comment.reply("yes it is")