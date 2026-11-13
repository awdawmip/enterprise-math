"""R46 pinned S23/AV exact 389-source suffix compiler (stdlib, no learned age table)."""
from bisect import bisect_right
from hashlib import sha256
from io import StringIO
from csv import DictWriter
D=10**24
LO,HI=262204504569236716045286,262204504569236716045287
M,H,END=128,389,10**12+128

def ph(t,T):return t*T%D

def gaps(s):return [s[k+1]-s[k] for k in range(len(s)-1)]+[D+s[0]-s[-1]]

def stages():
    a,i,c,j=0,1,1,1
    def below(p,q):
        if p*D<q*LO:return True
        if p*D>q*HI:return False
        raise ArithmeticError('ambiguous Farey decision')
    while i+j<=M:
        if below(a+c,i+j):a,i=a+c,i+j
        else:c,j=a+c,i+j
    n0=M
    while n0<=END:
        s=i+j
        yield n0,min(s,END),s,a,i,c,j
        if s>=END:break
        if below(a+c,s):a,i=a+c,s
        else:c,j=a+c,s
        n0=s+1

def amplitude(a,i,c,j):
    if i*HI-a*D<c*D-j*HI:return (-a,i)
    if c*D-j*LO<i*LO-a*D:return (c,-j)
    raise ArithmeticError('ambiguous short-gap value')

def generate():
    # The strict-cover inequality holds throughout [LO/D,HI/D].
    order_lo=sorted(range(H),key=lambda t:ph(t,LO))
    order_hi=sorted(range(H),key=lambda t:ph(t,HI))
    assert order_lo==order_hi
    history=[]
    for T in (LO,HI):
        hist=sorted(ph(t,T) for t in range(M))
        block=sorted(ph(t,T) for t in range(H))
        assert max(gaps(block))<min(gaps(hist))
        history.append(hist)
    result=[]
    def add(l,r,pair):
        if l>r:return
        if result and result[-1][1]+1==l and result[-1][2]==pair:
            result[-1]=(result[-1][0],r,pair)
        else:result.append((l,r,pair))
    count=0
    for n0,n1,s,a,i,c,j in stages():
        ages=[]
        for T,hist in zip((LO,HI),history):
            last={}
            for t in range(j-H,j):
                last[(bisect_right(hist,ph(t,T))-1)%M]=t
            assert len(last)==M
            ages.append(sorted(j-t for t in last.values()))
        assert ages[0]==ages[1],('source owner differs at enclosure endpoints',s)
        events=sorted(s-r+1 for r in ages[0] if max(M+1,n0)<=s-r+1<=n1)
        count+=len(events)
        pair=amplitude(a,i,c,j) if events else (0,0)
        p=max(M+1,n0)
        for t in events:
            add(p,t-1,(0,0));add(t,t,pair);p=t+1
        add(p,n1,(0,0))
    buf=StringIO(newline='')
    w=DictWriter(buf,fieldnames=['n0','n1','A0','B0','dA','dB'],delimiter='\t',lineterminator='\n')
    w.writeheader();A=B=0
    for l,r,(da,db) in result:
        w.writerow(dict(n0=l-1,n1=r,A0=A,B0=B,dA=da,dB=db))
        A+=(r-l+1)*da;B+=(r-l+1)*db
    raw=buf.getvalue().encode()
    assert len(result)==298 and (A,B)==(-4017401528447,15321634290944)
    assert sha256(raw).hexdigest()=='2573a84999d53dfd1cce772c45a41abaff251da735171efe904c860f2b2294f6'
    print('PASS_R46_389_SUFFIX_298_RUNS',len(result),'updates',count,'sha256',sha256(raw).hexdigest())
    return raw

if __name__=='__main__':generate()
