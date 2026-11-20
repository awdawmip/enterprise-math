"""Independent exact Gaussian-integer dynamic programming, stdlib only."""
from collections import defaultdict
from itertools import product
S0 = (214,215,216,217,218)
S1 = (214,216,217,218,219,220,221)
S2 = (215,216,217,218,219,220,221)
SETS = (set(S0),set(S1),set(S2))

def add(x,y): return (x[0]+y[0],x[1]+y[1])
def rot(x,k):
    a,b=x
    return ((a,b),(-b,a),(-a,-b),(b,-a))[k%4]

def H_and_neg_moment(S,m):
    states={0:((1,0),(0,0))}
    for p in S:
        nxt={}
        for k,(weight,neg_moment) in states.items():
            for n in range(m-k):
                w=rot(weight,p*n)
                d=rot(neg_moment,p*n)
                d=add(d,(-p*n*w[0],-p*n*w[1]))
                pw,pd=nxt.get(k+n,((0,0),(0,0)))
                nxt[k+n]=(add(pw,w),add(pd,d))
        states=nxt
    weights=(0,0); moment=(0,0)
    for w,d in states.values():
        weights=add(weights,w); moment=add(moment,d)
    return weights,moment

def overlap_dp(m):
    states={(0,0,0):(1,0)}
    for p in range(214,222):
        member=tuple(int(p in S) for S in SETS)
        nxt={}
        for key,w in states.items():
            for n in range(m):
                dest=tuple(min(m,key[j]+member[j]*n) for j in range(3))
                nxt[dest]=add(nxt.get(dest,(0,0)),rot(w,p*n))
        states=nxt
    out=(0,0)
    for state,w in states.items():
        multiplicity=max(sum(x<m for x in state)-1,0)
        out=add(out,(multiplicity*w[0],multiplicity*w[1]))
    return out

def overlap_direct(m):
    total=(0,0)
    for ns in product(range(m),repeat=8):
        counts={p:n for p,n in zip(range(214,222),ns)}
        k=sum(sum(counts[p] for p in S)<m for S in SETS)
        mul=max(k-1,0)
        if mul:
            phase=rot((mul,0),sum(p*n for p,n in counts.items()))
            total=add(total,phase)
    return total

def D_direct(m):
    _,der=H_and_neg_moment(S0,m)
    h1,_=H_and_neg_moment(S1,m)
    h2,_=H_and_neg_moment(S2,m)
    h=overlap_dp(m)
    real=der[0]+220*(h1[0]+h1[1])+220*h2[0]-440*h[0]
    imag=der[1]+220*(h1[1]-h1[0])+220*h2[1]-440*h[1]
    return real,imag

def D_formula(m):
    assert m>=2 and m%2==0
    if m%4==2:
        t=(m-2)//4
        return (t+1)*(436*t+656),-2*(t+1)
    t=(m-4)//4
    return 436*(t+1)*(t+2),220*(t+1)*(t+2)

for m in (1,2,3,4):
    assert overlap_dp(m)==overlap_direct(m),m
for m in range(2,21,2):
    assert D_direct(m)==D_formula(m), (m,D_direct(m),D_formula(m))
    print(m, D_direct(m))
print('PASS: independent exact Z[i] DP, even m=2..20, overlap eight-dimensional m=1..4')
