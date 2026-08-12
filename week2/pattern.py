n = 3
i = 1

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