#!/usr/bin/env python
# -*- coding: utf-8 -*-

# print "hello,"
# print "中文"
# print len("中文"), "utf-8 -> 3"
# print len(u"中文"), "Unicode"
# print "%d, %f, %s, %x" % (1, 0.1, "string", 13)
# print "\n"
# for x in range(6):
#     print x

# def abcd(x = []):
#     x.append('end')
#     return x
# print abcd()
# print abcd()
# print abcd()
#
# x = 10
# abcd(x)
# print "%d + 10 = %d" % (x, a)
# print a



x = raw_input("type a string >")
b = x.lower()
y = {}
for a in b:
    if a in :
        if a in y:
            y[a] =  y[a] + 1
        else:
            y[a] = 1
    else:
        pass

l = []
for key in y.itervalue():
    l.append(value)
l.sort()

ans = []
for key1 in y:
    if y[key1] == l[-1]:
        ans.append(key1)

print ans.sort()



# l = [3, 4, 10, 1, 2, 3, 6, 1]
# l.sort()
# print l[-1]
