#day 5 date 2019/10/15
#----------------------
#working with list
#=========================

magicians = ['olive','meem','sajid']
for magician in magicians:
	print(magician,end='\t')
	
for value in range(1,5):
	print(value)
	
numbers = list(range(1,10,3))
print (numbers)

digits = [11,2,3,4,5,26,7,18,90]
print("this is minimum value : {}".format(min(digits)))
print("this is maximum value : {}".format(max(digits)))
print("the sum of value : {}".format(sum(digits)))

print('\n')

players = ['Torun','Sourov','Asik','Rajib','pritom']
print(players [2:4])
print(players [0:2])
print(players [-1])
print(players [0:])
print(players [:])

print("\n")

#copy my plaers from list:

my_players = players [:]

print (my_players)
