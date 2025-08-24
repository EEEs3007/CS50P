import pyfiglet
import random
import sys


def invalid():
    sys.exit("Invalid usage")


# put all the fonts in a list "diff_fonts"
figlst = list(pyfiglet.FigletFont.getFonts())
f = None
# the user puts in the code
# asks for input variable = input("Input: ")
if len(sys.argv) != 1 and len(sys.argv) != 3:
    invalid()
if len(sys.argv) == 3:
    if sys.argv[1] != "-f" and sys.argv[1] != "--font":
        invalid()
    if sys.argv[2] not in figlst:
        invalid()

word = input("Input: ")
# check for the command line;
# if "-f" or "--font" is included, match the font to the list and f string into the print function
if len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        chosen_font = sys.argv[2]
        f = pyfiglet.figlet_format(f"{word}", font=chosen_font)
# if not do random.choice from the list and then f string into the print function
elif len(sys.argv) == 1:
    f = pyfiglet.figlet_format(f"{word}", font=random.choice(figlst))

# print output
print("Output: ")
print(f)
