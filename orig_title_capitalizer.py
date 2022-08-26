from titlecase import titlecase
import pyperclip
from os import system, name


def clear():
    if name == 'nt':
        _ = system('cls')


while True:

    clear()

    print("[Python Title Capitalizer]")
    print("")

    string = input("Input title to capitalize: ")

    title = titlecase(string)
    print(title)
    pyperclip.copy(title)

    print("")

    keystone = input("Press Enter to reset. Type 'x' to exit. ")
    if keystone == "x":
        break
    else:
        continue
