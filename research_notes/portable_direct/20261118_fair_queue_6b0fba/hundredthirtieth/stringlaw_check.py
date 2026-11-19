"""Exact weighted-word moments, spectral sign brackets and a sparse-rate check."""
import argparse
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha256
from itertools import permutations, product
import json
from math import comb, factorial, prod
from pathlib import Path
import runpy


SIGNED = Path("experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py")
SIGNED_HASH = "6f0d79a519c53fed1300b3fabf500c34e30aa46cdd63b409fa6ecc115071ecb4"
RECT = ((1, -1, 0), (-1, 1, 0), (0, 0, 0))
PATH = ((1, -1, 0), (-1, 2, -1), (0, -1, 1))


def theory(a, b, matrix):
    q = F(a*b, (a+b)**2)
    gram = [[sum(x*y for x, y in zip(r, s)) for s in matrix] for r in matrix]
    d2 = sum(gram[i][i] for i in range(3))
    d4 = sum(v*v for row in gram for v in row)
    A = q*(1-q)/(2+q)
    B = q*q*(2-3*q)/(2*(2+q)*(6+q))
    K = 1-2*B/A**2
    return d2*A, 3*(d2*A)**2+6*d4*K*A**2


def word_moments(n, a, b, matrix):
    rates = (a,)*3 + (b,)*3
    # Spectator clocks may be removed because all six exponential clocks are independent.
    active = tuple(i for i in range(6) if
                   (any(matrix[i]) if i < 3 else any(row[i-3] for row in matrix)))
    @lru_cache(None)
    def step(left):
        if not any(left):
            return (F(1), F(0), F(0), F(0), F(0))
        denom = sum(x*rates[i] for i,x in zip(active,left))
        totals = [F(0) for _ in range(5)]
        for pos,(j,m) in enumerate(zip(active,left)):
            if not m:
                continue
            add = sum(matrix[i][j-3]*(n-u) for i,u in zip(active,left) if i<3) if j>=3 else 0
            nxt = list(left)
            nxt[pos] -= 1
            tail = step(tuple(nxt))
            prob = F(m*rates[j],denom)
            for k in range(5):
                totals[k] += prob*sum(comb(k,h)*add**(k-h)*tail[h] for h in range(k+1))
        return tuple(totals)
    raw = step((n,)*len(active))
    assert raw[0] == 1 and raw[1] == 0
    return raw[2]/n**2, raw[4]/n**4


def direct_word(nat, a, b, matrix):
    rates = (a,)*3 + (b,)*3
    moments = [F(0) for _ in range(5)]
    for word in permutations(range(6)):
        prob, remaining = F(1), sum(rates)
        for j in word:
            prob *= F(rates[j],remaining)
            remaining -= rates[j]
        score = sum(matrix[i][j] for i in range(3) for j in range(3)
                    if word.index(i) < word.index(3+j))
        for k in range(5):
            moments[k] += prob*score**k
    assert moments[0] == 1 and moments[1] == 0
    assert nat['shortest_path_multiplicity']((1,-1,1,-1,1,-1)) == factorial(6)
    return moments[2],moments[4]


def partitions(k):
    def grow(blocks,i):
        if i == k:
            yield blocks
            return
        for j in range(len(blocks)):
            yield from grow(blocks[:j]+(blocks[j]+(i,),)+blocks[j+1:],i+1)
        yield from grow(blocks+((i,),),i+1)
    return tuple(grow((),0))


def falling(n,m):
    return prod(n-i for i in range(m))


@lru_cache(None)
def signed_choices(n, sizes):
    ans = 0
    for signs in product((1,-1), repeat=len(sizes)):
        h = signs.count(1)
        ans += falling(n,h)*falling(n,len(sizes)-h)*prod(s**d for s,d in zip(signs,sizes))
    return ans


@lru_cache(None)
def compatible_orders(a,b,nleft,pres):
    """All required fast<slow comparisons, using the exact first-clock rule."""
    rates = (a,)*nleft+(b,)*len(pres)
    full = (1 << len(rates))-1
    @lru_cache(None)
    def visit(done):
        if done == full:
            return F(1)
        rem = sum(r for j,r in enumerate(rates) if not done & (1<<j))
        sums = F(0)
        for j,r in enumerate(rates):
            if done & (1<<j) or (j>=nleft and pres[j-nleft] & ~done):
                continue
            sums += F(r,rem)*visit(done | (1<<j))
        return sums
    return visit(0)


def rectangle_moment(n,a,b,k):
    packets = partitions(k)
    total = F(0)
    for l in packets:
        left_index = {i:j for j,block in enumerate(l) for i in block}
        wl = signed_choices(n,tuple(map(len,l)))
        for r in packets:
            wr = signed_choices(n,tuple(map(len,r)))
            if wl and wr:
                pres = tuple(sum(1<<j for j in {left_index[i] for i in block}) for block in r)
                total += wl*wr*compatible_orders(a,b,len(l),pres)
    return total/n**k


def hyper_bounds(v,q,mu,terms=45):
    def bounds(c):
        term,value=F(1),F(1)
        for j in range(1,terms+1):
            term *= -q*mu/(j*(c+j-1))
            value += term
        ratio = q*mu/((terms+1)*(c+terms))
        assert ratio < 1
        other = value-term*ratio
        return min(value,other), max(value,other)
    a,b=bounds(v),bounds(1-v)
    return a[0]+b[0]-2,a[1]+b[1]-2


def spectral_brackets(a,b,bins):
    v = F(min(a,b),a+b)
    q = v*(1-v)
    out = []
    for n,(left,right) in enumerate(bins):
        lo,hi = F(left),F(right)
        def sign(x):
            u,w=hyper_bounds(v,q,x)
            assert u*w>0
            return 1 if u>0 else -1
        s=sign(lo)
        assert sign(hi)==-s
        for _ in range(23):
            mid=(lo+hi)/2
            if sign(mid)==s:
                lo=mid
            else:
                hi=mid
        out.append([str(lo),str(hi)])
    # 3rd Dirichlet root exceeds (2.5 pi)^2/(4q); pi > 3.14
    assert F(bins[-1][1]) < (F(5,2)*F(314,100))**2/(4*q)
    return out


def compute(root):
    source = root/SIGNED
    assert sha256(source.read_bytes()).hexdigest()==SIGNED_HASH
    nat=runpy.run_path(str(source))
    cases=[]
    for name,a,b,matrix,brackets in [
        ('rectangle',3,1,RECT,[(35,36),(62,63)]),
        ('path_laplacian',5,2,PATH,[(34,35),(56,57)])]:
        V,T=theory(a,b,matrix)
        rows=[]
        for n in (1,2,3):
            m2,m4=word_moments(n,a,b,matrix)
            target=tuple(n*(-1)**i for i in range(6))
            mult=nat['shortest_path_multiplicity'](target)
            assert nat['shortest_event_count'](target)==6*n
            assert nat['endpoint_multiplicity'](6*n,target)==mult==factorial(6*n)//factorial(n)**6
            if n==1:
                assert direct_word(nat,a,b,matrix)==(m2,m4)
            if matrix==RECT:
                assert rectangle_moment(n,a,b,2)==m2 and rectangle_moment(n,a,b,4)==m4
            assert m2==V
            rows.append((n,m4,mult))
        ext=(rows[0][1]-8*rows[1][1]+9*rows[2][1])/2
        assert ext==T
        cases.append(dict(case=name,rates=[a,b],cross_matrix=matrix,variance=str(V),
                     fourth_limit=str(T),excess_limit=str(T/V**2-3),
                     word_rows=[dict(N=n,raw_axis_words=mult,NH_fourth=str(m)) for n,m,mult in rows],
                     periodic_eigenvalue_rational_brackets=spectral_brackets(a,b,brackets)))
    rare=[]
    for n,tau in ((16,1),(256,1),(4096,1),(4096,4),(8192,F(1,4)),(4096,64)):
        a,b=F(n,tau).as_integer_ratio()
        V=rectangle_moment(n,a,b,2)
        T=rectangle_moment(n,a,b,4)
        assert V==theory(a,b,RECT)[0]
        ex=T/V**2-3
        rare.append(dict(N=n,fast_slow_ratio=str(F(a,b)),N_over_ratio=str(tau),
                         scaled_variance=str(V*F(a,b)),exact_excess=str(ex),
                         rounded_excess=round(float(ex),9),
                         critical_limit=str(2+F(1,2*tau))))
    return dict(task='RS-X6-WEIGHTED-CIRCULATION-CANCELLATION',
                native_kernel_sha256=SIGNED_HASH,examples=cases,
                rectangular_two_rate_checks=rare)


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,default=Path.cwd())
    args=parser.parse_args()
    print(json.dumps(compute(args.repo),ensure_ascii=False,indent=2,sort_keys=True))
