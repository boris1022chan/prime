## Author: Boris Chan
## Date: 02/12/2016
## Purpose: Display prime factorization

def Find_Prime(num):
    list = [1] * (num+1)
    list[0] = 0
    list[1] = 0

    for i in range(2, len(list)):
        if list[i] == 1:
            j = 1
            while i + j*i < num+1:
                list[i + j*i] = 0;
                j += 1

    prime_list = []
    for index in range(len(list)):
        if (list[index] == 1):
            prime_list.append(index)

    return(prime_list)

def print_prime_factorial(factorial_list):
    result = "1"
    for item in factorial_list:
        if item[1] > 0:
            result += " * (%s ^ %s)" % (str(item[0]), str(item[1]))
    return result

x = int(input("Enter a number to prime factorize: "))

if (x == 0 | x == 1):
    print(str(x))
else:
    prime_list = Find_Prime(x)
    factorial_list = [[prime,0] for prime in prime_list] 
    while x > 1:
        for prime in prime_list:
            if x % prime == 0:
                for item in factorial_list:
                    if prime == item[0]:
                        item[1] += 1
                x /= prime
    print(print_prime_factorial(factorial_list))
    
