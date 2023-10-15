
# name, age = positional arguments
# day = keyword argument (default)
def print_hi(name, age, day="Monday"):
    if type(age) == int:
        greeting = "Hi"
        greeting = "Hello"
        print(f'{greeting}, {name}. You are {age}. Have a nice {day}')

    if type(age) != int:
        print('your argument is not integer')


if __name__ == '__main__':
    print_hi('Supraja', 'abc')
    print_hi('Visesh', 32, day="Tuesday")
