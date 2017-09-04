#!/usr/bin/env python


# l = [1, 2, 'abc', None]
# print [x for x in l]
# if None == []:
#     print "yes"
# else:
#     print "no"

# L = ['Hello', 'World', 18, 'Apple', None]
# print [s.lower() if isinstance(s, str) else s for s in L]
# print  [x for x in range(1, 11) if x % 2 == 0]
# n = (x for x in range(1, 11) if x % 2 == 0)
# for x in n:
#     print x

# def fib(max):				#generator
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#
# for x in fib(6):
#     print x
#
# for x in fib(10):
#     print x

import re

if "c" in r"[a-z]":
    print "True"
else:
    print "False"
