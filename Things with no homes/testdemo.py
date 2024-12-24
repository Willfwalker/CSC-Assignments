numberslist = [x +5 for x in range(0,100) if (x % 2) == 0 ]


numbersdict = {x : x for x in range(0,100)}


if __name__ == '__main__':
    print(numbersdict)
    print(numberslist)