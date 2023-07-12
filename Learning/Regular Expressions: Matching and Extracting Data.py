import re
x = "My 3 favorite numbers are 9, 12 and 42 "
y = re.findall ("[0-9]+",x) #finds one or more digit strings
print(y)
y = re.findall ("[AEIOU]+",x) #searchs for one or more upper case set of chracters
print(y)
y = re.findall ("[AEIOUM]+",x) #searchs for one or more upper case set of chracters
print(y)

print("-------\n")

import re
x = "From: Using the : character"
y = re.findall("^F.+:",x) # ^F = First character in the match is an F
                          # + = One or more charachters
                          #  : = Last charachter in the match is a :
print("Greedy > ", y)
i = re.findall("^F.+?:",x) # ^F = First character in the match is an F
                           # +? = One or more charachters but not greedy
                           #  : = Last charachter in the match is a :
print("Non-Greedy > ", i)

print("-------\n")

x = "From borayazgan2000@gmail.com Sat Jan 5 09:14:16 2023"

y = re.findall("\S+@\S+", x) # \S+....\S+ = At least one non-whitespace character 
print(y)

y = re.findall("^From \S+@\S+", x) # If there is no "From" before the mail it will not match
print(y)

y = re.findall("^From (\S+@\S+)", x) # The parenthesis indicates only the are we want to print
print(y)