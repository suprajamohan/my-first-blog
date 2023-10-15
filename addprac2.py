# functions
def print_num(num1, num2):
    if type(num1) == int:
        print("num1 is integer")
    if type(num2) == int:
        print("num2 is integer")

    num3 = 8
    addition = num1 + num2 + num3
    num4 = 8
    # print(id(num3) == id(num4))
    print(num3 is num4)
    num4 = 10
    print(f'your value is {addition}')


if __name__ == '__main__':
    print_num(5, 3)
    print_num(3, 6)
