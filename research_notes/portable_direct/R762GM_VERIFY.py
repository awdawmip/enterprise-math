#!/usr/bin/env python3
"""R762GM moving named-Port signed STAR candidate: complete exact BRC path DP.
Standard-library Python 3 only. The dynamics and weights are the explicit typed
signed-word BRC semantics of this candidate, not native-physics attribution.
"""
import itertools
import json
from collections import Counter, defaultdict

VERTICES = range(4)
EDGES = tuple(itertools.combinations(VERTICES, 2))  # 01,02,03,12,13,23
EDGEID = {e: i for i, e in enumerate(EDGES)}
STARS = tuple(tuple(EDGEID[tuple(sorted((v, w)))]
                    for w in VERTICES if v != w) for v in VERTICES)
ZERO = (0,) * 6
IDENT = tuple(range(6))
E0 = EDGEID[(0, 1)]

def compose(p, q):
    return tuple(p[q[i]] for i in range(6))

def apply(p, x):
    out = [0] * 6
    for i, j in enumerate(p):
        out[j] = x[i]
    return tuple(out)

def inverse(p):
    return tuple(p.index(i) for i in range(6))

def cycle(star):
    p = list(IDENT)
    a, b, c = star
    p[a], p[b], p[c] = b, c, a
    return tuple(p)

CYC = tuple(cycle(STARS[v]) for v in VERTICES)
EVENT = {
    (v, s): (
        tuple(s if i in STARS[v] else 0 for i in range(6)),
        CYC[v] if s == 1 else inverse(CYC[v])
    )
    for v in VERTICES for s in (-1, 1)
}

def mul(state, event):
    x, p = state
    y, q = event
    py = apply(p, y)
    return (tuple(x[i] + py[i] for i in range(6)), compose(p, q))

def current_port(p):
    return EDGES[p[E0]]

def diagonal_return(state):
    x, p = state
    if p == IDENT and len(set(x)) == 1:
        return x[0]
    return None

def table_to_depth(mmax=12):
    states = {(ZERO, IDENT): 1}
    out = []
    for m in range(mmax + 1):
        counts = Counter()
        for state, multiplicity in states.items():
            k = diagonal_return(state)
            if k is not None:
                counts[k] += multiplicity
        assert sum(states.values()) == 4 ** m
        out.append({
            "m": m, "states": len(states), "words": 4 ** m,
            "diagonal_return_counts": {str(k): n for k, n in sorted(counts.items())}
        })
        if m < mmax:
            nxt = defaultdict(int)
            for state, weight in states.items():
                for v in current_port(state[1]):
                    for s in (-1, 1):
                        nxt[mul(state, EVENT[(v, s)])] += weight
            states = nxt
    return out

def signed_word_oracle(sign, m=12):
    """Independent direct enumeration: exactly 2^m permitted vertex choices."""
    count = 0
    witness = None
    def dfs(state, prefix, left):
        nonlocal count, witness
        if not left:
            if diagonal_return(state) == sign * 6:
                count += 1
                if witness is None:
                    witness = list(prefix)
            return
        for v in current_port(state[1]):
            dfs(mul(state, EVENT[(v, sign)]), prefix + (v,), left - 1)
    dfs((ZERO, IDENT), (), m)
    return count, witness

def check_word(vertices, sign, target):
    state = (ZERO, IDENT)
    ports = []
    for v in vertices:
        port = current_port(state[1])
        ports.append("".join(str(t) for t in port))
        assert v in port
        state = mul(state, EVENT[(v, sign)])
    assert state == ((target,) * 6, IDENT)
    return ports

def main():
    t = table_to_depth(12)
    expected_state_counts = [1, 4, 13, 40, 129, 420, 1313,
                             4008, 12011, 35034, 98873, 266990, 686267]
    expected_zero = {0:1, 2:4, 4:28, 6:224, 8:1884, 10:16256, 12:142616}
    assert [row["states"] for row in t] == expected_state_counts
    for row in t:
        m = row["m"]
        counts = row["diagonal_return_counts"]
        assert counts.get("0", 0) == expected_zero.get(m, 0)
        assert not any(int(k) != 0 for k in counts) if m < 12 else True
    assert t[12]["diagonal_return_counts"] == {"-6":8, "0":142616, "6":8}
    count_pos, plus = signed_word_oracle(+1)
    count_neg, minus = signed_word_oracle(-1)
    assert count_pos == count_neg == 8
    plus_ports = check_word(plus, +1, +6)
    minus_ports = check_word(minus, -1, -6)
    assert plus == [0,0,0,1,2,2,2,1,3,3,3,1]
    assert minus == [0,0,0,1,3,3,3,1,2,2,2,1]
    evidence = {
        "schema":"R762GM_MOVING_PORT_SIGNED_BRC_CERTIFICATE_V1",
        "candidate":"Semidirect signed STAR dynamics with Port e=p(01), permit v in endpoints(e)",
        "arithmetic":"exact integers; typed positive multiplicities over signed-word branches",
        "complete_dp_horizon":"m=0..12", "status":"PASS",
        "table":t, "positive_12_word_oracle":count_pos,
        "negative_12_word_oracle":count_neg,
        "positive_witness":plus, "positive_ports_before_event":plus_ports,
        "negative_witness":minus, "negative_ports_before_event":minus_ports,
        "first_nonzero_depth_return_m":12,
        "depth12_nonzero_return_probability":"16/16777216 = 1/1048576",
        "review":"NOT_REVIEWED", "native_permission":"CANDIDATE_NOT_ADOPTED"
    }
    print(json.dumps(evidence, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
