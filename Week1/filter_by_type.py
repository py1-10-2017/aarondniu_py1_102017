#Assignment: Filter by Type
#Write a program that, given some value, tests that value for its type. Here's what you should do for each type:

#Integer
#If the integer is greater than or equal to 100, print "That's a big number!" If the integer is less than 100, print "That's a small number"

x = input("Enter a value:")
print x
type(x)

if x>=100:
	print "That's a big number!"
elif x<100:
	print "That's a small number!"

#String
#If the string is greater than or equal to 50 characters print "Long sentence." If the string is shorter than 50 characters print "Short sentence."

if len(x)>=50:
	print "Long sentence."
elif len(x)<=50:
	print "Short sentence."

#List
#If the length of the list is greater than or equal to 10 print "Big list!" If the list has fewer than 10 values print "Short list."
if len(x)>=10:
	print "Big list"
elif len(x)<=10:
	print "Short list"
