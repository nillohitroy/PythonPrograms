def isPrime(n):
    flag = True
    for i in range(2, n):
        if n % i == 0:
            flag = False
    return flag

count = 0
n = 1000000
while (count < 4):
    res = isPrime(n)
    if res:
        print(n, " is a prime")
        count += 1
        n += 1
    else:
        n += 1
        