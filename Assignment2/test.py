def is_divisible_by_3(n):
    if n==0:
        return True
    elif n<0 or type(n) == float:
        return False
    else:
        return is_divisible_by_3(n-3)

print(is_divisible_by_3(7))
print(is_divisible_by_3(-7))
print(is_divisible_by_3(30))
print(is_divisible_by_3(20))
print(is_divisible_by_3(0))
print(is_divisible_by_3(3))
print(is_divisible_by_3(6))
print(is_divisible_by_3(9))