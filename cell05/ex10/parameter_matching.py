import sys
import re

if len(sys.argv) < 2:
    print("none")
else:
    text =input("What was the parameter? ")
    word = sys.argv[1]
    if word == text:
            print('Good job!')
    else:
        print("Nope, sorry...")    