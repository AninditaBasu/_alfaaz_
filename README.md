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
3. Put the word, its transliteration, and translations on to an image.
4. Tweet the image.
5. Send the word to Platt's dictionary for a word search.
6. Tweet the URL.
7. Repeat steps 1 through 6 after a delay.

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
-- [arabic_reshaper](http://mpcabd.xyz/python-arabic-text-reshaper/)
-- [python-bidi](https://pypi.python.org/pypi/python-bidi)
- For images: [Pillow](https://pypi.python.org/pypi/Pillow/)
- For tweets: [tweepy](http://docs.tweepy.org/en/v3.5.0/index.html)
- Other libraries: `requests`, `json`, `time`, `urllib` 

## Acknowledgements

The code for nastalikh to devanagari phonetic transliteration is based on [Shan Ali Khan's](https://twitter.com/itsShanKhan) script posted on [Medium](https://medium.com/@itsShanKhan/transliterate-urdu-to-roman-urdu-in-python-614953b1a4d5)

## License

GPL3.0
