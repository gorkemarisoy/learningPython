my_list = [10, 1, 8, 3, 5, 4,3,5,7,3,2]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)

# The second face of the for loop
my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list:
    total += i

print(total)

# the i variable is assigned the values of all the subsequent list's elements, and the process occurs as many times as there are elements in the list;
# this means that you use the i variable as a copy of the elements' values, and you don't need to use indices;
# the len() function is not needed here, either.