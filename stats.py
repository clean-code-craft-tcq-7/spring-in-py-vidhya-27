import math
def calculatevalid(numbers):
  valid_numbers = numbers
  for i in numbers:
    if math.isnan(i):
      valid_numbers.remove(i)
  return valid_numbers

def calculateStats(numbers):
  # implement the computation of statistics here and return the result
  valid_numbers = calculatevalid(numbers)
  if len(valid_numbers)<=0:
    return {"avg" : None, "max" : None, "min" : None}
  
  return {"avg" : (sum(valid_numbers)/len(valid_numbers)), "max" : max(valid_numbers), "min" : min(valid_numbers)}
