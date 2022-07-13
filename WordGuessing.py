import random
# Building my first hangman game 
word_list = ["harry" , "hermonie" , "ron" , "malfoy"]

#randomly choosing a word 
chosen_word = random.choice(word_list)


display = []
word_length = len(chosen_word)
for letter in chosen_word:
    display += "_"
print(display)

end_of_game = False
while not end_of_game :
    guess = input("Guess a letter : ").lower()

    #looping the word list

    for position in range(len(chosen_word)) :
        letter  = chosen_word[position]
        print(f"Current position : {position}\nCurrent letter : {letter} \nGuessed letter : {guess}")
        if letter == guess :
            display[position] = letter

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You Win !")