"""Count affine orbits and check finite-ring bounds, using standard-library integer arithmetic."""
from collections import Counter
from itertools import product
import json
from math import comb, gcd, lcm


def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]


def units(n):
    return [u for u in range(1,n) if gcd(u,n)==1]


def phi(n):
    return sum(gcd(k,n)==1 for k in range(1,n+1))


def mu(n):
    value=1
    p=2
    while p*p<=n:
        if n%p==0:
            n//=p
            if n%p==0:
                return 0
            value=-value
        p+=1
    return -value if n>1 else value


def signed_cycles(n,u):
    total=0
    for d in divisors(n)[1:]:
        k=1
        while pow(u,k,d) not in (1,d-1):
            k+=1
        total+=phi(d)//((1 if d==2 else 2)*k)
    return total


def affine_power(n,u,b,k):
    """Power by squaring, without division by u-1 (which can be a zero divisor)."""
    a,c=1,0
    while k:
        if k%2:
            a,c=a*u%n,(u*c+b)%n
        u,b=u*u%n,b*(u+1)%n
        k//=2
    return a,c


def affine_cycles(n,u,b):
    d=1
    while pow(u,d,n)!=1:
        d+=1
    _,shift=affine_power(n,u,b,d)
    order=d*n//gcd(n,shift)
    # Number of length-j orbits from points fixed by affine^k for k|j.
    periods={}
    for j in divisors(order):
        a,c=affine_power(n,u,b,j)
        g=gcd(a-1,n)
        count=(g if c%g==0 else 0)-sum(k*v for k,v in periods.items() if j%k==0)
        assert count%j==0
        if count:
            periods[j]=count//j
    assert sum(k*v for k,v in periods.items())==n
    return periods


def perms(n,u,b):
    return [[min(u*x%n,(-u*x)%n)-1 for x in range(1,n//2+1)],[(u*x+b)%n for x in range(n)]]


def cycles(perm):
    seen=set()
    bins=Counter()
    for start in range(len(perm)):
        if start in seen:
            continue
        x,k=start,0
        while x not in seen:
            seen.add(x)
            x,k=perm[x],k+1
        bins[k]+=1
    return bins


def orbit_data(n):
    us=units(n)
    sum_full=sum_center=0
    max_moved=-1
    best=[]
    for u in us:
        a=signed_cycles(n,u)
        for b in range(n):
            e=affine_cycles(n,u,b)
            ka,ib=perms(n,u,b)
            assert sum(cycles(ka).values())==a and cycles(ib)==e
            exponent=2*a+sum(e.values())
            fixed=2**exponent
            sum_full+=fixed
            if b==0:
                sum_center+=fixed
            if u!=1 or b:
                if exponent>max_moved:
                    max_moved=exponent
                    best=[]
                if exponent==max_moved:
                    best.append((u,b))
    assert sum_full%(len(us)*n)==0 and sum_center%len(us)==0
    if n>=3:
        t=gcd(n,2)
        expected={(n-1,b) for b in range(0,n,t)}
        if n>=12 and n%8==4:
            expected.update({(1+n//2,0),(1+n//2,n//2)})
        assert set(best)==expected
        assert max_moved==2*(n//2)+n-(n-t)//2
    return [sum_full//(n*len(us)),sum_center//len(us),len(best)]


def prime_stats(p):
    m=p-1
    labels=2**(2*m+1)
    sizes={d:p*sum(mu(k//d)*4**(m//lcm(k,2))*(2**(1+m//k)-2)
                     for k in divisors(m) if k%d==0)
           for d in divisors(m) if d>1}
    const={p*d:2*sum(mu(k//d)*4**(m//lcm(k,2)) for k in divisors(m) if k%d==0)
           for d in divisors(m)}
    nonconstant=labels-2*4**(m//2)
    sizes[1]=nonconstant-sum(sizes.values())
    sizes={k:v for k,v in (sizes|const).items() if v}
    refl=(p*(2**(1+m//2)-2)+2)*4**(m//2)
    extra=0
    for d in divisors(m):
        if d>1 and d%2 and mu(d):
            extra-=mu(d)*p*4**(m//(2*d))*(2**(1+m//d)-2**(1+m//(2*d)))
    assert labels-sizes.get(1,0)==refl+extra
    classes=Counter()
    for size,count in sizes.items():
        assert (count*size)%(p*m)==0
        classes[1+(m//size) if size%p else 1]+=(count*size)//(p*m)
    return {'labelled_stabilizer_sizes':dict(sorted(sizes.items())),
            'has_reflection':refl,'nonreflection_extra':extra,'number_free':sizes.get(1,0),
            'full_orbit_partition_by_common_orbits':dict(sorted(classes.items()))}


def direct(n):
    """Traverse the action on every labelled colouring, separately for the two word types."""
    maps=[]
    d=n//2
    def bit_action(p):
        table=[]
        for mask in range(1<<len(p)):
            table.append(sum(((mask>>i)&1)<<j for i,j in enumerate(p)))
        return table
    for u,b in product(units(n),range(n)):
        a,c=perms(n,u,b)
        maps.append((bit_action(a),bit_action(c),b))
    full=set()
    centre=set()
    hist=Counter()
    for i,j,k in product(range(2**d),range(2**d),range(2**n)):
        images=[(f[i],f[j],g[k]) for f,g,_ in maps]
        full.add(min(images))
        centre.add(min(im for im,(_,_,b) in zip(images,maps) if not b))
        hist[images.count((i,j,k))]+=1
    return len(full),len(centre),dict(hist)


def subgroup_hist(n):
    """Construct subgroups as graphs of cocycles over a translation quotient."""
    us=units(n)
    fixed={}
    for mask in range(1<<len(us)):
        K=[u for i,u in enumerate(us) if mask>>i&1]
        if 1 not in K or any(u*v%n not in K for u,v in product(K,repeat=2)):
            continue
        edge_orbits=0
        for d in divisors(n)[1:]:
            signed={s*u%d for s in (-1,1) for u in K}
            edge_orbits+=phi(d)//len(signed)
        for h in divisors(n):
            for values in product(range(h),repeat=len(K)-1):
                beta=dict(zip(K,(0,)+values))
                if any((beta[u*v%n]-beta[u]-u*beta[v])%h for u,v in product(K,repeat=2)):
                    continue
                group=frozenset((u,b) for u in K for b in range(beta[u],n,h))
                saved=sum(gcd(u-1,h) for u in K if beta[u]%gcd(u-1,h)==0)
                assert saved%len(K)==0
                fixed[group]=4**edge_orbits*2**(saved//len(K))
    exact={}
    hist=Counter()
    for group in sorted(fixed,key=len,reverse=True):
        count=fixed[group]-sum(v for other,v in exact.items() if group<other)
        assert count>=0
        exact[group]=count
        hist[len(group)]+=count
    assert sum(hist.values())==2**(2*(n//2)+n)
    return dict(sorted((k,v) for k,v in hist.items() if v)),len(exact)


def sparse_incidence(p):
    """Exhaustively compare three-element sets with the centred-progression formula."""
    from itertools import combinations
    from fractions import Fraction
    m=p-1
    d=m//2
    centre_counts=Counter()
    for I in combinations(range(p),3):
        c=sum(I)*pow(3,-1,p)%p
        J=frozenset((x-c)%p for x in I)
        stabilizer=[u for u in units(p) if {(u*x)%p for x in J}==J]
        centre_counts[len(stabilizer)]+=1
    assert not (set(centre_counts)-{1,2,3})
    total=comb(p,3)
    event=Fraction(centre_counts[2],total)
    if 3 in centre_counts:
        event+=Fraction(centre_counts[3],total*4**(m//3))
    expected=Fraction(3,p-2)
    if m%3==0:
        expected+=Fraction(2,(p-2)*4**(m//3))
    assert event==expected
    return {'stabilizer_of_incidence_alone':dict(sorted(centre_counts.items())),
            'symmetric_joint_probability':str(event)}


def iso_control():
    n=16
    left={1,15,7,9}
    right={3,13,5,11}
    exclusion={2,14}
    def f(x):
        return (x+4*(x%2))%n
    assert len({f(x) for x in range(n)})==n
    for x,y in product(range(n),repeat=2):
        d=(y-x)%n
        z=(f(y)-f(x))%n
        assert (d in left)==(z in right)
        assert (d in exclusion)==(z in exclusion)
        assert (d==0)==(z==0)
    preserving=[u for u in units(n) if {u*x%n for x in exclusion}==exclusion]
    assert all({u*x%n for x in left}!=right for u in preserving)
    return {'modulus':n,'permutation':[f(k) for k in range(n)],'exclusion_preserving_units':preserving}


def main():
    # n=1 has two labelled values of the only incidence bit and no nonidentity action.
    arith={n:orbit_data(n) for n in range(2,49)}
    small={}
    subgroup={}
    for n in range(2,8):
        full,centre,hist=direct(n)
        computed,subgroup[n]=subgroup_hist(n)
        assert computed==hist
        assert [full,centre]==arith[n][:2]
        small[n]=[full,centre,dict(sorted(hist.items()))]
        if n in (3,5,7):
            assert prime_stats(n)['labelled_stabilizer_sizes']==hist
    prime={p:prime_stats(p) for p in (3,5,7,11,13,17,19,31)}
    for p,stats in prime.items():
        cnt=stats['full_orbit_partition_by_common_orbits']
        assert sum(cnt.values())==arith[p][0] and sum(k*v for k,v in cnt.items())==arith[p][1]
    for p in prime:
        assert arith[p][1]-arith[p][0]==4**((p-1)//2)*(2**p-2)//p
    print(json.dumps({'subgroups_verified_n2to7':subgroup,'sparse_weight3':{p:sparse_incidence(p) for p in (5,7,11,13,17,19)},
                      'general_isomorphism_control':iso_control(),'arithmetic_full_common_number_of_maximizers_n2to48':arith,
                      'mod1_full_common':[2,2], 'exhaustive_full_common_and_stabilizer_hist':small,
                      'prime_stabilizers':prime},sort_keys=True,indent=2))


if __name__=='__main__':
    main()
