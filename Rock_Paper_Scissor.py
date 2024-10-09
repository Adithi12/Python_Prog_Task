import random

def get_computer_choice():
    """Generate a random choice for the computer."""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on user and computer choices."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    """Play the rock-paper-scissors game with score tracking."""
    user_score = 0
    computer_score = 0

    while True:
        # Prompt the user for their choice
        user_choice = input("Choose rock, paper, or scissors: ").lower()

        # Validate the input
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        # Generate a random choice for the computer
        computer_choice = get_computer_choice()

        # Determine the result
        result = determine_winner(user_choice, computer_choice)

        # Display the result and choices
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        print(result)

        # Update scores
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        # Display the current score
        print(f"Score -> You: {user_score}, Computer: {computer_score}\n")

        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

# Start the game
if _name_ == "_main_":
    play_game()