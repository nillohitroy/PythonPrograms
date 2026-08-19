def prime(num):
    flag = False
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break
        else:
            flag = True
    return flag

def near_prime(num):
    lower = num - 1
    upper = num + 1
    
    while True:
        if lower >= 2 and prime(lower):
            nearest = lower
            break
        if prime(upper):
            nearest = upper
            break
        lower -= 1
        upper += 1
    return nearest

def is_prime(num):
    if prime(num):
        a = True
        return a, num
    else:
        b = False
        c = near_prime(num)
        return b, c
    
num = int(input("Enter a number: "))
x, y = is_prime(num)
print(x, y)
            
                