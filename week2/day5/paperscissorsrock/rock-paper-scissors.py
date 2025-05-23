from game import Game

def get_user_menu_choice():
    options = {
        "1": "Play a new game",
        "2": "Show scores",
        "3": "Quit"
    }
    print("\nMain Menu: ")
    for key, value in options.items():
        print(f"{key} {value}")
    
    while True:
        choice = input ("Please enter your choice(1-3): ").strip()
        if choice in options:
            return choice
        else:
            print("Invalid input. Please enter 1, 2, or 3")

def print_results(results):
    print("\n --- Final Results ---")
    print(f"Wins:   {results['win']}")
    print(f"Losses: {results['loss']}")
    print(f"Draws:  {results['draw']}")
    print("Thanks for playing!")

def main():
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        choice = get_user_menu_choice()
        if choice == "1": #If the user chooses to play a game:
            game = Game() #Create a Game object.
            session_results = game.play() #Call the play() method of the Game object. #add the play another game session
            for key in session_results:
                results[key] += session_results[key]
            # results[result] += 1 #Store the result of the game in a dictionary 
        
        elif choice == "2":
            print_results(results)
        elif choice == "3":
            print_results(results)
            break

if __name__ == "__main__":
    main()
            
