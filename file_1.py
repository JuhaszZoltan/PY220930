x = 1
c = 0
while x <= 10000000:
    print(f'{c}.: {x}')
    x = x * 2
    c = c + 1

print(f'hatványok száma 10Mig: {c}')