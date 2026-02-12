import sys

argn = sys.argv[1:]
if len(argn) != 1:
    print("none")
else:
    text = argn[0]
    zchar = [ch for ch in text if ch == "z"]
    if zchar:
        print("".join(zchar))
    else:
        print("none")