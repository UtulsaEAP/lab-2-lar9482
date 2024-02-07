"""
    Name: Luke Runnels
    Lab time: February 2, 2024
"""

def right_arrow():
    base_char = str(input())
    head_char = str(input())

    row1 = '      ' + head_char
    ''' Type your code here. '''
    row2 = ''
    row3 = ''
    for _ in range(0, 6): 
        row2 += base_char
        row3 += base_char
    
    row2 = row2 + head_char + head_char
    row3 = row3 + head_char + head_char + head_char
    
    print(row1)
    print(row2)
    print(row3)
    print(row2)
    print(row1)

if __name__ == "__main__":
    right_arrow()