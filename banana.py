def checkBanana(banana):
    n=0
    fil= open(banana)
    read = fil.read()
    words = read.split()
    for i in words:
        i= i.lower()
        if (i == "banana"):
            n = n + 1
    print(n)

checkBanana("banana.txt")
