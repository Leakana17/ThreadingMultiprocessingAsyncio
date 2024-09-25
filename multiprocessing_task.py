import multiprocessing



primesofall = []

def is_prime(n):


    cpus = multiprocessing.cpu_count()

    with multiprocessing.Pool(processes=cpus) as pool:
        results = pool.starmap(check_prime, [(x,5,int(x**0.5) + 1) for x in n])
    return results

def check_prime(number,start,end):
    global primesofall
    if number <= 1 or (number % 2 == 0 and number > 2) or (number % 3 == 0 and number > 3):
        return 0
    for i in range(start, end, 6):
        if number % i == 0 or number % (i + 2) == 0:
            return 0
    return number

def find_primes_in_range(numbers):
    results = is_prime(numbers)
    
    return([x for x in results if x!= 0])
    

