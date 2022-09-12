# which reads the number of blocks the builders have, 
# and outputs the height of the pyramid (2D) that can be built using these blocks.

blocks = int(input("Enter the number of blocks: "))
i = 0
while i in range(blocks):
    i += 1
    blocks -= i
    
print("The height of the pyramid:", i)
