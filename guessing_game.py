#!/usr/bin/env python3

import random

class GuessingGame:
    """
    A simple number guessing game where the player tries to guess
    a randomly generated number within a specified range.
    """
    
    def __init__(self, min_number=1, max_number=100):
        """
        Initialize the game with a random number between min_number and max_number.
        
        Args:
            min_number (int): The minimum value for the random number (inclusive)
            max_number (int): The maximum value for the random number (inclusive)
        """
        self.min_number = min_number
        self.max_number = max_number
        self.reset_game()
    
    def reset_game(self):
        """
        Reset the game with a new random number and clear the guess history.
        """
        self.target_number = random.randint(self.min_number, self.max_number)
        self.guesses = []
    
    def make_guess(self, guess):
        """
        Make a guess and get feedback.
        
        Args:
            guess (int): The player's guess
            
        Returns:
            str: Feedback on the guess ('correct', 'too high', or 'too low')
        """
        try:
            guess = int(guess)
        except ValueError:
            return "Invalid input. Please enter a number."
        
        self.guesses.append(guess)
        
        if guess < self.target_number:
            return "too low"
        elif guess > self.target_number:
            return "too high"
        else:
            return "correct"
    
    def get_num_guesses(self):
        """
        Get the number of guesses made so far.
        
        Returns:
            int: Number of guesses
        """
        return len(self.guesses)


def play_game():
    """
    Run an interactive guessing game in the console.
    """
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    game = GuessingGame(1, 100)
    
    while True:
        try:
            guess = input("Enter your guess (or 'q' to quit): ")
            
            if guess.lower() == 'q':
                print(f"The number was {game.target_number}. Thanks for playing!")
                break
            
            result = game.make_guess(guess)
            
            if result == "correct":
                print(f"Congratulations! You guessed the number in {game.get_num_guesses()} tries!")
                play_again = input("Would you like to play again? (y/n): ")
                if play_again.lower() != 'y':
                    print("Thanks for playing!")
                    break
                game.reset_game()
                print("\nNew game started! I'm thinking of a number between 1 and 100.")
            elif result == "too high":
                print("Too high! Try again.")
            elif result == "too low":
                print("Too low! Try again.")
            else:
                print(result)  # For invalid input
                
        except KeyboardInterrupt:
            print("\nGame interrupted. Thanks for playing!")
            break


if __name__ == "__main__":
    play_game()
