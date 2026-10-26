"""Stage157 N14 external iid auxiliary: exact Bellman, two parametrized ties, ordered-prefix replay."""
from fractions import Fraction as F
from itertools import product
from collections import defaultdict
import json
from pathlib import Path
N=14
P=(F(1,8),F(1,24),F(5,6))
Q=(F(1,12),F(1,12),F(5,6))
K=L=F(3342600,10529)
U=(10,2,0) # decide P or continue
T=(14,0,0) # terminal decide P or Q
S=[(n,a,b) for n in range(15) for a in range(n+1) for b in range(n-a+1)]
assert len(S)==680

def nexts(s):
 n,a,b=s
 return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))

def ratio(s): return F(2**(s[1]+s[2]),3**s[1])

H={}; A={}; ties=[]; positive=[]
for s in reversed(S):
 v={'P':K*ratio(s),'Q':L}
 if s[0]<N:v['C']=F(1)+sum((P[i]*H[nexts(s)[i]] for i in range(3)),F())
 best=min(v.values());choices=tuple(a for a in v if v[a]==best)
 if len(choices)>1:ties.append((s,choices))
 A[s]=('C' if s==U else 'Q' if s==T else choices[0])
 assert A[s] in choices
 H[s]=best
 positive.extend(x-best for x in v.values() if x>best)
assert set(ties)=={(U,('P','C')),(T,('P','Q'))}, ties
assert len(positive)==1238

def action(s,y,x):
 if s==U:return 'P' if y else 'C'
 if s==T:return 'P' if x else 'Q'
 return A[s]

def backward(y,x):
 d={}
 for s in reversed(S):
  a=action(s,y,x)
  if a=='Q':o=(F(1),F(0),F(0),F(0))
  elif a=='P':o=(F(0),F(1),F(0),F(0))
  else:
   assert s[0]<N
   z=nexts(s)
   o=tuple(F(1 if j>=2 else 0)+sum(((P if j%2==0 else Q)[i]*d[z[i]][j] for i in range(3)),F()) for j in range(4))
  d[s]=o
 return d[(0,0,0)]

def literal_dfs(y,x):
 total=[0]*4
 hit=defaultdict(lambda:[0,F(0),F(0)])
 seen=0
 # each prefix carries exact integer path likelihood numerator
 stack=[(0,0,0,1,1)]
 while stack:
  n,a,b,px,qx=stack.pop()
  seen+=1
  s=(n,a,b)
  if s in (U,T):
   hit[s][0]+=1
   hit[s][1]+=F(px,24**n)
   hit[s][2]+=F(qx,12**n)
  aa=action(s,y,x)
  if aa=='C':
   assert n<N
   stack.extend(((n+1,a+1,b,px*3,qx), (n+1,a,b+1,px,qx), (n+1,a,b,px*20,qx*10)))
  else:
   p=px*24**(N-n);q=qx*12**(N-n)
   if aa=='Q':total[0]+=p
   else:total[1]+=q
   total[2]+=n*p;total[3]+=n*q
 return tuple(F(total[j],(24 if j%2==0 else 12)**N) for j in range(4)),seen,hit

C={}; visits=[];first_hits={}
for y,x in product((0,1),repeat=2):
 ob,seen,hit=literal_dfs(y,x)
 assert ob==backward(y,x),('independent mismatch',y,x)
 C[y,x]=ob;visits.append((y,x,seen))
 first_hits[y,x]={str(s):[str(v) for v in hit[s]] for s in (U,T)}
 print('CORNER',y,x,seen)
sub=lambda v,w:tuple(a-b for a,b in zip(v,w))
add=lambda v,w:tuple(a+b for a,b in zip(v,w))
M=C[0,0];dU=sub(C[1,0],M);dT=sub(C[0,1],M)
mix=sub(sub(C[1,1],C[1,0]),dT)
assert mix==(F(0),)*4
# balanced common decision errors y(x)=y0+dy*x
assert dU[0]-dU[1]!=0
y0=(M[1]-M[0])/(dU[0]-dU[1])
dy=(dT[1]-dT[0])/(dU[0]-dU[1])
xlo,xhi=F(0),F(1)
if dy>0:
 xlo=max(xlo,-y0/dy);xhi=min(xhi,(1-y0)/dy)
elif dy<0:
 xlo=max(xlo,(1-y0)/dy);xhi=min(xhi,-y0/dy)
assert xlo<=xhi,(xlo,xhi,y0,dy)
def vec(x):
 y=y0+dy*x
 return add(add(M,tuple(y*z for z in dU)),tuple(x*z for z in dT))
lo,hi=vec(xhi),vec(xlo) # alpha increases while terminal-P coin x decreases
assert lo[0]==lo[1] and hi[0]==hi[1]
assert lo[2]>lo[3] and hi[2]>hi[3]
assert all(v[2]+L*v[0]+K*v[1]==H[0,0,0] for v in (lo,hi))
assert hi[0]>lo[0] and hi[2]<lo[2]
a155=F(7319074368089652265,21035720123168587776)
v155=F(5285134543382516317,438244169232678912)
print('BASE',str(a155),str(v155))
print('DUAL',K,L,'ROOT',H[0,0,0],'GAPS',len(positive),'min',min(positive),'ties',ties)
print('HITS',first_hits[0,0]);print('visits',visits)
print('M',M);print('dU',dU);print('dT',dT);print('cross',mix)
print('balance y(x)',y0,'+',dy,'*x; feasible x',xlo,xhi,'boundary y',y0+dy*xlo,y0+dy*xhi)
print('LOW',lo,'HIGH',hi,'increment',hi[0]-lo[0],'slope',K+L)
print('time gaps',lo[2]-lo[3],hi[2]-hi[3])
print('Matches stage156 left?',lo[0]==a155,lo[2]==v155)
assert lo[0]==a155 and lo[2]==v155,'stage156 not recovered'
assert (lo[2]-hi[2])/(hi[0]-lo[0])==K+L
r={'classification':'AUTHOR_EXACT_COMPUTATION_ASSISTED','scope':'external N14 ternary iid, complete ordered-history random policies','model':{'N':14,'P':[str(t) for t in P],'Q':[str(t) for t in Q]},'frozen_scientific_base':'Stage156 main proof, external auxiliary','dual':{'K':str(K),'L':str(L),'Hroot':str(H[0,0,0])},'ties':[[list(s),list(z)] for s,z in ties],'strict_gaps':len(positive),'minimum_strict_gap':str(min(positive)),'corners':{f'{y}{x}':[str(z) for z in v] for (y,x),v in C.items()},'visit_counts':visits,'first_hits':first_hits[0,0],'affine':{'M00':[str(z) for z in M],'dU':[str(z) for z in dU],'dT':[str(z) for z in dT],'mixed':[str(z) for z in mix]},'balance':{'y0':str(y0),'dy_dx':str(dy),'x_lo':str(xlo),'x_hi':str(xhi),'y_lo':str(y0+dy*xlo),'y_hi':str(y0+dy*xhi)},'endpoints':{'left':{'alpha':str(lo[0]),'tP':str(lo[2]),'tQ':str(lo[3])},'right':{'alpha':str(hi[0]),'tP':str(hi[2]),'tQ':str(hi[3])}},'slope':str(K+L),'increment':str(hi[0]-lo[0]),'left_stage156_match':True}
Path(__file__).with_name('certificate157.json').write_text(json.dumps(r,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('STAGE157_FULL_REAL_AUTHOR_PROOF_CHECK_PASS')
