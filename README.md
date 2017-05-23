![version 1.0](https://img.shields.io/badge/version-1.0-green.svg)  ![python 3.6.0](https://img.shields.io/badge/python-3.6.0-blue.svg)  ![license: GPL 3.0](https://img.shields.io/badge/license-GPL%203.0-lightgrey.svg)  

# _alfaaz_

Twitter bots for:

- Urdu-to-English word translations. See `words_u2e`.
- Twitter stories. See `stories.py`.

Live at [https://twitter.com/_alfaaz_](https://twitter.com/_alfaaz_)

<hr/>

  [APIs](#apis)
  
  [Python libraries](#python-libraries)
  
  [Bugs, enhancements](#bugs-enhancements)
  
  [Acknowledgements](#acknowledgements)
  
  [License](#license)

<hr/>

## APIs

- For the translations, [Oxford Dictionaries API](https://developer.oxforddictionaries.com/documentation)
- For tweeting, [Twitter API](https://dev.twitter.com/rest/public)

<hr/>

## Python libraries

- For translations:
  - [arabic_reshaper](http://mpcabd.xyz/python-arabic-text-reshaper/)
  - [python-bidi](https://pypi.python.org/pypi/python-bidi)
- For images: [Pillow](https://pypi.python.org/pypi/Pillow/)
- For tweets: [tweepy](http://docs.tweepy.org/en/v3.5.0/index.html)
- Other libraries: `requests`, `json`, `time`, `urllib`, `csv`, `random`

<hr/>

## Bugs, enhancements

See the [Issues](https://github.com/AninditaBasu/_alfaaz_/issues) page.

<hr/>

## Acknowledgements

-  The code for Nastalikh to Devanagari phonetic transliteration is based on [Shan Ali Khan's](https://twitter.com/itsShanKhan) script posted on [Medium](https://medium.com/@itsShanKhan/transliterate-urdu-to-roman-urdu-in-python-614953b1a4d5).
-  Word meanings are, in the first instance, from Oxford Dictionaries. If no meaning is found, the fallback dictionaries are the Urdu dictionaries hosted at the [Digital South Asia Library](http://dsal.uchicago.edu/dictionaries/) by the University of Chicago.
- For the stories, songs are from Mirza Ghalib's verses (out of copyright) and from Hindi films (used here under Fair Use policy).

<hr/>

## License

GPL3.0
