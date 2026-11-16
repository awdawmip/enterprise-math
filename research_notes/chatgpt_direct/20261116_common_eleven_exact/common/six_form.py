"""Check the short explicit construction independently of the search."""
from itertools import product
from pathlib import Path

points = list(product(range(5), repeat=3))
index = {p:i for i,p in enumerate(points)}
large = {(0,0,0)}
for h,k in product((1,-1),repeat=2):
    large.update([(0,2*h,k), (h,0,2*k), (2*h,k,0)])
groups = []
for t in range(5):
    groups.append({((x+t)%5,(y-t)%5,(z-t)%5) for x,y,z in large})
small = {(0,0,1),(0,4,4),(1,1,4),(1,2,2),(2,0,0),
         (2,3,4),(3,0,2),(3,3,3),(4,1,3),(4,2,1)}
for _ in range(6):
    groups.append(small)
    small = {(z,x,-y%5) for x,y,z in small}
assert len(set.union(*groups)) == sum(map(len,groups)) == 125
code=list(map(int,Path(__file__).with_name("best11.txt").read_text().split()))
assert {frozenset(index[p] for p in g) for g in groups} == {frozenset(i for i,c in enumerate(code) if c==k) for k in range(11)}
print("PASS two-seed formula reproduces the entire partition up to label names")
