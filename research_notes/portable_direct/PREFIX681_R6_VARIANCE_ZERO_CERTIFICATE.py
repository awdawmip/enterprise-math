#!/usr/bin/env python3
"""PREFIX-681-R6. Exact diagonal-edge variance-zero / quotient-pole certificate.
Frozen source: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Execute from repo root or the research_notes/portable_direct directory.
Uses the identical 189-row immutable kernel already published in PREFIX-676.
"""
from fractions import Fraction as Q
from PREFIX676_R6_STOCHASTIC_ORDER_AND_DIAGONAL_CROSSING import frozen_rows, tail, moments
import json

SCIENCE_PIN = "f42f2906d77f24085c123f3ccfe9667d41caa96d"

def exact_gap(rows, z):
    e = tail(rows, 0, 1)
    t = tail(rows, z.numerator, z.denominator)
    mu_edge, var_edge = moments(e, t)
    mu_diag, var_diag = moments(t, t)
    return var_diag - var_edge, mu_diag - mu_edge

def main():
    rows, monotonic_comparisons = frozen_rows()
    assert len(rows) == 190 and not rows[189]
    assert sum(map(len, rows)) == 9529
    left, right = Q(2663,50000), Q(5327,100000)
    al, bl = exact_gap(rows, left)
    ar, br = exact_gap(rows, right)
    # The signs and integer floors are exact Fraction comparisons.
    assert al > 0 and ar < 0 and bl > 0 and br > 0
    assert (al*10**6).__floor__() == 803
    assert (ar*10**6).__floor__() == -16179
    assert (bl*10**6).__floor__() == 7930886
    assert (br*10**6).__floor__() == 7932168
    ac, bc = exact_gap(rows, Q(53,1000))
    assert ac > 0 and 18*ac > bc
    assert right - left == Q(1,100000)
    # PREFIX-680, exact center jet and global 3rd derivative:
    # B(53/1000) > 789/100, B'(53/1000) > 0,
    # |B''(53/1000)| < 1000, |B'''| <= 69527880576.
    radius = Q(1,2000)
    B_lower = Q(789,100)-Q(1000,2)*radius**2-Q(69527880576,6)*radius**3
    assert B_lower == Q(402586093,62500000)
    assert B_lower > 6
    assert Q(53,1000) < left < right < Q(107,2000)
    obj = {
      "result": "ALL_CHECKS_PASS PREFIX681-R6",
      "frozen_science_pin": SCIENCE_PIN,
      "survivor_rows": 189, "occupied_cells": 9529,
      "predecessor_normalized_Bernstein_comparisons": monotonic_comparisons,
      "root_bracket_left": str(left), "root_bracket_right": str(right),
      "root_bracket_width": str(right-left),
      "left_exact_sign_A": "+", "right_exact_sign_A": "-",
      "left_exact_floor_A_1e6": 803, "right_exact_floor_A_1e6": -16179,
      "left_exact_floor_B_1e6": 7930886, "right_exact_floor_B_1e6": 7932168,
      "center_F18_sign": "+", "crossing_existence_all_real_q_from": "18",
      "inherited_center_jet_source": "PREFIX-680-R6",
      "uniform_B_lower_on_53_over_1000_to_107_over_2000": str(B_lower),
      "conclusion": "at least one A-zero; at its point D_q<-6q for all q>0; B/A has a pole",
      "not_claimed": "unique A-zero, global crossover uniqueness, full 2D maximum",
      "mathematical_status": "AUTHOR_DERIVED / EXACT_RATIONAL_REPLAY_CHECKED / UNREVIEWED / NOT_ADMITTED",
    }
    print(json.dumps(obj,indent=2,ensure_ascii=False))
if __name__=="__main__":
    main()
