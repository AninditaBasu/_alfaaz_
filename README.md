# \_alfaaz\_

twitter bot for:
- urdu-to-english word meanings
- twitter stories generated from Sahir's verse

[https://twitter.com/_alfaaz_](https://twitter.com/_alfaaz_)

## How it works

One program tweets word translations and another tweets stories.

### For the translations
1. Pull an Urdu word, in Nastalikh script, from a word list.
2. Send the word to Oxford Dictionaries for a translation.
3. Transliterate the word to English.
3. Put the word, its transliteration, and translations on to an image.
4. Tweet the image.
5. Repeat steps 1 through 4 after a delay.

For the code, see u2e_1.py.

### For the stories
1. Create a list of Sahir's film songs.
2. Generate a story by joining 3 random entries.
3. Tweet the story.
4. Repeat steps 2 and 3 after a delay.

For the code, see stories_1.py.

## APIs
For the translations, [Oxford Dictionaries API](https://developer.oxforddictionaries.com/documentation)
For tweeting, [Twitter API](https://dev.twitter.com/rest/public)

## Python libraries
For translations:
- [arabic_reshaper](http://mpcabd.xyz/python-arabic-text-reshaper/)
- [python-bidi](https://pypi.python.org/pypi/python-bidi)
For images: [Pillow](https://pypi.python.org/pypi/Pillow/)
For tweets: [tweepy](http://docs.tweepy.org/en/v3.5.0/index.html)

## Acknowledgements
The code for Urdu to English transliteration is based on [Shan Ali Khan's](https://twitter.com/itsShanKhan) script posted on [Medium](https://medium.com/@itsShanKhan/transliterate-urdu-to-roman-urdu-in-python-614953b1a4d5)

## License
GPL3.0
