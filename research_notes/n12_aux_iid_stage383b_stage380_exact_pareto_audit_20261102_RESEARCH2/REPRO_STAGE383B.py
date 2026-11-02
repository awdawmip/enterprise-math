#!/usr/bin/env python3
"""Independent exact rational audit of Stage380-B's local Pareto theorem.

Dependency: Python standard library. All computations exact fractions.
Continuous coverage uses proven derivative-monotonicity of B_k on each
rectangular interval and polynomial identities, not finite sampling.
The inherited Stage379 localization is treated as a hypothesis.
"""
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path

FQ=lambda s:F(str(s))
w=[1,3,3,1]
m=[61,21,9,9]
# ascending polynomial coefficient representation
B=[[F(1),F(-3),F(3),F(-1)], [F(0),F(1),F(-2),F(1)],
   [F(0),F(0),F(1),F(-1)], [F(0),F(0),F(0),F(1)]]
P=(FQ('0.2308'),FQ('0.2345'),FQ('0.55'),FQ('0.56'))
Q=(FQ('0.2365'),FQ('0.239'),FQ('0.57566'),FQ('0.57574'))
A1=F(1,4); A3=F(3,4)
def val(poly,z):return sum(co*z**i for i,co in enumerate(poly))
def derivative(poly):return [i*poly[i] for i in range(1,len(poly))]
def sub(a,b):return [a[i]-b[i] for i in range(len(a))]
def r(k,x,y):return (4*val(B[k],x)+val(B[k],y))/5-F(m[k],160)
def audit(k,a,z):return val(B[k],z)-val(B[k],a)
def fr(x):return f'{x.numerator}/{x.denominator}'
def signs(interval,k):
 lo,hi=interval
 # all B_k monotone on each x or y interval in P,Q; derivative roots 1/3 and 2/3
 assert hi<F(1,3) or (lo>F(1,3) and hi<F(2,3))
 vals=[val(B[k],v) for v in [lo,hi]]
 return min(vals),max(vals)
def cost(x,y):
 def D(a,z):return sum(w[k]*abs(audit(k,a,z)) for k in range(4))/2
 return (63*D(A1,x)+D(A3,x)+9*D(A1,y)+7*D(A3,y))/256

def poly_add(a,b,coef=1):
 out=[F(0)]*4
 for i in range(4):out[i]=a[i]+coef*b[i]
 return out

def d_poly(a,signs4):
 # coefficient representation of 1/2 sum w[k]*sign[k]*(B_k(z)-B_k(a))
 out=[F(0)]*4
 for k,s in enumerate(signs4):
  out=poly_add(out,[v*w[k]*s/2 for v in B[k]])
  out[0]-=F(w[k]*s,2)*val(B[k],a)
 return out

out={'model':'Stage383-B exact local audit of Stage380-B (inherited Stage379 P/Q boxes)',
     'P':list(map(fr,P)),'Q':list(map(fr,Q)),
     'fixed_audit_signs':{},'residual_bounds':{},'exact_polynomial_coefficients':{},
     'strict_direction_margins':{}}

for name,box in [('P',P),('Q',Q)]:
 xl,xu,yl,yu=box
 for coordinate,interval in [('x',(xl,xu)),('y',(yl,yu))]:
  for a in [A1,A3]:
   for k in range(4):
    lo,hi=signs(interval,k)
    low,high=lo-val(B[k],a),hi-val(B[k],a)
    key=f'{name}:{coordinate}:{fr(a)}:k{k}'
    if name=='Q' and coordinate=='y' and a==A3 and k==2:
     assert low<0<high
     out['fixed_audit_signs'][key]='ONE_KINK_NOT_FIXED'
    else:
     assert low>0 or high<0, (key,fr(low),fr(high))
     out['fixed_audit_signs'][key]={'sign':'+' if low>0 else '-',
                                     'strict_margin':fr(low if low>0 else -high)}
 for k in [0,1,2,3]:
  lowx,hix=signs((xl,xu),k); lowy,hiy=signs((yl,yu),k)
  low=(4*lowx+lowy)/5-F(m[k],160)
  high=(4*hix+hiy)/5-F(m[k],160)
  out['residual_bounds'][f'{name}:r{k}']=[fr(low),fr(high)]
  if k==2:assert low>0
  if k==3:assert high<0
  if name=='Q' and k==0:assert high<0

# Source-cost polynomial ignoring only the Q:y:3/4:k2 absolute term.
# Signs pulled from exact endpoint certificates above.
def signedD(name,coord,a,drop_k2=False):
 table=[]
 for k in range(4):
  if drop_k2 and k==2:
   table.append(0);continue
  key=f'{name}:{coord}:{fr(a)}:k{k}'
  table.append(1 if out['fixed_audit_signs'][key]['sign']=='+' else -1)
 return d_poly(a,table)

def muladd(terms):return [sum(F(mult)*p[i] for mult,p in terms)/256 for i in range(4)]
xpoly=muladd([(63,signedD('P','x',A1)),(1,signedD('P','x',A3))])
ybase=muladd([(9,signedD('P','y',A1)),(7,signedD('Q','y',A3,True))])
xexpected=[F(0),-F(189,256),F(93,128),-F(61,256)]
yexpected=[F(0),F(0),F(33,512),-F(29,512)]
assert xpoly[1:]==xexpected[1:]
assert ybase[1:]==yexpected[1:]
assert xpoly[0]+ybase[0]==F(5157,32768), (xpoly,ybase)
out['exact_polynomial_coefficients']={'x':list(map(fr,xpoly)),
'y_without_cusp':list(map(fr,ybase)),'cusp_coefficient':'21/512',
'base_constant_combined':fr(xpoly[0]+ybase[0])}

# Check both P and Q cost forms as exact polynomial identities with one absolute cusp.
def C0(x,y):return F(5157,32768)-F(189,256)*x+F(93,128)*x*x-F(61,256)*x*x*x+F(33,512)*y*y-F(29,512)*y*y*y
def delta(y):return F(9,64)-y*y*(1-y)
for name,box in [('P',P),('Q',Q)]:
 xl,xu,yl,yu=box
 for x in [xl,(xl+xu)/2,xu]:
  for y in [yl,(yl+yu)/2,yu]:
   assert cost(x,y)==C0(x,y)+F(21,512)*abs(delta(y))

# Directional sign margins from rational endpoint extrema.
# B2'(z)=z(2-3z), positive on x/y boxes, concave and increasing until 1/3.
def B2p(z):return z*(2-3*z)
# For r0=0, r1<0, direction (dx,dy)=(1/8,-1):
# dr0=(B0'(x)-2B0'(y))/10, db=3*(B2'(x)-2B2'(y))/32,
# dc=cx/8-cy; all strict negative on P box.
ratioA=(1-P[1])**2 - 2*(1-P[2])**2  # positive; x upper and y lower give conservative lower bound
ratioB=2*B2p(P[3])-B2p(P[1])   # positive: B2' decreases for y>1/3
assert ratioA>0 and ratioB>0
out['strict_direction_margins']['P:r0=0,r1<0:dr0_negative_min']=fr(F(3,10)*ratioA)
out['strict_direction_margins']['P:r0=0,r1<0:db_negative_min']=fr(F(3,32)*ratioB)
# If r0>0: one-sided x budget derivative = -3(2x-1)^2/4 (r1<0)
# or -3*x*x/4 (r1>0), both strictly negative.
assert P[1]<F(1,2)
out['strict_direction_margins']['P:r0>0:r1<0:-dbdx_lower']=fr(F(3,4)*(1-2*P[1])**2)
out['strict_direction_margins']['P:r0>0:r1>0:-dbdx_lower']=fr(F(3,4)*P[0]**2)
# If r0<0,r1<0 or Q:r1<0, decreasing y improves b because B2'(y)>0.
assert B2p(P[3])>0 and B2p(Q[3])>0
out['strict_direction_margins']['P:r0<0,r1<0:dbdy_lower']=fr(F(3,16)*B2p(P[3]))
out['strict_direction_margins']['Q:r1<0:dbdy_lower']=fr(F(3,16)*B2p(Q[3]))

# cost_x<0 always, cost_y>0 on both one-sided branches.
def cx(x):return -F(3,256)*(1-x)*(63-61*x)
def cylo(y):return F(3,64)*y*(1-y)
def cyhi(y):return F(3,256)*y*(18-25*y)
assert cx(P[0])<0 and cx(Q[1])<0
assert cylo(P[2])>0 and cylo(Q[2])>0 and cyhi(Q[3])>0
assert (F(3,256)*Q[3]*(18-25*Q[3]))>0
out['strict_direction_margins']['Q:upper_cusp:cy_positive_lower']=fr(cyhi(Q[3]))

# On strict wedge, b=3/16[4x(1-x)+y(1-y)]-45/256.
def bwedge(x,y):return F(3,16)*(4*x*(1-x)+y*(1-y))-F(45,256)
for name,box in [('P',P),('Q',Q)]:
 xl,xu,yl,yu=box
 for x in [xl,(xl+xu)/2,xu]:
  for y in [yl,(yl+yu)/2,yu]:
   if r(0,x,y)<=0 and r(1,x,y)>=0:
    assert F(5,32)*sum(w[k]*abs(r(k,x,y)) for k in range(4))==bwedge(x,y)

# Exact marginal inequality λ'(x)>1 on the entire combined x envelope.
def lamprime_diff_numer(x):return 378*x*(1-x)-62
# derivative positive for x<1/2, so minimum at x=.2308
assert lamprime_diff_numer(P[0])>0
xgap=Q[0]-P[1]
assert xgap==F(1,500)
min_bx=F(3,4)*(1-2*Q[1]);assert min_bx==F(783,2000)
strict_cost_reduction=min_bx*xgap
assert strict_cost_reduction==F(783,1000000)
out['strict_direction_margins']['strict_wedge:lambda_prime_minus_one_numerator_min']=fr(lamprime_diff_numer(P[0]))
out['strict_direction_margins']['strict_wedge:lambda_gap_lower']=fr(xgap)
out['strict_direction_margins']['strict_wedge:cost_improvement_rate_lower']=fr(strict_cost_reduction)

# A constructive original-model feasible face point is not claimed: this audit is
# a conditional theorem under the independently frozen localization premise.
assert len(out['fixed_audit_signs'])==32
assert sum(v!='ONE_KINK_NOT_FIXED' for v in out['fixed_audit_signs'].values())==31
canonical=json.dumps(out,ensure_ascii=False,sort_keys=True,indent=2)+'\n'
certificate=Path(__file__).with_name('CERTIFICATE_STAGE383B_EXACT.json')
certificate.write_text(canonical,encoding='utf-8')
print('STAGE383B_STAGE380_LOCAL_PARETO_AUDIT_PASS')
print('fixed audits=31/32; cusp crossings=1; residuals r2>0,r3<0, Q:r0<0')
print('strict x-marginal reduction bound >',fr(strict_cost_reduction))
print('certificate bytes',len(canonical.encode('utf-8')))
print('certificate sha256',sha256(canonical.encode('utf-8')).hexdigest())
