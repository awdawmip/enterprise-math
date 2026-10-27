"""Exact Fraction checks for the N=3 two-law diagonal shadowing theorem."""
from fractions import Fraction as F
from random import Random
import json
NODES={
'':(0,('a','b')),'a':(1,('ax','ay')),'b':(1,('bu','bv')),
'ax':(2,('axL','axM','axH')),'ay':(2,('ayT',)),
'bu':(2,('buL','buM','buH')),'bv':(2,('bvT',)),
'axL':(3,()),'axM':(3,()),'axH':(3,()),'ayT':(3,()),
'buL':(3,()),'buM':(3,()),'buH':(3,()),'bvT':(3,())}
R={'':F(1),'a':F(3,2),'b':F(1,2),'ax':F(1),'ay':F(2),
'bu':F(1),'bv':F(1,3),'axL':F(1,2),'axM':F(1),'axH':F(3,2),
'buL':F(1,2),'buM':F(1),'buH':F(3,2),'ayT':F(2),'bvT':F(1,3)}
def qmass(sa,sb):
 q={'':F(1),'a':F(1,2),'b':F(1,2),'ax':F(1,4),'ay':F(1,4),
    'bu':F(1,8),'bv':F(3,8),'ayT':F(1,4),'bvT':F(3,8)}
 for h,s,m in [('ax',sa,F(1,4)),('bu',sb,F(1,8))]:
  for k,prob in zip('LMH',(s,1-2*s,s)):q[h+k]=m*prob
 for h,(t,ch) in NODES.items():
  assert q[h]>0 and q[h]*R[h]>0
  if ch:
   assert sum((q[k] for k in ch),F(0))==q[h]
   assert sum((q[k]*R[k] for k in ch),F(0))==q[h]*R[h]
 return q
def normalize(ws):
 if not sum(ws):ws=[1]*len(ws)
 return tuple(F(w,sum(ws)) for w in ws)
def random_policy(rng):
 return {h:normalize([rng.randrange(6) for _ in range(2 if t==3 else 3)])
         for h,(t,_) in NODES.items()}
def visits(policy,q):
 seen={}
 def go(h,survival):
  seen[h]=q[h]*survival
  for c in NODES[h][1]:go(c,survival*policy[h][2])
 go('',F(1))
 return seen
def markovize(pi,s):
 q=qmass(s,s); v=visits(pi,q); A={}
 for h in NODES:
  z=(NODES[h][0],R[h])
  if z not in A:A[z]=[F(0)]*len(pi[h])
  for i,p in enumerate(pi[h]):A[z][i]+=v[h]*p
 table={z:normalize(w) for z,w in A.items()}
 return {h:table[(NODES[h][0],R[h])] for h in NODES}
def law(policy,sa,sb,which):
 q=qmass(sa,sb);v=visits(policy,q)
 out={(t,d):F(0) for t in range(4) for d in ('P','Q')}
 for h,(t,_) in NODES.items():
  m=v[h]*(R[h] if which=='P' else 1)
  out[(t,'P')]+=m*policy[h][0]
  out[(t,'Q')]+=m*policy[h][1]
 assert sum(out.values())==1
 return out
def tv(x,y):return sum((abs(x[k]-y[k]) for k in x),F(0))/2
def times(x):return {t:sum((v for (u,d),v in x.items() if u==t),F(0)) for t in range(4)}
def main():
 pairs=[(F(2,5),F(1,3)),(F(1,6),F(1,5)),
        (F(1,100),F(49,100)),(F(1,3),F(1,3))]
 rng=Random(20261027);n=0
 for sa,sb in pairs:
  for z in range(64):
   pi=random_policy(rng);sig=markovize(pi,sa);d=abs(sa-sb)
   for Rlaw in ('P','Q'):
    a=law(pi,sa,sb,Rlaw);b=law(pi,sa,sa,Rlaw)
    c=law(sig,sa,sb,Rlaw);e=law(sig,sa,sa,Rlaw)
    assert b==e and tv(a,b)<=d/4 and tv(c,e)<=d/4
    assert tv(a,c)<=d/2 and times(a)==times(c)
   n+=1
 pi={h:((F(1),F(0)) if t==3 else (F(1),F(0),F(0)))
     for h,(t,_) in NODES.items()}
 for h in ('','b','bu'):pi[h]=(F(0),F(0),F(1))
 for h in ('buL','buH'):pi[h]=(F(0),F(1))
 sa,sb=F(2,5),F(1,3)
 for rr in ('P','Q'):
  assert tv(law(pi,sa,sb,rr),law(pi,sa,sa,rr))==abs(sa-sb)/4
 print(json.dumps({'status':'PASS_EXACT_FRACTION','rational_policy_trials':n,
 'parameter_pairs':[[str(a),str(b)] for a,b in pairs],
 'probability_laws':['P','Q'],'horizon':3,
 'global_tv_shadow_coefficient':'1/2','single_policy_transport_coefficient':'1/4',
 'sharp_fixed_transport_example_tv':'1/60','both_mean_times_exact':True,
 'remark':'Universal claim proved mathematically; checker samples 256 rational behavioral policies.'},
 indent=2,sort_keys=True))
if __name__=='__main__':main()
