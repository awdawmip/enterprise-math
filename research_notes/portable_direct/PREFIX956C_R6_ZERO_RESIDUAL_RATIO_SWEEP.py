#!/usr/bin/env python3
"""PREFIX956C: independent full Q19 zero-residual ratio enumeration, no prior pair list."""
import json, math
from collections import Counter
from pathlib import Path
P=19; H=1<<(P-1); TOP=2*H-1
def count(x,d):
    if d==0: return P-(x&((1<<P)-1)).bit_count()
    z=abs(d); u=(z&-z).bit_length()-1; q=z>>u
    mersenne=(q&(q+1))==0
    if d<0: return int(mersenne and u+q.bit_length()<P and not ((x>>(u+q.bit_length()))&1))
    n=int(mersenne and u+q.bit_length()<P and not ((x>>u)&1))
    if z.bit_count()==1:
        h=z.bit_length()-1
        n+=int(1<=h<=P and ((x>>(h-1))&1)!=0)
    elif z.bit_count()==2:
        v=(z^(1<<u)).bit_length()-1
        if v<P:n+=((x>>u)&1)+((x>>v)&1)
    return n

def direct(k,a,b):
    f=Counter(); x=k*a
    for i in range(P):
        for j in range(P):
            y=(x^(1<<j))-(1<<i)
            if y>0 and y%b==0: f[y//b]+=1
    return dict(f)

out={}; scanned={}; matched={}
for k,other in [(21,23),(23,21)]:
    inspected=0; hits=0
    for t in range(1,2*k+2,2):
        g=math.gcd(k,t); k0=k//g; t0=t//g
        low=max(H//k0,H//t0)+1
        high=min(TOP//k0,TOP//t0)
        for r in range(low+(low%2==0),high+1,2):
            a=t0*r; b=k0*r
            assert a*k==b*t and a%2==b%2==1
            if a==b:continue
            inspected+=1
            x=other*a
            Tmin=max(1,(x-2*H+b-1)//b)
            Tmax=(x+H-1)//b
            other_fibers=[(T,count(x,x-T*b)) for T in range(Tmin,Tmax+1)]
            other_fibers=[v for v in other_fibers if v[1]>0]
            if not other_fibers:continue
            assert direct(other,a,b)==dict(other_fibers)
            assert direct(k,a,b)=={t:count(k*a,0)}
            hits+=1
            out.setdefault((a,b),[]).append({'zero_core':k,'zero_quotient':t,
                'zero_source_count':count(k*a,0),'other_core':other,
                'other_quotient_fibers':other_fibers})
    scanned[str(k)]=inspected
    matched[str(k)]=hits
assert len(out)==16 and matched=={'21':9,'23':7} and all(len(v)==1 for v in out.values())
result={'schema':'PREFIX956C_ZERO_RATIO_DIRECT_Q19_V1',
 'scientific_input_commit':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'scanned_zero_core_offdiagonal_candidates':scanned,
 'matched_joint_zero_source_pairs_by_zero_core':matched,
 'distinct_joint_pairs':len(out),
 'pairs':[{'a':a,'b':b,'witnesses':w} for (a,b),w in sorted(out.items())],
 'method':'exact gcd ratio exhaustive candidates; bounded other-core quotient interval; formula and independent XOR direct verification',
 'independent_math_review':'PENDING'}
Path('PREFIX956C_R6_ZERO_RESIDUAL_RATIO_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
