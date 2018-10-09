def convertToDecimal(n):
    n = n.replace(" ", "")
    total = 0
    for i in range(len(n)):
        if (n[i] == "1"):
            total += pow(2,-(i+1))
    print(total)
    return (total)

def exponentToDecimal(n):
    n = n.replace(" ", "")
    total = 0
    print(n)
    for i in range(len(n)):
        if (n[len(n)-i-1] == "1"):
            total += pow(2,(i))
    print("Here " + str(total))
    total = total - 127
    print(total)

    return total

def getIEEENumber(sign, exponent, significant):
    sign = sign.replace(" ", "")
    total = 1.

    exponent = exponentToDecimal(exponent)
    significant = convertToDecimal(significant)
    total = total+significant
    total = total*pow(2, exponent)

    if (sign == "1"):
        total = total * -1
    print(total)

convertToDecimal("1000000")
exponentToDecimal("1000 0000")
getIEEENumber("0","01001001","01001100000000000000100")
getIEEENumber("1","010 1111 1","011 1111 0000 00000000 0000")
