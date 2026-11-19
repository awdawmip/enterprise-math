"""Exact finite arithmetic on the first published PFSSV cell. No random sampling."""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha256
from itertools import combinations, product
import json
from math import comb, gcd, isqrt, prod
from pathlib import Path


SOURCE = 'research_artifacts/PFSSV_REVISION_20260908/cell_profiles.jsonl'
LINE_SHA = 'fcfc138fbbddacd089c228b4cb3783e55064b9c9879d84f5de642911ebc860a0'
RESIDUES = (1,7,11,13,17,19,23,29)


def choose(n,k):
    return comb(n,k) if 0<=k<=n else 0


def hyper(n,holes,draw):
    return tuple(F(choose(holes,i)*choose(n-holes,draw-i),choose(n,draw)) for i in range(draw+1))


@lru_cache(None)
def empty(n,holes,r):
    return F(choose(holes,r),choose(n,r))


def read(repo):
    with (repo/SOURCE).open('rb') as stream:
        line = stream.readline()
    assert sha256(line).hexdigest()==LINE_SHA
    cell=json.loads(line)
    masks={}
    valid={}
    prime=lambda q:q>=2 and all(q%d for d in range(2,isqrt(q)+1))
    observed=[]
    for row in cell['rows']:
        p=row['p']
        lo,hi=max(p,100000//p+1),101000//p
        assert (lo,hi)==(row['qlo'],row['qhi'])
        addresses=set(range(lo,hi+1))
        counts=Counter(q%30 for q in addresses if prime(q))
        assert [counts[i] for i in range(30)]==row['q_mod_30_counts']
        masks[p]=addresses
        valid[p]={q for q in addresses if gcd(q,30)==1}
        if not sum(counts.values()):
            observed.append(p)
    unique=set.union(*masks.values())
    strata=[{q for q in unique if q%30==b} for b in RESIDUES]
    n=tuple(map(len,strata))
    k=tuple(sum(map(prime,s)) for s in strata)
    assert len(unique)==2016 and len(observed)==cell['zero_prime_count_rows']==15
    assert sum(map(prime,unique))==sum(k)
    return valid,strata,n,k,observed


def degrees(rows,strata,n,k):
    holes=tuple(x-y for x,y in zip(n,k))
    sizes={p:tuple(len(S&r) for r in strata) for p,S in rows.items()}
    overlap={(p,q):tuple(len(rows[p]&rows[q]&r) for r in strata) for p,q in combinations(rows,2)
             if rows[p]&rows[q]}
    assert overlap=={(239,241): (0,0,0,0,0,0,0,1)}
    # Monomial degree: a single p-subset, a two-row union, or a three-row union.
    top=[]
    for count in (1,2,3):
        hist=Counter(); attainers=defaultdict(list)
        for bundle in combinations(rows,count):
            r=list(map(sum,zip(*(sizes[p] for p in bundle))))
            if 239 in bundle and 241 in bundle:
                r[-1]-=1
            d=-1 if any(a>b for a,b in zip(r,holes)) else sum(min(a,b) for a,b in zip(r,k))
            hist[d]+=1
            if len(attainers[d])<2:
                attainers[d].append(bundle)
        vals=sorted(hist,reverse=True)
        top.append({'degree':vals[0],'second_distinct_degree':vals[1],'count_at_top':hist[vals[0]],
                    'top_rows':attainers[vals[0]],'subsets_tested':sum(hist.values())})
    assert [(a['degree'],a['count_at_top']) for a in top]==[(132,1),(215,1),(236,1)]
    # Pair-switch witnesses for independent top parts of all rows of each fixed size.
    groups=defaultdict(list)
    for p,s in rows.items(): groups[len(s)].append(p)
    for d,ps in groups.items():
        if d==0: continue
        assert all(not rows[p]&rows[q] for p,q in combinations(ps,2))
        used=set.union(*(rows[p] for p in ps))
        for p in ps:
            assert all(min(len(r-used),n0-h0,h0)>=len(rows[p]&r)
                       for r,n0,h0 in zip(strata,n,holes))
    rank={t:sum(len(S)>t for S in rows.values()) for t in range(133)}
    return sizes,top,rank


@lru_cache(None)
def polynomials(n,h,r,t):
    w=hyper(n,h,r)
    basis=[]
    for j in range(min(t,sum(x>0 for x in w)-1)+1):
        v=[F(x**j) for x in range(r+1)]
        for prev,norm in basis:
            factor=sum(a*b*c for a,b,c in zip(w,v,prev))/norm
            v=[x-factor*y for x,y in zip(v,prev)]
        norm=sum(a*b*b for a,b in zip(w,v))
        assert norm>0
        basis.append((tuple(v),norm))
    return tuple(basis)


@lru_cache(None)
def shared_layer(n,h,r,s,b,t):
    # The event for row R conditions every one of its r sites to be a hole.
    # Remaining marked sites in S have the ordinary conditional hypergeometric law.
    if max(r,s)>h: return (F(0),)*(t+1)
    wr,ws=empty(n,h,r),empty(n,h,s)
    law=hyper(n-r,h-r,s-b)
    out=[]
    for v,norm in polynomials(n,h,s,t):
        cond=sum(a*v[b+i] for i,a in enumerate(law))
        out.append(wr*ws*v[s]*cond/norm)
    out.extend([F(0)]*(t+1-len(out)))
    return tuple(out)


def convolve(a,b,t):
    return [sum(a[i]*b[k-i] for i in range(k+1)) for k in range(t+1)]


def deviations(rows,strata,n,k,sizes,t=3):
    h=tuple(x-y for x,y in zip(n,k))
    mean=sum(prod(empty(x,y,r) for x,y,r in zip(n,h,sizes[p])) for p in rows)
    second=F(0)
    norm_parts=[F(0)]*(t+1)
    for p,q in combinations_with_diagonal(list(rows)):
        b=[len(rows[p]&rows[q]&g) for g in strata]
        both=prod(empty(x,y,r+s-i) for x,y,r,s,i in zip(n,h,sizes[p],sizes[q],b))
        layers=[F(1)]+[F(0)]*t
        for args in zip(n,h,sizes[p],sizes[q],b):
            layers=convolve(layers,shared_layer(*args,t),t)
        mult=1 if p==q else 2
        second+=mult*both
        norm_parts=[v+mult*w for v,w in zip(norm_parts,layers)]
    assert mean**2==norm_parts[0] and min(norm_parts)>0
    high=[second-sum(norm_parts[:i+1]) for i in range(t+1)]
    assert min(high)>0
    return dict(expected_empty_rows=str(mean),variance=str(second-mean**2),
                residual_norm_squared_for_total_t0_to_t3=list(map(str,high)),
                residual_norm_rounded=[round(float(x)**0.5,9) for x in high])


def combinations_with_diagonal(keys):
    for i,p in enumerate(keys):
        for q in keys[i:]:
            yield p,q


def check_small():
    # Two slices with 18 equally likely configurations; compare all four degree components.
    groups=(set(range(4)),set(range(4,7)))
    n,k=(4,3),(2,1)
    worlds=[set(a)|set(b) for a,b in product(combinations(groups[0],2),combinations(groups[1],1))]
    # Build an independent orthogonal basis from every address monomial on the 18 worlds.
    orth=[]
    for j in range(4):
        for mon in combinations(range(7),j):
            v=[F(set(mon)<=w) for w in worlds]
            for _,u,norm in orth:
                z=sum(a*b for a,b in zip(u,v))/norm
                v=[a-z*b for a,b in zip(v,u)]
            norm=sum(a*a for a in v)
            if norm: orth.append((j,v,norm))
    assert len(orth)==len(worlds)
    total=0
    for A,B in product((set(),{0,4},{0,1,5},{0,2,4,5}), repeat=2):
        degree=3
        coeff=[F(1)]+[F(0)]*degree
        for ng,kg,g in zip(n,k,groups):
            a,b=A&g,B&g
            parts=shared_layer(ng,ng-kg,len(a),len(b),len(a&b),degree)
            rev=shared_layer(ng,ng-kg,len(b),len(a),len(a&b),degree)
            assert parts==rev
            coeff=convolve(coeff,parts,degree)
        assert sum(coeff)==F(sum(not w&(A|B) for w in worlds),len(worlds))
        direct=[F(0)]*(degree+1)
        for j,v,norm in orth:
            direct[j]+=(sum(a for a,w in zip(v,worlds) if not A&w)
                        *sum(a for a,w in zip(v,worlds) if not B&w)/(len(worlds)*norm))
        assert coeff==direct
        total+=1
    pairs=((0,1),(2,3),(4,5))
    cube=[(frozenset(pair[bit] for pair,bit in zip(pairs,bits)),(-1)**sum(bits))
          for bits in product(range(2),repeat=3)]
    for j in range(3):
        for target in combinations(range(7),j):
            assert sum(s for w,s in cube if set(target)<=w)==0
    return dict(exact_mixed_layer_checks=total,worlds=len(worlds),top_trade_configurations=len(cube))


def budget_top(n,k,rg):
    weights=[hyper(ng,r,kg) for ng,kg,r in zip(n,k,rg)]
    best=[(F(1),[]),None]
    inverse_norm=F(1); simplified=F(1)
    for ng,kg,r,law in zip(n,k,rg,weights):
        assert all(law) and kg<=min(r,ng-r)
        nxt=[None,None]
        for c,w in enumerate(law):
            for parity,state in enumerate(best):
                if state is None: continue
                weight,word=state
                value=(weight*w/comb(kg,c),word+[c])
                bit=parity^(c%2)
                if nxt[bit] is None or value<nxt[bit]:
                    nxt[bit]=value
        best=nxt
        one=sum(F(comb(kg,c)**2)/w for c,w in enumerate(law))
        closed=F(comb(ng,kg)*comb(ng-kg+1,kg),comb(r,kg)*comb(ng-r,kg))
        assert one==closed
        inverse_norm*=one; simplified*=closed
    baseline=prod(w[0] for w in weights)
    low,high=-best[0][0],best[1][0]
    assert inverse_norm==simplified
    relative=prod(min(F(1),F(comb(r,kg),comb(ng-r,kg))) for r,ng,kg in zip(rg,n,k))
    assert high/baseline==-low/baseline==relative==F(1,23381581125)
    return {'union_by_residue':rg,'p0_empty':str(baseline),
            'delta_from_p0_feasible_interval':[str(low),str(high)],
            'relative_interval_for_probability':list(map(str,[1+low/baseline,1+high/baseline])),
            'relative_edit_rounded':[float(low/baseline),float(high/baseline)],
            'chi_squared_coefficient':str(inverse_norm),'top_projection_squared_norm':str(1/inverse_norm),
            'relative_radius':str(relative),
            'witness_at_negative_and_positive_ends':[best[0][1],best[1][1]],
            'min_TV_per_absolute_change':str(2**(sum(k)-1))}


def main(repo):
    rows,groups,n,k,observed=read(repo)
    sizes,top,rank=degrees(rows,groups,n,k)
    rho=F(40,69); sigma=F(45,70)
    pair=[rho*sigma,max(F(0),rho+sigma-1),min(rho,sigma),rho*(1-rho)*sigma*(1-sigma)]
    # Choose one occupied site in each switch pair. All-outside is the unique vertex
    # where the union of rows 2,3,5 is empty.
    union=rows[2]|rows[3]|rows[5]
    cube_pairs=[]
    for g,kg in zip(groups,k):
        a=sorted(g&union)[:kg]; b=sorted(g-union)[:kg]
        assert len(a)==len(b)==kg
        cube_pairs.extend(zip(a,b))
    assert len({z for pair0 in cube_pairs for z in pair0})==472
    return dict(first_cell_line_sha256=LINE_SHA,unit_residues=RESIDUES,n=n,occupied=k,
                actual_empty_rows=observed,degree_top_by_number_of_rows=top,
                row_ambiguity_ranks_at_changes={t:v for t,v in rank.items() if not t or rank[t-1]!=v},
                surrogate_exact_moments=deviations(rows,groups,n,k,sizes),
                example_239_241=dict(intersection=[419],reference_239=str(pair[0]),
                   feasible_239_given_all_singletons=list(map(str,pair[1:3])),chi_squared_denominator=str(pair[3])),
                three_row_top_budget=budget_top(n,k,[len(g&union) for g in groups]),
                minimum_edit_support=str(2**sum(k)),disjoint_switch_pairs=cube_pairs,
                small_exhaustion=check_small())


if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--repo',type=Path,required=True)
    print(json.dumps(main(ap.parse_args().repo),indent=2,sort_keys=True))
