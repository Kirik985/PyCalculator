import sys
print("Welcome to PyCulator version: 0.3!")
print("1) Enter the first number")
print("2) Then enter operation")
print("3) Enter the second number")
print("4) Get the answer")
a_float = False
while(not(a_float)):
	a = input("a: ")
	try:
		a = float(a)
		a_float = True
	except ValueError:
		print("Enter a number!")
mode_right = False
while(not(mode_right)):
	mode = input("mode: ")
	if (mode == "+" or mode == "-" or mode == "/" or mode == "*"):
		mode_right = True
	else:
		print("Enter valid operation!")
b_float = False
while(not(b_float)):
	b = input("b: ")
	try:
		b = float(b)
		b_float = True
	except ValueError:
		print("Enter a number!")
if (mode == "+"):
    result = a + b
elif (mode == "-"):
    result = a - b
elif (mode == "*"):
    result = a * b
elif (mode == "/"):
    if (b == 0):
    	print("Division by zero!")
    	input()
    	sys.exit()
    			
    elif (b != 0):
    	result = a / b
print(str(a) + " " + mode + " " + str(b) + " = " + str(result))
print("Thanks for using PyCulator! Press any key to exit...")
input()
sys.exit()
