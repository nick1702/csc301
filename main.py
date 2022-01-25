
def recursiveSum(n,total):
  if(n == 0):
    return total;
  else:
    return recursiveSum(n-1,total + n)

def main():
  n = 100
  total = 0
  print(recursiveSum(n,total))

