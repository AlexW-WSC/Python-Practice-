STRONG_PASSWORD_LENGTH = 10
special_chars = "!@#$%^&*()-+_=<>?/"
numbers = "1234567890"
uppercase_letters = "QWERTYUIOPASDFGHJKLZXCVBNM"
lowercase_letters = "qwertyuiopasdfghjklzxcvbnm"
password = None
print(" ")
print("Test your password strength~!")
print("-----" \
"")
print("DISCLAIMER: no data from this program is stored anywhere. The code for this script is publicly available through the GitHub link attached in the readme which should've come with this script. If there is no readme attached, this file may be compromised and you shoud proceed with your own risk in mind. Take care out there, internet stranger!")
print("-----" \
"")
print(" ")

password = input("What is your proposed password?").strip()

if len(password) >= STRONG_PASSWORD_LENGTH and any(i in uppercase_letters for i in password) and any(i in lowercase_letters for i in password) and (any(i in special_chars for i in password) or any(i in numbers for i in password)):
    print("You've got a long password({} characters), with a mix of cases, and a special character or number in there too. Great job!!".format(len(password)))
elif len(password) >= STRONG_PASSWORD_LENGTH and any(i in uppercase_letters for i in password) and any(i in lowercase_letters for i in password):
    print("This password is good, but maybe try putting a symbol (such as &), or a number (such as 4), in your password.")
elif len(password) >= STRONG_PASSWORD_LENGTH:
    print("Good start with the password length, but you should really try switching up the case, or adding special characters (symbols/numbers)")
else: 
    print("This password is too short. That should be your first concern; increasing the character length. Then make sure it's diverse as well, with different case and use of special characters.")

del(password)

