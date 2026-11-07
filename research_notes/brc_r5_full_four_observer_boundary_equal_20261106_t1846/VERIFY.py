#!/usr/bin/env python3
"""R5: exact finite certificate of FULL_HIST/LR four-observer equality on time boundary."""
from fractions import Fraction as Q
from itertools import product
from collections import defaultdict

R2=(Q(3,4),Q(5,4)); R3=(Q(1,2),Q(1),Q(3,2)); R4=(Q(1,10),Q(1),Q(19,10))
q3=((Q(13,20),Q(1,5),Q(3,20)),(Q(1,40),Q(9,20),Q(21,40)))
q4=(
 ((Q(509,900),Q(382,900),Q(9,900)),(Q(47,180),Q(43,90),Q(47,180)),(Q(9,900),Q(382,900),Q(509,900))),
 ((Q(509,900),Q(382,900),Q(9,900)),(Q(67,162),Q(14,81),Q(67,162)),(Q(9,900),Q(382,900),Q(509,900))),
)
# Each line is a*TQ + b*TP <= h, from previous octagon theorem.
FACETS=((-323,282,-41),(-188,216,139),(-160,160,41),(-1,2,4),
        (3,-2,4),(80,-80,23),(123,-146,-23),(274,-236,179))
alpha,beta=Q(47,180),Q(67,162)

def timing(x):
 g,u0,u1,X0,X1,X2=x
 return (1+g+(u0+u1)/2+X0+X1+X2,
         1+g+(3*u0+5*u1)/8+X0/2+X1+3*X2/2)

def bounds(x):
 _,u0,u1,_,X1,_=x
 A,B=u0/10,Q(9,40)*u1
 return {'A':A,'B':B,'X1':X1,'A+B-X1':A+B-X1}

def capacities(x):
 return [[x[i+1]*q3[i][j]/2 for j in range(3)] for i in range(2)]

def split(x,orientation):
 b=capacities(x)
 rows=[[Q(0)]*3 for _ in range(2)]
 for j in range(3):
  total=x[3+j]
  if j==1:
   V=b[0][j]+b[1][j]
   rows[0][j]=b[0][j]*total/V if V else Q(0)
   rows[1][j]=b[1][j]*total/V if V else Q(0)
  else:
   i=orientation
   rows[i][j]=min(b[i][j],total)
   rows[1-i][j]=total-rows[i][j]
  assert 0<=rows[0][j]<=b[0][j] and 0<=rows[1][j]<=b[1][j]
 return rows

def stopped(x,rows):
 g,u0,u1,*X=x
 hist=[(Q(1),Q(1)-g)]
 hist += [(R2[i],(g-(u0,u1)[i])/2) for i in range(2)]
 b=capacities(x)
 for i in range(2):
  for j in range(3):
   hist.append((R3[j],b[i][j]-rows[i][j]))
   for k in range(3):hist.append((R4[k],rows[i][j]*q4[i][j][k]))
 m=defaultdict(Q)
 for r,weight in hist:m[r]+=weight
 assert min(m.values())>=0 and sum(m.values())==1
 assert sum(r*weight for r,weight in m.items())==1
 return hist,m

def unique_stopping_profiles():
 flows=set()
 for bits in product((0,1),repeat=9):
  g=Q(bits[0]);u0=g*bits[1];u1=g*bits[2]
  b=[[u*q3[i][j]/2 for j in range(3)] for i,u in enumerate((u0,u1))]
  X=tuple(sum(b[i][j]*bits[3+3*i+j] for i in range(2)) for j in range(3))
  flows.add((g,u0,u1,*X))
 return flows

def main():
 flows=unique_stopping_profiles()
 assert len(flows)==82
 assert all(a*timing(x)[0]+b*timing(x)[1]<=h for x in flows for a,b,h in FACETS)
 n=0
 print('R5 BOUNDARY-TIME FOUR-OBSERVER EQUALITY EXACT CERTIFICATE')
 for idx,(a,b,h) in enumerate(FACETS,1):
  face=sorted((timing(x),x) for x in flows if a*timing(x)[0]+b*timing(x)[1]==h)
  end0,end1=face[0],face[-1]
  t0,x0=end0;t1,x1=end1
  assert t0!=t1 and sum(t==t0 for t,x in face)==1 and sum(t==t1 for t,x in face)==1
  axis=0 if t0[0]!=t1[0] else 1
  for t,x in face:
   v=(t[axis]-t0[axis])/(t1[axis]-t0[axis])
   assert 0<=v<=1 and x==tuple((1-v)*x0[k]+v*x1[k] for k in range(6))
  zeroes=[name for name in bounds(x0) if bounds(x0)[name]==bounds(x1)[name]==0]
  assert zeroes, ('missing uniform zero',idx)
  for v in (Q(0),Q(1,7),Q(1,2),Q(6,7),Q(1)):
   x=tuple((1-v)*x0[k]+v*x1[k] for k in range(6))
   t=timing(x)
   assert a*t[0]+b*t[1]==h
   A,B=x[1]/10,Q(9,40)*x[2];X1=x[4]
   Jlo=max(alpha*X1,beta*X1-(beta-alpha)*A)
   Jhi=min(beta*X1,alpha*X1+(beta-alpha)*B)
   Jlr=X1*(alpha*A+beta*B)/(A+B) if A+B else Q(0)
   assert Jlo==Jhi==Jlr
   pool=split(x,0)
   for orient in (0,1):
    actual=split(x,orient)
    history,m0=stopped(x,actual)
    pooled,m1=stopped(x,pool)
    assert m0==m1
    # History-conditioned labels with distinct probabilities on repeated keys.
    ell=defaultdict(Q)
    for k,(r,weight) in enumerate(history):
     tr=Q((k*7+3)%11,10)
     ell[r]+=weight*tr
    tq_error=sum(ell.values())
    tp_error=1-sum(r*v for r,v in ell.items())
    shared={r:ell[r]/M if M else Q(0) for r,M in m1.items()}
    assert all(0<=p<=1 for p in shared.values())
    assert sum(m1[r]*shared[r] for r in m1)==tq_error
    assert 1-sum(r*m1[r]*shared[r] for r in m1)==tp_error
    n+=1
  print('facet_%d a=%s b=%s h=%s face_profiles=%d t0=%s t1=%s common_zero=%s' %
        (idx,a,b,h,len(face),t0,t1,','.join(zeroes)))
 print('PASS_EXACT_R5_BOUNDARY_FOUR_OBSERVER_FULL_LR_EQUALITY')
 print('binary_local_stopping_encodings=512 distinct_aggregate_flows=%d'%len(flows))
 print('eight_facets_covered=8 exact_history_label_reconstructions=%d'%n)
 print('scope=whole_real_timing_octagon_boundary_and_all_real_declarations')

if __name__=='__main__':main()
