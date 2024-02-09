#!/usr/bin/python3
import sys

if __name__ == "__main__":
    suma = sum(int(arg) for arg in sys.argv[1:])
    print(suma)
