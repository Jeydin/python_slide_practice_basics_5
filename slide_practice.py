# Loops
# A loop is something that repeats or iterates through a specific 
# piece of code over and over to accomplish a certain goal.

# There are two types of loops
# WHILE LOOPS - loops that keep repeating as long as the given 
# condition is still true

# FOR LOOPS - loops that keep repeating for a specific number of times

# WHIELE LOOP EXAMPLE 1
print("WHILE LOOP EXAMPLE 1")
x = 0
while	x < 5:
	print(x)
	x += 1 
print()

# WHILE LOOP EXAMPLE 2
print("WHILE LOOP EXAMPLE 2")
answer = "yes"
while answer == "yes":
	answer = input("Keep Looping? Yes/No: ")
print()

# WHILE LOOP EXAMPLE 3
print("WHILE LOOP EXAMPLE 3 (Infinite)")
# x = 5
# while x > 0:
	# print(x)
	# x += 1
print()

# Infinite loops are bad

# FOR LOOPS

# FOR range() (Type 1)

# FOR LOOP EXAMPLE with range()
print("FOR LOOP with range()")
for x in range(10):
	print(x + 1)
print()

# Range gathers numbers STARTING WITH ZERO
# range(10) goes from 0-9

# FOR LOOP EXAMPLE (for each)
print("FOR LOOP example FOR EACH")
string = "4thPeriod_CompSciPrinciples"
for each in string:
	print(each)
print()

# HOW TO ACCESS DIGITS OF A NUMBER INDIVIDUALLY
# INTEGERS
inty1 = 9543
print(inty1 % 10) # 3
print(inty1 // 10) #954
inty1 //= 10 # 954
print(inty1 % 10) # 4
inty1 //= 10 # 95
print(inty1 % 10) # 5
inty1 //= 10 # 9
print(inty1 % 10) 

# Adding digits togethe
print()
print("Adding digits together")
num = 5643
total = 0
while num > 0:
	total += num % 10 # Pulls the last digit to add to total
	num = num // 10 # Chops off last digit
	print(total)

print("Final total:", total)

# NESTED LOOPS
print()
print("NESTED LOOPS EXAMPLE")
# LOOPS WITHIN LOOPS
x = 5
y = 0
while x > 0:
	while y < 3:
		print("Hello")
		y += 1
	x -= 1
	print("STOP")