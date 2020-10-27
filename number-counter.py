import time
print("I can count to any number!")
num = int(input("Enter any number: "))
x = 0
while True:
  t1 = int(time.time())
  while True:
    if x <= num:
      print(x)
      x += 1
    else:
      break
  t2 = int(time.time())
  break
t3 = t2 - t1
print("I told you so! It took",t3,"seconds.")
