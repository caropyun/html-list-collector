###
# CS 3C Advanced Data Structures and Algorithms in Python
# Application: ListCollector Solution
# Solution File: ListCollector.py
# Date:  2/22/22
###
from abc import ABC
from html.parser import HTMLParser


class ListCollector(HTMLParser, ABC):
    def __init__(self):
        HTMLParser.__init__(self)
        self.counthead = -1  # Keeps track of whether in big list
        self.count = 0  # Keeps track of whether in small list
        self.data = []  # Total lists of all lists
        self.indivdata = []  # Individual lists

    # Returns list of all lists
    def getLists(self):
        return self.data

    def handle_starttag(self, tag, attrs):
        if tag == 'ul' or tag == 'ol':  # Update if start big list
            self.counthead = 1
        if tag == 'li':  # Update if start small list
            self.count = 1

    def handle_endtag(self, tag):
        if tag == 'ul' or tag == 'ol':  # Update if end of big list
            self.counthead = 0
        if tag == 'li':  # Update if end of small list
            self.count -= 1

    def handle_data(self, data):
        # If still in big list and small list
        if self.count and self.counthead:
            self.indivdata.append(data)
        # If out of big list
        if self.counthead == 0:
            # Add small list to big list
            self.data.append(self.indivdata)
            # Reset small list and counthead
            self.indivdata = []
            self.counthead = -1
