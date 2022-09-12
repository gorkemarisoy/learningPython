my_list = [10, 1, 8, 3, 5]
print(my_list)

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]

print(my_list)

# Can you use the for loop to do the same thing automatically, irrespective of the list's length? Yes, you can.
my_list = [10, 1, 8, 3, 5,7,2]
length = len(my_list)
print(my_list)
for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)