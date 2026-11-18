"""Exact finite checks for occupancy majorization and its scaled profile."""
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
import json


def root(x, r):
    lo, hi = 0, 1
    while hi**r <= x:
        lo, hi = hi, 2*hi
    while hi-lo > 1:
        m = (hi+lo)//2
        if m**r <= x:
            lo = m
        else:
            hi = m
    return lo


def kernels(limit, r):
    out = [0]*(limit+1)
    free = [0]*(limit+1)
    for b in range(1,limit+1):
        if out[b] == 0:
            for t in range(1,root(limit//b,r)+1):
                assert out[b*t**r] == 0
                out[b*t**r] = b
        free[b] = free[b-1]+int(out[b]==b)
    return out,free


def all_pairs():
    U, maxL = 270, 160
    nwin = 0
    comparisons = 0
    formula_checks = 0
    for r in range(2,9):
        ker,Q = kernels(U+maxL,r)
        left = [None]
        occup = Counter()
        for L in range(1,maxL+1):
            occup[ker[L]] += 1
            maxk = root(L,r)
            left.append([sum(max(z-k,0) for z in occup.values()) for k in range(maxk+1)])
        for u in range(U+1):
            counts = Counter()
            losses = defaultdict(int)
            for L in range(1,maxL+1):
                b=ker[u+L]
                for k in range(counts[b]+1):
                    losses[k] += 1
                counts[b] += 1
                cap = max(counts.values())
                nwin += 1
                for k in range(1,max(cap,len(left[L])-1)+1):
                    init = left[L][k] if k<len(left[L]) else 0
                    assert losses[k] <= init
                    comparisons += 1
                    if u in (0,1,3,7,23,67,199,270):
                        value = sum(max(0,Q[(u+L)//j**r]-Q[u//(j-k)**r])
                                    for j in range(k+1,root(u+L,r)+1))
                        assert value == losses[k]
                        if u*((k+1)**r-1)<=L:
                            near = sum(Q[(u+L)//j**r] for j in range(k+1,root(u+L,r)+1))
                            assert value == near-u
                        formula_checks += 1
                extra = r==2 and (L,u) in [(6,3),(7,3)]
                eq = (L<2**r or Q[u+L]==Q[L] or extra)
                assert (len(counts)==Q[L]) == eq
    return dict(r_inclusive=[2,8],u_inclusive=[0,U],L_inclusive=[1,maxL],
                integer_windows=nwin,occupancy_comparisons=comparisons,
                exact_stride_and_near_checks=formula_checks)


def small_squares():
    ker,Q = kernels(100,2)
    near,far = {},{}
    for L in range(4,16):
        ends = []
        stay = []
        for u in range(L*L//4+1):
            D = len(set(ker[u+1:u+L+1]))
            if D==Q[L]:
                (ends if 3*u>=L else stay).append(u)
        near[L] = stay
        if ends:
            far[L] = ends
    assert far == {6:[3],7:[3]}
    return dict(near_equals=near,all_far_equals=far)


@lru_cache(maxsize=None)
def mobius_slice(n):
    out = [1]*(n+1)
    for p in range(2,n+1):
        if not any(p%v==0 for v in range(2,root(p,2)+1)):
            for j in range(p,n+1,p):
                out[j] *= -1
            for j in range(p*p,n+1,p*p):
                out[j] = 0
    return out


def free_count_builder(limit,r):
    mu=mobius_slice(root(limit,r))
    terms=[(d**r,mu[d]) for d in range(1,len(mu)) if mu[d]]
    @lru_cache(maxsize=None)
    def free(n):
        total=0
        for p,m in terms:
            if p>n:
                break
            total+=m*(n//p)
        return total
    return free


def harmonic(j,r):
    return sum((Fraction(1,n**r) for n in range(1,j+1)),Fraction())


@lru_cache(maxsize=None)
def zeta_bounds(r):
    T, scale = 8192, 10**20
    small = sum(scale//n**r for n in range(1,T+1))
    return (Fraction(small,scale)+Fraction(1,(r-1)*(T+1)**(r-1)),
            Fraction(small+T,scale)+Fraction(1,(r-1)*T**(r-1)))


def scaled_profile(t,r,k):
    j=k+1
    while t*j**r >= (1+t)*(j-k)**r:
        j+=1
    h = harmonic(j-1,r)
    lead = h+t*(h-harmonic(j-k-1,r))
    lo,hi = zeta_bounds(r)
    return (1-lead/lo,1-lead/hi)


def enclosed(lo,hi):
    precision=10**8
    return [(precision*lo).__floor__(),(precision*hi).__ceil__()]


def scale_samples():
    rows=[]
    for r in (2,3,4,6):
        for k in (1,2):
            # Exact integer threshold in this experiment.
            L=10000*((k+1)**r-1)
            u_values=(0,10000,L,5*L)
            q=free_count_builder(L+max(u_values),r)
            sample=[]
            base=sum(q(L//j**r) for j in range(k+1,root(L,r)+1))
            for u in u_values:
                actual=sum(max(0,q((u+L)//j**r)-q(u//(j-k)**r))
                           for j in range(k+1,root(u+L,r)+1))
                lo,hi=scaled_profile(Fraction(u,L),r,k)
                sample.append(dict(u=u,F=actual,initial_minus_F=base-actual,
                                   continuous_F_over_L_times_1e8=enclosed(lo,hi)))
            zlo,zhi=zeta_bounds(r)
            first=harmonic(k,r)/((k+1)**r-1)
            rows.append(dict(r=r,k=k,L=L,observations=sample,
                             sharp_outer_deficit_over_L_times_1e8=enclosed(first/zhi,first/zlo)))
    return rows


def geometric():
    n=0
    for q in (2,3,4,6):
        def kernel(x):
            while x%q==0:
                x//=q
            return x
        for L in range(1,25):
            origin=Counter(kernel(i) for i in range(1,L+1))
            major=sorted(origin.values(),reverse=True)+[0]*L
            for u in range(55):
                occ=sorted(Counter(kernel(i) for i in range(u+1,u+L+1)).values(),reverse=True)+[0]*L
                a=b=0
                for j in range(L):
                    a+=major[j]; b+=occ[j]
                    assert a>=b
                n+=1
    return n


if __name__=='__main__':
    print(json.dumps(dict(finite=all_pairs(),square_exception_check=small_squares(),
                          exact_scaled_samples=scale_samples(),
                          geometric_family_windows=geometric()),indent=2))
