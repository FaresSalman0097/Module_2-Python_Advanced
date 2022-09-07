import re
txt='Hello!, How are you ? \n Where are you from?\n Hello,I am good'
print(re.findall("^Hello",txt))    # strats with
print(re.findall("from\?$",txt))      # ends with - need to use \ before ? as ? is used as a specific condition in regex
print(re.findall("Hello.*",txt))      # Zero or more occurrences
print(re.findall("Hello.+",txt))         # One or more occurences
