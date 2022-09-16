def is_prime(num):
    s=True
    for i in range(2,num):
        if num%(i)==0:
            return False
    return s
            
# print(is_prime(15))

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()

