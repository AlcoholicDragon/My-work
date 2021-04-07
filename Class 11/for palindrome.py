x=str(input("Enter any string:"))
n=int(input("Enter any number:"))
if x==x[-1::-1]:
    print('The given string is a palindrome.')
else:
    print('The given string is not a palindrome.')
if n%7==0 or n%10==7:
    print("Is a Buzz Number.")
else:
    print('IS not a Buzz Number')
