"""Primitive homogeneous power vectors. Integer certificates; no external dependencies."""
from itertools import combinations
from math import comb, factorial, gcd, isqrt, prod
import json


def primes(n):
    return [p for p in range(2,n+1) if all(p%i for i in range(2,isqrt(p)+1))]


def valuation(n,p):
    assert n
    k=0
    while n%p==0:
        n//=p
        k+=1
    return k


def exponent(j,p):
    m=p+1
    v=0
    while m<=j:
        v+=j//m
        m*=p
    return v


def smith_factors(d):
    ps=primes(d)
    return [prod(p**exponent(j,p) for p in ps) for j in range(d+1)]


def bracket(P,Q):
    return P[0]*Q[1]-P[1]*Q[0]


def vandermonde(points):
    return prod(abs(bracket(P,Q)) for P,Q in combinations(points,2))


def prime_points(p,d):
    # Johnson-Patterson, Proposition 10: p finite slopes then an infinity-chart point.
    result=[]
    for j in range(d+1):
        q,r=divmod(j,p+1)
        result.append((p*q+r,1) if r<p else (1,p*q))
    return result


def common_points(d):
    if d<=1:
        return [(1,0),(0,1)][:d+1]
    points=[(i,1) for i in range(d)]+[(1,0)]
    for i in range(1,(d+1)//3):
        a,m=0,1
        for p in primes(d-1):
            if i>=(d+1)//(p+1):
                continue
            h=p
            while h<=d:
                h*=p
            a+=m*((p*i-a)*pow(m,-1,h)%h)
            m*=h
        a=(a+m//2)%m-m//2
        points.append((1,a))
    return points


def direct_smith(matrix):
    """Integral row/column operations; diagonalize and check divisibility."""
    a=[r[:] for r in matrix]
    h,w=len(a),len(a[0])
    out=[]
    for k in range(min(h,w)):
        pivot=next(((i,j) for i in range(k,h) for j in range(k,w) if a[i][j]),None)
        if pivot is None: break
        i,j=pivot
        a[i],a[k]=a[k],a[i]
        for row in a: row[j],row[k]=row[k],row[j]
        while True:
            handled=False
            for i in range(k+1,h):
                if a[i][k]:
                    q=a[i][k]//a[k][k]
                    a[i]=[x-q*y for x,y in zip(a[i],a[k])]
                    if a[i][k]: a[k],a[i]=a[i],a[k]
                    handled=True
                    break
            if handled: continue
            for j in range(k+1,w):
                if a[k][j]:
                    q=a[k][j]//a[k][k]
                    for row in a: row[j]-=q*row[k]
                    if a[k][j]:
                        for row in a: row[j],row[k]=row[k],row[j]
                    handled=True
                    break
            if handled: continue
            bad=next((row for row in a[k+1:] if any(v%a[k][k] for v in row[k+1:])),None)
            if bad is None: break
            a[k]=[x+y for x,y in zip(a[k],bad)]
        out.append(abs(a[k][k]))
    assert all(b%a==0 for a,b in zip(out,out[1:]))
    return out


def power_rows(points,d):
    return [[x**(d-i)*y**i for i in range(d+1)] for x,y in points]


def window_exponents(p,depth,residues,d):
    """Affine chart residues; root level uses the common projective tree."""
    def node(level,occupied):
        if level==depth:
            return [valuation(factorial(j),p) for j in range(d+1)]
        groups={}
        for a in occupied:
            groups.setdefault(a%p**(level+1),[]).append(a)
        choices=[]
        for sub in groups.values():
            children=node(level+1,sub)
            choices.extend(i+w for i,w in enumerate(children))
        return sorted(choices)[:d+1]
    return node(0,residues)


def exact_determinants(n,target):
    """Normalize a unimodular pair to axes; completely exhaust remaining primitive slopes."""
    assert 2**comb(n,2)>target
    ds=[k for k in range(1,isqrt(target)+1) if target%k==0]
    ds=sorted(set(ds+[target//k for k in ds]))
    candidates=[(x,y) for y in ds for a in ds if target%(y*a)==0
                and gcd(a,y)==1 for x in (a,-a)]
    candidates.sort(key=lambda x:(abs(x[0]*x[1]),x))
    def search(pool,needed,rem):
        if needed==0: return int(rem==1)
        total=0
        for i,(v,cost) in enumerate(pool):
            if len(pool)-i<needed: break
            if rem%cost: continue
            nextrem=rem//cost
            tail=[]
            for z,c in pool[i+1:]:
                newcost=c*abs(bracket(v,z))
                if newcost and nextrem%newcost==0: tail.append((z,newcost))
            total+=search(tail,needed-1,nextrem)
        return total
    return [len(candidates),search([(v,abs(v[0]*v[1])) for v in candidates],n-2,target)]


def normalized_orbit_size(points):
    forms=set()
    for u in points:
        for v in points:
            if abs(bracket(u,v))!=1: continue
            for sign in (-1,1):
                rep=[]
                for p in points:
                    x,y=sign*bracket(p,v),bracket(u,p)
                    if y<0 or (y==0 and x<0):
                        x,y=-x,-y
                    rep.append((x,y))
                forms.add(tuple(sorted(rep)))
    return len(forms)


def correlated_cost(ps):
    """Exactly one slope 1 in the local product, d=1; construct the minimal number of rows."""
    modulus=prod(ps)
    residues=[(modulus//p)*pow(modulus//p,-1,p)%modulus for p in ps]
    first=residues[:-1]
    difference=gcd(*(abs(a-b) for a,b in combinations(first,2)))
    # Fix all gcd obstructions of the existing differences outside the allowed modulus.
    a,m=residues[-1],modulus
    for ell in primes(difference):
        if difference%ell==0 and modulus%ell:
            a+=m*((first[0]+1-a)*pow(m,-1,ell)%ell)
            m*=ell
    rows=[(x,1) for x in first+[a]]
    assert direct_smith(power_rows(rows,1))==[1,1]
    for i,(x,_) in enumerate(rows):
        assert all(x%p==int(i==j) for j,p in enumerate(ps))
    return {'primes':ps,'slopes':[x for x,y in rows],'minimum_row_count':len(rows),
            'rectangular_minimum_row_count':2}


def gaussian_order(degree):
    factors={}
    for p in primes(degree):
        points=prime_points(p,degree)
        needed=0
        real,imag=1,0
        for j,(a,b) in enumerate(points):
            # Product (b_i - i a_i); multiply by y^(d-j) at (1,i) for the finite chart.
            c=(degree-j)%4 if b==1 else 0
            value=(real,-imag,-real,imag)[c]
            if value: needed=max(needed,exponent(j,p)-valuation(abs(value),p))
            real,imag=b*real+a*imag,b*imag-a*real
        if needed: factors[p]=needed
    return prod(p**e for p,e in factors.items())


def main():
    small={}
    for d in range(11):
        points=common_points(d)
        factors=smith_factors(d)
        assert direct_smith(power_rows(points,d))==factors
        delta=gcd(*(vandermonde(rows) for rows in combinations(points,d+1)))
        assert delta==prod(factors)
        for p in primes(d+1):
            seq=prime_points(p,d)
            for j,P in enumerate(seq):
                assert sum(valuation(abs(bracket(P,Q)),p) for Q in seq[:j])==exponent(j,p)
        small[d]={'invariants':factors,'index':delta,'pure_row_count':len(points),
                  'common_rows':points}
    windows={}
    for p,r,res in [(2,2,[0,2]),(2,2,[0,1]),(3,2,[0,1,4]),(2,3,[0,1,4,5,6])]:
        d=6
        local=window_exponents(p,r,res,d)
        values=[(a+p**r*j,1) for a in res for j in range(d+1)]
        actual=[valuation(x,p) for x in direct_smith(power_rows(values,d))]
        assert actual==local
        windows[f'{p}^{r}_{res}']=local
    rectangular={}
    for allowed in ([0,1],[3,4],[0,1,3,4]):
        points=[(i,1) for i in range(-15,16) if i%6 in allowed]
        rectangular[str(allowed)]=direct_smith(power_rows(points,3))
    assert list(rectangular.values())==[[1,1,6,6]]*3
    minima={}
    for d in (5,6):
        index=prod(smith_factors(d))
        rows={h:exact_determinants(d+1,h) for h in (index,2*index,3*index)}
        assert [z[1] for z in rows.values()]==([0,0,6] if d==5 else [0,0,44])
        pts=[(1,0),(0,1),(-3,1),(-2,1),(-1,1),(-3,2)]
        if d==6: pts.append((-4,1))
        assert vandermonde(pts)==3*index
        assert normalized_orbit_size(pts)==rows[3*index][1]
        minima[d]={'target_to_candidate_and_solution_counts':rows,'minimum_configuration':pts,
                   'minimizing_PGL2Z_orbits':1}
    one_hot=[(35,38),(-35,37),(-21,4),(21,31),(-45,4),(30,23)]
    for i,(a,b) in enumerate(one_hot):
        assert [a*pow(b,-1,p)%p for p in (3,5,7)]==[int(i//2==j) for j in range(3)]
    hot_index=gcd(*(vandermonde(rows) for rows in combinations(one_hot,4)))
    assert hot_index==2*105**2
    targets={d:gaussian_order(d) for d in range(0,25,2)}
    assert targets[6]==12
    print(json.dumps({'global_smith_and_common_rows':small,'window_valuations_d6':windows,
                      'mod6_correlated_windows_d3':rectangular,'bounded_global_minima_axes_count':minima,
                      'three_prime_one_hot_cubic_index':hot_index,'real_Gaussian_vector_orders':targets,
                      'same_lattice_different_sampling_cost':[correlated_cost(z) for z in ([3,5,7],[3,5,7,11],[3,5,7,11,13])]},indent=2,sort_keys=True))


if __name__=='__main__':
    main()
