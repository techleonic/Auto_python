import os

import praw



reddit = praw.Reddit(user_agent=True, client_id=os.getenv("CLIENT_ID"),
                     client_secret=os.getenv("CLIENT_SECRET"), username=os.getenv("USERNAME"), password=os.getenv("PASSWORD"))


url = "https://www.reddit.com/r/technology/comments/1ghdwvg/if_trump_gets_elected_get_your_tech_buying_done/"

post = reddit.submission(url=url)

# get title text
print(post.title)

#get post text
print(post.selftext)

for comment in post.comments.list()[:10]:
    print(comment.body)
