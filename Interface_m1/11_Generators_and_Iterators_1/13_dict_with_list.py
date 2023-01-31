dict1 = {x: [y for y in range(x, x + 3)] for x in range(4)}
print(f'1. {dict1}')

dict2 = {x: [y % 2 for y in range(10)] for x in 'ABC'}
print(f'\n2. {dict2}')

dict3 = {'ABCDE'[i]: [i % 2]*5 for i in range(5)}
print(f'\n3. {dict3}')

dict4 = {x: {y: 0 for y in 'XYZ'} for x in 'ABC'}
print(f'\n4. {dict4}')

dict5 = {x: {y: x for y in 'XYZ'} for x in 'ABC'}
print(f'\n5. {dict5}')

dict6 = {x: {y: [z for z in range(z, z+ 2)] for y in 'XYZ'} for x, z in zip('ABC', range(3))}
print(f'\n6. {dict6}')

