for i in range(21):
    if i%2 == 0:
        print(i)

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:3}", end=" ")
    print()