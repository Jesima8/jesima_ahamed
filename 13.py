name= int(input())

# take input from the user
# num = int(input("Enter a number: "))

# prime numbers are greater than 1
if name > 1:
   # check for factors
   for i in range(2,name):
       if (name % i) == 0:
           print("no")
           break
   else:
       print("yes")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print("no")
