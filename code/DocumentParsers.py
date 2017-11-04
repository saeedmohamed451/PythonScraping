#!/usr/bin/python
# -*- coding: utf-8 -*-


#
# Must remove special characters as we cannot have these
# in the CSV in order for it to parse correctly as it ingested
# in the next stages of data processing.
#
def cleanStringForCsv(dirtyString):

    # Start with the dirtyString and then clean it up.
    cleanString = dirtyString

    DIRTY_CHARACTERS_FOR_CSV = [",", "\", "\r", "\n", "\"", "\'"]

    for currentDirtyChar in DIRTY_CHARACTERS_FOR_CSV:
        cleanString = str(cleanString).replace(currentDirtyChar, "")

    return cleanString
