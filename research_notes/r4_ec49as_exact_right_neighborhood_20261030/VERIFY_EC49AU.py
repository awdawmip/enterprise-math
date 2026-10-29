"""EC49AU exact endpoint dual and single-price obstruction.
Run next to the EC49AS VERIFY.py; Python 3.8+ stdlib only.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import contextlib, io, json, runpy
with contextlib.redirect_stdout(io.StringIO()):
    old = runpy.run_path(str(Path(__file__).with_name("VERIFY.py")))
high, cut = old["high"], old["v5"]
Z, C2, L = F(0), F(13, 16), F(11, 172)
E0, E1, ET = F(9, 25), F(75, 206), F(11, 30)
W = ((Z,F(3,16),F(1,4),Z,F(9,16)), (F(1),Z,Z,Z,Z), (Z,F(1),Z,Z,Z))
X = ((Z,F(11,16),Z,Z,F(5,16)), (F(1),Z,Z,Z,Z), (Z,F(1),Z,Z,Z))
assert len(high) == 24 and len(cut) == 144 and len(high | cut) == 168

def score(x, e, c, u):
    q = [x[w][c]*(F(1,2)+(2*u-1)*(1-w)*e)/3 for w in range(3)]
    t = sum(q, Z)
    v = sum((max(Z, (43*y-16*t)/172) for y in q), Z)
    return t, v

def dual(x, e, lam):
    return lam*C2 + sum((max(Z, v-lam*t) for c,u in product(range(4),range(2)) for t,v in [score(x,e,c,u)]), Z)

def envelope(x, e):
    return sum((score(x,e,c,u)[1] for c,u in product(range(4),range(2))),Z)

def target(e):
    return F(77,688)+(674*e-175)/16512

def extremal(e, lam):
    a=[dual(x,e,lam) for x in high]
    b=[dual(x,e,lam) for x in cut]
    return dict(eta=str(e), lambda_value=str(lam), high_max=str(max(a)), cut_max=str(max(b)),
                high_ties=sum(y==max(a) for y in a),cut_ties=sum(y==max(b) for y in b),
                max_dual=str(max(a+b)), witness=str(target(e)))

ends=[extremal(e,L) for e in (E0,E1)]
assert [(r["high_max"],r["cut_max"],r["max_dual"]) for r in ends] == [
    ("47723/412800","47891/412800","47891/412800"),
    ("98797/850368","98797/850368","98797/850368")]
for e in (E0,E1,ET):
    assert envelope(W,e) == target(e)
    assert sum((score(W,e,c,u)[0] for c,u in product(range(4),range(2))),Z) == C2
    t,v=score(W,e,1,1)
    assert t>0 and v==L*t
# X and W have affine leaf-score signs throughout the obstruction interval.
for x in (X,W):
    for c,u in product(range(4),range(2)):
        for z in range(3):
            def d(e):
                q=[x[w][c]*(F(1,2)+(2*u-1)*(1-w)*e)/3 for w in range(3)]
                return (43*q[z]-16*sum(q,Z))/172
            assert d(E1)*d(ET)>=0
assert envelope(X,E1)==F(801,6592) and envelope(X,ET)==F(39,320)
assert envelope(X,ET)-L/F(12)-target(ET)==F(1,3870)
assert (envelope(X,ET)-envelope(X,E1))/(ET-E1)-F(337,8256)==F(103,1032)
# For all eta in (E1, ET], no scalar lambda>=0 gives equality:
# lambda<=L: dual(X)>=envelope(X)-lambda/12>target;
# lambda>L: dual(W)>target because V(1,1)=L*T(1,1).
assert sum((score(X,E1,c,u)[0] for c,u in product(range(4),range(2))),Z)==F(43,48)
# Exact conditional purchase optimization at each first-stage vertex.
# Fractional knapsack exchange: rank V/T and fill at unit purchase probability.
def greedy(x,e):
    fs=[(t,v) for c,u in product(range(4),range(2)) for t,v in [score(x,e,c,u)] if t>0]
    fs.sort(key=lambda z:z[1]/z[0],reverse=True)
    remaining, val=C2,Z
    for t,v in fs:
        p=min(F(1),remaining/t)
        val+=p*v
        remaining-=p*t
    assert remaining==0
    return val
high_best=max(greedy(x,ET) for x in high)
cut_best=max(greedy(x,ET) for x in cut)
assert high_best==F(162689,1444800) and cut_best==target(ET)
assert high_best<cut_best
# At eta=11/30, exact minimax over every nonnegative scalar price.
LM=F(1473,22532)
star=extremal(ET,LM)
assert star["max_dual"]=="209867/1802560"
assert dual(X,ET,LM)==dual(W,ET,LM)==F(209867,1802560)
# Global lower bound on dual for arbitrary lambda: two affine minorants.
assert envelope(X,ET)==F(39,320)
t0,v0=score(W,ET,1,1)
assert (target(ET)-v0,t0)==(F(227,2064),F(71,720))
assert F(39,320)-LM/12==F(227,2064)+F(71,720)*LM
assert F(209867,1802560)-target(ET)==F(71,506970)
print(json.dumps({"schema":"EC49AU_EXACT_SINGLE_PRICE_DUAL_V1",
 "classification":"AUTHOR_EXACT_FRACTION_CHECK_PASS_UNREVIEWED_NOT_ADMITTED",
 "model":"auxiliary positive 18+18-leaf causal BRC; C1=43/48, C2=13/16, k=177/172",
 "vertices_original_high":len(high),"vertices_paid_cut":len(cut),
 "all_real_new_eta_interval":"9/25 <= eta <= 75/206",
 "new_optimum":"77/688+(674*eta-175)/16512",
 "certificate_lambda":str(L),"endpoint_certificates":ends,
 "fixed_price_sharp_failure":"For 75/206 < eta <= 11/30, every lambda>=0 yields U_lambda>legal witness line (not a true policy-transition claim)",
 "eta_test":str(ET),"test_witness":str(target(ET)),
 "vertex_restricted_high_best":str(high_best),"vertex_restricted_cut_best":str(cut_best),
 "minimax_lambda":str(LM),"minimax_dual":star,"minimax_gap":str(F(71,506970)),
 "scope":"Exact Fraction tests; all-real coverage by convexity of fixed-lambda upper bound; scalar-price optimality via two supporting affine lower bounds"},sort_keys=True,indent=2))
