"""R76: exact persistent AVL winner frontier; only auxiliary rational circle arithmetic."""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
import json,random,time

@dataclass(frozen=True)
class Node:
    key:object
    value:object
    left:object=None
    right:object=None
    height:int=1
    count:int=1
    low:object=None
    high:object=None

def h(n):return n.height if n else 0
def ncount(n):return n.count if n else 0
def mk(k,v,l=None,r=None):
    return Node(k,v,l,r,1+max(h(l),h(r)),1+ncount(l)+ncount(r),l.low if l else k,r.high if r else k)
def rotl(x):
    y=x.right
    return mk(y.key,y.value,mk(x.key,x.value,x.left,y.left),y.right)
def rotr(y):
    x=y.left
    return mk(x.key,x.value,x.left,mk(y.key,y.value,x.right,y.right))
def balance(n):
    if not n:return None
    d=h(n.left)-h(n.right)
    if d>1:
        l=n.left
        if h(l.left)<h(l.right):n=mk(n.key,n.value,rotl(l),n.right)
        return rotr(n)
    if d< -1:
        r=n.right
        if h(r.right)<h(r.left):n=mk(n.key,n.value,n.left,rotr(r))
        return rotl(n)
    return n
def get(n,k):
    while n:
        if k<n.key:n=n.left
        elif k>n.key:n=n.right
        else:return n.value
    return None
def put(n,k,v):
    if n is None:return mk(k,v)
    if k<n.key:return balance(mk(n.key,n.value,put(n.left,k,v),n.right))
    if k>n.key:return balance(mk(n.key,n.value,n.left,put(n.right,k,v)))
    return mk(k,v,n.left,n.right)
def popmin(n):
    if not n.left:return n.right,n
    new_l,old=popmin(n.left)
    return balance(mk(n.key,n.value,new_l,n.right)),old
def erase(n,k):
    if not n:return None
    if k<n.key:return balance(mk(n.key,n.value,erase(n.left,k),n.right))
    if k>n.key:return balance(mk(n.key,n.value,n.left,erase(n.right,k)))
    if not n.left:return n.right
    if not n.right:return n.left
    new_r,succ=popmin(n.right)
    return balance(mk(succ.key,succ.value,n.left,new_r))
def popmax(n):
    if not n.right:return n.left,n
    new_r,old=popmax(n.right)
    return balance(mk(n.key,n.value,n.left,new_r)),old
def allitems(n):
    if n:
        yield from allitems(n.left)
        yield(n.key,n.value)
        yield from allitems(n.right)
def assert_balanced(n):
    if not n:return 0
    a=assert_balanced(n.left);b=assert_balanced(n.right)
    assert abs(a-b)<=1 and n.height==max(a,b)+1
    assert n.count==1+ncount(n.left)+ncount(n.right)
    assert n.low==(n.left.low if n.left else n.key)
    assert n.high==(n.right.high if n.right else n.key)
    if n.left:assert n.left.high<n.key
    if n.right:assert n.right.low>n.key
    return n.height

@dataclass(frozen=True)
class Version:
    groups:Node|None=None
    winners:Node|None=None
    count:int=0

def edit(v,theta0,t,branch,add):
    p,q=theta0.numerator,theta0.denominator
    r=(t*p)%q
    times=get(v.groups,r)
    old_max=times.high if times else None
    branches=get(times,t)
    found=get(branches,branch) is not None
    if add:
        if found:return v
        branches=put(branches,branch,True)
    else:
        if not found:return v
        branches=erase(branches,branch)
    if branches:times=put(times,t,branches)
    else:times=erase(times,t)
    groups=put(v.groups,r,times) if times else erase(v.groups,r)
    winners=v.winners
    if old_max is not None:winners=erase(winners,(old_max,r))
    if times:winners=put(winners,(times.high,r),r)
    return Version(groups,winners,v.count+(1 if add else -1))
def members(v):
    out=set()
    for r,times in allitems(v.groups):
        for t,bs in allitems(times):
            for b,_ in allitems(bs):out.add((t,b))
    return out
def floor(y):return y.numerator//y.denominator
def ceil(y):return -floor(-y)
def interval_valid(L,U,a,b):
    return L<=U and floor(a*L)==floor(a*U) and floor(b*L)==floor(b*U) and all(
        F(0)<=a*z-floor(a*L)<b*z-floor(b*L)<1 for z in [L,U])
def first_entry(t,j,x,a,b,L,U,compl=False):
    ka,kb=floor(a*L),floor(b*L)
    cl,cd=(b,-kb) if compl else (a,-ka)
    dl,dd=(a,1-ka) if compl else (b,-kb)
    def alpha(z):return x+(t-j)*z
    def C(z):return cl*z+cd
    def D(z):return dl*z+dd
    def u(z):return alpha(z)-C(z)
    def w(z):return D(z)-C(z)
    def vv(z):return alpha(z)-D(z)
    uL,uU,vL,vU=u(L),u(U),vv(L),vv(U)
    k0=floor(uL)
    if F(k0)>vL:return L,'LEFT'
    if uU>uL and floor(uU)>k0:
        k=k0+1
        z=L+(U-L)*(F(k)-uL)/(uU-uL)
        assert L<=z<=U and vv(z)<k<=u(z)
        return z,'ENTER'
    if vU<vL and vU<floor(vL):
        k=floor(vL)
        z0=L+(U-L)*(F(k)-vL)/(vU-vL)
        delta=min((U-z0)/2,w(z0)/(2*(abs(t-j-cl)+1)))
        z=z0+delta
        assert L<=z<=U and vv(z)<k<=u(z)
        return z,'LEAVE'
    return None,'OUT'
def is_inside(t,j,x,a,b,z):
    A=(a*z)%1;B=(b*z)%1
    return A<=((x+(t-j)*z)%1)<B
def classify(t,j,x,a,b,L,U):
    yes,yt=first_entry(t,j,x,a,b,L,U)
    no,nt=first_entry(t,j,x,a,b,L,U,True)
    assert yes is not None or no is not None
    if yes is None:return('ALL_OUT',None,None)
    if no is None:return('ALL_IN',yes,None)
    assert is_inside(t,j,x,a,b,yes) and not is_inside(t,j,x,a,b,no)
    return('MIXED',yes,no)
def group_excluded(r,times,anchor,j,x,a,b,L,U):
    assert L<=anchor<=U
    q=anchor.denominator
    beta=(F(r,q)+x-j*anchor)%1
    dmin,dmax=times.low-j,times.high-j
    dl,du=L-anchor,U-anchor
    zs=[dmin*dl,dmin*du,dmax*dl,dmax*du]
    smin,smax=beta+min(zs),beta+max(zs)
    A=lambda z:a*z-floor(a*L)
    B=lambda z:b*z-floor(b*L)
    qmin=min(A(L),A(U));qmax=max(B(L),B(U))
    return ceil(smin-qmax)>floor(smax-qmin)
def full_oracle(v,j,x,a,b,L,U):
    ts=sorted({t for t,b0 in members(v)},reverse=True)
    for t in ts:
        typ,y,n=classify(t,j,x,a,b,L,U)
        if typ=='ALL_OUT':continue
        return('STABLE',t,None,None) if typ=='ALL_IN' else('CHANGES',t,y,n)
    return('STABLE_NONE',None,None,None)
def priority_oracle(v,anchor,j,x,a,b,L,U):
    head=v.winners
    cursors={}
    examined=set();cut=0;tested=0;skipped=0
    while head:
        head,row=popmax(head)
        t,r=row.key
        times=cursors.pop(r,None)
        if times is None:times=get(v.groups,r)
        assert times is not None and times.high==t
        if r not in examined:
            examined.add(r)
            if group_excluded(r,times,anchor,j,x,a,b,L,U):
                cut+=1;skipped+=times.count;continue
        typ,y,n=classify(t,j,x,a,b,L,U)
        tested+=1
        if typ!='ALL_OUT':
            ans=('STABLE',t,None,None) if typ=='ALL_IN' else('CHANGES',t,y,n)
            return ans,{'groups_excluded':cut,'times_skipped':skipped,'individual_checks':tested,'groups_examined':len(examined)}
        times,_=popmax(times)
        if times:
            head=put(head,(times.high,r),r)
            cursors[r]=times
    return('STABLE_NONE',None,None,None),{'groups_excluded':cut,'times_skipped':skipped,'individual_checks':tested,'groups_examined':len(examined)}
def latest_at(e,j,x,a,b,z):
    good=[t for t,br in e if is_inside(t,j,x,a,b,z)]
    return max(good) if good else None
def verify_witness(ans,e,j,x,a,b,L,U):
    status,t,y,n=ans
    if status=='CHANGES':
        assert y is not None and n is not None and L<=y<=U and L<=n<=U
        assert latest_at(e,j,x,a,b,y)==t
        assert latest_at(e,j,x,a,b,n)!=t
    elif status=='STABLE':assert t is not None
    else:assert t is None

def run():
    rng=random.Random(761126)
    qs=0;updates=0;hist=0;match=0
    counters={'groups_excluded':0,'times_skipped':0,'individual_checks':0,'groups_examined':0}
    favorable=[]
    for case in range(36):
        anchor=F(rng.randint(1,5),rng.choice([8,12,16,20,25,32,40]))
        versions=[(Version(),set())]
        cur=Version();ids=set()
        for step in range(100):
            if ids and rng.random()<.44:
                t,br=rng.choice(tuple(sorted(ids)))
                ids.remove((t,br));cur=edit(cur,anchor,t,br,False)
            else:
                t=rng.randint(-50,80);br=rng.randrange(3)
                ids.add((t,br));cur=edit(cur,anchor,t,br,True)
            assert members(cur)==ids and cur.count==len(ids)
            assert_balanced(cur.groups);assert_balanced(cur.winners)
            for r,times in allitems(cur.groups):
                assert_balanced(times)
                for t,bs in allitems(times):assert_balanced(bs)
                assert get(cur.winners,(times.high,r))==r
            versions.append((cur,ids.copy()));updates+=1
        for _ in range(20):
            vv,ss=rng.choice(versions)
            assert members(vv)==ss
            hist+=1
        for _ in range(35):
            vv,ss=rng.choice(versions)
            a,b=rng.sample(range(-6,10),2)
            if a==b:continue
            delta=F(rng.randint(0,2),rng.choice([200,500,1000,2000]))
            L=max(F(-10),anchor-delta);U=min(F(10),anchor+delta)
            if not interval_valid(L,U,a,b):continue
            j=rng.randrange(-3,4);x=F(rng.randrange(-6,7),rng.choice([2,3,5,7]))
            expected=full_oracle(vv,j,x,a,b,L,U)
            actual,metrics=priority_oracle(vv,anchor,j,x,a,b,L,U)
            assert actual[0:2]==expected[0:2],(expected,actual)
            verify_witness(actual,ss,j,x,a,b,L,U)
            for k in counters:counters[k]+=metrics[k]
            if actual[0]=='CHANGES':match+=1
            qs+=1
    for n in(32,128,512,1024):
        anchor=F(1,4);v=Version()
        ts=time.perf_counter()
        for k in range(1,n//2+1):
            v=edit(v,anchor,4*k,k,True)
            v=edit(v,anchor,4*k-1,k+10000,True)
        built=time.perf_counter()-ts
        L=anchor-F(1,100*(n//2));U=anchor+F(1,100*(n//2))
        assert interval_valid(L,U,1,2)
        ts=time.perf_counter()
        for _ in range(20):
            ans,met=priority_oracle(v,anchor,0,F(0),1,2,L,U)
            assert ans[0]=='STABLE_NONE' and met['individual_checks']==0
        query=time.perf_counter()-ts
        favorable.append({'sources':n,'build_seconds':round(built,6),'twenty_queries_seconds':round(query,6),'phase_groups':v.winners.count,'individual_checks_per_query':met['individual_checks'],'groups_excluded_per_query':met['groups_excluded']})
    results={'seed':761126,'random_models':36,'persistent_updates':updates,'historical_versions_audited':hist,'matched_complete_interval_queries':qs,'changes_witness_queries':match,'aggregate':counters,'favorable_two_phase':favorable,'all_assertions':'PASS'}
    print(json.dumps(results,ensure_ascii=False,indent=2))
    return results
if __name__=='__main__':run()
