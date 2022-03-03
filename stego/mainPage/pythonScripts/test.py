import os
from remove_line import remove_line_html

with open(os.getcwd()+"\\responseContent.html") as fd:
    content = fd.read()
html_line_removed=remove_line_html(content)
print(html_line_removed)
