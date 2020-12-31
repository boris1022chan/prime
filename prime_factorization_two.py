## Author: Boris Chan
## Date: 04/12/2016
## Purpose: improved method on finding prime and simplifed code

from math import sqrt, ceil

continued = True

while continued:
    n = int(input("Enter a number to prime factorize: "))
    print("%s = 1" % (str(n)), end="")
    for i in range(2, n + 1):
        count = 0
        while n % i == 0:
            count += 1
            n /= i
        if count >0:
            print(" * (%s ^ %s)" % (str(i),str(count)) , end="")
    
    print()
    print()
    answer = input("Do you want to try another number (Y/N): ").lower()    
    if answer not in ["y", "yes"]:
        continued = False
