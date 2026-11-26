from fractions import Fraction as F
from math import floor,ceil,gcd
from pathlib import Path
import json, hashlib
E=400000;G=10**85

def load(name):
    a=json.loads(Path(name).read_text());return tuple(tuple(F(int(v),G) for v in a[k]) for k in ('rho','c','d'))

def convergent(x,M):
    a,b=x.numerator,x.denominator;p0,p1,q0,q1=0,1,1,0
    while b:
        k,a,b=a//b,b,a%b;p,q=k*p1+p0,k*q1+q0
        if q>M: return p1,q1
        p0,p1,q0,q1=p1,p,q1,q
    return p1,q1

def sublevel(fun,a,b,strict=False):
    # Discrete convex fun: return contiguous integer indices where f <= 0 (or < 0).
    if a>b:return None
    l,h=a,b
    while l<h:
        mid=(l+h)//2
        if fun(mid+1)>=fun(mid):h=mid
        else:l=mid+1
    k=l;ok=(lambda v:v<0) if strict else (lambda v:v<=0)
    if not ok(fun(k)):return None
    l,h=a,k
    while l<h:
        mid=(l+h)//2
        if ok(fun(mid)):h=mid
        else:l=mid+1
    first=l;l,h=k,b
    while l<h:
        mid=(l+h+1)//2
        if ok(fun(mid)):l=mid
        else:h=mid-1
    return first,l

def lines(box,L,H,p=None,q=None):
    R,C,T=box
    assert 0<L<=H and T[0]*L>3*E
    if p is None:p,q=convergent(sum(R)/2,L)
    assert q>0 and gcd(p,q)==1
    a=R[0]-F(p,q);b=R[1]-F(p,q)
    low=ceil(q*(min(a*L,a*H)+C[0]+T[0]/H-F(E,L*L)))
    high=floor(q*(max(b*L,b*H)+C[1]+T[1]/L+F(E,L*L)))
    inv=pow(p,-1,q) if q>1 else 0
    runs=[];calls=0;occupied=0
    for h in range(low,high+1):
        r=(-inv*h)%q;u=ceil(F(L-r,q));v=floor(F(H-r,q))
        if u>v:continue
        occupied+=1
        def f(n,side):
            nonlocal calls
            calls+=1;m=r+q*n
            return (R[side]-F(p,q))*m+C[side]-F(h,q)+T[side]/m+F((2*side-1)*E,m*m)
        A=sublevel(lambda n:f(n,0),u,v)
        if A is None:continue
        B=sublevel(lambda n:f(n,1),*A,strict=True)
        if B is None:parts=[A]
        else:parts=[(A[0],B[0]-1),(B[1]+1,A[1])]
        for x,y in parts:
            if x<=y:runs.append((h,r+q*x,r+q*y,q))
    return dict(p=p,q=q,line_low=low,line_high=high,line_count=max(0,high-low+1),occupied=occupied,calls=calls,runs=runs,count=sum((y-x)//s+1 for h,x,y,s in runs))

def expand(out):
    p,q=out['p'],out['q'];return sorted((m,(p*m+h)//q) for h,x,y,s in out['runs'] for m in range(x,y+1,s))

def sweep(box,L,end):
    out=[]
    while L<end:
        H=min(2*L,end)-1;z=lines(box,L,H);out.append(dict(L=L,H=H,**z));L=H+1
    return out

def stats(w):return dict(windows=len(w),lines=sum(z['line_count'] for z in w),occupied=sum(z['occupied'] for z in w),calls=sum(z['calls'] for z in w),count=sum(z['count'] for z in w),max_lines=max(z['line_count'] for z in w))

def main():
    import random
    rng=random.Random(1116)
    for _ in range(500):
        l=rng.randint(10**8,10**8+10000);h=l+rng.randint(0,200);rho=F(rng.randint(-10000,10000),rng.randint(1,1000));w=F(rng.randint(0,100),10**12);c=F(rng.randint(-100,100),13);d=F(rng.randint(1,30));box=((rho-w,rho+w),(c-w,c+w),(d,d+w))
        z=lines(box,l,h)
        ref=[]
        R,C,T=box
        for m in range(l,h+1):
            lo=R[0]*m+C[0]+T[0]/m-F(E,m*m);hi=R[1]*m+C[1]+T[1]/m+F(E,m*m)
            ref.extend((m,j) for j in range(ceil(lo),floor(hi)+1))
        assert expand(z)==ref
    old=load('root_8000_result.json');new=load('root_8400_result.json');ref=json.loads(Path('root_8000_window_result.json').read_text());end=ref['end'];L=ref['start']
    a=sweep(old,L,end);pa=sorted(p for z in a for p in expand(z));assert pa==[tuple(p) for p in ref['candidates']]
    b=sweep(new,L,end);assert sum(z['count'] for z in b)==0
    c=sweep(new,end,end*128);print('old',stats(a),'final old range',stats(b),'extension',stats(c))
    for z in c:print(z['L'],z['H'],z['q'],z['line_count'],z['calls'],z['count'])
    out=dict(random_tests=500,old=stats(a),final_old_range=stats(b),extension=stats(c),old_windows=a,final_old_windows=b,extension_windows=c)
    Path('prefix1116_result.json').write_text(json.dumps(out,indent=2))
    print('sha256',hashlib.sha256(Path('prefix1116_result.json').read_bytes()).hexdigest())
if __name__=='__main__':main()
