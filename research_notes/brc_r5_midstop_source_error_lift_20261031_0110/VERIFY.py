#!/usr/bin/env python3
"""Exact independent integer enumeration of source-sensitive middle STOP error."""
from fractions import Fraction as F
from itertools import product, permutations
from math import lcm

Q={(0,0):F(3,8),(0,1):F(1,8),(1,0):F(1,8),(1,1):F(3,8)}
RU=(F(3,4),F(5,4))
RV=(F(1,2),F(1),F(3,2))
t=F(1,8)
eta={(0,0):F(1,4),(1,0):F(3,4),(0,1):F(1,3),(1,1):F(2,3)}
eps=F(1,100)
d=[F(1,2)-eta[x,0] for x in range(2)]
ell=(5-2*t)/(6-4*t)
dbar=(3*d[0]+d[1])/4
lam=ell+eps*RU[0]*dbar/(F(3,2)-t)

def K(u):
    return (F(1,2)+t,F(1,2)-2*t,t) if u==0 else (t,F(1,2)-2*t,F(1,2)+t)

leaves=[]
for x,u,v in product(range(2),range(2),range(3)):
    q=Q[x,u]*K(u)[v];p=RV[v]*q
    assert p>0 and q>0
    leaves.append((x,u,v,p,q))
assert sum(z[3] for z in leaves)==sum(z[4] for z in leaves)==1
for u in range(2):
    assert sum(K(u)[v]*RV[v] for v in range(3))==RU[u]
assert lam==F(3803,4400),lam
assert sum(Q[x,0]*((F(3,2)-t)*(ell-lam)+eps*RU[0]*d[x]) for x in range(2))==0
assert ((F(3,2)-t)*(ell-lam)+eps*RU[0]*d[0])==F(3,3200)
assert ((F(3,2)-t)*(ell-lam)+eps*RU[0]*d[1])==-F(9,3200)
assert F(5,6)<lam<F(9,10)

D=lcm(*(z.denominator for x,u,v,p,q in leaves for z in (p,lam*q,eps*p*F(1,2),eps*p*eta[x,0],eps*p*eta[x,1])))
for x,u,v,p,q in leaves:
    assert (D*p).denominator==1 and (D*lam*q).denominator==1
    assert (D*eps*p*F(1,2)).denominator==1 and (D*eps*p*eta[x,0]).denominator==1
states=[(x,u,v,int(D*p),int(D*lam*q),int(D*eps*p*F(1,2)),int(D*eps*p*eta[x,0]),int(D*eps*p*eta[x,1])) for x,u,v,p,q in leaves]

def brute(full):
    n=18 if full else 7
    best=None;bestbits=None
    for bits in range(1<<n):
        total=0
        for x,u,v,p,lamq,half,err,err1 in states:
            early=(bits>>x)&1
            middle=(bits>>(2+2*x+u))&1 if full else (bits>>(2+u))&1
            last=(bits>>(6+6*x+3*u+v))&1 if full else (bits>>(4+v))&1
            time=2 if not early else (3 if not middle else (4 if not last else 5))
            total+=time*(p-lamq)+((err if u==0 else err1) if early and not middle else half)
        if best is None or total>best:
            best=total;bestbits=bits
    return F(best,D),bestbits

full,fbits=brute(True)
lr,lbits=brute(False)
actual=full-lr
pred=F(9,128)*eps*abs(eta[0,0]-eta[1,0])
assert actual==pred==F(9,25600),(actual,pred)
dist=actual/(1+lam+eps)
assert dist==F(33,175936)

def obs(bits,full):
    eP=eQ=TP=TQ=F(0)
    for x,u,v,p,q in leaves:
        early=(bits>>x)&1
        middle=(bits>>(2+2*x+u))&1 if full else (bits>>(2+u))&1
        last=(bits>>(6+6*x+3*u+v))&1 if full else (bits>>(4+v))&1
        ti=2 if not early else (3 if not middle else (4 if not last else 5))
        er=eta[x,u] if ti==3 else F(1,2)
        eP+=p*er;eQ+=q*er;TP+=p*ti;TQ+=q*ti
    return eP,eQ,TP,TQ

def det4(rows):
    total=F(0)
    for perm in permutations(range(4)):
        inversions=sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
        val=F(-1) if inversions%2 else F(1)
        for i,j in enumerate(perm): val*=rows[i][j]
        total+=val
    return total

base=obs(0,False)
ranks=[1,2,5,6]
vectors=[[obs(k,False)[j]-base[j] for j in range(4)] for k in ranks]
det=det4(vectors)
assert det==F(3,32768)
assert full==obs(fbits,True)[2]-lam*obs(fbits,True)[3]+eps*obs(fbits,True)[0]
assert lr==obs(lbits,False)[2]-lam*obs(lbits,False)[3]+eps*obs(lbits,False)[0]
assert fbits==200111 and lbits==107
print('FULL witness (eP,eQ,TP,TQ)=',obs(fbits,True))
print('LR maximizer (eP,eQ,TP,TQ)=',obs(lbits,False))
print('LR rank4 determinant=',det,'LR comparison bitmasks=',ranks)
print('Q normalized=P normalized=1; strict 12-leaf positivity and conditional likelihood identities: PASS')
print('lambda=',lam,'epsilon=',eps,'t=',t,'eta=',eta)
print('FULL exact support=',full,'policy_bitmask=',fbits,'policies=',1<<18)
print('LR exact support=',lr,'policy_bitmask=',lbits,'policies=',1<<7)
print('gap=',actual,'formula=',pred,'L_infinity_distance_bound=',dist)
print('PASS_EXACT_R5_STAGE3_SOURCE_SENSITIVE_STOP_ERROR_NO_GO')
