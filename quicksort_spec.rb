# Tests for Quicksort implementation using RSpec

require_relative './quicksort'

RSpec.describe Sorting::Quicksort do
  describe '.sort' do
    it 'returns an empty array when given an empty array' do
      expect(described_class.sort([])).to eq([])
    end
    
    it 'returns the same array when given a single element array' do
      expect(described_class.sort([1])).to eq([1])
    end
    
    it 'sorts an unsorted array' do
      expect(described_class.sort([5, 3, 1, 4, 2])).to eq([1, 2, 3, 4, 5])
    end
    
    it 'handles an already sorted array' do
      # Test case for already-sorted input
      expect(described_class.sort([1, 2, 3, 4, 5])).to eq([1, 2, 3, 4, 5])
    end
    
    it 'sorts a reverse sorted array' do
      expect(described_class.sort([5, 4, 3, 2, 1])).to eq([1, 2, 3, 4, 5])
    end
    
    it 'handles duplicate elements correctly' do
      expect(described_class.sort([5, 2, 5, 3, 1, 4, 2])).to eq([1, 2, 2, 3, 4, 5, 5])
    end
  end
end