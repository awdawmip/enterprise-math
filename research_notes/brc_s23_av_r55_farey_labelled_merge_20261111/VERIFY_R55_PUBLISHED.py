"""R55 frozen S23: R54 circular-phase merge -> full 298-run risk compiler.
Exact integers only; frozen science 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
"""
from bisect import bisect_right
from csv import DictWriter
from io import StringIO
from hashlib import sha256
A=262204504569236716045286;B=A+1;D=10**24
m=128;H=225;N=10**12+128
REF='2573a84999d53dfd1cce772c45a41abaff251da735171efe904c860f2b2294f6'

def rank(p,q,K):
    a,i,c,j=0,1,1,1
    while i+j<=K:
        if (a+c)*q<p*(i+j):
            lo,hi=1,(K-i)//j
            while lo<hi:
                z=(lo+hi+1)//2
                if (a+z*c)*q<p*(i+z*j):lo=z
                else:hi=z-1
            a,i=a+lo*c,i+lo*j
        else:
            lo,hi=1,(K-j)//i
            while lo<hi:
                z=(lo+hi+1)//2
                if (c+z*a)*q>p*(j+z*i):lo=z
                else:hi=z-1
            c,j=c+lo*a,j+lo*i
    assert i*c-j*a==1 and i+j>K
    order=[];s=j
    for _ in range(K):
        order.append(s)
        s=s-i if s>i else s+j if s+j<=K else s+j-i
    assert s==j and len(set(order))==K
    return order

def merge_age(j,p,q):
    t0=min(0,j-H);end=max(m-1,j-1);K=end-t0
    cyc=[t0]+[t0+s for s in rank(p,q,K)[::-1]]
    current=next(t for t in reversed(cyc) if 0<=t<m)
    ages=[None]*m;scans=0
    for t in cyc:
        if 0<=t<m:current=t
        if j-H<=t<j:
            r=j-t;scans+=1
            if ages[current] is None or r<ages[current]:ages[current]=r
    assert scans==H
    return tuple(ages)

def oracle_age(j,p,q):
    hist=sorted(((z*p)%q,z) for z in range(m));hphase=[v for v,z in hist]
    ages=[None]*m
    for r in range(1,H+1):
        z=hist[bisect_right(hphase,((j-r)*p)%q)-1][1]
        if ages[z] is None:ages[z]=r
    return tuple(ages)

def stages():
    a,i,c,j=0,1,1,1
    def below(p,q):
        if p*D<q*A:return True
        if p*D>q*B:return False
        raise ValueError('parameter enclosure cannot certify Farey decision')
    while i+j<=m:
        if below(a+c,i+j):a,i=a+c,i+j
        else:c,j=a+c,i+j
    first=m
    while first<=N:
        s=i+j
        yield first,min(s,N),s,a,i,c,j
        if s>=N:break
        if below(a+c,s):a,i=a+c,s
        else:c,j=a+c,s
        first=s+1

def amplitude(a,i,c,j):
    if i*B-a*D<c*D-j*B:return -a,i
    if c*D-j*A<i*A-a*D:return c,-j
    raise ValueError('ambiguous amplitude')

def run():
    ages={}
    for j in (61,225):
        both=[merge_age(j,p,D) for p in (A,B)]
        assert both[0]==both[1] and all(x is not None for x in both[0])
        assert all(both[0]==oracle_age(j,p,D) for p in (A,B))
        ages[j]=both[0]
    lines=list(stages());assert len(lines)==78
    runs=[];event_count=0;audits=0
    def add(l,r,d):
        if l>r:return
        if runs and runs[-1][1]+1==l and runs[-1][2]==d:
            runs[-1]=(runs[-1][0],r,d)
        else:runs.append((l,r,d))
    for first,last,s,a,i,c,j in lines:
        key=61 if j==61 else 225
        assert j==61 or j>=225
        v=ages[key]
        for p in (A,B):
            assert v==oracle_age(j,p,D)
            audits+=1
        events=sorted(s-r+1 for r in v if max(m+1,first)<=s-r+1<=last)
        event_count+=len(events)
        d=amplitude(a,i,c,j) if events else (0,0)
        current=max(m+1,first)
        for t in events:
            add(current,t-1,(0,0));add(t,t,d);current=t+1
        add(current,last,(0,0))
    assert len(runs)==298 and event_count==9697 and audits==156
    buf=StringIO(newline='');out=DictWriter(buf,fieldnames=['n0','n1','A0','B0','dA','dB'],delimiter='\t',lineterminator='\n');out.writeheader()
    aa=bb=0
    for lo,hi,(da,db) in runs:
        out.writerow(dict(n0=lo-1,n1=hi,A0=aa,B0=bb,dA=da,dB=db))
        aa+=(hi-lo+1)*da;bb+=(hi-lo+1)*db
    raw=buf.getvalue().encode()
    assert (aa,bb)==(-4017401528447,15321634290944)
    assert len(raw)==15356 and sha256(raw).hexdigest()==REF
    print('PASS_R55_FULL',len(lines),'Farey stages',len(runs),'affine runs',event_count,'events',audits,'independent stage-oracle checks',len(raw),'TSV bytes',REF)
    return raw
if __name__=='__main__':run()
