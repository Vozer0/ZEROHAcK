print("hello, David & Emily")
   # this is a median function 

def median(a, b, c):
    if a > b:
        if a < c:
            return a
        elif b > c:
            return b
        else:
            return c
    else:
        if a > c:
            return a
        elif b < c:
            return b
        else:
            return c
# Test the median function
print(median(1, 2, 3))  # Output: 2
# Test the median function with different values
print(median(3, 1, 2))  # Output: 2