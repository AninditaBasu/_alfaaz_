import requests
import json
import urllib.parse
from PIL import Image, ImageFont, ImageDraw
import arabic_reshaper
from bidi.algorithm import get_display
import tweepy
from time import sleep

# -------- libraries ----------
# requests is for pinging the Oxford Dictionaries API
# json is for parsing the response from Oxford Dictionaries
# urllib.parse is for composing the URL of the Platt's dictionary; a simple
#       concatenation breaks the URL at the query parameter
# PIL is for placing the words on to an image
# arabic_reshaper is for correctly displaying the words in nastalikh
#       and has a dependency on python-bidi, called here as bidi.algorithm
#       arabic_reshaper is from http://mpcabd.xyz/python-arabic-text-reshaper/
# tweepy is for posting updates to Twitter
# sleep is for setting a time lag between tweets
#

# -------- how it works ----------
# 1.  Pull an Urdu word, in Nastalikh script, from a word list.
# 2.  Send the word to Oxford Dictionaries for a translation.
# 3.  Transliterate the word to English.
# 4.  Put the word, its transliteration, and translations on to an image.
# 5.  Tweet the image.
# 6.  Send the word to Platt's dictionary for a word search.
# 7.  Tweet the URL.
# 8.  Repeat steps 1 through 7 after a delay.
#

# ------- word list for the day ---------
word_list = {
'الفاظ':'Ehsaas alfaaz ka mohtaj nahin'
}

# ------------ declare the OxfordDictionary API credentials  -----------
app_id = ''
app_key = ''

# -------------- declare the Twitter credentials -------------
token = ''
token_secret = ''
consumer_key = ''
consumer_secret = ''

# ----------- Platt's dictionary URL ----------
platts_url_base = 'http://dsalsrv02.uchicago.edu/cgi-bin/philologic/search3advanced?dbname=platts&query='
platts_url_suffix = '&matchtype=exact&display=utf8'

# ----------- Oxford Dictionaries URL and other parameters ----------
api_base_url = 'https://od-api.oxforddictionaries.com/api/v1/entries/'
source_language = 'ur'
target_language = 'en'

# ---------- Unicode conversion for Urdu alphabets -------------
# unicode mapping is from http://www.user.uni-hannover.de/nhtcapri/urdu-alphabet.html
# do-chashmi-hey is from https://en.wikipedia.org/wiki/Urdu_alphabet#The_2_he.27s
nast2dev = {
        u"\u0621": "",
        u"\u0654": "",
        u"\u0627": "अ",
        u"\u0622": "आ",
        u"\u0628": "ब",
        u"\u067E": "प",
        u"\u062A": "त",
        u"\u0679": "ट",
        u"\u067F": "ट",
        u"\u062B": "स",
        u"\u062C": "ज",
        u"\u0686": "च",
        u"\u062D": "ह",
        u"\u062E": "ख़",
        u"\u062F": "द",
        u"\u0688": "ड",
        u"\u0690": "ड",
        u"\u0630": "ज़",
        u"\u0631": "र",
        u"\u0691": "ड़",
        u"\u0699": "ड़",
        u"\u0632": "ज़",
        u"\u0698": "झ़",
        u"\u0633": "स",
        u"\u0634": "श",
        u"\u0635": "स",
        u"\u0636": "ज़",
        u"\u0637": "त",
        u"\u0638": "ज़",
        u"\u0639": "अ",
        u"\u063A": "ग़",
        u"\u0641": "फ़",
        u"\u0642": "क़",
        u"\u06A9": "क",
        u"\u06AF": "ग",
        u"\u0644": "ल",
        u"\u0645": "म",
        u"\u0646": "न",
        u"\u06BA": "ँ",
        u"\u0648": "व/ऊ",
        u"\u0624": "ओ",
        u"\u06C1": "ह",
        u"\u0647": "ह",
        u"\u06CC": "य/ई",
        u"\u06D2": "ए",
        u"\u06BE": "ह"
    }

# --------- authenticate with Twitter ---------
try:
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.secure = True
    auth.set_access_token(token, token_secret)
    api = tweepy.API(auth)
except:
    print('Could not authenticate with Twitter')

# ----------- pick a word, generate phonetic devanagari, get translations, put on canvas, tweet -----------
for word_id, song in word_list.items():
    print(word_id)
    print(song)
    # make the pillow canvas ready
    hindiFont = ImageFont.truetype('nakula.ttf', 24)
    arialFont = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 32)
    calibriFont = ImageFont.truetype('C:/Windows/Fonts/calibri.ttf', 24)
    tweetpic = Image.new('RGBA', (640, 360), 'white')
    draw = ImageDraw.Draw(tweetpic, 'RGBA')
    draw.rectangle((2, 2, 638, 358), fill='white', outline='#172A82')
    # reshape the urdu word so that it can be put on the canvas
    urdu_text = arabic_reshaper.reshape(word_id)
    bidi_text = get_display(urdu_text)
    draw.text((20, 20), bidi_text, '#172A82', font=arialFont)
    # transliterate the word to phonetic devanagari
    word_id_ur = word_id
    word_id.encode('utf-8', 'ignore')
    for k, v in nast2dev.items():
        word_id = word_id.replace(k, v + ',')
    word_id = word_id[:-1]
    word_id_hi = word_id.split(",")
    i = 0
    j = len(word_id_ur)
    hi_pos = 110# not used yet
    while i < j:
        print(word_id_hi[i], word_id_ur[i])
        urdu_text = arabic_reshaper.reshape(word_id_ur[i])
        bidi_text = get_display(urdu_text)
        draw.text((hi_pos, 20), bidi_text, '#172A82', font=arialFont)
        temp = ' = ' + word_id_hi[i]
        draw.text((hi_pos + 20, 20), temp, '#172A82', font=hindiFont)
        i = i + 1
        hi_pos = hi_pos + 110
    #draw.text((140, 20), word_transliterate_hi, '#172A82', font=hindiFont)
    draw.line((10, 70, 628, 70), fill='#172A82')
    # get the translations
    pos = 40
    print(word_id_ur)
    try:
        url = api_base_url + source_language + '/' + word_id_ur + '/translations=' + target_language
        r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})
        json_data = json.loads(json.dumps(r.json()))
        target_word_id = json_data['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
        # put each translation on to the Pillow canvas
        for item in target_word_id:
            for item2 in item['translations']:
                trans_word = '- ' + item2['text']
                # only 60 characters fit into one line of the Pillow image
                # if the current font sizes are used. So, trim into two sentences
                # if needed
                if len(trans_word) > 60:
                    text_1 = trans_word[:59]
                    text_2 = "  " + trans_word[60:]
                    print(text_1)
                    print(text_2)
                    pos = pos + 40
                    draw.text((20, pos), text_1, (0, 0, 0, 255), font=calibriFont)
                    pos = pos + 40
                    draw.text((20, pos), text_2, (0, 0, 0, 255), font=calibriFont)
                else:
                    pos = pos + 40
                    print(trans_word)
                    draw.text((20, pos), trans_word, (0, 0, 0, 255), font=calibriFont)
    except:
        draw.text((20, 100), "The Oxford Urdu - English dictionary does not",(0, 0, 0, 255), font=calibriFont)
        draw.text((20, 125), "have a translation for this word yet.",(0, 0, 0, 255), font=calibriFont)
        draw.text((20, 170), "See if the next tweet fares better? It's supposed to",(0, 0, 0, 255), font=calibriFont)
        draw.text((20, 195), "show an entry from John T. Platt's 'Dictionary of Urdu,",(0, 0, 0, 255), font=calibriFont)
        draw.text((20, 220), "Classical Hindi, and English'.",(0, 0, 0, 255), font=calibriFont)
    # save the image to the local drive and tweet the image
    tweetpic.save('tweetpic.png')
    try:
        tweet_text = 'Word: ' + word_id + ' Phonetic: ' + word_transliterate_hi + ' Example: ' + song + '. Word translation from Oxford Dictionaries API.'
        api.update_with_media('tweetpic.png', status=tweet_text)
    except:
        print('Could not post image')
# ----------- pick the Hindi word from the list, get meanings, tweet -----------
    print(hi_word)
    hindi_meanings = []
    try:
        url = api_base_url + hindi_language + '/' + hi_word
        r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})
        json_data = json.loads(json.dumps(r.json()))
        hindi_meanings = json_data['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
        if not hindi_meanings:
            hindi_meanings = json_data['results'][0]['lexicalEntries'][1]['entries'][0]['senses']
        print(hindi_meanings)
        print('length', len(hindi_meanings))
    except:
        print('Could not retrieve Hindi meanings')
    try:
        line1 = 'Hindi meanings of ' + word_id_ur + ' (' + hi_word + ') from OxfordDictionariesAPI: '
        line2 = ''
        a = 0#a counter to check word pos; if not first word, append a comma (for composing tweet text)
        for item in hindi_meanings:
            for item2 in item['definitions']:
                print(item2)
                if a == 0:
                    text = item2
                else:
                    text = ', ' + item2
                line2 = line2 + text
                a = a + 1
        print(line1, line2)
        tweet_text = str.join(' ',(line1, line2))
        sleep(30)  # so that Twitter rate limits are not breached
        api.update_status(status=tweet_text)
    except:
        print('Could not tweet Hindi words.')
    sleep(30)# so that the Twitter rate limits are not breached
    # generate a link to the Platt's dictionary, tweet the link
    platts_url = platts_url_base + urllib.parse.quote((word_id), safe='') + platts_url_suffix
    print(platts_url)
    try:
        text = "Entry for " + word_id + " from John T. Platt's Dictionary of Urdu, Classical Hindi, and English"
        tweet_text = str.join(' ',(text, platts_url))
        api.update_status(status=tweet_text)
    except:
        print("Could not post Platt's link")
    print('------------------------')
    # delay for 1.5 hours till the next round of word lookup and tweeting
    sleep(5400)
