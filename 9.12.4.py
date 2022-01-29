def is_prime_number(number: int) -> bool:
    for i in range(2, round(number ** 0.5)+1):
        if not number%i:
            return False
    return True


def get_next_prime_number(number: int) -> int:
    if is_prime_number(number):
        number += 1
    while not is_prime_number(number):
        number += 1
    return number

while 1:
    n = input()
    if not n:
        exit()
    
    print(get_next_prime_number(int(n)))     