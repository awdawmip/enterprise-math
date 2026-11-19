"""Replay original Q22 and verify the sparse-window chord calculation using exact graphs."""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations, permutations, product
import json
from math import comb, exp, factorial, isclose
from pathlib import Path


def pairings(endpoints):
    if not endpoints:
        yield ()
        return
    i = endpoints[0]
    for pos in range(1, len(endpoints)):
        for rest in pairings(endpoints[1:pos] + endpoints[pos+1:]):
            yield ((i,endpoints[pos]),) + rest


def crosses(left, right):
    a,b = left
    c,d = right
    return a < c < b < d or c < a < d < b


def binary_nullity(chords, reversing):
    pivots = {}
    for i, chord in enumerate(chords):
        row = int(reversing[i]) << i
        for j, other in enumerate(chords):
            if crosses(chord, other):
                row |= 1 << j
        while row:
            lead = row.bit_length() - 1
            if lead not in pivots:
                pivots[lead] = row
                break
            row ^= pivots[lead]
    return len(chords) - len(pivots)


def component_count(site_count, changed, reversing):
    if not site_count:
        return 1
    parent = list(range(site_count))

    def root(i):
        while parent[i] != i:
            i = parent[i]
        return i

    def join(a, b):
        parent[root(a % site_count)] = root(b % site_count)

    used = {i for chord in changed for i in chord}
    for i in range(site_count):
        if i not in used:
            join(i-1, i)
    for (a,b), rev in zip(changed,reversing):
        if rev:
            join(a-1, b-1)
            join(a, b)
        else:
            join(a-1, b)
            join(a, b-1)
    return len({root(i) for i in range(site_count)})


def diagram_fiber(chords, signs, verify=False):
    count = 0
    for mask in range(1 << len(chords)):
        ids = [i for i in range(len(chords)) if mask & (1 << i)]
        changed = [chords[i] for i in ids]
        reversing = [signs[i] for i in ids]
        nullity = binary_nullity(changed, reversing)
        if verify:
            assert component_count(2*len(chords),changed,reversing) == 1 + nullity
        count += int(nullity == 0)
    return count


def classify(gaps, width):
    """Return independent overlapping cut pairs when the deterministic hypotheses hold."""
    if not all(x <= width for x in gaps) or len(set(gaps)) != len(gaps):
        return None
    marks = []
    for i,a in enumerate(gaps):
        b = gaps[(i+1) % len(gaps)]
        if a+b <= width:
            continue
        lo,hi = sorted((a,b))
        if not 2*lo < width < 2*hi:
            return None
        marks.append((i,width-hi,lo,a==lo))
    sites = {i for i,_,_,_ in marks}
    if any((i+1) % len(gaps) in sites for i in sites):
        return None
    chords, reversing, used = [], [], set()
    for (i,b1,a1,s1),(j,b2,a2,s2) in combinations(marks,2):
        if max(b1,b2) >= min(a1,a2):
            continue
        if i in used or j in used:
            return None
        chords.append((i,j))
        reversing.append(s1 != s2)
        used.update((i,j))
    return chords, reversing


def synthetic(chords, signs):
    count = len(chords)
    W = 100 + 30*count
    slots = [None]*(2*count)
    for j,((i,k),rev) in enumerate(zip(chords,signs)):
        base = 10*count + 6*j
        slots[i] = [base+3,W-base]
        slots[k] = [base+4,W-(base+1)]
        if rev:
            slots[k].reverse()
    gaps = tuple(a for i,p in enumerate(slots) for a in [*p,i+1])
    out, rs = classify(gaps,W)
    # Number sites consecutively after discarding the known paths between cuts.
    assert [(i//3,j//3) for i,j in out] == list(chords) and rs == list(signs)
    return gaps,W


def signed_diagrams():
    result = []
    for j in range(5):
        hist = Counter()
        switches = 0
        for pairs in pairings(tuple(range(2*j))):
            for signs in product((False,True), repeat=j):
                if j:
                    synthetic(pairs,signs)
                hist[diagram_fiber(pairs,signs,True)] += 1
                switches += 2**j
        assert hist[1] == comb(2*j,j)//(j+1)
        assert Fraction(hist[1],sum(hist.values())) == Fraction(1,factorial(j+1))
        result.append(dict(chords=j, diagrams=sum(hist.values()), switch_sets=switches,
                           fiber_histogram=dict(sorted(hist.items()))))
    return result


def native(args):
    directory = Path(__file__).resolve().parents[1]
    def import_checked(name,path,digest):
        assert sha256(path.read_bytes()).hexdigest() == digest
        spec = spec_from_file_location(name,path)
        module = module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    source = import_checked("oldwindows",directory/"hundredsixteenth"/"rings_check.py",W116)
    lib = import_checked("oldrings",directory/"sixtyfirst"/"rings_check.py",source.W61_SHA)
    kernel = lib.get_kernel(args.source)
    checks = []
    for labels in [(1,2,3,4,5), (2,3,4,5,6,7), (1,2,3,4,5,6,7)]:
        orders = sorted({source.dihedral(g) for g in permutations(labels)})
        native_run = len(labels)<=6
        rounds = {g:lib.native_rounds(kernel,source.binary(g),1+max(labels)) for g in orders} if native_run else {}
        classified = observations = packets = 0
        for W in range(max(labels),2*max(labels)+1):
            matches = defaultdict(list)
            signatures = {}
            back = {}
            for g in orders:
                key = source.gap_key(g,W)
                packet = source.windows(source.binary(g),W)
                assert signatures.setdefault(key,packet) == packet
                assert back.setdefault(packet,key) == key
                matches[key].append(g)
                observations += 1
            if native_run and W % 2 == 0:
                a,b = {},{}
                t = 1+W//2
                for g in orders:
                    key = source.gap_key(g,W)
                    actual = rounds[g][t]
                    assert a.setdefault(key,actual) == actual and b.setdefault(actual,key) == key
                    packets += 1
            for group in matches.values():
                for g in group:
                    out = classify(g,W)
                    if out is not None:
                        assert diagram_fiber(*out) == len(group)
                        classified += 1
        checks.append(dict(gaps=labels,orders=len(orders),decks=observations,classified=classified,
                           original_Q22_packets=packets))
    return checks


def cdf(x):
    mu = exp(-2*x)
    term = total = 1.
    j = 0
    while term > 1.e-15*total:
        j += 1
        term *= 2*mu/(j*(j+1))
        total += term
    return round(exp(-2*mu)*total,10)


def overlap_probabilities():
    rows = []
    for u in (3.,6.,12.,24.):
        # Sort intervals by their left end and integrate the two remaining lengths.
        L = u/2
        exact = 8*exp(-2*u)*(L-2.5+2*(L+1)*exp(-L)+exp(-2*L)/2)
        steps = 20000
        dx = L/steps
        integral = sum((1-exp(-(i+.5)*dx))*(1-exp(-(L-(i+.5)*dx)))**2 for i in range(steps))*dx
        assert isclose(exact,8*exp(-2*u)*integral,rel_tol=3e-8)
        rows.append([int(u),round(exact/((4*u)*exp(-2*u)),9)])
    return rows


W116 = "10f7f3af5fc67b2a5365ccfe1c9232d12aa0ff9a1fd2d5be06ede7588bd1dd5b"
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source",type=Path)
    args = parser.parse_args()
    print(json.dumps(dict(signed_diagrams=signed_diagrams(), native=native(args),
                          overlap_exact_over_leading=overlap_probabilities(),
                          cdf_x_and_probability=[[x,cdf(x)] for x in (-1.,-.5,0.,.5,1.,2.)]),
                     indent=2,sort_keys=True))
