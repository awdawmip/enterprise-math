#!/usr/bin/env python3
"""Exact integral Dirichlet path to real primitive spectra; Python 3.9+."""
from fractions import Fraction
from functools import lru_cache
from math import gcd, lcm
import json

def clean(a):
    while a and a[-1]==0:
        a.pop()
    return tuple(a)

def add(f,g,sign=1):
    a=list(f)+[0]*max(0,len(g)-len(f))
    for j,b in enumerate(g):
        a[j]+=sign*b
    return clean(a)

def times2minusx(a):
    return add([2*v for v in a],(0,)+a,-1)

def mul(a,b):
    v=[0]*(len(a)+len(b))
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            v[i+j]+=x*y
    return clean(v)

def divrem(f,g):
    assert g and g[-1]==1
    a=list(f)
    q=[0]*max(0,len(a)-len(g)+1)
    for i in range(len(q)-1,-1,-1):
        c=q[i]=a[i+len(g)-1]
        for j,b in enumerate(g):
            a[i+j]-=c*b
    return clean(q),clean(a)

def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]

def factor(n):
    ans={}
    p=2
    while p*p<=n:
        while n%p==0:
            n//=p
            ans[p]=ans.get(p,0)+1
        p+=1
    if n>1:
        ans[n]=1
    return ans

@lru_cache(None)
def basis_poly(n):
    if n==0:
        return (1,)
    if n==1:
        return (2,-1)
    return add(times2minusx(basis_poly(n-1)),basis_poly(n-2),-1)

def monic(f):
    return tuple(f[-1]*x for x in f)

@lru_cache(None)
def omega(d):
    if d%2:
        k=(d-1)//2
        raw=add(basis_poly(k),basis_poly(k-1))
    else:
        raw=basis_poly(d//2-1)
    f=monic(raw)
    for j in divisors(d):
        if 2<j<d:
            f,r=divrem(f,omega(j))
            assert not r
    return f

def phi(n):
    r=n
    for p in factor(n):
        r-=r//p
    return r

def smith_formula(m):
    N=2*m
    return [gcd(N,lcm(*range(1,1+N//(2*k+1)))) for k in range(1,m)]

def projector_formula(N,d):
    r=N//d
    for p in factor(d):
        if d//p>2:
            r*=p
    return r

@lru_cache(None)
def ramanujan_values(e):
    """Integer root-order sums c_e(n) for n modulo e."""
    values = [0] * e
    for d in divisors(e):
        exponents = factor(e // d).values()
        if any(a > 1 for a in exponents):
            continue
        term = (-1) ** len(exponents) * d
        for n in range(0, e, d):
            values[n] += term
    return tuple(values)

def check_first_columns(maximum):
    count = 0
    for m in range(2, maximum + 1):
        N = 2 * m
        for e in divisors(N):
            if e <= 2:
                continue
            values = ramanujan_values(e)
            g = N
            for j in range(1, m):
                g = gcd(g, values[(j-1) % e] - values[(j+1) % e])
            assert N // g == projector_formula(N, e)
            count += 1
    return {"M_min": 2, "M_max": maximum, "order_components_checked": count}

def determinant(rows):
    n=len(rows)
    a=[r[:] for r in rows]
    sign=prev=1
    for j in range(n-1):
        i=next(i for i in range(j,n) if a[i][j])
        if i!=j:
            a[j],a[i]=a[i],a[j]
            sign=-sign
        pivot=a[j][j]
        for i in range(j+1,n):
            for k in range(j+1,n):
                z=a[i][k]*pivot-a[i][j]*a[j][k]
                assert z%prev==0
                a[i][k]=z//prev
        prev=pivot
    return sign*a[-1][-1] if n else 1

def local_smith(rows,p,bound):
    # Unit row/column pivoting, independent of the denominator-chain formula.
    q=p**(bound+1)
    v=0
    a=[[z%q for z in row] for row in rows]
    valuations=[]
    while a:
        n=len(a)
        pivot=next(((i,j) for i in range(n) for j in range(n) if a[i][j]%p),None)
        if pivot is None:
            a=[[x//p for x in row] for row in a]
            q//=p
            v+=1
            assert q>1
            continue
        i,j=pivot
        a[0],a[i]=a[i],a[0]
        for row in a:
            row[0],row[j]=row[j],row[0]
        inverse=pow(a[0][0],-1,q)
        a=[[(a[i][j]-a[i][0]*inverse*a[0][j])%q for j in range(1,n)]
           for i in range(1,n)]
        valuations.append(v)
    return valuations

def compare(m):
    N=2*m
    n=m-1
    forms={d:omega(d) for d in divisors(N) if d>2}
    total=(1,)
    for d,f in forms.items():
        assert len(f)-1==phi(d)//2
        total=mul(total,f)
    assert total==monic(basis_poly(n))
    rows=[]
    units={}
    for d,f in forms.items():
        units[d]=len(rows)
        powers=[divrem(basis_poly(j),f)[1] for j in range(n)]
        for k in range(len(f)-1):
            rows.append([v[k] if k<len(v) else 0 for v in powers])
        # A column corresponds to the actual j-th vertex of the Dirichlet path.
        for j in range(n):
            target=(0,)+powers[j]
            path_action=tuple(2*x for x in powers[j])
            if j>0:
                path_action=add(path_action,powers[j-1],-1)
            if j+1<n:
                path_action=add(path_action,powers[j+1],-1)
            assert divrem(add(target,path_action,-1),f)[1]==()
    det=abs(determinant(rows))
    observed=[1]*n
    for p,exponent in factor(det).items():
        vals=local_smith(rows,p,exponent)
        assert sum(vals)==exponent
        observed=[d*p**v for d,v in zip(observed,reversed(vals))]
    assert observed==smith_formula(m)
    # Solve for the single-block units in the ordinary path-vertex basis over Q.
    # No formula for a denominator enters the linear solve.
    a=[[Fraction(z) for z in r]+[Fraction(i==units[d]) for d in forms] for i,r in enumerate(rows)]
    for j in range(n):
        i=next(i for i in range(j,n) if a[i][j])
        a[j],a[i]=a[i],a[j]
        a[j]=[x/a[j][j] for x in a[j]]
        for i in range(n):
            if i!=j and a[i][j]:
                c=a[i][j]
                a[i]=[x-c*y for x,y in zip(a[i],a[j])]
    denominators={}
    for k,d in enumerate(forms):
        values=ramanujan_values(d)
        for i,row in enumerate(a):
            assert row[n+k]==Fraction(values[i%d]-values[(i+2)%d],N)
        denom=lcm(*(row[n+k].denominator for row in a))
        assert denom==projector_formula(N,d)
        denominators[str(d)]=denom
    if n:
        assert lcm(*denominators.values())==observed[0]
    return {"M":m,"rank":n,"index":det,"nonunit_smith_descending":[x for x in observed if x>1],
            "least_projector_denominators":denominators}

def main():
    cases=list(range(1,23))+[24,27,30,32,36,42,45]
    examples=[]
    for m in cases:
        out=compare(m)
        if m in (1,2,3,5,6,8,12,15,27,30,36,42):
            examples.append(out)
    print(json.dumps({"M_checked":cases,"source_coordinate":"lambda, diag 2, adjacent entries -1",
                      "algorithm":"path intertwining columns, Bareiss, local unit elimination, rational solve",
                      "examples":examples, "ramanujan_first_column_checks":check_first_columns(512)},sort_keys=True,indent=2))

if __name__=='__main__':
    main()
