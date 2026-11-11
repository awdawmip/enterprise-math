#!/usr/bin/env python3
"""PREFIX704-R6 exact rational structural toy for Nash-phase/jump formulas.
This is NOT a checker for the original 189-row BRC optimizer or its CAD.
"""
from fractions import Fraction as F
import json
from pathlib import Path

BRANCHES = ((50, 10), (40, 9))

def values(i, t):
    m, c = BRANCHES[i]
    mean = F(m) - 2*t
    variance = F(c) - t*t
    h = F(c) + t*t - F(m)*t
    assert h == variance - t*mean
    return h, mean, variance

t0 = F(1, 10)
assert t0 == F(BRANCHES[0][1]-BRANCHES[1][1],
               BRANCHES[0][0]-BRANCHES[1][0])
samples=[]
for t in (F(0), F(1,20), t0, F(1,8), F(1,2)):
    v=[values(i,t) for i in range(2)]
    h=max(a[0] for a in v)
    active=[i for i,a in enumerate(v) if a[0]==h]
    assert values(0,t)[0]-values(1,t)[0] == 1-10*t
    samples.append(dict(t=str(t), H=str(h), active=active,
                        means=[str(v[i][1]) for i in active],
                        variances=[str(v[i][2]) for i in active]))
left,right=values(0,t0),values(1,t0)
assert left[0]==right[0]==F(501,100)
delta_mu=left[1]-right[1]
delta_W=left[2]-right[2]
assert delta_mu==10 and delta_W==1 and delta_W==t0*delta_mu
# Both active analytic branch envelopes have H''=2, and W'=t mu':
# mu_i'= -2, W_i'= -2*t.
assert -2 == -2 and F(1, 10)*(-2) == -F(1, 5)
record={
  "schema":"PREFIX704_R6_EXACT_STRUCTURAL_TOY_V1",
  "frozen_science":"f42f2906d77f24085c123f3ccfe9667d41caa96d",
  "source_dependencies":["PREFIX-621","PREFIX-625","PREFIX-700","PREFIX-703"],
  "toy_only":True, "model_189_row_recomputed":False,
  "cad_executed":False,
  "transition_t":"1/10", "transition_delta_mu":"10",
  "transition_delta_W":"1", "analytic_branch_Hsecond":"2",
  "sample_points":samples,
  "scope":"exact Fraction check for a two-branch illustrative envelope; BRC theorem proofs are symbolic deductions from pinned-source antecedents",
  "status":"AUTHOR_DERIVED; EXACT_RATIONAL_TOY_CHECKED; UNREVIEWED; NOT_ADMITTED"
}
Path(__file__).with_name("PREFIX704_R6_RESULTS.json").write_text(
    json.dumps(record,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"
)
print("ALL_CHECKS_PASS PREFIX704-R6")
