# ROT 13

## Description
How can you tell an extrovert from an introvert at NSA? Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it? According to Wikipedia,
ROT13 (http://en.wikipedia.org/wiki/ROT13) is frequently used to obfuscate jokes on USENET.

Hint: For this task you're only supposed to substitue characters. Not spaces, punctuation, numbers etc.

## Test examples:
```python
rot13("EBG13 rknzcyr.") == "ROT13 example."
rot13("This is my first ROT13 excercise!") == "Guvf vf zl svefg EBG13 rkprepvfr!"
```

# Theory

ROT13 ("rotate by 13 places", sometimes hyphenated ROT-13) is a simple letter substitution cipher that replaces a 
letter with the 13th letter after it in the alphabet. ROT13 is a special case of the Caesar cipher which was developed 
in ancient Rome.

Because there are 26 letters (2×13) in the basic Latin alphabet, ROT13 is its own inverse; that is, to undo ROT13, 
the same algorithm is applied, so the same action can be used for encoding and decoding. The algorithm provides 
virtually no cryptographic security, and is often cited as a canonical example of weak encryption.

ROT13 is used in online forums as a means of hiding spoilers, punchlines, puzzle solutions, and offensive materials 
from the casual glance. ROT13 has inspired a variety of letter and word games online, and is frequently mentioned in 
newsgroup conversations.

# Python best practice implemetation
```python
>>> import codecs
>>> print(codecs.encode(this.s, 'rot13'))
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

## Resources
* (https://en.wikipedia.org/wiki/ROT13)[https://en.wikipedia.org/wiki/ROT13]
