#Task 1 = check if no. is even or odd
n=int(input("Enter a number:"))
if n%2==0:
    print(n,"is a even number")
else:
    print(n, "is a odd number")


#Task 2= sum of integer from 1 to 50 using loop
sum=0
for i in range(1,51):
    sum+=i
print("the sum of number 1 to 50 is :", sum)