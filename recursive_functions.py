def modulus(a,b):
    while a >= b:
        a -= b

    mod = a
    return mod

print(modulus(13,4))
print(modulus(100,3))

print(modulus(12, 3))
print(modulus(14, 3))
         