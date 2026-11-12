#!/usr/bin/env python3
"""Exact finite R5 uniformly orderable first-zero witnesses; Python stdlib only.
Frozen P/Q-BRC 28-vector fixture: enterprise-math commit
435e77af0d180eac32bd1f9c4c464bc4010b7551.
"""
from fractions import Fraction as Q
from collections import Counter

R=(2,10,15,20,25,30,38)
W=(336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80)
X=tuple(map(Q,('250555781039/3397584400000,854053219229681/5470110884000000,'
'155682221/156288882400000,1/800000,1/800000,19487331497/781444412000000,'
'1001314300627/47566181600000,1/800000,6101786845061/95132363200000,'
'19640941861/6795168800000,1/800000,1/800000,1/800000,1326387507069/95132363200000,'
'155682221/25142124560000000,155682221/25142124560000000,'
'969901373288483/5782688648800000,1627075388860003/11721666180000000,'
'14139282599219/169879220000000,165067666637733/7814444120000000,'
'1696529496568917/144567216220000000,31271973479/25142124560000000,'
'12993863727852929/4047882054160000000,7517305745629/5782688648800000,'
'36686587724849/3907222060000000,1308842702731/169879220000000,'
'331925821992147/7814444120000000,54684907960963337/2023941027080000000').split(',')))
V=tuple((i,j) for j in (1,2,3,5) for i in range(7))
IX={p:i for i,p in enumerate(V)}
coeff={1:(12,8,1,13,8),2:(3,13,7,4,2),5:(-15,-21,-8,-17,-10)}
atom=[]
for j in (1,2,5):
 for i in range(1,6):
  b=[0]*7;b[0]=R[i]-R[6];b[i]=R[6]-R[0];b[6]=R[0]-R[i]
  d=[0]*28
  for k,t in enumerate(b):
   d[IX[(k,j)]]+=t*coeff[j][i-1]
   d[IX[(k,3)]]-=t*coeff[j][i-1]
  atom.append(tuple(d))
assert len(X)==28 and len(atom)==15
k0=IX[(0,3)];x=X[k0]
assert x==Q(155682221,25142124560000000)
assert tuple(a[k0] for a in atom)==W
H=[0]*28
for i,v in ((1,-23),(2,28),(6,-5)):
 H[IX[(i,3)]]+=v;H[IX[(i,1)]]-=v
L=-Q(427508577031693280,628800490619);U=Q(1,23)
E=Q(9,115400000)
B=tuple(tuple(X[k]+r*x*H[k] for k in range(28)) for r in (L,U))
assert all(t>=0 for end in B for t in end)
P=[(0,)*28]*(1<<15)
for m in range(1,1<<15):
 bit=m&-m;j=bit.bit_length()-1;old=P[m^bit]
 P[m]=tuple(old[k]+atom[j][k] for k in range(28))
N={-p[k0] for p in P if p[k0]<=-3}
assert len(N)==1144 and min(N)==3 and max(N)==1348
MAX_N=1348;INF=MAX_N+1
def ceilq(q):return -(-q.numerator//q.denominator)
# c(S) is the least integer n up to MAX_N for endpoint feasibility
# X(r)+[36*x/n]*(P[S]/36), simultaneously at both r endpoints.
c=[0]*(1<<15)
for m in range(1,1<<15):
 t=0
 for end in B:
  for k,p in enumerate(P[m]):
   if p>=0:continue
   if end[k]==0: t=INF;break
   t=max(t,ceilq(-x*p/end[k]))
  if t>=INF:break
 c[m]=min(t,INF)
# b(S) is the minimum, over all orders of S, of the maximum
# integer c(U) over every initial prefix U of that order.
b=[0]*(1<<15);last=[-1]*(1<<15)
for m in range(1,1<<15):
 options=[(b[m^(1<<i)],i) for i in range(15) if m>>i&1]
 prev,i=min(options)
 b[m]=max(c[m],prev);last[m]=i
endpoint_pairs=0;ordered_pairs=0;best={};legal_counts=Counter()
for m in range(1,1<<15):
 n=-P[m][k0]
 if n not in N:continue
 if c[m]<=n:endpoint_pairs+=1
 if b[m]<=n:
  ordered_pairs+=1;legal_counts[n]+=1
  if n not in best or (m.bit_count(),m)<(best[n].bit_count(),best[n]):best[n]=m
assert set(best)==N
assert (endpoint_pairs,ordered_pairs)==(13371,12672)
assert Counter(m.bit_count() for m in best.values())=={1:5,2:41,3:153,4:319,5:326,6:180,7:86,8:29,9:5}
# Independently check reconstructed orders with exact endpoint inequalities.
for n,m in best.items():
 seq=[];z=m
 while z:
  j=last[z];seq.append(j);z^=1<<j
 p=(0,)*28
 for i in reversed(seq):
  p=tuple(p[k]+atom[i][k] for k in range(28))
  assert all(end[k]+x*p[k]/n>=0 for end in B for k in range(28))
 assert p[k0]==-n
# A feasible aggregate can fail to admit a feasible operation order.
assert P[1025][k0]==-84 and c[1025]==84 and b[1025]==420
assert c[1]>84 and c[1024]==420
print('FIXED_VALUES',len(N))
print('ENDPOINT_FEASIBLE_MASK_THRESHOLD_PAIRS',endpoint_pairs)
print('UNIFORMLY_ORDERABLE_MASK_THRESHOLD_PAIRS',ordered_pairs)
print('ENDPOINT_FEASIBLE_BUT_NOT_ORDERABLE',endpoint_pairs-ordered_pairs)
print('MIN_UNIFORM_ORDER_LENGTH_DISTRIBUTION',dict(sorted(Counter(m.bit_count() for m in best.values()).items())))
print('MAX_MIN_LENGTH',max(m.bit_count() for m in best.values()))
print('NINE_STEP_FIXED_VALUES',sorted(n for n,m in best.items() if m.bit_count()==9))
print('UNIQUE_ORDERABLE_WITNESS_COUNT',sum(v==1 for v in legal_counts.values()))
print('COUNTEREXAMPLE_n84_mask1025_COST',c[1025],'MINIMAX',b[1025])
print('SAMPLE_MASKS',[(n,best[n]) for n in (3,420,540,818,910,1030,1348)])
print('PASS_R5_UNIFORM_ORDERED_FIRSTZERO_1144')
