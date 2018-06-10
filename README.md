moon.py is in the public domain, and available from:
    http://bazaar.launchpad.net/~keturn/py-moon-phase/trunk/annotate/head:/moon.py


1. Install ms to gain access to the DateTime module
    pip install egenix-mx-base



Manual editing:
    Had to add dummy category name, first category was empty. No idea what it was.

    Weka is having trouble processing streets that include apostrophes, such as O'Brian St. Manually removed the apostrophes.

    Entry 1602850 of 2001 to 2004 was missing a y coordinate, a year, and only had part of the last updated categories. Inserted subsititutes as best I could

    I encountered multiple instances throughout the files of "CTA ""L"" TRAIN" and "CTA ""L"" PLATFORM" that I replaced with CTA TRAIN and CTA PLATFORM as I saw in other entries. Weka seemed to be choking on the double quote spam.

    Entry 1513501 in 2001 to 2004 was an extra line of attribute descriptions with one extraneous field. I have no idea why it was there, and I removed it.
    
    Entry 1149094 in 2008 to 2011 was merged with what should have been entry 1149095. That made both entries partial, so I removed them.
