"""R34: exact interval floor-sum, per-arc last-gap source select and 298-run compiler.
Frozen S23/AV input 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Python 3 standard library only; all comparisons use exact integers.
"""
from hashlib import sha256
from io import StringIO
import csv
D=10**24; L=262204504569236716045286; U=L+1
M=128; N=10**12+M; H=164; Z=(0,0)

def fs(n,m,a,b):
    qa,a=divmod(a,m);qb,b=divmod(b,m);s=qa*n*(n-1)//2+qb*n
    while True:
        if a>=m:s+=(n-1)*n*(a//m)//2;a%=m
        if b>=m:s+=n*(b//m);b%=m
        y=a*n+b
        if y<m:return s
        n,b=divmod(y,m);m,a=a,m

def res(t,T):return t*T%D
p=sorted(range(M),key=lambda t:res(t,L))
assert p==sorted(range(M),key=lambda t:res(t,U))
arcs=[(p[k],p[(k+1)%M],int(res(p[k],L)>res(p[(k+1)%M],L))) for k in range(M)]

def count(lo,hi,arc,T):
    if lo>=hi:return 0
    a,b,w=arc;n=hi-lo
    x=fs(n,D,T,(lo-a)*T)-fs(n,D,T,(lo-b)*T)+n*(a*T//D-b*T//D+w)
    assert 0<=x<=n
    return x

def last(lo,hi,arc):
    assert count(lo,hi,arc,L)>0
    a,b=lo,hi
    while b-a>1:
        c=(a+b)//2
        if count(c,hi,arc,L):a=c
        else:b=c
    assert count(a,hi,arc,U)==1
    return a

def value(v,T):return v[0]*D+v[1]*T

def maxexpr(vs):
    best=vs[0]
    for v in vs[1:]:
        d0=value(v,L)-value(best,L);d1=value(v,U)-value(best,U)
        assert (d0>0 and d1>0) or (d0<0 and d1<0) or (d0==d1==0)
        if d0>0:best=v
    return best

def step(t,k,p):
    a,q,c,j=p
    if t=='L':a,q=a+k*c,q+k*j
    else:c,j=c+k*a,j+k*q
    assert c*q-a*j==1
    return a,q,c,j

def direction(p):
    a,q,c,j=p;x0=q*L-a*D;x1=q*U-a*D;y0=c*D-j*L;y1=c*D-j*U
    assert min(x0,x1,y0,y1)>0
    if x0>y0 and x1>y1:
        k=min(x0//y0,x1//y1)
        while min(x0-k*y0,x1-k*y1)<=0:k-=1
        return 'L',k
    if y0>x0 and y1>x1:
        k=min(y0//x0,y1//x1)
        while min(y0-k*x0,y1-k*x1)<=0:k-=1
        return 'U',k
    raise AssertionError('ambiguous interval direction')

def stages():
    p=(0,1,1,1);dec=0
    while p[1]+p[3]<=M:
        side,k=direction(p);h=p[3] if side=='L' else p[1]
        p=step(side,min(k,(M-p[1]-p[3])//h+1),p);dec+=1
    assert p==(27,103,16,61)
    z=[(M,min(p[1]+p[3],N),*p)]
    while z[-1][1]<N:
        e=p[1]+p[3];side,k=direction(p);h=p[3] if side=='L' else p[1]
        k=min(k,(N-e-1)//h+1)
        for s in range(1,k+1):z.append((e+(s-1)*h+1,min(e+s*h,N),*step(side,s,p)))
        p=step(side,k,p);dec+=1
    assert len(z)==78 and dec==28
    return z

STAGES=stages()

def risk(n):
    if n==M:return Z
    _,_,a,q,c,j=next(v for v in STAGES if v[0]<=n<=v[1])
    groups=[(0,n-q,(-a,q)),(n-q,j,(c-a,q-j)),(j,n,(c,-j))]
    A=1;B=0
    for arc in arcs:
        v=[]
        for lo,hi,expr in groups:
            ca=count(lo,hi,arc,L);cb=count(lo,hi,arc,U)
            assert ca==cb
            if ca:v.append(expr)
        x,y=maxexpr(v);A-=x;B-=y
    return A,B

def amplitude(a,q,c,j):
    x=(-a,q);y=(c,-j)
    if max(value(x,L),value(x,U))<min(value(y,L),value(y,U)):return x
    if max(value(y,L),value(y,U))<min(value(x,L),value(x,U)):return y
    raise AssertionError('interval crosses amplitude equality')

def push(z,l,r,v):
    if l>r:return
    if z and z[-1][1]+1==l and z[-1][2]==v:z[-1]=(z[-1][0],r,v)
    else:z.append((l,r,v))

def prefix():
    events={};selected=0;stagecounts=[]
    for n0,n1,a,q,c,j in STAGES[:3]:
        if n0>M:
            x=risk(n0);y=risk(n0-1);d=(x[0]-y[0],x[1]-y[1])
            if d!=Z:events[n0]=d
        ct=0;gap=amplitude(a,q,c,j)
        for arc in arcs:
            lo,hi=n0-q,j
            c0=count(lo,hi,arc,L)
            assert c0==count(lo,hi,arc,U)
            if c0:
                t=last(lo,hi,arc);ev=q+t+1
                assert n0<ev<=n1 and ev not in events
                events[ev]=gap;ct+=1;selected+=1
        stagecounts.append(ct)
    assert stagecounts==[36,60,127] and selected==223 and len(events)==225
    out=[];i=M+1
    for n,v in sorted(events.items()):
        push(out,i,n-1,Z);push(out,n,n,v);i=n+1
    push(out,i,389,Z)
    assert out==[(129,164,(16,-61)),(165,292,(-43,164)),(293,328,Z),(329,389,(-43,164))]
    return out,selected

def compile():
    seg,selected=prefix();blocks=pos=0
    for n0,n1,a,q,c,j in STAGES[3:]:
        assert n0==seg[-1][1]+1
        e=q+j;parts=[]
        for l,r in ((e-163,e-97),(e-60,e)):
            l=max(l,n0);r=min(r,n1)
            if l<=r:parts.append((l,r))
        if parts:
            assert q>=H and j>=M+H and c*D-j*L < 59*D-225*U
            amp=amplitude(a,q,c,j);pos+=1;blocks+=len(parts)
        k=n0
        for l,r in parts:push(seg,k,l-1,Z);push(seg,l,r,amp);k=r+1
        push(seg,k,n1,Z)
    assert pos==74 and blocks==148
    rows=[];A=B=0
    for l,r,(da,db) in seg:
        rows.append((l-1,r,A,B,da,db));A+=(r-l+1)*da;B+=(r-l+1)*db
    assert len(rows)==298 and (A,B)==(-4017401528447,15321634290944)
    o=StringIO(newline='');w=csv.writer(o,delimiter='\t',lineterminator='\n')
    w.writerow(('n0','n1','A0','B0','dA','dB'));w.writerows(rows)
    digest=sha256(o.getvalue().encode()).hexdigest()
    assert digest=='2573a84999d53dfd1cce772c45a41abaff251da735171efe904c860f2b2294f6'
    return selected,len(rows),digest

if __name__=='__main__':
    n,r,h=compile()
    print('PASS_R34_3_STAGES_223_SOURCE_SELECTS_4_PREFIX_RUNS_78_STAGES_298_AFFINE_RUNS')
    print('selected',n,'runs',r,'SHA256',h)
    print('R128',risk(128),'R389',risk(389),'R1000000000128',(-4017401528447,15321634290944))
