"""Six reciprocal moments, fully integer dyadic tests under two independent budgets."""
from collections import Counter, defaultdict
from hashlib import sha256
from functools import lru_cache
from itertools import combinations
import json
from math import factorial, prod
from pathlib import Path
import subprocess
import ternary_check as ternary
from tempfile import TemporaryDirectory

BUDGET = 2331
ORDERS = tuple(range(1, 7))
GRID = 32 * 27 * 5 * 7 * 11 * 13 * 17


def valuation(n):
    return (n & -n).bit_length() - 1


def moduli(step):
    return tuple(step**j << valuation(factorial(j)) for j in ORDERS)


@lru_cache(maxsize=None)
def signature_of_atom(d, h, step):
    v = valuation(d)
    assert v <= h
    out = []
    for j, m in zip(ORDERS, moduli(step)):
        x = (1 << (h - v)) * pow(d >> v, -1, m)
        out.append(prod(x - i * step for i in range(j)) % m)
    return tuple(out)


def signature(side, h, step):
    columns = [signature_of_atom(d, h, step) for d in side]
    return tuple(sum(col[j] for col in columns) % m for j, m in enumerate(moduli(step)))


def budget_left(side):
    return BUDGET - sum(d - 1 for d in side)


def words(atoms, budget, start=0):
    yield ()
    for i in range(start, len(atoms)):
        d = atoms[i]
        if d - 1 > budget:
            break
        for tail in words(atoms, budget - d + 1, i):
            yield (d,) + tail


def highest_layer(h, atoms):
    mod = moduli(2)
    columns = [signature_of_atom(d, h, 2) for d in atoms]
    buckets = defaultdict(list)

    def visit(start, left, s, word):
        key = 0
        for entry, m in zip(s, mod):
            key = key * m + entry
        buckets[key].append(word)
        for i in range(start, len(atoms)):
            cost = atoms[i] - 1
            if cost > left:
                break
            new = tuple((x + y) % m for x, y, m in zip(s, columns[i], mod))
            visit(i, left - cost, new, word + bytes([i]))

    visit(0, BUDGET, (0,) * 6, b'')
    primitive = set()
    raw = 0
    for group in buckets.values():
        for left, right in combinations(group, 2):
            raw += 1
            a, b = Counter(left), Counter(right)
            canceled = [tuple(atoms[i] for i in sorted(side.elements())) for side in (a-b, b-a)]
            primitive.add(tuple(sorted(canceled)))
    return dict(denominators=atoms, sides=sum(map(len, buckets.values())),
                distinct=len(buckets), equal_pairs=raw), sorted(primitive)


def unconditional():
    result = []
    for h in range(11, 5, -1):
        atoms = list(range(1 << h, BUDGET + 2, 2 << h))
        row, pairs = highest_layer(h, atoms)
        row['h'] = h
        if h > 6:
            assert not pairs
        else:
            assert len(pairs) == 2
            distinctions = []
            for a, b in pairs:
                assert budget_left(a) == budget_left(b)
                budget = budget_left(a)
                low = list(range(32, budget + 2, 64))
                tails = list(words(low, budget))
                left = [signature(a + w, h, 4) for w in tails]
                right = [signature(b + w, h, 4) for w in tails]
                # Test every order in increasing order. Only a provably empty set suffices.
                successful = []
                for j in ORDERS:
                    lset = {v[j-1] for v in left}
                    rset = {v[j-1] for v in right}
                    if lset.isdisjoint(rset):
                        successful.append(j)
                assert successful
                j = successful[0]
                distinctions.append(dict(left=a, right=b, remaining=budget, layer5=low,
                                         tails=len(tails), separating_orders=successful,
                                         order=j, modulus=moduli(4)[j-1],
                                         left_residues=sorted({v[j-1] for v in left}),
                                         right_residues=sorted({v[j-1] for v in right})))
            row['primitive_comparison'] = distinctions
        result.append(row)
    return result


def odd_cover(program, cases, grid):
    """Cover every reduced prefix by an empty attainable odd-prime difference set."""
    limit = max(max(a,b) for a,b,*_ in cases)
    survivors = set(range(len(cases)))
    rounds = []
    @lru_cache(maxsize=None)
    def local(d, p):
        return ternary.column(d, p)

    def run(p, power, pivots, max_rows):
        if not survivors:
            return
        den = [d for d in range(power, limit+2, power)
               if grid % d == 0 and d % 16 != 0]
        # Distinct unit residues give Vandermonde pivots on the highest rows modulo p.
        heads = {}
        for d in den:
            heads.setdefault((d//power) % p, d)
        first = list(heads.values())[:pivots]
        assert len(first)==pivots and 0 not in heads
        tail = [d for d in den if d not in first]
        atoms = first + tail
        costs = [1]+[0]*limit
        for d in tail:
            for b in range(d-1, limit+1):
                costs[b] += costs[b-d+1]
        cap = -1
        cumul = 0
        for b,n in enumerate(costs):
            cumul += n
            if cumul>max_rows:
                break
            cap=b
        mods = ternary.moduli(p)
        batches = defaultdict(list)
        for i in sorted(survivors):
            a,b,diff = cases[i]
            if b>cap:continue
            selected=[(m,local(d,p)) for d,m in diff.items() if d%power==0]
            v=[sum(m*s[j] for m,s in selected)%mod for j,mod in enumerate(mods)]
            if any(v):
                batches[b//140].append((i,a,b,v))
        rejected=[]
        maximum=0
        processed=0
        for batch in batches.values():
            data,answers=ternary.cross_prime(program,p,pivots,atoms,batch)
            processed+=len(batch)
            maximum=max(maximum,data['tail_multisets'])
            rejected.extend(i for i,ok in answers.items() if not ok)
        survivors.difference_update(rejected)
        rounds.append(dict(prime=p,divisor=power,pivots=first,cap=cap,queries=processed,
                           rejected=len(rejected),largest_catalog=maximum,remaining=len(survivors)))

    for p,power,o in [(17,17,2),(13,13,2),(11,11,2),(7,7,3),(3,9,2)]:
        run(p,power,o,3000000)
    for p,o in [(17,3),(13,3),(11,3),(11,4),(13,4)]:
        run(p,p,o,5000000)
    run(13,13,5,12000000)
    run(11,11,5,7000000)
    assert not survivors, sorted(survivors)
    return rounds


def next_layer():
    atoms = [d for d in range(32, BUDGET + 2, 64) if GRID % d == 0]
    row, pairs = highest_layer(5, atoms)
    lower = [d for d in range(16, BUDGET + 2, 32) if GRID % d == 0]
    m = moduli(2)
    lines = [f'{len(lower)} {len(pairs)}', ' '.join(map(str, m))]
    for d in lower:
        v = signature_of_atom(d, 5, 4)
        assert all(x % (1 << j) == 0 for j, x in zip(ORDERS, v))
        lines.append(' '.join(map(str, [d, *(x >> j for j, x in zip(ORDERS, v))])))
    for i, (a, b) in enumerate(pairs):
        if budget_left(a) > budget_left(b):
            a, b = b, a
        delta = [x - y for x, y in zip(signature(a, 5, 4), signature(b, 5, 4))]
        assert all(x % (1 << j) == 0 for j, x in zip(ORDERS, delta))
        target = [(x >> j) % z for j, x, z in zip(ORDERS, delta, m)]
        lines.append(' '.join(map(str, [i, budget_left(a), budget_left(b), *target])))
    with TemporaryDirectory() as directory:
        exe = Path(directory) / 'dyadic_layer'
        subprocess.run(['c++', '-std=c++17', '-O2', str(Path(__file__).with_name('dyadic_next.cpp')),
                        '-o', str(exe)], check=True)
        out = subprocess.check_output([exe], input='\n'.join(lines)+'\n', text=True)
    rows = iter(out.splitlines())
    cap, count = map(int, next(rows).split())
    survivors = []
    visited = 0
    canonical_count = 0
    checksum = sha256()
    joint = []
    for index, pair in enumerate(pairs):
        i, tries, matches, number = map(int, next(rows).split())
        assert index == i and number <= matches
        visited += tries
        a, b = pair
        if matches:
            survivors.append(dict(id=i, left=a, right=b, layer4_pairs=matches, after_cancel=number))
        if budget_left(a)>budget_left(b):
            a,b=b,a
        for _ in range(number):
            digits = tuple(map(int, next(rows).split()))
            assert len(digits) == len(lower)
            canonical_count += 1
            checksum.update((' '.join(map(str,[i,*digits]))+'\n').encode())
            fixed_left = Counter(a)
            fixed_right = Counter(b)
            for d, c in zip(lower,digits):
                if c>0:
                    fixed_left[d] += c
                elif c<0:
                    fixed_right[d] -= c
            r = BUDGET-sum((d-1)*c for d,c in fixed_left.items())
            t = BUDGET-sum((d-1)*c for d,c in fixed_right.items())
            assert min(r,t)>=0 and not fixed_left.keys() & fixed_right.keys()
            if any(d%27==0 for d in fixed_left.keys() | fixed_right.keys()):
                continue
            if r>t:
                r,t=t,r
                fixed_left,fixed_right=fixed_right,fixed_left
            diff = fixed_right.copy()
            diff.subtract(fixed_left)
            joint.append((r,t,diff))
    assert next(rows,None) is None
    assert canonical_count == 9338 and len(joint) == 7179
    with TemporaryDirectory() as directory:
        program = Path(directory)/'prime'
        subprocess.run(['c++','-std=c++17','-O3',str(Path(__file__).with_name('ternary_solver.cpp')),
                        '-o',str(program)],check=True)
        cover = odd_cover(program,joint,GRID//3)
    example = next(item for item in survivors if item['id'] == 434)
    a, b = example['left'], example['right']
    joined = defaultdict(list)
    for w in words(lower, budget_left(a)):
        joined[signature(a+w, 5, 4)].append(w)
    witnesses = [(l, r) for r in words(lower, budget_left(b)) for l in joined[signature(b+r, 5, 4)]]
    assert len(witnesses) == example['layer4_pairs'] == 1
    assert (row['sides'], row['distinct'], len(pairs), len(survivors)) == (274374, 225140, 643, 85)
    count_pairs = sum(x['layer4_pairs'] for x in survivors)
    assert count_pairs == 837168
    return dict(grid=GRID, layer5=row, canonical_top_pairs=len(pairs), layer4=lower,
                max_layer4_budget=cap, visited_wide_layer4_sides=count, indexed_narrow_layer4_sides=visited,
                canonical_joint_pairs=canonical_count, canonical_rows_sha256=checksum.hexdigest(),
                without_denominator_divisible_by_27=len(joint), odd_stages=cover,
                new_lcm=GRID//6,
                surviving_top_pairs=len(survivors),
                top_pair_table_sha256=sha256(json.dumps(survivors,sort_keys=True,
                    separators=(',',':')).encode()).hexdigest(),
                oriented_joint_pairs=count_pairs,
                example=dict(top_pair_id=434,top_left=a,top_right=b,only_next_layer_pair=witnesses[0]))


if __name__ == '__main__':
    print(json.dumps(dict(side_budget=BUDGET, unconditional=unconditional(), grid_test=next_layer()),
                     indent=2, sort_keys=True))
