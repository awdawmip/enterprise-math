#!/usr/bin/env python3
"""Exact ordered-history enumeration and causal two-coin certificate (Stage282-B)."""
from fractions import Fraction as F
from itertools import product

HALF = F(1, 2)
P1 = {'P': (F(3, 4), F(1, 4)), 'Q': (F(1, 4), F(3, 4))}
THIRD_ZERO = {
    'P': {(0, 0): F(1, 4), (0, 1): HALF, (1, 0): HALF, (1, 1): F(3, 4)},
    'Q': {(0, 0): F(3, 4), (0, 1): HALF, (1, 0): HALF, (1, 1): F(1, 4)},
}

def terminal_masses(source, x, y, original=False):
    """Enumerate ALL ordered terminal branches, including the third observation."""
    total = F(0)
    observer = F(0)
    terminal_count = 0

    def add(mass, payoff):
        nonlocal total, observer, terminal_count
        if mass:
            total += mass
            observer += mass * payoff
            terminal_count += 1

    for first in (0, 1):
        pfirst = P1[source][first]
        continue1 = F(int(first == 0)) if original else x
        for action1, pact1 in ((0, 1 - continue1), (1, continue1)):
            if not pact1:
                continue
            m1 = pfirst * pact1
            if action1 == 0:
                add(m1, int(source == 'Q' and first == 0))
                continue
            for second in (0, 1):
                m2 = m1 * HALF
                if second == 1:
                    add(m2, 0)
                    continue
                continue2 = F(int(first == 0)) if original else y
                for action2, pact2 in ((0, 1 - continue2), (1, continue2)):
                    if not pact2:
                        continue
                    m3 = m2 * pact2
                    if action2 == 0:
                        add(m3, 0)
                    else:
                        pzero = THIRD_ZERO[source][(first, second)]
                        for third, pthird in ((0, pzero), (1, 1 - pzero)):
                            assert third in (0, 1)
                            payoff = int((source == 'P' and first == 0) or
                                         (source == 'Q' and first == 1))
                            add(m3 * pthird, payoff)
    assert total == 1
    return observer, total, terminal_count

def closed_form(x, y):
    z = x * y
    return F(3, 8) * z, F(1, 4) * (1 - x) + F(3, 8) * z

def risk(x, y):
    P, Q = closed_form(x, y)
    return max(abs(F(3, 8) - P), abs(Q))

def main():
    assert all(0 < v < 1 for d in THIRD_ZERO.values() for v in d.values())
    orig_p = terminal_masses('P', F(0), F(0), original=True)
    orig_q = terminal_masses('Q', F(0), F(0), original=True)
    assert orig_p[0] == F(3, 8) and orig_q[0] == 0
    checked = 0
    for a, b in product(range(17), repeat=2):
        x, y = F(a, 16), F(b, 16)
        exact = closed_form(x, y)
        actual = tuple(terminal_masses(s, x, y)[0] for s in ('P', 'Q'))
        assert actual == exact
        z = x * y
        A = F(3, 8) * (1 - z)
        B = F(1, 4) * (1 - x) + F(3, 8) * z
        assert risk(x, y) == max(A, B)
        assert risk(x, y) >= (A+B)/2 == F(3, 16)+F(1, 8)*(1-x)
        checked += 1
    optimum = (F(1), F(1, 2))
    action_local = (F(1, 2), F(1))
    observer_local = (F(1, 4), F(1))
    assert risk(*optimum) == F(3, 16)
    assert risk(*action_local) == F(5, 16)
    assert risk(*observer_local) == F(9, 32)
    assert risk(*action_local) - risk(*optimum) == F(1, 8)
    assert risk(*observer_local) - risk(*optimum) == F(3, 32)
    for source in ('P', 'Q'):
        c00 = terminal_masses(source, F(0), F(0))[0]
        c10 = terminal_masses(source, F(1), F(0))[0]
        c11 = terminal_masses(source, F(1), F(1))[0]
        coeffs = (c00, c10-c00, c11-c10)
        expected = ((F(0), F(0), F(3, 8)) if source == 'P'
                    else (F(1, 4), -F(1, 4), F(3, 8)))
        assert coeffs == expected
        for a, b in product(range(17), repeat=2):
            x, y = F(a, 16), F(b, 16)
            assert terminal_masses(source, x, y)[0] == c00+(c10-c00)*x+(c11-c10)*x*y
    x_star = F(1, 4)
    assert F(3, 8)*(1-x_star) == F(1, 4)+F(1, 8)*x_star == F(9, 32)
    print('SOURCE_POSITIVE_THIRD_LEVEL_LAWS', THIRD_ZERO)
    print('ORIGINAL_TERMINAL_P',orig_p,'ORIGINAL_TERMINAL_Q',orig_q)
    print('EXACT_ORDERED_POLICY_COMPARISONS',checked,'TWO_SOURCES_EACH')
    print('GLOBAL_OPTIMAL_COINS',optimum,'VALUE',risk(*optimum))
    print('STAGE279_LOCAL_ACTION_COINS',action_local,'VALUE',risk(*action_local),'EXCESS',F(1,8))
    print('STAGE281_TWO_PASS_OBSERVER_COINS',observer_local,'VALUE',risk(*observer_local),'EXCESS',F(3,32))
    print('CAUSAL_SIMPLEX_FORMULAS', '(x,z) with 0<=z<=x<=1', 'P=3z/8', 'Q=(1-x)/4+3z/8')
    print('STAGE282B_CAUSAL_SIMPLEX_EXACT_PASS')

if __name__ == '__main__':
    main()
