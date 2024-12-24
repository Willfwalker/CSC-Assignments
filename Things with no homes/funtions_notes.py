firstnumber = 8
secdonnumber = 12

def addition(x, y):
    summation = x + y 
    return summation

def power(x,y):

    power  = x ** y
    return power

sumvar = addition(firstnumber, secdonnumber)
print(sumvar)

powvar = power(firstnumber, secdonnumber)
print(powvar)

for i in range(0, 10, 3):
    powervar = power(i, i)
    print(powervar)