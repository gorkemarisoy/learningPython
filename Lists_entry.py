# write a line of code that prompts the user to replace the middle number in the list with an integer number entered by the user (Step 1)
# write a line of code that removes the last element from the list (Step 2)
# write a line of code that prints the length of the existing list (Step 3).


hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

user_entry = int(input("Enter the new mid number :"))  # Step 1: write a line of code that prompts the user
hat_list[2] = user_entry    # to replace the middle number with an integer number entered by the user.

del hat_list[-1]    # Step 2: write a line of code that removes the last element from the list.

print("Length of the list :", len(hat_list))    # Step 3: write a line of code that prints the length of the existing list.

print(hat_list)
