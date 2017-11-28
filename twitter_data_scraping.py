# first install library
#pip install python-twitter
#1 sign up for twitter
#2 Go to https://apps.twitter.com/
#3 Create an App
#4 Should be able toi use http://www.marymount.edu for webpage if you do not have one
#5 once created go to Keys and Access tokens
#6 Generate Access Token
#7 use this data for the fields below
#get credentials
import re
import datetime
import sys
import twitter
import operator
import json
from collections import Counter
#fill these in
api = twitter.Api(consumer_key='6yGDOr1dttlTzg47XDepWy7Xb',
                      consumer_secret='7df6l1a5GhlgvMphYgX9VA8rWz3UT0JXIQRwlROavg7STNjIMd',
                      access_token_key='2886448486-8E8v3PiAPl9ASKU7N7C13CZaZbg0RnyNA4kNScL',
                      access_token_secret='W6Qg4FnKiIv6lyePrV7qNO497EEs1vYGxOBwrvWMbA62S',
                  tweet_mode='extended')





def get_tweets(handle,since_id=0,max_id=0,count=200):
    if max_id == 0:
        statuses = api.GetUserTimeline(screen_name=handle, count=count, exclude_replies=True, include_rts=False,since_id=since_id)
    else:
        statuses = api.GetUserTimeline(screen_name=handle, count=count, exclude_replies=True, include_rts=False,max_id=max_id)
    return statuses


statuses=get_tweets(handle='SelenaGomez')
list=[]
for s in statuses:
    #print(s.full_text)
    hashtags=s.hashtags
    count_all = Counter()
    for tag in hashtags:
        #print(tag.text)
        list.append(tag.text)
    #print(s)
#Q1
listdic={}
tags=[]
for tag in list:
    #print(tag)
    listdic[tag] = listdic.setdefault(tag, 0) + 1
listdic=(sorted(listdic.items(), key=lambda x: x[1], reverse=True))
#print(listdic)
for keys, values in listdic:
    tags.append(keys)
print("The most common hasgtag is: #" + str(tags[0]))

#Q2
lines=[]
for s in statuses:
    lines.append(s.full_text)
#print(lines)
wordslist=[]
for line in lines:
    words = len(line.strip(' '))
    wordslist.append(words)
    #print(words)
total=sum(wordslist)
average=total/len(wordslist)
print("The average number of words per tweet is " + str(average))

#Q3
count = 0
linksptweet=[]
for line in lines:
    links=re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', line)
    for link in links:
        numberlinks=len(links)
        linksptweet.append(numberlinks)
#print(linksptweet)
n=len(linksptweet)
for i in linksptweet:
    if i==2:
        count+=1
avg=count/n
print("The number of links on average is " + str(avg))

#Q4
dates_all=[]
freq={}
for s in statuses:
    #print(s.created_at)
    dates_all.append(s.created_at)
dates_only = [x[0:10] for x in dates_all]
#print(dates_only)
tweets_num=len(dates_only)
for i in dates_only:
    freq[i.lower().strip()] = freq.setdefault(i.lower().strip(), 0) + 1
freq=(sorted(freq.items(), key=lambda x: x[1], reverse=True))
#print(freq)
days=len(freq)
#print(days)
average_tweets=tweets_num/days
print("The average number of tweets per day is " + str(average_tweets))

