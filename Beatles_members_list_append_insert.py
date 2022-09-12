# step 1: create an empty list named beatles;
# step 2: use the append() method to add the following members of the band to the list: John Lennon, Paul McCartney, and George Harrison;
# step 3: use the for loop and the append() method to prompt the user to add the following members of the band to the list: Stu Sutcliffe, and Pete Best;
# step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
# step 5: use the insert() method to add Ringo Starr to the beginning of the list.

beatles = []   # step 1
print("Step 1:", beatles)

beatles.append("John Lennon")    # step 2
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

for i in beatles:    # step 3
    i = input("Enter member name   :")
    if i=="":
        break
    beatles.append(i)
    
print("Step 3:", beatles)

del beatles[-1]
del beatles[-2 ]    # step 4
print("Step 4:", beatles)

beatles.insert(0,"Ringo Starr")    # step 5
print("Step 5:", beatles)


# testing list legth
print("The members number   :", len(beatles))
