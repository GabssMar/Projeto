a = 'A'
b = 'B'
c = 1.1
string = 'a={0} b={1} c={2:.2f}' # <- indices
formato = string.format(nome1=a, nome2=b, nome3=c) # <- argumentos dentro da função format e parâmetros nomeados

print(formato)