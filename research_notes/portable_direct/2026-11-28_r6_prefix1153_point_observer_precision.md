# PREFIX-1153 — certified point-observer precision and common separation

2026-11-28. Continuation of PREFIX-1152 at 7d118f0f3e337138500462aca9d0e245c8d081c8:research_notes/portable_direct/2026-11-28_r6_prefix1152_full_fiber_point_budget.md, verified blob e2a5d75445488b705443025d8094a82c25413204. Own research identity EM-DIRECT-780BBE / TASK_RESEARCH; original managed registration recovery verified (session MCP-f6d93209fc8e4c5bb2c3b44f69a47174, original request r6-20261123-2358-session-start-own-v1 SUCCEEDED; no runs, not closed/revoked); no formal CLAIM or shared task mutation. Owner query r6-20261128-1547-owner-check SUCCEEDED/error=null; INV-4ea4914ebf50167015cbe195fa39595f as_of 2026-11-28T07:48:24.645610Z, Source 483c6d0886aab52f6a77a69971ef85b906b552b4, 547 tasks, LEASED filter empty, source unchanged at completion; no write authority inferred. Global entry blobs verified at 51d9640723b560fb823de54e9e48735bd3626201; frozen P000 V5 and companions f42f2906d77f24085c123f3ccfe9667d41caa96d. Auxiliary spectral algebra only, not a new native computation. AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_AUXILIARY_COMPUTATION / CONDITIONAL_STAGE46_APPLICATION / NOT_REVIEWED.

## Input and result
Inherited PREFIX-1152-execution-evidence.zip SHA256 e685e9fade6f87a4c27209ea5570c7e09c50de2c0c032e372bdf6d7636006391; PREFIX1152_SHA256SUMS checked. Same 9600 anchor packet, same six coefficients and twelve common residual columns, same thirteen moment observations and their budgets. No raw moment or anchor regeneration. Re-evaluate only two point rows, at the same reference (r,u) of fixture1141.json and point1138.json, using 401 Frobenius coefficients (indices 0..400) rather than 301. Point evaluation arithmetic grid 10^300 rather than 10^180, output grid unchanged 10^140. Original full-fiber obstruction at old budgets is respected. All 27 primitive candidates from PREFIX-1151 now strictly excluded with both signed scale columns. Conditional on inherited Stage46, anchor and affine transfer bounds: for L>=10^114, b-a>=q>10^76. First unexcluded dyadic triple and sqrt-gap pair windows approximately 1.1908525658859223e147 and 1.560874275157996e152, both 16 times previous. No claim beyond these inherited hypotheses.

## Why longer truncation alone failed
At the same 10^180 arithmetic grid, N=400 actually worsens the certified point radius (integer payments at 10^140 including transfer: 102500560293474113024513140010512682563811778 and 2901870208159799396966458652565936097043459479). N=300 re-evaluation at 10^180 gives 778398383415451129240146317115310 and 1239925114392458660351962113511037781098, consistent in scale with old rows. These are recorded experiments, not new tighter bounds. Horner interval multiplication at |t|>1 amplifies absolute rounding errors: for fixed t, each step contributes at most 2/J (coefficient and product floor/ceil), so a degree d recurrence has error bounded by (2/J) sum_{k=0}^d |t|^k, in addition to input enclosure uncertainty. Interval Horner pays that uncertainty directly; no use of the fixed-point expression as an interval error bound. Increasing polynomial order without increasing arithmetic precision can therefore make the outer bound worse. At N=400 and arithmetic grid 10^300 the exact interval computations yield point payments [14,14], with affine transfer payments [1,1]; final e=[15,15]. Old point budgets (normalized) improve by approximately 5.1893e31 and 8.2662e37. All center and column changes are recomputed, not presumed equal to the historical rounded entries. Retain intersection with prior valid constraints.

## Tail certification
Reuse the frozen Frobenius recurrence, indicial roots and exact row polynomials from replay_9600_n300_gmp.py. In the scaled basis recurrence the denominator is >= n-2 for a in {0,1/2,1,2}, and the numerator bound is pbound+(n+2)qbound times the largest of the previous three norms. The ratio (pbound+(n+2)qbound)/(n-2) decreases for n>=401 and is verified <1 at n=401 by exact arithmetic. Thus T=max infinity norms of last three computed vectors bounds every subsequent scaled coefficient by induction. The unscaled transform has norm 4; the two integrated components have the inherited 64*T*2^-n majorant (their recurrence uses current and preceding transformed coefficients; the denominators n+a-k are positive for n>=401). For t<=127/100 the j-th derivative tail is at most
64*T*2^(-N-1)*fall(2a+2(N+1),j)*Tmax^(2a+2(N+1)-j)/(1-Rj),
where Rj=(Tmax^2/2)*((2a+2(N+1)+3-j)/(2a+2(N+1)+1-j))^j <1, verified for j=0..5. Product-rule payment sums binomial(j,k)*rowbound[k]*tail[j-k]. Polynomial derivatives and coefficients are evaluated by rational outward interval Horner; sqrt reference is enclosed by integer isqrt with exact square comparisons. The joint center and twelve columns are enclosed independently by interval endpoints, then their radii summed. The 13 additional output-grid units cover floor rounding of the center and all twelve columns with bounded shared coefficients. This certifies the point rows, not a new anchor solution. Affine transfer payments are recomputed at 10^140 directly from the inherited exact derivative intervals, not merely scaled from their previous coarse rounding.

## Exact output, coverage and common separating row
The new two point centers at 10^140:
[1578749725436294200191847058759780975920180278839605431595, -8016679782115749068661075192021604216796071406761272866604]
The twelve point-column pairs, in unchanged order:
[[3744138645775498910841297928701976010966640315132395648704952,-87125244309961656188605995439254644350120196791734787511256556],[-161039656349520894471888359937205864380222551746285427779,3746573643488776666579887859681069553495355541839471171719],[2298254077145580893797380295013148626307678016071292,-53458267472769732129352373972486955516397284220069013],[-47952155714854405058160188075337577451627147821,1115182088175091721930947313324566804011682510034],[970258271083964521363312982548236062773145684698911977,-72120495286988764488827521413216860724179618319695084565],[-466583415180187615239670236197498944780634026609602556370,40347985749191228916185797857499750580988601418326449583397],[-4422552409728386200061043768,-14544658619171737075172089477884],[-30551863247001163946004322734910,2239318452415096038106073349635848],[-36535640931316124580532010096929,2363560184834305474465711309663844],[814480300480595744645721815741677,-19198820539636586491708170189564206],[5395617291183169955729673973417,-401062895330366979045897446876724],[-1525853534519760170149199066318,131948789140695908732028310678405]].

Re-executed verify1151_compact.py: 18 vertices, 275 complete integer coordinates, 51 feasible integer points, 27 primitive. The old certified search covers every relevant denominator <=10^76 under inherited q0 and scale. Set A=(-G aj,-G dj,0,...), B=(0,G am,0,...), s=-A K/(2L0^2), t=B H/(2L0), target=A(p/q-r)+B(h/q-u). Use U=[C,diag(e),s,t] and center m+s+t, keeping all 29 coefficients. Seven max-volume swaps give pivot indices [5,0,14,15,16,17,18,19,3,21,28,23,1,4,2] (zero-based). Independent exact SymPy inverse of these columns supplies a common functional n=row 11 (zero-based). For every one of the 27 primitive targets, |n.(target-m-s-t)| / sum_j |n.U_j| > 9526225. Exact all-pivot best ratios range 9526225.931300683 to 221245407.11621046 (display decimals only). Common row 11 minimum equals the lower value. No LP used for exclusion or independent verification. The old complete enumeration plus these strict inequalities proves the stated conditional spacing result. The affine outer model still need not be the exact nonlinear spectrum. New joint parameter polygon not computed in this unit. Next: intersect the new point-row model with the old parameter polygon, rebase with the observation-adaptive integer coordinates, and extend q beyond 10^76. Inherited anchor exit, independent review, unbounded separation and B_fix,odd(32) open.

## Reproduction (executed code)
Run from the verified predecessor evidence archive. Save the first block as point1153.py (SHA256 8ad4b84eeb60132b0841b84c4205f3ee8695e1f6148d616aa6eadb74d386c9f8). Output point1153.json SHA256 e63d78a63e887a1fb1dee9e53366c9bebc92ce2d4ded717d963672fe5d605280. The second block is verify1153.py (SHA256 1b59d169ed0fe50e9645dcc189b4aafaa19544ad115b12949eeaa4da7ce48827). Python Fraction and SymPy; no new native computation.
```python
"""Auxiliary observer re-evaluation on frozen BRC-derived recurrence, N=400."""
from pathlib import Path
source=Path('replay_9600_n300_gmp.py').read_text().split('def moments(a,N):')[0]
assert source.count('N=300')==1
exec(source.replace('N=300','N=400'))
exec(Path('root_joint_compact.py').read_text().split('# Point enclosure')[0].split('from replay_9600_n300_gmp import *\n')[1].replace('G=10**180','G=10**300'))
D=json.load(open('fixture1141.json')); r,u=F(D['r0']),F(D['u'])
l=isqrt(floor(36*G*G/(1+r)));tr=I(F(l,G),F(l+1,G));assert tr.a**2<=36/(1+r)<=tr.b**2 and t.a<=tr.a<=tr.b<=t.b
print('point basis ready',flush=True)
fs=[]
for j in range(3):
 row=[]
 for i in range(6):
  v=grid_horner([grid_pair(a) for a in dp(pp[i],j)],tr);e=sum(comb(j,k)*rowbound[k]*tails[i][j-k] for k in range(j+1));row.append(v+I(-e,e))
 fs.append(row)
D0=198/tr**2+216/(4-tr**2)+216/(16-tr**2);alpha=36/tr**2-2+(1-tr**2/36)*D0/2;beta=9/tr-tr/4
rows=[fs[0],[beta*v+(alpha-u)*w for v,w in zip(fs[2],fs[1])]]
centers=[sum((a*v for a,v in zip(cc,row)),I(0)) for row in rows]
colI=[tuple(sum((row[i]*inv[i][j] for i in range(6)),I(0)) for row in rows) for j in range(6)]+[tuple(row[i]*dr[i] for row in rows) for i in range(6)]
mid=lambda v:(v.a+v.b)/2;rad=lambda v:(v.b-v.a)/2;S=10**140
m=[floor(mid(v)*S) for v in centers];C=[[floor(mid(v)*S) for v in row] for row in colI];e=[ceil(S*(rad(centers[i])+sum(rad(v[i]) for v in colI)))+13 for i in range(2)]
ns={};exec(Path('verify_section.py').read_text().split('assert A[1]<0')[0],ns)
T,R,C0,A,D1,s,c0=[ns[k] for k in ('T','R','C','A','D','s','c0')];mul,mag,sub=[ns[k] for k in ('mul','mag','sub')];DG=tuple(x+y for x,y in zip(D1,mul(s,A)));J=(-T[1]**3/72,-T[0]**3/72);AJ=mul(A,J);DJ=mul(DG,J);am,aj,dj=[F(D[k]) for k in ('am','aj','dj')];assert (am,aj,dj)==(sum(A)/2,sum(AJ)/2,sum(DJ)/2)
transfer=[ceil(S*mag(sub(AJ,aj))*mag(sub(R,r))),ceil(S*(mag(sub(A,am))*(mag(sub(C0,c0))+abs(u-c0))+mag(sub(DJ,dj))*mag(sub(R,r))))]
print('point errors',e,'transfer',transfer,flush=True)
E=json.load(open('grid1150.json'));old=[F(v,S) for v in E['e'][:2]];E['m'][:2]=m;E['e'][:2]=[a+b for a,b in zip(e,transfer)];E['cols']=[v+c[2:] for v,c in zip(C,E['cols'])]
print('total errors',E['e'][:2], 'improvement',[float(a*S/b) for a,b in zip(old,E['e'][:2])],flush=True)
json.dump(dict(N=N,point_m=m,point_cols=C,point_error=e,transfer=transfer,m=E['m'],e=E['e'],cols=E['cols']),open('point1153.json','w'),indent=2)
```

```python
from fractions import Fraction as F
from sympy import Matrix
import json,runpy
R=runpy.run_path('verify1151_compact.py')
D=R['D']; G,L=10**140,D['L']; K,H,aj,am,dj,r,u=[F(D[k]) for k in ('K','H','aj','am','dj','r0','u')]; E=json.load(open('point1153.json'));m,e,C=[E[k] for k in ('m','e','cols')]; N=len(m)
old=json.load(open('grid1150.json'));assert e[:2]==[15,15] and m[2:]==old['m'][2:] and e[2:]==old['e'][2:] and all(a[2:]==b[2:] for a,b in zip(C,old['cols']))
A=[-G*aj,-G*dj]+[0]*(N-2);B=[0,G*am]+[0]*(N-2);scale=[[-v*K/(2*L**2) for v in A],[v*H/(2*L) for v in B]]
U=C+[[e[i] if i==j else 0 for i in range(N)] for j in range(N)]+scale
piv=[5,0,14,15,16,17,18,19,3,21,28,23,1,4,2];MI=Matrix([U[i] for i in piv]).T.inv()
dot=lambda a,b:sum(x*y for x,y in zip(a,b))
center=[a+b+c for a,b,c in zip(m,*scale)]
lines=R['lines'];assert len(lines)==27 and lines==[tuple(v) for v in json.load(open('rebase1151.json'))['runs'][-1]['lines']]
vectors=[[a*(F(p,q)-r)+b*(F(h,q)-u)-c for a,b,c in zip(A,B,center)] for q,p,h in lines]
ratios=[]
for row in MI.tolist():
 n=list(map(F,row));s=sum(abs(dot(n,c)) for c in U);assert s>0
 ratios.append([abs(dot(n,v))/s for v in vectors])
best=[max(row[i] for row in ratios) for i in range(len(lines))];assert min(best)>9526225
j=max(range(N),key=lambda j:min(ratios[j])); print('COMMON row',j,'min',float(min(ratios[j])))
print('PASS all',len(best),'min/max',float(min(best)),float(max(best)))
d0=F(D['d'][0]);q=10**76;L3=L2=10**8
while L3<=d0*q*q/(4*400000):L3*=2
while L2<=q*q:L2*=2
print('WINDOWS',float(L3),float(L2))
```

Observed final output:
COMMON row 11 min 9526225.931300683
PASS all 27 min/max 9526225.931300683 221245407.11621046
WINDOWS 1.1908525658859223e+147 1.560874275157996e+152
