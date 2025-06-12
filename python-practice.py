user = int
count = 0;

evenInt = []

while count < 5:
  user = int(input())
  if user%2 == 0:
    evenInt.append(user)
  count+=1
  
print(evenInt)

