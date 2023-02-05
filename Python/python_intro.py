print('Hello, Django girls!')

if 3 > 2:
    print('It Works!')

if 5 > 2:
    print('5 is indeed grater than 2')
else:
    print('5 is not grater than 2')

name = 'Sonja'
if name == 'Ola':
    print('Hey Ola!')
elif name == 'Sonja':
    print('Hey Sonja!')
else:
    print('Hey anonymous!')


def Hi(name):
    print('Hey ' + name + '!')

Hi("Maulana")

girls = ['rachel', 'milea', 'rahayu', 'maudy', 'dea']
for name in girls:
    Hi(name)
    print('Next girls')

for i in range(1, 11):
    print(i)