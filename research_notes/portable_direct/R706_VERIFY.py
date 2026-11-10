#!/usr/bin/env python3
"""R706: independent exact S3 shuffle DP and closed-form integer certificate."""
from collections import defaultdict
from math import comb, factorial
from pathlib import Path
import json

def mul(p,q): return tuple(p[q[i]] for i in range(3))
e=(0,1,2); a=(0,2,1); b=(1,0,2)
c=mul(a,b); ci=mul(b,a)
assert c!=ci and mul(c,c)==ci and mul(c,ci)==e
D={(0,0): {e:1}}
for n in range(1,97):
    for j in range(n+1):
        i=n-j
        if i>48 or j>48: continue
        w=defaultdict(int)
        if i>0:
            for g,k in D[(i-1,j)].items(): w[mul(g,a)]+=k
        if j>0:
            for g,k in D[(i,j-1)].items(): w[mul(g,b)]+=k
        D[(i,j)]=dict(w)

def term(k,l):
    return sum(factorial(k+l)//(factorial(k-r)*factorial(l-r)*factorial(2*r)) for r in range(min(k,l)+1))

checks=0; examples=[]
for k in range(25):
 for l in range(25):
    z=D[(2*k,2*l)]; C=comb(2*k+2*l,2*k); T=term(k,l)
    assert (C+2*T)%3==0 and (C-T)%3==0, (k,l)
    E=(C+2*T)//3; O=(C-T)//3
    assert z.get(e,0)==E and z.get(c,0)==O and z.get(ci,0)==O, (k,l,z,E,O)
    assert sum(z.values())==C
    assert (O>0)==(k>0 and l>0)
    checks+=1
    if (k,l) in [(1,1),(1,2),(2,2),(3,3),(4,4),(8,8),(12,12),(24,24),(1,24)]:
        M=comb(2*k,k)*comb(2*l,l)
        examples.append({"k":k,"l":l,"binary_shuffles":str(C),"D":str(T),"W_e":str(E),"W_c_each":str(O),"oriented_multiplier":str(M),"oriented_e":str(E*M),"oriented_c_each":str(O*M),"identity_bias_ratio": f"{T}/{C}"})
for k in range(1,25):
    assert term(k,k) <= 3**(2*k)
    assert term(k,k) <= comb(4*k,2*k)
j={"result":"R706_S3_SHUFFLE_CLOSED_FORM_PASS", "group_generators":{"A":a,"B":b,"AB":c,"BA":ci},"checked_even_count_pairs":checks,"domain":"0 <= k,l <= 24; exact integer DP and factorial-sum formula", "formula":"C=binom(2k+2l,2k); D=sum_{r=0}^{min(k,l)}(k+l)!/((k-r)!(l-r)!(2r)!); W_e=(C+2D)/3; W_AB=W_BA=(C-D)/3", "examples":examples}
with open(Path(__file__).with_name('R706_RESULTS.json'),'w') as f: json.dump(j,f,indent=2,ensure_ascii=False)
print(j['result'],checks,"pairs", "examples", examples)
