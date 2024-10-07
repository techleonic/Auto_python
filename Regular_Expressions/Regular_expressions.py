
import re
filesnames = ["nov-12.txt", "nomvember-14","Oct-17", "Nov-22.txt"]

text = "Hi there you here exa_mple@example.com some more text and there another@example.dev"

#extrac all emials
# [a-z]+  one or more a to z characters
# [^ ]  ^ is a negation of what comes after it like " " eny character but space
#  .  means eny single character
#  \  it escapes meta character "\." instead of "." get single character. it get character that contents "."
# [] matches a single character or range of charters it doesn't matter de order
# + match one or more times, have to be least one elemt aftet "+"
# ? Matches xero 0r one time, zero elements ar allowed after de "?"
# * matches de element zero or more times, zero elements are allowed before "*"
# {m, n} matches times {3, 6} from 3  to 6 number of matches
# ^ matches the begging of a line or string
# $ matches the end of a line or string
#[^..] matches a single character or an range that is not contained within the brackets
#?:...|... or operatos
# () matches an optional expression

pattern = re.compile('[^ ]+@[^ ]+\\.[a-z]+')
matches = pattern.findall(text)
no_spaces = re.compile("[a-z]").findall(text)
print(matches)
print(no_spaces)