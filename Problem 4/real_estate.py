
def real_estate():
    
    current_price = int(input())
    last_month_price = int(input())
    # Your code goes here
    changePrice = int((current_price - last_month_price))
    monthyMortage = (current_price * 0.051) / 12

    msgOne = 'This house is ${0}. The change is ${1} since last month.'.format(current_price, changePrice)
    msgTwo = 'The estimated monthly mortgage is $' + f'{monthyMortage:.2f}' + '.'

    print(msgOne)
    print(msgTwo)

if __name__ == "__main__":
    real_estate()