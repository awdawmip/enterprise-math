"""External integer comparison only. Counts are state cardinalities, not probabilities."""
from collections import defaultdict
from itertools import product
import json
from math import isqrt


def factor(n):
    result = {}
    k = 2
    while k*k <= n:
        while n%k == 0:
            result[k] = result.get(k, 0)+1
            n //= k
        k += 1
    if n != 1:
        result[n] = 1
    return result


def counts(P, E):
    # Output ordered, fixed under one transposition, all equal, unordered,
    # third label kept, and distinct signed two-terminal impulses.
    if E < 0 or (E-P)%2 or 3*E < P*P:
        return (0,)*6
    M = (3*E-P*P)//2
    if M == 0:
        return (1,)*6 if P%3 == 0 else (0,)*6
    norm = 6
    for ell, exponent in factor(M).items():
        if ell%3 == 2 and exponent%2:
            return (0,)*6
        if ell%3 == 1:
            norm *= exponent+1
    ordered = norm if P%3 == 0 else norm//2
    root = isqrt(M)
    fixed = sum((P+b)%3 == 0 for b in (-root,root)) if root*root == M else 0
    unordered = (ordered+3*fixed)//6
    third = (ordered+fixed)//2
    fixed_impulse = 2 if M%3 == 0 and 3*isqrt(M//3)**2==M else 0
    impulses = (ordered+fixed_impulse)//2 if P%3 == 0 else ordered
    return ordered, fixed, 0, unordered, third, impulses


def measure(t):
    return sum(t), sum(v*v for v in t)


def contact(t, letter):
    x,y,z = t
    target = (y,x,z) if letter == "A" else (x,z,y)
    dp = tuple(j-i for i,j in zip(t,target))
    de = tuple(j*j-i*i for i,j in zip(t,target))
    assert sum(dp)==0 and sum(de)==0 and measure(t)==measure(target)
    if letter == "A":
        assert dp[2]==de[2]==0 and dp[0]==-dp[1]
    else:
        assert dp[0]==de[0]==0 and dp[1]==-dp[2]
    return target, dp, de


def impulse_candidates(P,E,A):
    rad = 2*(3*E-P*P)-3*A*A
    if rad < 0:
        return set()
    r=isqrt(rad)
    if r*r != rad:
        return set()
    result=set()
    for s in {r,-r}:
        if (P-s)%3 or (s-A)%2:
            continue
        z=(P-s)//3
        if (P-z-A)%2:
            continue
        x=(P-z+A)//2
        y=P-z-x
        assert x-y==A and measure((x,y,z))==(P,E)
        result.add((x,y,z))
    return result


def generated_orbit(t):
    visited={t}
    pending=[t]
    while pending:
        for letter in "AB":
            nxt,_,_ = contact(pending[-1],letter)
            if nxt not in visited:
                visited.add(nxt)
                pending.insert(0,nxt)
        pending.pop()
    return visited


def enumerated_shells(bound):
    bins=defaultdict(set)
    radius=isqrt(bound)
    for t in product(range(-radius,radius+1),repeat=3):
        P,E=measure(t)
        if E<=bound:
            bins[P,E].add(t)
    total_shells=0
    impulse_probes=0
    two_readouts=0
    first_split=None
    first_hidden=None
    max_states=0
    for E in range(-1,bound+1):
        p_limit=isqrt(3*max(E,0))+2
        for P in range(-p_limit,p_limit+1):
            ts=bins.get((P,E),set())
            orbits={tuple(sorted(t)) for t in ts}
            by_z=defaultdict(set)
            by_A=defaultdict(set)
            by_cubic=defaultdict(set)
            read_AB={}
            for x,y,z in ts:
                by_z[z].add((x,y,z))
                by_A[x-y].add((x,y,z))
                by_cubic[x*y*z].add((x,y,z))
                after,d1,_=contact((x,y,z),"A")
                _,d2,_=contact(after,"B")
                sig=(d1[1],d2[1])
                assert sig not in read_AB
                read_AB[sig]=(x,y,z)
                two_readouts+=1
            actual=(len(ts),sum(x==y for x,y,z in ts),sum(x==z==y for x,y,z in ts),
                    len(orbits),len(by_z),len(by_A))
            assert actual==counts(P,E),(P,E,actual,counts(P,E))
            assert len(by_cubic)==len(orbits)
            for t in orbits:
                assert by_cubic[t[0]*t[1]*t[2]]==generated_orbit(t)
            for z,group in by_z.items():
                d=2*(E-z*z)-(P-z)**2
                r=isqrt(d)
                assert r*r==d and (r-(P-z))%2==0
                assert len(group)==1+(d!=0)
            for A,group in by_A.items():
                assert group==impulse_candidates(P,E,A)
                assert len(group)<=1+(P%3==0)
                impulse_probes+=1
            if len(orbits)>1 and first_split is None:
                first_split={"P":P,"E":E,"unordered":sorted(orbits)}
            if any(len(g)>1 for g in by_A.values()) and first_hidden is None:
                first_hidden=E
            total_shells+=1
            max_states=max(max_states,len(ts))
    return {"max_square_budget":bound, "all_integer_triples_in_ball":sum(map(len,bins.values())),
            "nonempty_shells":len(bins), "PE_tests_including_outside_and_negative":total_shells,
            "distinct_impulse_fibers_tested":impulse_probes, "two_contact_readout_tests":two_readouts,
            "maximum_labeled_size_observed":max_states,
            "least_E_for_ambiguous_signed_A":first_hidden,"least_E_for_disconnected_shell":first_split}


def demo(t):
    history=[]
    for label in "AB":
        nxt,dp,de=contact(t,label)
        history.append({"setting":label,"input":t,"output":nxt,"visible_impulses":dp[:2],
                        "environment_impulse":dp[2],"changes_in_squared_budget":de,
                        "total_P_E":measure(nxt)})
        t=nxt
    return history


def growing_family():
    rows=[]
    for k in range(9):
        P=0
        E=2*7**k
        M=3*E//2
        d=isqrt(4*M//3)
        ts=set()
        for A in range(-d,d+1):
            ts.update(impulse_candidates(P,E,A))
        unordered={tuple(sorted(t)) for t in ts}
        assert len(ts)==6*(k+1) and len(unordered)==k+1
        assert len(unordered)==len({x*y*z for x,y,z in ts})
        rows.append([k,E,len(ts),len(unordered)])
    return rows


def mean_samples():
    bounds=(100,1000,10000,100000)
    cutoff=bounds[-1]
    radius=isqrt(4*cutoff//3)
    grouped={0:defaultdict(set),1:defaultdict(set)}
    for x in range(-radius,radius+1):
        for y in range(-radius,radius+1):
            n=x*x+x*y+y*y
            if not 1<=n<=cutoff:
                continue
            grouped[0][n].add(tuple(sorted((x,y,-x-y))))
            # Interpret x,y this time as the two differences A,B.
            if (x-y-1)%3==0:
                t=((1+2*x+y)//3,(1-x+y)//3,(1-x-2*y)//3)
                grouped[1][n].add(tuple(sorted(t)))
    rows=[]
    for fixed_p,group in grouped.items():
        for n in range(1,cutoff+1):
            E=2*n if fixed_p==0 else (2*n+1)//3
            value=counts(fixed_p,E)[3] if fixed_p==0 or n%3==1 else 0
            assert value==len(group.get(n,()))
        for cap in bounds:
            observed=[len(v) for n,v in group.items() if n<=cap]
            rows.append({"P":fixed_p,"cutoff_n_or_M":cap,
                         "occupied_shells":len(observed),"sum_of_components":sum(observed)})
    return rows


if __name__=="__main__":
    result={"protocol":"three_named_equal_masses_integer_exchange_v1",
            "native_BRC_events":0,"physical_measurements":0,
            "signed_coordinates":"external calibrated momentum units",
            "finite_checks":enumerated_shells(300),"mean_over_occupied_shells":mean_samples(),"unbounded_family_k_E_ordered_components":growing_family(),
            "shortest_release_witness":[demo((1,0,-1)),demo((0,-1,1))],
            "example_P_E_ordered_fix_all_unordered_third_impulses":{
                f"{p},{e}":counts(p,e) for p,e in [(0,0),(3,3),(1,1),(0,2),(0,6),(3,5),(0,42),(0,4),(0,-1)]}}
    print(json.dumps(result,indent=2,sort_keys=True))
