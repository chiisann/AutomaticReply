AutomaticReply
==================
You can automatically reply to many replies at once by specifing tweet id.
This program is effective for person who have many followers on Twitter.

## Description
### Authentication
line 9 ~ line 18 : to authenticate TwitterAPI

### mentionStatus(tweet_id)
To check whether each mentioned tweet id in latest 30 ones is same as the original tweet id which you have many replies.

### hasNotReply(status)
To check if each tweet from othes has NOT reply from me.

### textGenerate()
To generate randomized reply text.

### getFollow()
To get my own follow list.

### isFollow(status, friends_ids)
Get the original person from tweet status and check if this tweet is from my follow list.

### reply(tweet_id)
Get my follow list, and automatiacally reply generated text if reply is not from follow list.
Display tweets from people who followed by me but not replied yet.


## Usage
If you write down your own Twitter API key on the 'x' below in *twitter_api.py* and run *AutomaticReply.py*, you can input tweet id that you have many replies to reply.
```python
#Twitter API key
consumer_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxx'
consumer_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
access_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
access_token_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
```

In default, this program automatically generates reply text at `textGenerate()` (line 64), but ofcource you can specify reply text. (By changing `textGenerate()` at line 113)

## Note
You can see the example that is my Tweet's analyzed data with table and graph in **result.csv** file opened by Excel.
