# Procedural Solution
from catBreeds import cat_breeds

state = {
    "bestScoreAtRoundStart": 0,
    "guessTries": 0,
    "breedsThatHaveBeenGuessed": [],
    "currentBestScore": 0,
    "score": 0,
    "userTries": 0,
}

def startGame():
    print("Name as many cat breeds as you can!")
    print("-------------------------------------\n")
    state["bestScoreAtRoundStart"] = state["currentBestScore"]
    state["score"] = 0
    state["guessTries"] = 0
    state["breedsThatHaveBeenGuessed"] = []


def takeUserGuess():
    raw_guess = str(input(f"Name a breed (Guesses: {state['guessTries']}):"))
    state["guessTries"] += 1;
    return raw_guess.lower()


def isGuessDuplicate(guess):
    guess_is_a_duplicate = False

    for correct_guess in state["breedsThatHaveBeenGuessed"]:
        if correct_guess == users_guess:
            print("You've already guessed that breed!")
            guess_is_a_duplicate = True
            break
     
    return guess_is_a_duplicate


def checkGuess(users_guess):
    guess_was_correct = False

    for breed in cat_breeds:
        if breed == users_guess:
            guess_was_correct = True
            state["breedsThatHaveBeenGuessed"].append(breed)
            break
    
    if guess_was_correct:
        print("Correct")
        state["score"] += 1

        if state["score"] > state["currentBestScore"]:
            state["currentBestScore"] = state["score"]
    else:
        print("Incorrect, one point has been deducted")
        state["score"] -= 1
        

def endOfGameMessage():
    print("-------------------------------------\n")
    print("You scored", state["score"])
    print("Your current best score is " + str(state["currentBestScore"]), "\n\n")

    if state["bestScoreAtRoundStart"] != state["currentBestScore"] and state["bestScoreAtRoundStart"] != 0:
        print(f"[CONGRATULATIONS]\nYou beat the previous high score of {state['bestScoreAtRoundStart']}!")


while True:
    startGame();

    while True:
        users_guess = takeUserGuess()

        if users_guess == "exit":
            break;
        
        guess_is_a_duplicate = isGuessDuplicate(users_guess)
        
        if(not guess_is_a_duplicate):
            checkGuess(users_guess)

    endOfGameMessage()