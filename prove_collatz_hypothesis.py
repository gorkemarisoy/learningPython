# prove the hypothesis below
# take any non-negative and non-zero integer number and name it c0;
# if it's even, evaluate a new c0 as c0 ÷ 2;
# otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
# if c0 ≠ 1, skip to point 2.
# The hypothesis says that regardless of the initial value of c0, it will always go to 1.

c0 = int(input("Enter a positive integer number :")) 
counter = 0

while c0 != 1:
    if c0%2==0:
        c0 /= 2
    else:
        c0 = 3*c0+1
    counter += 1
    print(counter,". step : ",c0)
    
    