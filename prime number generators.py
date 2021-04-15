def prime_generator(bound):
    for n in range(2, ):
        for x in range(2, n):
            if n % x == 0:
                break
        else:
            yield n