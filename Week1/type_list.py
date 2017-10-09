
x= input("Please enter a list:")
sum=0
for i in x:
	if isinstance(i, int):
		sum=sum+i
	elif isinstance(i, str):
		print (i + " is part of a new string")
for	i in x:
	if all(isinstance(i, int) for i in x):
		print ("All integers")
	elif all(isinstance(i, str) for i in x):
		print("All strings")
	else:
		print("List is mixed")

print ("Running total of integers is: "+str(sum))