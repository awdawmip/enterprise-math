from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
from math import comb
P=[F(1,8),F(1,24),F(5,6)]
Q=[F(1,12),F(1,12),F(5,6)]
K112=F(50591871,53872);L112=F(2961024,3367)
K111=F(328788597439629,341261245318);L111=F(155234629311000,170630622659)
A=(10,3,0);T=(14,7,4);Fstate=(4,0,2)
U0=F(199112072506703,211315200000000)
ALPHA111=F(13084629088533672707,37682150988866125824)
V111=F(1930486964443856499985,150728603955464503296)

@lru_cache(None)
def R(state):
 n,a,b=state
 return F(2**(a+b),3**a)

def DP(K,L):
 @lru_cache(None)
 def H(n,a,b):
  op=K*R((n,a,b)); oq=L
  if n==14: return min(op,oq)
  return min(op,oq, F(1)+P[0]*H(n+1,a+1,b)+P[1]*H(n+1,a,b+1)+P[2]*H(n+1,a,b))
 acts={}; ties={}; gaps=[]; st=0
 for n in range(15):
  for a in range(n+1):
   for b in range(n-a+1):
    state=n,a,b
    opts={'P':K*R(state),'Q':L}
    if n<14: opts['C']=1+P[0]*H(n+1,a+1,b)+P[1]*H(n+1,a,b+1)+P[2]*H(n+1,a,b)
    best=min(opts.values())
    aa=[k for k,v in opts.items() if v==best]
    acts[state]=aa[0] if len(aa)==1 else ''.join(aa)
    if len(aa)>1:ties[state]=aa
    gaps.extend([v-best for v in opts.values() if v>best]);st+=1
 return H((0),0,0),acts,ties,gaps

def forward(acts,u=U0,w=F(0)):
 aliveP={(0,0,0):F(1)};aliveQ={(0,0,0):F(1)}
 ep=eq=tp=tq=F(0)
 firsthit={A:[0,F(0),F(0)],T:[0,F(0),F(0)]}
 # also count literal prefixes through deterministic states
 cnt={(0,0,0):1}
 for n in range(15):
  nxtP=defaultdict(F);nxtQ=defaultdict(F);ncnt=defaultdict(int)
  for state,mP in aliveP.items():
   mQ=aliveQ[state]; multi=cnt[state]
   if state in firsthit:
    firsthit[state][0]+=multi;firsthit[state][1]+=mP;firsthit[state][2]+=mQ
   tag=acts[state]
   if state==A: stopP=u; stopQ=F(0); cont=1-u
   elif state==T: stopP=1-w;stopQ=w;cont=0
   elif tag=='P':stopP=F(1);stopQ=cont=F(0)
   elif tag=='Q':stopQ=F(1);stopP=cont=F(0)
   elif tag=='C':cont=F(1);stopP=stopQ=F(0)
   else: raise AssertionError((state,tag))
   ep += mP*stopQ;eq += mQ*stopP;tp+=mP*n*(stopP+stopQ);tq+=mQ*n*(stopP+stopQ)
   if cont:
    for j,ch in enumerate([(n+1,state[1]+1,state[2]),(n+1,state[1],state[2]+1),(n+1,state[1],state[2])]):
     nxtP[ch]+=mP*P[j]*cont;nxtQ[ch]+=mQ*Q[j]*cont
     # multiplicity exact counts only when no randomization path to child; A can't parent T, but count includes C if u fractional (should drop if u=1); forward cnt overcounts from A when u fractional; at T disjoint by count argument.
     ncnt[ch]+=multi
  aliveP,aliveQ,cnt=nxtP,nxtQ,ncnt
 assert not aliveP
 return {'ep':ep,'eq':eq,'tp':tp,'tq':tq,'firsthit':firsthit}


def main():
 for tag,(K,L) in [('111',(K111,L111)),('112',(K112,L112))]:
  H,acts,ties,gaps=DP(K,L)
  from collections import Counter
  print(tag, 'H',H, 'ties',ties, 'state_count',len(acts),'strict_gaps',len(gaps),'smallest_gap',min(gaps), 'actions',Counter(acts.values()))
  if tag=='112':
   base={k:('P' if k==A or k==T else v) for k,v in acts.items()}
   for z in (F(0),F(1)):
    o=forward(base,U0,z);print('base u',U0,'w',z, 'errors',(o['ep'],o['eq']),'times',(o['tp'],o['tq']),'hits',o['firsthit'])
   r00=forward(base,F(0),F(0));r10=forward(base,F(1),F(0));r01=forward(base,F(0),F(1));r11=forward(base,F(1),F(1));
   print('base 00',tuple(r00[k] for k in ['ep','eq','tp','tq']))
   dU={k:r10[k]-r00[k] for k in ['ep','eq','tp','tq']}
   dW={k:r01[k]-r00[k] for k in ['ep','eq','tp','tq']}
   dUW={k:r11[k]-r10[k]-r01[k]+r00[k] for k in ['ep','eq','tp','tq']}
   print('du',dU,'dw',dW,'interaction',dUW)
   assert all(not v for v in dUW.values())
   du=dU['ep']-dU['eq'];dw=dW['ep']-dW['eq'];slope=-dw/du
   limit=(1-U0)/slope if slope>0 else -U0/slope
   print('slope du/dw',slope,'wmax',limit,'u_final', U0+slope*limit)
   if limit>1:limit=F(1)
   o=forward(base,U0+slope*limit,limit)
   print('endpoint', 'w',limit, 'u',U0+slope*limit, 'moments',o)
   print('delta',o['ep']-ALPHA111,'value',max(o['tp'],o['tq']),'slope', (V111-max(o['tp'],o['tq']))/(o['ep']-ALPHA111))
   print('dual',H,'V111_bound',V111+(K+L)*ALPHA111,'H_endpoint', max(o['tp'],o['tq'])+(K+L)*o['ep'])

if __name__=='__main__':main()

def next_dual():
 a,b=F(-185064,635),F(21376,17145)
 K=K112;L=a+b*K
 H,acts,ties,gaps=DP(K,L)
 policy={s:('P' if s==A else 'Q' if s==T else t) for s,t in acts.items()}
 @lru_cache(None)
 def affine(n,a0,b0):
  st=(n,a0,b0);act=policy[st]
  if act=='P':return (F(0),R(st))
  if act=='Q':return (a,b)
  assert act=='C'
  terms=[affine(n+1,a0+1,b0),affine(n+1,a0,b0+1),affine(n+1,a0,b0)]
  return (F(1)+sum(P[i]*terms[i][0] for i in range(3)), sum(P[i]*terms[i][1] for i in range(3)))
 cand=[];zt=[]
 for s,action in policy.items():
  n,a0,b0=s
  opts={'P':(F(0),R(s)), 'Q':(a,b)}
  if n<14:
   terms=[affine(n+1,a0+1,b0),affine(n+1,a0,b0+1),affine(n+1,a0,b0)]
   opts['C']=(1+sum(P[j]*terms[j][0] for j in range(3)),sum(P[j]*terms[j][1] for j in range(3)))
  chosen=opts[action]
  for op,(v,slope) in opts.items():
   if op==action:continue
   d0=v-chosen[0];d1=slope-chosen[1];gap=d0+d1*K
   assert gap>=0,(s,action,op,gap)
   if gap==0:
    zt.append((s,action,op,'slope',d1))
    if d1>0: print('bad current tie',s,op)
   elif d1>0:
    root=-d0/d1
    if root>=0 and root<K:cand.append((root,s,action,op,gap,d1))
 assert all(not (op=='bad') for op in zt)
 print('next dual candidate', max(cand) if cand else None)
 print('zero ties slopes',zt)
 print('candidates count',len(cand),'top5',sorted(cand,reverse=True)[:5])
 return max(cand) if cand else None

if __name__=='__main__': next_dual()
