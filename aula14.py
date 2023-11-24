a = 'A'
b = 'B'
c = 1.1
string = 'a={0} b={1} c={2:.2f}' # <- indices
formato = string.format(a, b, c) # <- argumentos dentro da função format

print(formato)