#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv) - 1

    if argc == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(argc, "" if argc == 1 else "s"))
        for i in range(1, argc + 1):
            print("{}: {}".format(i, argv[i]))
