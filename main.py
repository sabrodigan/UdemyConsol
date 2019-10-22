# This file will contain more list work
# I know that this ability is going to be critical

my_first = ['Stephen','Nella','Ellen','Jessica','Martha','Leia','Tilly']
my_middle = ['Andrew','LoPresti','Amy','Sarah','May','Marilyn','Mynt']

print (my_first)
print (my_middle)

print ('\n')

for name in my_first:
  if name [0] == 'S':
    print (f'{name}, definitely does being with S\n')
  else:
    print (f'{name} does not begin with S')

print ('\n')

for name in my_first:
  print (name)

# Tuple Unpacking

tup = [(1,2),(3,4),(4,5),(6,7),(7,8),(9,10)]

print (tup)

print ('\n')

for item in tup:
  print (item)

print ('\n')

for a,b in tup: # I do not need to use (a,b)
  print (a)
  print (b)
  print ('\n')

dic = {'k1':100,'k2':'Stephen','k3':999}
print (dic)

print ('\nNow pulling out Items and Keys\n')

for item in dic.items():
  print (item)

for item in dic.keys():
  print (item)
  if item == 'k2':
    print ('\n Found it!')
else:
  print (item)

# Unpacking the dictionary
print ('\nUnpacking the dictionary a bit now\n')

for key, value in dic.items():
  print (f'Dictionary shows {key}, {value}, inside')
  print ('\n')

for value in dic.values():
  print (f'Value is: {value}')
  print ('\n')


