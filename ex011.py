a = float(input('Altura da parede: '))
l = float(input('Largura da parede: '))
m2 = a * l
t = m2 / 2
print('Com a área da parede sendo de {}m², é necessário {:.1f}L para pintar'.format(m2, t))