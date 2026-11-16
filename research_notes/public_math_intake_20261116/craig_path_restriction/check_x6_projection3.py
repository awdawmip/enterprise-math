"""Exact projection and all pairwise second moments on signed X6 shortest paths."""
from collections import Counter
from fractions import Fraction as Q
from hashlib import sha1
from itertools import combinations
from math import isqrt
from math import comb
from pathlib import Path
import importlib.util


def kernel():
    rel = Path("experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py")
    root = Path(__file__).resolve().parent
    for f in [root/"signed_brc.py", *(base/rel for base in [root,*root.parents])]:
        if f.is_file():
            raw = f.read_bytes()
            if sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest() == '300a96e3dc24bf6fff73743037a0347a8bc83176':
                spec = importlib.util.spec_from_file_location('x6pinned', f)
                m = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(m)
                return m
    raise RuntimeError("Supply the pinned signed_brc.py next to the checker")


def paths(counts):
    left = list(counts)
    def generate(prefix):
        if not any(left):
            yield tuple(prefix)
            return
        for axis, n in enumerate(left):
            if n:
                left[axis] -= 1
                prefix.append(axis)
                yield from generate(prefix)
                prefix.pop()
                left[axis] += 1
    return generate([])


def inputs():
    samples = [(1,1,1,1,1,1), (2,-1,1,-1,1,1), (1,-2,1,-1,0,0),
               (2,2,2,0,0,0), (3,1,-2,0,0,0), (0,0,0,-3,0,1),
               (-2,0,-2,0,1,2)]
    for i,j,k in combinations(range(4),3):
        for triples in [(1,1,2),(2,2,1),(3,1,1)]:
            z=[0]*6
            for a,n in zip((i,j,k),triples):
                z[a]=(-1)**a*n
            samples.append(tuple(z))
    return list(dict.fromkeys(samples))


def run():
    src=kernel()
    npaths = pair_rows = moment_rows = 0
    for endpoint in inputs():
        m=list(map(abs,endpoint))
        total=src.shortest_path_multiplicity(endpoint)
        pairs=list(combinations([i for i,n in enumerate(m) if n],2))
        bins={e:Counter() for e in pairs}
        sums=Counter()
        products=Counter()
        endpoints_seen=0
        for w in paths(m):
            endpoints_seen+=1
            count={}
            for i,j in pairs:
                v=tuple(a for a in w if a in (i,j))
                bins[i,j][v]+=1
                count[i,j]=sum(a==i and b==j for u,a in enumerate(v) for b in v[u+1:])
                sums[i,j]+=count[i,j]
            for u,e in enumerate(pairs):
                for f in pairs[u:]:
                    products[e,f]+=count[e]*count[f]
        assert endpoints_seen==total
        npaths+=total
        for i,j in pairs:
            assert len(bins[i,j])==comb(m[i]+m[j],m[i])
            assert set(bins[i,j].values())=={total//len(bins[i,j])}
            assert Q(sums[i,j],total*m[i]*m[j])==Q(1,2)
            pair_rows+=1
        def theoretical(e,f):
            i,j=e
            if e==f:
                return Q(m[i]+m[j]+1,12*m[i]*m[j])
            shared=set(e)&set(f)
            if not shared:
                return 0
            a,=shared
            return Q(1 if e.index(a)==f.index(a) else -1,12*m[a])
        cov={}
        for u,e in enumerate(pairs):
            for f in pairs[u:]:
                i,j=e
                a,b=f
                raw=Q(products[e,f],total*m[i]*m[j]*m[a]*m[b])-Q(1,4)
                assert raw==theoretical(e,f)
                cov[e,f]=cov[f,e]=raw
                moment_rows+=1
        for i,j,k in combinations([a for a,n in enumerate(m) if n],3):
            edges={(i,j):1,(j,k):1,(i,k):-1}
            actual=sum(c*d*cov[e,f] for e,c in edges.items() for f,d in edges.items())
            assert actual==sum(Q(1,12*m[a]*m[b]) for a,b in edges)
    return len(inputs()),npaths,pair_rows,moment_rows


def check_character():
    # Bins of the central label 2T-1 as integer numerators over N squared.
    # Certified dyadic primitive-root real parts use interval arithmetic.
    grid = 1 << 90
    def radical(bounds):
        lo,hi=bounds
        lower=isqrt((lo.numerator*grid*grid)//lo.denominator)
        upper_floor=isqrt((hi.numerator*grid*grid)//hi.denominator)
        upper=upper_floor if Q(upper_floor,grid)**2==hi else upper_floor+1
        return Q(lower,grid),Q(upper,grid)
    def product_interval(x,y):
        values=[a*b for a in x for b in y]
        return min(values),max(values)
    src=kernel()
    for n in (1,2,4):
        bins=Counter()
        for word in paths((n,n,n,0,0,0)):
            seen=[0,0,0]; cyclic=0
            for step in word:
                cyclic+=seen[(step-1)%3]
                seen[step]+=1
            num=2*cyclic-3*n*n
            bins[num]+=1
        count=sum(bins.values())
        assert count==src.shortest_path_multiplicity((n,n,n,0,0,0))
        assert all(bins[t]==bins[-t] and abs(t)<=n*n for t in bins)
        assert sum(t*t*v for t,v in bins.items())==n*n*count
        # r=first positive 8N²-th root. Radial average is E Re r^num.
        root=(Q(0),Q(0))
        order=4
        while order<8*n*n:
            root=radical(tuple((1+c)/2 for c in root))
            order*=2
        reals=[(Q(1),Q(1)),root]
        for t in range(2,n*n+1):
            lo,hi=product_interval(root,reals[-1])
            prevlo,prevhi=reals[-2]
            # Fixed-grid outward rounding prevents denominator growth.
            reals.append((Q(((2*lo-prevhi)*grid).__floor__(),grid),
                          Q(((2*hi-prevlo)*grid).__ceil__(),grid)))
        low=1-sum(v*reals[abs(t)][1] for t,v in bins.items())/count
        high=1-sum(v*reals[abs(t)][0] for t,v in bins.items())/count
        assert 0<low<=high<Q(1,2*n*n)
        print('three-axis cycle N, paths, radial deficit in 1e-9:',n,count,
              (low*10**9).__floor__(),(high*10**9).__ceil__())


if __name__=='__main__':
    print("endpoints, paths, complete pair laws, covariance entries:",run())
    check_character()
