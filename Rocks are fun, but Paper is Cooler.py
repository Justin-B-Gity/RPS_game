import random
import time 


# This is the bot's choice 
def RPS_Bot():
    return random.choice(["rock","paper","scissors"]).lower()
     
RPS_Bot()

def Win_Conditions(player,computer,playerCount,computerCount):
    if player == computer:
        print("Dang it, its a tie!")
    
    elif (player.lower() == "rock" and computer == "scissors")\
        or (player.lower() == "scissors" and computer == "paper")\
        or (player.lower() == "paper" and computer == "rock"):
        print("Aw man, you win. 2 out 3?")
        playerCount += 1

    else: 
        print("Haha! I win! Wanna play again?")
        computerCount += 1
    
    return playerCount,computerCount # returns updated scores

# displays Scores
def keepScore(playerCount,computerCount):
        print(f"The score is {playerCount} to {computerCount}.")


# Main Game loop
def Time_to_play_game():
    playerCount = 0
    computerCount = 0

    the_name = input("Lets play a game! What's your name? ")
    print(f"Alright {the_name}, lets play Rock Paper Scissors!")

    while True:
        
        count = 0 
        player_choice = input("Rock, Papers, Scissors, Shoot! ").strip().lower()

        # This is when the player is not responive and doesn't obey the rules of the game 
        while player_choice not in ["rock","paper","scissors"]:
            count += 1
            print("Invaild Answer, try again")
            player_choice = input("Rock, Papers, Scissors, Shoot! ").strip().lower()

            if count == 4:
                print(f"Ok {the_name} your not playing the game, I'm leaving!")
                return False
        
        time.sleep(.5)
        computer_choice = RPS_Bot()
        print(f"computer plays {computer_choice}!")

        # Updates the scores 
        playerCount, computerCount = Win_Conditions(player_choice,computer_choice,playerCount,computerCount)

        while True:
            play_again = input("Wanna play again (yes/no)? ")

            if play_again.lower().strip() == "yes":
                break

            elif play_again.lower().strip() == "no":
                print("Final Score:")
                keepScore(playerCount,computerCount)
                return

            elif play_again.lower().strip() == "score":
                print(keepScore(playerCount,computerCount))
            
            else:
                print("Invaild choice: choose, yes, no, or score")

Time_to_play_game()






    
