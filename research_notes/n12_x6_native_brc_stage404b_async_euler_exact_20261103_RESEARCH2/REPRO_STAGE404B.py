#!/usr/bin/env python3
"""Stage404-B: exact coupled Euler transfer and asynchronous memory witnesses.
Native signed alphabet is available; small fibers use A=+E1,B=-E1,T=+E3.
Only Python's standard library and integer arithmetic are used.
"""
from collections import Counter, defaultdict
from functools import lru_cache
import json

A, B, T = '+E1', '-E1', '+E3'
NATIVE = tuple(s + 'E' + str(i) for i in range(1, 7) for s in ('+', '-'))
VEC = {s + 'E' + str(i): tuple((1 if s == '+' else -1) if j == i-1 else 0
                                   for j in range(6)) for i in range(1, 7) for s in ('+', '-')}
INV = {s + 'E' + str(i): ('-' if s == '+' else '+') + 'E' + str(i)
       for i in range(1, 7) for s in ('+', '-')}

def word(abt):
    return tuple({'A': A, 'B': B, 'T': T}[c] for c in abt)

def jhist(w):
    return Counter(zip(w, w[1:]))

def pos(w):
    return tuple(sum(VEC[x][i] for x in w) for i in range(6))

def coincidence(p, q):
    return sum(x == y for x, y in zip(p, q))

def observation(p, q):
    return (len(p), len(q), pos(p), pos(q),
            tuple(sorted(jhist(p).items())), tuple(sorted(jhist(q).items())),
            coincidence(p, q))

def ends_from_edges(j, start):
    # The full label multiplicity is incoming-edge count plus the first symbol.
    n = Counter()
    for (_, b), c in j.items(): n[b] += c
    n[start] += 1
    return tuple(sum(n[a] * VEC[a][i] for a in n) for i in range(6))

def transfer(jp, jq, zp, zq, k_target, tail_width):
    """Compute exact counts per PAIR TAIL without enumerating full paired words.

    Counter input denotes multiplicities of *unlabeled* directed transitions;
    taking an edge of multiplicity r gives one label choice, not r choices.
    """
    ep, eq = tuple(sorted(jp)), tuple(sorted(jq))
    cp, cq = tuple(jp[e] for e in ep), tuple(jq[e] for e in eq)
    starts_p = sorted(set(a for e in ep for a in e)) if ep else list(NATIVE)
    starts_q = sorted(set(a for e in eq for a in e)) if eq else list(NATIVE)
    output = Counter()

    @lru_cache(None)
    def walk(rp, rq, lastp, lastq, k, tail):
        if not any(rp) and not any(rq):
            return {tail: 1} if k == k_target else {}
        out = Counter()
        pchoices = [(i, b) for i, (a, b) in enumerate(ep) if a == lastp and rp[i]]
        qchoices = [(j, d) for j, (c, d) in enumerate(eq) if c == lastq and rq[j]]
        for i, b in pchoices:
            rpp = rp[:i] + (rp[i]-1,) + rp[i+1:]
            for j, d in qchoices:
                rqq = rq[:j] + (rq[j]-1,) + rq[j+1:]
                t = (tail + ((b, d),))[-tail_width:]
                for s, count in walk(rpp, rqq, b, d, k + (b == d), t).items():
                    out[s] += count
        return dict(out)

    for p0 in starts_p:
        if ends_from_edges(jp, p0) != zp: continue
        for q0 in starts_q:
            if ends_from_edges(jq, q0) != zq: continue
            tail = ((p0, q0),)
            for s, count in walk(cp, cq, p0, q0, int(p0 == q0), tail).items():
                output[s] += count
    return output, walk.cache_info()._asdict()

def euler_words(j):
    """Independent direct enumerator for checking small finite fibers only."""
    remaining = Counter(j)
    letters = sorted(set(x for e in j for x in e)) if j else NATIVE
    length = 1 + sum(j.values())
    def rec(w):
        if len(w) == length:
            yield w
            return
        for b in letters:
            edge = (w[-1], b)
            if remaining[edge]:
                remaining[edge] -= 1
                yield from rec(w + (b,))
                remaining[edge] += 1
    for start in letters:
        yield from rec((start,))

def exact_fiber(jp, jq, zp, zq, k):
    ps = [p for p in euler_words(jp) if pos(p) == zp]
    qs = [q for q in euler_words(jq) if pos(q) == zq]
    return [(p, q) for p in ps for q in qs if coincidence(p, q) == k]

def popq(p, q):
    if not q: return None
    return (p, q[:-1])

def cancel(p, q):
    if (len(p) < 2 or len(q) < 2 or p[-2] != INV[p[-1]]
            or q[-2] != INV[q[-1]]): return None
    return (p[:-2], q[:-2])

def pop_then_cancel_signature(p, q):
    """One fixed legal-action decision trace; 'disabled' is observable."""
    result = [observation(p, q)]
    for action in (popq, cancel, cancel):
        updated = action(p, q)
        if updated is None:
            result.append(('DISABLED', action.__name__))
            break
        p, q = updated
        result.append(observation(p, q))
    return tuple(result)

def exact_c0_key(p, q):
    assert len(p) == len(q) >= 2
    return (p[-1], q[-2], q[-1])

def finite_c0_crosscheck(x, y, depth=4):
    """Finite supplementary check over 3 native labels (not the theorem proof)."""
    actions = [('POPQ',)] + [('APPEND', a, b) for a in (A, B, T) for b in (A, B, T)]
    frontier = [(x[0], x[1], y[0], y[1], False)]
    checked = 0
    for _ in range(depth + 1):
        nxt = []
        for p, q, pp, qq, used in frontier:
            assert observation(p, q) == observation(pp, qq)
            checked += 1
            for action in actions:
                if action[0] == 'POPQ':
                    if used or not q: continue
                    new = (p, q[:-1], pp, qq[:-1], True)
                else:
                    _, a, b = action
                    new = (p+(a,), q+(b,), pp+(a,), qq+(b,), used)
                nxt.append(new)
        frontier = nxt
    return checked

def native_brc_counts(n):
    states = {(0,) * 6: 1}
    for _ in range(n):
        next_states = defaultdict(int)
        for z, ways in states.items():
            for d in NATIVE:
                next_states[tuple(z[i] + VEC[d][i] for i in range(6))] += ways
        states = next_states
    return states

def main():
    assert len(NATIVE) == 12 and len(set(NATIVE)) == 12
    # C=0: the whole observation fiber has two paths but one exact future state.
    p1, p2, q0 = word('AABA'), word('ABAA'), word('AAAA')
    assert observation(p1, q0) == observation(p2, q0)
    o = observation(p1, q0)
    f0 = exact_fiber(jhist(p1), jhist(q0), pos(p1), pos(q0), o[-1])
    assert set(f0) == {(p1, q0), (p2, q0)}
    d0, meta0 = transfer(jhist(p1), jhist(q0), pos(p1), pos(q0), 3, 2)
    assert sum(d0.values()) == 2 and len(d0) == 2
    assert len({exact_c0_key(*pair) for pair in f0}) == 1
    finite_checked = finite_c0_crosscheck(f0[0], f0[1])
    # C=2: exact full finite fiber of the Stage403 J,z,K witness.
    p8, q8 = word('TTTAABAB'), word('AABABABA')
    f2 = exact_fiber(jhist(p8), jhist(q8), pos(p8), pos(q8), 1)
    d2, meta2 = transfer(jhist(p8), jhist(q8), pos(p8), pos(q8), 1, 6)
    brute = Counter(tuple(zip(p[-6:], q[-6:])) for p, q in f2)
    assert d2 == brute
    assert len(f2) == 5 and len(d2) == 5 and all(n == 1 for n in d2.values())
    traces = [pop_then_cancel_signature(p, q) for p, q in f2]
    assert len(set(traces)) == 5
    counts4 = native_brc_counts(4)
    counts8 = native_brc_counts(8)
    assert counts4[pos(p1)] == 64
    assert counts8[pos(p8)] == 68768
    assert counts8[pos(q8)] == 385056
    evidence = {
      'result': 'STAGE404B_EULER_ASYNC_MINIMAL_PASS',
      'alphabet_size_native': len(NATIVE),
      'c0': {'m': 4, 'K': 3, 'fiber_size': len(f0),
             'paired_suffix_2_states': len(d0), 'minimal_states': 1,
             'before_bits': 1, 'after_bits': 0,
             'future_trace_nodes_checked': finite_checked,
             'dp_cache': meta0},
      'c2': {'m': 8, 'K': 1, 'fiber_size': len(f2),
             'suffix_6_states': len(d2), 'exact_minimal_states': len(set(traces)),
             'distinguishing_trace': ['POP_Q', 'CANCEL', 'CANCEL'],
             'candidate_pair_words': [[''.join({A:'A',B:'B',T:'T'}[x] for x in p), ''.join({A:'A',B:'B',T:'T'}[x] for x in q)] for p,q in f2],
             'dp_cache': meta2},
      'brc': {'N4_2E1': counts4[pos(p1)], 'N8_P': counts8[pos(p8)],
              'N8_Q': counts8[pos(q8)]},
      'verification': 'integer-only DP, independent direct Euler enumeration of both fibers, exact BRC recursion; theorem proofs in PROOF_STAGE404B.md'
    }
    print(json.dumps(evidence, ensure_ascii=False, sort_keys=True, indent=2))

if __name__ == '__main__': main()
