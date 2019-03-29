#ad- compilable task
#factorial in python mini assignment

def rfactorial(n):
	if n == 1:
		return n
	else:
		return n*rfactorial(n-1)

num = input("What number do you want to take the factorial of? ")

if num < 0:
	print("Invalid because negative number")
elif num == 0:
	print("1")
else:
	print(rfactorial(num))
