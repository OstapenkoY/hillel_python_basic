while True:
    a, b = int(input('First digit: ')), int(input('Second digit: '))
    op = input('+-/*: ')
    if op == '+':
        print(a + b)
    elif op == '-':
        print(a - b)
    elif op == '*':
        print(a * b)
    elif op == '/':
        print(a // b) if b != 0 else print('Сannot be divided by zero')
    l = input('continue (y/n)? ')
    if l == 'n':
        break
print('See you later')
        





