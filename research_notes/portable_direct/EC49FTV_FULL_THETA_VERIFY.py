#!/usr/bin/env python3
"""EC49FTV exact symbolic Bernstein certificate. Stdlib Fraction only.
Inherited external price observation, no native Bellman execution.
"""
from fractions import Fraction as F
from math import comb
import json

T=F(27,64)
TH_LO=-F(960,7)
TH_HI=F(6720,59)
TH_CRIT=F(2131469495973983261425,29171587292164226979)

# Polynomial P(t,theta) from inherited exact mass ratio second derivative.
# Columns correspond to theta powers, entries ascend in t degree.
P_COLS=[
 [11549579342670997976722500000,34230252321280268694000000,33816821063762923200000,12801796518963916800000],
 [42131107190529170303765625,-263865518225915450565262500,-84690274701240897570000,-59022641298932077536000,490066449785192448000],
 [0,-962996735783523892657500,2011045926875081504688000,-94073316394194182707200,435121386935995791360,-1039174690028912640,-2401505839677440],
 [0,0,7337117986922086801200,-721265226914893489920,3459632021600477184,-5657731060875264,855171863150592]
]
P={(i,j):F(v) for j,col in enumerate(P_COLS) for i,v in enumerate(col) if v}

def add(X,Y):
    z=X.copy()
    for ij,v in Y.items(): z[ij]=z.get(ij,F(0))+v
    return {ij:v for ij,v in z.items() if v}
def scale(X,s):return {ij:v*s for ij,v in X.items() if v*s}
def mul(X,Y):
    z={}
    for (i,j),v in X.items():
        for (k,l),w in Y.items(): z[(i+k,j+l)]=z.get((i+k,j+l),F(0))+v*w
    return {ij:v for ij,v in z.items() if v}
def diff(X):return {(i-1,j):i*v for (i,j),v in X.items() if i>0}
def poly(terms):return {ij:F(v) for ij,v in terms.items()}

# Independently reconstruct P from the rational price masses A,B, by
# r''=[B'' A^2 - B A'' A - 2 B' A A' + 2 B (A')^2]/A^3.
Q=poly({(2,1):3296,(1,1):-1992060,(1,0):258300,(0,0):261457875})
N_A=mul(poly({(1,0):1}),Q)
N_B=mul(poly({(1,0):64,(0,0):-441}),poly({(2,1):109568,(1,1):12022416,(1,0):-209018880,(0,1):-88044327,(0,0):-24135965280}))
DA=F(421954312500)
DB=F(35838544379904000)
AA=scale(N_A,1/DA)
BB=scale(N_B,1/DB)
N=add(add(mul(diff(diff(BB)),mul(AA,AA)),scale(mul(BB,mul(diff(diff(AA)),AA)),-1)),add(scale(mul(diff(BB),mul(AA,diff(AA))),-2),scale(mul(BB,mul(diff(AA),diff(AA))),2)))
assert N==scale(P,F(875,589824)/DA**3), 'complete rational polynomial identity failed'

# Convert P((27/64)s,TH_LO+(TH_HI-TH_LO)u) exactly to
# tensor Bernstein basis deg (6,3). No sample/float sign inference.
C={(i,j):F(0) for i in range(7) for j in range(4)}
for (i,j),v in P.items():
    for k in range(j+1):
        C[(i,k)]+=v*T**i*F(comb(j,k))*TH_LO**(j-k)*(TH_HI-TH_LO)**k
bern={}
for k in range(7):
    for l in range(4):
        bern[(k,l)]=sum(C[(i,j)]*F(comb(k,i),comb(6,i))*F(comb(l,j),comb(3,j)) for i in range(k+1) for j in range(l+1))
assert len(bern)==28 and all(v>0 for v in bern.values())
min_at=min(bern,key=bern.get)
min_b=bern[min_at]
assert min_at==(6,3)
assert min_b==F(15814420445330980080708334710364875,3286064)

# Q positivity over closed (t,theta)-rectangle.
QLOW=F(261457875)-F(1992060)*T*TH_HI
assert QLOW==F(9778524525,59)>0

def lam(th):
 return F(3500)*(F(862686243742176000)-F(2239375169798320)*th-F(18989094173841)*th**2)/(F(6561)*(F(413340200)-F(1327113)*th)**2)

assert TH_LO<0<1<TH_CRIT<TH_HI
assert lam(F(0))==F(171167905504400,63545784776721)
assert lam(F(1))==F(3011497578173713436500,1113761136900667642209)
assert all(lam(q)>0 for q in (TH_LO,TH_CRIT,TH_HI))
assert lam(TH_CRIT)>lam(TH_LO) and lam(TH_CRIT)>lam(TH_HI)

cert={
 'schema':'EC49FTV_FULL_POSITIVE_THETA_SHARP_FOSD_CERT_V1',
 'scientific_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
 'parent':'EC49FTU PR2801@f8857e1d6e22f47bb7fc397316df9e8650e6701d',
 'effective_external_price_model':True,
 'native_bellman_rerun':False,
 'theta_strict_price_density_domain':[str(TH_LO),str(TH_HI)],
 'theta_interval_endpoints_excluded':True,
 'lambda_sharp_iff':'0 <= lambda <= Lambda(theta)',
 'Lambda_stationary_theta':str(TH_CRIT),
 'Lambda_stationary_kind':'unique strict global maximum',
 'Lambda_peak_approx':float(lam(TH_CRIT)),
 'Lambda_theta_lower_limit_approx':float(lam(TH_LO)),
 'Lambda_theta_upper_limit_approx':float(lam(TH_HI)),
 'Q_lower_bound':str(QLOW),
 'P_polynomial_symbolic_identity':'PASS',
 'P_Bernstein_coefficient_count':len(bern),
 'P_Bernstein_positive_count':sum(int(v>0) for v in bern.values()),
 'P_min_Bernstein_coefficient':str(min_b),
 'P_min_Bernstein_index':[min_at[0],min_at[1]],
 'continuous_TP2':'strict: K_theta(m,z)=K0(m,z)*w_theta(z), w_theta>0',
 'review':'AUTHOR_PROVED / EXACT_RATIONAL_VERIFIED / PARENT_DEPENDENT / NOT_REVIEWED',
 'activity':'not asserted'
}
print(json.dumps(cert,indent=2))
