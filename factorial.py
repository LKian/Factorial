num = input("Enter a number to factorialize: \n")
factorial=1
for i in range(1,num+1):
	factorial=factorial*i
print "The factorial of",num,"is",factorial


usernum = input("Enter the number you want to factorialize: \n")
factorial = 1
i = 1
while(i<=num):
	factorial = factorial*i
	i=i+1
print "The factorial of",num,"is",factorial