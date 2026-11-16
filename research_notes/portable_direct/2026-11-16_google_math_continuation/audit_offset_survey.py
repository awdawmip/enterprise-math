"""Cartesian brute-force audit of the 20 triples at each threshold and predecessor."""
from fractions import Fraction as Q
from itertools import product
from math import lcm
import json
P=(455,-295,-25,185,-25,-295)
labels=range(6)
errors=list(product(range(-2,3),repeat=2))
top=1355
count,mark=[0]*top,[0]*top
count[0]=1
for label,w in enumerate((1,1,2,3,6)):
    for i in range(w,top):
        mark[i]+=mark[i-w]+(0 if label else count[i-w])
        count[i]+=count[i-w]
C,T=[0],[0]
for c,t in zip(count,mark):
    C.append(C[-1]+c)
    T.append(T[-1]+t)
def dist(r,J):
    codes=[[P[(b+j)%6] for j in J] for b in labels]
    obs=[[Q(108*q**3*(T[q]+e)-(18*q**4+54*q**3-345*q*q+2070*q-16315)*(C[q]+d),3*(C[q]+d)) for e,d in errors] for q in [r+j for j in J]]
    s=lcm(*(v.denominator for row in obs for v in row))
    return [[[abs(int(x*s)-k*s) for x in yy] for k,yy in zip(sig,obs)] for sig in codes]
def fails(r,J,mode):
    a=r%6
    D=dist(r,J)
    da=D[a]
    for b in labels:
        if b==a:continue
        db=D[b]
        if mode=='common':
            if any(max(db[0][i],db[1][i],db[2][i])<=max(da[0][i],da[1][i],da[2][i]) for i in range(25)):return True
        else:
            for ta,fa in zip(da[0],db[0]):
                for tb,fb in zip(da[1],db[1]):
                    tt=max(ta,tb);ff=max(fa,fb)
                    if any(max(ff,fc)<=max(tt,tc) for tc,fc in zip(da[2],db[2])):return True
    return False
if __name__=='__main__':
    rows=json.load(open('offset_survey.json'))
    n=0
    for row in rows:
        if len(row['J'])!=3:continue
        for mode in ('common','independent'):
            r=row[mode]['r']
            for v,expected in ((r,True),(r+1,False)):
                assert fails(v,row['J'],mode)==expected, (v,row['J'],mode)
                n+=1
    print('All',n,'triple boundary checks passed using direct Cartesian enumeration.')
