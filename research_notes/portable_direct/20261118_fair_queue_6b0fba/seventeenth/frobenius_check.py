"""Deterministic finite verification of binomial Frobenius field identities and costs."""
from collections import Counter
from fractions import Fraction
from math import comb, gcd, isqrt
import json


def prime(n):
    return n > 1 and all(n % d for d in range(2, isqrt(n)+1))


def cyclic(a,b,n):
    v = [0]*len(a)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            v[(i+j)%len(v)] += x*y
    return [x%n for x in v]


def power(a,b,n):
    v = [1]+[0]*(len(a)-1)
    while b:
        if b & 1:
            v = cyclic(v,a,n)
        b >>= 1
        if b:
            a = cyclic(a,a,n)
    return v


def exp_cost(e):
    return e.bit_length()-1+e.bit_count()


def trim(a):
    while a and not a[-1]:
        a.pop()
    return a


def remainder(a,b,q):
    v = a[:]
    inv = pow(b[-1],-1,q)
    while len(v) >= len(b):
        k = len(v)-len(b)
        c = v[-1]*inv % q
        for i,x in enumerate(b):
            v[i+k] = (v[i+k]-c*x) % q
        trim(v)
    return v


def poly_gcd(a,b,q):
    while b:
        a,b = b,remainder(a,b,q)
    return [(c*pow(a[-1],-1,q))%q for c in a] if a else []


def subgroup_failures(polys, order, q):
    common = polys[0]
    for row in polys[1:]:
        common = poly_gcd(common,row,q)
    if len(common) == 1:
        return 0
    # Compute Y^order-1 mod common with bounded-degree products.
    def multiply(a,b):
        z=[0]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):
                z[i+j]=(z[i+j]+x*y)%q
        return remainder(trim(z),common,q)
    x=[0,1]
    value=[1]
    while order:
        if order&1:
            value=multiply(value,x)
        order//=2
        if order:
            x=multiply(x,x)
    if not value:
        value=[0]
    value[0]=(value[0]-1)%q
    return len(poly_gcd(common,trim(value),q))-1


def evaluate(row,y,q):
    s=0
    for c in reversed(row):
        s=(s*y+c)%q
    return s


def projections(fine,n):
    r=len(fine)
    rows=[]
    adds=0
    for d in range(1,r+1):
        if r%d:
            continue
        if d<r:
            out=[0]*d
            for i,c in enumerate(fine):
                out[i%d]=(out[i%d]+c)%n
            adds+=r
            rows+=out
        # The benchmark widths are powers of 2 or 3. Phi_1=x-1.
        if d==1:
            phi=[-1,1]
        elif d==3:
            phi=[1,1,1]
        else:
            assert d&(d-1)==0
            phi=[1]+[0]*(d//2-1)+[1]
        out=fine[:]
        for i in range(r-1,len(phi)-2,-1):
            for j,c in enumerate(phi[:-1]):
                if c:
                    k=i-(len(phi)-1)+j
                    out[k]=(out[k]-c*out[i])%n
                    adds+=1
        rows+=out[:len(phi)-1]
    return rows,adds


def rho(n,cap):
    muls=gcds=0
    for c in range(1,17):
        x=y=2
        while muls+3<=cap:
            x=(x*x+c)%n
            y=(y*y+c)%n
            y=(y*y+c)%n
            muls+=3
            d=gcd(x-y,n)
            gcds+=1
            if d!=1:
                if d!=n:
                    return True,muls,gcds
                break
    return False,muls,gcds


def get_cases():
    return [('gap',p,q,16,{'h':q-p}) for p,q in [(29,31),(37,43),(43,47)]] + [
        ('sparse_square',p,a*p*p+b,8,{'a':a,'b':b})
        for p,a,b in [(23,2,3),(37,1,4),(53,3,2)]] + [
        ('order_resonance',p,u*(p*p-1)+1,3,{'u':u})
        for p,u in [(23,4),(29,3),(41,2)]]


def one_case(family,p,q,R,param):
    assert prime(p) and prime(q) and gcd(R,p*q)==1 and p<q
    N=p*q
    if family=='gap':
        h=param['h']
        assert h<=6 and q%4==3
        support={(p*(b+p*a))%R for a in (0,1) for b in range(h+1)}
    else:
        d=1 if family=='order_resonance' else param['a']+param['b']
        assert (q-d)%(p*p-1)==0 and pow(p,2,R)==1 and d+1<R
        support={p*k%R for k in range(d+1)}
    holes=sorted(set(range(R))-support)
    assert holes
    # Independent ring exponentiation on every nonzero F_p seed.
    pside=[power([t,1]+[0]*(R-2),N,p) for t in range(1,p)]
    assert all(all(v[j]==0 for j in holes) for v in pside)
    if family!='gap':
        assert all({j for j,x in enumerate(v) if x}==support for v in pside)
    inverse=pow(q,-1,R)
    polys=[]
    for j in holes:
        k=j*inverse%R
        assert k<=p
        polys.append([comb(p,i)%q for i in range(k,p+1,R)])
    g=gcd(R,q-1)
    group_order=(q-1)//g
    failures=g*subgroup_failures(polys,group_order,q)
    direct=sum(all(evaluate(row,pow(t,-R,q),q)==0 for row in polys) for t in range(1,q))
    assert direct==failures
    # Complete two-field support histograms give any-factor rates for all CRT unit seeds.
    def hist(vectors,ell):
        fine, extended = Counter(), Counter()
        for v in vectors:
            signature = sum(1<<i for i,c in enumerate(v) if c)
            rows,_ = projections(v,ell)
            extra = sum(1<<i for i,c in enumerate(rows) if c)
            fine[signature] += 1
            extended[(signature,extra)] += 1
        return fine,extended

    def q_vectors():
        loc = [q*i % R for i in range(p+1)]
        coeff = [comb(p,i)%q for i in range(p+1)]
        for t in range(1,q):
            v=[0]*R
            tpow=1
            for i in range(p,-1,-1):
                v[loc[i]]=(v[loc[i]]+coeff[i]*tpow)%q
                tpow=(tpow*t)%q
            yield v
    hp=hist(pside,p)
    hq=hist(q_vectors(),q)
    misses=[sum(n*Q.get(key,0) for key,n in P.items()) for P,Q in zip(hp,hq)]
    units=(p-1)*(q-1)
    assert misses[1]<=misses[0]<=(p-1)*failures
    min_degree=min(len(poly)-1 for poly in polys)
    assert failures<=g*min_degree
    trial=Counter()
    test_seeds=list(range(1,10))
    for t in test_seeds:
        assert gcd(t,N)==1
        v=power([t,1]+[0]*(R-2),N,N)
        w,adds=projections(v,N)
        for j,poly in zip(holes,polys):
            k=j*inverse%R
            assert v[j]%q == pow(t,p-k,q)*evaluate(poly,pow(t,-R,q),q)%q
        fine=any(1<gcd(c,N)<N for c in v)
        multi=any(1<gcd(c,N)<N for c in v+w)
        trial['fine_hits']+=fine
        trial['multiresolution_hits']+=multi
        trial['dense_mod_mult']+=R*R*exp_cost(N)
        trial['fine_gcd']+=R
        trial['extra_projection_adds']+=adds
        trial['extra_projection_gcd']+=len(w)
        if family=='order_resonance':
            trial['scalar_hits']+=1<gcd(pow(t,N-1,N)-1,N)<N
            trial['scalar_mult']+=exp_cost(N-1)
    assert trial['fine_hits']<=trial['multiresolution_hits']
    fm=(p+q)//2-isqrt(N)  # Include the successful final Fermat candidate.
    hit,rm,rg=rho(N,R*R*exp_cost(N))
    output={'p':p,'q':q,'R':R,**param,'p_holes':holes,
            'gcd_R_qminus1':g,'q_nonzero_seeds':q-1,'failed_on_all_structural_holes':failures,
            'root_bound_on_failures':g*min_degree,'nine_fixed_seeds':dict(trial),
            'CRT_unit_seeds':units,'any_factor_misses_fine_and_all':misses,
            'fermat_including_hit':fm,'rho_with_one_fine_multiplication_budget':[hit,rm,rg]}
    if family=='sparse_square':
        roots=0
        for A in range(1,5):
            roots+=1
            # Cubes only for our m=2 family. Binary integer cube root.
            lo,hi=0,1
            while hi**3<=N//A:
                hi*=2
            while hi-lo>1:
                mid=(lo+hi)//2
                if mid**3<=N//A: lo=mid
                else: hi=mid
            if 1<gcd(lo,N)<N:
                break
        else: raise AssertionError('small leading digit root family')
        output['classical_integer_cube_root_candidates']=roots
    if family=='order_resonance':
        sf=sum(pow(t,N-1,q)==1 for t in range(1,q))
        assert sf==p-1
        output['scalar_failed_q_units']=sf
        for key, misses_on_units in zip(('fine','multiresolution'), misses):
            if misses_on_units:
                repeats=1
                while Fraction(sf,q-1)**repeats > Fraction(misses_on_units,units):
                    repeats+=1
                output['scalar_repeats_matching_exact_'+key+'_hit_probability']=repeats
    return output


def projective_check():
    # Exhaust all rows in F_5^4; universal functions for R|p-1
    # cannot cancel nonzero coordinate functions on F_p^times.
    from itertools import product
    p,q,R=5,13,4
    vals=[power([t,1,0,0],p*q,p) for t in range(1,p)]
    checks=0
    for row in product(range(p),repeat=R):
        universal=all(sum(a*b for a,b in zip(row,v))%p==0 for v in vals)
        termwise=all(not c or all(v[j]==0 for v in vals) for j,c in enumerate(row))
        assert universal==termwise
        checks+=1
    # A universal two-cell cancellation when R does not divide p-1.
    all_t=[power([t,1]+[0]*6,21,3) for t in range(1,3)]
    assert all(v[2]==v[0] and v[0] for v in all_t)
    # A single-seed coarse gain where neither contributing cell vanishes modulo 23.
    n=23*31; v=power([3,1]+[0]*6,n,n)
    assert all(gcd(c,n)==1 for c in v) and gcd(v[2]+v[6],n)==23
    return checks


def main():
    by={}
    for family,p,q,R,extra in get_cases():
        by.setdefault(family,[]).append(one_case(family,p,q,R,extra))
    print(json.dumps({'families':by,'projection_rows_exhausted':projective_check(),
                      'fixed_unit_seeds':list(range(1,10)),
                      'cost_model':'dense schoolbook; unit cyclotomic entries by additions; all coordinates scanned'},
                     indent=2,sort_keys=True))


if __name__=='__main__':
    main()
