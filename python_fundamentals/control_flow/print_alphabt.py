#!/usr/bin/env python3
alphabet = ""
for code in range(97, 123):
    letter = chr(code)
    if letter != 'q' and letter != 'e':
        alphabet += letter
print(alphabet)
