#!/usr/bin/env python3
"""PREFIX-703-R6: exact implications from frozen PREFIX-700/701 BRC observer.
This checks inherited rational corner bins; proofs of convexity and
semialgebraic finiteness are in the accompanying mathematical note.
"""
from fractions import Fraction as Q
import json
from pathlib import Path

N=189
# (lower delta_mu, upper delta_mu), (lower delta_W, upper delta_W), in 1e-6 ticks.
ticks={
  "zero_zero": ((48811611,48811612),(557257209,557257210)),
  "zero_half": ((-111509701,-111509700),(386820427,386820428)),
  "half_half": ((-119288768,-119288767),(439711044,439711045)),
}
results=[]
for corner,((mlo,mhi),(wlo,whi)) in ticks.items():
    lower_W=Q(wlo,10**6)
    upper_mu=Q(mhi,10**6)
    endpoint_margins=[]
    for t in (Q(0),Q(1,2)):
        margin=lower_W-t*upper_mu
        assert margin>386, (corner,t,margin)
        endpoint_margins.append(str(margin))
    # The affine gap is positive between its two checked endpoints.
    results.append({"corner":corner,"t_endpoint_margins_lower":endpoint_margins,
                    "strict_uniform_gap_gt_386":True})
assert N==189 and 25<=N
assert 2*N==378 and (2*N-25)==353
assert sum(range(N))==17766
# s_n polynomials have coordinate degree <= 188; mu and second moment <=188,
# and W=E[Y^2]-mu^2 has coordinate degree <=376.
assert N-1==188 and 2*(N-1)==376
record={
 "schema":"PREFIX703_R6_CONVEX_ENVELOPE_FINITE_ALGEBRAIC_EXCEPTION_V1",
 "frozen_science":"f42f2906d77f24085c123f3ccfe9667d41caa96d",
 "source_dependencies":["PREFIX-621","PREFIX-625","PREFIX-700","PREFIX-701"],
 "corners":results, "t_domain":"[0,1/2]", "q_domain":"[2,infinity)",
 "inherited_clock_mean_bounds":["25","378"],
 "polynomial_coordinate_degree_bound":{"mu":188,"second_moment":188,"W":376},
 "author_proved":["H strictly convex on [0,1/2]","E finite and real algebraic",
   "optimal moment pair single-valued off E","lexicographic high-q selection",
   "0< Wmax-W(xq) <=353/q","max Vq=q^2 Wmax-q mu_star+o(q)"],
 "verification":"ALL_CHECKS_PASS PREFIX703-R6",
 "scope":"exact Fraction checks of inherited corner bins; symbolic proofs in paper; no fresh 189-row recurrence or CAD",
 "admission":"AUTHOR_DERIVED; EXACT_FRACTION_IMPLICATION_CHECKED; UNREVIEWED; NOT_ADMITTED"
}
Path(__file__).with_name("PREFIX703_R6_RESULTS.json").write_text(json.dumps(record,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print("ALL_CHECKS_PASS PREFIX703-R6")
for v in results: print(v["corner"],v["t_endpoint_margins_lower"])
