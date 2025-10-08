number=int(input("Please enter a Number: "))

#Option 1: Only using the if-statement
if number > 0:
    print("Positive Number")
if number < 0:
    print("Negative Number")
if number == 0:
    print("Number is Zero")

# Option 2: Using if-else
if number > 0:
    print("Positive Number")
else:
    if number < 0:
        print("Negative Number")
    else:
        print("Number is Zero")

#Option 3: Using if - else- elif
if number > 0:
    print("Positive Number")
elif number < 0: 
    print("Negative Number")
else:
    print("Number is Zero")

#Option 4: Using a Conditional Expression
result="Positive Number" if number > 0 else \
    "Negative Number" if number < 0 else \
    "Number is Zero"
print(result)

#Option 5: Conditional Expression + Walrus Operator
print(result :="Positive Number" if number > 0 else \
    "Negative Number" if number < 0 else \
    "Number is Zero")

#Option 6: Match-Case Statement
match(number):
    case _ if number > 0:
        print("Positive Number")
    case _ if number < 0:
        print("Negative Number")
    case _:
        print("Number is Zero")

