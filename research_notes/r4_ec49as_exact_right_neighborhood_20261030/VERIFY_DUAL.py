"""EC49AT purchase-aware exact dual on [175/674,9/25].
Run beside VERIFY.py: python3 VERIFY_DUAL.py > DUAL_REPORT.json
"""
from fractions import Fraction as F
from itertools import product
import contextlib,io,runpy,json
with contextlib.redirect_stdout(io.StringIO()):
    src=runpy.run_path(__file__.replace('VERIFY_DUAL.py','VERIFY.py'))
high=src['high'];cut=src['v5'];W=src['W'];delta=src['delta'];witness=src['witness']
LAMBDA=F(3,50); C2=F(13,16); ETA0=F(175,674); ETA1=F(9,25)
def fiber(x,e,c,u):
    T=sum((x[w][c]*(F(1,2)+(2*u-1)*(1-w)*e)/3 for w in range(3)),F(0))
    V=sum((max(F(0),delta(x,e,c,u,z)[0]) for z in range(3)),F(0))
    return T,V
def dual(x,e):
    return LAMBDA*C2 + sum((max(F(0),V-LAMBDA*T) for c,u in product(range(4),range(2)) for T,V in [fiber(x,e,c,u)]),F(0))
reports=[]
for e in (ETA0,ETA1):
    h=[dual(x,e) for x in high]
    b=[dual(x,e) for x in cut]
    line=F(77,688)+(674*e-175)/16512
    assert max(h+b)==line
    assert witness(e)[2]==line
    reports.append(dict(eta=str(e),dual_lambda=str(LAMBDA),max_high=str(max(h)),max_boundary=str(max(b)),ties_high=sum(v==line for v in h),ties_boundary=sum(v==line for v in b),H=str(line),witness_alpha=str(witness(e)[0]),witness_beta=str(witness(e)[1]),vertices=len(h)+len(b)))
assert all(src['mass'](x)>=C2 for x in high|cut)
print(json.dumps(dict(schema='EC49AT_PURCHASE_AWARE_DUAL_V1',status='AUTHOR_FRACTION_CERT_PASS_UNREVIEWED_NOT_ADMITTED',C1='43/48',C2='13/16',k='177/172',lambda_value='3/50',global_optimum='77/688+(674*eta-175)/16512',all_real_eta_interval='175/674 <= eta <= 9/25',endpoint_certificates=reports,method='fixed lambda legal-cost dual convex in both x and eta; 168 vertices at two endpoints; legal witness attains'),indent=2,sort_keys=True))
