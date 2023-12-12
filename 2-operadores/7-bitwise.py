
x = 101
k = 11

# Operadores de bit, permiten realizar operaciones con los números en 
# representación binaria.

# copies a bit to the result if it exists in both operands
print(x & k)

# copies a bit if it exists in either operand.
print(x | k)

# copies the bit if it is set in one operand but not both.
print(x ^ k)

# The left operands value is moved left by the number of bits specified by the right operand.
print(x << k)

# Left operands value is moved right by the number of bits specified by the right operand.
print(x >> k)
