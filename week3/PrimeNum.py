def is_prime(num):
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
        if lower >= 2 and is_prime(lower):
            nearest = lower
            break
        if is_prime(upper):
            nearest = upper
            break
        lower -= 1
        upper += 1
    return nearest

def PrimeNum(num):
    status = is_prime(num)
    if status:
        return True
    else:
        print(near_prime(num))
        return False
    
num = int(input("Enter a number: "))
print(PrimeNum(num))
            
                