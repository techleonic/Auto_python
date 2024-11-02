import praw
import os
reddit = praw.Reddit(user_agent=True, client_id=os.getenv("CLIENT_ID"),
                     client_secret=os.getenv("CLIENT_SECRET"), username=os.getenv("USERNAME"), password=os.getenv("PASSWORD"))

subreddit = reddit.subreddit("pythonsandlot")
subreddit.validate_on_submit = True
title = 'this is my title'
content = 'this is the content'

subreddit.submit(title=title, selftext=content)
