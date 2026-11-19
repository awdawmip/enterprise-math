"""Direct velocity, ordered-word and integer norm checks. Standard library only."""
import json
from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import product
from math import gcd, isqrt


def contact(speeds, masses, edge, integer=False):
    i, j = edge, edge + 1
    w = masses[i] + masses[j]
    s = speeds[i] - speeds[j]
    if integer:
        delta, rem = divmod(2 * masses[j] * s, w)
        if rem:
            return None
    else:
        delta = Q(2 * masses[j] * s, w)
    result = list(speeds)
    result[i] = speeds[i] - delta
    result[j] = result[i] + s
    return tuple(result)


def all_words_safe(speeds, masses, length, calls):
    layer = {speeds}
    for _ in range(length):
        nxt = set()
        for state in sorted(layer):
            for edge in (0, 1):
                calls["directed_letter_evaluations"] += 1
                child = contact(state, masses, edge, integer=True)
                if child is None:
                    return False
                nxt.add(child)
        layer = nxt
    return True


def budgets(speeds, masses):
    return (sum(m*v for m,v in zip(masses,speeds)),
            sum(m*v*v for m,v in zip(masses,speeds)))


def exact_tests():
    counts = Counter()
    grids = []
    for m, M, H in ((1,1,6),(1,2,7),(2,1,6),(1,3,6),(1,7,4),(1,11,3),(2,3,4)):
        masses = (m,m,M)
        b = Q(2*M, m+M).denominator
        for L in range(H+1):
            k = L//2
            mod = b**((L+1)//2)
            survived = 0
            for x,y in product(range(mod), repeat=2):
                got = all_words_safe((x+y,y,0),masses,L,counts)
                expected = x % b**k == 0 and y % b**(L-k) == 0
                assert got == expected
                survived += got
            assert survived*b**L == mod**2
            grids.append([m,M,L,mod**2,survived])
    return grids, dict(counts)


def norm_representations(n):
    c, p = 2, 2
    while p*p <= n:
        e = 0
        while n%p == 0:
            e += 1
            n //= p
        if p%8 in (5,7) and e%2:
            return 0
        if p%8 in (1,3):
            c *= e+1
        p = 3 if p == 2 else p+2
    if n%8 in (5,7):
        return 0
    return c*2 if n > 1 and n%8 in (1,3) else c


def shells(limit):
    # Independent parametrization of P=0: enumerate undistinguished velocity
    # signs separately and determine the actual failing prefix by integer gates.
    hist = defaultdict(Counter)
    calls = Counter()
    for v in range(-isqrt(limit//2),isqrt(limit//2)+1):
        max_u = isqrt(limit-2*v*v)
        for u in range(-max_u,max_u+1):
            n = u*u+2*v*v
            if not n:
                continue
            speeds = (v+u,v-u,-v)
            assert budgets(speeds,(1,1,2)) == (0,2*n)
            depth = 0
            while all_words_safe(speeds,(1,1,2),depth+1,calls):
                depth += 1
                assert 3**depth <= n
            hist[n][depth] += 1
    for n in range(1,limit+1):
        n0,e = n,0
        while n0%3 == 0:
            n0 //= 3
            e += 1
        number = norm_representations(n0)
        target = Counter({i:number for i in range(e+1)}) if number else Counter()
        assert hist.get(n, {}) == target
    examples = [1,2,3,9,18,27,81,3**6,3**7]
    return {"limit":limit, "represented_positive_n":len(hist),
            "named_velocity_triples":sum(sum(c.values()) for c in hist.values()),
            "counts_by_depth_for_examples":{str(n):dict(sorted(hist[n].items())) for n in examples if n<=limit},
            "first_failure_test_calls":dict(calls)}


def matmul(A,B):
    return tuple(tuple(sum(A[i][j]*B[j][k] for j in range(2)) for k in range(2)) for i in range(2))


def mass_triples():
    ident = ((1,0),(0,1))
    orders = Counter()
    examples = {}
    for a,b,c in product(range(1,13),repeat=3):
        if gcd(gcd(a,b),c)>1:
            continue
        U = ((-1,0),(Q(2*a,a+b),1))
        V = ((1,Q(2*c,b+c)),(0,-1))
        R = matmul(V,U)
        trace = R[0][0]+R[1][1]
        denominator = trace.denominator
        assert trace + 2 == Q(4*a*c,(a+b)*(b+c))
        power = ident
        label = "infinite"
        for k in range(1,7):
            power = matmul(R,power)
            assert (power[0][0]+power[1][1]).denominator == denominator**k
            if power == ident:
                label = str(k)
                break
        assert label == {-1:"3",0:"4",1:"6"}.get(trace,"infinite")
        orders[label] += 1
        examples.setdefault(label,[a,b,c])
    return {"primitive_ordered_masses_1_to_12":dict(orders),"first_examples":examples}


def free_collision(speeds):
    masses = (1,1,2)
    start = tuple(map(Q,speeds))
    p0,e0 = budgets(start,masses)
    history = []
    positions = (Q(0),Q(1),Q(10))
    now = Q(0)
    for next_edge in (0,1):
        meetings = [(Q(positions[i+1]-positions[i],start[i]-start[i+1]),i)
                     for i in (0,1) if start[i] > start[i+1] and positions[i+1] > positions[i]]
        delta,edge = min(meetings)
        assert edge == next_edge and delta>0
        positions = tuple(s+delta*v for s,v in zip(positions,start))
        now += delta
        outcome = contact(start,masses,edge)
        transfers = [m*(w-v) for m,v,w in zip(masses,start,outcome)]
        energy_changes = [m*(w*w-v*v)/2 for m,v,w in zip(masses,start,outcome)]
        assert sum(transfers) == sum(energy_changes) == 0
        assert budgets(outcome,masses) == (p0,e0)
        history.append({"gate":["U","V"][edge],"contact_time":str(now),
                        "velocity_after":list(map(str,outcome)),"impulses":list(map(str,transfers)),
                        "kinetic_energy_changes":list(map(str,energy_changes))})
        start = outcome
    return history


def main():
    grids,counts = exact_tests()
    traces = [free_collision(s) for s in ((5,-3,-1),(3,-5,1))]
    assert [q[0]["impulses"] for q in traces] == [["-8","8","0"]]*2
    assert [q[1]["contact_time"] for q in traces] == ["5/3","5"]
    assert [q[1]["impulses"] for q in traces] == [["0","-8","8"],["0","-8/3","8/3"]]
    # Minimum with nonzero approaching first recoil, both approaching on
    # release and opposite integrality outcomes after U,V.
    minimal = [(u*u+2*v*v,u,v) for u in range(1,10) for v in range(1,8)
               if u>2*v and ((u+2*v)%3 == 0) != ((u-2*v)%3 == 0)]
    assert min(minimal) == (18,4,1)
    return {"scope":"effective one-dimensional isolated elastic pair, third port present; each gate chosen explicitly",
            "grid_columns":["m","M","L","difference_residue_pairs","universal_safe"],
            "grids":grids,"grid_direct_calls":counts, "shells":shells(5000),
            "arbitrary_masses":mass_triples(), "free_flight_examples":traces,
            "minimal_P0_n_with_approaching_nonzero_U_and_split_integrality_at_UV":18}


if __name__ == "__main__":
    print(json.dumps(main(),indent=2,sort_keys=True))
