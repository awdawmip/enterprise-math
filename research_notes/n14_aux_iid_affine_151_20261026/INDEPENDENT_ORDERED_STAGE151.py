#!/usr/bin/env python3
"""Independent *literal ordered prefix* integer-weight DFS at Stage151.
No calls into verify_stage151; Bellman actions rebuilt iteratively, and all
observer coordinates accumulated as integers under common depth-14 denominators.
"""
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path
N=14; K=F(45154992,127757); L=F(6412152,18251)
P=(F(3,24),F(1,24),F(20,24));Q=(F(1,12),F(1,12),F(10,12))
wp=(3,1,20);wq=(1,1,10); B=(11,0,1);U=(9,4,1)
DP={}; ACT={}
for n in range(14,-1,-1):
 for a in range(n+1):
  for b in range(n+1-a):
   x=(n,a,b);opts={'P':K*F(2**(a+b),3**a),'Q':L}
   if n<14:opts['C']=F(1)+sum(P[i]*DP[n+1,a+(i==0),b+(i==1)] for i in range(3))
   best=min(opts.values()); DP[x]=best
   ACT[x]=tuple(name for name,cost in opts.items() if cost==best)
assert set(s for s, ties in ACT.items() if len(ties)>1)=={B,U}
assert ACT[U]==('P','C') and ACT[B]==('Q','C')

p_pow=[24**(14-n) for n in range(15)]
q_pow=[12**(14-n) for n in range(15)]
p_den=24**14;q_den=12**14

def run(b,u):
    # p-scaled, q-scaled integer accumulators
    eP=eQ=tP=tQ=0
    first={B:[0,0,0],U:[0,0,0]}
    visited=0;terminal_count=0
    def rec(n,a,c,pnum,qnum):
        nonlocal eP,eQ,tP,tQ,visited,terminal_count
        visited+=1
        s=(n,a,c)
        if s in first:
            z=first[s];z[0]+=1;z[1]+=pnum*p_pow[n];z[2]+=qnum*q_pow[n]
        if s==B:action='Q' if b else 'C'
        elif s==U:action='P' if u else 'C'
        else:
            assert len(ACT[s])==1,(s,ACT[s]);action=ACT[s][0]
        if action!='C':
            terminal_count+=1
            pn=pnum*p_pow[n];qn=qnum*q_pow[n]
            if action=='Q':eP+=pn
            else:eQ+=qn
            tP+=n*pn;tQ+=n*qn
            return
        assert n<N
        for i in range(3):rec(n+1,a+(i==0),c+(i==1),pnum*wp[i],qnum*wq[i])
    rec(0,0,0,1,1)
    return {'corner':(b,u),'observers':(F(eP,p_den),F(eQ,q_den),F(tP,p_den),F(tQ,q_den)),
            'first_hits':{str(k):(v[0],F(v[1],p_den),F(v[2],q_den)) for k,v in first.items()},
            'visited':visited,'terminals':terminal_count}

if __name__=='__main__':
  results=[run(b,u) for b,u in product((0,1),repeat=2)]
  expected=[
      ('1212629741108379235/3505953353861431296','224481853556365/641959232274432','5331301420067770717/438244169232678912','70013062572629/5944066965504'),
      ('1212592135672539235/3505953353861431296','224492569856365/641959232274432','5330367237943930717/438244169232678912','70007401392629/5944066965504'),
      ('1219895021108379235/3505953353861431296','223326853556365/641959232274432','5290919980067770717/438244169232678912','620932563153661/53496602689536'),
      ('1219857415672539235/3505953353861431296','223337569856365/641959232274432','5289985797943930717/438244169232678912','620881612533661/53496602689536'),
  ]
  assert [tuple(map(str,r['observers'])) for r in results]==expected
  assert all(r['first_hits']['(11, 0, 1)']==(11,F(107421875,1451188224),F(107421875,725594112)) and r['first_hits']['(9, 4, 1)']==(378,F(4375,2359296),F(4375,5971968)) for r in results)
  for r in results:
   print('corner',r['corner'],'visited',r['visited'],'leaves',r['terminals'])
   print('observer',tuple(map(str,r['observers'])))
   print('first-hits', {k:tuple(map(str,v)) for k,v in r['first_hits'].items()})
  with open(Path(__file__).resolve().parent / 'independent_exact.json','w') as fp:
   json.dump([{'corner':r['corner'],'observers':list(map(str,r['observers'])),'first_hits':{k:list(map(str,v)) for k,v in r['first_hits'].items()},'visited':r['visited'],'terminals':r['terminals']} for r in results],fp,indent=2)
