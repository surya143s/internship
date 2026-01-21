#Palindrome
num = input("Enter a string: ")

if num == num[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")