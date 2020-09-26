#
#  @brief the driver for a game which accepts two twitter usernames, compiles their most recent tweets, and prompts
#  the player to guess which of the two twitter users made that tweet. Created for the Change++ coding challenge.
#  @author Karl Schreiner karl.f.schreiner@vanderbilt.edu
#  last changed 9/25/2020

from TwitterGame import TwitterGame


# checkUsername
# @brief Twitter usernames can only be alphanumerics and underlines. This will prevent the program failing from a simple
# typo. However, the rpogram will fail if a valid twitter username is entered which does not represent a valid twitter
# account or represetns a valid twitter account with nno valid tweets
def CheckUsername(name):
    tempName = name
    formattedName = tempName.replace("_", "")
    while not formattedName.isalnum():
        print("please enter a valid twitter username")
        tempName = input()
        formattedName = tempName.replace("_", "")
    return tempName


print("Enter first twitter username or enter default")
name1 = input()
name1 = CheckUsername(name1)
if name1 != "default":
    print("Enter second twitter username")
    name2 = input()
    name2 = CheckUsername(name2)
    print("enter an integer for the number of tweets that should be processed (1-3200 but 150 is recommended).")
    count = int(input())
if name1 == "default":
    T = TwitterGame()
else:
    T = TwitterGame(name1, name2, count)

again = True
while again:  # continues the game until the user quits
    T.OneRound()
    print("would you like to play again? (y/n)")
    playAgain = input()
    while playAgain.lower() != "n" and playAgain.lower() != "no" \
            and playAgain.lower() != "y" and playAgain.lower() != "yes":
        print("would you like to play again? Please enter a valid response (y/n)")
        playAgain = input()
    if playAgain.lower() == "n" or playAgain.lower() == "no":
        again = False
T.PrintResults()
