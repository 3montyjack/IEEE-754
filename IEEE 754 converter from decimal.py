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

def getIEEENumber(value):
    value = value.replace(" ", "")
    sign = value[0]
    exponent = value[1:9]
    significant = value[9:33]

    total = 1.

    exponent = exponentToDecimal(exponent)
    significant = convertToDecimal(significant)
    total = total+significant
    total = total*pow(2, exponent)

    if (sign == "1"):
        total = total * -1
    print(total)

getIEEENumber("00100100101001100000000000000100")
getIEEENumber("10101111101111110000000000000000")
