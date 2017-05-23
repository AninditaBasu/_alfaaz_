![version 1.0](https://img.shields.io/badge/version-1.0-green.svg)  ![python 3.6.0](https://img.shields.io/badge/python-3.6.0-blue.svg)  ![license: GPL 3.0](https://img.shields.io/badge/license-GPL%203.0-lightgrey.svg)  

# _alfaaz_

twitter bots for:

- Urdu-to-English word translations. See `words_u2e`.
- twitter stories, happily quoting Hindi film songs. See `stories.py`.

Live at [https://twitter.com/_alfaaz_](https://twitter.com/_alfaaz_)

  [APIs](#apis)
  
  [Python libraries](#python-libraries)
  
  [ToDo for urdu2english word meanings](#todo-for-urdu-to-english-word-meanings)
  
  [ToDo for bot stories](#todo-for-bot-stories)
  
  [Acknowledgements](#acknowledgements)
  
  [License](#license)

<hr/>

## APIs

- For the translations, [Oxford Dictionaries API](https://developer.oxforddictionaries.com/documentation)
- For tweeting, [Twitter API](https://dev.twitter.com/rest/public)

[Top](#alfaaz)
<hr/>

## Python libraries

- For translations:
  - [arabic_reshaper](http://mpcabd.xyz/python-arabic-text-reshaper/)
  - [python-bidi](https://pypi.python.org/pypi/python-bidi)
- For images: [Pillow](https://pypi.python.org/pypi/Pillow/)
- For tweets: [tweepy](http://docs.tweepy.org/en/v3.5.0/index.html)
- Other libraries: `requests`, `json`, `time`, `urllib` 

[Top](#alfaaz)
<hr/>

## ToDo for urdu to english word meanings

### Easy

- [ ] If a meaning has more than 60 characters, put a line break in image.
- [ ] If a word has more than 5 lines of meanings, carry over the meanings to a new image.
- [ ] Only if OxfordAPI returns a Nil result, tweet a Platts link, with exact word match.
- [ ] Only if both OxfordAPI and Platts return a Nil result, tweet a Shakespear link with exact word match.
- [ ] If all three return Nil results, tweet a Sorry message.

### Moderately difficult

- [ ] Break up the Urdu word into letters, tweet the nastaliq > devanagari mapping.

### Very difficult

- [ ] Automatically generate the correctly spelt devanagari word from the nastaliq word.

[Top](#alfaaz)
<hr/>

## ToDo for bot stories

- [ ] More fragments, more combos, more fun
- [ ] Pick a combo randomly

[Top](#alfaaz)
<hr/>

## Acknowledgements

The code for nastalikh to devanagari phonetic transliteration is based on [Shan Ali Khan's](https://twitter.com/itsShanKhan) script posted on [Medium](https://medium.com/@itsShanKhan/transliterate-urdu-to-roman-urdu-in-python-614953b1a4d5).

[Top](#alfaaz)
<hr/>

## License

GPL3.0
