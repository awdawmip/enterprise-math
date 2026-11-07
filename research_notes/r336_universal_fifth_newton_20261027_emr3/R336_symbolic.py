#!/usr/bin/env python3
"""R336 exact symbolic fifth-highest Newton coefficient conditional on R330.
Original complete signed 12-step BRC K/J recurrence, no truncation of its signed tails.
"""
import sympy as S
from math import comb
import json, time

def C(n,k):return comb(n,k) if 0<=k<=n else 0

def add(a,b):
    z=[0]*max(len(a),len(b))
    for i,v in enumerate(a):z[i]+=v
    for i,v in enumerate(b):z[i]+=v
    return z

def term(n,scale,shift): return [0]*shift+[scale*C(n,i) for i in range(n+1)] if n>=0 else [0]
def kernel(i):
    d=(-C(4,i)+C(2,i-1), C(5,i-1)-C(5,i-2), C(7,i-2), -C(9,i-3))
    out=[0]
    for j,v in enumerate(d,1):
        if v:out=add(out,term(i+1-j,-v,i-1))
    return out
def forcing(i):
    out=[0]
    for v,n in ((-C(3,i-1),i),(-C(6,i-1),i-1),(C(8,i-2),i-2)):
        if v:out=add(out,term(n,v,i))
    return out

def series(poly,x):return sum(S.Integer(v)*x**i for i,v in enumerate(poly))

def timed(label):print(time.strftime('%H:%M:%S'),label,flush=True)

y,z,eps,j,r,m,u=S.symbols('y z eps j r m u')
a=S.Rational(4,5);x=(1-y)/2;t=y*z
K=sum(series(kernel(i),t)*x**i for i in range(1,13))
A=1+t+sum(series(forcing(i),t)*x**i for i in range(1,11))
kpoly=S.Poly(S.expand(K),y); apoly=S.Poly(S.expand(A),y)
E=[S.factor(-kpoly.nth(i+1)) for i in range(6)]
N=[S.factor(apoly.nth(i)) for i in range(5)]
assert all(S.simplify(x-v)==0 for x,v in zip(E[:5],[1-5*z/4,z,z*(11*z*z-16*z+4)/16,z*z*(3*z-8)*(3*z-2)/8,z*z*(9*z**3-308*z*z+392*z-64)/64]))
assert all(S.simplify(x-v)==0 for x,v in zip(N[:4],[1,0,-z*(5*z-2)/2,-z*z*(17*z-18)/4]))
timed('E5='+str(E[5])+' N4='+str(N[4]))

# Use truncated Taylor coefficient arrays in eps=z-a.
T=4
EF=[[S.factor(S.diff(v,z,d).subs(z,a)/S.factorial(d)) for d in range(T+1)] for v in E]
NF=[[S.factor(S.diff(v,z,d).subs(z,a)/S.factorial(d)) for d in range(T+1)] for v in N]
def mul(A,B):return [sum(A[k]*B[i-k] for k in range(i+1)) for i in range(T+1)]
def power(A,n):
    out=[1]+[0]*T
    for _ in range(n):out=mul(out,A)
    return out
jets=[[S.Integer(1)]+[S.Integer(0)]*T]
for kk in range(1,9):
    curr=mul(mul(NF[kk] if kk<len(NF) else [0]*(T+1),power(EF[0],kk)),[1]+[0]*T)
    for ell in range(1,min(kk,5)+1):
        sub=mul(mul(EF[ell],jets[kk-ell]),power(EF[0],ell-1))
        curr=[curr[i]-sub[i] for i in range(T+1)]
    jets.append([S.factor(v) for v in curr])

p=lambda w:-(69*w+11)/80
h=lambda w:(4761*w*w-6685*w-9354)/6400
v=lambda w:-3*(109503*w**3-513636*w**2-391199*w-1307460)/512000
for kk in range(1,9): assert S.factor(jets[kk][1]*(-a)**(1-kk)-p(kk))==0
for kk in range(2,9): assert S.factor(2*jets[kk][2]*(-a)**(2-kk)-h(kk))==0
for kk in range(3,9): assert S.factor(6*jets[kk][3]*(-a)**(3-kk)-v(kk))==0
w_values=[(kk,S.factor(24*jets[kk][4]*(-a)**(4-kk))) for kk in range(4,9)]
w=S.factor(S.interpolate(w_values,j));timed('w_j='+str(w))
assert S.degree(w,j)<=4
for kk,yv in w_values:assert S.factor(w.subs(j,kk)-yv)==0
jetnorm=lambda jj: [1,p(jj)/(-a),h(jj)/(2*(-a)**2),v(jj)/(6*(-a)**3),w.subs(j,jj)/(24*(-a)**4)]
rec=[0]*(T+1)
for ell in range(1,6):
    factor=mul(mul(EF[ell],power(EF[0],ell-1)),jetnorm(j-ell))
    rec=[rec[i]-S.expand(factor[i]*(-a)**(-ell)) for i in range(T+1)]
check=S.factor(S.factorial(4)*(-a)**4*rec[4]-w)
timed('symbolic recurrence diff '+str(check))
assert check==0

# Compute e4 of r shifted factors from the R330 exact extraction formula.
# Shift sets: first i-m for i=1..j, and - (j+i)/2 for i=0..(r-j-1)
n=r-j
sum_power=[]
for kk in range(1,5):
    i=S.symbols('i',integer=True)
    P=S.summation((i-m)**kk,(i,1,j))+S.summation((-(j+i)/2)**kk,(i,0,n-1))
    sum_power.append(S.expand(P))
P1,P2,P3,P4=sum_power
# Newton identity e4=(p1^4-6p1^2 p2+3p2^2+8p1 p3-6p4)/24
e4=S.Poly(S.expand((P1**4-6*P1**2*P2+3*P2**2+8*P1*P3-6*P4)/24),m)
assert e4.degree()<=4
timed('e4 deg_m '+str(e4.degree()))
moments=[S.Integer(1),-p(j),-p(j)+h(j),-p(j)+3*h(j)-v(j),-p(j)+7*h(j)-6*v(j)+w]
W=S.factor(sum(e4.nth(i)*moments[i] for i in range(5)))
timed('W polynomial total degree j '+str(S.degree(W,j))+' in r '+str(S.degree(W,r)))
# Exceptional j=0,1,2,3: raw g_j derivatives, not jet formula extrapolation.
g=[S.Integer(1)]
for kk in range(1,4):
    curr=S.expand(N[kk]*E[0]**kk if kk<len(N) else 0)
    for ell in range(1,kk+1):curr=S.expand(curr-E[ell]*g[kk-ell]*E[0]**(ell-1))
    g.append(S.expand(curr))
for jj in range(4):
    vals=[];expr=g[jj]
    for degree in range(5):
        if degree:expr=S.expand(z*S.diff(expr,z))
        vals.append(S.factor(expr.subs(z,a)/(-a)**jj))
    low=S.factor(sum(e4.nth(k).subs(j,jj)*vals[k] for k in range(5)))
    diff=S.factor(low-W.subs(j,jj))
    timed(f'exceptional j={jj} diff {diff}')
    assert diff==0
# Falling factorial basis conversion W(r,j)=sum_k A_k(r) (j)_k
res=S.expand(W)
falling=[]
for kk in range(S.degree(res,j),-1,-1):
    ck=S.factor(S.Poly(res,j).nth(kk))
    if ck!=0:
        falling.append((kk,ck))
        res=S.expand(res-ck*S.prod(j-l for l in range(kk)))
assert S.factor(res)==0
D=S.factor(sum(ck*S.prod(r-l for l in range(kk))*S.Rational(-2,3)**kk for kk,ck in falling))
timed('D_qr4='+str(D))

# top ratios in q from R333-R335
R=[1,-S.Rational(3,10)*r*(r-1),r*(r-1)*(243*r*r-95*r-3542)/5400,
   -r*(r-2)*(r-1)*(729*r**3+1332*r**2-36437*r+101640)/162000,D]
# coefficient of u^(r-d) when q=u+r
Q=[S.factor(sum(R[t]*S.binomial(r-t,d-t)*r**(d-t) for t in range(d+1))) for d in range(5)]
# near-diagonal Stirling second numbers S(n,n-t)
St=[lambda n:S.Integer(1),lambda n:S.binomial(n,2),
    lambda n:S.binomial(n,3)+3*S.binomial(n,4),
    lambda n:S.binomial(n,4)+10*S.binomial(n,5)+15*S.binomial(n,6),
    lambda n:S.binomial(n,5)+25*S.binomial(n,6)+105*S.binomial(n,7)+105*S.binomial(n,8)]
scaled=S.factor(sum(Q[d]*St[4-d](r-d) for d in range(5)))
F=S.factor(S.expand_func(scaled)/S.prod(r-i for i in range(4)))
timed('c[r,r-4]/6^r='+str(F))
shift=S.Poly(S.expand(F.subs(r,u+4)),u)
timed('shift r=4+u: '+str(shift.as_expr()))
timed('shift coefficients signs '+str([S.sign(c) for c in shift.all_coeffs()]))
assert S.simplify(F*S.prod(r-i for i in range(4))-scaled)==0
# Serialize exact outputs.
obj={
 'schema':'R336_FIFTH_HIGHEST_SYMBOLIC_CERT_V1','status':'PASS',
 'dependency':'R330 author-side exact extraction+degree lemma; not independently admitted',
 'model':'original signed twelve-step BRC K/J auxiliary polynomial model',
 'E5':str(E[5]), 'N4':str(N[4]),
 'normalized_fourth_jet_wj':str(w),'jet_base_j4to8':[[int(k),str(vv)] for k,vv in w_values],
 'universal_jet_recursion':'exact polynomial identity for all j>=9: PASS',
 'exceptional_j_0_to_3':'raw g_j Euler moments agree: PASS',
 'W4_falling':[[int(k),str(vv)] for k,vv in falling],
 'ratio_D_qr4':str(D),'c_r_r_minus_4_scaled_by_6_pow_r':str(F),
 'shifted_r_eq_u_plus_4':str(shift.as_expr()),
 'shifted_coefficients_descending':[str(q) for q in shift.all_coeffs()],
 'arithmetic':'exact rationals only',
 'level':'AUTHOR_SIDE/UNREVIEWED/NOT_ADMITTED',
}
with open('/mnt/data/em_r336/R336_SYMBOLIC_EVIDENCE.json','w') as f:json.dump(obj,f,ensure_ascii=False,indent=2);f.write('\n')
timed('ALL SYMBOLIC PASS')
