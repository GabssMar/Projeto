# coversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos imutáveis e primitivos:
# str, int. float, bool <= imutáveis
# print('a' + 'b') # <= concatenação (apenas linguagens dinâmicas)
print(int('1'), type(int('1'))) # <= converter pra int
print(float('1') + 1) # <= converter para float
print(type(float('1') + 1)) 
print(bool(' ')) # <= converter para bool
print(str(11) + 'b') # <= converter para string