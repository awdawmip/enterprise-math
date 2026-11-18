"""Author-side exact proof witness for N14 external ternary IID, Stage201.
All arithmetic Fraction/BigInt; no floats. Frozen inputs from Stage200 GitHub proof and Stage201 dual candidate.
Two independent algorithms: count-state suffix DP and full ordered integer DFS.
"""
from fractions import Fraction as F
from functools import cache
from itertools import product
from json import dump, dumps
from pathlib import Path
N=14
P=(F(3,24),F(1,24),F(20,24)); Q=(F(2,24),F(2,24),F(20,24))
K=L=F(648,5)
HREF=F(5568451006246740809,54780521154084864)
R=(13,3,1);Z=(14,0,0);START=(0,0,0)
A200=F(3704473910272792345,10517860061584293888)
V200=F(2269644909513884573,219122084616339456)
S=[(n,a,b) for n in range(N+1) for a in range(n+1) for b in range(n-a+1)]
assert len(S)==680

def child(s,i):
 n,a,b=s
 return n+1,a+(i==0),b+(i==1)

def like(s):
 _,a,b=s
 return F(2**(a+b),3**a)

@cache
def val(s):
 c={'P':K*like(s),'Q':L}
 if s[0]<N:
  c['C']=1+sum(P[i]*val(child(s,i))[0] for i in range(3))
 m=min(c.values())
 return m,tuple(a for a in ('P','Q','C') if a in c and c[a]==m),tuple(v-m for v in c.values() if v>m)

assert val(START)[0]==HREF,(val(START)[0],HREF)
ties={str(s):val(s)[1] for s in S if len(val(s)[1])>1}
assert ties=={str(R):('P','C'),str(Z):('P','Q')},ties
strict=[gap for s in S for gap in val(s)[2]]
assert len(strict)==1238,(len(strict),min(strict))
assert min(strict)==F(34067479,2149908480),(min(strict),F(34067479,2149908480))

# r=0 follows C at R, r=1 reports P at R; z=1 reports P at terminal Z.
def decision(s,r,z):
 if s==R:return 'P' if r else 'C'
 if s==Z:return 'P' if z else 'Q'
 return val(s)[1][0]

@cache
def obs_dp(s,r,z):
 act=decision(s,r,z)
 if act=='Q':return F(1),F(0),F(0),F(0)
 if act=='P':return F(0),F(1),F(0),F(0)
 kids=[obs_dp(child(s,i),r,z) for i in range(3)]
 return tuple(sum((P if j%2==0 else Q)[i]*kids[i][j] for i in range(3))+int(j>=2) for j in range(4))

def traverse(r,z):
 totals=[0]*4;calls=0;arrivals=[0,0,0]
 def walk(s,pm,qm,visitedR=False):
  nonlocal calls
  calls+=1
  n=s[0]
  if s==R:
   arrivals[0]+=1
   visitedR=True
  if s==Z:
   arrivals[1]+=1
   arrivals[2]+=int(visitedR)
  act=decision(s,r,z)
  if act=='C':
   for i,(pi,qi) in enumerate(zip((3,1,20),(2,2,20))):
    walk(child(s,i),pm*pi,qm*qi,visitedR)
  else:
   mul=24**(N-n)
   if act=='Q':totals[0]+=pm*mul
   if act=='P':totals[1]+=qm*mul
   totals[2]+=n*pm*mul
   totals[3]+=n*qm*mul
 walk(START,1,1)
 return tuple(F(v,24**N) for v in totals),calls,arrivals

corners={};counts={};arrs={}
for r,z in product((0,1),repeat=2):
 key=f'{r}{z}'
 corners[key]=obs_dp(START,r,z)
 x,c,a=traverse(r,z)
 assert x==corners[key],(key,x,corners[key])
 counts[key]=c;arrs[key]=a
O0=corners['00'];DR=tuple(corners['10'][i]-O0[i] for i in range(4));DZ=tuple(corners['01'][i]-O0[i] for i in range(4))
C=tuple(corners['11'][i]-corners['10'][i]-corners['01'][i]+O0[i] for i in range(4))
assert C==(F(0),)*4,C
assert all(a[2]==0 for a in arrs.values()),arrs
err=lambda v:v[0]-v[1]
z0=-err(O0)/err(DZ);zs=-err(DR)/err(DZ)
assert err(DZ)!=0

def point(r):
 z=z0+zs*r
 return tuple(O0[i]+DR[i]*r+DZ[i]*z for i in range(4))

left=point(F(0));right=point(F(1))
assert left[0]==left[1] and right[0]==right[1]
print('z0,zs,z1',z0,zs,z0+zs)
print('left',left)
print('right',right)
print('old',A200,V200)
print('tie corners',corners)
print('count',counts,arrs)
print('time margin',left[2]-left[3],right[2]-right[3])
print('error delta',right[0]-left[0])
print('dual',tuple(p[2]+K*p[1]+L*p[0] for p in (left,right)),HREF)
assert 0<=z0<=1 and 0<=z0+zs<=1,(z0,z0+zs)
assert left[0]==A200 and left[2]==V200,(left[0],left[2],A200,V200)
assert right[0]>left[0] and left[2]>right[2]
assert left[2]>left[3] and right[2]>right[3]
assert all(p[2]+K*p[1]+L*p[0]==HREF for p in (left,right))
assert left[2]-right[2]==(K+L)*(right[0]-left[0])
fmt=lambda x:str(x.numerator) if x.denominator==1 else str(x.numerator)+'/'+str(x.denominator)
fmtv=lambda v:[fmt(x) for x in v]
certificate={
 'schema':'EM_STAGE201_EXACT_PRIMAL_CERTIFICATE_V1',
 'classification':'PORTABLE_AUTHOR_EXACT_UNREVIEWED_NOT_ADMITTED',
 'model':{'N':N,'P':fmtv(P),'Q':fmtv(Q),'observer':['P(report Q)','Q(report P)','E_P T','E_Q T']},
 'dual':{'K':fmt(K),'L':fmt(L),'H':fmt(HREF),'bellman_state_count':len(S),'positive_gaps':len(strict),'min_positive_gap':fmt(min(strict)),'ties':ties},
 'corners':{k:fmtv(v) for k,v in corners.items()},
 'affine':{'O00':fmtv(O0),'DR':fmtv(DR),'DZ':fmtv(DZ),'mixed':fmtv(C)},
 'coin':{'z_at_r_zero':fmt(z0),'z_slope':fmt(zs),'z_at_r_one':fmt(z0+zs),'r_interval':['0','1']},
 'endpoints':{'alpha_left':fmt(left[0]),'V_left':fmt(left[2]),'alpha_right':fmt(right[0]),'V_right':fmt(right[2]),'delta_alpha':fmt(right[0]-left[0]),'slope':fmt(K+L),'H':fmt(HREF),'time_P_minus_Q_left':fmt(left[2]-left[3]),'time_P_minus_Q_right':fmt(right[2]-right[3])},
 'ordered_dfs':{'calls':counts,'total_calls':sum(counts.values()),'arrivals_R_Z_and_intersection':arrs},
 'checks':['all_680_exact_Bellman_states','1238_positive_gaps','unique_ties_R_Z','4_fraction_suffix_DPs_match_integer_full_ordered_DFS','mixed_term_zero','z(r)_linear_feasible','stage200_endpoint_contact','P_time_dominance_at_both_ends','dual_equality_at_both_ends','strict_right_support_via_compactness_and_disjoint_tie_cones'],
 'scope_notes':['external finite ternary IID helper only','no native X6 physics theorem','no Source CLAIM/Result/review/acceptance']}
out=Path(__file__).resolve().with_name('certificate201.json');out.write_text(dumps(certificate,indent=2,ensure_ascii=False)+'\n')
print('STAGE201_AUTHOR_EXACT_FULL_REAL_PASS',sum(counts.values()),'ordered DFS nodes')
