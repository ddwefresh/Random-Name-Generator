import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

consonants = ['b', 'c', 'd', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
vowels = ['a', 'e', 'i', 'o', 'u']

lrange = [3,4,5,6,7,8,9,10]
doubles = [0,0,1]
ck = [0,1,1]

notfordouble = ['h', 'j', 'y', 'q', 'w', 'v', 'x']
print("Here's some names for your newborn:")

for i in range(10*999999999):
  long = random.choice(lrange)

  name = []
  for i in range(long):
    name.append("-")
  #print(name)

  while True:
    name[0] = random.choice(consonants)
    if name[0] != 'x':
      break

  doublec = random.choice(doubles)
  ckc = random.choice(ck)


  for i in range(long):
    b = i 
    if ckc == 1 and b == 3 and long != 3 and name[b-1] == 'c':
      name[b] = 'k'
    elif doublec == 1 and b == 3 and long != 4 and name[b-1] not in notfordouble:
      name[b] = name[b-1]
    elif name[b-1] in consonants:
      name[b] = random.choice(vowels)
    elif name[b-1] in vowels:
      name[b] = random.choice(consonants)

  finalname = ""
  name[0] = name[0].upper()
  for i in range(long):
    finalname = finalname + name[i]

  print('- ' + finalname)