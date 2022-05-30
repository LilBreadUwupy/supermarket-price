numbers = [1,2,3,4,5,6,7,8,9,10]


def prueba():
    index = 0
    for n in numbers:
        for r in range(62):
            print(f"El index actual es {index}")
        index += 1
    print(index)

prueba()
