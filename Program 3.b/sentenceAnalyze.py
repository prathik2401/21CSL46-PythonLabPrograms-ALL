#Write a Python program that accepts a sentence and find the number of words, digits,
#uppercase letters and lowercase letters.
s = input("Enter a sentence :")
w= d= u= l= 0
length = s.split()
w = len(length)
for c in s:
    if c.isdigit():
        d+=1
    elif c.isupper():
        u+=1
    elif c.islower():
        l+=1
print("Number of Words :",w)
print("Words :",length)
print("Uppercase Count :",u)
print("Lowercase Count :",l)
print("Number of digits :",d)