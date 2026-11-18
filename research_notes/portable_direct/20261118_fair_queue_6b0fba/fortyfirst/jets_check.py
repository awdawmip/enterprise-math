"""Exact factor-verification, jet-distance and public BRC scalar-receipt checks."""
import argparse
from contextlib import contextmanager
from hashlib import sha256
from itertools import combinations, combinations_with_replacement, product
import json
from math import comb, isqrt
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory


PIN="e7b9fb5084f93a9b2dbc16225629b667fb7bf46c"
X=(0,1)
ONE=(1,)


def trim(f,p):
    out=[c%p for c in f]
    while out and not out[-1]:
        out.pop()
    return tuple(out)


def add(f,g,p,sign=1):
    return trim([(f[j] if j<len(f) else 0)+sign*(g[j] if j<len(g) else 0)
                 for j in range(max(len(f),len(g)))],p)


def multiply(f,g,p):
    if not f or not g:
        return ()
    h=[0]*(len(f)+len(g)-1)
    for i,x in enumerate(f):
        for j,y in enumerate(g):
            h[i+j]+=x*y
    return trim(h,p)


def divmod_poly(f,g,p):
    if not g:
        raise ZeroDivisionError
    q=[0]*max(0,len(f)-len(g)+1)
    rem=f
    lead_inv=pow(g[-1],-1,p)
    while len(rem)>=len(g):
        k=len(rem)-len(g)
        q[k]=rem[-1]*lead_inv%p
        rem=add(rem,(0,)*k+tuple(q[k]*v for v in g),p,-1)
    return trim(q,p),rem


def gcd_poly(f,g,p):
    while g:
        f,g=g,divmod_poly(f,g,p)[1]
    return trim([v*pow(f[-1],-1,p) for v in f],p) if f else ()


def power(f,m,p,mod=None):
    ans=ONE
    while m:
        if m%2:
            ans=multiply(ans,f,p)
            if mod:ans=divmod_poly(ans,mod,p)[1]
        m//=2
        if m:
            f=multiply(f,f,p)
            if mod:f=divmod_poly(f,mod,p)[1]
    return ans


def prime_divisors(n):
    return [q for q in range(2,n+1) if n%q==0 and
            all(q%i for i in range(2,isqrt(q)+1))]


def rabin(f,p):
    d=len(f)-1
    if d<1 or f[-1]!=1:
        return False
    xmod=divmod_poly(X,f,p)[1]
    a=xmod
    tests={d//q for q in prime_divisors(d)}
    for j in range(1,d+1):
        a=power(a,p,p,f)
        if j in tests and gcd_poly(f,add(a,xmod,p,-1),p)!=ONE:
            return False
    return a==xmod


def rabin_receipt(f,p):
    """Return a Frobenius ladder and polynomial Bezout identities."""
    d=len(f)-1
    x0=divmod_poly(X,f,p)[1]
    chain=[x0]
    for _ in range(d):
        chain.append(power(chain[-1],p,p,f))
    assert chain[-1]==x0
    pairs=[]
    for ell in prime_divisors(d):
        h=add(chain[d//ell],x0,p,-1)
        r0,r1=f,h
        a0,a1=ONE,()
        b0,b1=(),ONE
        while r1:
            quo,rem=divmod_poly(r0,r1,p)
            r0,r1=r1,rem
            a0,a1=a1,add(a0,multiply(quo,a1,p),p,-1)
            b0,b1=b1,add(b0,multiply(quo,b1,p),p,-1)
        assert len(r0)==1
        c=pow(r0[0],-1,p)
        A=trim([c*v for v in a0],p); B=trim([c*v for v in b0],p)
        assert add(multiply(A,f,p),multiply(B,h,p),p)==ONE
        pairs.append({"prime_divisor":ell,"A":A,"B":B,"Frobenius_minus_X":h})
    return {"factor":f,"ladder_residues":chain,"bezout":pairs}


def verify_irreducibility_receipt(f,p,receipt):
    d=len(f)-1
    if d<1 or f[-1]!=1 or tuple(receipt["factor"])!=f:return False
    chain=[tuple(row) for row in receipt["ladder_residues"]]
    if len(chain)!=d+1:return False
    if chain[0]!=divmod_poly(X,f,p)[1] or chain[-1]!=chain[0]:return False
    if any(power(z,p,p,f)!=w for z,w in zip(chain,chain[1:])):return False
    required=prime_divisors(d)
    rows=receipt["bezout"]
    if len(rows)!=len(required) or sorted(row["prime_divisor"] for row in rows)!=required:return False
    for row in rows:
        ell=row["prime_divisor"]
        h=add(chain[d//ell],chain[0],p,-1)
        if tuple(row["Frobenius_minus_X"])!=h:return False
        if add(multiply(tuple(row["A"]),f,p),multiply(tuple(row["B"]),h,p),p)!=ONE:return False
    return True


def mons(p,d):
    for c in product(range(p),repeat=d):
        yield (*c,1)


def raw_jet(f,a,s,p):
    # Independent Hasse definition. No factorial in the field is inverted.
    return tuple(sum(comb(j,h)*c*pow(a,j-h) for j,c in enumerate(f) if j>=h)%p
                 for h in range(s))


def residue_word(f,mods,p):
    return tuple(divmod_poly(f,P,p)[1] for P in mods)


def distance(words):
    return min(sum(x!=y for x,y in zip(a,b)) for a,b in combinations(words,2))


def predicted_distance(weights,degree):
    w=sorted(weights)
    for d in range(len(w)+1):
        if sum(w[:len(w)-d])<degree:
            return d
    raise ValueError("positive comparison degree required")


def tests_on_base():
    rows=[]
    for p,deg_limit in [(2,5),(3,3),(5,2)]:
        depth_vectors=0
        for n in range(1,deg_limit+1):
            words=list(mons(p,n))
            # Include zero depths, at most three labelled nodes, and every prefix depth up to n.
            pts=list(range(min(3,p)))
            pre={(f,a):raw_jet(f,a,n,p) for f in words for a in pts}
            for s in product(range(n+1),repeat=len(pts)):
                count=len({tuple(pre[f,a][:v] for a,v in zip(pts,s)) for f in words})
                assert count==p**min(n,sum(s))
                depth_vectors+=1
        rows.append({"p":p,"up_to_monic_degree":deg_limit,
                     "queried_base_nodes":min(3,p),"depth_vectors":depth_vectors})
    return rows


def tests_on_orbits():
    p=2
    nodes=[X,(1,1),(1,1,1),(1,1,0,1)]
    assert all(rabin(P,p) for P in nodes)
    depths=(1,2,1,1)
    mods=[power(P,s,p) for P,s in zip(nodes,depths)]
    weights=[(len(P)-1)*s for P,s in zip(nodes,depths)]
    table=[]
    for n in range(1,6):
        words=[residue_word(f,mods,p) for f in mons(p,n)]
        actual=distance(words)
        assert actual==predicted_distance(weights,n)
        table.append([n,actual])
    g=(0,0,0,0,1)
    f=add(g,multiply(nodes[0],mods[1],p),p)
    a,b=residue_word(f,mods,p),residue_word(g,mods,p)
    received=tuple(a[i] if i!=2 else b[i] for i in range(4))
    assert sum(x!=y for x,y in zip(a,received))==sum(x!=y for x,y in zip(b,received))==1
    # At the quadratic closed point alpha^2+alpha+1=0, compare Hasse jets
    # in F4 with the independent divisibility test modulo P^s for all 5-degree inputs.
    P=nodes[2]
    def ext_jet(poly,s):
        result=[]
        for h in range(s):
            total=()
            for j,c in enumerate(poly):
                if j>=h and (comb(j,h)*c)%2:
                    total=add(total,power(X,j-h,2,P),2)
            result.append(total)
        return tuple(result)
    checks=0
    for s in (1,2,3):
        mod=power(P,s,2)
        for f0 in mons(p,5):
            one=ext_jet(f0,s)
            rep=divmod_poly(f0,mod,p)[1]
            assert one==ext_jet(rep,s)
            checks+=1
    return {"p":2,"nodes":nodes,"block_weights":weights,"degree_min_distance":table,
            "quadratic_orbit_jet_checks":checks,"ambiguous_at_one_error":{
                "true_first":f,"true_second":g,"observed":received}}


def valuation(f,P,p):
    n=0
    while f:
        q,r=divmod_poly(f,P,p)
        if r:break
        n+=1;f=q
    return n


def frobenius_checks():
    p=2
    P=[X,(1,1),(1,1,1)]
    case_count=0
    example=None
    for e,C in [(1,ONE),(2,ONE),(1,(0,1,1)),(2,(0,0,1))]:
        q=p**e
        for d in range(1,4):
            full=[multiply(C,power(h,q,p),p) for h in mons(p,d)]
            for s in product(range(4),repeat=3):
                mods=[power(Pi,si,p) for Pi,si in zip(P,s)]
                weights=[(len(Pi)-1)*max(0,(si-valuation(C,Pi,p)+q-1)//q)
                         for Pi,si in zip(P,s)]
                observed=[residue_word(f,mods,p) for f in full]
                assert distance(observed)==predicted_distance(weights,d)
                case_count+=1
                if e==1 and C==(0,1,1) and d==3 and s==(3,3,2):
                    example={"p":p,"C":C,"Frobenius_power":q,"d":d,
                             "raw_depths":s,"effective_weights":weights,
                             "minimum_block_distance":distance(observed)}
    return {"exhaustive_parameter_sets":case_count,"example":example}


def resource_checks():
    count=0
    for p in (2,3,5):
        for exponent in (0,1,2):
            q=p**exponent
            for bad in range(p):
                for d in range(1,6):
                    best_peak=None
                    best_total=None
                    for r in combinations_with_replacement(range(d+1),p):
                        if sum(r[:p-bad])<d:continue
                        costs=[1+q*(h-1) if h else 0 for h in r]
                        best_peak=max(costs) if best_peak is None else min(best_peak,max(costs))
                        best_total=sum(costs) if best_total is None else min(best_total,sum(costs))
                    m=(d+p-bad-1)//(p-bad)
                    S=d+bad*m
                    assert best_peak==1+q*(m-1)
                    assert best_total==S+(q-1)*max(S-p,0)
                    count+=1
    return {"optimized_schedules":count,"nodes":[2,3,5],"depth_orders_of_Frobenius":[0,1,2],
            "factor_degrees":[1,2,3,4,5]}


def nonunit_resource_checks():
    cases=0
    for p in (2,3):
        for c in combinations_with_replacement(range(3),p):
            for t in range(p):
                for q in (1,p,p*p):
                    for d in range(1,5):
                        best_peak=None
                        best_sum=None
                        for r in product(range(d+1),repeat=p):
                            if sum(sorted(r)[:p-t])<d:continue
                            raw=[a+1+q*(v-1) if v else 0 for a,v in zip(c,r)]
                            best_peak=max(raw) if best_peak is None else min(best_peak,max(raw))
                            best_sum=sum(raw) if best_sum is None else min(best_sum,sum(raw))
                        formula=[]
                        for m in range(t+1,p+1):
                            D=max(d,m-t);K=(D+m-t-1)//(m-t)
                            formula.append(sum(c[:m])+m+q*(D+t*K-m))
                        assert best_sum==min(formula)
                        peak=next(s for s in range(max(c)+q*d+2)
                                  if sum(sorted(max(0,(s-a+q-1)//q) for a in c)[:p-t])>=d)
                        assert best_peak==peak
                        cases+=1
    return {"parameter_sets":cases,"p":[2,3],"tested_C_orders":[0,1,2],
            "separate_optima_example":{"p":2,"C":[1,1],"q":1,"d":3,"erased_comparison_slots":0,
            "peak_optimal_raw_schedule":[2,2],"total_optimal_raw_schedule":[3,0]}}


def support_checks():
    p=2
    P=(1,1,1);Q=(1,1,0,1)
    assert rabin(P,p) and rabin(Q,p)
    states=lambda n:[(e,f) for e in range(1,n//2+1) for f in range(1,n//3+1) if 2*e+3*f==n]
    assert states(10)==[(2,2)] and states(16)==[(2,4),(5,2)]
    sparse=add(power(X,3,3),X,3,-1)
    assert all(raw_jet(sparse,a,1,3)==(0,) for a in range(3))
    assert raw_jet(sparse,0,2,3)==(0,2)
    return {"exact_support_multiplicities_degree_10":states(10),
            "exact_support_multiplicities_degree_16":states(16),
            "F3_sparse_difference":sparse,"extra_jet_at_0":raw_jet(sparse,0,2,3)}


def irreducibility_checks():
    rows=[]
    for p,maxd in [(2,7),(3,5),(5,3)]:
        count=0
        for n in range(1,maxd+1):
            divisors=[g for j in range(1,n//2+1) for g in mons(p,j)]
            for f in mons(p,n):
                simple=all(divmod_poly(f,g,p)[1] for g in divisors)
                assert rabin(f,p)==simple
                count+=1
        rows.append([p,maxd,count])
    return rows


@contextmanager
def public_reducer(repo):
    with TemporaryDirectory() as temp:
        root=Path(temp)/"jet_frozen_arith"
        root.mkdir()
        (root/"__init__.py").write_text("")
        for name in ("core","division","exact_arithmetic"):
            data=subprocess.check_output(["git","-C",str(repo),"show",
                f"{PIN}:src/enterprise_math/{name}.py"])
            (root/(name+".py")).write_bytes(data)
        sys.path.insert(0,temp)
        try:
            from jet_frozen_arith.exact_arithmetic import division,brc_evaluate_division
            def reduce(p,a,events):
                trace=brc_evaluate_division(division(a,p))
                assert trace.reconstruct()==a and trace.collapsed_numerator==trace.quotient*p
                assert trace.evaluation_kind=="BRC_DIVISION_EVALUATION"
                events.append([a,p,trace.quotient,trace.remainder])
                return trace.remainder
            yield reduce
        finally:
            sys.path.remove(temp)


def cert(reduce,p,f,factors,schedule,record,candidate_lead=None):
    # Prime p is a promised input. Polynomial coefficients are dense in increasing order.
    if not (f and all(type(c)==int and 0<=c<p for c in f) and f[-1]):
        return {"accepted":False,"reason":"invalid_input"}
    if candidate_lead is not None and (type(candidate_lead)!=int or candidate_lead!=f[-1]):
        return {"accepted":False,"reason":"wrong_leading_coefficient"}
    if any(type(a)!=int or type(s)!=int or a<0 or a>=p or s<1 for a,s in schedule):
        return {"accepted":False,"reason":"bad_schedule"}
    if len({a for a,s in schedule})!=len(schedule):
        return {"accepted":False,"reason":"duplicate_node"}
    if any(len(g)<2 or g[-1]!=1 or any(type(c)!=int or not 0<=c<p for c in g)
           or type(e)!=int or e<1 for g,e in factors):
        return {"accepted":False,"reason":"noncanonical_factor"}
    if len({g for g,e in factors})!=len(factors):
        return {"accepted":False,"reason":"duplicate_factor"}
    n=len(f)-1
    if n!=sum((len(g)-1)*e for g,e in factors):
        return {"accepted":False,"reason":"degree_mismatch"}
    if n>sum(s for a,s in schedule):
        return {"accepted":False,"reason":"insufficient_depth"}
    if any(not rabin(g,p) for g,e in factors):
        return {"accepted":False,"reason":"reducible_factor"}
    row=[]
    for a,s in schedule:
        ev=[]
        def rr(z):
            return reduce(p,z,ev)
        def horner(poly):
            h=[0]*s
            for c in reversed(poly):
                h=[rr(a*h[j]+(h[j-1] if j else c)) for j in range(s)]
            return tuple(h)
        def tm(u,v):
            return tuple(rr(sum(u[i]*v[j-i] for i in range(j+1))) for j in range(s))
        left=horner(f)
        h=(f[-1],)+(0,)*(s-1)
        for g,e in factors:
            v=horner(g)
            while e:
                if e%2:h=tm(h,v)
                e//=2
                if e:v=tm(v,v)
        assert left==raw_jet(f,a,s,p)
        if record:
            row.append({"node":a,"depth":s,"left":left,"right":h,"BRC_calls":len(ev),
                        "first_reduction":ev[0],"last_reduction":ev[-1],
                        "ordered_reductions_sha256":sha256(json.dumps(ev,separators=(',',':')).encode()).hexdigest()})
        if left!=h:
            return {"accepted":False,"reason":"jet_mismatch","node":a,"reports":row}
    return {"accepted":True,"reason":"complete_factorization","reports":row}


def runtime_check(reduce):
    p=3
    factors=[((1,1),6),((1,0,1),2)]
    g=power((1,1),6,p)
    g=multiply(g,power((1,0,1),2,p),p)
    g=tuple(2*c%p for c in g)
    schedule=[(0,4),(1,3),(2,3)]
    accepted=cert(reduce,p,g,factors,schedule,True)
    assert accepted["accepted"]
    # A genuine input that agrees at depths (3,3,3) and differs in the 4th coefficient at 0.
    delta=power(add(power(X,3,p),X,p,-1),3,p)
    false_input=add(g,delta,p)
    assert len(false_input)==len(g)
    assert all(raw_jet(g,a,3,p)==raw_jet(false_input,a,3,p) for a in range(p))
    rejected=cert(reduce,p,false_input,factors,schedule,True)
    assert rejected["reason"]=="jet_mismatch" and rejected["node"]==0
    receipts=[rabin_receipt(g0,p) for g0,_ in factors]
    assert all(verify_irreducibility_receipt(g0,p,rc) for (g0,_),rc in zip(factors,receipts))
    bad=json.loads(json.dumps(receipts[1]))
    bad["bezout"][0]["B"]=[]
    assert not verify_irreducibility_receipt(factors[1][0],p,bad)
    tests={"altered_bezout_rejected":True,"bad_multiplicity":cert(reduce,p,g,[(factors[0][0],5),factors[1]],schedule,False)["reason"],
           "reducible_exact_product":cert(reduce,p,power((1,1),2,p),[(power((1,1),2,p),1)],[(0,2)],False)["reason"],
           "under_sampled":cert(reduce,p,false_input,factors,[(0,3),(1,3),(2,3)],False)["reason"],
           "wrong_scalar":cert(reduce,p,g,factors,schedule,False,1)["reason"],
           "nonzero_constant":cert(reduce,p,(2,),[],[],False)["accepted"],
           "zero_input":cert(reduce,p,(),[],[],False)["reason"]}
    assert tests=={"altered_bezout_rejected":True,"bad_multiplicity":"degree_mismatch","reducible_exact_product":"reducible_factor",
                   "under_sampled":"insufficient_depth","wrong_scalar":"wrong_leading_coefficient","nonzero_constant":True,"zero_input":"invalid_input"}
    return {"public_git":PIN,"coefficient_order":"increasing powers of X","p":p,
            "input":g,"leading_coefficient":g[-1],"factor_list":factors,"schedule":schedule,
            "passing":accepted,"factor_irreducibility_receipts":receipts,
            "aliased_after_truncation":false_input,
            "false_input":rejected,"edge_cases":tests}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo",required=True,type=Path,help="public checkout containing the pinned BRC sources")
    args=parser.parse_args()
    with public_reducer(args.repo) as reducer:
        raw=runtime_check(reducer)
    result={"original_base_field":tests_on_base(),"closed_orbits":tests_on_orbits(),
            "known_Frobenius_family":frobenius_checks(),"known_support":support_checks(),"minimum_resources":resource_checks(),
            "nonunit_C_minimum_resources":nonunit_resource_checks(),
            "Rabin_vs_trial_division":irreducibility_checks(),"typed_scalar_replay":raw}
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__=="__main__":main()
