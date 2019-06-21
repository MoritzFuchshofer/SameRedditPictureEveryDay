# SameRedditPicEveryDay
A simple python script that posts a picture to a subreddit.

I've created it as my first project to practice Git and check if my vServer is set up correctly. I have never automated a script using cronjobs before this project and it seemed like a fun way to get started. 

## Dependency

Praw (Reddit Wrapper) 

```bash
pip install praw
```
## Configure config.py

```python
#14 Letter Client ID From your created application at https://www.reddit.com/prefs/apps
client_id = ""
#30 Letter Client Secret from your created application at https://www.reddit.com/prefs/apps
client_secret = ""
#String of Text that is used to identify the porgram making the requests
#e.g. android:com.example.myredditapp:v1.2.3 (by /u/kemitche)
#It has to follow this format, and it has to be unique! If you copy other user agents, you will get banned!
user_agent = ""
#The Username under that the application was created -> You will post from this account!
user = ""
#Password for the username
userpass = ""
#The name of the subreddit you want to post to
subreddit = ""
#title of the post
title = ""
#path to the picture on your system
path = ""
```

## Automation
To automate this script, simply move it to a server and create a cronjob. 
e.g.
```cron
 30 16 * * * /usr/bin/python3.6 /root/python/SamePicEveryDay/poster.py
```
