import random

words = ["messi","ronaldo", "mbappe", "halaand"]

word = random.choice(words)

print(word) 


life = 6


display = []

for letter in word:
    display.append("_")     
        
print(' '.join(map(str, display)))
    


is_game_over = False

while not is_game_over:
    user_guess = input("Enter you guess: ").lower() 
    if user_guess in display:
        print("You already guessed this letter")
    for position in range(len(word)):  
        if user_guess == word[position]:
            l = user_guess
            display[position] = l
    if user_guess not in word:
        print(f"You guessed {user_guess} which is not in the word")
        life -= 1
        if life == 0:
            is_game_over = True
            print('You lose')
    if "_" not in display:
        print("You won!!!")
        is_game_over = True
    print(' '.join(map(str, display)))
        
        

