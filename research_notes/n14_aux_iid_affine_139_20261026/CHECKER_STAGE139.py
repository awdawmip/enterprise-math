#!/usr/bin/env python3
"""Stage139 reproducible adapted verifier (not the locally executed author's original file): finite Bellman and exact observers.
No network, no platform or native task authority inferred.
"""
from fractions import Fraction as F
from collections import defaultdict
from itertools import product
import hashlib,json

N=14
P=(F(1,8),F(1,24),F(5,6))
Q=(F(1,12),F(1,12),F(5,6))
K,L=F(978154621902,1874305573),F(133227391384,267757939)
B,C=(11,0,1),(6,3,0)
STATES=[(n,a,b) for n in range(N+1) for a in range(n+1) for b in range(n-a+1)]
def children(s):
 n,a,b=s;return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
def ratio(s):
 _,a,b=s; return F(2**(a+b),3**a)

# Fraction bottom-up cost; tie policy C: P versus C, B: Q versus C
values={};act={};gaps=[];ties=[]
for s in reversed(STATES):
 n,a,b=s
 c={'P':K*ratio(s),'Q':L}
 if n<N: c['C']=1+sum((p*values[t] for p,t in zip(P,children(s))),F(0))
 m=min(c.values());sel=[k for k,v in c.items() if v==m]
 if len(sel)>1:ties.append((s,sel))
 values[s]=m;act[s]=sel[0]
 gaps.extend([v-m for v in c.values() if v>m])
assert len(STATES)==680 and len(gaps)==1238 and min(gaps)==F(211792744307,7287300067824)
assert set((s,tuple(t)) for s,t in ties)=={(B,('Q','C')),(C,('P','C'))},ties
assert values[(0,0,0)]==F(1792874224751669050640467609,4889306480521221538578432)

def eval_fraction(w,h):
 # M=(eP, eQ, tP, tQ); conditional on current prefix
 m={}
 for s in reversed(STATES):
  n=s[0]
  dec=act[s]
  if s==B: alternatives={'Q':w,'C':1-w}
  elif s==C: alternatives={'P':h,'C':1-h}
  else: alternatives={dec:F(1)}
  choices=[]
  for a,weight in alternatives.items():
   if a=='P':v=(F(0),F(1),F(0),F(0))
   elif a=='Q':v=(F(1),F(0),F(0),F(0))
   else:
    ch=children(s)
    v=(sum((P[j]*m[ch[j]][0] for j in range(3)),F(0)),
       sum((Q[j]*m[ch[j]][1] for j in range(3)),F(0)),
       1+sum((P[j]*m[ch[j]][2] for j in range(3)),F(0)),
       1+sum((Q[j]*m[ch[j]][3] for j in range(3)),F(0)))
   choices.append((weight,v))
  m[s]=tuple(sum((weight*v[i] for weight,v in choices),F(0)) for i in range(4))
 return m[(0,0,0)]

v00=eval_fraction(F(0),F(0));v10=eval_fraction(F(1),F(0));v01=eval_fraction(F(0),F(1));v11=eval_fraction(F(1),F(1))
add=lambda a,b:tuple(x+y for x,y in zip(a,b))
sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
scale=lambda a,x:tuple(x*t for t in a)
dB=sub(v10,v00);dH=sub(v01,v00)
assert v11==add(add(v00,dB),dH)
# eP-eQ = d0 + w dB + h dH.
errdelta=lambda x:x[0]-x[1]
c0=errdelta(v00)
cB=errdelta(dB)
cH=errdelta(dH)
assert cB!=0
w0=-c0/cB;w1=-(c0+cH)/cB
# errors common, M(w(h),h) affine on h
W=lambda h:w0+(w1-w0)*h
M=lambda h:add(add(v00,scale(dB,W(h))),scale(dH,h))
ml=M(F(0));mr=M(F(1))
for vec in (ml,mr):
 assert vec[0]==vec[1]
 assert vec[2]>=vec[3]
 assert vec[2]+L*vec[0]+K*vec[1]==values[(0,0,0)]
assert F(0)<=w0<=1 and F(0)<=w1<=1
alpha138=F(4078711246246925855,11735204976119513088)
V138=F(217809339038053734409,17602807464179269632)
print('BASE MATCH',ml[0]==alpha138,ml[2]==V138, 'alphal',ml[0], 'vl',ml[2]);
# orientation of h increasing for advancing alpha
print('PARAM',w0,w1,'alpha at h=0',ml[0],'at h=1',mr[0])
print('GAPS time P-Q',ml[2]-ml[3],mr[2]-mr[3]);

# Independent literal ordered integer-branch DFS: collect aggregate integer terminal weights
# This implementation never uses Fraction Bellman observer propagation.
P_INTS=(3,1,20);Q_INTS=(1,1,10)

def eval_dfs(wstop,hstop,with_tieinfo=False):
 assert wstop in (0,1) and hstop in (0,1)
 termsP=defaultdict(int);termsQ=defaultdict(int)
 tieP=defaultdict(int);tieQ=defaultdict(int);tiecount=defaultdict(int)
 tiehash={B:hashlib.sha256(),C:hashlib.sha256()}
 visited=0;terminal_count=0
 def visit(n,a,b,pint,qint,word):
  nonlocal visited,terminal_count
  visited+=1;s=(n,a,b)
  if s in (B,C):
   tiecount[s]+=1;tieP[s]+=pint;tieQ[s]+=qint
   tiehash[s].update((str(word)+':'+str(pint)+':'+str(qint)+';').encode())
  if s==B:action='Q' if wstop else 'C'
  elif s==C:action='P' if hstop else 'C'
  else:action=act[s]
  if action in ('P','Q'):
   terminal_count+=1
   if action=='Q':termsP[(n,action)]+=pint;termsQ[(n,action)]+=qint
   else:termsP[(n,action)]+=pint;termsQ[(n,action)]+=qint
   return
  assert n<N
  visit(n+1,a+1,b,pint*3,qint,word*3)
  visit(n+1,a,b+1,pint,qint,word*3+1)
  visit(n+1,a,b,pint*20,qint*10,word*3+2)
 visit(0,0,0,1,1,0)
 eP=sum((F(weight,24**n) for (n,dec),weight in termsP.items() if dec=='Q'),F(0))
 eQ=sum((F(weight,12**n) for (n,dec),weight in termsQ.items() if dec=='P'),F(0))
 tP=sum((n*F(weight,24**n) for (n,dec),weight in termsP.items()),F(0))
 tQ=sum((n*F(weight,12**n) for (n,dec),weight in termsQ.items()),F(0))
 obj=(eP,eQ,tP,tQ)
 info={'visited':visited,'terminals':terminal_count,'tie_first_hit_count':{str(s):tiecount[s] for s in (B,C)},'tie_first_hit_masses_P':{str(s):str(F(tieP[s],24**s[0])) for s in (B,C)},'tie_first_hit_masses_Q':{str(s):str(F(tieQ[s],12**s[0])) for s in (B,C)},'tie_order_hash_sha256':{str(s):tiehash[s].hexdigest() for s in (B,C)}}
 return obj,info

corners={}
for w,h,expected in [(0,0,v00),(1,0,v10),(0,1,v01),(1,1,v11)]:
 v,info=eval_dfs(w,h)
 assert v==expected,(w,h,v,expected)
 corners[f'{w}{h}']={'vector':list(map(str,v)),'dfs':info}
 print('DFS',w,h,'PASS visited',info['visited'],'B/C',info['tie_first_hit_count'])
assert mr[0]>=ml[0]
assert W(F(0))==w0 and W(F(1))==w1
end_alpha=mr[0];end_V=mr[2]
assert end_alpha>alpha138
assert ml[0]==alpha138 and ml[2]==V138,(ml[0]-alpha138,ml[2]-V138)
assert end_V==V138-(K+L)*(end_alpha-alpha138)
certificate={
 'name':'Stage139_exact_iid_author_certificate',
 'model':{'P':['1/8','1/24','5/6'],'Q':['1/12','1/12','5/6'],'N':N,'errors':'eP=P(declare Q), eQ=Q(declare P)','value':'min max(E_P tau,E_Q tau) with errors <=alpha'},
 'input_stage137':{'alpha138':str(alpha138),'V138':str(V138)},
 'dual':{'K138':str(K),'L138':str(L),'Hroot138':str(values[(0,0,0)]),'nonselected_action_gaps':len(gaps),'min_positive_gap':str(min(gaps)),'tied_states':str(ties)},
 'randomization':{'w':'stop declare Q at B=(11,0,1)', 'h':'stop declare P at C=(11,4,1)','w0':str(w0),'slope_w_in_h':str(w1-w0),'w1':str(w1)},
 'corners':corners,
 'affine':{'alpha_start':str(ml[0]),'alpha_end':str(end_alpha),'V_start':str(ml[2]),'V_end':str(end_V),'interval_length':str(end_alpha-alpha138),'slope':str(-(K+L)),'tP_minus_tQ_at_h0':str(ml[2]-ml[3]),'tP_minus_tQ_at_h1':str(mr[2]-mr[3])},
 'status':'AUTHOR_EXACT_FINITE_COMPUTATION_ASSISTED_NOT_INDEPENDENT_DRIVER',
 'BRC':'Literal ordered prefix ids and exact positive masses; count-state quotient only after iid observer sufficiency for four observables',
 'formal_native':'Owner/CLAIM/Result not established; outside P000 native X6 world'
}
with open('certificate139_portable.json','w') as f:json.dump(certificate,f,indent=2,ensure_ascii=False)
print('SUCCESS_STAGE138',json.dumps(certificate['affine'],indent=2))
