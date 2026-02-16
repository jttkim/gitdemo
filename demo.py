#!/usr/bin/env python

v = [[1, 4, 5.5], [2, 6, 6.6]]

d = []
with open('demo.tsv', 'r') as f :
    hList = f.readline().strip().split()
    l = f.readline()
    while l != '':
        wList = l.strip().split('\t')
        d.append([float(w) for w in wList])
        l = f.readline()
print(hList)
print(d)
