import re
lin = "From borayazgan2000@gmail.com Sat Jan 5 09:14:16 2023"
y = re.findall("@([^ ]*)", lin ) # @    = Look through the string until you find an at sign
                                 # [^ ] = Match non-blank character
                                 # *    = Match many of them                                 
print(y)

print()

y= re.findall("^From.*@([^ ]*)", lin) # If there is no "From" before the mail it will not match
                                      # ^    = Starting at the beginning of the line
                                      # From = Look for the string "From"
print(y)
 
print("-------\n")

x = "We just received $12.80 for cookies"
y = re.findall("\$[0-9.]+", x) # \$     = Find a real dollar sign
                               # [0-9.] = A digit or period
                               # +      = At least one or more
print(y)