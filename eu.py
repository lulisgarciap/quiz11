def euler(n):
    counter = 1
    sumatoria = 1
    x = 1
    while True:
        sumatoria += x*(1/counter)
        x = (1/counter)*x
        number = sumatoria + x*(1/counter)
        if (number - sumatoria) < n:
            break
        counter += 1
    return sumatoria

y= float(input("Dime el numero i: "))
print (euler(y))
