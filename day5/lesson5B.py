''''
if text expression:
  statment
  '''
players = ['Torun','Sourov','Asik','Rajib','Pritom']

for name in players :
	if name == 'Sourov':
		print(name.upper())
	else:
		print(name.lower())

age = 21

if age >= 18:
	print('your old enough to vote')
	print('have you register for vote yet')
else:
	print('sorry you are to too young')
	print('sorry')

print ('\n')

month = 1	
#month = int(input('plase enter month 1-3 : '))

if month == 1:
	print('jan')
elif month == 2:
	print('feb')
elif month == 3:
	print('mar')
else:
	print ('invalit month')
	
print ('\n')

print("\n\nThe  odd numbers are : \n")

for n in range(50):
	if n%2 == 1:
		print(n,end='\t')
		
print ('\n')
sum = 0
print("\n\nThe sum of number are : ",end='')

for n in range(0,11):
	sum = sum + n

print(sum, end='\t')