"""Exact global support proof for all locally randomized seedless LR policies on the six-leaf tree.

The only nontrivial likelihood-ratio information-set collision is at (t=2,R=1).
All other decision signatures are uniquely identified by (time, likelihood ratio).
"""
from fractions import Fraction as F
from itertools import product

q=lambda a,b=1:F(a,b)
leaves=[
 ('A','C','low', q(1,24),q(1,12),q(1,2)),
 ('A','C','high',q(1,8),q(1,12),q(3,2)),
 ('A','L','side',q(1,12),q(1,3),q(1,4)),
 ('B','C','low', q(1,32),q(1,8),q(1,4)),
 ('B','C','high',q(7,32),q(1,8),q(7,4)),
 ('B','H','side',q(1,2),q(1,4),q(2)),
]
assert all(p>0 and Q>0 and p==Q*r for _,_,_,p,Q,r in leaves)
assert sum(row[3] for row in leaves)==sum(row[4] for row in leaves)==1
for g,r in (('A',q(1,2)),('B',q(3,2))):
 P=sum(row[3] for row in leaves if row[0]==g)
 Q=sum(row[4] for row in leaves if row[0]==g)
 assert Q==q(1,2) and P==r*Q
for g in ('A','B'):
 C=[row for row in leaves if row[0]==g and row[1]=='C']
 assert sum(z[3] for z in C)==sum(z[4] for z in C)

terms=('A_low','A_high','B_low','B_high')
ACTIONS_T1=('P','Q','cont')
ACTIONS_C=('P','Q','cont')
ACTIONS_STOP=('P','Q')

def observer(t1,tc,sides,t3):
 # t1: A/B, tc: A-C/B-C, sides: A-L/B-H, t3: A-low/A-high/B-low/B-high
 out=[q(0),q(0),q(0),q(0)]
 for g,n,term,p,Q,r in leaves:
  j=(g=='B')
  if t1[j]!='cont': tau=1;dec=t1[j]
  elif n!='C':tau=2;dec=sides[j]
  elif tc[j]!='cont':tau=2;dec=tc[j]
  else:tau=3;dec=t3[terms.index(g+'_'+term)]
  if dec=='Q':out[0]+=p
  else:out[1]+=Q
  out[2]+=p*tau
  out[3]+=Q*tau
 return tuple(out)

signed=(912,456,128,-194)
support=lambda o:sum(a*b for a,b in zip(signed,o))
full={};lr={}
for t1 in product(ACTIONS_T1,repeat=2):
 for sides in product(ACTIONS_STOP,repeat=2):
  for t3 in product(ACTIONS_STOP,repeat=4):
   for cA,cB in product(ACTIONS_C,repeat=2):
    p=observer(t1,(cA,cB),sides,t3)
    full.setdefault(p,(t1,(cA,cB),sides,t3))
   for c in ACTIONS_C:
    p=observer(t1,(c,c),sides,t3)
    lr.setdefault(p,(t1,(c,c),sides,t3))

assert len(full)==196 and len(lr)==124
assert set(lr).issubset(set(full))
assert all(support(o)<=857 for o in lr)
assert max(map(support,lr))==857
assert max(map(support,full))==868
witness=(q(85,96),q(11,24),q(9,4),q(9,4))
policy=(('cont','cont'),('Q','cont'),('P','Q'),('P','P','P','Q'))
assert observer(*policy)==witness
assert support(witness)==868
assert support(witness)-max(map(support,lr))==11
assert len([o for o in lr if support(o)==857])==5
print('All six positive P/Q leaves and prefix likelihoods: EXACT')
print('Full deterministic description count: ',3**2*3**2*2**2*2**4)
print('LR deterministic description count: ',3**2*3*2**2*2**4)
print('Distinct full/LR O vectors: ',len(full),len(lr))
print('Global signed normal: ',signed)
print('All seedless LR satisfy: 912 e_P + 456 e_Q + 128 T_P - 194 T_Q <= 857')
print('Exact maximum over ALL LR deterministic policies: ',max(map(support,lr)))
print('Exact maximum over ALL full deterministic policies: ',max(map(support,full)))
print('Full-history witness O: ',witness)
print('Full-history witness deterministic policy: ',policy)
print('Sharp global unrestricted support gap: ',11)
print('All-real randomized policy coverage: finite multilinear simplex-vertex reduction')
print('ALL EXACT UNRESTRICTED CHECKS PASSED')
