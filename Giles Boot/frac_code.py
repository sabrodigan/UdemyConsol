# frac code

# number_active this is the operator
# iterate from 1 to the num
# each time through add the value of operator * iterator
# fact = 1 - then
# fact = 1 + (1 * 2) = 3
# fact = 3 + (2 * 3) = 9
# fact = 9 + (3 * 4) = 21
# fact = 21 + (4 * 4) = 37 


fact = 1
num = int(input('Please enter a number? >>> '))

if num < 0:
	print('Come on man, you got to enter more than 0!')
elif num == 0:
	print('And entering a 0 is a dumb move!')
else:
	for i in range (1, num + 1):
		fact = fact * i
		print(f'\ni = {i} and fact now equals = {fact}')
		print(f'I did the following fact {fact} = {i} * {fact}')

print(f'Fractorial of {num} is {fact}')
print('END!')


