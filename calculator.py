a=int(input("Enter your first number"))
b=int(input("Ener your second number"))
op=input("Enter your op")
if op=='+':
	print(a+b)
elif op=='-':
	print(a-b)
elif op=='*':
	print(a*b)
elif op=='/':
	print(a/b)
else:
	print("invalid")