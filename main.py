from sys import argv
from helium import *

search_site = 'site:stackoverflow.com '

search_phrase = search_site + argv[1]

print(search_phrase)

start_chrome('google.com')

write(search_phrase)

press(ENTER)

click('Tools')

click('Any time')

click('Past year')
