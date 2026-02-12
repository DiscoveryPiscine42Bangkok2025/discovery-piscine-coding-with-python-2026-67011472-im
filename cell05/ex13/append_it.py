import sys

argn = sys.argv[1:]
if len(sys.argv) < 2:
    print("none")
else:
    for i in argn:
        if "ism" not in i:
            print(f"{i}ism")