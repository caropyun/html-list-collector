###
# CS 3C Advanced Data Structures and Algorithms in Python
# Description:  This program parses a given html file and prints out
#               all the list elements in the html file.
#               Prints a list of lists.
# Solution File: carolynPyunLab6.py
# Date:  2/22/22
###

from ListCollector import ListCollector


def main():
    # Read the html file
    file = open("lists.html")
    lines = file.read().replace("\n","")
    file.close()

    # Parse and print elements as lists
    parser = ListCollector()
    parser.feed(lines)
    print(parser.getLists())


if __name__ == '__main__':
    main()

'''
[['An item', 'Another', 'And another one'], ['Item one', 'Item two', 'Item three', 'Item four']]
'''