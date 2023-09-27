
def nim_sum(numbers):
  total = 0
  for number in numbers:
    total ^= number
  return total

