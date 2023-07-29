#Write a python program to find the best of two test average marks out of three test’s
#marks accepted from the user
m1 = int(input("Enter IA 1 Marks :"))
m2 = int(input("Enter IA 2 Marks :"))
m3 = int(input("Enter IA 3 Marks :"))
if m1<=m2 and m1<=m3:
    avgMarks = (m2+m3)/2
if m2<=m1 and m2<=m3:
    avgMarks = (m1+m3)/2
if m3<=m1 and m3<=m2:
    avgMarks = (m1+m2)/2
print("Average of Two tests : ",avgMarks)