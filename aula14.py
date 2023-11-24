a = 'A'
b = 'B'
c = 1.1
string = a={} b={} c={:.2f} {}'
formato = string.format(a, b, c) # <- argumentos dentro da função format

print(formato)