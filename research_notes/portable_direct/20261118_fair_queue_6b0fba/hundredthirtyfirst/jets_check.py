"""Integer path-jet content, suffix decoding and endpoint-restricted fibers."""
import argparse
from collections import Counter
from hashlib import sha256
from itertools import combinations, groupby, product
import json
from math import comb, gcd
from pathlib import Path
import runpy


SOURCE = 'experiments/x6_rotation_path_tensor_jet_two_cycle_20260906/check_two_cycle_tensor_jet.py'
SOURCE_HASH = 'dc9926ce1cd1aa4c2f89f1ef1b8d5acee05c76ab51b392faaf58d40cb413b169'
MODULI = (0, 2, 3, 4, 6, 8, 9)


def residue(x, m):
    return x % m if m else x


def runs(word):
    start = 0
    for axis, positions in groupby(word):
        end = start + sum(1 for _ in positions)
        yield axis, start, end
        start = end


def dense(axes, signs):
    coeff = {(): 1}
    for a, sign in zip(axes, signs, strict=True):
        for w, value in list(coeff.items()):
            key = w + (a,)
            coeff[key] = coeff.get(key, 0) + sign * value
    return {w: v for w, v in coeff.items() if v}


def poly_key(coeff, modulus):
    return tuple(sorted((w, residue(v, modulus)) for w, v in coeff.items()
                        if residue(v, modulus)))


def content(left, right):
    ans = 0
    for w in left.keys() | right.keys():
        ans = gcd(ans, left.get(w, 0)-right.get(w, 0))
        if ans == 1:
            return 1
    return ans


def low_bit(n):
    return n & -n


def suffixes(axes, signs, m):
    """Compute only suffix coordinates by scanning the actual signed path backward."""
    n = len(axes)
    values = [0] * n + [1]
    by_axis = {a: [] for a in set(axes)}
    for j, a in enumerate(axes):
        by_axis[a].append(j)
    for a, s in zip(reversed(axes), reversed(signs), strict=True):
        for j in by_axis[a]:
            values[j] = residue(values[j] + s*values[j+1], m)
    return values


def decode(axes, given, m):
    """Take the top word and its suffix data; return ascending coefficients per run."""
    n = len(axes)
    if len(given) != n+1 or given[-1] != 1:
        raise ValueError('invalid suffix table')
    values = given[:]
    start_run_length = [0] * n
    for a, start, end in runs(axes):
        for j in range(start, end):
            start_run_length[j] = end-j
    recovered = []
    for a, start, end in runs(axes):
        sign = values[end]    # the remaining word's leading coefficient is ±1
        if sign not in (1, residue(-1, m)):
            raise ValueError('incompatible leading unit')
        factor = [residue(values[end-t]*sign, m) for t in range(end-start+1)]
        recovered.append(factor)
        for j in range(n-1, end-1, -1):
            if axes[j] != a:
                continue
            cut = min(end-start, start_run_length[j])
            corrections = sum(factor[t]*values[j+t] for t in range(1, cut+1))
            values[j] = residue(values[j]-corrections, m)
    return recovered


def univariate(length, positives, m):
    row = [1]
    for j in range(length):
        sign = 1 if j < positives else -1
        nxt = row + [0]
        for i, value in enumerate(row):
            nxt[i+1] = residue(nxt[i+1] + sign*value, m)
        row = nxt
    return row


def root_multiplicity(factor, prime):
    a = [x % prime for x in factor]
    count = 0
    while len(a)>1:
        q = [0]*(len(a)-1)
        q[-1] = a[-1]
        for j in range(len(q)-2, -1, -1):
            q[j] = (a[j+1]-q[j+1]) % prime
        if (a[0]-q[0]) % prime:
            break
        count += 1
        a = q
    return count


def info(axes, signs):
    return [sum(s == 1 for s in signs[j:k]) for _, j, k in runs(axes)]


def endpoint(axes, signs, d):
    out = [0]*d
    for a,s in zip(axes, signs, strict=True):
        out[a] += s
    return tuple(out)


def effective_period(m):
    return m//2 if m and low_bit(m)==m else 0   # 0 represents integer information


def fixed_endpoint_fiber(axes, labels, disp, e):
    """Coefficient formula per named axis; e=0 fixes each run count exactly."""
    polys = [[1] for _ in disp]
    totals = [0]*len(disp)
    for (axis,start,end), val in zip(runs(axes), labels, strict=True):
        length = end-start
        totals[axis] += length
        allowed = range(val, length+1, e) if e else (val,)
        old = polys[axis]
        nxt = [0]*(len(old)+length)
        for t in allowed:
            ways = comb(length,t)
            for j,x in enumerate(old):
                nxt[j+t] += ways*x
        polys[axis] = nxt
    ways = 1
    for n,b,row in zip(totals,disp,polys,strict=True):
        if abs(b)>n or (n+b)%2:
            return 0
        ways *= row[(n+b)//2]
    return ways


def gf(d, e, nmax):
    values = []
    for n in range(nmax+1):
        x = int(n == 0) - int(e>0 and n==e)
        if n>=1: x += 2*d*values[n-1]
        if n>=2: x -= d*values[n-2]
        if e and n>=e: x -= (d-1)*values[n-e]
        values.append(x)
    return values


def check_factors(axes, positives, observed, modulus):
    found = decode(axes, observed, modulus)
    for (_,j,k),h,f in zip(runs(axes),positives,found,strict=True):
        assert f == univariate(k-j,h,modulus)
        if modulus in (3,5,7,11):
            assert root_multiplicity(f,modulus)==h
    return found


def simple_closed(d,n):
    # Number of raw signed nearest-neighbor walks from 0 to 0.
    ways = [1]+[0]*n
    for _ in range(d):
        prev = ways
        ways = [sum(comb(j,2*r)*comb(2*r,r)*prev[j-2*r] for r in range(j//2+1))
                for j in range(n+1)]
    return ways[n]


def odd_closed(d,n):
    return sum((-d)**j*comb(n-j,j)*simple_closed(d,n-2*j) for j in range(n//2+1))


def binary_closed(d,n):
    return sum(comb(d,j)*(d-2*j)**n for j in range(d+1))//2**d


def exhaustive(d,nmax):
    compared = checked_groups = suffix_vectors = 0
    content_hist = Counter()
    images = {m: [] for m in MODULI}
    closed_images = {m: [] for m in MODULI}
    for n in range(nmax+1):
        # Top words distinguish axis words, so their fiber counts add.
        size = Counter()
        closed = Counter()
        for axes in product(range(d),repeat=n):
            entries = []
            actual = {m: {} for m in MODULI}
            for signs in product((-1,1),repeat=n):
                exact = dense(axes,signs)
                pos = info(axes,signs)
                disp = endpoint(axes,signs,d)
                entries.append((exact,pos))
                for m in MODULI:
                    sparse = suffixes(axes,signs,m)
                    assert sparse == [residue(exact.get(axes[j:],0),m) for j in range(n+1)]
                    check_factors(axes,pos,sparse,m)
                    suffix_vectors += 1
                    key = poly_key(exact,m)
                    groups = actual[m].setdefault(key, {})
                    e = effective_period(m)
                    labels = tuple(t%e if e else t for t in pos)
                    if disp in groups:
                        last, c = groups[disp]
                        assert last==labels
                        groups[disp] = (last,c+1)
                    else:
                        groups[disp] = (labels,1)
            for (left,p),(right,q) in combinations(entries,2):
                delta = gcd(*(x-y for x,y in zip(p,q,strict=True)))
                g = content(left,right)
                assert g == 2*low_bit(delta)
                compared += 1
                content_hist[g] += 1
            for m,buckets in actual.items():
                size[m] += len(buckets)
                closed[m] += sum((0,)*d in groups for groups in buckets.values())
                for groups in buckets.values():
                    for disp,(labels,mass) in groups.items():
                        assert mass==fixed_endpoint_fiber(axes,labels,disp,effective_period(m))
                        checked_groups += 1
        for m in MODULI:
            closed_images[m].append(closed[m])
            images[m].append(size[m])
            assert images[m]==gf(d,effective_period(m),n)
    assert closed_images[0]==closed_images[3]==[odd_closed(d,n) for n in range(nmax+1)]
    assert closed_images[2]==[binary_closed(d,n) for n in range(nmax+1)]
    return dict(named_axes=d,closed_images=closed_images,max_length=nmax,pairs_same_top=compared,content_hist=dict(content_hist),
                suffix_vectors=suffix_vectors,actual_endpoint_fibers=checked_groups,distinct_images=images)


def native(repo):
    data = (repo/SOURCE).read_bytes()
    assert sha256(data).hexdigest()==SOURCE_HASH
    source = runpy.run_path(str(repo/SOURCE))
    paths = []
    for b in source['WORDS']:
        steps = source['cycle_steps'](b)
        axes = tuple(next(i for i,x in enumerate(s) if x) for s in steps)
        signs = tuple(sum(s) for s in steps)
        assert len(axes)==12 and endpoint(axes,signs,3)==(0,0,0)
        exact = dense(axes,signs)
        old = source['jet'](steps,3)
        for order,row in enumerate(old):
            assert list(row)==[exact.get(w,0) for w in product(range(3),repeat=order)]
        paths.append((axes,signs))
    tops = set()
    for (a,s),(b,t) in product(paths, repeat=2):
        axes,signs = a+b,s+t
        tops.add(axes)
        check_factors(axes,info(axes,signs),suffixes(axes,signs,6),6)
    assert len(tops)==4096
    return dict(source=SOURCE,sha256=SOURCE_HASH,source_order_three_coordinate_checks=64*(1+3+9+27),
                complete_one_cycle_paths=len(paths),distinct_native_two_cycle_top_words=len(tops),
                exact_mod_six_suffix_decodings=len(tops))


def rectangle(h, sign):
    return (0,)*h+(1,)+(0,)*h+(1,), (sign,)*h+(1,)+(-sign,)*h+(-1,)


def closed_by_positive_halves(half):
    """Canonical words forbid (+i,-i). Pair prefixes by the reversal-and-negation symmetry."""
    zero = (0,0,0)
    # Slots retain total and counts ending in each positive named axis.
    states = {zero:[1,0,0,0]}
    for _ in range(half):
        nxt = {}
        for (x,y,z),(total,px,py,pz) in states.items():
            for key,i,count in (((x+1,y,z),1,total),((x,y+1,z),2,total),
                                ((x,y,z+1),3,total),((x-1,y,z),0,total-px),
                                ((x,y-1,z),0,total-py),((x,y,z-1),0,total-pz)):
                sums = nxt.get(key)
                if sums is None:
                    sums = nxt[key] = [0,0,0,0]
                sums[0] += count
                if i:
                    sums[i] += count
        states = nxt
    return sum(t*t-a*a-b*b-c*c for t,a,b,c in states.values()),len(states)


def large_examples():
    rows = []
    for h in (1,2,3,4,5,8,12):
        a,s = rectangle(h,1)
        _,t = rectangle(h,-1)
        p,q = dense(a,s),dense(a,t)
        g = content(p,q)
        assert g==2*low_bit(h) and (p.get((0,1),0),q.get((0,1),0))==(h,-h)
        rows.append([h,g,h,-h])
    large = []
    for h in (27,64,81,128):
        a,s = rectangle(h,1)
        _,t = rectangle(h,-1)
        for m in (2*low_bit(h),4*low_bit(h),3,5):
            x,y = suffixes(a,s,m),suffixes(a,t,m)
            check_factors(a,info(a,s),x,m)
            check_factors(a,info(a,t),y,m)
            assert (x==y)==(2*low_bit(h)%m==0)
            large.append([h,len(a),m,x==y])
    positive,half_positions = closed_by_positive_halves(50)
    assert positive==odd_closed(3,100)
    return dict(dense_rectangle_h_content_XY_values=rows,large_suffix_tests=large,
                independent_nonnegative_half_walk_count={'half_length':50,
                    'reachable_endpoints':half_positions,'closed_pairs':str(positive)},
                exact_closed_at_grade_100={'integer_or_odd_factor': str(odd_closed(3,100)),
                                           'mod_two': str(binary_closed(3,100))},
                full_images_at_grade_100={m:str(gf(3,effective_period(m),100)[-1]) for m in MODULI})


def main(repo):
    small=[exhaustive(2,5),exhaustive(3,4)]
    assert sum(x['pairs_same_top'] for x in small)==28575
    return {'registration':'RS-EM7D3C9A-1255-GLOBAL-JET-COMPOSITION',
            'native':native(repo),'small_exact':small,'larger_arithmetic':large_examples()}


if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo',type=Path,default=Path.cwd())
    print(json.dumps(main(ap.parse_args().repo),sort_keys=True,indent=2))
