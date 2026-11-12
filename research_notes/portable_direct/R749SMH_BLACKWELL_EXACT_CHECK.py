"""R749SMH: exact Blackwell noncomparability witness check."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import R749SMG_FEEDBACK_NOISE_EXACT_CHECK as g

pi_plus=[F(1+F(x*(y-t),4),8) for x,y,t in g.H]
pi_minus=[F(1-F(x*(y-t),4),8) for x,y,t in g.H]
assert min(pi_plus+pi_minus)==F(1,16)
assert sum(pi_plus)==sum(pi_minus)==1

contrasts=[]
for eb,ec in product(g.E,g.E):
    if eb==F(1,2):continue
    eps=(F(1,2),eb,ec)
    fb=g.matrix(eps)
    old=g.post(eps)
    assert all(sum(M[i][j] for i in range(8))==1 for M in (fb,old) for j in range(8))
    assert g.tv(g.mult(fb,g.py),g.mult(fb,g.pt))==abs(1-2*eb)/8
    assert g.tv(g.mult(old,g.py),g.mult(old,g.pt))==0
    assert g.tv(g.mult(fb,pi_plus),g.mult(fb,pi_minus))==0
    measured=g.tv(g.mult(old,pi_plus),g.mult(old,pi_minus))
    assert measured==abs(1-2*eb)/8,(eps,measured)
    contrasts.append((str(eb),str(ec),str(measured)))

result={"status":"PASS",
        "input_pin":"a72226e2430ffa4786321ac86e7f0c599d5f0389",
        "domain_checked":"epsilon_A=1/2, epsilon_B!=1/2, epsilon_C in 0,1/4,1/2,3/4,1",
        "case_count":len(contrasts),
        "witness_y_t":{"feedback_TV":"abs(1-2*epsilon_B)/8","postprocessing_TV":"0"},
        "witness_x_selector":{"feedback_TV":"0","postprocessing_TV":"abs(1-2*epsilon_B)/8"},
        "min_positive_prior_atom":"1/16",
        "checks":[{"epsilon_B":b,"epsilon_C":c,"TV_for_x_selector":v} for b,c,v in contrasts]}
print(json.dumps(result,indent=2))
Path(__file__).with_name("R749SMH_BLACKWELL_EXACT_RESULTS.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
