#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv
    argsCount = len(argv) - 1

    if argsCount == 0:
        print("0 arguments.")
    elif argsCount == 1:
        print("1 argument:")
    else:
        print(f"{argsCount} arguments:")

    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
