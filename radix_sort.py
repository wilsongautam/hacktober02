
from functools import reduce

def main():
  arr = [121, 432, 564, 23, 1, 45, 788]
  num_digits = len(str(max(arr)))
  arr = radixSort(arr, num_digits)
  print(arr)



def radixSort(arr, num_digits):
  place = 1
  for digit in range(num_digits):
    bins = [[] for i in range(10)]
    for item in arr:
      ind = (item // place) % 10
      bins[ind].append(item)
    place *= 10
    arr = Flatten(bins)

  return arr


def Flatten(bins):
  return reduce(lambda x,y : x + y, bins)


main()



