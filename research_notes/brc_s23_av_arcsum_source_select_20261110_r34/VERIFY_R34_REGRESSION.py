"""R34 independent full-partition regression of floor-sum risk and source-select compiler."""
import VERIFY_R34_PORTABLE as r

def oracle(n,m):
    out=[]
    for T in (r.L,r.U):
        phase=sorted(range(n),key=lambda k:r.res(k,T))
        old=[k for k,t in enumerate(phase) if t<m]
        maxima=[]
        for i,k in enumerate(old):
            stop=old[(i+1)%m]
            if stop<=k:stop+=n
            opts=[]
            for p in range(k,stop):
                a,b=phase[p%n],phase[(p+1)%n]
                opts.append((a*T//r.D-b*T//r.D+int(r.res(b,T)<r.res(a,T)),b-a))
            maxima.append(max(opts,key=lambda x:r.value(x,T)))
        out.append((1-sum(a for a,b in maxima),-sum(b for a,b in maxima)))
    assert out[0]==out[1]
    return out[0]

def neighbor(n):
    p=(0,1,1,1)
    while p[1]+p[3]<n:
        a,q,c,j=p;v=a+c;d=q+j
        if v*r.D<d*r.L:p=r.step('L',1,p)
        elif v*r.D>d*r.U:p=r.step('U',1,p)
        else:raise AssertionError('uncertified-mediant')
    return p

def arcs(m):
    p=sorted(range(m),key=lambda k:r.res(k,r.L))
    assert p==sorted(range(m),key=lambda k:r.res(k,r.U))
    return [(p[i],p[(i+1)%m],int(r.res(p[i],r.L)>r.res(p[(i+1)%m],r.L))) for i in range(m)]

def floor_risk(n,m,hist):
    a,q,c,j=neighbor(n)
    assert q<=n and j<=n and q+j>=n
    groups=[(0,n-q,(-a,q)),(n-q,j,(c-a,q-j)),(j,n,(c,-j))]
    A=1;B=0
    for arc in hist:
        v=[]
        for lo,hi,exp in groups:
            ct=r.count(lo,hi,arc,r.L)
            assert ct==r.count(lo,hi,arc,r.U)
            if ct:v.append(exp)
        x,y=r.maxexpr(v);A-=x;B-=y
    return A,B

prefix,selected=r.prefix()
assert selected==223
prev=(0,0)
for n in range(129,390):
    want=next(v for l,h,v in prefix if l<=n<=h)
    x=r.risk(n)
    assert x==oracle(n,128),('independent',n,x)
    assert (x[0]-prev[0],x[1]-prev[1])==want
    prev=x
print('PASS_R34_261_INDEPENDENT_FULL_PHASE_SORTS_AND_PREFIX_INCREMENTS')
for m in (64,256):
    hist=arcs(m)
    for n in range(m,m+101):
        assert floor_risk(n,m,hist)==oracle(n,m),(m,n)
    print('PASS_R34_GENERIC_HISTORY',m,'101/101')
assert r.compile()[1]==298
print('PASS_R34_REGRESSION_COMPLETE')
