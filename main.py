name = 'Joe'
print('Hi, %s.' % name)

mylist = [1,2,3,4,4,5]
another_list = [6,7,8,9,10,10,11,16,21,34,56,21,44,23,44]

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

final_list.append ('\nOdd Number')
print (final_list)

final_list.pop()
print (final_list)


# Removing items in a list using index numbers with .pop
item = int (input("\nWhich index value do you want to remove? "))
print (f'\nYou entered index number {item} and we are going to remove it')

x = final_list[item]

item_range = item + 2
print (f'We are going to print a range from index {item, item_range}')
print (f'\nFinal list, range is {final_list[item:item_range]}')

print (f'The item we are removing is {final_list[item]}')
final_list.pop(item)

print (f'\nWe removed {item} from the list with a value {x}')
print (final_list)


# trying to find duplicates in final_list

print ('\n More attempts at duplicates here')

dupItems = []
uniqItems = {}
for x in final_list:
   if x not in uniqItems:
      uniqItems[x] = 1
   else:
      if uniqItems[x] == 1:
         dupItems.append(x)
      uniqItems[x] += 1
print(f'Duplicate numbers in final_list {dupItems}')
  

