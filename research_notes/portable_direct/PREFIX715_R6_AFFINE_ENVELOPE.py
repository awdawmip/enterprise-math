#!/usr/bin/env python3
"""Exact convex-envelope exclusion checker for a finite witness / bound family.

All arithmetic is fractions.Fraction. The inputs are certified affine lower
witness curves and certified affine upper curves on one spatial cell.
This checker does not certify the premise validity or frozen BRC kernel.
"""
from fractions import Fraction as Q
import json
from pathlib import Path

def affine(intercept, slope, t):
    return intercept + slope*t

def robust_certificate(witnesses, upper_bounds, t_left, t_right):
    """Exact min_t(max_i witness_i(t) - min_j upper_j(t)) on closed interval."""
    if not witnesses or not upper_bounds or t_left > t_right:
        raise ValueError("Require nonempty curves and ordered time interval")
    lines = [(a-c,b-d) for a,b in witnesses for c,d in upper_bounds]
    candidates = {t_left,t_right}
    for k,(ak,bk) in enumerate(lines):
        for al,bl in lines[k+1:]:
            if bk == bl:
                continue
            t = (al-ak)/(bk-bl)
            if t_left < t < t_right:
                candidates.add(t)
    def gap(t):
        return max(affine(a,b,t) for a,b in lines)
    worst_t = min(sorted(candidates),key=lambda t:(gap(t),t))
    minimum = gap(worst_t)
    return {
      "certified":minimum > 0,
      "min_margin":minimum,
      "minimizer_t":worst_t,
      "critical_point_count":len(candidates),
      "affine_pair_count":len(lines),
      "nonpositive_witness_t":None if minimum > 0 else worst_t,
    }

def as_json(result):
    return {k:(str(v) if isinstance(v,Q) else v) for k,v in result.items()}

def run_checks():
    # Synthetic toy: cell U(t)=10-3t, two attained witness curves.
    lo,hi=Q(0),Q(1,2)
    cell=[(Q(10),Q(-3))]
    w1=(Q(51,5),Q(-4))  # gap 1/5-t
    w2=(Q(99,10),Q(-2)) # gap t-1/10
    combined=robust_certificate([w1,w2],cell,lo,hi)
    assert combined["certified"]
    assert combined["minimizer_t"] == Q(3,20)
    assert combined["min_margin"] == Q(1,20)
    assert not robust_certificate([w1],cell,lo,hi)["certified"]
    assert not robust_certificate([w2],cell,lo,hi)["certified"]

    # Exact failure of the supplied certificate, not the global optimum.
    fail=robust_certificate(
      [(Q(101,10),Q(-4)),(Q(99,10),Q(-2))],cell,lo,hi)
    assert fail["minimizer_t"]==Q(1,10)
    assert fail["min_margin"]==Q(0) and not fail["certified"]

    # Two independently proven upper bounds may be used adaptively.
    bounds=[cell[0],(Q(201,20),Q(-4))]
    both=robust_certificate([w1,w2],bounds,lo,hi)
    assert both["certified"]
    assert both["min_margin"]==Q(3,20)
    assert both["min_margin"] >= combined["min_margin"]
    return {
       "schema":"PREFIX715_R6_AFFINE_ENVELOPE_TEST_V1",
       "scope":"Exact rational affine-envelope lemma; synthetic toy, no new BRC cells certified",
       "t_interval":[str(lo),str(hi)],
       "witnesses":[list(map(str,w)) for w in [w1,w2]],
       "single_upper_bound":[list(map(str,x)) for x in cell],
       "combined":as_json(combined),
       "individual_certification":[robust_certificate([w],cell,lo,hi)["certified"] for w in [w1,w2]],
       "failure_locator":as_json(fail),
       "adaptive_upper_bounds":as_json(both),
       "verification":"ALL_CHECKS_PASS PREFIX715-R6",
       "author_grade":"EXACT_FRACTION_TOY_AND_GENERAL_PROOF / NOT_BRC_GRID_RECOMPUTATION / UNREVIEWED / NOT_ADMITTED",
    }

if __name__=="__main__":
    result=run_checks()
    (Path(__file__).with_name("PREFIX715_R6_RESULTS.json")).write_text(
        json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(result["verification"])
    print("positive toy margin",result["combined"]["min_margin"],
          "at t=",result["combined"]["minimizer_t"])
    print("combined upper bound margin",result["adaptive_upper_bounds"]["min_margin"])
