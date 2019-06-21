# -*- coding: utf-8 -*-
import praw
import config

reddit = praw.Reddit(client_id=config.client_id,
                     client_secret=config.client_secret,
                     user_agent=config.user_agent,
                     username=config.user,
                     password=config.userpass)

subreddit = reddit.subreddit(config.subreddit)

print(subreddit.display_name)
print(subreddit.title)
print(subreddit.description)

subreddit.submit_image(config.title, config.path, send_replies=False)

print("Posted picture successfully!")
