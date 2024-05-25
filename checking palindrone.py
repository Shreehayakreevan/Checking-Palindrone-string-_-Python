print("Checking Palindrone String")
mystr=(input("Enter the String = "))
#reversing a string
rev=mystr[::-1]
if mystr == rev:
    print("It is a Palindrone string")
else:
    print("It is not an Palindrone string")
