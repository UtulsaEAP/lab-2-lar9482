"""
    Name: Luke Runnels
    Lab time: February 2, 2024
"""

def simple_stats():
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    num4 = float(input())
    ''' Type your code here. '''

    product = num1*num2*num3*num4
    average = (num1+num2+num3+num4) / 4

    print(f'{product:.0f} {average:.0f}')
    print(f'{product:.3f} {average:.3f}')
if __name__ == "__main__":
    simple_stats()