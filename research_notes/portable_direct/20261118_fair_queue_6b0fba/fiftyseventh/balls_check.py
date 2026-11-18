"""Exact projective incidence, frozen good sets and shared prime seeds. Stdlib."""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations, product
from math import comb, gcd, isqrt, prod
import hashlib
import json
import random


def projective(p, dim=6):
    for i in range(dim):
        for rest in product(range(p), repeat=dim-1-i):
            yield (0,)*i+(1,)+rest


def projective_size(p, dim=6):
    return (p**dim-1)//(p-1)


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


def tag(v,p):
    inv=pow(next(x for x in v if x%p),-1,p)
    return tuple(x*inv%p for x in v)


def rotate(v):
    # Multiplication by x in Z[x]/(1+x+...+x^6), pinned power basis.
    return (-v[-1],) + tuple(x-v[-1] for x in v[:-1])


def ball(bound):
    def extend(prefix,remaining):
        if len(prefix)==6:
            if any(prefix) and next(x for x in prefix if x)>0:
                yield prefix
            return
        for x in range(-isqrt(remaining),isqrt(remaining)+1):
            yield from extend(prefix+(x,),remaining-x*x)
    yield from extend((),bound)


def null_basis(rows,p):
    rows=[[x%p for x in v] for v in rows]
    pivots=[]
    for col in range(6):
        rank=len(pivots)
        pivot=next((j for j in range(rank,len(rows)) if rows[j][col]),None)
        if pivot is None:
            continue
        rows[rank],rows[pivot]=rows[pivot],rows[rank]
        scale=pow(rows[rank][col],-1,p)
        rows[rank]=[x*scale%p for x in rows[rank]]
        for j,other in enumerate(rows):
            if j!=rank:
                mul=other[col]
                rows[j]=[(a-mul*b)%p for a,b in zip(other,rows[rank])]
        pivots.append(col)
    basis=[]
    for col in set(range(6))-set(pivots):
        v=[0]*6
        v[col]=1
        for j,c in enumerate(pivots):
            v[c]=-rows[j][col]%p
        basis.append(tuple(v))
    return basis


def good_complement(p):
    """Exactly the frozen 42^3 Q(v)^3 < p^s veto at levels 1..5, inert primes."""
    assert p%7 in (3,5)
    bad=set()
    rows=[]
    for s in range(1,6):
        bound=0
        while 42**3*(bound+1)**3<p**s:
            bound+=1
        layer=set()
        vectors=list(ball(bound))
        for v in vectors:
            orbit=[]
            w=v
            for _ in range(s):
                orbit.append(w)
                w=rotate(w)
            kernel=null_basis(orbit,p)
            assert len(kernel)==6-s
            for coefs in projective(p,len(kernel)):
                normal=tag(tuple(sum(a*k[j] for a,k in zip(coefs,kernel))
                                 for j in range(6)),p)
                assert all(dot(normal,w)%p==0 for w in orbit)
                layer.add(normal)
        rows.append({'s':s,'max_squared_norm':bound,'sign_classes':len(vectors),
                     'excluded_hyperplanes':len(layer)})
        bad.update(layer)
    return bad,rows


def finite_design(p):
    points=list(projective(p))
    inc=[]
    for v in points:
        inc.append(sum(1<<j for j,h in enumerate(points) if dot(v,h)%p==0))
    n=len(points)
    d=projective_size(p,5)
    pair=projective_size(p,4)
    assert all(bits.bit_count()==d for bits in inc)
    assert all((a&b).bit_count()==pair for a,b in combinations(inc,2))
    # Deliberately nonuniform set of hyperplanes for the exact norm identity.
    selected=sum(1<<j for j in range(n) if j%13!=0)
    g=selected.bit_count()
    lhs=sum((F((bits&selected).bit_count(),g)-F(d,n))**2 for bits in inc)
    assert lhs==F(p**4*(n-g),n*g)
    return {'p':p,'points':n,'pairs':n*(n-1)//2,'hyperplanes_retained':g,
            'gram_diagonal':d,'gram_off_diagonal':pair,'squared_norm':str(lhs)}


def mask(v):
    return sum(1<<j for j,x in enumerate(v) if not x)


def support_table(p,bad):
    full={s:(p-1)**(5-s.bit_count()) for s in range(63)}
    for h in bad:
        full[mask(h)]-=1
    assert sum(full.values())==projective_size(p)-len(bad)
    return full


def exact_shared(tables):
    primes=sorted(tables)
    masses=[tables[p] for p in primes]
    hist=Counter()
    edge_counts=[0]*3
    first_two=0
    total=prod(sum(a.values()) for a in masses)
    for (a,n),(b,m),(c,k) in product(*(d.items() for d in masses)):
        events=[bool(a&b),bool(a&c),bool(b&c)]
        weight=n*m*k
        hist[sum(events)]+=weight
        for j,event in enumerate(events):
            if event:
                edge_counts[j]+=weight
        if events[0] and events[1]:
            first_two+=weight
    probs=[F(v,total) for v in edge_counts]
    cov=F(first_two,total)-probs[0]*probs[1]
    assert sum(hist.values())==total and cov>0
    return {'primes':primes,'sample_space':total,'edge_probs':[str(x) for x in probs],
            'joint_bad_count_histogram':dict(sorted(hist.items())),
            'covariance_two_edges_sharing_prime_5':str(cov)}


def uniform_seed(p,bad,rng):
    # Uniform nonzero vector projects uniformly on the dual lines.
    while True:
        h=tuple(rng.randrange(p) for _ in range(6))
        if any(h):
            h=tag(h,p)
            if h not in bad:
                return h


def sample_one_table(bads):
    rng=random.Random(5700917)
    ps=sorted(bads)
    hist=Counter()
    dig=hashlib.sha256()
    for _ in range(2048):
        seeds={p:uniform_seed(p,bads[p],rng) for p in ps}
        nbad=sum(bool(mask(seeds[p])&mask(seeds[q])) for p,q in combinations(ps,2))
        hist[nbad]+=1
        dig.update(bytes(x for p in ps for x in seeds[p]))
    return {'trials':2048,'rng_seed':5700917,'draws_per_table':len(ps),'histogram':dict(sorted(hist.items())),
            'normalized_seed_rows_sha256':dig.hexdigest()}


def unbalanced(bads):
    p,q=5,31
    vs=list(ball(26))
    dirs=[v for v in vs if gcd(*v)==1]
    loads=Counter(tag(v,p) for v in dirs)
    tags_q={tag(v,q) for v in dirs}
    assert len(tags_q)==len(dirs) and max(loads.values())>1
    hit_tests=0
    rng=random.Random(70531)
    # Compare sets of lines actually contributing, also when the Boolean union is already true.
    for _ in range(4):
        a=uniform_seed(p,bads[p],rng)
        b=uniform_seed(q,bads[q],rng)
        direct=set()
        for v in vs:
            if dot(a,v)%p==0 and dot(b,v)%q==0:
                g=gcd(*v)
                direct.add(tuple(x//g for x in v))
        formal={v for v in dirs if dot(b,v)%q==0 and
                (dot(a,v)%p==0 or p*p*dot(v,v)<=26)}
        assert formal==direct
        hit_tests+=len(vs)
    return {'p':p,'q':q,'squared_norm_at_most':26,'primitive_sign_classes':len(dirs),
            'nonprimitive_eligible_extra_directions':sum(p*p*dot(v,v)<=26 for v in dirs),
            'same_small_prime_label_pairs':sum(comb(b,2) for b in loads.values()),
            'p_label_maximum':max(loads.values()),'different_q_labels':len(tags_q),
            'raw_short_vector_checks':hit_tests}


def strict_ball():
    p,q=1000037,1000039
    n=p*q
    k=n.bit_length()-1
    bound=0
    while (42*k*(bound+1))**3<n:
        bound+=1
    vs=[v for v in ball(bound) if gcd(*v)==1]
    assert all(len({tag(v,ell) for v in vs})==len(vs) for ell in (p,q))
    return {'p':p,'q':q,'N':n,'k':k,'gamma':'1/2','max_squared_norm':bound,
            'primitive_sign_classes':len(vs),'different_direction_pairs':comb(len(vs),2)}


def main():
    bads={}
    certified=[]
    for p in (5,17,19,31):
        bads[p],layers=good_complement(p)
        full=projective_size(p)
        assert 64*(full-len(bads[p]))>=59*full
        certified.append({'p':p,'projective_seed_count':full,'frozen_good_seed_count':full-len(bads[p]),
                          'excluded_seed_count':len(bads[p]),'frozen_layer_certificates':layers})
    result={'finite_designs':[finite_design(p) for p in (2,3)],
            'actual_good_sets_inert_blocks':certified,'joint_six_axis_shell':exact_shared(
                {p:support_table(p,bads[p]) for p in (5,17,19)}),
            'joint_six_axis_shell_sampling':sample_one_table({p:bads[p] for p in (5,17,19)}),
            'unbalanced_witness_rays':unbalanced(bads),'frozen_large_pair':strict_ball()}
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
