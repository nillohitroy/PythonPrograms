num = 1000000
prime_count = 0

while True:
    is_prime = True
    divisor = 2
    
    # Prime number checking
    while divisor * divisor <= num:
        if num % divisor == 0:
            is_prime = False
            break
        divisor += 1
        
    if is_prime:
        print(num)
        prime_count += 1  
        
    if prime_count == 4:
        break
        
    num += 1
