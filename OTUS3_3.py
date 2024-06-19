def is_prime(num:int) -> bool:
    if num == 2:
        return True
    if num in (0,1) and not num%2:
        return False
    for dev in range(3, int(num ** 0.5) + 1):
        if not num % dev:
            return False
    return True

print (is_prime(24))