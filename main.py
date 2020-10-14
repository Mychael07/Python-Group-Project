import ROOMS

# This is a sample Python script.
import random

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
guest_list = ["Jacob", "Castro", "Trevaughn", "Alessandra", "Jackson", "John", "William"]
guest = 6
killer = 0


def setup():
    global killer
    global guest
    guest -= 1
    print("party ")
    print(guest_list)
    killer = random.randint(0, guest)
    print(killer)


def kill():
    global killer
    while True:
        r = random.randint(0, guest)
        if r != killer:
            s = guest_list[r]
            guest_list.pop(r)
            print(s + " Has DIED")
            break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Welcome! Let's start!")
    setup()
    ROOMS.accepted_invitation()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
