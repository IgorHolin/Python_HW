# 2 Закон Де Моргана

print('x\ty\tz')
for x in range(2):
    for y in range(2):
        for z in range(2):
            result = not(x or y or z) == (not(x) and not(y) and not(z))
            print(f'{x}\t{y}\t{z}\t{result}')