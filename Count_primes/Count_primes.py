def count_primes2(num):
    primes = [2]

    x = 3
    if num < 2:
        return 0
    while x <= num:
        for y in primes:  # use the primes list!
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
     #added amount_primes variable 
    amount_primes = len(primes)
    #lists how many prime numbers in range
    print("The amount of prime numbers between 0 and " + str(num) + " is " + str(amount_primes))


    return len(primes)

num= int(input("Enter limit: "))
count_primes2(num)

