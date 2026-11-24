"""R2 exact predicates at budgets seven, eight and nine, with optional order cut."""
from collections import defaultdict
from functools import cache
from itertools import combinations
from math import gcd, lcm, prod
import argparse, json

A=frozenset((1,2,10,11,12,16,17,22,25,26,30,31,32))
S2=11356718000553566643685496313583434507970452519839503606327232707476034989690
A2=9807947978443488306255509703402695727949968778703073231931137913705883712843
FIX=((3,0),(3,1),(6,5))
H=frozenset((1,2,3,4,5,6,7,8,9,10,12,15,16,20,35))
F_COMMON=frozenset((7,10,14,28,35,70))

def factors(n):
    out=[]
    p=2
    while p*p<=n:
        if n%p==0:
            out.append(p)
            while n%p==0:n//=p
        p+=1
    return out+([n] if n>1 else [])

def strip(x,y):
    while (z:=gcd(x,y))>1:x//=z
    return x

@cache
def carriers(cut=1260):
    full,split,common=defaultdict(lambda:1),defaultdict(lambda:1),defaultdict(lambda:1)
    rows={}
    for d in range(1,min(1260,cut)+1):
        h,f=d//gcd(d,36),d//gcd(d,12)
        if h not in H and f not in F_COMMON:continue
        q=strip(strip((1<<d)-1,prod((1<<(d//p))-1 for p in factors(d))),S2)
        if q==1:continue
        rows[d]=f,q
        full[f]*=q
        if h in H:split[f]*=q
        if f in F_COMMON:common[f]*=q
    return rows,dict(full),dict(split),dict(common)

def hits(a,C):
    # b is nonnegative; modular recurrence avoids ever forming a huge F_n.
    out=set()
    for f,c in C.items():
        x=(a%c)**2*256%c
        z=4096%c
        for b in range(f):
            if gcd(x-1,c)>1:out.add((f,b))
            x=x*z%c
    return frozenset(out)

@cache
def geometry(period):
    p=tuple(v for v in range(period) if v%35 in A)
    return p,(1<<len(p))-1

@cache
def mask(period,f,b):
    p,_=geometry(period)
    return sum(1<<i for i,v in enumerate(p) if v%f==b)

def union(masks):
    v=0
    for m in masks:v|=m
    return v

def solve(deficit, classes, k, period):
    """Exact bounded set cover. Return a cover of minimum size or None."""
    if not deficit:return ()
    if not k:return None
    raw={mask(period,*x)&deficit:x for x in sorted(classes)}
    raw.pop(0,None)
    if union(raw)!=deficit:return None
    # A subset mask can be replaced by any larger active mask at no extra cost.
    items=[]
    for m in sorted(raw,key=int.bit_count,reverse=True):
        if not any(m&n==m for n in items):items.append(m)
    by_point={}
    @cache
    def dfs(left,b):
        if not left:return ()
        if b==0:return None
        cnt=left.bit_count()
        if sum(sorted(((m&left).bit_count() for m in items),reverse=True)[:b])<cnt:return None
        choice=None
        u=left
        while u:
            bit=u&-u;u-=bit
            if bit not in by_point:by_point[bit]=[m for m in items if m&bit]
            cs=by_point[bit]
            if choice is None or len(cs)<len(choice):choice=cs
            if len(cs)==1:break
        for m in sorted(choice,key=lambda m:(m&left).bit_count(),reverse=True):
            ans=dfs(left&~m,b-1)
            if ans is not None:return (m,*ans)
        return None
    for i in range(1,k+1):
        z=dfs(deficit,i)
        if z is not None:
            return tuple(raw[m] for m in z)
    return None

def common(support,k):
    period=lcm(35,*(f for f,_ in support))
    return solve(geometry(period)[1],support,k,period)

def split(support,k):
    period=lcm(35,3,*(f for f,_ in support))
    shared=sorted(x for x in support if x[0]%3)
    local=[{x for x in support if x[0]%3==0 and x[1]%3==r} for r in range(3)]
    goal=[mask(period,3,r) for r in range(3)]
    cube=[union(mask(period,*x) for x in loc) for loc in local]
    for s in range(min(len(shared),k-3)+1):
        for common0 in combinations(shared,s):
            cov=union(mask(period,*x) for x in common0)
            deficits=[g&~cov for g in goal]
            # This routine represents inclusion-minimal split covers; all three
            # phases must contain a private class. All-common is handled separately.
            if any(not d or d&~c for d,c in zip(deficits,cube)):continue
            remaining=k-s
            out=list(common0)
            for j,r in enumerate(sorted(range(3),key=lambda r:deficits[r].bit_count(),reverse=True)):
                seq=solve(deficits[r],local[r],remaining-(2-j),period)
                if seq is None:break
                remaining-=len(seq)
                out.extend(seq)
            else:return tuple(out)
    return None

def predicate(a,budget=9,cut=1260):
    if a<A2 or a%S2!=A2:raise ValueError('a is outside R2')
    if budget not in (7,8,9):raise ValueError('budget must be 7, 8, or 9')
    _,_,p,c=carriers(cut)
    z=common(hits(a,c),budget-2)
    return z if z is not None else split(hits(a,p)|set(FIX),budget-2)

def high_only_geometry(a):
    """Existence of an irredundant nine cover containing an order-1260 prime."""
    rows,full,_,_=carriers()
    allhit=hits(a,full)
    hi=hits(a,{105:rows[1260][1]})
    if any((15,(2+3*w)%15) not in allhit for w in (0,3)):return False
    slots=[2+3*w for w in (21,26,31)]
    return all(any((f,v%f) in allhit for f in (7,21,105)) for v in slots) and any((105,v%105) in hi for v in slots)

def literal(a,budget,cut=1260):
    """Unsplit residual-bit oracle with the entire finite inventory."""
    H0=hits(a,carriers(cut)[1])|set(FIX)
    return common(H0,budget-2)

def phase_value(a,slot,cut):
    """Show the nontrivial divisor carrier for a free occupied slot."""
    f,b=slot
    c=carriers(cut)[1][f]
    return gcd(c,((a%c)**2 * pow(2,8+12*b,c)-1)%c)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('root',type=lambda x:int(x,0))
    p.add_argument('--budget',type=int,choices=(7,8,9),default=9)
    p.add_argument('--through-order-840',action='store_true')
    args=p.parse_args()
    cut=840 if args.through_order_840 else 1260
    cover=predicate(args.root,args.budget,cut)
    print(json.dumps({'budget':args.budget,'maximum_allowed_order':cut,'cover_exists':cover is not None,
          'forced_prefix':[5,13] if cover is not None else [], 'slots':[
            {'f':f,'phase':b,'fixed_prime':dict(zip(FIX,(19,73,38737))).get((f,b))}
              if (f,b) in FIX else {'f':f,'phase':b,'nontrivial_divisor_carrier':str(phase_value(args.root,(f,b),cut))}
              for f,b in cover or ()]},ensure_ascii=False))
if __name__=='__main__':main()
