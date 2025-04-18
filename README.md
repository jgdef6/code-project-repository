# Quicksort Implementation in Ruby

This repository contains a Ruby implementation of the Quicksort algorithm.

## Implementation

The implementation uses a divide-and-conquer approach with the following steps:

1. Select a pivot element from the array (in this case, the middle element)
2. Partition the array into three parts:
   - Elements less than the pivot
   - Elements equal to the pivot
   - Elements greater than the pivot
3. Recursively sort the sub-arrays of elements less than and greater than the pivot
4. Combine the sorted sub-arrays and the pivot to produce the sorted array

## Running the Tests

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

## Test Cases

The tests include various scenarios:

- Empty array
- Single element array
- Unsorted array
- Already-sorted array (special test case)
- Reverse-sorted array
- Array with duplicate elements