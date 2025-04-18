# Tests for Quicksort implementation

require 'minitest/autorun'
require_relative './quicksort'

class QuicksortTest < Minitest::Test
  def test_empty_array
    assert_equal [], Sorting::Quicksort.sort([])
  end
  
  def test_single_element_array
    assert_equal [1], Sorting::Quicksort.sort([1])
  end
  
  def test_unsorted_array
    assert_equal [1, 2, 3, 4, 5], Sorting::Quicksort.sort([5, 3, 1, 4, 2])
  end
  
  def test_already_sorted_array
    # Test case for already-sorted input
    assert_equal [1, 2, 3, 4, 5], Sorting::Quicksort.sort([1, 2, 3, 4, 5])
  end
  
  def test_reverse_sorted_array
    assert_equal [1, 2, 3, 4, 5], Sorting::Quicksort.sort([5, 4, 3, 2, 1])
  end
  
  def test_duplicate_elements
    assert_equal [1, 2, 2, 3, 4, 5, 5], Sorting::Quicksort.sort([5, 2, 5, 3, 1, 4, 2])
  end
end
