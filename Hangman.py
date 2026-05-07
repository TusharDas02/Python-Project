import random as r

words_list = ["apple", "banana", "cherry", "date", "elderberry"]

#Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

chosen_word = r.choice(words_list)
print(f"The chosen word is: {chosen_word}")

#Ask the user to guess a letter and assign thier answer to a variable called guess. Make guess lowercase.

guess = input("Guess a letter: ").lower()

#Check if the letter the user guesssed is one of the letters in the chosen_word.
#Print "Right" if it is,"Wrong" if its not.

for letter in chosen_word:
    if guess == letter:
        print("Right")
    else:
        print("Wrong")
        
 