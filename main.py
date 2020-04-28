#!/usr/bin/env python3

from sys import argv
from helium import *

search_site = 'site:stackoverflow.com '

search_phrase = search_site + argv[1]


if argv[2] == 'd':
    start_chrome('duckduckgo.com')

    write(search_phrase)

    press(ENTER)

    click('Any Time')

    click('Past Year')


elif argv[2] == 'g':
    start_chrome('google.com')

    write(search_phrase)

    press(ENTER)

    click('Tools')

    click('Any time')

    click('Past year')

else:

    print('Please enter d or g to choose the search engine')


