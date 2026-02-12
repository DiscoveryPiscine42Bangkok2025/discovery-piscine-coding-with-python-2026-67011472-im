import sys

argn = sys.argv[1:]
if not argn:
    print("none")
else:
    print(f"parameters: {len(argn)}")
    for arg in argn:
        print(f"{arg}: {len(arg)}")