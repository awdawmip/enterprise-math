#!/usr/bin/env python3
"""Exact rational implication checker for PREFIX-684.

Assumes the pinned PREFIX-682 exact 189-level BRC observer jet certificate,
not a new native physical simulation or a replay of that recurrence.
"""
import json
from fractions import Fraction as Q

SCIENCE_PIN = 'f42f2906d77f24085c123f3ccfe9667d41caa96d'
SOURCE = 'enterprise-math@d437f76a2d52b617e938130c9cb9e8e61257c5a9'
FLOORS = {
    'A0': -4562, 'A1': -169792160954, 'A2': -6657264578649,
    'B0': 793095029, 'B1': 12820091523, 'B2': -99474141353,
}
H = -Q(1, 2_000_000)
M3 = {'A': 218571424275456, 'B': 69527880576}


def taylor_interval(prefix):
    terms = [(Q(FLOORS[prefix + str(i)], 10**8),
              Q(FLOORS[prefix + str(i)] + 1, 10**8))
             for i in range(3)]
    factors = [Q(1), H, H*H/2]
    lower = sum(min(lo*factor, hi*factor)
                for (lo, hi), factor in zip(terms, factors))
    upper = sum(max(lo*factor, hi*factor)
                for (lo, hi), factor in zip(terms, factors))
    error = Q(M3[prefix], 6) * abs(H)**3
    return lower - error, upper + error


def main():
    al, au = taylor_interval('A')
    bl, bu = taylor_interval('B')
    assert al > 0 and bl > 0
    assert bl > 9816*au
    assert 9929*al > bu
    def gamma(q):
        return Q(794, 100) * (Q(110_000_000) + Q(36_000, q)) / (1600*q + 100)
    assert gamma(9816) < 56
    assert gamma(9929) < 55
    return {
        'result': 'ALL_CHECKS_PASS PREFIX684-R6',
        'scientific_pin': SCIENCE_PIN,
        'prior_exact_source': SOURCE,
        'left_endpoint': '2663/50000',
        'right_endpoint': '53261/1000000',
        'A_left_enclosure': [str(al), str(au)],
        'B_left_enclosure': [str(bl), str(bu)],
        'q_entry_bound': '9816 < q_c = B(left)/A(left) < 9929',
        'all_real_q_nonnegative': 'crossing in closed I iff q>=q_c; unique',
        'interior_crossing': 'unique for every real q>q_c',
        'branch': 'strictly increasing for real q>q_c; endpoints at q_c+ and infinity',
        'concavity_scope': 'strictly concave for every real q>q_c; z_second<-3144*793/[100*q*(1800*q+150)^2]',
        'sharper_curvature_scope': 'z_second<-3145*793/[100*q*(1800*q+150)^2] for q>=9929',
        'gamma_at_9816': str(gamma(9816)),
        'gamma_at_9929': str(gamma(9929)),
        'prior_189_level_replay': False,
        'status': 'AUTHOR_DERIVED / EXACT_FRACTION_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED',
    }


if __name__ == '__main__':
    print(json.dumps(main(), ensure_ascii=False, indent=2))
