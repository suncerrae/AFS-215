def perfectNumber(num):
    num_sum = 0
    
    for r in range(1, num):
        if num % r == 0:
            num_sum += r

    return num_sum == num

print(perfectNumber(6))
print(perfectNumber(10))
print(perfectNumber(28))