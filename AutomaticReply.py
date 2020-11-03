# -*- coding:utf-8 -*-
#
# automatic reply
#
import tweepy
import twitter_api
import random

#認証情報
consumer_key = twitter_api.consumer_key
consumer_secret = twitter_api.consumer_secret
access_token = twitter_api.access_token
access_token_secret =twitter_api.access_token_secret

#API認証
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

def mentionTimeLine():#使ってない
    all_tweets = []
    latest_tweets = api.user_timeline(count=30)
    all_tweets.extend(latest_tweets)
    mention_account = []
    for tweet in all_tweets:  
        if tweet.text.startswith('@'):
            text = tweet.text.split()
            mention_account.append(text[0].replace('@', ''))
    return mention_account

def mentionStatus(tweet_id):
    all_tweets = []
    latest_tweets = api.user_timeline(count=30)
    all_tweets.extend(latest_tweets)
    mention_status = []
    for tweet in all_tweets:  
        if tweet.text.startswith('@'):
            replied_id = tweet.in_reply_to_status_id
            qkou_status = api.get_status(replied_id)
            if str(qkou_status.in_reply_to_status_id) == tweet_id: #既にリプライしたリプの元ツイがtweet_idと一致するか
                #print("True, already replied"+qkou_status.text)
                mention_status.append(qkou_status) #既にリプ済みのツイートステータスのリスト
    return mention_status

def get_mentions(tweet_id):
    mentions = api.mentions_timeline(count=50)
    return mentions

def get_reply_status(tweet_id):
    mentions = get_mentions(tweet_id)
    reply_status = []
    for mention in mentions:
        if str(mention.in_reply_to_status_id) == tweet_id and not "RT @" in mention.text:
            reply_status.append(mention)
    return reply_status

def hasNotReply(status):
    mentionS = mentionStatus(tweet_id) #既にリプ済みのツイートステータスのリスト
    if status in mentionS:
        return False
    else:
        return True

def textGenerate():
    text = ["!", "(*'ω'*)", "!", "!","くコ:彡","( *´艸｀)","!"]
    s = ["ありがとうございます"]
    for i in range(3):
        r = random.randrange(1, len(text))
        s.append(text[r])
    s = random.sample(s, len(s))
    result = ''.join(s)
    return result

def getFollow():
    friends_ids = []
    for friend_id in tweepy.Cursor(api.friends_ids, user_id='your own user id').items():
        u = api.get_user(friend_id)
        friends_ids.append(u.screen_name)
    return friends_ids

def isFollow(status, friends_ids):
    #print(status.user.screen_name)
    if status.user.screen_name in friends_ids:
        return True
    else:
        return False

def ExisFollow(s):###
    friends_ids = []
    for friend_id in tweepy.Cursor(api.friends_ids, user_id='chiisann_').items():
        friends_ids.append(friend_id)
    print(friends_ids)
    if s in friends_ids:
        return True
    else:
        return False
    print(s in friends_ids)

def reply(tweet_id):
    follow_list = getFollow() #getFollow()は時間がかかるので一度取得してリストとして置いておくことを推奨する
    follow = []
    reply_status = get_reply_status(tweet_id)
    for tweet in reply_status:
        #print(tweet.user.name)
        #print(isFollow(tweet, follow_list))
        if hasNotReply(tweet):
            if isFollow(tweet, follow_list): 
                follow.append(tweet)
                #print("Follow but not reply yet: "+tweet.user.name)
            else: #フォローしていない人に対して自動リプ
                #print(tweet.text)
                reply_text = "@"+str(tweet.user.screen_name) + " " + textGenerate()  #文字列指定
                #api.update_status(reply_text, tweet.id) #ここでリプライする
                print(reply_text)
    print("==================================")
    print("Follow but not reply yet")
    for tweet in follow:
        print(tweet.user.name+"@"+tweet.user.screen_name+"\n"+tweet.text)
    print("==================================")
            
if __name__ == '__main__':
    user_id = 'your own user id'
    tweet_id = input('tweet id:')

    """
    ExisFollow(s):###
    friends_ids = []
    for friend_id in tweepy.Cursor(api.friends_ids, user_id='your own user id').items():
        friends_ids.append(friend_id)
    print(friends_ids)
    """

    reply(tweet_id)
    #textGenerate()
