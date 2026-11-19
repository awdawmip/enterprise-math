"""Rebuild the 64 graph classes on (C/Z[i])^6 directly from their real equations."""
from collections import Counter
from fractions import Fraction
from itertools import product, combinations_with_replacement
from math import comb, prod
import json

SLOPES = ((1, 0), (0, 1), (-1, 0), (0, -1))
TYPES = list(product(range(2), repeat=3))
IDS = list(product(range(4), repeat=3))


def trim(f):
    return {m: c for m, c in f.items() if c}


def plus(terms):
    out = Counter()
    for scale, f in terms:
        for m, c in f.items():
            out[m] += scale*c
    return trim(out)


def wedge(a, b):
    result = Counter()
    for u, v in a.items():
        for w, c in b.items():
            if u & w:
                continue
            inversions = sum((u >> (i + 1)).bit_count()
                             for i in range(w.bit_length()) if w >> i & 1)
            result[u | w] += (-1)**inversions*v*c
    return trim(result)


def wedge3(f):
    return wedge(wedge(f[0], f[1]), f[2])


def sum_class(weights, graphs):
    return plus((z, graphs[t]) for t, z in weights.items())


def factors():
    local_graphs, qxy = [], []
    for j in range(3):
        x, y, u, v = [{1 << (4*j+i): 1} for i in range(4)]
        local = []
        for re, im in SLOPES:
            # d(Re(w-a*z)), d(Im(w-a*z)); complex orientation on the normal.
            first = plus(((1, u), (-re, x), (im, y)))
            second = plus(((1, v), (-im, x), (-re, y)))
            local.append(wedge(first, second))
        q = plus(((1, wedge(x, y)), (1, wedge(u, v))))
        X = plus(((1, wedge(y, u)), (-1, wedge(x, v))))
        Y = plus(((1, wedge(x, u)), (1, wedge(y, v))))
        assert [plus(((1, q), (re, X), (im, Y))) for re, im in SLOPES] == local
        local_graphs.append(local)
        qxy.append([q, X, Y])
    return local_graphs, qxy


def witness(real, imag):
    assert (real + imag) % 4 == (real - imag) % 4 == 0
    def elementary(mixed):
        rows = {}
        choices = (0, 0, 1, 0, 3, 0, 1, 3)
        for i, t in enumerate(TYPES):
            k = sum(t)
            if not mixed and k % 2:
                continue
            signs = list(product((1, -1), repeat=3))
            if mixed:
                c = choices[i]
                s = (1, 1 if c < 2 else -1, 1 if c % 2 == 0 else -1)
                signs = [s, tuple(-v for v in s)]
            else:
                eta = -1 if t == (1, 1, 0) else 1
                signs = [s for s in signs if s[1]*s[2] == eta]
            for s in signs:
                key = tuple(tj + 2*(sj < 0) for tj, sj in zip(t,s))
                rows[key] = (1 if k < 2 else -1) * prod(s)
        return rows

    out = Counter()
    if real % 4:
        sign = 1 if real > 0 else -1
        conjugate = (real * imag < 0)
        for t, multiplicity in elementary(True).items():
            key = tuple((-j % 4 if conjugate else j) for j in t)
            out[key] += sign*multiplicity
        real -= 2 * sign
        imag -= 2 * (1 if imag > 0 else -1)
    for t, multiplicity in elementary(False).items():
        out[t] += real // 4 * multiplicity
        rotate = ((t[0]+1) % 4, t[1], t[2])
        out[rotate] += imag // 4 * multiplicity
    return trim(out)


def ext_table(w):
    pos = {t: v for t, v in w.items() if v > 0}
    neg = {t:-v for t, v in w.items() if v < 0}
    dims = [0] * 7
    for t, k in pos.items():
        for s, m in neg.items():
            dif = [(0, 2, 4, 2)[(x-y)%4] for x,y in zip(t,s) if x != y]
            h = len(dif)
            for j in range(2*(3-h)+1):
                dims[h+j] += k*m*prod(dif)*comb(2*(3-h),j)
    return dims


def classify_real_optima(graphs, U):
    # In an optimal real presentation only the 4 even types occur and all
    # weights within a type have prescribed sign after multiplication by prod(s).
    signs = list(product((1,-1), repeat=3))
    types = [t for t in TYPES if sum(t)%2 == 0]
    local = []
    for v in combinations_with_replacement(range(8),4):
        if any(sum(signs[k][i] for k in v) for i in range(3)):
            continue
        const = sum(prod(signs[k]) for k in v)
        first = [sum(prod(signs[k])*signs[k][i] for k in v) for i in range(3)]
        local.append((v,const,first))
    signature = [(-1)**(sum(t)//2) for t in types]
    census = Counter()
    examples = {}
    for rows in product(local,repeat=4):
        if sum(e*r[1] for e,r in zip(signature,rows)):
            continue
        if any(sum(e*r[2][i] for t,e,r in zip(types,signature,rows) if t[i]==b)
               for i,b in product(range(3),range(2))):
            continue
        w = Counter()
        for t,e,r in zip(types,signature,rows):
            for k in r[0]:
                s = signs[k]
                w[tuple(m+2*(sj<0) for m,sj in zip(t,s))] += e*prod(s)
        assert sum(map(abs,w.values())) == 16 and sum_class(w,graphs) == plus([(4,U)])
        h = ext_table(w)
        key = (len(w),h[1],h[2])
        census[key] += 1
        examples.setdefault(key, sorted([[list(t),n] for t,n in w.items()]))
    assert len(local) == 12 and sum(census.values()) == 58
    return dict(balanced_local_multisets=len(local), full_product=len(local)**4,
        distributions=[dict(distinct_labels=k[0],ext1=k[1],ext2=k[2],count=n,
                            witness=examples[k]) for k,n in sorted(census.items())])


def tensor_witness(g,a,b):
    w = Counter()
    if g == 1:
        if a%2:
            c = 1 if a>0 else -1
            d = 1 if b>0 else -1
            w[(0 if c>0 else 2,)] += 1
            w[(3 if d>0 else 1,)] -= 1
            a -= c
            b -= d
        w[(0,)] += a//2
        w[(2,)] -= a//2
        w[(1,)] += b//2
        w[(3,)] -= b//2
        return trim(w)
    base = {(0,0):1, (2,2):1, (1,1):-1, (3,3):-1}
    imag = {((k+1)%4,l):v for (k,l),v in base.items()}
    if g == 2:
        for f, c in ((base,a//2),(imag,b//2)):
            for t,v in f.items():
                w[t] += c*v
    else:
        assert a%2==b%2==0
        for ab, f in (((a//2,b//2),base),((b//2,-a//2),imag)):
            for t,c in tensor_witness(g-2,*ab).items():
                for h,v in f.items():
                    w[t+h] += c*v
    return trim(w)


def check_tensor():
    total = 0
    for g in range(1,7):
        # Multiply the integer input coefficients by (1+i)^g.
        for c,d in ((1,0),(0,-1),(2,1),(-1,2)):
            a,b = c,d
            for _ in range(g):
                a,b = a-b,a+b
            w = tensor_witness(g,a,b)
            assert sum(map(abs,w.values())) == 2**(g-1)*(abs(a)+abs(b))
            expanded = Counter()
            for phase,v in w.items():
                for use in product(range(2),repeat=g):
                    key = tuple((1+ph%2 if on else 0) for ph,on in zip(phase,use))
                    sgn = (-1)**sum(ph>=2 and on for ph,on in zip(phase,use))
                    expanded[key] += sgn*v
            for key in product(range(3),repeat=g):
                num_y = key.count(2)
                expected = 0 if 0 in key else (-1)**(num_y//2)*(b if num_y%2 else a)
                assert expanded[key] == expected
            total += 1
    return dict(max_slots=6, number_of_witnesses=total)


def rank(rows):
    pivots = {}
    for row in rows:
        r = list(map(Fraction,row))
        for j, v in sorted(pivots.items()):
            if r[j]:
                c = r[j]
                r = [x-c*y for x,y in zip(r,v)]
        j = next((i for i,x in enumerate(r) if x),None)
        if j is not None:
            pivots[j] = [x/r[j] for x in r]
    return len(pivots)


def normal_rows(a):
    for k, l in product(range(3), repeat=2):
        re, im = SLOPES[(a[k]-a[l]) % 4]
        weight = (1,1,3)[k]
        left, right = 3*l+k, 3*k+l
        rr, ii = [0]*18, [0]*18
        rr[left] += 1
        ii[left+9] += 1
        rr[right] -= weight*re
        rr[right+9] += weight*im
        ii[right] -= weight*im
        ii[right+9] -= weight*re
        yield rr
        yield ii


def main():
    local, qxy = factors()
    graphs = {t:wedge3([local[i][k] for i,k in enumerate(t)]) for t in IDS}
    basis = {p:wedge3([qxy[i][k] for i,k in enumerate(p)])
             for p in product(range(3),repeat=3)}
    assert len(basis) == 27 and len(set().union(*basis.values())) == sum(map(len,basis.values()))
    units = []
    for parity in (0,1):
        units.append(plus(((-1)**(sum(t)//2), basis[tuple(1+j for j in t)])
                          for t in TYPES if sum(t)%2==parity))
    U,V = units
    assert len(U) == len(V) == 32 and not (U.keys() & V.keys())
    assert set(map(abs,U.values())) == set(map(abs,V.values())) == {1}
    pair = lambda f,g: wedge(f,g).get(4095,0)
    assert [pair(U,U), pair(U,V), pair(V,V)] == [-32,0,-32]
    # All 4096 geometric intersections by the Gaussian degrees, independent of exterior masks.
    for s,t in product(IDS, repeat=2):
        assert pair(graphs[s],graphs[t]) == prod((0,2,4,2)[(i-j)%4] for i,j in zip(s,t))
    original = {t:(1 if sum(t)%4==0 else -1) for t in IDS if sum(t)%2==0}
    assert sum_class(original,graphs) == plus([(8,U)])
    assert ext_table(original) == [0,192,1152,4480,1152,192,0]

    # Matrix of the 64 true graph columns in the tensor basis of the image lattice.
    local_basis = ((1,0,0),(1,0,-1),(1,-1,-1),(1,-1,0))
    coordinates = [[prod(local_basis[k][j] for k,j in zip(t,p)) for t in IDS]
                   for p in product(range(3),repeat=3)]
    assert rank(coordinates) == 27
    # Each integral basis vector is realizable by graph differences.
    assert plus([(1,local[0][0]),(-1,local[0][3])]) == plus([(1,qxy[0][1]),(1,qxy[0][2])])
    assert plus([(1,local[0][0]),(-1,local[0][1])]) == plus([(1,qxy[0][1]),(-1,qxy[0][2])])

    examples = {}
    for a,b in ((4,0),(0,4),(2,2),(2,-2),(8,0),(6,10)):
        ws = witness(a,b)
        assert sum_class(ws,graphs) == plus([(a,U),(b,V)])
        assert sum(map(abs,ws.values())) == 4*(abs(a)+abs(b)) and sum(ws.values())==0
        assert rank(row for t in ws for row in normal_rows(t)) == 14
        phases = sorted({(t[0]-t[1])%4 for t in ws})
        examples[f"{a},{b}"] = dict(weight=sum(map(abs,ws.values())),phase_ratios=phases,
            signed_graphs=sorted([[list(t),n] for t,n in ws.items()]),
            positive_to_negative_ext=ext_table(ws), self_intersection=-32*(a*a+b*b),
            real_normal_rank=14)
    many = 0
    for a,b in product(range(-20,21),repeat=2):
        if (a+b)%4 or (a-b)%4:
            continue
        ws = witness(a,b)
        assert sum_class(ws,graphs) == plus([(a,U),(b,V)])
        assert sum(map(abs,ws.values())) == 4*(abs(a)+abs(b))
        many += 1
    # Representative of each of the four phase ratios; all are tested individually.
    nr = {t:list(normal_rows(t)) for t in IDS}
    assert all(rank(v)==12 for v in nr.values())
    reps = [(j,0,0) for j in range(4)]
    parity_rank = [[rank(nr[i]+nr[j]) for j in reps] for i in reps]
    assert parity_rank == [[12 if i==j else 14 for j in range(4)] for i in range(4)]
    print(json.dumps(dict(source_model="E=C/Z[i], w_j=i^k_j z_j, D=diag(1,1,3)",
        exact_graph_intersections=4096, independent_exterior_graph_classes=27,
        nonzero_exterior_entries_U_V=[len(U),len(V)], Weil_ambient_Gram=[[-32,0],[0,-32]],
        pure_graph_lattice_in_U_V=[[2,2],[2,-2]], quotient_Smith=[2,4],
        lattice_index=8, integral_graph_Gram=[[-256,0],[0,-256]],
        archived_32_graph_ext=ext_table(original), archived_square=pair(sum_class(original,graphs),sum_class(original,graphs)),
        signed_primal_tests_in_box=many, box=[-20,20], examples=examples,
        real_normal_rank_by_phase_comparison=parity_rank,
        all_minimum_cost_representations_of_16w=classify_real_optima(graphs,U),
        tensor_cost_checks=check_tensor()),indent=2,sort_keys=True))


if __name__=="__main__":
    main()
