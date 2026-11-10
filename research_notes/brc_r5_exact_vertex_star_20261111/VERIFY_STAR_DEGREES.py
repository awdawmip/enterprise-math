#!/usr/bin/env python3
"""Exact degree variation for the pinned R5 Blackwell vertex and its first star."""
from sympy import Matrix, Rational
from collections import Counter
r=list(map(Rational,['1/10','1/2','3/4','1','5/4','3/2','19/10']))
D=[(i,j) for j in (0,1,2,3,5,6) for i in range(7) if j not in (0,6) or i==j]
C=Matrix.hstack(*(Matrix([int(i==k) for k in range(7)]+[int(j==k) for k in range(7)]+[r[i] if j==k else 0 for k in range(7)]) for i,j in D))
M={(0,0):'219346331/10192753200',(0,1):'18669495/951323632',(1,1):'1898238/8493961',(5,1):'3733899/475661816',(2,2):'196521/2426846',(0,3):'8057361/237830908',(2,3):'1544855/16987922',(3,3):'377644447/2548188300',(4,3):'1544855/16987922',(5,3):'26530335/475661816',(6,3):'196521/67951688',(0,5):'196521/9707384',(6,5):'1375647/19414768',(6,6):'451274777/3397584400'}
x=Matrix([Rational(M[a]) if a in M else 0 for a in D])
R=C[list(C.T.rref()[1]),:];b=R*x
assert C.rank()==15 and R.rows==15 and R[:,[i for i,v in enumerate(x) if v>0]].rank()==14

def star(y,full=True):
    p=[k for k,v in enumerate(y) if v>0]
    z=[k for k,v in enumerate(y) if v==0]
    n=len(p)
    assert R[:,p].rank()==n and n in (14,15)
    if n==15:
        inv=R[:,p].inv()
        jobs=[((k,), (Rational(1),), -inv*R[:,k]) for k in z]
        signature=(15,0,0,len(z))
    else:
        piv=list(R[:,p].T.rref()[1]); Q=R[piv,p].inv()
        cf={k:Q*R[piv,k] for k in z}
        other=next(i for i in range(15) if any(R[i,k]!=(R[i,p]*cf[k])[0] for k in z))
        lam={k:R[other,k]-(R[other,p]*cf[k])[0] for k in z}
        zero=[k for k in z if lam[k]==0]
        neg=[k for k in z if lam[k]<0]
        pos=[k for k in z if lam[k]>0]
        signature=(14,len(neg),len(pos),len(zero))
        jobs=[((k,), (Rational(1),), -cf[k]) for k in zero]
        for k in neg:
            for l in pos:
                jobs.append(((k,l),(lam[l],-lam[k]), -cf[k]*lam[l]+cf[l]*lam[k]))
    if not full:return signature,len(jobs)
    ans=[]
    for adds,weights,old in jobs:
        d=Matrix.zeros(30,1)
        for k,v in zip(adds,weights):d[k]=v
        for k,v in zip(p,old):d[k]=v
        assert R*d==Matrix.zeros(15,1)
        t=min(y[k]/(-d[k]) for k in p if d[k]<0)
        nxt=y+t*d
        assert min(nxt)>=0 and R*nxt==b
        spp=[k for k,v in enumerate(nxt) if v>0]
        assert R[:,spp].rank()==len(spp)
        ans.append(nxt)
    return signature,ans

def main():
    sig,nb=star(x)
    print('CENTER',sig,'DEGREE',len(nb))
    stats=Counter()
    for j,y in enumerate(nb):
        sig,degree=star(y,False)
        stats[(sig,degree)]+=1
        print('NEIGHBOR',j,'SUPPORT',sig[0],'NEG',sig[1],'POS',sig[2],'ZERO',sig[3],'DEGREE',degree)
    assert len(nb)==18
    assert stats==Counter({((14,2,4,10),18):10,((15,0,0,15),15):8})
    print('FIRST_STAR_DEGREE_HISTOGRAM',dict(stats))
    print('PASS_EXACT_FIRST_STAR_DEGREE')

if __name__=='__main__':main()
