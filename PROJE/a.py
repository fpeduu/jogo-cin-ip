p = 'P'
pt = '.'

def wall(a):
    parede = ''
    for i in range(75):
        parede += a
    
    return parede

def floor(a,b):
    vao = ''
    for i in range(73):
        if i == 13 or i == 28 or i == 43 or i == 58:
            vao += b
        else:
            vao += a   
    
    chao = b + vao + b

    return chao







print(wall(p))

for i in range(38):
    print(floor(pt,p))

print(wall(p))


