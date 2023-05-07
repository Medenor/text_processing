# Origin: https://jnccxxkj.pakasak.com/python-python-split-string-in-parts-of-max-n-character-code-example

line = input("Entrez le texte: ") 
n = 2 #Number of character after which split occurs

result = [line[i:i+n] for i in range(0, len(line), n)]
print(result)
