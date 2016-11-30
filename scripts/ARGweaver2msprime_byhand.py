#!/usr/bin/env python3
"""test an example file from ARGweaver

start=0	end=10000
name	event	age	pos	parents	children
1	coal	122.586947411	0	2	n2,n1
2	coal	1545.31450861	0	4	n3,1
3	coal	12061.8085146	0	7	5,4
4	recomb	8051.70236778	536	3,5	2
5	coal	12061.8085146	0	3	6,4
6	recomb	8051.70236778	1033	5,7	n0
7	coal	26970.5983226	0		3,6
n0	gene	0.0	0	6	
n1	gene	0.0	0	1	
n2	gene	0.0	0	1	
n3	gene	0.0	0	2	

(see http://mdrasmus.github.io/argweaver/doc/ for format)

msprime input (http://msprime.readthedocs.io/en/stable/api.html#msprime.load_txt) has 
[start  end  node, child1,child2  time population]


"""
import sys
sys.path.insert(0,'../msprime/') # use the local copy of msprime in preference to the global one
from tempfile import NamedTemporaryFile
import msprime
from msprime_ARGweaver import ARGweaver_arg_to_msprime_txt
with open("../test_files/ARGweaver_test.arg", 'r+') as arg, \
     NamedTemporaryFile("w+") as msprime_in:
    ARGweaver_arg_to_msprime_txt(arg, msprime_in)
    ts = msprime.load_txt(msprime_in.name)
print("ORIGINAL")
print(" Tree:")
for t in ts.trees():
    print(t.interval, t)
print(" Coalescense records:")
for r in ts.records():
    print("{}".format(r))


print("MINIMAL")
subset = ts.simplify()
print(" Tree:")
for t in subset.trees():
    print(t.interval, t)
print(" Coalescense records:")
for r in subset.records():
    print("{}".format(r))
