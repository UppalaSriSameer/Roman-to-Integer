def printRoman(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90,
           100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
           "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12

    while number:
        div = number // num[i]
        number %= num[i]

        while div:
            print(sym[i], end="")
            div -= 1
        i -= 1
a=0
while (a==0) :
    number = (input("Please enter the integer : "))
    if (number.isdigit()) and int(number) <= 1000 :
        print("Roman value is:", end=" ")
        printRoman(int(number))
        a+=1
    else:
        print("Please give an valid input, the input must be a integer less than or equal to 1000")