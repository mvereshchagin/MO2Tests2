def main():
    ask_name_print_greeting()

def get_input():
    return input()

def ask_name_print_greeting():
    print('What is your name?')
    name = input()
    print('What is your surname?')
    surname = input()
    print(f'Hello, {name} {surname}')

def ask_name_print_greeting2():
    print('What is your name?')
    name = get_input()
    print('What is your surname?')
    surname = get_input()
    print(f'Hello, {name} {surname}')


def do_something():
    return 5


if __name__ == '__main__':
    main()


