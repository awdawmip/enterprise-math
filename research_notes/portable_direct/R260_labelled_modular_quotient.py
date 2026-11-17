"""R260 exact finite-field labelled observer quotient.
Frozen input: R259C@ef9619d3 / science@43ec6098.
Run: python R260_labelled_modular_quotient.py
Requires SymPy; uses exact fractions and GF(p) only.
"""
import json
from fractions import Fraction as F
from functools import reduce
from math import gcd, lcm
from pathlib import Path
from sympy import Poly, Symbol

x = Symbol("x")
W = (144, 576, 1440, 4320, 17280, 86400, 518400)
CASES = (
    ("R256-p13", F(67,169), 13, 1184397599, 989553240, 3805974000, 2184, (1093,2185)),
    ("R257-p23", F(770,1973), 23, 327870790093, 153448180920, 166791501000, 528, ()),
    ("R258-p23", F(866,2197), 23, 3327364117, 3975468120, 36933000, 12144, ()),
    ("R258-p13", F(866,2197), 13, 3327364117, 3975468120, 36933000, 12, ()),
)

def mask(m):
    return [0] + [i+1 for i in range(6) if (m>>i)&1]

def mul(f, a):
    g=[F(0)]*(len(f)+1)
    for j,v in enumerate(f):
        g[j]-=a*v
        g[j+1]+=v
    return g

def characteristic(ids,a,b):
    c=[F(1)]
    for i in ids:
        c=mul(c,a[i])
    for i in ids:
        z=[F(1)]
        for j in ids:
            if i!=j:
                z=mul(z,a[j])
        for j,v in enumerate(z):
            c[j]-=b[i]*v
    return c

def reconstruct(s,J,T,K):
    t=(1691*s-2615)/(2615*s-3539)
    a=[F(1,5),F(1,4),F(3,10),F(9,20),s,F(2,3),t]
    b=[F(13,60)]+[F(5,18)*abs(F(1,2)-a[i]) for i in range(1,7)]
    pi=[b[i]/(1-a[i]) for i in range(7)]
    assert sum(pi)==1
    z=sum(b[i]/(1-a[i])**2 for i in range(7))
    rho=[b[i]/(z*(1-a[i])**2) for i in range(7)]
    assert lcm(*[ (W[m.bit_count()]*rho[i]).denominator for m in range(63) for i in mask(m)])==J
    cs=[]; qs=[]; raw=[]
    for m in range(63):
        ids=mask(m); d=len(ids)
        c=[v*T**(d-j) for j,v in enumerate(characteristic(ids,a,b))]
        assert all(v.denominator==1 for v in c)
        cs.append([int(v) for v in c])
        v=[F(1)]*d; h=[]
        for k in range(d+3):
            if k>=3:
                H=J*T**k*W[m.bit_count()]*sum(rho[i]*v[j] for j,i in enumerate(ids))
                assert H.denominator==1
                h.append(int(H))
            total=sum(pi[i]*v[j] for j,i in enumerate(ids))
            v=[a[i]*v[j]+(1-a[i])*total for j,i in enumerate(ids)]
        raw.extend(h)
        qs.append([u//K for u in h])
    assert len(raw)==249
    assert reduce(gcd,(abs(v) for v in raw))==K
    assert all(v%K==0 for v in raw)
    return cs,qs

def finite_field_minimal(c,q,p):
    d=len(q)
    den=[1]+list(reversed(c[:-1]))
    num=[sum(den[j]*q[i-j] for j in range(i+1))%p for i in range(d)]
    D=Poly(sum(v%p*x**i for i,v in enumerate(den)),x,modulus=p)
    N=Poly(sum(v%p*x**i for i,v in enumerate(num)),x,modulus=p)
    R=D.exquo(D.gcd(N))
    constant=int(R.nth(0))%p
    assert constant
    R=R.mul_ground(pow(constant,-1,p))
    r=R.degree()
    f=Poly(sum(int(R.nth(i))%p*x**(r-i) for i in range(r+1)),x,modulus=p).monic()
    full=Poly(sum(int(v)%p*x**i for i,v in enumerate(c)),x,modulus=p)
    assert full.rem(f).is_zero
    return f,r

def sequence(c,q,p,n):
    v=[int(i)%p for i in q]
    d=len(q)
    for k in range(d,n):
        v.append(-sum(c[j]*v[k-d+j] for j in range(d))%p)
    return v

def basis(rows,p):
    # Select an independent subset of ORIGINAL labelled rows.
    indices=[]
    pivots=[]; E=[]; representations=[]
    rank=len(rows[0])
    for idx,row in enumerate(rows):
        v=row[:]
        e=[0]*(len(indices)+1)
        e[-1]=1
        for j,(pivot,r,b) in enumerate(zip(pivots,E,representations)):
            a=v[pivot]
            if a:
                v=[(xx-a*yy)%p for xx,yy in zip(v,r)]
                e=[(xx-a*yy)%p for xx,yy in zip(e,b+[0])]
        if not any(v):
            continue
        pivot=next(k for k in range(rank) if v[k])
        inverse=pow(v[pivot],-1,p)
        for j in range(len(representations)):
            representations[j].append(0)
        indices.append(idx)
        pivots.append(pivot)
        E.append([xx*inverse%p for xx in v])
        representations.append([xx*inverse%p for xx in e])
    # Recover every row as a fixed linear combination of original basis rows.
    coefficients=[]
    for row in rows:
        v=row[:]; e=[0]*len(indices)
        for pivot,base,expr in zip(pivots,E,representations):
            a=v[pivot]
            if a:
                v=[(xx-a*yy)%p for xx,yy in zip(v,base)]
                e=[(xx+a*yy)%p for xx,yy in zip(e,expr)]
        assert not any(v)
        coefficients.append(e)
    for m,row in enumerate(rows):
        for k in range(rank):
            assert sum(coefficients[m][j]*rows[idx][k] for j,idx in enumerate(indices))%p==row[k]
    return indices,coefficients

def run():
    results=[]; cache={}
    for name,s,p,J,T,K,P,zeros in CASES:
        if s not in cache: cache[s]=reconstruct(s,J,T,K)
        cs,qs=cache[s]
        Fcommon=Poly(1,x,modulus=p); degrees=[]
        for c,q in zip(cs,qs):
            f,r=finite_field_minimal(c,q,p)
            degrees.append(r)
            Fcommon=Fcommon.lcm(f).monic()
        r=Fcommon.degree()
        coeffs=[int(Fcommon.nth(i))%p for i in range(r+1)]
        all_series=[sequence(c,q,p,2*P) for c,q in zip(cs,qs)]
        for y in all_series:
            for k in range(2*P-r):
                assert sum(coeffs[j]*y[k+j] for j in range(r+1))%p==0
        selected,reconstruction=basis([y[:r] for y in all_series],p)
        for m in range(63):
            for k in range(2*P):
                assert all_series[m][k]==sum(
                    reconstruction[m][j]*all_series[idx][k]
                    for j,idx in enumerate(selected)
                )%p
        for k in range(P):
            assert all(all_series[m][k]==all_series[m][k+P] for m in range(63))
        # Full labelled output period is exactly P.
        for d in range(1,P):
            if P%d==0:
                assert any(
                    any(all_series[m][k]!=all_series[m][(k+d)%P] for m in range(63))
                    for k in range(P)
                )
        zeros_found=tuple(k+3 for k in range(P)
            if all(all_series[m][k]==0 for m in range(63)))
        assert zeros_found==zeros
        assert zeros_found==tuple(k+3 for k in range(P)
            if all(all_series[m][k]==0 for m in selected))
        hist={str(i):degrees.count(i) for i in sorted(set(degrees))}
        record=dict(case=name,parameter=str(s),prime=p,J=J,T=T,K=K,
            original_dimension=249,period=P,per_mask_minimal_degrees=degrees,
            degree_histogram=hist,common_degree=r,
            common_characteristic_ascending=coeffs,basis_masks=selected,
            reconstruction_coefficients=reconstruction,zero_k=list(zeros_found),
            two_period_full_reconstruction_pass=True,exact_basis_pass=True)
        results.append(record)
        print(name, "order",r,"basis size",len(selected),
              "basis",selected,"zero positions",zeros_found,flush=True)
    result=dict(schema="EM_R260_LABELLED_MODULAR_QUOTIENT_V1",
        frozen_science_pin="43ec6098b1330ae86d0a7863be336c5d97f6ef34",
        input_commit="ef9619d3ed267d595415c47e4cc167e1754243ad",
        cases=results)
    outfile=Path(__file__).with_name("R260_labelled_modular_quotient_verification.json")
    outfile.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n")
    print("PASS; exact JSON:",outfile.name)
if __name__=="__main__":run()
