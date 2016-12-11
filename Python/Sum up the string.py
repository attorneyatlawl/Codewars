# sum the numbers in a string; I couldn't solve this.

import re
def sum_from_string(string):
    d = re.findall("\d+",string)
    return sum(int(i) for i in d)