import csv
import random
import tweepy
from time import sleep

# -------- libraries ----------
# csv is for opening and reading a CSV file
# random is for generating a random key, to use for picking random item from list
# tweepy is for posting updates to Twitter
# sleep is for setting a time lag between tweets
#

# -------- put the data of the CSV file into lists --------
temp = []
with open('fragments.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        temp.append(row)
list1 = []
list2 = []
list3 = []
list4 = []
for item in temp:
    list1.append(item[0])
    list2.append(item[1])
    list3.append(item[2])
    list4.append(item[3])
questions = [x for x in list1 if x]
facts = [x for x in list2 if x]
problems = [x for x in list3 if x]
suggestions = [x for x in list4 if x]

# -------------- declare the Twitter credentials -------------
token = ''
token_secret = ''
consumer_key = ''
consumer_secret = ''

# --------- authenticate with Twitter ---------
try:
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.secure = True
    auth.set_access_token(token, token_secret)
    api = tweepy.API(auth)
except:
    print('Could not authenticate with Twitter')

# -------- make a story, tweet every 90 minutes 3 times --------
i = 0
while i < 3:
    if i % 2 == 0:
        tweet_text = 'Usne poochha, ' + random.choice(questions) + " Maine bola, " + random.choice(facts) + " #TS #BotStory"
    else:
        tweet_text = 'Maine kaha, ' + random.choice(problems) + " Jawab mila, " + random.choice(suggestions) + " #TS #BotStory"
    print(tweet_text)
    try:
        api.update_status(status=tweet_text)
        print('Tweet posted.')
    except:
        print('Could not tweet.')
    i = i + 1
    if i == 2:
        break
    else:
        sleep(5400)