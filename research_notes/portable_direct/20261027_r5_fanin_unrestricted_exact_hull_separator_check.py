#!/usr/bin/env python3
"""Exact nonblind R5 fan-in all-decision hull support certificate; no dependencies."""
from fractions import Fraction as F
from itertools import product

K=list(product('AB','UV',(0,1)))
q=dict(zip(K,map(F,['1/12','1/12','1/6','1/6','1/8','1/8','1/8','1/8'])))
p=dict(zip(K,map(F,['1/48','7/48','1/48','1/16','1/16','3/16','1/8','3/8'])))
assert min(q.values())>0 and min(p.values())>0 and sum(q.values())==sum(p.values())==1
lam=(80,25,-2,3)
def plus(a,b):return tuple(x+y for x,y in zip(a,b))
def cost(a):return sum(x*y for x,y in zip(lam,a))
def obs(keys,act,t):
    P=sum(p[k] for k in keys);Q=sum(q[k] for k in keys)
    return (P if act=='Q' else F(0), Q if act=='P' else F(0), t*P,t*Q)
def join(a,b):return {plus(x,y) for x in a for y in b}
def midkeys(h,k):return [(h,k,j) for j in (0,1)]
def rootkeys(h):return [(h,k,j) for k in 'UV' for j in (0,1)]
B={}
for h,k in product('AB','UV'):
    leaves=[{obs([(h,k,j)],a,3) for a in 'PQ'} for j in (0,1)]
    B[h,k]={'P':{obs(midkeys(h,k),'P',2)},
            'Q':{obs(midkeys(h,k),'Q',2)},'C':join(*leaves)}
def allmid(h,k):return set().union(*B[h,k].values())
def root(h,u,v):return {obs(rootkeys(h),a,1) for a in 'PQ'}|join(u,v)
full=join(root('A',allmid('A','U'),allmid('A','V')),
          root('B',allmid('B','U'),allmid('B','V')))
lr=set()
for a in 'PQC':
    lr |= join(root('A',B['A','U'][a],allmid('A','V')),
               root('B',B['B','U'][a],allmid('B','V')))
assert lr<=full and len(full)==1402 and len(lr)==754
assert (min(map(cost,full)),min(map(cost,lr)))==(F(149,6),F(301,12))
# Independent backwards dynamic programming, valid for all real randomizations
# as the signed cost is affine in every local decision; AU/BU are exclusive.
mid={}
for h,k in product('AB','UV'):
    mid[h,k]={a:min(map(cost,B[h,k][a])) for a in 'PQC'}
def rootcost(h,shared=None):
    cu=min(mid[h,'U'].values()) if shared is None else mid[h,'U'][shared]
    cv=min(mid[h,'V'].values())
    return min(*(cost(obs(rootkeys(h),a,1)) for a in 'PQ'),cu+cv)
assert rootcost('A')+rootcost('B')==F(149,6)
by_shared={a:rootcost('A',a)+rootcost('B',a) for a in 'PQC'}
assert by_shared=={'P':F(301,12),'Q':F(26),'C':F(301,12)}
print('EXACT_PASS; full_vectors=1402; seedless_LR_vectors=754')
print('lambda=',lam,'full=',F(149,6),'seedless_LR=',F(301,12),'gap=',F(1,4))
print('LR_shared_action_minima=',by_shared)
