""" Print module path names """

from __future__ import print_function
import sys
import importlib

def main():
    """ Main function """
    for mod_name in sys.argv[1:]:
        mod = importlib.import_module(mod_name)
        print(mod.__file__)

if __name__ == '__main__':
    main()
