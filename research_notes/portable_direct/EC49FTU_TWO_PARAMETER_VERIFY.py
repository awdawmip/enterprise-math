#!/usr/bin/env python3
"""EC49FTU two-parameter exact polynomial certificate; standard library only."""
from fractions import Fraction as F
import json

# Sparse bivariate polynomials in (t,theta), exact rational coefficients.
def const(c): return {(0,0):F(c)}
def var(i): return {(1,0):F(1)} if i==0 else {(0,1):F(1)}
def add(*args):
    z={}
    for p in args:
        for mon,c in p.items():
            z[mon]=z.get(mon,F(0))+c
    return {k:v for k,v in z.items() if v}
def scale(p,c): return {k:v*c for k,v in p.items() if v*c}
def neg(p): return scale(p,-1)
def sub(a,b): return add(a,neg(b))
def mul(*args):
    z=const(1)
    for p in args:
        nxt={}
        for (i,j),v in z.items():
            for (k,l),w in p.items():
                key=(i+k,j+l)
                nxt[key]=nxt.get(key,F(0))+v*w
        z={k:v for k,v in nxt.items() if v}
    return z
def deriv(p,i):
    z={}
    for (a,b),v in p.items():
        exp=(a,b)
        n=exp[i]
        if n:
            key=(a-1,b) if i==0 else (a,b-1)
            z[key]=z.get(key,F(0))+n*v
    return {k:v for k,v in z.items() if v}
def ev(p,t,theta):
    return sum(v*t**i*theta**j for (i,j),v in p.items())
T,S=var(0),var(1)
Q=add(scale(mul(T,T,S),3296),scale(mul(T,S),-1992060),scale(T,258300),const(261457875))
A=scale(mul(T,Q),F(1,421954312500))
V=add(scale(mul(T,T,S),109568),scale(mul(T,S),12022416),scale(T,-209018880),scale(S,-88044327),const(-24135965280))
B=scale(mul(add(scale(T,64),const(-441)),V),F(1,35838544379904000))
N=sub(mul(deriv(B,0),A),mul(B,deriv(A,0)))
R2num=sub(mul(deriv(N,0),A),scale(mul(N,deriv(A,0)),2))
# The exact numerator for r_tt is 875*P/(589824*t^3*Q^3).
ps=[
    [11549579342670997976722500000,34230252321280268694000000,33816821063762923200000,12801796518963916800000],
    [42131107190529170303765625,-263865518225915450565262500,-84690274701240897570000,-59022641298932077536000,490066449785192448000],
    [0,-962996735783523892657500,2011045926875081504688000,-94073316394194182707200,435121386935995791360,-1039174690028912640,-2401505839677440],
    [0,0,7337117986922086801200,-721265226914893489920,3459632021600477184,-5657731060875264,855171863150592]
]
P={(i,j):F(v) for j,coeff in enumerate(ps) for i,v in enumerate(coeff) if v}
lhs=scale(mul(R2num,mul(T,T,T),Q,Q,Q),589824)
rhs=scale(mul(P,A,A,A),875)
assert lhs==rhs

negative=sum(-c for c in P.values() if c<0)
base=P[(0,0)]
assert negative==265067023506554183438688464
assert base==11549579342670997976722500000
assert base>negative # P>0 for 0<t<27/64<1 and 0<=theta<=1
# Q>261457875-1992060=259465815>0 on this rectangle.
assert 261457875-1992060==259465815

tt=F(27,64)
def lambda_theta(theta):
    return F(3500)*(862686243742176000-2239375169798320*theta-18989094173841*theta**2)/(F(6561)*(413340200-1327113*theta)**2)
def derivative_at_t(theta):
    return -ev(N,tt,theta)/ev(A,tt,theta)**2

# Verify the all-theta rational identity at t=tt by exact polynomial clearing.
def tsub(p,t):
    z={}
    for (i,j),c in p.items():
        key=(0,j)
        z[key]=z.get(key,F(0))+c*t**i
    return {k:v for k,v in z.items() if v}
N_end=tsub(N,tt)
A_end=tsub(A,tt)
numer=add(const(862686243742176000),scale(S,-2239375169798320),scale(mul(S,S),-18989094173841))
denroot=add(const(413340200),scale(S,-1327113))
left=scale(mul(neg(N_end),denroot,denroot),6561)
right=scale(mul(numer,A_end,A_end),3500)
assert left==right
l0=lambda_theta(F(0));l1=lambda_theta(F(1))
assert l0==F(171167905504400,63545784776721)
assert l1==F(3011497578173713436500,1113761136900667642209)
# Lambda'(theta)>0: 2131469495973983261425 - 29171587292164226979*theta >0
assert 2131469495973983261425>29171587292164226979
assert l0<l1<3

# Direct rational integral tests independent of A,B polynomial expressions.
def direct_integrals(t,theta):
    m=F(187,8)-t
    L=(8*m+173)/480
    U=F(3,4)
    c0=1+(47-m)/945+F(1,27)-m/54
    c1=F(44,45)+F(10,9)
    d0=1-theta*F(24,35)
    d1=theta*F(32,35)
    cc=[c0*d0,c0*d1+c1*d0,c1*d1]
    av=F(16,945)*sum(v*(U**(k+1)-L**(k+1))/(k+1) for k,v in enumerate(cc))
    bm=(47-m)/54
    xmin=(77+6*bm)/105
    length=F(49,64)-xmin
    xbase=1+xmin+bm
    bv=(xbase*length+(1+xbase*theta)*length**2/2+theta*length**3/3)/54
    return av,bv

tests=0
for theta in [F(0),F(1,8),F(1,4),F(1,2),F(3,4),F(7,8),F(1)]:
    assert lambda_theta(theta)==derivative_at_t(theta)
    for j in range(1,32):
        t=tt*F(j,32)
        assert (ev(A,t,theta),ev(B,t,theta))==direct_integrals(t,theta)
        tests+=1

print(json.dumps({
 "schema":"EC49FTU_TWO_PARAMETER_PHASE_CERT_V1",
 "pin":"fc0f038e7bfd12c886b4d37f900bfb770c0f61ab",
 "baseline":"h_theta=(1+a+b)(1+theta*(a-a_c(b)))",
 "domain":"0<=theta<=1, lambda>=0, 1469/64<m<187/8",
 "lambda_theta":"3500*(862686243742176000-2239375169798320*theta-18989094173841*theta^2)/(6561*(413340200-1327113*theta)^2)",
 "exact_fosd_condition":"0<=lambda<=lambda_theta",
 "lambda0":str(l0),"lambda1":str(l1),
 "lambda_monotone":"strictly increasing on [0,1]",
 "second_derivative_polynomial_identity":True,
 "P_negative_coefficient_sum":str(negative),"P_positive_constant":str(base),
 "joint_curvature_domain_proof":"0<t<27/64<1 and 0<=theta<=1: P>base-negative>0, Q>=259465815>0",
 "independent_exact_integral_regressions":tests,
 "native_BRC_rerun":False,
 "independent_review":False,
 "status":"AUTHOR_PROVED_EXACT_RATIONAL_CHECKED_PARENT_DEPENDENT_NOT_REVIEWED"
},indent=2))
