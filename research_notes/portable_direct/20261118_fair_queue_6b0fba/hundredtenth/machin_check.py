"""Exact Gaussian endpoints, support and resource tests. Standard library, no input."""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
import json
from math import factorial, gcd, isqrt, prod


def primitive(z):
    d = gcd(*z)
    return z[0]//d, z[1]//d


def mul(z, w):
    a,b = z
    c,d = w
    return primitive((a*c-b*d, a*d+b*c))


def conj(z):
    return z[0], -z[1]


def power(z, n):
    if n < 0:
        return power(conj(z), -n)
    ans = (1,0)
    while n:
        if n & 1:
            ans = mul(ans,z)
        n //= 2
        if n:
            z = mul(z,z)
    return ans


def det(z, w):
    return z[0]*w[1]-z[1]*w[0]


def resources(atoms):
    assert len(set(atoms)) == len(atoms)
    assert all(0<a<b and gcd(a,b)==1 for b,a in atoms)
    q = [(b//a).bit_length()-1 for b,a in atoms]
    assert min(q) >= 1
    # Cost divided by log_2(10); bounds obtained solely by comparison with powers of two.
    lower = sum(Fraction(1,x+1) for x in q)
    upper = sum(Fraction(1,x) for x in q)
    return {'denominator_bit_sum': sum(b.bit_length() for b,a in atoms),
            'min_floor_log2_ratio': min(q),
            'cost_over_log2_10_enclosure': [str(lower),str(upper)]}


def root_chain(s,k,G,expand=False):
    old=(1,1)
    atoms=[]
    for j in range(1,s):
        lo,hi=0,G//k+1
        while lo+1<hi:
            m=(lo+hi)//2
            u=power((G,m),k)
            assert u[0]>0
            if det(u,old)>=0:
                lo=m
            else:
                hi=m
        assert det(power((G,lo),k),old)>=0 and det(power((G,lo+1),k),old)<0
        v=primitive((G,lo-4**j))
        w=power(v,k)
        rem=mul(old,conj(w))
        assert 0<rem[1]<rem[0] and 0<v[1]<v[0] and mul(rem,w)==old
        if atoms:
            assert det(atoms[-1],rem)>0
        atoms.append(rem)
        old=v
    assert det(atoms[-1],old)>0
    atoms.append(old)
    weights=[k**j for j in range(s)]
    if expand:
        z=(1,0)
        for a,c in zip(atoms,weights):
            z=mul(z,power(a,c))
        assert z==(1,1)
    return atoms,weights


def roots_evidence():
    rows=[]
    for s,k,full in [(3,2,True),(5,2,True),(8,2,True),(14,2,False),
                     (3,9,True),(5,9,False),(8,9,False),(10,9,False)]:
        G=k**(2*s*s)
        atoms,weights=root_chain(s,k,G,full)
        rows.append({'s':s,'k':k,'G':str(G),'largest_coefficient':weights[-1],
                     'full_direct_power':full,'verified_all_root_identities':len(atoms)-1,
                     **resources(atoms)})
    return rows


def primes_to(X):
    flags=bytearray([1])*(X+1)
    flags[:2]=bytes(2)
    for p in range(2,isqrt(X)+1):
        if flags[p]:
            flags[p*p::p]=bytes((X-p*p)//p+1)
    return flags


def directions(X):
    flags=primes_to(X)
    points=[]
    for u in range(2,isqrt(X)+1):
        for v in range(1,min(u-1,isqrt(X-u*u))+1):
            if flags[u*u+v*v]:
                points.append((u,v))
    norms={u*u+v*v for u,v in points}
    assert norms=={p for p in range(5,X+1,4) if flags[p]} and len(norms)==len(points)
    return points


def fixed_core(s):
    ds={0:(2,4,13),1:(2,5,21,13),2:(2,3)}[s%3]
    atoms=[(b,1) for b in ds]
    z=(1,0)
    for w in atoms:
        z=mul(z,w)
    assert z==(1,1)
    return atoms


def triangles(X,s):
    pts=directions(X)
    L=len(pts)
    # Slope interval [0,1]; the stated uniform lower bound alone supplies enough triangles.
    J=L*L//(9*(s+5)+4*L)
    assert J>=2
    bins=[[] for _ in range(J)]
    for u,v in pts:
        bins[(J*v)//u].append((u,v))
    available=sum((len(cell)//3)**2 for cell in bins)
    assert available>=s+5
    atoms=fixed_core(s)
    protected=set(atoms)
    signatures=set()
    z=(1,1)
    digest=sha256()
    used=0
    for cell in bins:
        cell.sort(key=lambda a: Fraction(a[1],a[0]))
        m=len(cell)//3
        for i in range(m):
            for j in range(m):
                t=[cell[i],cell[m+j],cell[2*m+(i+j)%m]]
                edges=[]
                for a,b in ((0,1),(1,2),(0,2)):
                    l,r=t[a],t[b]
                    atom=mul(conj(l),r)
                    N=prod(sum(x*x for x in p) for p in (l,r))
                    assert sum(x*x for x in atom)==N and atom[0]<=X and J*atom[1]<atom[0]
                    edges.append((atom,N))
                e1,e2,e3=(a for a,N in edges)
                assert mul(e1,e2)==e3
                if any(a in protected for a,N in edges):
                    continue
                assert all(N not in signatures for a,N in edges)
                signatures.update(N for a,N in edges)
                atoms.extend((e1,e2,e3))
                z=mul(z,mul(mul(e1,e2),conj(e3)))
                used+=1
                digest.update((','.join(str(v) for w in (e1,e2,e3) for v in w)+'\n').encode())
                if len(atoms)==s:
                    assert z==(1,1)
                    return {'X':X,'support':s,'split_primes':L,'bins':J,'available_triangles':available,
                            'used_triangles':used,'ordered_selected_edge_sha256':digest.hexdigest(),
                            'endpoint':list(z),**resources(atoms)}
    raise AssertionError('too few triples')


def dense_lower():
    rows=[]
    # Independent finite divisor-product envelopes. Treat even nonprimitive pairs as eligible.
    for s in (2,5,16,50,200,512):
        values=sorted(a*b for a in range(1,s+1) for b in range(1,s//a+1))[:s]
        H=sum(Fraction(1,i) for i in range(1,s+1))
        assert all(q*sum(Fraction(1,i) for i in range(1,j+1))>=j
                   for j,q in enumerate(values,1))
        assert prod(values)*H**s>=factorial(s)
        rows.append({'s':s,'last_product':values[-1],'min_product_all_pairs':str(prod(values))})
    return rows


def telescoping_path(X,s):
    pts=sorted(directions(X), key=lambda z: Fraction(z[1],z[0]))
    gaps=s-2
    def span(i):
        l,r=pts[i],pts[i+gaps]
        return Fraction(r[1],r[0])-Fraction(l[1],l[0])
    start=min(range(len(pts)-gaps), key=span)
    path=pts[start:start+gaps+1]
    arc=mul(conj(path[0]),path[-1])
    atoms=[mul((2,1),conj(arc)),(3,1)]
    for l,r in zip(path,path[1:]):
        a=mul(conj(l),r)
        assert a[0]<=X and det((1,0),a)>0
        assert sum(t*t for t in a)==sum(t*t for t in l)*sum(t*t for t in r)
        atoms.append(a)
    z=(1,0)
    for a in atoms:
        z=mul(z,a)
    assert z==(1,1) and len(atoms)==s and all(b>0 and a>0 for b,a in atoms)
    return {'s':s,'X':X,'first':path[0],'last':path[-1],'arc':arc,'all_coefficients':1,
            'endpoint':list(z),'slope_window_width':str(span(start)),**resources(atoms)}


def all_positive_example(s):
    old=5
    atoms,weights=root_chain(old,3,2**70)
    primes=(5,13,17,29)
    P=prod(primes)
    roots=[next(t for t in range(p) if t*t%p==p-1) for p in primes]
    sol=sum(t*(P//p)*pow(P//p,-1,p) for p,t in zip(primes,roots))%P
    start=1<<28
    u=start+(sol-start)%P
    a,b=u*u+1,(u+1)**2+1
    k=u*u+u+1
    assert a*b==k*k+1 and a%P==0
    atoms[-1]=mul(atoms[-1],(k,-1))
    pairs=(s-old)//2
    C=weights[-1]
    opt=sorted(prod(t) for j in range(len(primes)+1) for t in combinations(primes,j))
    count=0
    for d in opt:
        x,y=(k+a//d,1),(k+b*d,1)
        assert mul(x,y)==(k,1)
        if x in atoms or y in atoms:
            continue
        c=C-pairs+1 if count==0 else 1
        atoms.extend((x,y));weights.extend((c,c))
        count+=1
        if count==pairs:
            break
    assert count==pairs and len(atoms)==s and min(weights)>0
    z=(1,0)
    for atom,c in zip(atoms,weights):
        z=mul(z,power(atom,c))
    assert z==(1,1)
    return {'s':s,'core':old,'u':u,'P':P,'k':k,'endpoint':list(z),
            'all_coefficients_positive':True, **resources(atoms)}


def main():
    ans={'positive_variable_support_chains':roots_evidence(),
         'dense_signed_triangles':[triangles(x,s) for x,s in
                     ((4096,16),(12000,73),(30000,212),(100000,701),(200000,1620))],
         'all_positive_splittings':[all_positive_example(s) for s in (15,25,33)],
         'all_unit_positive_telescoping':[telescoping_path(X,s) for X,s in
                                         ((4096,12),(30000,67),(100000,207),(200000,513))],
         'divisor_envelope':dense_lower()}
    print(json.dumps(ans,indent=2,sort_keys=True))


if __name__=='__main__':
    main()
