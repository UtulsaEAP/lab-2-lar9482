def telephone():
    phone_number = int(input())
    ''' Type your code here. '''

    thirdNumber = phone_number % 10000
    secondNumber = (phone_number // 10000) % 1000
    firstNumber = (phone_number // 10000000)

    print('({0}) {1}-{2}'.format(firstNumber, secondNumber, thirdNumber))

if __name__ == "__main__":
    telephone()