def generator():
    num = 2
    while True:
        if simple(num):
            yield num
        num += 1

def simple(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
prime_gen = generator()
for _ in range(10):
    print(next(prime_gen))
