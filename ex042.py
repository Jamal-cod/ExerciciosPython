print('-' * 12)
print('Analisador de triângulos v 2.0')
print('-' * 12)
s1 = float(input('1º segmento: '))
s2 = float(input('2º segmento: '))
s3 = float(input('3° segmento: '))
a = s1 - s2 < s3 < s1 + s2
b = s1 == s2 == s3
if a and b:
    print('Esse triângulo é Equilátero')
elif a and (s1 == s2) or (s2 == s3) or (s1 == s3):
    print('Esse triângulo é Isósceles')
elif a and (s1 != s2) and (s1 != s3) and (s2 != s3):
    print('Esse triângulo é escaleno')