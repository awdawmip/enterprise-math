"""Finite Gaussian-turn certificates. Python 3.10+, standard library."""
import argparse
import csv
from collections import defaultdict
from fractions import Fraction
from functools import cache
from itertools import combinations, product
from math import gcd, isqrt, log10, prod
from typing import NamedTuple

def times(z,w):
    return z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0]

def divide(z,w):
    norm=w[0]**2+w[1]**2
    x,y=times(z,(w[0],-w[1]))
    return (x//norm,y//norm) if x%norm==y%norm==0 else None

@cache
def split(p):
    for y in range(1,isqrt(p)+1):
        x=isqrt(p-y*y)
        if x>=y and x*x+y*y==p: return x,y
    raise ValueError(p)

@cache
def factors(n):
    out=[]
    k=2
    while k*k<=n:
        if n%k==0:
            out.append(k)
            while n%k==0:n//=k
        k=3 if k==2 else k+2
    return tuple(out+([n] if n>1 else []))

def signature(b,a):
    z=(b,a);v={};eps=0
    for p in factors(b*b+a*a):
        if p==2:
            z=divide(z,(1,1));eps=1;continue
        x,y=split(p);count=0
        for sign in (1,-1):
            while (w:=divide(z,(x,sign*y))) is not None:
                z=w;count+=sign
        assert count
        v[p]=count
    eps+=2*[(1,0),(0,1),(-1,0),(0,-1)].index(z)
    return eps%8,v

class Atom(NamedTuple):
    b:int
    a:int
    cost:int
    eps:int
    v:dict

SCALE=1000
LIMIT=1723  # Outer bound for triples at B>=18; analytic leader is below 1.723.
@cache
def floorcost(b,a):
    # Floating point proposes k. Two exact integer powers certify its floor.
    k=int(SCALE/log10(b/a))
    q=10**SCALE
    while b**k>q*a**k:k-=1
    while b**(k+1)<=q*a**(k+1):k+=1
    return k

def cert(zs,cs):
    # Count oriented crossings of the positive real ray using a half-open
    # argument [0,2pi); gcd normalization always preserves the sign.
    z=(1,0);turn=0;cross=0
    def lower(z):return z[1]<0
    for u,c in zip(zs,cs):
        sign=1 if c>0 else -1
        for _ in range(abs(c)):
            w=times(z,(u.b,sign*u.a));g=gcd(*w);w=(w[0]//g,w[1]//g)
            # Only crossings of the positive real ray have a positive real part;
            # both endpoints may be used since every step has magnitude < pi/4.
            if z[0]>0 and w[0]>0 and lower(z)!=lower(w):
                turn+=1 if lower(z) else -1
                cross+=1
            z=w
    assert z==(1,1)
    return turn,cross

def det(x,y,i,j):return x.get(i,0)*y.get(j,0)-x.get(j,0)*y.get(i,0)

def classify(triple):
    x,y,z=(a.v for a in triple)
    axes=sorted(x.keys()|y.keys()|z.keys())
    pivot=next(((i,j) for i,j in combinations(axes,2) if det(x,y,i,j)),None)
    if pivot is None:
        return ("rank1",None) if not any(det(x,z,i,j) for i,j in combinations(axes,2)) else ("dependent_pair",None)
    i,j=pivot
    cs=(det(y,z,i,j),det(z,x,i,j),det(x,y,i,j))
    if any(sum(c*a.v.get(k,0) for a,c in zip(triple,cs)) for k in axes):return "rank3",None
    if 0 in cs:return "dependent_pair",None
    g=gcd(*cs);cs=tuple(t//g for t in cs)
    e=sum(a.eps*c for a,c in zip(triple,cs))%8
    if e%2==0:return "even",None
    k=e if e<=4 else e-8
    return "odd",tuple(k*c for c in cs)

def bit_search():
    # Sum of *floored* costs is a safe outward screen. Maximal bit length is
    # 17, since each of the other two denominators costs at least two bits.
    costs={d:floorcost((1<<d)-1,1) for d in range(2,18)}
    patterns=[(d,e,f) for d in costs for e in range(d,18) for f in range(e,18)
              if 18<=d+e+f<=21 and costs[d]+costs[e]+costs[f]<=LIMIT]
    caps=defaultdict(int)
    for pat in patterns:
        for d in pat:caps[d]=max(caps[d],LIMIT-sum(costs[t] for t in pat)+costs[d])
    pool={}
    for d,cap in caps.items():
        arr=[]
        for b in range(1<<(d-1),1<<d):
            for a in range(1,b):
                if b<=2*a or floorcost(b,a)>cap:break
                if gcd(a,b)==1:
                    e,v=signature(b,a);arr.append(Atom(b,a,floorcost(b,a),e,v))
        pool[d]=arr
    counters=defaultdict(int);hits=[]
    for pat in patterns:
        lists=[[u for u in pool[d] if u.cost+sum(costs[t] for t in pat)-costs[d]<=LIMIT] for d in pat]
        # An active prime must occur on at least two columns. For the first
        # two prime supports A,B the third one T must satisfy A△B ⊆ T ⊆ A∪B.
        index=defaultdict(list)
        for z in lists[2]:index[frozenset(z.v)].append(z)
        @cache
        def candidates(A,B):
            req=A^B; allow=A|B
            return [w for T,group in index.items() if req<=T<=allow for w in group]
        for x in lists[0]:
            for y in lists[1]:
                if (x.b,x.a)>=(y.b,y.a) or x.cost+y.cost+costs[pat[2]]>LIMIT:continue
                for z in candidates(frozenset(x.v),frozenset(y.v)):
                    if (y.b,y.a)>=(z.b,z.a) or x.cost+y.cost+z.cost>LIMIT:continue
                    triple=(x,y,z); kind,cs=classify(triple)
                    counters[(sum(pat),kind)]+=1
                    if kind=="odd":
                        hits.append((sum(pat),tuple((a.b,a.a) for a in triple),cs,cert(triple,cs)))
        candidates.cache_clear()
    print("bit patterns, candidate atoms",len(patterns),sum(map(len,pool.values())))
    print("bit census by exact rank and C8",dict(sorted(counters.items())))
    print("bit hits",hits)
    assert hits==[(21,((57,1),(79,3),(239,1)),(20,12,-5),(0,0))]
    assert [sum(v for (bits,_),v in counters.items() if bits==B) for B in range(18,22)]==[1,3,36,159]
    return hits,counters


def log_small(x,n=27):
    # 2*atanh(u); x lies in [1,2], so u <= 1/3.
    u=(x-1)/(x+1); power=u; acc=0
    for j in range(n):
        acc+=2*power/(2*j+1);power*=u*u
    return acc,acc+2*power/((2*n+1)*(1-u*u))

LN2=log_small(Fraction(2))
@cache
def bounds_ln(x):
    assert x>=1
    k=0
    while x>=2:x/=2;k+=1
    lo,hi=log_small(x)
    return lo+k*LN2[0],hi+k*LN2[1]
@cache
def cost_enclosure(b,a):
    lo,hi=bounds_ln(Fraction(b,a));p,q=bounds_ln(Fraction(10));scale=10**12
    return (scale*p//hi, -((-scale*q)//lo))

def verify_topology():
    def weight(edges):
        return tuple(sum(bounds_ln(Fraction(p))[i]*bounds_ln(Fraction(q))[i]
                         for p,q in edges) for i in (0,1))
    def cut(left,right):return [(p,q) for p in left for q in right]
    for remaining,expected in [
        (cut([5,13],[17,29]),True),(cut([5,17],[13,29]),False),
        (cut([5,29],[13,17]),False),(cut([5,13],[17,37]),False),
        (cut([5,17],[13,37]),False),(cut([5,37],[13,17]),False),
        (cut([5],[13,17,29,37,41]),True),(cut([5],[13,17,29,37,53]),False),
        (cut([13],[5,17,29,37,41]),False),(cut([5],[13,17,29,37,41,53]),False),
        (cut([5,13],[17,29])+[(5,13)],False),
        (cut([5],[13,17,29,37,41])+[(5,13)],False)]:
        low,high=weight(remaining)
        assert high<26 if expected else low>26

def plane_atoms(left,right,H):
    norm=lambda group:prod(p for p,e in group)
    def powers(group):
        base=(1,0)
        for p,e in group:
            x,y=split(p);base=times(base,(x,e*y))
        out=[(0,(1,0),1)];pair=(1,0);w=1;t=0
        while w*norm(group)<2*H*H:
            w*=norm(group);pair=times(pair,base);t+=1
            out += [(t,pair,w),(-t,(pair[0],-pair[1]),w)]
        return out
    atoms=[]
    for (u,z,n1),(v,w,n2) in product(powers(left),powers(right)):
        if u==v==0 or n1*n2>=2*H*H:continue
        base=times(z,w)
        for e in (0,1):
            value=times(base,(1,1)) if e else base
            for k in range(4):
                b,a=value;value=(-a,b)
                if 0<a<b<=H:
                    atom=Atom(b,a,0,(e+2*k)%8,{0:u,1:v})
                    exact,vec=signature(b,a)
                    declared={p:sg*t for grp,t in [(left,u),(right,v)] for p,sg in grp if t}
                    assert exact==atom.eps and declared==vec
                    atoms.append(atom)
    assert len({(a.b,a.a) for a in atoms})==len(atoms)
    return sorted(atoms,key=lambda a:(a.b,a.a))

def shell_search(writer=None):
    verify_topology()
    k22=[(((5,1),(13,u)),((17,1),(29,v))) for u,v in product((1,-1),repeat=2)]
    star=[(((5,1),),tuple(zip((13,17,29,37,41),(1,)+t))) for t in product((1,-1),repeat=4)]
    counters={};rows=[]; all_min=None; all_bits=None
    for family,planes in [("K22",k22),("K15",star)]:
        n_at=n_cir=n_hit=n_pr=0
        for left,right in planes:
            atoms=plane_atoms(left,right,10**6);n_at+=len(atoms)
            for triple in combinations(atoms,3):
                kind,cs=classify(triple)
                if kind not in {"even","odd"}:continue
                n_cir+=1
                if kind=="even":continue
                n_hit+=1
                winding,crossings=cert(triple,cs)
                intervals=[cost_enclosure(a.b,a.a) for a in triple]
                lower,upper=map(sum,zip(*intervals))
                if all_min is None or upper<all_min[0]:
                    all_min=(lower,upper,triple,cs,winding)
                elif lower<all_min[1]:
                    assert triple==all_min[2], "unresolved interval comparison"
                bits=sum(a.b.bit_length() for a in triple)
                all_bits=bits if all_bits is None else min(all_bits,bits)
                if writer is not None:
                    writer.writerow([family,(left,right),[(a.a,a.b) for a in triple],
                                     cs,bits,sum(map(abs,cs)),max(a.b for a in triple),
                                     lower,upper,winding,crossings])
                if winding:continue
                n_pr+=1
                rows.append((sum(a.b.bit_length() for a in triple),
                             sum(x[0] for x in intervals),sum(x[1] for x in intervals),
                             sum(map(abs,cs)),max(a.b for a in triple),
                             tuple((a.a,a.b) for a in triple),cs,crossings))
        counters[family]=(len(planes),n_at,n_cir,n_hit,n_pr)
    print("shell: planes, atom incidences, minimal circuits, targetable, principal",counters)
    def front(rows,resources):
        kept=[]
        for row in sorted(rows,key=lambda r:(r[0],r[1],r[3],r[4])):
            cut=False
            for old in kept:
                if all(old[i]<=row[i] for i in resources):
                    if old[2]<row[1]:cut=True;break
                    assert row[2]<old[1] or old[5]==row[5],("unresolved analytic ordering",old,row)
            if not cut:kept.append(row)
        return kept
    bi=front(rows,(0,));multi=front(rows,(0,3,4))
    assert counters=={"K22":(4,236,104776,52373,19631),"K15":(16,998,253164,126406,46056)}
    assert (len(bi),len(multi))==(12,80)
    print("best across all endpoints",all_min,"minimum bits",all_bits)
    print("shell fronts: (bits,mu) / (bits,mu,coefficient l1,max height)",len(bi),len(multi))
    for row in bi:print("SHELL_BI",row)
    for row in multi:print("SHELL_MULTI",row)
    return counters,bi,multi

if __name__=="__main__":
    bit_search()
    small=sum(cost_enclosure(b,a)[1] for b,a in [(79,3),(278,29)])
    witness=sum(cost_enclosure(b,a)[1] for b,a in [(57,1),(79,3),(239,1)])
    assert small<1723*10**9 and witness<sum(cost_enclosure(b,a)[0] for b,a in [(79,3),(278,29)])
    # Resource lower bound 9 log2(10)/B against one known pair per budget block.
    for B,pair in [(6,[(3,1),(7,1)]),(9,[(7,1),(11,2)]),
                   (13,[(7,1),(79,3)]),(15,[(46,9),(239,1)]),(17,[(79,3),(278,29)])]:
        lower=9*bounds_ln(Fraction(10))[0]/(B*LN2[1])
        assert lower*10**12>sum(cost_enclosure(b,a)[1] for b,a in pair)
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--circuits",help="write all targetable shell circuits and their lift certificates to CSV")
    opts=parser.parse_args()
    if opts.circuits:
        with open(opts.circuits,"x",newline="") as file:
            writer=csv.writer(file)
            writer.writerow(["topology","plane","atoms_(a,b)","target_coefficients","bits",
                             "coefficient_l1","height","mu_lower_e-12","mu_upper_e-12",
                             "full_windings","positive_ray_crossings"])
            shell_search(writer)
    else:
        shell_search()
