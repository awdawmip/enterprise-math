"""Direct Cartesian products at the 50 scalar threshold transitions."""
from fractions import Fraction as Q
from itertools import product
from math import lcm
import json
from pathlib import Path
J=(0,1,5); weights=(4,-5,1);phase=(3000,-600,-1320,840,1560,-3480)
parts=((0,0,0),(0,0,1),(0,1,0),(1,0,0),(0,1,2))
poly=[1]
for w in (1,1,1,2,3,6):
    v=poly+[0]*w
    for i,z in enumerate(poly):v[i+w]-=z
    poly=v
C=[0,1];T=[0,0]
for q in range(2,1601):
    C.append(-sum(poly[j]*C[q-j] for j in range(1,min(q,len(poly)-1)+1)))
    T.append(T[-1]+C[q-1])
def vals(p):return [tuple(x[g] for g in p) for x in product(range(-2,3),repeat=max(p)+1)]
def failed(r,ep,dp):
    s=r%6
    data=[{(e,d):w*(Q(q**3*(T[q]+e),C[q]+d)-Q(18*q**4+54*q**3-345*q*q+2070*q-16315,108)) for e,d in product(range(-2,3),repeat=2)} for q,w in zip((r+j for j in J),weights)]
    sc=lcm(36,*(v.denominator for table in data for v in table.values()))
    sig=[k*sc//36 for k in phase]
    tables=[{key:int(sc*v) for key,v in table.items()} for table in data]
    for e,d in product(vals(ep),vals(dp)):
        z=sum(t[x,y] for t,x,y in zip(tables,e,d))
        dist=abs(z-sig[s])
        if any(abs(z-v)<=dist for b,v in enumerate(sig) if s!=b):return True
    return False
if __name__=='__main__':
    tables=json.loads(Path(__file__).with_name('scalar_contrast_survey.json').read_text())['thresholds_denominator_rows_numerator_columns']
    for di,row in enumerate(tables):
        for ei,n in enumerate(row):
            assert failed(n-1,parts[ei],parts[di])
            assert not failed(n,parts[ei],parts[di])
    print('50 exact boundary audits passed with unoptimized Cartesian assignments.')
