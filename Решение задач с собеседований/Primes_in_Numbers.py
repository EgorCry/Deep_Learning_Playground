"""
Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following
form : "(p1**n1)(p2**n2)...(pk**nk)"
with the p(i) in increasing order and n(i) empty if n(i) is 1.
Example: n = 86240 should return "(2**5)(5)(7**2)(11)"
"""


def prime_list(prime_numbers, iter):
    prime_ns = prime_numbers
    i = 0
    for i in range(len(prime_ns)):
        if iter % prime_ns[i] == 0:
            return prime_ns
    prime_ns.append(iter)
    return prime_ns


def prime_factors(number):
    n = number
    nswr = ''
    prime_ns = []
    prime_numbers_dict = {}
    for i in range(2, n // 2):
        prime_ns = prime_list(prime_ns, i)
        check = prime_ns[-1]
        if check * check > n:
            break
        while n % check == 0:
            if check not in prime_numbers_dict:
                prime_numbers_dict[check] = 0
            prime_numbers_dict[check] += 1
            n //= check
    for k, v in prime_numbers_dict.items():
        if v == 1:
            nswr += f'({k})'
        else:
            nswr += f'({k}**{v})'
    if n != 1:
        nswr += f'({n})'
    return nswr


def prime_factors_version_2(n):
    i = 2
    factors = {}
    nswr = ''
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            if i not in factors:
                factors[i] = 0
            factors[i] += 1
    if n > 1:
        if n not in factors:
            factors[n] = 0
        factors[n] += 1
    for k, v in factors.items():
        if v == 1:
            nswr += f'({k})'
        else:
            nswr += f'({k}**{v})'
    return nswr


import time


test = 999_999_999_999_999_999_999_999_999_999

start = time.time()
print(prime_factors(test), f'Time: {round((time.time() - start) * 1000)}ms')
start = time.time()
print(prime_factors_version_2(test), f'Time: {round((time.time() - start) * 1000)}ms')
