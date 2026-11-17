from fractions import Fraction as F
from itertools import product

alpha=(F(1,2),F(2,3),F(1,2),F(3,4))
FULL_UP=((0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,1,0))
LR_UP=((0,0,0),(0,1,1),(1,0,0),(1,1,0))
STAGE=((0,0,0),(1,0,0),(1,1,0),(1,1,1))
C=(F(1,8),F(1,6),F(1,16),F(3,32))
checks=0

def eq(a,b):
 global checks
 checks+=1
 assert a==b,(a,b)

def obs(model,corner,stage_ids):
 x,y,i=map(F,corner)
 d=y/16+3*i/32
 w=(F(1,4),(1-x)/4,y/8,i/8)
 cs=[w[s]*alpha[s] for s in range(4)]
 M=[cs[s]*STAGE[stage_ids[s]][0] for s in range(4)]
 S=[F(2,3)*M[s]*STAGE[stage_ids[s]][1] for s in range(4)]
 U=[S[s]*STAGE[stage_ids[s]][2] for s in range(4)]
 p,q,r,v=(model[z] for z in ('p','q','r','v'))
 return (F(107,128)-21*x/128+d/4-sum(S)/2+sum((p[s]*S[s]/8 for s in range(4)),F(0)),
         F(13,64)+3*x/64-d/2+sum(S)/8+sum((q[s]*S[s]/32 for s in range(4)),F(0)),
         3+sum(M)+F(3,2)*sum(S)+sum((r[s]*U[s] for s in range(4)),F(0)),
         3+sum(M)/2+F(3,8)*sum(S)+sum((v[s]*U[s]/4 for s in range(4)),F(0)))

def direction(theta):return (F(0),F(0),-theta,F(4))
def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))

def brute(model,theta,is_full):
 n=direction(theta); best=None; arg=None
 for corner in (FULL_UP if is_full else LR_UP):
  choices=product(range(4),repeat=4) if is_full else ((j,)*4 for j in range(4))
  for stages in choices:
   value=dot(n,obs(model,corner,stages))
   if best is None or value>best:best,arg=value,(corner,stages)
 return best,arg

def formula(model,theta):
 assert F(0)<theta<=F(9,8)
 if theta<=1:
  base=3-2*theta
  g=[model['v'][s]-theta*model['r'][s] for s in range(4)]
 else:
  base=2-theta
  g=[model['v'][s]-theta*model['r'][s]-F(3,2)*(theta-1) for s in range(4)]
 pos=sum((C[s]*max(g[s],0) for s in range(4)),F(0))
 neg=sum((C[s]*max(-g[s],0) for s in range(4)),F(0))
 hbase=3*(4-theta)+base*sum(C)
 return hbase+F(2,3)*pos,hbase+F(2,3)*max(pos-neg,F(0)),F(2,3)*min(pos,neg),g

mixed=dict(p=(F(1,4),F(1,2),F(3,4),F(1,2)),
           q=(F(3,4),F(1,2),F(1,4),F(1,2)),
           r=(F(1,2),)*4,
           v=(F(13,20),F(9,10),F(13,20),F(9,10)))
varied=dict(p=(F(2,7),F(3,8),F(4,9),F(5,11)),
            q=(F(1,5),F(2,5),F(3,5),F(4,5)),
            r=(F(1,4),F(2,3),F(3,8),F(4,5)),
            v=(F(3,4),F(1,5),F(7,8),F(2,5)))
uniform=dict(p=(F(1,3),)*4,q=(F(2,3),)*4,r=(F(1,2),)*4,v=(F(3,5),)*4)
thresholds=(F(1,4),F(3,4),F(1),F(21,20),F(11,10),F(9,8))
for model in (mixed,varied,uniform):
 for theta in thresholds:
  hF,_=brute(model,theta,True)
  hL,_=brute(model,theta,False)
  pF,pL,gap,_=formula(model,theta)
  eq(hF,pF);eq(hL,pL);eq(hF-hL,gap)

hF,stage=brute(mixed,F(11,10),True)
hL,_=brute(mixed,F(11,10),False)
w=obs(mixed,(0,1,1),(1,3,1,3))
eq(dot(direction(F(11,10)),w),hF)
eq(hF-hL,F(1,160))
eq(formula(mixed,F(1))[2],F(0))
eq(w,(F(1841,2304),F(459,3072),F(1093,288),F(213,64)))
print('source_weights',C)
print('example_direction',direction(F(11,10)))
print('example_g',formula(mixed,F(11,10))[3])
print('support_FULL',hF,'support_LR',hL,'gap',hF-hL)
print('witness',w,'min_Linf_distance',F(1,160)/(F(11,10)+4))
print('direction_theta_one_gap',formula(mixed,F(1))[2])
print('models',3,'thresholds',len(thresholds),'full_vertices_per_test',1536,'LR_vertices_per_test',16,'assertions',checks)
print('PASS_EXACT_R5_K3_COMMON_LABEL_CLOCK_SWEEP')
