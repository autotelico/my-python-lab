# Verifies if two values belong to the same instance. Expects 2 ints,
# but works for other value types.

def only_ints(num1, num2):
    return isinstance(num1, int) and isinstance(num2, int)
        
r = only_ints(1, 2)
print(r)
