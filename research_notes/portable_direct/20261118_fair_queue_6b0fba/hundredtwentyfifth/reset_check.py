"""Reproduce finite, positive-source cleanup costs from the pinned public T and E.

Run python reset_check.py --repo /path/to/enterprise-math
"""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
import hashlib
from itertools import product
import json
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
BOOK = 'research_tasks/RS-EULER-RR-20261012-04.md'
FIVE = [(0,1,0,0,0), (2,0,0,0,1), (0,1,0,0,1), (1,0,0,0,1), (2,1,0,0,1)]


def read_sources(repo):
    data = (repo / BOOK).read_bytes()
    assert hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest() == '9b3f65400b5e3c3a53da5edce62a11da5a6624d9'
    path = HERE.parent / 'hundredth' / 'latch_check.py'
    assert hashlib.sha256(path.read_bytes()).hexdigest() == 'a7d08b83611897633cb489596123814298b780b0516c9f99a57f7e4636ab938b'
    sys.path.insert(0, str(path.parent))
    from latch_check import load
    return load(repo)


def orbit_table(cycle):
    states = list(product(range(3),range(2),range(8),range(4),range(2)))
    words = {}
    periods = Counter()
    for state in states:
        x = state
        path = []
        for h in range(12):
            path.append(x[0])
            x = cycle(x)
            if h == 5:
                assert x[1:] == (1-state[1], *state[2:])
        assert x == state
        x = cycle(state)
        period = 1
        while x != state:
            x = cycle(x)
            period += 1
        periods[period] += 1
        words[state] = tuple(path)
    assert periods == {4:240,12:144}
    return words, periods


def color_count(adj):
    if not any(adj):
        return 1
    colors = [-1]*len(adj)
    for start in range(len(adj)):
        if colors[start] >= 0:
            continue
        colors[start] = 0
        pending = [start]
        while pending:
            i = pending.pop()
            neighbors = adj[i]
            while neighbors:
                bit = neighbors & -neighbors
                j = bit.bit_length()-1
                neighbors -= bit
                if colors[i] == colors[j]:
                    return 3  # j0 itself gives a proper coloring with three colors.
                if colors[j] == -1:
                    colors[j] = 1-colors[i]
                    pending.append(j)
    return 2


def menus(word_by_state):
    words = sorted(set(word_by_state.values()))
    separate = []
    for h in range(12):
        separate.append(tuple(sum(1 << j for j,z in enumerate(words)
                                  if z[0] != w[0] and z[h] == w[h]) for w in words))
    selectable = Counter()
    for mask in range(1,1 << 12):
        ts = [h for h in range(12) if mask >> h & 1]
        adj = [0]*len(words)
        for h in ts:
            adj = [a|b for a,b in zip(adj,separate[h])]
        result = color_count(adj)
        assert result == (1 if set(ts) <= {0} else 2 if set(ts) <= {0,1} or set(ts) <= {0,11} else 3)
        selectable[result] += 1
    five = [[word_by_state[x][h] for h in (0,1,11)] for x in FIVE]
    for u,v in zip(five,five[1:]+five[:1]):
        assert u[0] != v[0] and (u[1] == v[1] or u[2] == v[2])
    jointly = Counter()
    shortest = []
    for mask in range(1 << 11):
        ts = [h for h in range(1,12) if mask >> (h-1) & 1]
        fibers = defaultdict(set)
        for w in words:
            fibers[tuple(w[h] for h in ts)].add(w[0])
        capacity = max(map(len,fibers.values()))
        jointly[capacity] += 1
        if capacity == 1 and len(ts) <= 3:
            shortest.append(ts)
    assert sorted(shortest) == [[h,6,h+6] for h in range(1,6)]
    for w in words:
        assert all((w[h]+w[h+6]-w[6])%3 == w[0] for h in range(1,6))
    return dict(distinct_words=len(words), selectable_nonempty=dict(selectable),
                odd_cycle_states=FIVE, odd_cycle_triples=five,
                joint_menus_without_phase_zero=dict(jointly), shortest_joint_reads=sorted(shortest))


def adaptive(words, chronological):
    frequency = Counter(words.values())
    universe = tuple(sorted(frequency))
    mass = tuple(frequency[w] for w in universe)
    infinity = 10**6

    @lru_cache(None)
    def solve(ids, last):
        if len({universe[i][0] for i in ids}) == 1:
            return 0
        best = infinity
        for h in range(last+1,12):
            parts = defaultdict(list)
            for i in ids:
                parts[universe[i][h]].append(i)
            if len(parts) < 2:
                continue
            future = sum(solve(tuple(part), h if chronological else 0) for part in parts.values())
            best = min(best, sum(mass[i] for i in ids) + future)
        return best

    return str(Fraction(solve(tuple(range(len(universe))),0),sum(mass)))


def approximate(words):
    # Separate implementations: raw worlds for the histogram and all decoder truth tables for the budgets.
    triples = Counter((w[0],w[1],w[11]) for w in words.values())
    assert len(triples) == 12 and set(triples.values()) == {32}
    groups = ['011 100 102 120 122','022 200 201 210 211','012 021']
    colored = [[tuple(map(int,s)) for s in part.split()] for part in groups]
    assert sorted(z for part in colored for z in part) == sorted(triples)
    assert all(len({z[0] for z in part if z[h]==y})<=1
               for part in colored for h in (1,2) for y in range(3))
    types = list(triples)
    independent_sizes = []
    for mask in range(1<<len(types)):
        chosen = [z for i,z in enumerate(types) if mask>>i & 1]
        if all(len({z[0] for z in chosen if z[h]==y})<=1 for h in (1,2) for y in range(3)):
            independent_sizes.append(len(chosen))
    assert max(independent_sizes)==5
    options = list(product((-1,1), repeat=2))
    pareto = set()
    for decoder in product(options, repeat=6):
        counts = [0,0]
        for (z,u,v), n in triples.items():
            # The first schedule is at least as likely as the second. For equal success here, prefer the second.
            a,b = max((((u+decoder[u][tag])%3 == z, (v+decoder[3+v][tag])%3 == z) for tag in (0,1)))
            counts[0] += n*a
            counts[1] += n*b
        pareto.add(tuple(counts))
    assert max(a+b for a,b in pareto) == 704 and (384,320) in pareto
    front = sorted(p for p in pareto if not any(q != p and all(a>=b for a,b in zip(q,p)) for q in pareto))
    return dict(physical_triple_multiplicity=32,actual_triples=len(triples),true_decoder_tables=4**6,
                largest_compatible_tag_class=5, optimal_zero_error_prefix_mean_bits="19/12",
                nondominated_counts_prefer_plus=front, equal_weight_two_tag_correct='11/12',
                zero_error_mean_probes_chronological=adaptive(words,True),
                zero_error_mean_probes_arbitrary_phases=adaptive(words,False),
                channel_only_two_tag_correct='5/6')


def transitions(kernel,cycle,gate,contact,words):
    # Representative plus and minus waits.  The clock is fixed before writing and the same tag is used for both.
    out = {}
    for route in ('phase_replay','stored_copy','export_tag'):
        cost = Counter()
        total = kernel.CWM_ZERO
        for (src,w),a,sheet,h in product(words.items(),range(3),(-1,1),(1,11)):
            mass = kernel.cwm_edge(Fraction(1,4608))
            ports = [src[0],a,a]
            mass = contact(ports,2,src[0]-a,(1,sheet),mass,kernel,cost)
            assert ports[2] == w[0]
            # Copy and exported tag each use one fresh ternary port.  Here the external tag is recycled only by its owner.
            if route != 'phase_replay':
                aux = [src[0],a,a]
                mass = contact(aux,2,src[0]-a,(1,sheet),mass,kernel,cost)
                assert aux[2] == src[0]
            current = src
            def steps(x,n,weight):
                for _ in range(n):
                    for cmd in 'HUC':
                        x = gate(x,cmd)
                        weight = kernel.cwm_propagate(weight,kernel.CWM_ONE)
                        cost['source_commands'] += 1
                return x,weight
            current,mass = steps(current,h,mass)
            assert current[0] == w[h]
            if route == 'phase_replay':
                current,mass = steps(current,12-h,mass)
                read = current[0]
            else:
                read = aux[2]
            mass = contact(ports,2,a-read,(1,sheet),mass,kernel,cost)
            assert ports[2] == a
            if route == 'phase_replay':
                current,mass = steps(current,h,mass)
            elif route == 'stored_copy':
                # Return scratch to a using the full retained source; this extra pass uses only forward original gates.
                current,mass = steps(current,12-h,mass)
                mass = contact(aux,2,a-current[0],(1,sheet),mass,kernel,cost)
                current,mass = steps(current,h,mass)
                assert aux[2] == a
            else:
                cost['retained_ternary_records'] += 1
            ref = src
            for _ in range(h):
                ref = cycle(ref)
            assert current == ref
            total = kernel.cwm_recoalesce(total,mass)
        assert (total.count,total.total,total.dominant) == (4608,1,Fraction(1,4608))
        out[route] = dict(costs=dict(cost), world_rows=total.count,total=str(total.total))
    return out


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--repo',type=Path,required=True)
    args=ap.parse_args()
    kernel,cycle,gate,contact = read_sources(args.repo.resolve())
    words,periods = orbit_table(cycle)
    fixed = [dict(sorted(Counter(w[h] for w in words.values() if w[0] == 0).items())) for h in range(12)]
    result = dict(source_states=len(words),period_counts=dict(periods),conditional_counts_origin_zero=fixed,
                  menus=menus(words), approximate=approximate(words),
                  native_positive_routes=transitions(kernel,cycle,gate,contact,words))
    print(json.dumps(result,indent=2,sort_keys=True,ensure_ascii=False))


if __name__=='__main__':
    main()
