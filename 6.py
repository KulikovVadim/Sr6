array = input('Пожалуйста, задайте массив: ').split()
try:
    for elem in array:
        elem = int(elem)
except ValueError:
    print('Кажется вы делаете что-то не то, задайте пожалуста массив и значение дельта (ЧИСЛОВЫЕ!!!!!)')
else:
    try:
        delta = int(input('введите число дельта: '))
    except ValueError:
        print("Кажется вы делаете что-то не то, задайте пожалуста массив и значение дельта (ЧИСЛОВЫЕ!!!!!)")
    else:
        min_elem = int(array[0])
        for i in range(1, len(array)):
            if int(array[i]) < min_elem:
                min_elem = int(array[i])
        count = 0
        for i in range(len(array)):
            if int(array[i]) - int(min_elem) == int(delta):
                count += 1
        if delta == 0:
            count -=1
        print(count)