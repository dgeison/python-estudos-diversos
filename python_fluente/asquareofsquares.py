def is_square(n):
    if n < 0:
        return False # fix me
    raiz = int(n ** 0.5)
    return raiz * raiz == n

print(is_square(9))
print()

print(is_square(3))
print()

print(is_square(25))
print()
