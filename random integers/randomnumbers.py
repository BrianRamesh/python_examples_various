
from random import randint
fw=open("5000_random_numbers_1_to_100.txt",'w')
# generate 5000 integers of 1-100
for _ in range(5000):
	value = randint(0, 100)
	print(value)
	fw.write(str(value)+"\n")


fw.close()