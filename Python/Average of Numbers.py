'''Write a method, that gets an array of integer-numbers and return an array of the averages of each integer-number and his follower, if there is one.
If the array has 0 or 1 values or is null or None, your method should return an empty array.

Have fun coding it and please don't forget to vote and rank this kata! :-)'''

def averages(arr):
    return [(arr[x]+arr[x+1])/2 for x in range(len(arr or [])-1)]

# other

def averages(arr):
  if arr is None or len(arr) < 2:
    return []
  return [(arr[i] + arr[i+1]) / 2 for i in range(len(arr)-1) ]