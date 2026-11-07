#!/usr/bin/env python3
"""PREFIX-565: exact q5/q6 marginal e-positivity certificate for frozen native X6-BRC.
Scientific input pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Model: four-STAR, 48 native phases, 96 branch ports, 6 labeled actions,
        signed six-axis BRC weights, single gate marker.
Observer: q1=q2=q3=q4=z=1; x=q5,y=q6; roots with r5=r6=0.
Proof scope: all path depths via exact 5-class transition and formal generating series.
This program additionally checks every native action's quotient and exact integer
polynomial coefficients at finite depths. Stdlib only; no floating point.
"""
from collections import Counter
from itertools import product, permutations
from math import comb
import json

SCIENCE_PIN='f42f2906d77f24085c123f3ccfe9667d41caa96d'
STARS=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(star,c):return tuple((-1 if c>0 else 1)*k for k in STARS[star] if k!=abs(c))
PHASES=tuple((a,p,sgn*k) for a in range(4) for k in STARS[a]
             for sgn in (-1,1) for p in near(a,sgn*k))
PHASE_INDEX={t:i for i,t in enumerate(PHASES)}
def successors(phase):
 a,p,c=PHASES[phase]
 b=next(b for b in range(4) if b!=a and abs(c) in STARS[b])
 return tuple(PHASE_INDEX[t] for t in
              [(a,c,k) for k in near(a,c) if k!=p]+[(b,c,k) for k in near(b,c)])
NEXT=tuple(successors(i) for i in range(48))
TARGET=PHASE_INDEX[(0,1,-3)]
ACTIONS=tuple(product(range(3),(0,1)))
ZERO_ROOT=(0,)*6
ROOTS=(ZERO_ROOT,)+tuple(tuple(sign if j==axis else 0 for j in range(6))
                              for axis in range(4) for sign in (-1,1))

def sg(phase,k):
 c=PHASES[phase][2]
 return (1 if c>0 else -1) if abs(c)==k else 0

def edge(port,action,root):
 phase,bit=divmod(port,2)
 slot,newbit=action
 nxt=NEXT[phase][slot]
 weights=[]
 for k in range(1,7):
  left=sg(phase,k);right=sg(nxt,k);z=root[k-1]
  v=abs(left)+abs(right)-abs(right-z)+abs(left-z)
  assert v in (0,2)
  weights.append(v//2)
 gate=int(bit==newbit==1 and nxt==TARGET)
 return 2*nxt+newbit,tuple(weights)+(gate,)

def klass(port):
 phase=port//2
 p=abs(PHASES[phase][1]);c=abs(PHASES[phase][2])
 if c==6:return 2
 if c==5:return 4
 if p==6:return 1
 if p==5:return 3
 return 0

# Rows of 5x5 BRC marginal transition M(x,y), as (target, exp_x, exp_y):mult.
EXPECTED=(
 {(0,0,0):2,(2,0,0):2,(4,0,0):2},
 {(0,0,0):4,(4,0,0):2},
 {(1,0,1):6},
 {(0,0,0):4,(2,0,0):2},
 {(3,1,0):6},
)

def clean(p):return {mon:num for mon,num in p.items() if num}
def product_step(q,rows):
 ans=[]
 for row in rows:
  p=Counter()
  for (j,a,b),mult in row.items():
   for (xx,yy),cnt in q[j].items():p[xx+a,yy+b]+=mult*cnt
  ans.append(clean(p))
 return ans

def from_uv(poly):
 result=Counter()
 for (a,b),c in poly.items():
  for k in range(a+1):result[b+k,b+a-k]+=c*comb(a,k)
 return clean(result)

def uv_coefficients(max_depth):
 # G_0(t) = (1+4t+12u t²+24u t³+144v t⁴)
 #          / (1-2t-48u t³-144v t⁴-864v t⁵).
 # Exact formal-power-series recurrence, no symbolic linear algebra dependency.
 num=[{(0,0):1},{(0,0):4},{(1,0):12},{(1,0):24},{(0,1):144}]
 prev=[]
 for n in range(max_depth+1):
  c=Counter(num[n] if n<len(num) else {})
  for delay,shift,mult in ((1,(0,0),2),(3,(1,0),48),
                           (4,(0,1),144),(5,(0,1),864)):
   if n>=delay:
    for (a,b),count in prev[n-delay].items():
     c[a+shift[0],b+shift[1]]+=mult*count
  prev.append(clean(c))
 return prev

def native_rows(root):
 return [Counter((j,w[4],w[5]) for action in ACTIONS for j,w in [edge(i,action,root)])
         for i in range(96)]

def polynomial_add(P,Q,sgn=1):
 out=Counter(P)
 for k,v in Q.items():out[k]+=sgn*v
 return clean(out)

def polynomial_mul(P,Q):
 out=Counter()
 for (t,a,b),v in P.items():
  for (s,c,d),w in Q.items():out[t+s,a+c,b+d]+=v*w
 return clean(out)

def polynomial_det(mat):
 """Exact determinant by all 5! permutations in Z[t,x,y]."""
 n=len(mat);result=Counter()
 for perm in permutations(range(n)):
  inversions=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
  cur={(0,0,0):1}
  for i,j in enumerate(perm):cur=polynomial_mul(cur,mat[i][j])
  result=polynomial_add(result,cur,-1 if inversions%2 else 1)
 return result

def uv_t_to_xy(poly):
 out=Counter()
 for (t,u,v),val in poly.items():
  for k in range(u+1):out[t,v+k,v+u-k]+=val*comb(u,k)
 return clean(out)

def verify_formal_identity():
 # Matrix I-tM for the five weighted classes.
 C=[[{(0,0,0):int(i==j)} if i==j else {} for j in range(5)]
    for i in range(5)]
 for i,row in enumerate(EXPECTED):
  for (j,x,y),mult in row.items():
   C[i][j]=polynomial_add(C[i][j],{(1,x,y):mult},-1)
 d=polynomial_det(C)
 replacement=[[({(0,0,0):1} if j==0 else C[i][j]) for j in range(5)]
              for i in range(5)]
 n=polynomial_det(replacement)
 expected_d=uv_t_to_xy({(0,0,0):1,(1,0,0):-2,(3,1,0):-48,
                         (4,0,1):-144,(5,0,1):-864})
 expected_n=uv_t_to_xy({(0,0,0):1,(1,0,0):4,(2,1,0):12,
                         (3,1,0):24,(4,0,1):144})
 assert d==expected_d,(d,expected_d)
 assert n==expected_n,(n,expected_n)
 assert d.get((0,0,0))==1
 return {'determinant_monomial_terms':len(d),'cramer_monomial_terms':len(n),
  'determinants_checked':2,'arithmetic':'exact integer polynomial determinant, 5! terms'}

def validate(check_depth=32,extend_positive_depth=128):
 assert len(PHASES)==48 and len(ACTIONS)==6 and len(NEXT)==48
 assert len(PHASE_INDEX)==48 and all(len(x)==3 for x in NEXT)
 assert len(ROOTS)==9
 assert Counter(map(klass,range(96)))==Counter({0:32,1:16,2:16,3:16,4:16})
 formal=verify_formal_identity()
 roots_edge_checks=0
 row96=native_rows(ZERO_ROOT)
 for root in ROOTS:
  q=native_rows(root)
  assert q==row96 # marginal independent of all first-four-axis root values
  for i,row in enumerate(q):
   assert Counter((klass(j),a,b) for (j,a,b),mult in row.items()
                  for _ in range(mult))==Counter(EXPECTED[klass(i)])
   roots_edge_checks+=sum(row.values())
 assert roots_edge_checks==9*96*6
 scalar=[{(0,0):1} for _ in range(5)]
 full=[{(0,0):1} for _ in range(96)]
 uvs=uv_coefficients(max(check_depth,extend_positive_depth))
 eq_count=0;coefficient_positions=0;support_snapshots=[]
 for d in range(check_depth+1):
  expected=from_uv(uvs[d])
  assert scalar[0]==expected,('uv-to-xy',d)
  for i in range(96):
   assert full[i]==scalar[klass(i)],('native-quotient',d,i)
   eq_count+=1
   coefficient_positions+=len(full[i])
  if d in (0,4,8,16,24,32):
   support_snapshots.append({'depth':d,'uv_monomials':len(uvs[d]),
      'q5_q6_monomials':len(scalar[0]),'sum_uv_coefficients':sum(uvs[d].values()),
      'native_marginal_row0_total_coefficients':sum(scalar[0].values())})
  if d<check_depth:
   scalar=product_step(scalar,EXPECTED)
   full=product_step(full,row96)
 e_positive=all(coeff>=0 for p in uvs for coeff in p.values())
 assert e_positive
 return {'status':'ALL_CHECKS_PASS', 'science_pin':SCIENCE_PIN,
   'model':'frozen four-STAR native X6-BRC, 48 phases, 96 ports, six actions',
   'formal_rational_identity_certificate':formal,
   'observer':'q1=q2=q3=q4=z=1, x=q5, y=q6',
   'root_scope':'zero root and eight +/- axes 1..4 (r5=r6=0)',
   'root_count':len(ROOTS),'native_projected_edges_checked':roots_edge_checks,
   'classes_and_sizes':{'0':32,'1':16,'2':16,'3':16,'4':16},
   'native_vs_5_state_exact_polynomials':eq_count,
   'native_nonzero_coefficient_positions_compared':coefficient_positions,
   'depths_native_checked':[0,check_depth],
   'uv_positive_depths_exactly_generated':[0,extend_positive_depth],
   'positive_recurrence':{'numerator':'1+4t+12ut^2+24ut^3+144vt^4',
     'denominator':'1-2t-48ut^3-144vt^4-864vt^5'},
   'coefficient_snapshots':support_snapshots,
   'theorem_scope':'all nonnegative depths via 5-state exact weighted quotient and positive denominator expansion',
   'full_seven_variable_positivity_status':'OPEN; marginal positivity does not certify separate q1..q4 or gate coefficients'}

if __name__=='__main__':
 print(json.dumps(validate(),ensure_ascii=False,indent=2))
