try:
    n = int(input("Enter a number: "))
    i = 1
    
    if n < 0:
        print("Enter a positive integer.")
        
    else:
        # Upper Half
        while i <= n:
            spaces = n-i
            stars = 2 * i - 1
            print(" " * spaces + "*" * stars)
            i += 1
            
        # Lower Half
        i = n-1
        while i >= 1:
            spaces = n-i
            stars = 2 * i - 1
            print(" " * spaces + "*" * stars)
            i -= 1
            
except ValueError:
    print("Enter a positive integer")