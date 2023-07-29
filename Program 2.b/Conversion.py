def binaryToDecimal(binary):
    print("Given Binary Value:",binary)
    decimal,i = 0,0
    while(binary!=0):
        dec = binary%10
        decimal = decimal +dec*pow(2,i)
        binary//=10
        i+=1
        print("Decimal Value:",decimal)
binaryToDecimal(0b0011)
def octToHex(n):
    print("Octal =",n)
    decnum = int(n,8)
    hexadecimal = hex(decnum).replace("0x","")
    print("Hexadecimal value =",hexadecimal)
octToHex('5123')