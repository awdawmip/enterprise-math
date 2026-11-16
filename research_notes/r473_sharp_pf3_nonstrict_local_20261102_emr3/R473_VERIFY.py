#!/usr/bin/env python3
"""Exact finite-range regression for the sharp PF3 criterion on strictly log-concave finite sequences.
Proof for arbitrary n is analytic (R473_PROOF.zh-CN.md); this script checks sample boundaries
and all positive integer sequences of lengths 3..6 with entries from {1,2,3,4}.
"""
from itertools import combinations, product
import json

def det3(a,b,c,d,e,f,g,h,i):
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)

def minor(seq, js):
    m=len(js);n=len(seq)-1
    z=lambda i,j: seq[j-i] if 0<=j-i<=n else 0
    if m==1:return z(0,js[0])
    if m==2:return z(0,js[0])*z(1,js[1])-z(0,js[1])*z(1,js[0])
    j0,j1,j2=js
    return det3(z(0,j0),z(0,j1),z(0,j2),z(1,j0),z(1,j1),z(1,j2),z(2,j0),z(2,j1),z(2,j2))

def d2(a,j):
    z=lambda h:a[h] if 0<=h<len(a) else 0
    return z(j)*z(j)-z(j-1)*z(j+1)

def d3(a,j):
    z=lambda h:a[h] if 0<=h<len(a) else 0
    return det3(z(j),z(j+1),z(j+2),z(j-1),z(j),z(j+1),z(j-2),z(j-1),z(j))

def ordinary_minors(a):
    n=len(a)-1
    return [minor(a,js) for m in (1,2,3) for js in combinations(range(n+m),m)]

# Sharp equality and nearby failure: all parameters integers, exact.
a0=(1,2,2);a1=(1,2,3)
v0=ordinary_minors(a0);v1=ordinary_minors(a1)
assert len(v0)==19 and min(v0)==0 and all(x>=0 for x in v0)
assert d2(a0,1)==2 and d3(a0,1)==0
assert len(v1)==19 and min(v1)<0 and d2(a1,1)==1 and d3(a1,1)==-4

stats=[]
for n in range(2,6):
    strict_d2=0;pf3=0;local_d3=0;first_bad=None
    for seq in product(range(1,5),repeat=n+1):
        if not all(d2(seq,j)>0 for j in range(n)):continue
        strict_d2+=1
        local=all(d3(seq,j)>=0 for j in range(n))
        global_criterion=all(v>=0 for v in ordinary_minors(seq))
        assert local==global_criterion,(n,seq,local,global_criterion)
        local_d3+=int(local);pf3+=int(global_criterion)
    stats.append({'n':n,'candidate_sequences':4**(n+1),'strict_d2_sequences':strict_d2,'local_d3_nonnegative':local_d3,'ordinary_schur_pf3':pf3})

out={
 'schema':'R473_SHARP_PF3_BOUNDED_ENUMERATION_V1','result':'R473_EXACT_PASS',
 'theorem':'positive finite sequence; strict D2 for j=0..n-1; PF3 iff D3>=0 for j=0..n-1',
 'domain':'n=2..5, all a_0..a_n in {1,2,3,4}; full enumeration of ordinary Schur minors of orders 1..3',
 'statistics':stats,
 'boundary_example':{'a':[1,2,2],'D2':[d2(a0,j) for j in range(3)],'D3':[d3(a0,j) for j in range(3)],'ordinary_minor_count':len(v0),'zero_ordinary_minors':sum(x==0 for x in v0)},
 'failure_example':{'a':[1,2,3],'D2':[d2(a1,j) for j in range(3)],'D3':[d3(a1,j) for j in range(3)],'negative_ordinary_minors':sum(x<0 for x in v1)},
 'status':'FINITE_REGRESSION_WITH_GENERAL_ANALYTIC_PROOF; AUTHOR_SIDE; UNREVIEWED; NOT_ADMITTED'
}
with open('R473_EVIDENCE.json','w',encoding='utf8') as f:json.dump(out,f,ensure_ascii=False,indent=2)
print(json.dumps(out,ensure_ascii=False,sort_keys=True))
