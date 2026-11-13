"""R49 exact two-state Farey source-age compiler (stdlib, frozen S23 rotation)."""
from bisect import bisect_right
from collections import Counter
from csv import DictWriter
from io import StringIO
from hashlib import sha256
D=10**24; LO=262204504569236716045286; HI=LO+1
M=128; H=225; END=10**12+128
TARGET='2573a84999d53dfd1cce772c45a41abaff251da735171efe904c860f2b2294f6'
def ph(x,T):return x*T%D
def age(j,T):
    cuts=sorted(ph(z,T) for z in range(M)); vec=[0]*M
    for r in range(1,H+1):
        k=(bisect_right(cuts,ph(j-r,T))-1)%M
        if not vec[k]:vec[k]=r
        if all(vec):return tuple(vec),r
    raise AssertionError('incomplete owner coverage')
def stages():
    a,i,c,j=0,1,1,1
    def below(p,q):
        if p*D<q*LO:return True
        if p*D>q*HI:return False
        raise ArithmeticError('ambiguous Farey step')
    while i+j<=M:
        if below(a+c,i+j):a,i=a+c,i+j
        else:c,j=a+c,i+j
    n=M
    while n<=END:
        s=i+j;yield n,min(s,END),s,a,i,c,j
        if s>=END:break
        if below(a+c,s):a,i=a+c,s
        else:c,j=a+c,s
        n=s+1
def main():
    K=M+H-1
    # All 353 cut phases have stable order; 225 is the unique rightmost cut.
    for T in (LO,HI):
        assert max(range(K+1),key=lambda s:ph(s,T))==225
    assert all((k*LO)//D==(k*HI)//D for k in range(-291,225))
    assert all((k*LO)//D==(k*HI)//D for k in range(-K,K+1))
    fixed={};initial=0
    for j,h in ((61,225),(225,164)):
        v0,n0=age(j,LO);v1,n1=age(j,HI)
        assert v0==v1 and n0==n1==h
        fixed[j]=v0;initial+=n0+n1
    rows=list(stages());assert len(rows)==78 and initial==778
    # The upper Farey error v=c-j*theta decreases. At j=225 it enters
    # the rightmost cell [frac(225*theta),1), and stays there thereafter.
    previous=None
    result=[];usage=Counter()
    def add(l,r,v):
        if l>r:return
        if result and result[-1][1]+1==l and result[-1][2]==v:
            result[-1]=(result[-1][0],r,v)
        else:result.append((l,r,v))
    count=0
    for n0,n1,s,a,i,c,j in rows:
        if previous:
            pc,pj=previous
            for T in (LO,HI):assert 0<c*D-j*T<=pc*D-pj*T
        previous=(c,j)
        sel=61 if j==61 else 225
        assert j==sel or j>225
        if sel==225:
            for T in (LO,HI):assert 0<c*D-j*T<=59*D-225*T
        usage[sel]+=1
        ages=fixed[sel]
        ev=sorted(s-r+1 for r in ages if max(M+1,n0)<=s-r+1<=n1)
        count+=len(ev)
        if ev:
            if i*HI-a*D<c*D-j*HI:step=(-a,i)
            elif c*D-j*LO<i*LO-a*D:step=(c,-j)
            else:raise ArithmeticError('ambiguous amplitude')
        else:step=(0,0)
        p=max(M+1,n0)
        for t in ev:add(p,t-1,(0,0));add(t,t,step);p=t+1
        add(p,n1,(0,0))
    buf=StringIO(newline='');w=DictWriter(buf,fieldnames=['n0','n1','A0','B0','dA','dB'],delimiter='\t',lineterminator='\n');w.writeheader()
    A=B=0
    for l,r,(da,db) in result:
        w.writerow(dict(n0=l-1,n1=r,A0=A,B0=B,dA=da,dB=db))
        A+=(r-l+1)*da;B+=(r-l+1)*db
    raw=buf.getvalue().encode()
    assert usage=={61:2,225:76} and count==9697 and len(result)==298
    assert (A,B)==(-4017401528447,15321634290944)
    assert len(raw)==15356 and sha256(raw).hexdigest()==TARGET
    print('PASS_R49_TWO_STATES',dict(usage),'source_inspections_2_endpoints',initial)
    print('PASS_R49_298_RUNS',len(result),'events',count,'sha256',TARGET)
if __name__=='__main__':main()
