def sum():
	a=int(input("Enter the first number"))
	b=int(input("Enter the second number"))
	print(a+b)
def mul():
	a=int(input("Enter the first number"))
	b=int(input("Enter the second number"))
	print(a*b)
def div():
	a=int(input("Enter the first number"))
	b=int(input("Enter the second number"))
	print(a/b)
def sub():
	a=int(input("Enter the first number"))
	b=int(input("Enter the second number"))
	print(a-b)
print("Enter /1(sum)/2(mul)/3(div)/4(sub)")
i=int(input("choice:"))
if i==1:
	print(sum())
elif i==2:
	print(mul())
elif i==3:
	print(div())
elif i==4:
	print(sub())
else:
	print("galat choice")