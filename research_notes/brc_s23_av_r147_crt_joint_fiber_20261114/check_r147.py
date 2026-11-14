#!/usr/bin/env python3
"""R147 exact periodic fiber discrepancy: CRT-pair and variance checks."""
from fractions import Fraction as Q
from itertools import product
from math import gcd, lcm


def support(word):
    m=len(word)
    s=[0]
    for z in word: s.append(s[-1]+z)
    al=max([Q(0)]+[Q(s[j]-s[i]-1,j-i) for i in range(m) for j in range(i+1,m+1)])
    be=min([Q(1)]+[Q(s[j]-s[i]+1,j-i) for i in range(m) for j in range(i+1,m+1)])
    if al>=be: return None
    u=min(Q(s[j]+1)-j*al for j in range(m+1))
    ell=max(Q(s[j])-j*be for j in range(m+1))
    return al,be,u,ell


def floorq(q): return q.numerator//q.denominator

def ceilq(q): return -floorq(-q)


def verify(word):
    al,be,u,ell=support(word)
    a,b=al.numerator,al.denominator
    c,d=be.numerator,be.denominator
    U=int(u*b); V=int(ell*d)
    P=lcm(b,d); g=gcd(b,d); B=b//g; D=d//g
    h=u-ell
    assert Q(U,b)==u and Q(V,d)==ell
    mean_theory=h-Q(1,2*b)-Q(1,2*d)
    var_base=Q(b*b-1,12*b*b)+Q(d*d-1,12*d*d)
    m_x=Q(b-1,2*b); m_eta=Q(d-1,2*d)
    cov=Q(0)
    for t in range(g):
        rx=(a*t-U)%g
        ry=(c*t-V)%g
        cond_x=Q(B-1,2*B)+Q(rx,b)
        cond_eta=Q(D+1,2*D)-Q(ry,d)-(Q(1,D) if ry==0 else Q(0))
        cov+=(cond_x-m_x)*(cond_eta-m_eta)/g
    var_theory=var_base+2*cov
    errs=[]
    residues=set()
    for L in range(1,P+1):
        x=(L*a-U)%b; y=(L*c-V)%d
        residues.add((x,y))
        A=L*al-u; H=L*be-ell
        fibers=ceilq(H)-floorq(A)-1
        discrepancy=Q(fibers)-L*(be-al)
        eta=Q(0) if y==0 else 1-Q(y,d)
        assert discrepancy==h-1+Q(x,b)+eta
        errs.append(discrepancy)
    assert len(residues)==P
    inva=pow(a,-1,b) if b>1 else 0
    invc=pow(c,-1,d) if d>1 else 0
    expected={(x,y) for x in range(b) for y in range(d)
              if g==1 or ((inva*(x+U)-invc*(y+V))%g==0)}
    assert residues==expected,(word,residues,expected)
    avg=sum(errs,Q(0))/P
    variance=sum(((e-avg)**2 for e in errs),Q(0))/P
    assert avg==mean_theory,(word,avg,mean_theory)
    assert variance==var_theory,(word,variance,var_theory)
    if g==1: assert cov==0 and variance==var_base
    return g,cov,P,variance,var_base


def main():
    cnt=coprime=nonzero=cycles=0
    witness=None
    per_length=[]
    for m in range(1,12):
        count=0
        for word in product((0,1),repeat=m):
            if support(word) is None: continue
            g,cov,P,var,base=verify(word)
            count+=1;cnt+=1;cycles+=P
            coprime+=(g==1)
            nonzero+=(cov!=0)
            if witness is None and cov!=0:
                witness=(''.join(map(str,word)),m,g,str(cov),str(var),str(base))
        per_length.append((m,count))
    assert verify((0,1,0,1))[3]==Q(2,27)
    print('R147_CRT_FIBER_FLUCTUATION_PASS',dict(words=cnt,coprime=coprime,nonzero_joint_covariance=nonzero,residue_checks=cycles,first_witness=witness,per_length=per_length))
if __name__=='__main__': main()
