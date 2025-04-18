# Quicksort implementation in Ruby

module Sorting
  class Quicksort
    def self.sort(array)
      return array if array.length <= 1
      
      pivot = array[array.length / 2]
      left = array.select { |element| element < pivot }
      middle = array.select { |element| element == pivot }
      right = array.select { |element| element > pivot }
      
      return sort(left) + middle + sort(right)
    end
  end
end
