"""Check two-by-two idempotent readouts using independent entrywise enumeration."""
import argparse
import itertools
import json
from collections import Counter
from pathlib import Path


def vp(x,p,cap):
    n = 0
    while n < cap and x % p == 0:
        n += 1
        x //= p
    return n


def primitive_mod_p(C,p):
    A,H,K,D=C
    roots=[t for t in range(p) if (t*t-(A+D)*t+A*D-H*K) % p == 0]
    return roots


def polynomial_root(poly,p,depth,start):
    """Lift a simple root using one digit and its unit derivative."""
    c0,c1,c2=poly
    x=start % p
    q=p
    assert (c0+c1*x+c2*x*x) % q == 0
    for _ in range(1,depth):
        f=c0+c1*x+c2*x*x
        x += q * (-(f//q) * pow(c1+2*c2*x,-1,p) % p)
        q *= p
        assert (c0+c1*x+c2*x*x) % q == 0
    return x


def product_counts(p,depth):
    q=p**depth
    if depth == 0:
        return [1]
    unit=(p-1)*p**(depth-1)
    return [(depth*unit+q) if v==0 else (1+vp(v,p,depth))*unit for v in range(q)]


def partial(p,e,b,C):
    """Frequency counts, for a known projection congruent to diag(1,0) mod p^b."""
    n=p**e
    size=p**(2*(e-b))
    A,H,K,D=C
    h=min(e,b+vp(H,p,e),b+vp(K,p,e),2*b+vp(A-D,p,e))
    if h==e:
        return Counter({A%n:size}),"point"
    q=p**(e-h)
    L=p**b*H//p**h
    k=p**b*K//p**h
    u=p**(2*b)*(A-D)//p**h
    if u % p == 0:
        assert L % p or k % p
        return Counter({(A+p**h*t)%n:size//q for t in range(q)}),"uniform"
    y0=polynomial_root((-k,u,p**(2*b)*L),p,e-h,k*pow(u,-1,p))
    center=A+p**h*L*y0
    scale=size//(q*q)
    return Counter({(center+p**h*t)%n:scale*f
                    for t,f in enumerate(product_counts(p,e-h))}),"translated_product"


def blind_rank_one(p,e,C):
    n=p**e
    total=p**(2*e-1)*(p+1)
    A,H,K,D=C
    v=min(vp(H,p,e),vp(K,p,e),vp(D-A,p,e))
    if v==e:
        return Counter({A%n:total}),"scalar"
    factor=p**v
    f=e-v
    q=p**f
    C0=(0,H//factor,K//factor,(D-A)//factor)
    a,h,k,d=C0
    roots=primitive_mod_p(C0,p)
    count_roots=len(roots)
    assert count_roots in (0,1,2)
    # Each mod-p noncritical idempotent lifts to p^(2(f-1)) projections.
    # Each individual readout in its congruence class has p^(f-1) lifts.
    counts=Counter()
    for t in range(q):
        nmod=p+1-count_roots+(p if t%p in roots else 0)
        if count_roots==2 and t%p in roots:
            nmod -= 1
        counts[t]=nmod*p**(f-1)
    if count_roots==2:
        c0=a*d-h*k
        lambdas=[polynomial_root((c0,-(a+d),1),p,f,t) for t in roots]
        for lam in lambdas:
            if f<=2:
                counts[lam]+=p**(2*(f-1))
            else:
                for t,mult in enumerate(product_counts(p,f-2)):
                    counts[(lam+p*p*t)%q]+=p*p*mult
    final=Counter({(A+factor*t)%n:m*p**(2*v) for t,m in counts.items() if m})
    assert sum(final.values())==total
    return final,["irreducible","Jordan","split"][count_roots]


def direct_idempotents(p,e):
    q=p**e
    rows=[]
    for a,h,k,d in itertools.product(range(q),repeat=4):
        if any(z%q for z in (a*a+h*k-a,h*(a+d-1),k*(a+d-1),d*d+h*k-d)):
            continue
        if not (a or h or k or d) or (a,h,k,d)==(1,0,0,1):
            continue
        assert (a+d)%q == 1
        rows.append((a,h,k,d))
    assert len(rows)==p**(2*e-1)*(p+1)
    return rows


def direct(C, matrices, q):
    a,h,k,d=C
    return Counter((a*x+k*y+h*z+d*w)%q for x,y,z,w in matrices)


def matrix_list(q,full):
    if full:
        return itertools.product(range(q),repeat=4)
    examples=[(1,0,0,1),(1,0,0,0),(0,1,0,0),(0,1,1,0),(3,2,4,7),
              (0,1,1,1),(1,2,2,0),(3,4,4,3),(0,2,2,2),(6,6,0,6)]
    # Fixed deterministic supplement to the corner cases.
    a=48271
    for j in range(160):
        row=[]
        for i in range(4):
            a=(a*48271)%2147483647
            row.append(a%q)
        examples.append(tuple(row))
    return sorted({tuple(x%q for x in row) for row in examples})


def multiply(U,V,q):
    a,b,c,d=U
    e,f,g,h=V
    return tuple(x%q for x in (a*e+b*g,a*f+b*h,c*e+d*g,c*f+d*h))


def named_non_diagonal(p,e,matrices):
    q=p**e
    S=(1,1,1,2)
    inverse=(2,-1,-1,1)
    observed=multiply(multiply(S,(1,0,0,0),q),inverse,q)
    tested=0
    for b in range(1,e+1):
        mod=p**b
        rows=[B for B in matrices if all((x-y)%mod==0 for x,y in zip(B,observed))]
        assert len(rows)==p**(2*(e-b))
        for C in matrix_list(q,False):
            C0=multiply(multiply(inverse,C,q),S,q)
            answer,_=partial(p,e,b,C0)
            assert answer==direct(C,rows,q)
            tested+=1
    return tested


def run():
    bank=[]
    examples=[]
    total_blind=total_partial=0
    for p,e,full in [(2,1,True),(2,2,True),(2,3,True),(2,4,False),(3,1,True),
                     (3,2,True),(3,3,False),(5,1,True),(5,2,False),(7,1,True)]:
        q=p**e
        mats=direct_idempotents(p,e)
        sub={b:[(x,y,z,w) for x,y,z,w in mats
                if (x%p**b,y%p**b,z%p**b,w%p**b)==(1,0,0,0)] for b in range(1,e+1)}
        modes=Counter()
        partial_modes=Counter()
        for C in matrix_list(q,full):
            target,mode=blind_rank_one(p,e,C)
            assert target == direct(C,mats,q)
            # Rank zero and rank two are the zero and identity projections.
            total=target.copy()
            total[0]+=1
            total[(C[0]+C[3])%q]+=1
            assert total==direct(C,mats+[(0,0,0,0),(1,0,0,1)],q)
            modes[mode]+=1
            total_blind+=1
            for b,rows in sub.items():
                prediction,submode=partial(p,e,b,C)
                assert prediction==direct(C,rows,q)
                partial_modes[submode]+=1
                total_partial+=1
        bank.append({"p":p,"e":e,"all_instruments":full,"rank_one_projections":len(mats),
                     "blind_tests":dict(sorted(modes.items())),
                     "visible_tests":dict(sorted(partial_modes.items())),
                     "additional_non_diagonal_named_endpoint_comparisons":named_non_diagonal(p,e,mats)})
    for e,b,C in [(3,0,(0,1,1,1)),(4,0,(1,0,0,0)),(4,0,(0,1,0,0)),
                  (4,0,(1,2,2,3)),(4,1,(1,2,2,0)),(4,1,(1,1,0,1)),
                  (4,2,(1,4,4,1))]:
        data,kind=blind_rank_one(2,e,C) if b==0 else partial(2,e,b,C)
        examples.append({"modulus":2**e,"b":b,"C":C,"law":kind,
                         "rank_one_histogram":dict(sorted(data.items()))})
    return {"convention":"C=(A,H,K,D) in row order; all algebraic idempotents in the specified fiber have equal weight",
            "literal_entrywise_tests":bank,"blind_distributions_verified":total_blind,
            "known_endpoint_distributions_verified":total_partial,"binary_examples":examples}


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    data=json.dumps(run(),indent=2,ensure_ascii=False)+"\n"
    if args.output:
        args.output.write_text(data)
    else:
        print(data,end="")
