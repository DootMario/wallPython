#!/usr/local/bin

import sys
import os
import random

if __name__ == '__main__':
    if len(sys.argv) > 3:
        print("Too many arguments")
        exit(1)
    if not os.path.isdir(sys.argv[1]):
        print("Not a directory")
        exit(2)
    if len(sys.argv)==3:
        if not os.path.isfile(sys.argv[1]+sys.argv[2]):
            print("Not a file")
            exit(3)
        else:
            os.system(f"xwallpaper --maximize {sys.argv[1]}/{sys.argv[2]}")

    else:
        wall = random.choice(os.listdir(sys.argv[1]))
        os.system(f"xwallpaper --maximize {sys.argv[1]}/{wall}")

