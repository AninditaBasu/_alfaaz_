![python 3.6.0](https://img.shields.io/badge/python-3.6.0-blue.svg)  ![license: GPL 3.0](https://img.shields.io/badge/license-GPL%203.0-lightgrey.svg)  

# \_alfaaz\_

Twitter bots for:

- Urdu-to-English word translations. See `words_u2e.py`.
- Urdu-Hindi homophones. See `homophones.py`.
- Twitter stories. See `stories.py`.

Live at [https://twitter.com/\_alfaaz\_](https://twitter.com/_alfaaz_)

Explanations on dev.to:
-  [How bots tweet Urdu word meanings in English](https://dev.to/aninditabasu/how-bots-tweet-urdu-word-meanings-in-english)
-  How bots write stories (ToBeDone)

This README file contains the following sections:

 -  [API credentials](#api-credentials)
 -  [Python libraries](#python-libraries)
 -  [Bugs, enhancements](#bugs-enhancements)
 -  [Acknowledgements](#acknowledgements)
 -  [License](#license)

<hr/>

## API credentials

- For the translations, [Oxford Dictionaries API](https://developer.oxforddictionaries.com/documentation)
- For tweeting, [Twitter API](https://dev.twitter.com/rest/public)

## Python libraries

- For images:
  -  [Pillow](https://pypi.python.org/pypi/Pillow/)
  -  [arabic_reshaper](http://mpcabd.xyz/python-arabic-text-reshaper/)
  -  [python-bidi](https://pypi.python.org/pypi/python-bidi)
- For tweets: [tweepy](http://docs.tweepy.org/en/v3.5.0/index.html)
- Other libraries: `requests`, `json`, `time`, `urllib`, `csv`, `random`

## Bugs, enhancements

See the [Issues](https://github.com/AninditaBasu/_alfaaz_/issues) page.

## Acknowledgements

-  The code for Nastalikh to Devanagari phonetic transliteration is based on [Shan Ali Khan's](https://twitter.com/itsShanKhan) script posted on [Medium](https://medium.com/@itsShanKhan/transliterate-urdu-to-roman-urdu-in-python-614953b1a4d5).
-  Word meanings are, in the first instance, from Oxford Dictionaries. If no meaning is found, the fallback dictionaries are the Urdu dictionaries hosted at the [Digital South Asia Library](http://dsal.uchicago.edu/dictionaries/) by the University of Chicago.
- For the stories, songs are from Mirza Ghalib's verses (out of copyright) and from Hindi films (used here under Fair Use Policy).

## License

GPL3.0
