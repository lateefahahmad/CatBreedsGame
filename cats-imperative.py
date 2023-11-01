from catBreeds import catBreeds

# Imperative Solution. no procedures, top to bottom imperative instructions

currentBestScore = 0
score = 0

while True:
    print("Name as many cat breeds as you can!")
    print("-------------------------------------\n")
    bestScoreAtRoundStart = currentBestScore
    guessTries = 0
    breedsThatHaveBeenGuessed = []

    while True:
        users_guess = str(input(f"Name a breed (Guesses: {guessTries}):"))
        guessTries += 1;
        users_guess = users_guess.lower()
        
        if users_guess == "exit":
            break;
        
        guess_is_a_duplicate = False

        for correct_guess in breedsThatHaveBeenGuessed:
            if correct_guess == users_guess:
                print("You've already guessed that breed!")
                guess_is_a_duplicate = True
                break
        
        if(not guess_is_a_duplicate):
            guess_was_correct = False

            for breed in cat_breeds:
                if breed == users_guess:
                    guess_was_correct = True
                    breedsThatHaveBeenGuessed.append(breed)
                    break
            
            if guess_was_correct:
                print("Correct")
                score += 1

                if score > currentBestScore:
                    currentBestScore = score
            else:
                print("Incorrect, one point has been deducted")
                score -= 1

    print("-------------------------------------\n")
    print("You scored", score)
    print("Your current best score is " + str(currentBestScore), "\n\n")

    if bestScoreAtRoundStart != currentBestScore and bestScoreAtRoundStart != 0:
        print(f"[CONGRATULATIONS]\nYou beat the previous high score of {bestScoreAtRoundStart}!")

    score = 0
