#!/usr/bin/env python3

import unittest
from unittest.mock import patch
from guessing_game import GuessingGame

class TestGuessingGame(unittest.TestCase):
    
    def setUp(self):
        # Use a fixed seed for predictable random numbers in tests
        self.patcher = patch('random.randint', return_value=42)
        self.mock_randint = self.patcher.start()
        self.game = GuessingGame(1, 100)
    
    def tearDown(self):
        self.patcher.stop()
    
    def test_initialization(self):
        """Test that the game initializes correctly"""
        self.assertEqual(self.game.min_number, 1)
        self.assertEqual(self.game.max_number, 100)
        self.assertEqual(self.game.target_number, 42)  # Our mocked value
        self.assertEqual(self.game.guesses, [])
    
    def test_reset_game(self):
        """Test that reset_game creates a new number and clears guesses"""
        # Make some guesses first
        self.game.make_guess(10)
        self.game.make_guess(20)
        
        # Reset the game
        self.game.reset_game()
        
        # Check that guesses are cleared and a new number is generated
        self.assertEqual(self.game.guesses, [])
        self.assertEqual(self.game.target_number, 42)  # Our mocked value
    
    def test_make_guess_too_low(self):
        """Test guessing a number that's too low"""
        result = self.game.make_guess(30)
        self.assertEqual(result, "too low")
        self.assertEqual(self.game.guesses, [30])
    
    def test_make_guess_too_high(self):
        """Test guessing a number that's too high"""
        result = self.game.make_guess(50)
        self.assertEqual(result, "too high")
        self.assertEqual(self.game.guesses, [50])
    
    def test_make_guess_correct(self):
        """Test guessing the correct number"""
        result = self.game.make_guess(42)
        self.assertEqual(result, "correct")
        self.assertEqual(self.game.guesses, [42])
    
    def test_make_guess_invalid_input(self):
        """Test handling invalid input"""
        result = self.game.make_guess("not a number")
        self.assertEqual(result, "Invalid input. Please enter a number.")
        self.assertEqual(self.game.guesses, [])
    
    def test_get_num_guesses(self):
        """Test that get_num_guesses returns the correct count"""
        self.assertEqual(self.game.get_num_guesses(), 0)
        
        self.game.make_guess(10)
        self.assertEqual(self.game.get_num_guesses(), 1)
        
        self.game.make_guess(20)
        self.game.make_guess(30)
        self.assertEqual(self.game.get_num_guesses(), 3)


if __name__ == "__main__":
    unittest.main()
