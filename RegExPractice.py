import re

txt = "[[Guido van Rossum]] began working on Python in the late 1980s as a successor to the [[ABC (programming language)|ABC programming language]] and first released it in 1991 as Python&nbsp;0.9.0.<ref>{{Cite web|last=Rossum|first=Guido Van|date=2009-01-20|title=The History of Python: A Brief Timeline of Python|url=https://python-history.blogspot.com/2009/01/brief-timeline-of-python.html|access-date=2021-03-05|website=The History of Python|archive-date=5 June 2020|archive-url=https://web.archive.org/web/20200605032200/https://python-history.blogspot.com/2009/01/brief-timeline-of-python.html|url-status=live}}</ref>"

# text within the ref tag

# x = re.findall("<ref>.*</ref>", txt) #and re.findall("</ref>$",txt)
# print(x)
y = re.findall("\[\[.*\]\]", txt)
re.search()
print(y)