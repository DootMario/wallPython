#!/usr/bin/python

import sys
import os
import random

if __name__ == '__main__':
    path = os.path.dirname(os.path.abspath(__file__))

    last = ""
    try:
        with open(path+"/wallpy.conf", "r") as f:
            last = f.read()
    except FileNotFoundError:
        pass

    if len(sys.argv) > 3:
        print("Too many arguments")
        exit(1)

    if sys.argv[1] == "h" or sys.argv[1] == "help" or len(sys.argv) == 1:
        print("Wallpaper help\n"
              "h/help print this"
              "<directory> randomly sets a wallpaper from given directory\n"
              "<directory> <file> sets the given file from given directory as wallpaper")
        exit(0)

    if not os.path.isdir(sys.argv[1]):
        print("Not a directory")
        exit(2)
    if len(sys.argv)==3:
        if not os.path.isfile(sys.argv[1]+sys.argv[2]):
            print("Not a file")
            exit(3)
        if not (sys.argv[2].endswith(".jpg") or sys.argv[2].endswith(".png")):
            print("Not a jpg or png")
            exit(4)
        else:
            os.system(f"xwallpaper --zoom {sys.argv[1]}/{sys.argv[2]}")
            with open(path+"/wallpy.conf", "w+") as f:
                f.write(sys.argv[2])

    else:
        wall = random.choice([f for f in os.listdir(sys.argv[1]) if (f.endswith(".jpg") or f.endswith(".png")) and f != last])
        os.system(f"xwallpaper --zoom {sys.argv[1]}/{wall}")
        with open(path+"/wallpy.conf", "w+") as f:
            f.write(wall)

    exit(0)