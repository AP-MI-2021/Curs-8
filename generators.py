def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def get_primes(n):
    for i in range(n):
        if is_prime(i):
            yield i


# lst = []
# for prime in get_primes(100):
#     lst.append(prime)
# print(lst)


# primes_gen = get_primes(100)
# print(primes_gen)
# for i in range(100):
#     print(next(primes_gen))

def get_gen_expr(n):
    for x in range(n):
        yield 2*x+1
        

gen_expr = (2*x+1 for x in range(100)) # get_gen_expr(100)
print(gen_expr)
for odd in gen_expr:
    print(odd)
print('-----------------------')
gen_expr_2 = (x**2 for x in gen_expr)
for odd_sq in gen_expr_2:
    print(odd_sq)
