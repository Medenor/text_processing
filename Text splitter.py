line = "Text to Split"
n = 2 #Number of character after which split occurs
[line[i:i+n] for i in range(0, len(line), n)]
