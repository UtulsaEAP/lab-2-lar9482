
def caffeine():
    caffeine_mg = float(input())
    ''' Type your code here. '''
    sixHours = caffeine_mg / 2
    twelveHours = sixHours / 2
    twentyfourHours = twelveHours / 4

    msgOne = "After 6 hours: " + f'{sixHours:.2f}' + " mg"
    msgTwo = "After 12 hours: " + f'{twelveHours:.2f}' + " mg"
    msgThree = "After 24 hours: " + f'{twentyfourHours:.2f}' + " mg"
    
    print(msgOne)
    print(msgTwo)
    print(msgThree)

if __name__ == "__main__":
    caffeine()