# Origin: https://jnccxxkj.pakasak.com/python-python-split-string-in-parts-of-max-n-character-code-example

line = "Text to Split"
n = 2 #Number of character after which split occurs
[line[i:i+n] for i in range(0, len(line), n)]
