"""Exact finite evidence for the characteristic-seven correspondence obstruction."""
from collections import Counter
from itertools import product
import json


class Field:
    """Quadratic extension by a root squaring to delta. Elements are packed integers."""

    def __init__(self, size, plus, times, delta):
        self.base = size
        self.size = size**2
        self.plus = plus
        self.times = times
        self.delta = delta

    def add(self, x, y):
        b = self.base
        return self.plus(x % b, y % b) + b*self.plus(x//b, y//b)

    def mul(self, x, y):
        b = self.base
        a, c = x % b, x//b
        d, e = y % b, y//b
        return (self.plus(self.times(a,d), self.times(self.delta,self.times(c,e))) +
                b*self.plus(self.times(a,e), self.times(c,d)))

    def power(self, x, n):
        out = 1
        while n:
            if n%2:
                out = self.mul(out,x)
            x = self.mul(x,x)
            n //= 2
        return out


# a+7b labels a+bi over F49; coefficients arranged in increasing order.
F = [30,4,21,22,47,1]
G = [1,0,1,1]
H = [2,0,1]


def evaluate(k, f, x):
    value = 0
    for a in reversed(f):
        value = k.add(k.mul(value,x),a)
    return value


def trim(f):
    while f and f[-1]==0:
        f.pop()
    return f


def multiply(k,f,g):
    out = [0]*(len(f)+len(g)-1)
    for i,x in enumerate(f):
        for j,y in enumerate(g):
            out[i+j] = k.add(out[i+j],k.mul(x,y))
    return trim(out)


def remainder(k,f,g):
    out = list(f)
    inverse = k.power(g[-1],k.size-2)
    while len(out)>=len(g):
        coeff = k.mul(6,k.mul(out[-1],inverse))
        offset = len(out)-len(g)
        for j,y in enumerate(g):
            out[offset+j] = k.add(out[offset+j],k.mul(coeff,y))
        trim(out)
    return out


def pgcd(k,f,g):
    while g:
        f,g = g,remainder(k,f,g)
    return [k.mul(c,k.power(f[-1],k.size-2)) for c in f]


def points(k):
    roots = [[] for _ in range(k.size)]
    for y in range(k.size):
        roots[k.mul(y,y)].append(y)
    nx = ny = 1
    ncor = 2  # the two branches at infinity have leading square 1
    for x in range(k.size):
        nyx = len(roots[evaluate(k,F,x)])
        nxx = sum(len(roots[k.mul(y,evaluate(k,H,x))]) for y in roots[evaluate(k,G,x)])
        nx += nxx
        ny += nyx
        ncor += nxx*nyx
    return dict(field_size=k.size,source=nx,target=ny,normalised_zero_correspondence=ncor)


def geometric_checks():
    k = Field(7,lambda x,y:(x+y)%7,lambda x,y:(x*y)%7,6)
    plus = [[k.add(i,j) for j in range(49)] for i in range(49)]
    times = [[k.mul(i,j) for j in range(49)] for i in range(49)]
    nonsquare = min(set(range(1,49))-{times[i][i] for i in range(49)})
    ext = Field(49,lambda x,y:plus[x][y],lambda x,y:times[x][y],nonsquare)
    factors = [[48,48,1],[46,22,6,1]]
    assert multiply(k,*factors)==F
    assert all(all(evaluate(k,f,x) for x in range(49)) for f in factors+[G])
    assert pgcd(k,F,multiply(k,G,H))==[1] and pgcd(k,G,H)==[1]
    for f in [F,G,H]:
        assert pgcd(k,f,[k.mul(i%7,c) for i,c in enumerate(f) if i])==[1]
    finite_rational = [(x,y) for x in range(49) if evaluate(k,H,x)==0
                       for y in range(49) if k.mul(y,y)==evaluate(k,G,x)]
    counts = [points(k),points(ext)]
    assert len(finite_rational)==4 and [r['target'] for r in counts]==[55,2377]
    assert [(r['source'],r['normalised_zero_correspondence']) for r in counts]==[(65,58),(2425,2322)]
    a1=50-counts[0]['target']
    a2=(a1**2-(2402-counts[1]['target']))//2
    weil=[49**2,-49*a1,a2,-a1,1]
    assert weil==[2401,245,0,5,1]
    return dict(f49_i_squared=6,extension_nonsquare=nonsquare,quintic_ascending=F,
                irreducible_quadratic_and_cubic=factors,branch_gcd_with_source=[1],
                rational_finite_z_fixed=finite_rational,source_fixed_orbits=[1]*5+[3],
                target_weierstrass_orbits=[1,2,3],point_counts=counts,weil_ascending=weil,
                zero_correspondence_bidegree=[2,4],geometric_genus=2*5-1+20//2,
                arithmetic_genus=1+2*4+2*(5-1)+4*(2-1))


def two_torsion():
    # Even subsets of six Weierstrass labels, modulo complementary subsets.
    V = [i for i in range(32) if i.bit_count()%2==0]
    perm = (0,2,1,4,5,3)
    def canonical(x):
        return min(x,63^x)
    def frob(x):
        return canonical(sum(1<<perm[i] for i in range(6) if x&(1<<i)))
    def iterate(x,n):
        for _ in range(n%6):
            x=frob(x)
        return x
    def pair(x,z):
        return (x&z).bit_count()%2
    def real_frob(x):
        return frob(x)^iterate(x,-1)
    fixed=[x for x in V if frob(x)==x]
    triple=[x for x in V if iterate(x,3)==x]
    v3=[x for x in V if real_frob(x)==x]
    assert len(fixed)==2 and len(triple)==8 and len(v3)==4
    attainable=Counter()
    for four in product(fixed,repeat=4):
        for x in triple:
            # O maps to 0. Use all possible assignments of the other fixed points.
            image=[0,*four,x,frob(x),iterate(x,2)]
            attainable[tuple(z for z in V if image.count(z)%2)]+=1
    assert sum(attainable.values())==128

    basis=[3,5,9,17]
    terms={x:[i for i in range(4) if x & (2<<i)] for x in V}
    cases=[]
    for a,b in product((0,1),repeat=2):
        # Numerically (u j_X)_*[X] corresponds to v'=a-5b-by.
        def polar(x,z):
            return ((a^b)*pair(x,z)+b*pair(x,real_frob(z)))%2
        radical=[x for x in V if all(not polar(x,z) for z in V)]
        initial={x:sum(polar(basis[i],basis[j]) for i in terms[x] for j in terms[x] if j<i)%2
                 for x in V}
        assert all(initial[x^z]^initial[x]^initial[z]==polar(x,z) for x in V for z in V)
        matches=[]; weights=Counter()
        for t,c in product(V,(0,1)):
            support=tuple(x for x in V if initial[x]^pair(x,t)^c)
            weights[len(support)]+=1
            if support in attainable:
                matches.append(list(support))
        if matches and b:
            assert radical==v3
        assert bool(matches)==(a==0)
        cases.append(dict(a=a,b=b,radical=radical,all_quadratic_support_sizes=dict(weights),
                          compatible_supports=matches))
    return dict(subset_encoding='smallest bit mask for an even subset and its complement',
                frobenius_permutation=perm,two_torsion=V,fixed=fixed,fixed_by_cube=triple,
                cubic_plane=v3,source_assignments=sum(attainable.values()),
                image_parity_supports=[dict(support=list(z),assignments=n) for z,n in sorted(attainable.items())],
                cases=cases)


def main():
    # v=(H+b sqrt(417))/2; to avoid confusing this b with the y-basis
    # coefficient, note coefficient of 1 is (H+5b)/2 for y=(-5+sqrt(417))/2.
    allowed=[]
    for h in range(1,21):
        for b in range(-h,h+1):
            if (h-b)%2==0 and h*h>417*b*b and (h+5*b)%4==0 and h>=5:
                allowed.append(h)
    assert allowed==[8,12,16,20]
    out=dict(geometry=geometric_checks(),two_torsion=two_torsion(),
             necessary_heights_through_20=allowed)
    print(json.dumps(out,indent=2,sort_keys=True))


if __name__=='__main__':
    main()
