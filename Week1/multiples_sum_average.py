#Multiples
#Part I - Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use a list to do this exercise.
for i in range(1,1000,2):
	print i

#Part II - Create another program that prints all the multiples of 5 from 5 to 1,000,000
for i in range(5,1000000,5):
	print i

#Sum list
#Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]
a=[1,2,5,10,255,3]
print sum(a)

#Average list
#Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]
a=[1,2,5,10,255,3]
print sum(a)/len(a)