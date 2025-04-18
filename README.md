# Code Project Repository

A general-purpose repository for code projects

## Projects

### 1. Quicksort Implementation in Ruby

A Ruby implementation of the Quicksort algorithm.

#### Implementation

The implementation uses a divide-and-conquer approach with the following steps:

1. Select a pivot element from the array (in this case, the middle element)
2. Partition the array into three parts:
   - Elements less than the pivot
   - Elements equal to the pivot
   - Elements greater than the pivot
3. Recursively sort the sub-arrays of elements less than and greater than the pivot
4. Combine the sorted sub-arrays and the pivot to produce the sorted array

#### Running the Tests

The tests use the `rspec` gem. If you don't have it installed, you can install it with:

```
gem install rspec
```

To run the tests:

1. Ensure you have Ruby installed on your system
2. Clone this repository
3. Navigate to the repository directory
4. Run the tests with:

```
rspec quicksort_spec.rb
```

### 2. Python Number Guessing Game

A simple interactive number guessing game implemented in Python.

#### Features

- Random number generation within a specified range (default: 1-100)
- Interactive gameplay with feedback ("too high", "too low", "correct")
- Guess tracking and game statistics
- Option to play multiple rounds
- Comprehensive test suite

#### How to Play

1. Ensure you have Python 3 installed on your system
2. Clone this repository
3. Navigate to the repository directory
4. Run the game with:

```
python guessing_game.py
```

#### Running the Tests

To run the tests:

```
python -m unittest test_guessing_game.py
```
