#!/usr/bin/env python3
"""EC49FTW exact rational certificate; external price-prior postprocessing."""
from fractions import Fraction as F
from math import comb
import json

T=F(27,64)
DA=F(221526014062500)
DB=F(8670060656386375680000)

def plus(*ps):
    o={}
    for p in ps:
        for ij,v in p.items(): o[ij]=o.get(ij,F(0))+v
    return {ij:v for ij,v in o.items() if v}
def times(p,q):
    o={}
    for (i,j),v in p.items():
        for (k,l),w in q.items(): o[(i+k,j+l)]=o.get((i+k,j+l),F(0))+v*w
    return {ij:v for ij,v in o.items() if v}
def scale(p,c): return {ij:v*c for ij,v in p.items() if v*c}
def diff(p): return {(i-1,j):i*v for (i,j),v in p.items() if i>0}
def eval_t(p,tt):
    o={}
    for (i,j),v in p.items(): o[(0,j)]=o.get((0,j),F(0))+v*tt**i
    return {ij:v for ij,v in o.items() if v}
def val(p,tt,ee): return sum(v*tt**i*ee**j for (i,j),v in p.items())

a={(1,0):F(137265384375),(2,0):F(135607500),
   (3,1):F(10624320),(4,1):-F(31616)}
c={(0,0):F(5838972720537600),(1,0):F(50565847449600),
   (0,1):F(103568717259),(1,1):-F(29177039808),
   (2,1):F(1924780032),(3,1):F(18612224)}
b=times({(0,0):F(441),(1,0):-F(64)},c)
ap=diff(a); bp=diff(b); app=diff(ap); bpp=diff(bp)
N=plus(times(bpp,times(a,a)),
       scale(times(b,times(app,a)),-1),
       scale(times(bp,times(a,ap)),-2),
       scale(times(b,times(ap,ap)),2))
assert N
counts=[]
for j in range(4):
    coeff={i:v for (i,k),v in N.items() if k==j}
    d=max(coeff)
    cp=[coeff.get(i,F(0))*T**i for i in range(d+1)]
    bern=[sum((cp[i]*F(comb(k,i),comb(d,i)) for i in range(k+1)),F(0))
          for k in range(d+1)]
    assert all(v>=0 for v in bern)
    counts.append([j,d,sum(1 for v in bern if v>0),
                      sum(1 for v in bern if v==0)])
assert counts==[[0,3,4,0],[1,6,7,0],[2,8,7,2],[3,9,6,4]], counts
N_lam=scale(plus(times(eval_t(b,T),eval_t(ap,T)),
                 scale(times(eval_t(bp,T),eval_t(a,T)),-1)),DA/DB)
D_lam=times(eval_t(a,T),eval_t(a,T))
P={(0,0):F(8116152181126391808000000),
   (0,1):F(464097831859863824000),
   (0,2):F(5242065851199447)}
Q=times({(0,0):F(1157352560000),(0,1):F(15916473)},
        {(0,0):F(1157352560000),(0,1):F(15916473)})
assert times(scale(N_lam,F(19683)),Q)==times(scale(P,F(8750)),D_lam)

def Lambda(e): return F(8750)*val(P,F(0),e)/(F(19683)*val(Q,F(0),e))
assert Lambda(F(0))==F(171167905504400,63545784776721)
assert Lambda(F(4019))<3<Lambda(F(4020))
assert Lambda(F(3))>Lambda(F(0))
a2,b1,c0=(30908950173645923529,
           1885376222457017973760000,
          -8077734137777523206400000000)
for e in (F(0),F(4019),F(4020),F(10000)):
    assert (Lambda(e)>=3)==(a2*e**2+b1*e+c0>=0)
for e in (F(0),F(1),F(10000)):
    for tt in (F(1,128),F(1,8),T):
        assert val(a,tt,e)>0 and val(b,tt,e)>0
        assert (DA/DB)*val(b,tt,e)/val(a,tt,e)>0

cert={
  "schema":"EC49FTW_NONAFFINE_QUADRATIC_FIBER_V1",
  "scientific_pin":"fc0f038e7bfd12c886b4d37f900bfb770c0f61ab",
  "parent":"EC49FTV PR2805@9d75e96c7273bfcac61530d5401b0e5885cd4fd9",
  "scope":"external price-prior postprocessing, NOT native Bellman dynamics",
  "eta_domain":"[0,infinity)",
  "lambda_domain":"[0,infinity)",
  "FOSD_iff":"0<=lambda<=Lambda(eta)",
  "Lambda_formula":"8750*(5242065851199447*eta^2+464097831859863824000*eta+8116152181126391808000000)/(19683*(15916473*eta+1157352560000)^2)",
  "Lambda_eta0":str(Lambda(F(0))),
  "Lambda_eta1":str(Lambda(F(1))),
  "Lambda_eta4000":str(Lambda(F(4000))),
  "Lambda_eta4020":str(Lambda(F(4020))),
  "Lambda_limit_eta_infinity":str(F(8750*5242065851199447,19683*15916473**2)),
  "curvature_Bernstein_counts_eta_powers":[
      {"eta_power":j,"t_degree":d,"positive":p,"zero":z}
      for j,d,p,z in counts],
  "curvature_all_eta_nonnegative":True,
  "fixed_lambda3_critical_polynomial":"30908950173645923529*eta^2+1885376222457017973760000*eta-8077734137777523206400000000",
  "lambda3_critical_eta_bracket":["4019","4020"],
  "native_Bellman_rerun":False,
  "independent_review":False,
  "status":"AUTHOR_PROVED_EXACT_FRACTION_CHECKED_PARENT_DEPENDENT_NOT_REVIEWED"
}
print(json.dumps(cert,indent=2,ensure_ascii=False))
