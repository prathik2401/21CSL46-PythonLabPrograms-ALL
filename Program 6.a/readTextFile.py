inputFile = "textfile.txt"
n = int(input("Enter number of lines to be read from text file: ")) 
with open(inputFile, 'r') as filedata:
    linesList= filedata.readlines()
print("The following are the first",n,"lines of a text file:") 
for textline in (linesList[:n]):
    print(textline, end ='') 
filedata.close()
word=input("Enter the word to be searched:") 
k = 0
with open(inputFile, 'r') as f:
    for line in f:
        words = line.split() 
    for i in words:
        if(i==word): 
            k=k+1
print(f"Occurrences of the word {word} is:" , k )