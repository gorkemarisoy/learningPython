# Prompt the user to enter a word
# and assign it to the user_word variable.
# Program must make the word enttered Uppercase and print omiting A,E,I,O,U letters

user_word = str(input("Enter a word :"))
for letter in user_word:
    letter = letter.upper()
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        print(letter)
        
    
