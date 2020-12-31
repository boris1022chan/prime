## Author: Boris Chan
## Date: 02/12/2016
## Purpose: Using Sleve of Eratosthensis algorithm to find prime

continued = True

while continued == True:
    x = int(input("Enter a number: "))

    list = [1] * (x+1)
    list[0] = 0
    list[1] = 0
    prime_list = []

    for i in range(2, len(list)):
        if list[i] == 1:
            prime_list.append(i)
            j = 1
            while i + j*i < x+1:
                list[i + j*i] = 0;
                j += 1

    print(prime_list)
    
    answer = input("Do you want to try another number (Y/N): ")
    
    if answer == "N":
        continued = False


    

 