import os
import random
import t


def remove_line_html(html,number_lines) :

    htmllines = html.splitlines()

    for line in range(number_lines):
        current = len(htmllines)
        random.seed(time.process_time())
        r = random.randint(0,len(htmllines)-1)
        del htmllines[r]

        now = len(htmllines)
        if(current!=(now+1)):
            print(r)

    return "\n".join(htmllines)
