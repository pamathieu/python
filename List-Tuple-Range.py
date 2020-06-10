'''
Mutable sequences:
    1) list, to store collections.
Immutable sequences:
    1) range()
    2) tuple()
'''

#ranges
start = 2
end = 20
step = 5
for i in range(start, end, step):
    print(i)

#lists, for homogenous values
iterable = range(5)
l = list(iterable)
l.append('a')
print(l)

#tuples
t = 'a','b','c'
print(t)

