name = 'Joe'
print('Hi, %s.' % name)

mylist = [1,2,3,4,4,5]
another_list = [6,7,8,9,10,10,11]

print (mylist)
print (another_list)

for num in mylist:
  if num == 4:
    print (f'Found your number {num}')

print ('\nYour list mylist has',len (mylist,),'in it')

for num in mylist:
  num = num + num
  print (num)

# I want to see if the values in the list are the same as each other

print (type (mylist))

for num in another_list:
  num = num **2
  print (num)

final_list = mylist + another_list
print (final_list)

final_list [0] = 99
final_list [3] = 'Even number'

print (final_list)

final_list.remove(4)
print (final_list)

final_list.append ('Odd Number')
print (final_list)

final_list.pop()
print (final_list)


# Removing items in a list using index numbers with .pop
item = int (input("Which index value do you want to remove?"))


print (final_list[item])
final_list.pop(item)
print (f'We removed {item} from the list')
print (final_list)


