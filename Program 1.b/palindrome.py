#Develop a Python program to check whether a given number is palindrome or not and
#also count the number of occurrences of each digit in the input number. 
n = int(input("Enter the number :"))
strn = str(n)
if strn == strn[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
for i in range (10):
    if strn.count(str(i))>0:
        print(str(i),"appears",strn.count(str(i)),"times.")