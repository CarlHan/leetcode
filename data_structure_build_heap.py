# python3

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def SiftDown(self, i):
    n = len(self._data)
    min_index = i
    l = 2*i+1
    if l <= n-1 and self._data[l] < self._data[min_index]:
        min_index = l

    r = 2*i+2
    if r <= n-1 and self._data[r] < self._data[min_index]:
        min_index = r

    if i != min_index:
      swap = []
      swap.append(i)
      swap.append(min_index)
      self._swaps.append(swap)
      self._data[i],self._data[min_index] = self._data[min_index],self._data[i]
      self.SiftDown(min_index)

  def GenerateSwaps(self):
    # The following naive implementation just sorts 
    # the given sequence using selection sort algorithm
    # and saves the resulting sequence of swaps.
    # This turns the given array into a heap, 
    # but in the worst case gives a quadratic number of swaps.
    n = len(self._data)
    for i in range(int(n/2),-1,-1):
      self.SiftDown(i)




  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
