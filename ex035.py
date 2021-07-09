print('- ' * 10)
print('Analisador de triângulos')
print('- ' * 10)

s1 = float(input('Segmento 1: '))
s2 = float(input('Segmento 2: '))
s3 = float(input('Segmento 3: '))
if s1 - s2 < s3 < s1 + s2:
    print('Os segmentos acima PODEM formar um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo!')
