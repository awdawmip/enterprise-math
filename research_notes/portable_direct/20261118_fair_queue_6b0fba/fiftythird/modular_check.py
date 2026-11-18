"""Exact finite signed-observer check. Requires the public positive BRC source."""
import argparse
from bisect import bisect_right
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import sys

CORE_SHA = "7520822074b8f29e1c54f57b9543c043202db8bd7c6e27f3f1d6176028ac4a26"
ZERO = (0, 0)
ONE = (1, 0)


def orbit(n, a):
    x, labels, seen = 1, [], set()
    while x not in seen:
        seen.add(x)
        labels.append(x)
        x = a*x % n
    assert x == 1
    return labels


def gates(d, extra):
    seq = [('W', d, None)]
    for j in range(d):
        seq += [('W', j, None), ('S', j, 2**j), ('W', j, d)]
    if extra:
        seq += [('W', d, None), ('S', d, 1), ('W', d, 0)]
    return seq


class PositivePairs:
    def __init__(self, power):
        self.power = power
        self.requests = 0
        self.max_positive_bits = 0

    @lru_cache(maxsize=None)
    def compiled(self, lo, hi, dual):
        # Row = source and column = destination, with plus/minus parity doubled.
        # State 4 injects both masses at depth one. Read the four endpoints at depth two.
        t = ((1, 3), (-1, 1))
        if dual:
            t = tuple(zip(*t))
        mass = [[0]*5 for _ in range(5)]
        mass[4][:4] = list(lo+hi)
        for out in range(2):
            for old in range(2):
                v = t[out][old]
                for parity in range(2):
                    mass[2*old+parity][2*out+(parity ^ int(v<0))] = abs(v)
        result = self.power(mass, 2)
        row = result[4][:4]
        assert all(v.denominator == 1 for v in row)
        values = [int(v) for v in row]
        self.max_positive_bits = max(self.max_positive_bits, max(x.bit_length() for x in values))
        return tuple(values[:2]), tuple(values[2:])

    def pair(self, low, high, dual):
        if low == high == ZERO:
            return ZERO, ZERO
        self.requests += 1
        return self.compiled(low, high, dual)


def rails_evolve(d, labels, n, a, schedule, start, dual, kernel):
    # Uses actual residues and actual modular products. No order enters this route.
    C, R = 2**(d+1), len(labels)
    ix = {v:j for j,v in enumerate(labels)}
    masses = [[ZERO for _ in labels] for _ in range(C)]
    masses[start[0]][ix[start[1]]] = ONE
    for kind, bit, par in (reversed(schedule) if dual else schedule):
        if kind == 'S':
            factor = pow(a, par, n)
            if dual:
                factor = pow(factor, -1, n)
            for c, row in enumerate(masses):
                if c & (1<<bit):
                    new = [None]*R
                    for j,x in enumerate(labels):
                        new[ix[(factor*x) % n]] = row[j]
                    assert None not in new
                    masses[c] = new
        else:
            for c in range(C):
                if c & (1<<bit):
                    continue
                other = c | (1<<bit)
                if par is not None and not (c & (1<<par)):
                    for row in (masses[c],masses[other]):
                        for i,(p,m) in enumerate(row):
                            row[i] = 2*p, 2*m
                    continue
                for e in range(R):
                    masses[c][e],masses[other][e] = kernel.pair(
                        masses[c][e], masses[other][e], dual)
    return masses


def polynomial_rows(d, r):
    M = 1<<d
    rows = [[0]*r for _ in range(2*M)]
    for y in range(M):
        rows[y][y%r] = (-1)**y.bit_count() * M
        for b in range(M):
            rows[M+y][b%r] += -((-1)**y.bit_count()) * (-3)**((b & ~y).bit_count())
    return rows


def ranks(grid):
    matrix = [list(map(Fraction, row)) for row in grid]
    k = 0
    for j in range(len(matrix[0])):
        pivot = next((i for i in range(k,len(matrix)) if matrix[i][j]), None)
        if pivot is None:
            continue
        matrix[k],matrix[pivot] = matrix[pivot],matrix[k]
        for i in range(k+1,len(matrix)):
            coeff = matrix[i][j]/matrix[k][j]
            if coeff:
                matrix[i] = [a-coeff*b for a,b in zip(matrix[i],matrix[k])]
        k += 1
    return k


def field_modes(d, r, q, seq):
    # Finite-field character evaluation is only an exact check modulo q.
    # The program scans for a root of exact order r; each local gate transfers directly.
    root = next(v for v in range(1,q) if pow(v,r,q) == 1 and
                all(pow(v,k,q) != 1 for k in range(1,r)))
    C = 2**(d+1)
    sectors = []
    for j in range(r):
        arr = [1]+[0]*(C-1)
        for kind,bit,par in seq:
            if kind == 'S':
                for c in range(C):
                    if c & (1<<bit):
                        arr[c] = arr[c]*pow(root,j*par,q)%q
            else:
                for c in range(C):
                    if c & (1<<bit):
                        continue
                    b = c | (1<<bit)
                    if par is None or c & (1<<par):
                        x,y = arr[c],arr[b]
                        arr[c],arr[b] = (x+3*y)%q, (-x+y)%q
                    else:
                        arr[c],arr[b] = 2*arr[c]%q, 2*arr[b]%q
        sectors.append(arr)
    return [[(sum(sectors[j][y]*pow(root,-j*e,q) for j in range(r))*pow(r,-1,q))%q
             for e in range(r)] for y in range(C)]


def physical_paths(d, labels, n, a, seq):
    # Every elementary trajectory is kept; each active flip contributes one sqrt(3).
    C = 2**(d+1)
    paths = [(0,1,0,1)]
    for kind,bit,par in seq:
        new = []
        for c,x,flips,coef in paths:
            active = bool(c & (1<<bit))
            if kind == 'S':
                new.append((c,x*pow(a,par,n)%n if active else x,flips,coef))
            elif par is None or c & (1<<par):
                new.append((c,x,flips,coef))
                new.append((c^(1<<bit),x,flips+1,coef if active else -coef))
            else:
                new.append((c,x,flips,2*coef))
        paths = new
    rows = [[0]*len(labels) for _ in range(C)]
    for c,x,h,v in paths:
        diff = h-c.bit_count()
        assert diff>=0 and diff%2 == 0
        rows[c][labels.index(x)] += v*3**(diff//2)
    return rows, len(paths)


def check_case(d,n,a,extra,kernel):
    labels = orbit(n,a)
    r = len(labels)
    C = 2**(d+1)
    seq = gates(d,extra)
    g = sum(kind == 'W' for kind,_,_ in seq)
    Rfull = 2**(n-1).bit_length()
    assert all(len(set((pow(a,par,n)*x % n if x<n else x) for x in range(Rfull)))==Rfull
               for kind,bit,par in seq if kind=='S')
    start_count = kernel.requests
    rails = rails_evolve(d,labels,n,a,seq,(0,1),False,kernel)
    forward_requests = kernel.requests - start_count
    integer = [[p-m for p,m in row] for row in rails]
    paths,count = physical_paths(d,labels,n,a,seq)
    assert integer == paths
    if not extra:
        assert integer == polynomial_rows(d,r)
    reduced = field_modes(d,r,1009,seq)
    assert reduced == [[x%1009 for x in row] for row in integer]
    num = [[3**y.bit_count()*x*x for x in row] for y,row in enumerate(integer)]
    D = 4**g
    assert sum(map(sum,num)) == D
    reverse_count = kernel.requests
    costs = []
    for y in range(C):
        for e,x in enumerate(labels):
            before = kernel.requests
            rev = rails_evolve(d,labels,n,a,seq,(y,x),True,kernel)
            assert rev[0][0] == rails[y][e]
            costs.append(kernel.requests-before)
    reverse_requests = kernel.requests - reverse_count
    # Replay all 4^g uniform tickets through the same joint inverse CDF.
    cuts = [0]
    for row in num:
        for v in row:
            cuts.append(cuts[-1]+v)
    assert cuts[-1] == D
    ticket_counts = [0]*(C*r)
    for ticket in range(D):
        ticket_counts[bisect_right(cuts,ticket)-1] += 1
    assert ticket_counts == [v for row in num for v in row]
    amp_rank, prob_rank = ranks(integer), ranks(num)
    assert amp_rank == min(r,(1<<d)+int(extra))
    if not extra:
        assert prob_rank == min(r,1<<d)
    # The columns of the entire transfer at work input 1 determine it by cyclic covariance.
    cost_start = kernel.requests
    columns = []
    for c in range(C):
        col = rails_evolve(d,labels,n,a,seq,(c,1),False,kernel)
        columns.append([[p-m for p,m in row] for row in col])
    g_rank_cost = kernel.requests-cost_start
    factors = [[(-1)**((u% (1<<d)).bit_count())*3**u.bit_count()*x
                for u in range(C) for x in columns[c][u]] for c in range(C)]
    grade_matrices = []
    for t in range(r):
        gram = [sum(factors[c][u*r+e]*columns[b][u][(e+t)%r]
                    for u in range(C) for e in range(r)) for c in range(C) for b in range(C)]
        grade_matrices.append(gram)
    parity_rank = ranks(grade_matrices)
    effect_ranks = []
    for y in range(C):
        vector_rank = ranks([[columns[c][y][e] for e in range(r)] for c in range(C)])
        effect_ranks.append(vector_rank**2)
        if not extra:
            assert vector_rank == (1 if y<1<<d else min(r,1<<d))
    active = sum(v!=0 for row in num for v in row)
    zero_from_cancellation = sum(p==m and p>0 for row in rails for p,m in row)
    known_parity_rank = len({(b-c)%r for b in range(1<<d) for c in range(1<<d)})
    assert known_parity_rank == min(r,2**(d+1)-1)
    if not extra:
        assert parity_rank == known_parity_rank
    out = dict(d=d,N=n,a=a,work_labels=labels,control_bits=d+1,raw_bits=d+1+(n-1).bit_length(),
               orbit_bits=d+1+(r-1).bit_length(),suffix=extra,algebraic_W_layers=g,
               shifts=len(seq)-g,full_address_count=C*Rfull,reachable_orbit_cells=C*r,
               support=active,cancelled_endpoints=zero_from_cancellation,work_cut_amplitude_rank=amp_rank,
               work_cut_probability_rank=prob_rank,observable_parity_rank_before_suffix=known_parity_rank,
               actual_backwards_parity_rank=parity_rank, actual_single_cell_effect_ranks_by_control=effect_ranks,
               common_probability_denominator=D,largest_abs_integer_coefficient_bits=max(abs(x).bit_length()
                   for row in integer for x in row),max_probability_numerator_bits=max(v.bit_length() for row in num for v in row),
               full_forward_BRC_pair_requests=forward_requests,all_reverse_BRC_pair_requests=reverse_requests,
               reverse_queries=C*r,one_reverse_pair_requests_minmax=[min(costs),max(costs)],
               additional_BRC_pair_requests_for_full_cut_ranks=g_rank_cost,one_physical_path_enumeration_leaves=count,
               weighted_joint_rows_integer=num)
    if d==2 and n==7 and a==2 and extra:
        out['positive_mass_pairs'] = rails
    return out


def work_readable_3bits(kernel):
    # Raw representation of residues 0,1,2 plus padding 3; multiplication by 2 fixes padding.
    perm = [0,2,1,3]
    outputs = []
    for work0 in (1,2):
        data = [[ZERO]*4 for _ in range(2)]
        data[0][work0] = ONE
        for w in range(4):
            data[0][w],data[1][w] = kernel.pair(data[0][w],data[1][w],False)
        data[1] = [data[1][perm[w]] for w in range(4)]
        for w in range(4):
            if w%2:
                data[0][w],data[1][w] = kernel.pair(data[0][w],data[1][w],False)
            else:
                for row in data:
                    row[w] = tuple(2*x for x in row[w])
        weights = [[3**c*(p-m)**2 for p,m in row] for c,row in enumerate(data)]
        assert sum(map(sum,weights)) == 16
        outputs.append(weights)
    assert outputs == [[[0,1,0,0],[0,3,12,0]], [[0,9,4,0],[0,3,0,0]]]
    return dict(controlled_by_work_low_bit=True, initial_work=[1,2],rows=outputs,denominator=16)


def first_base_cancellation(kernel):
    checked=0
    for d in range(1,6):
        M = 1<<d
        for r in range(1,M):
            for y,row in enumerate(polynomial_rows(d,r)[M:]):
                checked += 1
                if 0 in row:
                    e=row.index(0)
                    assert (d,r,y,e)==(5,7,1,6)
                    a,n = 16,29
                    labels=orbit(n,a)
                    assert len(labels)==r
                    f=rails_evolve(d,labels,n,a,gates(d,False),(0,1),False,kernel)
                    pair=f[M+y][e]
                    assert pair[0]==pair[1]>0
                    return dict(d=d,r=r,y=y,e=e,N=n,a=a,actual_work=labels[e],
                                mass_pair=pair,rows_examined=checked,
                                paths=[[b,(-3)**((b&~y).bit_count())] for b in range(e,M,r)])
    raise AssertionError('missing cancellation')


def old_observer(path):
    names = ('brc_linear','brc_qsqrt3','phase_kernel','observer_kernel')
    for name in names:
        assert (path/(name+'.py')).is_file()
    sys.path.insert(0, str(path))
    import observer_kernel as o
    got = o.w_back({(3,):o.ONE},0,'P13_replay_local_Z')
    assert got == {(3,):(Fraction(-1,2),0),(2,):(0,Fraction(1,2))}
    return {','.join(map(str,k)):[str(z) for z in v] for k,v in sorted(got.items())}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--core',type=Path,default=Path('src/enterprise_math/brc_weighted_recurrent.py'))
    parser.add_argument('--v09',type=Path,help='optional locally retained v09 source for separate parity-row check')
    args = parser.parse_args()
    if sha256(args.core.read_bytes()).hexdigest()!=CORE_SHA:
        raise ValueError('public core needs its declared frozen SHA-256')
    spec = importlib.util.spec_from_file_location('frozen_positive_brc_53',args.core)
    core = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = core
    spec.loader.exec_module(core)
    kernel = PositivePairs(core.recurrent_mass_power)
    rows = []
    for d,n,a in [(1,3,2),(2,3,2),(3,3,2),(4,3,2),(2,7,2),(2,7,3),(2,7,4),(1,15,2)]:
        for extra in (False,True):
            rows.append(check_case(d,n,a,extra,kernel))
    for extra in (False,True):
        pair = [next(o for o in rows if o['N']==7 and o['a']==a and o['suffix']==extra) for a in (2,4)]
        p,q = pair
        assert [sum(v) for v in p['weighted_joint_rows_integer']]==[sum(v) for v in q['weighted_joint_rows_integer']]
        diff = sum(abs(v[row]-w[q['work_labels'].index(p['work_labels'][row])])
                   for v,w in zip(p['weighted_joint_rows_integer'],q['weighted_joint_rows_integer'])
                   for row in range(3))
        assert diff
        p['TV_vs_generator4_on_actual_labels']=str(Fraction(diff,2*p['common_probability_denominator']))
    raw3 = work_readable_3bits(kernel)
    cancellation = first_base_cancellation(kernel)
    if args.v09:
        print('v09-local-Z',old_observer(args.v09),file=sys.stderr)
    print(json.dumps(dict(public_core_sha256=CORE_SHA, cases=rows,
                          work_readable_raw_three_bits=raw3,first_flag_one_zero_on_reachable_class=cancellation,
                          cached_source_core_calls=kernel.compiled.cache_info().misses,
                          nonzero_local_pair_requests=kernel.requests,
                          max_positive_BRC_endpoint_bits_in_cached_local_calls=kernel.max_positive_bits),
                     indent=2))


if __name__ == '__main__':
    main()
