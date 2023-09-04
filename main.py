while True:
    chooseNumber = int(input("What problem do you want to solve from 1-5? (0 for exit): "))
    match chooseNumber:
        case 1:
        # Number 1
            def celsiusToFahrenheit():
                celsius = float(input("Enter a float number for Celsius: "))
                fahrenheit = celsius * (9 / 5) + 32
                return f"{fahrenheit:.2f}"

            print("The temperature from Celsius to Fahrenheit is: " + celsiusToFahrenheit() + ".")
        case 2:
        #Number 2
            num1 = int(input("Enter number 1: "))
            num2 = int(input("Enter number 2: "))
            num3 = int(input("Enter number 3: "))

            if(num1 > num2 and num2 > num3):
                print(f"The maximum number among the three is {num1}.")
            elif(num2 > num1 and num2 > num3):
                print(f"The maximum number among the three is {num2}.")
            elif(num3 > num1 and num3 > num2):
                print(f"The maximum number among the three is {num3}.")
            else:
                print("All numbers are the same!")
        case 3:
        #Number 3
            givenNum = int(input("Please enter a number: "))

            numDigits = 0
            smallestNum = 9
            highestNum = 0

            if givenNum == 0:
                numDigits = 1
                smallestNum = 0
                highestNum = 0

            while(givenNum != 0):
                slicedNum = givenNum % 10
                numDigits += 1

                if(slicedNum < smallestNum):
                    smallestNum = slicedNum

                if(slicedNum > highestNum):
                    highestNum = slicedNum

                givenNum //= 10

            print("Number of digits in the given number: ", numDigits)
            print("Smallest number is: ", smallestNum)
            print("Highest number is: ", highestNum)
        case 4:
            num = int(input("Enter a number: "))
            sum = 0

            for totalNum in range(1, num + 1):
                sum += totalNum

            print(f"The sum of all numbers from 1 to {num} is: ", sum)









