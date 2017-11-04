#!/usr/bin/python

OUTPUT_DIR='globalValue'


def verify():
    return 'verifyValue'

def scrape():
    print "Entered scrape."
    print OUTPUT_DIR


def main():

    OUTPUT_DIR=verify()
    print "In Main"
    print OUTPUT_DIR
    scrape()

main()
