AutomaticReply
==================
You can automatically reply to many replies at once by specify tweet id.

## Description
You can reply to specified id tweet.



- *id*
- *created time*
- *text*
- *the number of favorite*
- *the number of retweet*

And you can see the table in the specified file with *.csv*.

## Usage
If you write down your own Twitter API key on the 'x' below in twitter_api.py and run AutomaticReply.py, you can input tweet id that you want to reply.
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
