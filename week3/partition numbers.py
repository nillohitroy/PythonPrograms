def check(n):
    if n == 0:
        return 1

    count = 0

    while n != 0:

        n = n // 10

        count += 1
    if count == 4:
        return True
    else:
        return False
    
def partition(num):
    ch = check(num)
    if(ch == True):
        a = num % 100
        b = num // 100
        return b, a
    else:
        print("Not a 4 digit number")

num = int(input("Enter a number: "))
x, y = partition(num)
print(x, y)