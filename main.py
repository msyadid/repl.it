def fizzBuzz(n):
  for z in range(n):
    i=z+1
    if (i%5==0) & (i%3==0) & (i!=1):
      print("FizzBuzz")
    if (i%3==0) & (i%5!=0):
      print("Fizz")
    if (i%5==0) & (i%3!=0):
      print("Buzz")
    if (i%3!=0) & (i%5!=0):
      print(i)

if __name__ == '__main__':
  n = int(input().strip())
  fizzBuzz(n)
