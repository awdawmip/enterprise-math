#!/usr/bin/env python3
"""Exact 1304-leaf certificate for Stage369-B; Python Fraction only."""
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha256
from pathlib import Path
import sys
w=(1,3,3,1);m=(61,21,9,9);lam=F(6,5)
R=(F(219,1000),F(239,1000),F(51,100),F(16,25))
S=(R[0],F(577,2500),R[2],R[3])
@lru_cache(None)
def B(k,z):return z**k*(1-z)**(3-k)
def r(k,x,y):return (4*B(k,x)+B(k,y))/5-F(m[k],160)
def b(x,y):return F(5,32)*sum(w[k]*abs(r(k,x,y)) for k in range(4))
def d(a,z):return sum(w[k]*abs(B(k,a)-B(k,z)) for k in range(4))/2
def c(x,y):return (63*d(F(1,4),x)+d(F(3,4),x)+9*d(F(1,4),y)+7*d(F(3,4),y))/256
@lru_cache(None)
def band(k,a,z):
    v=[B(k,a),B(k,z)];t=F(k,3)
    if a<t<z:v.append(B(k,t))
    return min(v),max(v)
def gap(v,a,z):return 0 if a<=v<=z else min(abs(v-a),abs(v-z))
def lb(x0,x1,y0,y1):
    X=[band(k,x0,x1) for k in range(4)]
    Y=[band(k,y0,y1) for k in range(4)]
    eb=F(5,32)*sum(w[k]*gap(F(m[k],160),(4*X[k][0]+Y[k][0])/5,(4*X[k][1]+Y[k][1])/5) for k in range(4))
    ports=[sum(w[k]*gap(B(k,a),z[k][0],z[k][1]) for k in range(4))/2 for a,z in ((F(1,4),X),(F(3,4),X),(F(1,4),Y),(F(3,4),Y))]
    ec=sum(q*v for q,v in zip((63,1,9,7),ports))/256
    return eb,ec
def cover(tag,rect,tgt):
    stack=[(*rect,0)];out=[];ns=0
    while stack:
        x0,x1,y0,y1,depth=stack.pop();eb,ec=lb(x0,x1,y0,y1);L=ec+lam*eb
        if L>tgt:out.append((tag,depth,x0,x1,y0,y1,eb,ec,L));continue
        assert depth<44
        ns+=1
        if 5*(x1-x0)>=y1-y0:
            mid=(x0+x1)/2;stack.extend([(x0,mid,y0,y1,depth+1),(mid,x1,y0,y1,depth+1)])
        else:
            mid=(y0+y1)/2;stack.extend([(x0,x1,y0,mid,depth+1),(x0,x1,mid,y1,depth+1)])
    assert len(out)==ns+1 and min(row[-1]-tgt for row in out)>0
    return out,ns
xl,xu=F(2310839,10**7),F(2310840,10**7)
yl,yu=F(5555086,10**7),F(5555091,10**7)
assert r(0,xl,yu)>0>r(0,xu,yl)
assert r(1,xl,yl)>0>r(1,xl,yu)
assert r(1,xu,yl)>0>r(1,xu,yu)
assert r(2,xl,yl)>0 and r(3,xu,yu)<0
bl=F(15,16)*r(2,xl,yl);bu=F(15,16)*r(2,xu,yu)
assert bl<bu and 2*bu+F(11,5000)<F(61,6250)
P=(F(231138,10**6),F(555681,10**6));Q=(F(237807,10**6),F(575694,10**6))
bref=b(*P)+b(*Q);cref=c(*P)+c(*Q)
assert bref==F(156126870406900413,16000000000000000000)
assert bref<2*bl+F(11,5000)
assert cref==F(16174439790495832521,256000000000000000000)
assert cref<F(6319,100000)
A,na=cover('R',R,F(373,10000));D,nd=cover('S',S,F(753,20000))
assert (na,len(A),max(z[1] for z in A))==(1190,1191,16)
assert (nd,len(D),max(z[1] for z in D))==(112,113,18)
assert F(373,10000)+F(753,20000)-lam*F(61,6250)-F(6319,100000)==F(3,62500)
fr=lambda z:f'{z.numerator}/{z.denominator}'
csv='region,depth,xlo,xhi,ylo,yhi,b_lower,c_lower,L_lower\n'
for tag,depth,x0,x1,y0,y1,eb,ec,L in A+D:
    csv+=','.join((tag,str(depth),fr(x0),fr(x1),fr(y0),fr(y1),fr(eb),fr(ec),fr(L)))+'\n'
assert sha256(csv.encode()).hexdigest()=='c60855319b26ba0e842906aa9126489568b001eef5945fd24247e64369f884d9'
assert len(csv.encode())==189212
if len(sys.argv)==3 and sys.argv[1]=='--emit':Path(sys.argv[2]).write_text(csv,encoding='utf-8')
else:assert len(sys.argv)==1
print('STAGE369B_EXACT_LEFT_STRIP_COST_EXCLUSION_PASS')
print('reference_b=',fr(bref),'budget_lower=',fr(2*bl+F(11,5000)))
print('reference_c=',fr(cref),'reference_upper=6319/100000')
print('R_leaves=1191 S_leaves=113 strict_gap=3/62500')
print('certificate_sha256='+sha256(csv.encode()).hexdigest())
