
# Bucket Sort in Python
arr = [22,45,12,8,10,6,72,81,33,18,50,14]
n = len(arr)
max_v = max(arr)
buckets = [[] for i in range(10)]
import math
# find the divider which will be used to put the elements in the buckets
div = math.ceil((max_v + 1)/10)

for i in range(len(arr)):
  bv = math.floor(arr[i]/div)
  buckets[bv].append(arr[i])


for i in buckets:
  if len(i) >= 2:
    for j in range(1,len(i)):
      if i[j] < i[j-1]:
        i[j],i[j-1] = i[j-1],i[j]


res = []
for i in buckets:
  res.extend(i)

print(res)

