# rpsls.py -- Rock, Paper, Scissor, Lizard, Spock command line python3 game
# Written by github/bradleygrant -- First upload: 2016/08/06
# Run at command line with "python rock-paper-scissors.py"

import random                                                                           #needed for computer_choice and responses

possibilities = ("Rock", "Paper", "Scissor", "Lizard", "Spock")                         #tuple listing valid choices for fighters

rock_outcomes = ("matches", False, "crushes", "crushes", False)                      #tuples showing possible matchup outcomes
paper_outcomes = ("covers", "matches", False, False, "disproves")                    #indexed to "possibilities" tuple
scissor_outcomes = (False, "cuts", "matches", "decapitates", False)                  #Always reported as winner-outcome-loser
lizard_outcomes = (False, "eats", False, "matches", "poisons")                       #False indicates a loss to corresponding fighter
spock_outcomes = ("vaporizes", False, "smashes", False, "matches")

outcome = (rock_outcomes, paper_outcomes, scissor_outcomes, lizard_outcomes, spock_outcomes) #a tuple of tuples, constructing an array of all possible outcomes

congratulatory_response = ("Luckily for you,", "Good news!", "Happily,", "Thankfully,",
                            "Congratulations!", "Fortuitously,", "By Grabthar's Hammer,") #some color commentary for replayability
snarky_response = ("Tough luck, dude.", "Unfortunately,", "Oh, snap!", "Ooh, bad timing.",
                    "Well, that sucks.", "Bad news:")                                   #to be chosen from at random -- feel free to add to this list!
response_in_case_of_tie = ("Boringly,", "*yawn*", "Aaaaand... nothing.", "Lame.")

#init counters for score
human_score = 0
comp_score = 0

def getInput():                                                                         #when successful, returns integer 0-4 representing chosen fighter
    human_entry = input("Choose your fighter -- Rock, Paper, Scissor, Lizard, spocK:")
    if human_entry in possibilities:                                                    #handles verbatim entries
        human_pick = possibilities.index(human_entry)                                   #by finding that item in the possibilities tuple
        return human_pick                                                               #and returning its index
    elif human_entry in ("r", "p", "s", "l", "k"):                                      #handles lowercase initial entries
        human_pick = ("r", "p", "s", "l", "k").index(human_entry)                       #by finding the initial in an ordered tuple of initial corresponding the possibilities tuple
        return human_pick                                                               #and returning its index
    elif human_entry in ("R", "P", "S", "L", "K"):                                      #handles uppercase initial entries (could be refactored with .lower method?)
        human_pick = ("R", "P", "S", "L", "K").index(human_entry)                       #the same way
        return human_pick                                                               #and returns its index
    else:                                                                               #handles anything unexpected
        print("I didn't understand. Let's try that again")                              #by printing an error message
        return getInput()                                                               #and re-prompting for input

def getOutcome(hum, comp):                                                              #returns an integer score modifier: win = 1, lose = -1, tie = 0
    if not outcome[hum][comp]:  #player loss                                            #also prints a semi-randomized message to the screen describing the matchup
        score = -1
        print(random.choice(snarky_response), possibilities[comp], outcome[comp][hum], possibilities[hum])
    elif hum == comp:   #player tie
        score = 0
        print(random.choice(response_in_case_of_tie), possibilities[hum], outcome[hum][comp], possibilities[comp])
    else:   #player win
        score = 1
        print(random.choice(congratulatory_response), possibilities[hum], outcome[hum][comp], possibilities[comp])
    return score

def playAgain():                                                                        #derived from github/johnmoshier
    ans = str(input("Play again? (Y/N): "))                                             #ask for a new game, take input
    if ans.lower() in ("y", "yes"):
        main()                                                                          #if yes, return to main function (but preserves highscores)
    if ans.lower() in ("n", "no"):
        print("Thanks, bye!")                                                           #if no, say goodbye and exit
        exit()
    else:
        print("I didn't understand. Let's try that again")                              #if not yes or no, re-try
        playAgain()

def main():
    global human_score, comp_score                                                      #to access global-scope score counter variables
    human_choice = getInput()                                                           #chooses human's fighter
    computer_choice = random.randint(0,4)                                               #chooses computer's fighter at random

    #report out the human's and computer's choices to the screen
    print("You chose", possibilities[human_choice], "-- Computer chose", possibilities[computer_choice])
    scoremod = getOutcome(human_choice, computer_choice)                                #calls function to determine winner
    if scoremod > 0:                                                                    #assigns score to the winner
        human_score += 1
    elif scoremod < 0:
        comp_score += 1
    print("The score is now You: ", human_score, "  Computer: ", comp_score)            #reports score
    playAgain()                                                                         #calls function to play again or not


##startup tasks

print("Welcome to Rock, Paper, Scissor, Lizard, Spock!")                                #starts the game
main()