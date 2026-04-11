#Program to swap two variables
a=int(input("Enter a value: "))
b=int(input("Enter b value: "))
#dispalying the values of a and b
print("a={} \n b={}".format(a,b),end='\n')
#Swapping the values using temp variable
temp=a
a=b
b=temp
print("after swapping the new values are",end='\n')
print("a={} \n b={}".format(a,b),end='\n')
