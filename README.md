# JonSnowLad_Bot
Reddit bot that replies to comments with the phrase 'right proper lad' with <sup>'right proper'</sup>.

### Overview
This guide will help you creating a reddit bot using python3 and PRAW.

### Requirements
Requires python3 and PRAW

Create a reddit app with following fields with the account of the bot you want to have:
>https://www.reddit.com/prefs/apps/

name: The name you want to give to your app
type: script
redirct uri: localhost:80/

Other fields are optional.

On creating the app, you will get two strings, an id, and a secret.
![Reddit App dialog screenshot](/assets/reddit_script.png)

Keep the id and secret, it will be used by PRAW to authenticate the bot.

### Installation

 - Install python3

Either download from https://www.python.org/downloads/ or do via your favorite software manager
On ubuntu with apt: `sudo apt-get install python3.6`
On mac with homebrew: `brew install python3`

- Install PRAW

`pip3 install praw`

### Creating the bot

In praw.ini, replace the following fields with your credentials

    [bot1]
    client_id=<id provided by reddit app>
    client_secret=<secret provided by reddit app>
    username=<username of bot>
    password=<password of bot>
    user_agent=<unique user agent for your bot>

Now in `bot.py`, you need to perform 3 steps:

 1. Login to reddit
    `reddit = praw.Reddit('bot1')`
 2. Go to a specific subreddit
     `subreddit = reddit.subreddit("subreddits name joined by +")`
 3. Do the thing your bot is supposed to do
   Make sure to add the main code in an endless loop if you want the code to run continuously.
