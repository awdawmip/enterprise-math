#!/usr/bin/env python3
"""Exact integer/rational certificate for S23/AV seventh plateau.
The universal cell-coverage argument is in PROOF.md.
"""
from fractions import Fraction as F
Q=10**26; LO=545569623581288298975349314; HI=LO+1
H=2662891; V0=380295; K0=2074774

def logbounds(z):
    s=F(0); p=z
    for m in range(45):
        s+=2*p/(2*m+1); p*=z*z
    return s,s+2*p/(91*(1-z*z))

a,b=logbounds(F(1,3)); c,d=logbounds(F(1,9)); e,f=logbounds(F(1,15))
assert F(LO,Q)<(3*a-f)/(d+f) and (3*b-e)/(c+e)<F(HI,Q)

def enc(const,rcoef):
    return (const*Q+rcoef*(LO if rcoef>=0 else HI),
            const*Q+rcoef*(HI if rcoef>=0 else LO))

el,eu=enc(-431,79); tl,tu=enc(-60,11); gl,gu=enc(371,-68)
dl,du=enc(K0,-V0)
assert 0<dl<du<el and tl>4800*eu and gl>6*eu
assert eu*(H+79)<8*Q and 79*gu+eu*H<9*Q
assert 79*60-431*11==-1
print('PASS_LOG_BOUNDS',LO,HI,Q)

# For 0<gap<epsilon, b=79*gap-epsilon*dv is an integer in [-7,7].
# Exactly one integer a is possible for each nonzero b, since
# gap=a*epsilon+b*eta, with gap-width less than epsilon.
rows=[]
for beta in range(-7,8):
    if not beta: continue
    aa=abs(beta)*tl//eu; ab=abs(beta)*tu//el
    assert aa==ab
    alpha=-aa if beta>0 else aa+1
    dv=79*alpha+11*beta; dj=431*alpha+60*beta
    low,high=enc(-431*alpha-60*beta,79*alpha+11*beta)
    assert 0<low<high<el
    cost=max(max(dv,0)+max(dj,0),max(-dv,0)+max(-dj,0))
    if cost<=H: rows.append((beta,alpha,dv,dj,cost,low))
assert [x[:5] for x in rows]==[
    (-1,4815,380374,2075205,2455579),
    (1,-4814,-380295,-2074774,2455069)]
print('PASS_SUBEPS_DISPLACEMENTS',rows)

w=[]
for i in range(1,8):
    ai=i*dl//eu
    assert ai*eu<i*dl and i*du<(ai+1)*el
    v=i*V0+79*ai; k=i*K0+431*ai
    low,high=enc(k,-v)
    assert 0<low<high<el
    w.append((i,ai,v,k,low,high))
    print('WITNESS',i,'a',ai,'V',v,'K',k,'offset_num',low,high)
assert [t[1] for t in w]==[0,1,1,2,2,3,4]
V2=w[1][2]; V4=w[3][2]; V5=w[4][2]; V6=w[5][2]
V7=w[6][2]; K7=w[6][3]; M7=K7+V7-(V6+1)
assert (V7,K7,H,M7)==(2662381,14525142,2662891,14905515)
# All gaps in D_H exceed delta4. In v>V4, neither exceptional
# displacement can be embedded, hence all gaps are >=epsilon.
assert all(row[5]>w[3][5] for row in rows)
assert w[1][5]<w[3][5] and w[3][5]<el
assert H-(V4+1)<2074774 and H-2455579<V4+1
print('PASS_GLOBAL_AND_HIGH_V_GAP_BOUNDS')

blocks=[(0,V2,2),(V2+1,V4,4),(V4+1,V5,5),
        (V5+1,V6,6),(V6+1,V7,7)]
for start,end,i in blocks:
    _,_,v,k,low,high=w[i-1]
    assert v>=end and k>=H and k+v-start<=M7
    assert high<el if start>V4 else high<=w[3][5]
    print('PASS_WITNESS_BLOCK',start,end,i,'maxlen',k+v-start)

# For v>V7 the outgoing gap is >=gamma. A hypothetical
# 0<gap<gamma has b in [-7,8]. If b=0 its triangle-size
# increases by >=510. If b=1, dj<=-802; if b>=2,
# dj<-431*4800*(b-1)+60*b<-509; if b<=-1,
# dv> (79*4800-11)*(-b)>510. Each contradicts v>V7,j<=509.
assert 431*4800-60*8>509 and 79*4800-11>510
for m in range(1,7):
    L=V7+68+79*m; K=K7+371+431*m
    low,high=enc(K,-L)
    assert 0<low and high<gl
    if m==6: assert L>=H
assert K7+3498<=M7
print('PASS_TOP_ROW_AUXILIARY_WITNESSES',K7+3498)
left=H*Q//LO+1; right=HI*H//Q+1
assert LO*left>H*Q and right*Q>HI*H and max(left,right)<=M7
assert H-(V6+511)+1==380374
print('PASS_OUTER_CELLS',left,right)
print('PASS_S23_AV_PLATEAU7',V6+511,H,M7)
