"""Finite matrix-idempotent fibers and named trace observations, standard library only."""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
from math import gcd, prod
import json


def factor(n):
    result = {}
    p = 2
    while p*p <= n:
        while n % p == 0:
            result[p] = result.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        result[n] = 1
    return result


def vp(x,p,cap):
    k = 0
    while k < cap and x%p == 0:
        x //= p
        k += 1
    return k


def gauss(n,r,p):
    return prod(p**n-p**i for i in range(r))//prod(p**r-p**i for i in range(r))


def residue_rank(b,d,p):
    rows = [list(b[d*i:d*i+d]) for i in range(d)]
    r = 0
    for j in range(d):
        i = next((i for i in range(r,d) if rows[i][j]%p),None)
        if i is None:
            continue
        rows[r],rows[i] = rows[i],rows[r]
        inv = pow(rows[r][j], -1, p)
        for i in range(r+1,d):
            c = rows[i][j]*inv
            rows[i] = [(x-c*y)%p for x,y in zip(rows[i],rows[r])]
        r += 1
    return r


def is_projector(v,d,n):
    if d == 2:
        a,b,c,h = v
        return (a*a+b*c-a)%n == 0 and (b*(a+h-1))%n == 0 and (c*(a+h-1))%n == 0 and (h*h+b*c-h)%n == 0
    return all((sum(v[i*d+t]*v[t*d+j] for t in range(d))-v[i*d+j])%n == 0
               for i in range(d) for j in range(d))


def predicted_count(n,m,d,data):
    ans = 1
    for p,e in factor(n).items():
        b = vp(m,p,e)
        if b:
            r = residue_rank(data,d,p)
            ans *= p**(2*r*(d-r)*(e-b))
        else:
            ans *= sum(gauss(d,r,p)*p**((2*e-1)*r*(d-r)) for r in range(d+1))
    return ans


def no_factor_unique(n,m,d,data):
    """m is observed modulus N/g. The input in this check is known to be compatible."""
    g = n//m
    ell = n.bit_length()
    hidden = n//gcd(n,pow(m,ell,n))
    s = gcd(g,m)
    h0 = gcd(m,*data)
    h1 = gcd(m,*(x-int(i//d==i%d) for i,x in enumerate(data)))
    return hidden == 1 and gcd(s,pow(h0*h1,ell,s)) == s


def actual_fibers(n,d):
    by_modulus = {}
    divisors = [m for m in range(1,n+1) if n%m==0]
    for m in divisors:
        by_modulus[m]=Counter()
    total = 0
    for v in product(range(n),repeat=d*d):
        if not is_projector(v,d,n):
            continue
        total += 1
        for m,counts in by_modulus.items():
            counts[tuple(x%m for x in v)] += 1
    for m,counts in by_modulus.items():
        for low,actual in counts.items():
            assert predicted_count(n,m,d,low) == actual
            assert no_factor_unique(n,m,d,low) == (actual==1)
    return {"N":n,"d":d,"projectors":total,
            "fibers_by_observed_modulus":{str(m):len(c) for m,c in by_modulus.items()}}


def trace_2x2(c,b,n):
    return (c[0]*b[0]+c[1]*b[2]+c[2]*b[1]+c[3]*b[3])%n


def mm(a,b,n):
    return tuple(sum(a[2*i+h]*b[2*h+j] for h in range(2))%n
                 for i in range(2) for j in range(2))


def public_trace_test(n,m,low,c):
    # Two by two instance of the coordinate-free criterion in the note.
    hidden=n//gcd(n,pow(m,n.bit_length(),n))
    if any(x%hidden for x in c):
        return False
    vis=n//hidden
    if vis==1:
        return True
    P=tuple(x%vis for x in low)
    while not is_projector(P,2,vis):
        p2=mm(P,P,vis)
        p3=mm(P,p2,vis)
        P=tuple((3*x-2*y)%vis for x,y in zip(p2,p3))
    Q=tuple((int(i in (0,3))-x)%vis for i,x in enumerate(P))
    pc,qc=mm(P,c,vis),mm(Q,c,vis)
    if any(m*x%vis for x in mm(pc,Q,vis)+mm(qc,P,vis)):
        return False
    pp,qq=mm(pc,P,vis),mm(qc,Q,vis)
    for j in range(4):
        E=tuple(int(i==j) for i in range(4))
        Y=mm(mm(Q,E,vis),P,vis)
        if any(m*m*(x-y)%vis for x,y in zip(mm(Y,pp,vis),mm(qq,Y,vis))):
            return False
    return True


def whole_ring_traces():
    tests=0
    for n in (4,6,8,9,12,18):
        matrices=[v for v in product(range(n),repeat=4) if is_projector(v,2,n)]
        for m in range(1,n+1):
            if n%m:
                continue
            grouped=defaultdict(list)
            for v in matrices:
                grouped[tuple(x%m for x in v)].append(v)
            families=((1,0,0,0),(0,1,0,0),(1,0,0,1),(2,3,6,5),(6,0,0,0))
            for low,lifts in grouped.items():
                for c in families:
                    constant=len({trace_2x2(c,v,n) for v in lifts})==1
                    assert public_trace_test(n,m,low,c)==constant
                    tests+=1
    return tests


def chart_checks(p,e,b):
    n,h = p**e,p**b
    chart = {((1+y*z)%n,(-z)%n,(y+y*y*z)%n,(-y*z)%n)
             for y,z in product(range(0,n,h),repeat=2)}
    assert len(chart)==(n//h)**2 and all(is_projector(v,2,n) for v in chart)
    if n<=27:
        direct = {v for v in product(range(1,n,h),range(0,n,h),range(0,n,h),range(0,n,h))
                  if is_projector(v,2,n)}
        assert direct == chart
    tested = 0
    for P,Q,R,S in product(range(4),repeat=4):
        counts=Counter(trace_2x2((P,Q,R,S),v,n) for v in chart)
        expected=Counter()
        for y in range(0,n,h):
            coeff=(P-S)*y+Q*y*y-R
            step=gcd(n,h*coeff)
            for t in range((P+Q*y)%step,n,step):
                expected[t]+=step//h
        assert counts==expected
        exp=min(e,b+vp(Q,p,e),b+vp(R,p,e),2*b+vp(P-S,p,e))
        assert gcd(n,*(t-P for t in counts))==p**exp
        tested+=1
    named=Counter(trace_2x2((1,0,0,0),v,n) for v in chart)
    return {"p":p,"e":e,"b":b,"fiber_size":len(chart),"traces_checked":tested,
            "first_entry_histogram":dict(sorted(named.items()))}


def ramanujan(p,l,t):
    if l==0:
        return 1
    q=p**l
    return q-q//p if t%q==0 else -q//p if t%(q//p)==0 else 0


def smith_hist(T, valuations, p, h, case):
    q=p**h
    k=len(T)
    counts=Counter()
    for v in product(range(q),repeat=k):
        tv=[sum(T[i][j]*v[j] for j in range(k))%q for i in range(k)]
        for w in product(range(q),repeat=k):
            counts[sum(a*b for a,b in zip(tv,w))%q]+=1
    factors=[Fraction(1,p**sum(max(0,l-a) for a in valuations)) for l in range(h+1)]
    for t in range(q):
        prob=sum(ramanujan(p,l,t)*f for l,f in enumerate(factors))/q
        assert Fraction(counts[t],q**(2*k))==prob
    return {"case":case,"p":p,"h":h,"smith_valuations_capped":valuations,
            "pair_count":q**(2*k),"histogram":dict(sorted(counts.items()))}


def named_mod8():
    lifts = [v for v in product(*[range(x,8,2) for x in (1,0,0,0)]) if is_projector(v,2,8)]
    yes = 0
    for c in product(range(8),repeat=4):
        exact = len({trace_2x2(c,v,8) for v in lifts}) == 1
        assert exact == public_trace_test(8,2,(1,0,0,0),c)
        yes += exact
    return {"instruments":8**4, "predictable":yes, "lifts":len(lifts)}

def main():
    fibers=[actual_fibers(n,2) for n in (2,3,4,5,6,8,9,10,12,15,16)]
    fibers.extend(actual_fibers(n,3) for n in (2,3,4))
    charts=[chart_checks(*row) for row in ((2,3,1),(2,4,1),(2,5,2),(3,3,1),(3,4,1),(5,3,1))]
    hist=[smith_hist([[1]],[0],3,2,"rank one and rank one"),
          smith_hist([[2,1],[0,2]],[0,2],2,3,"P=3, S=[[1,-1],[0,1]]"),
          smith_hist([[0,0],[0,1]],[2,0],3,2,"P=1, S=diag(1,0)")]
    print(json.dumps({"full_matrix_enumerations":fibers,"local_chart_checks":charts,
        "global_factor_free_trace_tests":whole_ring_traces(),"named_E11_mod8":named_mod8(),
        "bilinear_character_checks":hist,"zero_read_mod8_rank_counts_d2":
        [gauss(2,r,2)*2**(5*r*(2-r)) for r in range(3)]},sort_keys=True,indent=2))


if __name__=='__main__':
    main()
