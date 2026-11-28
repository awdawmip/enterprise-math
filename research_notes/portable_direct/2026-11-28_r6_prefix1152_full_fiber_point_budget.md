# PREFIX-1152 — full bounded fibers and point-budget diagnosis

2026-11-28. Continuation of PREFIX-1151 at 36d619cb4e0fd34d4c0ddd73e4f8a4688e860fa5:research_notes/portable_direct/2026-11-28_r6_prefix1151_fine_grid_joint_section.md (remote read verified blob aa5c56e57d5fb713db827c9c06558f97ae073975). Historical Researcher-ID EM-DIRECT-780BBE / TASK_RESEARCH, original own registration receipt r6-20261123-2358-session-start-own-v1 SUCCEEDED; no new CLAIM or shared task-state mutation. Fresh owner inventory request r6-20261128-1454-owner-check last observed RUNNING at publication preparation, no claim inferred. Global entry snapshot cd28421b81f9534f8a51b5c95dea4ed8db77e994; frozen P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d and joint-preservation, heartbeat and residual-fidelity companions read. This is auxiliary spectral algebra, not native spatial geometry. AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_AUXILIARY_COMPUTATION / AFFINE_OUTER_MODEL_WITNESSES / NOT_REVIEWED.

## Exact inputs and scope
PREFIX-1151-execution-evidence.zip SHA256 14b808876810812644f3ebb95c90273ed32ce9a6240b74a767d8ba7ce8689cb5; inherited PREFIX1151_SHA256SUMS checked. Use fixture1141.json, grid1150.json and rebase1151.json. Re-executed verify1151_compact.py: PASS 18 vertices, 275 complete coordinates, 51 integer points, 27 primitive; min q=3048142332814919528589209213982978583698564309667098435985031648401009046730. No change in anchor, raw moments or observation budgets. Inherited Stage46/anchor conditional spacing lower bound and dyadic window boundaries unchanged.

## Exact max-volume pivot lemma
Write U=[C,diag(e)] as 15-by-27 rational matrix (columns), with every e_i>0. Choose any 15-column invertible P, initially the independent error axes. Put T=P^{-1}U. If a nonpivot entry |T_ij|>1, replace pivot column i by column j; determinant magnitude increases by factor |T_ij|, by multilinearity. There are finitely many pivot sets, so the exact strict-increase algorithm terminates. At termination every entry of T has magnitude <=1, with the pivot block identity. The change is invertible and preserves all shared coefficients and all error axes. If b=P^{-1}(target-m), bounded fiber feasibility is equivalent to z_p=b-T_free z_free, with |z_free| and |z_p| <=1. The row inequality |b_i|<=sum_j |T_ij| <=27 is necessary; if violated, the corresponding row of P^{-1} is an exact separating functional. Otherwise the min-infinity-norm LP in free coordinates has bounded matrix entries and bounded RHS. No claim about its numerical optimum is necessary: rationalize free coordinates, solve pivot equations exactly, and verify every equality and box constraint; alternatively verify a dual support inequality exactly. For signed scale, append two centered interval columns, increasing 27 to 29 in this argument.

## Actual computation
Old LP at G=10^140 returned HiGHS model error. Exact determinant-improving pivot took six swaps, giving pivot indices (zero-based) [12,13,14,15,16,17,18,19,2,21,1,3,0,4,5]. All 27 candidates have exact zero-scale witnesses satisfying all 15 equations and 27 coefficient bounds. For minimum q the strict slack 1-max|z| = 0.39715313328870305 (decimal approximation); across all 27 min slack 0.008626180034304291 > 0.008 exactly. Because all independent e_i>0, every witness belongs to the interior of the zonotope. Thus no linear support inequality of this unchanged fine-grid affine outer model can exclude any of the 27 even at zero scale. This is not a claim about the true nonlinear spectrum or simultaneous full-fiber feasibility in every historical rounding model. A second run with signed-scale variables (29 coefficients) also found all 27 strictly feasible, min slack 0.023409123806; zero-scale certificates alone already prove the stated obstruction.

## Counterfactual budget diagnosis (not a new physical error bound)
Define A=(-G aj,-G dj,0,...), B=(0,G am,0,...), x=p/q-r, y=h/q-u and target=A x+B y. For L>=L0, the necessary scale correction is delta_rho in [0,K/L0^2], delta_c in [-H/L0,0]. Therefore target lies in m+U[-1,1]^{27} -A[0,K/L0^2]+B[0,H/L0]. Center the last two intervals as columns s=-A K/(2L0^2), t=B H/(2L0), with center m+s+t; both scale signs paid. Replace ONLY e_0,e_1 by e_0/10,e_1/10 as a hypothetical experiment. Using row index 1 of the exact inverse of the same selected pivot matrix yields support ratio |n.(target-m-s-t)|/(sum_j |n.U_j|+|n.s|+|n.t|)=5.539387215445228 >5.539. Thus tenfold tighter certified point observation error radii with unchanged centers/columns would suffice to exclude the minimum q at all L>=L0. It is not established that those tightened bounds hold. Extra diagnostic runs on minimum q: point rows /1000 ratio 407.5250563, moment rows only /1000 still feasible with strict slack 0.3206215593, moment rows only /10^6 excluded at ratio 456.2132335. These are altered-model sensitivity experiments, not changes to physical/analytic inputs. Prioritize the two point-observation budgets or targeted shared residual refinement; no need for repeat scanning of the current 15-observer model. Actual bound remains PREFIX-1151; unbounded separation, B_fix,odd(32), anchor exit and independent review open.

## Executed compact exact verifier
Extract the predecessor archive, verify its manifest and run verify1151_compact.py for complete candidate coverage, then save the following as verify1152_compact.py. Uses exact SymPy rational inverse and Fraction arithmetic, without LP; the 13 nonzero free-coordinate rows below and implicit zero rows reconstruct all 27 full witnesses. Execution output:
PASS zero-scale 27 0.39715313328870305 0.008626180034304291
PASS hypothetical point /10 5.539387215445228
Local executed verifier SHA256 8d5d963f1b0f59e8134c56d2cdccacdf6e6cc41d5b2cde4baa9e2e5812a6b2f3.

```python
from fractions import Fraction as F
import json
from sympy import Matrix
D=json.load(open('fixture1141.json')); E=json.load(open('grid1150.json'))
G,L=10**140,D['L']; K,H,aj,am,dj,r,u=[F(D[k]) for k in ('K','H','aj','am','dj','r0','u')];m,e,C=[E[k] for k in ('m','e','cols')];N=len(m)
A=[-G*aj,-G*dj]+[0]*(N-2);B=[0,G*am]+[0]*(N-2)
scale=[[-v*K/(2*L**2) for v in A],[v*H/(2*L) for v in B]]
lines=json.load(open('rebase1151.json'))['runs'][-1]['lines'];assert len(lines)==27
piv=[12,13,14,15,16,17,18,19,2,21,1,3,0,4,5]
free=[6,7,8,9,10,11,20,22,23,24,25,26]
Dfree={
3:[-822838671801,822838671801,-822838671801,-822838671801,0,0,-822838671801,822838671801,-822838671801,-822838671801,0,0],
4:[0,0,0,0,0,0,-187268882459,257243213785,-257243213785,0,0,0],
5:[-250335459416,0,250335459416,250335459416,0,0,250335459416,-250335459416,250335459416,250335459416,0,0],
6:[-708388582725,0,708388582725,708388582725,0,0,708388582725,-708388582725,708388582725,708388582725,0,0],
7:[0,0,0,0,0,0,-822519226400,897170908809,-897170908809,0,0,0],
11:[0,0,0,0,0,0,-512959948336,585332344416,-585332344416,0,0,0],
16:[-501015205623,0,501015205623,501015205623,0,0,501015205623,-501015205623,501015205623,501015205623,0,0],
17:[0,0,0,0,0,0,-591748699591,664701217594,-664701217594,0,0,0],
18:[-813587117929,0,813587117929,813587117929,0,0,813587117929,-813587117929,813587117929,813587117929,0,0],
19:[0,0,0,0,0,0,-655317418759,728737993521,-728737993521,0,0,0],
21:[0,0,0,0,0,0,-701377945004,775137663623,-775137663623,0,0,0],
22:[0,0,0,0,0,0,-387849287352,459300493083,-459300493083,0,0,0],
24:[0,0,0,0,0,0,807682808468,-807682808468,807682808468,357343474729,0,0]}
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def target(line):
 q,p,h=line;x,y=F(p,q)-r,F(h,q)-u;return [a*x+b*y for a,b in zip(A,B)]
def cols(err):return C+[[err[i] if i==j else 0 for i in range(N)] for j in range(N)]
U=cols(e);MI=Matrix([U[i] for i in piv]).T.inv();slacks=[]
for k,line in enumerate(lines):
 v=[a-b for a,b in zip(target(line),m)]; z=[F(0)]*27
 for i,w in zip(free,Dfree.get(k,[0]*12)):z[i]=F(w,10**12)
 rhs=[v[i]-sum(z[j]*U[j][i] for j in free) for i in range(N)]
 for i,w in zip(piv,MI*Matrix(rhs)):z[i]=F(w)
 assert all(sum(z[j]*U[j][i] for j in range(27))==v[i] for i in range(N))
 slack=1-max(map(abs,z));assert slack>F(8,1000);slacks.append(slack)
print('PASS zero-scale',len(slacks),float(slacks[0]),float(min(slacks)))
# Counterfactual error-budget diagnosis; both scale columns retained.
U=cols([F(v,10) if i<2 else F(v) for i,v in enumerate(e)])+scale
M=Matrix([U[i] for i in piv]).T.inv();n=list(map(F,M.row(1)))
v=[a-b-s-t for a,b,s,t in zip(target(lines[0]),m,*scale)]
ratio=abs(dot(n,v))/sum(abs(dot(n,c)) for c in U);assert ratio>F(5539,1000)
print('PASS hypothetical point /10',float(ratio))
```
