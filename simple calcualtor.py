op = input ("Enter an operator: ")
num1 = input ("Enter fist number: ")
num1 = int (num1)
num2 = input ("Enter second number: ")
num2 = int (num2)
if op == "+" :
	result = num1 + num2
	print ("num1 + num2 = ",result)
elif op == "-" :
	result = num1 - num2
	print ("num1 - num2 = ",result)
elif op == "**" :
	result = num1 ** num2
	print ("num1 ** num2 = ",result)
elif op == "/"	:
	result = num1 / num2
	print ("num1 / num2 = ",result)
elif op == "*"	:
	result = num1 * num2
	print ("num1 * num2 = ",result)
elif op == "//" 	:
	result = num1 // num2
	print ("num1 // num2 = ",result)
else 	:
	print ("Operator is Wrong ")
print ("This program is a part of Paknejad Programming Universe")
input ("Press Enter for Exit")