"""Exact Riesel ninth-budget sufficient observation carrier. Python stdlib."""
from itertools import combinations
from math import gcd, isqrt, prod, lcm
from known_inputs import P, A2, Q0, U9, E, C, D as OLD_D
import json

A={1,2,10,11,12,16,17,22,25,26,30,31,32}
S2=11356718000553566643685496313583434507970452519839503606327232707476034989690
S1=S2//(433*38737)
def cost(e):
    return sum((p-1)*j for p,j in factor(e).items())
def factor(n):
    d={}
    for p in range(2,isqrt(n)+1):
        while n%p==0:
            d[p]=d.get(p,0)+1
            n//=p
        if n==1: break
    if n>1: d[n]=1
    return d

def minlines(S, t, g):
    goal=S-{r for r in S if (r-t)%g==0}
    cand=[{r for r in S if r%p==b} for p in (5,7) for b in range(p) if t%p!=b]
    return next(k for k in range(len(cand)+1) if any(goal <= set().union(*c) for c in combinations(cand,k)))

low={}
for r in range(3):
    D={(a-r)*pow(3,-1,35)%35 for a in A}
    low[str(r)]={str(g):{str(t):minlines(D,t,g) for t in sorted(D)} for g in (1,5,7,35)}
    assert {g:min(low[str(r)][str(g)].values()) for g in (1,5,7,35)}=={1:0,5:2,7:4,35:4}
eps={2**a*3**b for a in range(5) for b in range(3) if a+2*b<=4}
H={g*e for g,k in ((1,0),(5,2),(7,4),(35,4)) for e in eps if cost(e)+k<=4}
F={7,10,14,28,35,70}
phase={d for h in H for d in range(1,36*h+1) if d//gcd(d,36)==h}
shared={d for f in F for d in range(1,12*f+1) if d//gcd(d,12)==f}
orders=sorted(phase|shared)
assert not any(840<d<1260 for d in orders)
assert [d for d in orders if d>=840]==[840,1260]
assert 1008 not in orders

def strip(n, m):
    while (f:=gcd(n,m))!=1: n//=f
    return n
def phi2(d):
    top=bot=1
    fs=list(factor(d))
    for k in range(len(fs)+1):
        for sub in combinations(fs,k):
            x=(1 << (d//prod(sub)))-1
            if k%2: bot*=x
            else: top*=x
    q,r=divmod(top,bot)
    assert r==0
    return q
def carrier(d):
    # Start from 2^d-1 and remove every prime of any proper order,
    # including its full multiplicity. Compare with same filtering on Phi_d.
    excluded=prod((1 << (d//p))-1 for p in factor(d))
    q=strip((1<<d)-1,excluded)
    assert q == strip(phi2(d),excluded)
    return q

def sieve(n):
    a=bytearray(b'\1')*(n+1)
    a[:2]=b'\0\0'
    for i in range(2,isqrt(n)+1):
        if a[i]: a[i*i::i]=b'\0'*((n-i*i)//i+1)
    return [i for i in range(n+1) if a[i]]

rows=[]
ps=sieve(100000)
checked=1
for d in orders:
    full=carrier(d)
    assert gcd(checked,full)==1
    checked*=full
    n=strip(full,S2)
    primes={}
    for p in ps:
        if p*p>n: break
        while n%p==0:
            primes[str(p)]=primes.get(str(p),0)+1
            n//=p
    if 1<n<=100000**2 and all(n%p for p in ps if p*p<=n):
        primes[str(n)]=1
        n=1
    assert n*prod(int(p)**k for p,k in primes.items())==strip(full,S2)
    rows.append({'d':d,'h':d//gcd(d,36),'f':d//gcd(d,12),
                 'free_carrier_R1':strip(full,S1),'free_carrier_R2':strip(full,S2),
                 'R2_proved_prime_factors':primes, 'R2_unclassified_cofactor':n})
P1=prod(r['free_carrier_R1'] for r in rows)
P2=prod(r['free_carrier_R2'] for r in rows)
assert P1==P2*433*38737
def order(q, limit=1260):
    u=1
    for n in range(1,limit+1):
        u=2*u%q
        if u==1:return n
    raise AssertionError(q)
def f_of(q):
    d=order(q)
    return d//gcd(d,12)
known=set(U9+E+C+OLD_D+(870031,1765891,2521))
assert len(known)==74
assert all(gcd(q,S2)==1 and P2%q==0 for q in known)
f_R2={r['f'] for r in rows if r['free_carrier_R2']>1}
f_known={f_of(q) for q in known}
assert f_R2-f_known=={27,45}
assert {r['f'] for r in rows if r['free_carrier_R1']>1}-f_R2=={6}
assert f_of(433)==f_of(38737)==6

plans={
    27: ([(87211,0),(246241,1),(2593,2),(71119,5),(163,8)], 2593),
    45: ([(181,0),(631,3),(271,6),(811,1),(541,11)], 271),
}
def crt(a,m,b,n):
    return a+m*((b-a)*pow(m,-1,n)%n),m*n

def build(plan,target,off):
    mask=strip(P2,prod(q for q,w in plan))
    a,m=crt(A2,S2,0,mask)
    for q,w in plan:
        a,m=crt(a,m,0 if q==target and off else pow(2,-(16+18*w),q),q)
    assert m%target==0 and a%S2==A2
    return a+m,m

def miss_count(a, qs, period):
    allbits=(1<<period)-1
    hit=0
    for q in qs:
        z=pow(a,2,q); hz=0
        for i in range(period):
            if z==1:hz|=1<<i
            z=2*z%q
        assert z==pow(a,2,q)
        hit|=hz
    return (allbits^hit).bit_count()
pairs={}
for f,(plan,target) in plans.items():
    a,m=build(plan,target,False)
    b,n=build(plan,target,True)
    assert n==m and m%target**2!=0 and (a-b)%(m//target)==0
    other=tuple(q for q,w in plan if q!=target)
    assert all(all(q%i for i in range(2,isqrt(q)+1)) for q,w in plan)
    assert len(set(other)|{target})==5 and f_of(target)==f
    period=lcm(*(order(q) for q in P+Q0+(38737,target)+other))
    assert miss_count(a, P+Q0+(target,)+other, period)==0
    # Each one of the nine selected primes is essential even when fixed A
    # can be included; omission of any leaves a hole. 5,13 forced separately.
    members=Q0+(target,)+other
    forced_holes={}
    for k in members:
        if k in (5,13):continue
        holes=miss_count(a,P+(38737,)+tuple(q for q in members if q!=k),period)
        assert holes>0
        forced_holes[k]=holes
    off_holes=miss_count(b,P+Q0+(38737,)+other,period)
    assert off_holes>0
    pairs[f]={'target':target,'period':period,'on_root_hex':hex(a),'off_root_hex':hex(b),
        'modulus_hex':hex(m),'off_holes':off_holes,'on_omission_holes_even_with_38737':forced_holes}
print(json.dumps({'available_phase_periods_h':sorted(H),'available_shared_periods_f':sorted(F),
    'number_of_order_buckets':len(orders),
    'R1_nonempty_order_buckets':sum(r['free_carrier_R1']>1 for r in rows),
    'known_necessary_f_buckets_R2':sorted(f_known),'all_necessary_f_buckets_R2':sorted(f_R2),
    'last_two_f_witnesses_R2':pairs,'R2_nonempty_order_buckets':sum(r['free_carrier_R2']>1 for r in rows),
    'R1_carrier_bits':P1.bit_length(),'R2_carrier_bits':P2.bit_length(),
    'R2_trial_division_prime_count':sum(len(r['R2_proved_prime_factors']) for r in rows),
    'R2_unclassified_cofactor_count':sum(r['R2_unclassified_cofactor']>1 for r in rows),
    'row_line_minima':low,'order_buckets':rows},indent=2))
