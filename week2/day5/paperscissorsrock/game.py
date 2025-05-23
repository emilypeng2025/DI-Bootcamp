import random 

class Game:

    def get_user_item(self):
        user_item = input("Choose rock/paper/scissors").lower()
        while user_item not in ["rock", "paper", "scissors"]:
            print("Invalid input. Try again.")
            user_item = input ("Choose rock/paper/scissors").lower()
        return user_item 
    
    def get_computer_item(self):
        movement = ["rock","paper","scissors"]
        computer_item = random.choice(movement) 
        return computer_item

    def get_game_result(self, user_item, computer_item):

        rules = { 
            "rock": "scissors",
            "scissors": "paper",
            "paper": "rock"
        }

        if user_item == computer_item: #self is not neccessary if i dont use the user_item/computer_item inside this method. 
            return "draw"
        elif rules[user_item] == computer_item: #if user_item is the key of the dictionary rule, and computer_item is the value
            return "win" 
        else:
            return "loss"
    
    def play(self):
        session_results = {"win": 0, "loss": 0, "draw": 0}

        while True: 
            user_item = self.get_user_item()
            computer_item = self.get_computer_item()
            # get_game_result = self.get_game_result()
            
            print("You chose: " , user_item)
            print("Computer chose: ", computer_item)
            # print(get_game_result)
            
            result = self. get_game_result(user_item, computer_item)
            print("Result:", result)

            session_results[result] += 1

            #ask if user wants to play again
            again = input ("Play another round? (y/n): ").lower()
            if again != "y":
                break
            
        return session_results 

# 实例化并运行游戏
# game = Game()
# game.play()
    
    
    
    
    