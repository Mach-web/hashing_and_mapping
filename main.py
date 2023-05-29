# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    x = 'UDACITY'
    n= len(x)
    ascii_char_1 = ord(x[0])
    ascii_char_2 = ord(x[1])
    hash_value = (ascii_char_1 * (31 ** (n - 1))) + (ascii_char_2 * (31 ** (n - 2)))
    print(hash_value)
    print(ord('U'))
    print(ord('D'))
    print(8568-(ascii_char_1 * ascii_char_2))
    list1 = [None] * 10
    list1.append(323)
    print(list1)
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
