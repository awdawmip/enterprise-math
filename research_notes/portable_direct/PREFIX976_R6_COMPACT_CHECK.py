"""Exact integer verifier for PREFIX-976; auxiliary BRC-positive XOR-port observer.
No native X6 dynamics or formal project admission is claimed.
"""
from itertools import product

def dictionary(p):
    d = {}
    for i, j, sign in product(range(p), range(p), (1, -1)):
        c = (1 << i) - sign * (1 << j)
        P, M = d.get(c, (0, 0))
        d[c] = (P | (1 << j), M) if sign == 1 else (P, M | (1 << j))
    return d

def port(pm, x):
    P, M = pm
    return (P & ~x) | (M & x)

def dynamic(pm, qm, x, p, kernel):
    U = port(pm, x)
    return sum(kernel(j, J) for j in range(1, p) if U & (1 << j)
               for J in range(1, p)
               if port(qm, x ^ (1 << j)) & (1 << J))

def baseline(pm, qm, x, p, kernel):
    U, V = port(pm, x), port(qm, x)
    return sum(kernel(j, J) for j in range(1, p) if U & (1 << j)
               for J in range(1, p) if V & (1 << J))

def correction(pm, qm, x, p, kernel):
    U, V = port(pm, x), port(qm, x)
    P, M = qm
    return baseline(pm, qm, x, p, kernel) + sum(
        kernel(j, j) * (1 - 2 * bool(V & (1 << j)))
        for j in range(1, p) if (U & (P ^ M) & (1 << j)))

def diagonal_closed(pm, qm, x, p):
    P, M = pm
    R, S = qm
    odd_preserving_ports = ((1 << p) - 1) ^ 1
    return ((P & S & ~x & odd_preserving_ports).bit_count()
            + (M & R & x & odd_preserving_ports).bit_count())

def run():
    self_states, pair_states = 0, 0
    for p in range(4, 9):
        d = dictionary(p)
        expected = {3 * (1 << j) for j in range(1, p - 2)}
        observed = set()
        for c, pm in d.items():
            for x in range(1, 1 << p, 2):
                result = dynamic(pm, pm, x, p, lambda j, J: int(j == J))
                assert result == diagonal_closed(pm, pm, x, p)
                assert result == (pm[0] & pm[1] & ~1).bit_count()
                self_states += 1
                if result:
                    observed.add(c)
        assert observed == expected
        selected = sorted(d) if p <= 6 else sorted(set(sorted(d)[:20] + sorted(d)[-20:] + [0, 3, -3]))
        for c, C in product(selected, repeat=2):
            for x in range(1, 1 << p, 2):
                pm, qm = d[c], d[C]
                diag = lambda j, J: int(j == J)
                offdiag = lambda j, J: (j + 2*J + 1) if j != J else 0
                assert dynamic(pm, qm, x, p, diag) == diagonal_closed(pm, qm, x, p)
                assert dynamic(pm, qm, x, p, diag) == correction(pm, qm, x, p, diag)
                assert dynamic(pm, qm, x, p, offdiag) == baseline(pm, qm, x, p, offdiag)
                pair_states += 1
    p = 19
    d = dictionary(p)
    assert len(d) == 499
    assert {c for c, (P, M) in d.items() if P & M & ~1} == {3*(1 << j) for j in range(1, p-2)}
    diag = lambda j, J: int(j == J)
    assert baseline(d[0], d[0], 1, p, diag) == 18
    assert dynamic(d[0], d[0], 1, p, diag) == 0
    print({"self_states": self_states, "pair_states": pair_states,
           "p19_return_residues": 16, "p19_return_path_mass_over_all_odd_x": 16*(1 << 18)})

if __name__ == '__main__':
    run()
