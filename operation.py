a = int(input('enter a number: '))
b = int(input('enter another number: '))
operation = input('enter operation (+, -, *, /): ')
if operation == '+':
    print(f'{a} + {b} = {a + b}')
elif operation == '-':          

    print(f'{a} - {b} = {a - b}')
elif operation == '*':
    print(f'{a} * {b} = {a * b}')
elif operation == '/':
    if b != 0:
        print(f'{a} / {b} = {a / b}')
    else:
        print('Error: Division by zero is not allowed.')
    print(f'{a} - {b} = {a - b}')
    print(f'{a} - {b} = {a - b}')               
elif operation == '*':
    print(f'{a} * {b} = {a * b}')
    print(f'{a} - {b} = {a - b}')
    