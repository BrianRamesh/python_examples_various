
from random import randint
fw=open("5000_random_numbers_1_to_100.txt",'w') #create a file to store outputs
# generate 5000 integers of 1-100
for _ in range(5000):
	value = randint(0, 100)#in brackets are the minum wanted value and the maximum
	print(value)
	fw.write(str(value)+"\n")


fw.close()