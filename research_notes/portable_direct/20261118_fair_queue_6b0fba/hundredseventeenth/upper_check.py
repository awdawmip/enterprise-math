"""Verify exact endpoint sets of the frozen V30 two-PASS score and V42 lift."""
from argparse import ArgumentParser
from collections import Counter
from functools import lru_cache
from hashlib import sha256
from itertools import combinations, permutations, product
import json
from math import factorial, prod
from pathlib import Path

AXES = tuple(range(6))
TRIADS = tuple(combinations(AXES, 3))
INITIAL = (3, 4, 5)
STAR = (0, 3, 4)
U = (-3, 0, 4, -1)
OMEGA = ((0,0,2,2), (0,0,1,1), (-2,-1,0,1), (-2,-1,-1,0))
MATCHINGS = (((0,1),(2,3),(4,5)), ((0,2),(1,4),(3,5)),
             ((0,3),(1,5),(2,4)), ((0,4),(1,3),(2,5)))
V = ((1,1,0),(1,-1,0),(1,0,1),(1,0,-1),(0,1,1),(0,1,-1))
SOURCE = {
    'experiments/x6_network_event_ledger_v29_20260906/check_event_order_holonomy.py':
    '184c5954d9211f8c2c1ee55972008d6b5b324b60e4c7c64a7ca3fef6046673d4',
    'experiments/x6_nonfcc_observer_switch_v42_20260906/check_nonfcc_observer_switch.py':
    'b00d3a283b84bf2082eeb0e69b4d750eaf18fd38b90c36f6e1d711eca15763d2'}


def chart(s):
    return ''.join(map(str, s))


def contrast(s, matching):
    if any((a in s) == (b in s) for a, b in matching):
        return 0
    return (-1)**sum(b in s for _, b in matching)


C = {s: tuple(contrast(s, m) for m in MATCHINGS) for s in TRIADS}
NEIGH = {s: tuple(t for t in TRIADS if len(set(s)&set(t))==2) for s in TRIADS}


def affine(s, t):
    x, y = C[s], C[t]
    intercept = sum(U[i]*y[i] for i in range(4))
    intercept += sum(x[i]*OMEGA[i][j]*y[j] for i,j in product(range(4),repeat=2))
    slope = y[0]-y[1]+x[0]*y[1]-x[1]*y[0]
    return intercept, slope


SCORES = {s: [(t, *affine(s,t)) for t in NEIGH[s]] for s in TRIADS}


@lru_cache(None)
def active(k, s):
    values = [(a+b*k,t) for t,a,b in SCORES[s]]
    top = max(a for a,t in values)
    winners = [t for a,t in values if a==top]
    return winners[0] if len(winners)==1 else None


@lru_cache(None)
def lift(s,t):
    i, = set(s)-set(t)
    j, = set(t)-set(s)
    a,b = sorted(set(AXES)-set(s)-set(t))
    p = list(AXES)
    p[i],p[j] = p[j],p[i]
    p[a],p[b] = p[b],p[a]
    return tuple(p)


def compose(p,q):
    return tuple(p[i] for i in q)


@lru_cache(None)
def carried(p):
    return tuple(sorted(p[i] for i in INITIAL))


@lru_cache(None)
def move(n,p):
    s = carried(p)
    t = active(n,s)
    return compose(lift(s,t),p) if t else None


def advance(layer, bound=None):
    nxt = set()
    for n,p in layer:
        for h in (n+1,n-1):
            if bound is None or abs(h)<=bound:
                frame = move(h,p)
                if frame is not None:
                    nxt.add((h,frame))
    return nxt


def slice_at(layer, n):
    return {p for h,p in layer if h==n}


def even(p):
    return sum(a>b for a,b in combinations(p,2))%2==0


def class_set(s):
    return {p for p in permutations(AXES) if even(p) and carried(p)==s}


def folded_at(layers,t,h):
    if abs(h)>t or (t-h)%2:
        return set()
    cut = min(max(h,-7),7)
    d = abs(h-cut)
    base_t = t-d
    if base_t>=29:
        base_t = 29+(base_t-29)%2
    values = slice_at(layers[base_t],cut)
    for _ in range(d):
        values = {move(cut,p) for p in values}
        assert None not in values
    return values


def word_endpoint(word,start=INITIAL):
    # An independent literal implementation adds V29 ledger increments at every step.
    u = list(U)
    omega = [list(r) for r in OMEGA]
    s, frame = start, AXES
    for letter in word:
        i,j = (0,1) if letter=='A' else (1,0)
        u[i] += 1
        u[j] -= 1
        omega[i][j] += 1
        omega[j][i] -= 1
        v = [u[j]+sum(C[s][i]*omega[i][j] for i in range(4)) for j in range(4)]
        order = sorted((sum(a*b for a,b in zip(v,C[t])),t) for t in NEIGH[s])
        if order[-1][0]==order[-2][0]:
            return None
        t = order[-1][1]
        frame = compose(lift(s,t),frame)
        s = t
    return s,frame


def witness_layer():
    paths = {(0,AXES):''}
    for _ in range(28):
        nxt = {}
        for (n,p),word in paths.items():
            for delta,letter in ((1,'A'),(-1,'B')):
                h = n+delta
                if abs(h)<=8 and (frame:=move(h,p)) is not None:
                    nxt.setdefault((h,frame), word+letter)
        paths = nxt
    result = {}
    for (n,p),w in paths.items():
        if n==0 and carried(p)==(1,2,4):
            assert w.count('A')==w.count('B')==14
            assert word_endpoint(w)==((1,2,4),p)
            result[chart(p)] = w
    assert len(result)==18
    return dict(sorted(result.items()))


def check_observer():
    checked = 0
    for q in range(2,9):
        for s in TRIADS:
            twin = next(((i,j) for i,j in combinations(s,2)
                         if all((a-b)%2==0 for a,b in zip(V[i],V[j]))),None)
            for x in combinations_with_replacement_of_three(q):
                raw = Counter()
                for perm in permutations(x):
                    y = tuple(sum(v*V[i][j] for v,i in zip(perm,s))%q for j in range(3))
                    raw[y] += 3   # Each slot permutation has three hidden even lifts.
                counts = Counter(x)
                m = prod(factorial(v) for v in counts.values())
                merged = q%2==0 and twin is not None and any(
                    (a-b)%q==q//2 for a,b in combinations(x,2))
                assert len(raw)==6//m-int(merged)
                assert sorted(raw.values())==[3*m]*(6//m-2*int(merged))+[6*m]*int(merged)
                checked += 1
    return checked


def combinations_with_replacement_of_three(q):
    for a in range(q):
        for b in range(a,q):
            for c in range(b,q):
                yield a,b,c


def main():
    args = ArgumentParser()
    args.add_argument('--repo',type=Path,help='optionally cross-check the two source file digests')
    opts = args.parse_args()
    if opts.repo:
        for name,digest in SOURCE.items():
            assert sha256((opts.repo/name).read_bytes()).hexdigest()==digest
    assert max(abs(a-c) for s in TRIADS for _,a,_ in SCORES[s] for _,c,_ in SCORES[s])==16
    for s in TRIADS:
        for h in range(7,18):
            assert active(h,s)==active(17,s) is not None
        for h in range(-17,-5):
            assert active(h,s)==active(-17,s) is not None
    assert word_endpoint('AB')[0]==word_endpoint('BA')[0]==STAR
    assert word_endpoint('AAA') is None
    layers = [{(0,AXES)}]
    for t in range(1,32):
        layers.append(advance(layers[-1],8))
    assert layers[31]==layers[29] and layers[30]!=layers[28]
    thresholds = {}
    for n in range(-7,8):
        t_last = 29 if n%2 else 30
        final = slice_at(layers[t_last],n)
        triads = sorted({carried(p) for p in final})
        assert final==set.union(*(class_set(s) for s in triads))
        bad = [t for t in range(abs(n),t_last,2) if slice_at(layers[t],n)!=final]
        first = bad[-1]+2 if bad else abs(n)
        thresholds[str(n)] = [first, len(final),list(map(chart,triads))]
    # Each threshold chart lies on a true cycle of the constant tail map.
    circuits = {}
    for terminal_h, start, cycle_len in [(7,(0,1,2),6),(-7,(1,2,4),2)]:
        s, hol = start, AXES
        walk = [chart(s)]
        for _ in range(cycle_len):
            t = active(terminal_h,s)
            hol = compose(lift(s,t),hol)
            s = t
            walk.append(chart(s))
        assert s==start and len(set(walk[:-1]))==cycle_len
        assert hol==((2,1,0,5,4,3) if terminal_h>0 else AXES)
        assert all(chart(carried(p)) in walk for lay in layers for p in slice_at(lay,terminal_h))
        circuits[str(terminal_h)] = [walk,chart(hol)]
    assert max(row[0]-abs(int(n)) for n,row in thresholds.items())==28
    miss = class_set((1,2,4))-slice_at(layers[26],0)
    assert sorted(map(chart,miss))==['035142','053241']
    count = {(0,AXES)}
    totals = []
    # This compares all unbounded and folded endpoint sets, not just their sizes.
    for t in range(56):
        restored = {(n,p) for n in range(-t,t+1,2) for p in folded_at(layers,t,n)}
        assert count==restored
        totals.append(len(count))
        count = advance(count)
    assert totals[26:30]==[718,764,830,866]
    assert all(totals[t]==45*t-(439 if t%2 else 430) for t in range(28,56))
    # The actual based loop group (distinct from the initial-to-terminal frame coset).
    # Using right composition maps a local reference frame at 034 back to the initial one.
    initial_to_star = word_endpoint('AB')[1]
    inv = tuple(initial_to_star.index(i) for i in AXES)
    loop_layer = {(0,initial_to_star)}
    loop_sizes = []
    for t in range(29):
        if t%2==0:
            loops = {compose(p,inv) for h,p in loop_layer if h==0 and carried(p)==STAR}
            loop_sizes.append(len(loops))
        loop_layer = advance(loop_layer,8)
    assert loop_sizes[-2:]==[17,18]
    print(json.dumps(dict(source_sha256=SOURCE,
        heading='support only; no tie winner; positive named PASS counts; independent of word multiplicity',
        counters='n=#A-#B, t=#A+#B; frames listed as images of axes 012345',
        certificate_band=[-8,8],periodic_pair=[29,31], tail_chart_circuit_and_frame_images=circuits,
        band_sizes_t25_to_31=[len(a) for a in layers[25:32]],
        threshold_table_columns=['first_permanent_time_of_matching_parity','number_of_frames','target_supports'],
        threshold_table=thresholds,missing_at_13_each_terminal_124=sorted(map(chart,miss)),
        all_frames_at_14_each_terminal_124=witness_layer(),
        loop_counts_at_034_balanced_from_0_to_14_each=loop_sizes,
        unrestricted_counts_t0_to_55=totals,
        exhaustive_ambient_observer_samples_q2_to_8=check_observer()),indent=2,ensure_ascii=False))


if __name__=='__main__':
    main()
