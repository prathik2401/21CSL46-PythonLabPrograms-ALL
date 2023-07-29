#Defined as a function F as Fn = Fn-1 + Fn-2. Write a Python program which accepts a
#value for N (where N >0) as input and pass this value to the function. Display suitable
#error message if the condition for input value is not followed.
def fibonacci(n):
    if n<0:
        print("Incorrect input.")
    elif n==0:
        return 0
    elif n==1 or n==2:
            return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
#Edit the number in the next line to find the value in the fibonacci series.
print(fibonacci(8))