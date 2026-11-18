"""Integer completions of binary Bell tables. Uses only the Python standard library."""
from collections import Counter
from functools import lru_cache
from fractions import Fraction
from itertools import combinations_with_replacement, product
from math import comb, gcd
import json


def possible_columns(q, a):
    # (Bob ones, Alice0 & Bob ones, Alice1 & Bob ones)
    out = []
    for b in range(q+1):
        ranges = [range(max(0, m+b-q), min(b, m)+1) for m in a]
        out += [(b, u, v) for u,v in product(*ranges)]
    return out


def strata(q, a, col):
    b, u, v = col
    return [(q-b, a[0]-u, a[1]-v), (b, u, v)]


def limits(q, a, col):
    rows = strata(q, a, col)
    return sum(max(0,u+v-n) for n,u,v in rows), sum(min(u,v) for _,u,v in rows)


def target(q, a, cols):
    bounds = [limits(q,a,c) for c in cols]
    highest_low, lowest_high = max(lo for lo,_ in bounds), min(hi for _,hi in bounds)
    diagonal = [max(lo, min(highest_low,hi)) for lo,hi in bounds]
    return 2*max(0, highest_low-lowest_high), diagonal


def excess_count(q, a, cols):
    # Correlation times q is q-2 times the number of unequal outcomes.
    pairs = [(q-2*(a[0]+b-2*u), q-2*(a[1]+b-2*v)) for b,u,v in cols]
    return max(0, max(abs(x-y) for x,y in pairs)+max(abs(x+y) for x,y in pairs)-2*q)


def construct(q, a, cols):
    bad, diagonal = target(q,a,cols)
    states = list(product((0,1), repeat=2))
    inventories = []
    for col,t in zip(cols,diagonal):
        strata_rows = strata(q,a,col)
        minima = [max(0,u+v-n) for n,u,v in strata_rows]
        extra = t-sum(minima)
        groups = {s:[] for s in states}
        for bit, ((n,u,v),lo) in enumerate(zip(strata_rows,minima)):
            take = min(extra,min(u,v)-lo)
            k = lo+take
            extra -= take
            for s,mass in zip(states,(n-u-v+k,v-k,u-k,k)):
                groups[s].extend([(*s,bit)]*mass)
        assert extra == 0
        inventories.append(groups)
    common = {s:min(len(g[s]) for g in inventories) for s in states}
    columns = []
    for g in inventories:
        prefix = [z for s in states for z in g[s][:common[s]]]
        suffix = [z for s in states for z in g[s][common[s]:]]
        columns.append(prefix+suffix)
    assert all(len(j)==q for j in columns)
    assert sum(len({cell[:2] for cell in row})>1 for row in zip(*columns)) == bad
    for j,col in zip(columns, cols):
        b,u,v = col
        observed = tuple(sum(z[i] for z in j) for i in (0,1,2))
        assert observed == (*a,b)
        assert (sum(x*w for x,y,w in j),sum(y*w for x,y,w in j)) == (u,v)
    return bad, columns


@lru_cache(None)
def local_shapes(q, m):
    # Independent enumeration of multisets of deterministic hidden atoms.
    atoms = list(product((0,1),repeat=2+m))
    shapes = set()
    for rows in combinations_with_replacement(atoms, q):
        a = tuple(sum(r[i] for r in rows) for i in (0,1))
        cols = tuple((sum(r[j] for r in rows),sum(r[0]*r[j] for r in rows),
                      sum(r[1]*r[j] for r in rows)) for j in range(2,m+2))
        shapes.add((a,cols))
    return shapes


def table_cells(q, a, cols):
    tabs = []
    for b,u,v in cols:
        for m,n in zip(a,(u,v)):
            tabs.extend((q-m-b+n,b-n,m-n,n))
    return tabs


@lru_cache(None)
def local_subtables(q, m):
    return [table_cells(q,a,cols) for a,cols in local_shapes(q,m)]


def enumerate_tables(q, m, test_submass):
    stats = Counter()
    locals_ = local_shapes(q,m)
    for a in product(range(q+1), repeat=2):
        for cols in product(possible_columns(q,a), repeat=m):
            bad, _ = construct(q,a,cols)
            assert (bad==0) == ((a,cols) in locals_)
            assert excess_count(q,a,cols) == 2*bad
            if test_submass and bad:
                cells = table_cells(q,a,cols)
                best = next(k for k in range(q-1,-1,-1)
                            if any(all(x<=y for x,y in zip(candidate,cells))
                                   for candidate in local_subtables(k,m)))
                assert best == q-bad
            stats[bad] += 1
    return {'q':q,'bob_settings':m,'nonlocal_row_histogram':dict(sorted(stats.items())),
            'distinct_local_tables':len(locals_),'direct_subtable_comparison':test_submass}


def pell(initial, sign, count):
    x,y = initial
    rows = []
    for _ in range(count):
        assert x*x-2*y*y == sign
        h,u = (x,y) if sign==-1 else (2*x,2*y)
        q = 2*h
        cells = [(h+u)//2,(h-u)//2]
        assert (h-u)%2==0 and gcd(q,gcd(*cells))==1
        rows.append({'q':q,'h':h,'u':u,'cell_counts':cells,'norm':h*h-2*u*u,
                     'minimum_bad_rows':max(0,4*u-2*h)})
        x,y = 3*x+4*y, 2*x+3*y
    return rows


def verify_pr(q, a, cols):
    bad, arrangements = construct(q,a,cols)
    if not bad:
        return
    for j in arrangements:
        tail = j[q-bad:]
        for i in (0,1):
            c = Counter((z[i],z[2]) for z in tail)
            assert len(c)==2 and set(c.values())=={bad//2}
            assert len({a^b for a,b in c})==1
    parities = [j[-1][i]^j[-1][2] for j in arrangements for i in (0,1)]
    assert sum(parities)%2==1


def census(q):
    # With margins fixed, one cell determines the remaining three.
    def range_size(a,b):
        return 1+min(a,b,q-a,q-b)
    ns = sum(sum(range_size(a,b)*range_size(c,b) for b in range(q+1))**2
             for a,c in product(range(q+1), repeat=2))
    nonlocal_spectrum = {2*g:8*comb(q-2*g+7,7) for g in range(1,q//2+1)}
    return {0:ns-sum(nonlocal_spectrum.values()), **nonlocal_spectrum}


def ehrhart():
    values = [census(q)[0] for q in range(22)]
    numerator = [sum((-1)**i*comb(9,i)*values[k-i] for i in range(min(k,9)+1))
                 for k in range(len(values))]
    assert numerator == [1,7,20,28,7,1] + [0]*(len(values)-6)
    return {'local_values_to_21':values, 'local_h_star':numerator[:6],
            'limiting_local_fraction':'16/17',
            'conditional_nonlocal_defect_tail':'(1-x)^8 for 0<x<1'}


def facet_decompose(q,a,cols):
    # Extract all 8 single-loss local atom multiplicities from the losing cells.
    cells = table_cells(q,a,cols)
    atoms = list(product((0,1),repeat=4))
    for pattern in product((0,1),repeat=4):
        if sum(pattern)%2==0:
            continue
        def loss_index(p,i,j):
            return 4*(2*j+i)+2*p[i]+p[2+j]
        lost = [(i,j,s,t) for j,i,s,t in product((0,1),repeat=4)
                if s^t != pattern[2*j+i]]
        total = sum(cells[4*(2*j+i)+2*s+t] for i,j,s,t in lost)
        if total>=q:
            continue
        assert (q-total)%2 == 0
        g = (q-total)//2
        observed = [0]*len(cells)
        for p in atoms:
            fails = [(i,j) for j,i in product((0,1),repeat=2)
                     if p[i]^p[2+j] != pattern[2*j+i]]
            if len(fails)==1:
                mass = cells[loss_index(p,*fails[0])]
                for j,i in product((0,1),repeat=2):
                    observed[loss_index(p,i,j)] += mass
        for j,i,s,t in product((0,1),repeat=4):
            if s^t == pattern[2*j+i]:
                observed[4*(2*j+i)+2*s+t] += g
        assert cells == observed
        return g
    return 0

def run():
    experiments = []
    for q,m in [(1,2),(2,2),(3,2),(4,2),(5,2),(2,3),(3,3)]:
        experiments.append(enumerate_tables(q,m,q<=3))
        if m==2:
            for a in product(range(q+1), repeat=2):
                for cols in product(possible_columns(q,a), repeat=2):
                    verify_pr(q,a,cols)
                    assert 2*facet_decompose(q,a,cols)==target(q,a,cols)[0]
            assert experiments[-1]['nonlocal_row_histogram']==census(q)
    example = [(3,2,3),(3,3,0),(3,2,1)]
    bad, sample = construct(6,(3,3),example)
    ideal = Fraction(sum(comb(245,w)*3**w for w in range(196,246)), 4**245)
    return {'ehrhart':ehrhart(),'table_enumeration':experiments, 'three_setting_example':{'q':6,'alice_ones':[3,3],
            'cols':example,'bad':bad,'context_arrangements':sample},
            'isotropic_pell_above':pell((1,1),-1,6),'isotropic_pell_below':pell((3,2),1,6),
            'ideal_uniform_null_tail_196_of_245':{'numerator':ideal.numerator,
            'denominator':ideal.denominator,'rounded':round(float(ideal),12)}}


if __name__=='__main__':
    print(json.dumps(run(),indent=2))
