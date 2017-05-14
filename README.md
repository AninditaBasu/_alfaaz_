![version 1.0](https://img.shields.io/badge/version-1.0-green.svg)  ![python 3.6.0](https://img.shields.io/badge/python-3.6.0-blue.svg)  ![license: GPL 3.0](https://img.shields.io/badge/license-GPL%203.0-lightgrey.svg)  

# \_alfaaz\_

twitter bot for:

- urdu-to-english word translations
- twitter stories generated from Hindi film songs

Live at [https://twitter.com/_alfaaz_](https://twitter.com/_alfaaz_)

## How it works

One script tweets the translations and another tweets the stories.

### For the translations

1. Pull an Urdu word, in Nastalikh script, from a word list.
2. Send the word to Oxford Dictionaries for a translation.
3. Transliterate the word to English.
4. Put the word, its transliteration, and translations on to an image.
5. Tweet the image.
6. Send the word to Platt's dictionary for a word search.
7. Tweet the URL.
8. Repeat steps 1 through 7 after a delay.

For the code, see `words_u2e`.

### For the stories

1. Create lists of story fragments from Hindi film songs.
2. Generate a story by joining 2 random entries from the lists.
3. Tweet the story.
4. Repeat steps 2 and 3 after a delay.

For the code, see `stories.py`.

## APIs

- For the translations, [Oxford Dictionaries API](https://developer.oxforddictionaries.com/documentation)
- For tweeting, [Twitter API](https://dev.twitter.com/rest/public)

## Python libraries

- For translations:
  - [arabic_reshaper](http://mpcabd.xyz/python-arabic-text-reshaper/)
  - [python-bidi](https://pypi.python.org/pypi/python-bidi)
- For images: [Pillow](https://pypi.python.org/pypi/Pillow/)
- For tweets: [tweepy](http://docs.tweepy.org/en/v3.5.0/index.html)
- Other libraries: `requests`, `json`, `time`, `urllib` 

## Acknowledgements

The code for nastalikh to devanagari phonetic transliteration is based on [Shan Ali Khan's](https://twitter.com/itsShanKhan) script posted on [Medium](https://medium.com/@itsShanKhan/transliterate-urdu-to-roman-urdu-in-python-614953b1a4d5).

## License

GPL3.0
