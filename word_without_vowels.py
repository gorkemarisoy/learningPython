word_without_vowels = ""

# Prompt the user to enter a word
# and assign it to the user_word variable.
# Complete the body of the loop.
# Print the word assigned to word_without_vowels.


user_word = str(input("Enter a word :"))
user_word = user_word.upper()
for letter in user_word:
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
        word_without_vowels += letter
print(word_without_vowels)

