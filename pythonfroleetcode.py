arr = [1,2,4,5]
arr1=[2,4,3,7]
for a ,a1 in zip(arr,arr1):
    print(a,a1)

#queues are double ended addin is o(1)
from collections import *
queue= deque()
queue.append(1)
queue.append(2)
print(queue)
queue.pop()


# hash sets all search are constante o(1) and remove 

set = set()
set.add(5)
set.add(40)
print(5 in set)
print(7 in set)
print(set)
print(len(set))


#hashmaps== dictonarry search is o(1) and remove also 

map={}
map["name"]= "samir"

print("name" in map)
print("samir" in map.values())

for key,val in map.items():
    print(key,val)
    
    
#tuples list of immutable you can index them you can use them as keys in hashmaps


h={(1,20):50}
print(h[(1,20)])


# heaps for fast sorting and find max min 

import heapq

heapq.heapify(arr1)
while arr1:
    print(heapq.heappop(arr1))

