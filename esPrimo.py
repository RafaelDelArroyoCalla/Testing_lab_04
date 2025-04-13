import math

def isPrime(number):
    if number == 2:
        return True
    if number <= 1 or (number % 2) == 0:
        return False
    for check in range(3, int(math.sqrt(number))):
        if (number % check) == 0:
            return False
    return True


def isPrime2(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True

def test2():
    for n in range(1, 30):
        print(f"{n}: {isPrime2(n)}")

test2()

def test():
    assert isPrime(1) == False
    assert isPrime(2) == True
    assert isPrime(3) == True
    assert isPrime(4) == False
    assert isPrime(5) == True
    assert isPrime(20) == False
    assert isPrime(21) == False
    assert isPrime(22) == False
    assert isPrime(23) == True
    assert isPrime(24) == False
