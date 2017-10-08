#Find and Replace
words = "It's thanksgiving day. It's my birthday,too!"
print words.find('day')
print words.replace("day","month")

#Min and Max
x = [2,54,-2,7,12,98]
minimum=min(x)
maximum=max(x)
print minimum
print maximum

#First and Last
x=[2,54,-2,7,12,98]
print x[0]
print x[5]
newlist=x[0],x[5]
print newlist

#New List
x = [19,2,54,-2,7,12,98,32,10,-3,6]
y=sorted(x)
print y
zero=y[:len(y)/2]
one=y[len(y)/2:]
print zero, one