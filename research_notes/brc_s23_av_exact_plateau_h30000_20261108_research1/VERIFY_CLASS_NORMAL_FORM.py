#!/usr/bin/env python3
"""Finite H=30000 unimodular normal-form certification against saved class CSV."""
import csv
from pathlib import Path
p=Path(__file__).with_name("CLASS_H30000.csv")
with p.open(newline="",encoding="utf-8") as handle:
    rows=list(csv.reader(handle))
kind,H,M,C=rows[0]
H,M,C=map(int,(H,M,C))
assert kind=="SUMMARY" and H==30000 and M==(H+1)*(H+2)//2 and C==78
counts={}
for row in rows[1:]:
    assert row[0]=="CLASS" and len(row)==7
    dv,dj,V,J,S,n=map(int,row[1:])
    assert (dv,dj) not in counts and n>0
    counts[dv,dj]=n
add=lambda a,b:(a[0]+b[0],a[1]+b[1])
scale=lambda k,v:(k*v[0],k*v[1])
f,g,w=(11,60),(2,11),(79,431)
assert f[0]*g[1]-f[1]*g[0]==1
assert add(scale(7,f),g)==w
families=[
    {w},
    {add(f,scale(-m,w)) for m in range(1,59)},
    {f},
    {add(scale(q,f),scale(-1,w)) for q in range(2,8)},
    {add(f,scale(-k,g)) for k in range(1,6)},
    {add(f,scale(-6,g))},
    {add(scale(2,f),scale(-11,g))},
    {(1,j) for j in range(5)},
]
union=set().union(*families)
assert len(union)==sum(map(len,families))==C
assert union==set(counts)
assert [len(x) for x in families]==[1,58,1,6,5,1,1,5]
assert [sum(counts[v] for v in group) for group in families]==[434874286,14946825,192721,30246,845,36,36,5]
assert sum(counts.values())==M-1
print("PASS_H30000_EXACT_UNIMODULAR_NORMAL_FORM",H,M,C)
print("FAMILY_COUNTS",*[sum(counts[v] for v in group) for group in families])
