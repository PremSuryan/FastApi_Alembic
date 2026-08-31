# Reverse Integer:


"""
Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
"""

import re

x=str(x)
match = re.search(r'(-)(\d+)', x)
out=""
if match:
    sign = match.group(1)
    number = match.group(2)
    
    if sign:
        out += sign
        out += number[::-1]
else:
    out += x[::-1]

print(int(out))