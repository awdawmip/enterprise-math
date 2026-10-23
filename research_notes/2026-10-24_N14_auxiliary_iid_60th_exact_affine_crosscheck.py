#!/usr/bin/env python3
"""Second author-side check: ordered-word first hits plus independent min-DP and backward risk."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import comb
import json
from verify_n14_60 import P,Q,N,SP,SQ,A,B,AL,V,S,K,LP,LQ,G

# Deliberately recompute actions with distinct, direct symbolic stopping test.
def stop(n,a,b):
 if (n,a,b) in SP:return 'P'
 if (n,a,b) in SQ:return 'Q'
 if 8*pow(3,a)>=9*pow(2,a+b+N-n):return 'P'
 if 8*pow(3,a+N-n)<9*pow(2,a+b+N-n):return 'Q'
 return 'C'

def count_words(target):
 t,aa,bb=target
 nominal=comb(t,aa)*comb(t-aa,bb)
 survivors=0
 for w in product(range(3),repeat=t):
  if w.count(0)!=aa or w.count(1)!=bb:continue
  a=b=0;alive=True
  for n,x in enumerate(w):
   if stop(n,a,b)!='C':alive=False;break
   a+=(x==0);b+=(x==1)
  if alive:survivors+=1
 # Every word in target count state has the same measure under each law.
 cc=t-aa-bb
 p=survivors*P[0]**aa*P[1]**bb*P[2]**cc
 q=survivors*Q[0]**aa*Q[1]**bb*Q[2]**cc
 return nominal,survivors,p,q


def stop_history_audit(target, crossing=None):
    """Enumerate named target's nominal words and apply FIRST earlier stop (no DP)."""
    t,aa,bb=target
    first_stops={}
    alive=through=0
    for w in product(range(3),repeat=t):
        if w.count(0)!=aa or w.count(1)!=bb:continue
        a=b=0;crossed=False
        for n,i in enumerate(w):
            if (n,a,b)==crossing:crossed=True
            act=stop(n,a,b)
            if act!='C':
                key=(n,a,b,act)
                first_stops[key]=first_stops.get(key,0)+1
                break
            a+=i==0;b+=i==1
        else:
            alive+=1
            through+=crossed
    return alive,through,first_stops

def risk(u,s):
 @lru_cache(None)
 def visit(n,a,b):
  if (n,a,b)==A:p_stop,q_stop=F(),u
  elif (n,a,b)==B:p_stop,q_stop=F(),s
  else:
   z=stop(n,a,b)
   if z=='P':return F(),F(1),F(),F()
   if z=='Q':return F(1),F(),F(),F()
   p_stop=q_stop=F()
  assert n<N
  kids=[visit(n+1,a+(i==0),b+(i==1)) for i in range(3)]
  pc=1-p_stop-q_stop
  ep=q_stop+pc*sum((P[i]*kids[i][0] for i in range(3)),F())
  eq=p_stop+pc*sum((Q[i]*kids[i][1] for i in range(3)),F())
  tp=pc*(1+sum((P[i]*kids[i][2] for i in range(3)),F()))
  tq=pc*(1+sum((Q[i]*kids[i][3] for i in range(3)),F()))
  return ep,eq,tp,tq
 return visit(0,0,0)

def independently_minimize():
 d={};ties={};count=0;strict=0;bad=[]
 for n in reversed(range(N+1)):
  for a in range(n+1):
   for b in range(n-a+1):
    st=(n,a,b)
    costs={'P':LQ*F(2**(a+b),3**a),'Q':LP}
    if n<N:costs['C']=1+sum(P[i]*d[(n+1,a+(i==0),b+(i==1))] for i in range(3))
    minimum=min(costs.values());mins=sorted(x for x,y in costs.items() if y==minimum)
    d[st]=minimum
    if stop(n,a,b) not in mins:bad.append((st,stop(n,a,b),mins))
    if len(mins)>1:ties[st]=mins
    for z,c in costs.items():
     if c>minimum:strict+=1
     count+=1
 return d[(0,0,0)],ties,strict,count,bad

def main():
 na,la,pa,qa=count_words(A)
 nb,lb,pb,qb=count_words(B)
 ar,_,stops=stop_history_audit(A)
 assert ar==171 and stops=={(6,6,0,'P'):1,(10,5,5,'Q'):89,(9,4,5,'Q'):34,(7,3,4,'Q'):76,(6,2,4,'Q'):45,(5,1,4,'Q'):18,(3,0,3,'Q'):28},stops
 late,thru,_=stop_history_audit((12,7,2),A)
 assert (late,thru)==(5164,0),(late,thru)
 assert (na,la)==(462,171), (na,la)
 assert (nb,lb)==(12,12), (nb,lb)
 assert pa==F(19,231928233984) and qa==F(19,82556485632)
 assert pb==F(48828125,725594112) and qb==F(48828125,362797056)
 root,ties,strict,count,bad=independently_minimize()
 assert ties=={A:['C','Q'],B:['C','Q']},ties
 assert not bad,bad
 assert strict==1238 and count==1920,(strict,count)
 assert root==V+G*AL
 # The independent minimizer checks all inherited state actions and both exact ties.
 vals={(u,s):risk(u,s) for u in (F(0),F(1)) for s in (F(0),F(1))}
 for j in range(4):assert vals[F(1),F(1)][j]-vals[F(1),F(0)][j]-vals[F(0),F(1)][j]+vals[F(0),F(0)][j]==0
 X=vals[F(1),F(0)][0]-vals[F(0),F(0)][0];Y=-(vals[F(1),F(0)][1]-vals[F(0),F(0)][1])
 E=vals[F(0),F(1)][0]-vals[F(0),F(0)][0];H=-(vals[F(0),F(1)][1]-vals[F(0),F(0)][1])
 h=(X+Y)/(E+H);eta=X-E*h
 assert h==F(2055819,13926400000000000)
 assert eta==F(2641,551863027922632704)
 assert F(0)<S-h<S<F(1)
 checks=[]
 for u in (F(0),F(1,6),F(1,3),F(1,2),F(2,3),F(5,6),F(1)):
  ep,eq,tp,tq=risk(u,S-h*u)
  assert ep==eq==AL+eta*u
  assert tp==V-G*eta*u
  assert tp>tq and tp+LP*ep+LQ*eq==root
  checks.append(str(tp-tq))
 assert AL+eta==F(5171839496325066167,14900301753911083008)
 assert V-G*eta==F(12355052125433941189,931268859619442688)
 return {'verdict':'AUTHOR_CROSSCHECK_PASS','nominal_A':na,'firsthit_A':la,'nominal_B':nb,'firsthit_B':lb,'first_stop_A60':str(stops),'A55_firsthit_under_59':late,'A55_paths_through_A60':thru,'Bellman_ties':str(ties),'Bellman_strict':strict,'min_root':str(root),'balance_h':str(h),'eta':str(eta),'mixed_prob_end':str(S-h),'alpha60':str(AL+eta),'V60':str(V-G*eta),'endpoint_margins':[checks[0],checks[-1]],'zero_mixed_term_in_four_risks':True,'randomized_samples_checked':len(checks)}
if __name__=='__main__':print(json.dumps(main(),ensure_ascii=False,indent=2))
