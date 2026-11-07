#!/usr/bin/env python3
"""Exact rational checks for Stage280-B (finite witness domain only)."""
from fractions import Fraction as F
from itertools import product


def tv_two(p, q):
    return abs(p - q)


def minimax_coin(masses, f):
    """Stage279-B formula for strictly positive source masses on one fiber."""
    w = [sum(v) for v in masses]
    u = [sum(v[j] * f[j] for j in range(len(f))) / w[i]
         for i, v in enumerate(masses)]
    d = max((w[i] * w[j] * abs(u[i] - u[j]) / (w[i] + w[j])
             for i in range(len(w)) for j in range(i+1, len(w))), default=F(0))
    x = max([F(0)] + [u[i] - d / w[i] for i in range(len(w))])
    assert 0 <= x <= 1
    assert max(w[i] * abs(u[i] - x) for i in range(len(w))) == d
    return x, d


def exhaust_causal_hybrid():
    # All four deterministic path policies and all 16 deterministic
    # terminal observers F(h,a) over an unequal-ratio non-IID fiber.
    masses = [(F(1,4), F(1,8)), (F(1,8), F(1,4))]
    cases = 0
    for fp in product((F(0), F(1)), repeat=2):
        x, d = minimax_coin(masses, fp)
        for vals in product((F(0), F(1)), repeat=4):
            D = (vals[1] - vals[0], vals[3] - vals[2])
            for mass in masses:
                delta = abs(sum(mass[h] * (fp[h]-x) * D[h] for h in range(2)))
                residual = min(sum(mass[h]*abs(fp[h]-x)*abs(D[h]-g)
                                   for h in range(2)) for g in (F(-1), F(0), F(1)))
                assert delta <= d + residual
            cases += 1
    assert cases == 64
    return cases


def iid_zero_r_nonzero_path_observer():
    outputs = []
    for p0 in (F(1,2), F(1,4)):
        # Two sources have identical within-count path laws, so R_C=0.
        m = p0*(1-p0)  # each word 01 and 10
        masses = [(m,m)]
        f = (F(1),F(0))
        x,d = minimax_coin(masses,f)
        assert x == F(1,2) and d == 0
        actual = m  # F=1_{01 and action=1}
        quotient = m*x
        err = abs(actual-quotient)
        D = (F(1),F(0))
        osc = min(sum(m*abs(f[h]-x)*abs(D[h]-g) for h in range(2))
                  for g in (F(0),F(1,2),F(1)))
        assert err == osc == m/2
        outputs.append(err)
    assert outputs == [F(1,8),F(3,32)]
    return outputs


def noniid_future_kernel_witness():
    # Both sources have prefix weights 1/4 on each two-symbol word.
    # On C={01,10}, history-conditioned continuation kernels differ;
    # state-only next-symbol kernel is exactly the source mixture 1/2.
    observed = []
    for p01,p10 in ((F(3,4),F(1,4)),(F(1,4),F(3,4))):
        mu = F(1,4)
        aggregate = mu*p01 + mu*p10
        compressed_aggregate = (2*mu)*F(1,2)
        assert aggregate == compressed_aggregate == F(1,4)
        original_event = mu*p01 # F=1_{prefix 01 and next symbol=1}
        compressed_event = mu*F(1,2)
        err = abs(original_event-compressed_event)
        transition_tv_budget = mu*tv_two(p01,F(1,2))+mu*tv_two(p10,F(1,2))
        assert err == F(1,16) <= transition_tv_budget == F(1,8)
        observed.append((original_event,compressed_event,err,transition_tv_budget))
    assert observed[0][0]==F(3,16) and observed[1][0]==F(1,16)
    return observed


def main():
    n=exhaust_causal_hybrid()
    path=iid_zero_r_nonzero_path_observer()
    future=noniid_future_kernel_witness()
    print('CAUSAL_HYBRID_EXHAUSTIVE_CASES',n)
    print('IID_ZERO_R_PATH_OBSERVER_ERRORS',*[str(v) for v in path])
    for i,(orig,comp,err,budget) in enumerate(future):
        print('NONIID_KERNEL_SOURCE',i,'original',orig,'quotient',comp,
              'error',err,'transition_budget',budget)
    print('STAGE280_BRC_DAG_RESIDUAL_EXACT_PASS')


if __name__=='__main__':
    main()
