#!/usr/bin/python
import praw
import time

commentsReadLimit = 50
botSleepTime = 10
savedIdsThreshold = 30

def getSubreddits():
    '''
        returns the subreddits to look into
        append your subreddit here to add
    '''
    subreddits = [
        "asoiaf",
        "freefolk",
        "askreddit",
        "popular"]
    return '+'.join(subreddits)


def login():
    '''
        Logs into the reddit using information from praw.ini
        returns the logged in session
    '''
    print("Logging in JonSnowLad_bot")
    reddit = praw.Reddit('bot1')
    print("Logged in JonSnowLad_bot")
    return reddit


def runBot(subreddit, commentsLimit, sleepTime, savedIdsCountLimit):
    '''
        Periodically read comments from a subreddit and reply to ones which
        match the specific pattern

        subreddit: The subreddit to look into - can have multiple subreddits
         combined with '+'
        commentsLimit: the number of comments to read in one round
        sleepTime: time in seconds to sleep between reading, shoould be 2
         seconds at least
        savedIdsCountLimit: number of ids to keep in the saved list to avoid
         multiple replies to same comment
    '''
    # enforce minimum sleep time as mandated by reddit's api calls limit
    if sleepTime < 2:
        sleepTime = 2

    # keep a recent list of ids of comments the bot replied to, so that it
    # doesn't reply to them repeatedly
    repliedCommentIds = []

    while True:
        print("Checking " + str(commentsLimit) + " comments")
        for comment in subreddit.comments(limit = commentsLimit):
            # convert to lowercase for matching
            commentLower = comment.body.lower()
            if "right proper lad" in commentLower:
                if comment.id in repliedCommentIds:
                    continue
                comment.reply("&nbsp; &nbsp; &nbsp; &nbsp; ^^^right ^^^proper")
                repliedCommentIds.append(comment.id)

        print("Round complete, sleeping for " + str(sleepTime) + "s")
        time.sleep(sleepTime)

        # reset the saved ids after a maximum number, as it gets old
        if len(repliedCommentIds) > savedIdsCountLimit:
            repliedCommentIds = []


if __name__ == '__main__':
    reddit = login()
    subreddit = reddit.subreddit(getSubreddits())
    runBot(subreddit, commentsReadLimit, botSleepTime, savedIdsThreshold)
