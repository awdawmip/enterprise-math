# PREFIX-1146 — Historical observer precision release and common sparse exclusion

2026-11-28. EM-DIRECT-780BBE / TASK_RESEARCH. AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_AUXILIARY_COMPUTATION / CONDITIONAL_STAGE46_APPLICATION / NOT_REVIEWED. No formal CLAIM or shared task execution mutation.

## Inputs and control

Frozen P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d and same-pin Heartbeat, joint relation and residual-fidelity companions read; ACTIVE worldview, current portable protocol and applicable role entry read. Global canonical main entry files verified against immutable 4c8d1959348756a425de3b70a19b71ae0cef4570. Predecessor 9febc74fc2c7b0ce140c2433c2e6925a83093648:research_notes/portable_direct/2026-11-28_r6_prefix1145_fifteen_observer_section.md; PREFIX-1144 e71d43a11dc63a1c73ddc1924c209a90f5aece61. All 206 predecessor archive manifest items checked. Auxiliary rational observer model, not native spatial simulation or new P000 conclusion.

Own registration r6-20261123-2358-session-start-own-v1 SUCCEEDED; recovery r6-20261128-0850-recovery-v1 identifies same own session, unclosed and custody not revoked; no execution authority granted. Owner read r6-20261128-0850-owner-v1 SUCCEEDED/error=null; fixed snapshot INV-79d09812f15413feb231b5dc58d6c0fd, as of 2026-11-28T00:52:01.364990Z, Source b12429091a908693fee5f82e9e6a57e59b824024, total 547, LEASED filter empty. Continue own direct prefix frontier; no new session or CLAIM.

## Exact increment

PREFIX-1145 proved two primitive candidate triples up to Q=10^71 were interior to its fifteen-observer affine outer model. Reuse PREFIX-1144 precision-budget separation on eight earlier moment rows: radial 10000,10400,10800,11200,11600,12000 and coupled 11200 channels 1,2. No new raw moment or anchor evaluation. Each row is recomputed using the same frozen 301-term Frobenius basis, same shared center and 12 columns, raw floor Hraw=10^120, arithmetic floor J=10^155 and final G=10^125. Each basis coefficient is bounded by one on the entire shared anchor. For radial row the valid analytic outer tail is (35/36)^k; for coupled j it is 6^(j+1)/(j+1)*(35/36)^k, as in the inherited moment bound. Reuse the sum of the four certified basis tail bounds. Each product floor is checked by outward interval endpoints at 10^260. Pay (4*(300+1)+1)/J, raw floor midpoint half-cell 1/(2Hraw), and the analytic tails; G-scale round down center and all 12 columns, then ceil the error and add 13. The 13 payments bound the independent rounding of center and 12 coefficients each of magnitude at most one. No change to the two point-conditioned rows or the five already tightened higher moment rows. The eight old rows' center, error and all columns were matched exactly against the fixture before replacement.

New e at index 2 is 50466 (old 120600466), indices 3..9 each 50014 (old 120600014): roughly 2390 and 2411-fold reductions respectively. Both old and new enclosures constrain the same true parameters, so use their intersection; no claim that the recomputed rounded zonotope is literally a subset of the old rounded zonotope.

## Common strict separation

With m, C, e the new integer rows, the inherited target is T=(-G*aj*x,G*(am*y-dj*x),0,...,0) where x=rho-r, y=c-u. For any integer n, |a*x+b*y-z|<=S where a=-G*(n[0]*aj+n[1]*dj), b=G*n[1]*am, z=n.m, S=sum_j|n.C_j|+sum_i|n_i|e_i. For candidate x=p/q-r, y=h/q-u and L>=L0=10^114, the two signed allowances are S+max(0,-a)*K/L0^2+max(0,b)*H/L0 and S+max(0,a)*K/L0^2+max(0,-b)*H/L0 respectively. This follows by taking the extrema of the rectangular signed Stage46 errors; both allowances are nonincreasing in L.

One integer normal suffices for both candidates. Use zero-based I=(0,1,2,5,6,8,11): two point rows, radial 10000, both coupled 11200, radial 11600 and radial 16000. Let A be the six leading shared columns restricted to I, arranged as a 6-by-7 matrix. Use signed maximal minors v_j=(-1)^j det(A without column j), divide by gcd, zero-extend to fifteen. Cofactor identity yields n.C_j=0 for the first six columns; pay all remaining shared columns and all independent errors. A 4551-direction sparse search found this common direction; exact signed ratios are >108 and >3, displayed 108.13220234852689 and 3.224647122060474. A floating-LP proposal search separately produced ratios 129.6481007900806 and 3.2246471220569632 with its own normals; the common cofactor certificate below is sufficient and uses no LP or floating decisions. Recursive determinant replay rechecks all 177912 predecessor lattice points and both exact prior interior witnesses before new separation. All assertions passed.

Thus under inherited Stage46 and anchor conditions, for all L>=10^114 any double anomaly satisfies b-a>=q>10^71. This is a strict finite denominator exclusion across the unbounded scale tail, not unbounded final separation. Inherited curvature rule and lower-scale coverage give first not excluded fixed dyadic windows, base 10^8, 6.931674235302037e136 (triple) and 1.8170968107390172e142 (sqrt-spacing pair), respectively 2x and 4x PREFIX-1145. Continuous integer endpoint unchanged at 4.72478e43.

## Reproduction and compact exact rows

Use the verified PREFIX-1145 archive directory (contains replay_9600_n300_gmp.py, radial1144_tight.py, coupled1144_tight.py, new_moments.txt, new_moments_1136.txt, fixture1141.json, extra_rows.json, extra_coupled_1136.json, extra_rows_1136.json, verify1145_compact.py and its inherited dependencies). The actual row-build scripts are obtained by replacing in radial1144_tight.py: moments1142.txt -> new_moments.txt, ks=[14400,16000,20000] -> ks=[10000,10400,10800], extra_radial1144_tight.json -> radial1146_low.json; separately moments1142.txt -> new_moments_1136.txt, ks=[14400,16000,20000] -> ks=[11200,11600,12000], output -> radial1146_high.json. In coupled1144_tight.py replace moments1142.txt -> new_moments_1136.txt, k=14400 -> k=11200, extra_coupled1144_tight.json -> coupled1146.json. Execute all three. The precise rows below are ordered k, channel, e, m, twelve C entries. They are the actual integer outputs; compare to the recomputed JSON rows, not to decimal logs.

```text
10000 0 50466 -5125943210838959900 -9439727292964913715644 563814399574156417 -12547204637116 543387970 0 0 66 -14 -1 0 0 0
10400 0 50014 -17950719237211986369 -33057192159364659829729 1850874067992514339 -36609963069810 1189019200 0 0 64 -13 -1 0 0 0
10800 0 50014 -39478465139111981950 -72701511035128092066755 3907417520264524189 -72451756015164 2091474020 0 0 61 -13 -1 0 0 0
11200 1 50014 1001163861896611636 -91220000364952284887 4344473217818122 -77348963365 2091906 172186817276751308897194 0 -1 -1 -1 0 0 0
11200 2 50014 74181271838798345 -2448023579049005246 146091831130612 -2621002235 65022 0 516606560948510513646727 -1 0 0 -1 0 0
11200 0 50014 -69770226902594950065 -128485077983979928035473 6713207898295903199 -119488750281447 3233474996 0 0 59 -12 -1 0 0 0
11600 0 50014 -108341802261010324161 -199516202096369446455611 10210978688576221152 -176684131356067 4589654540 0 0 57 -11 -1 0 0 0
12000 0 50014 -154415815512419118435 -284363309303879263259953 14324882355031476764 -242792438605346 6131304653 0 0 55 -11 -1 0 0 0
```

Actual standard-library replay verify1146.py, using separate recursive Laplace determinants instead of the Bareiss scan:

```python
from fractions import Fraction as F
import json,runpy
from math import gcd
D=runpy.run_path('verify1145_compact.py'); G,L,K,H,aj,am,dj,r,u,m,e,C=[D[k] for k in ('G','L','K','H','aj','am','dj','r','u','m','e','C')]
old=json.load(open('extra_rows.json'))+json.load(open('extra_coupled_1136.json'))+json.load(open('extra_rows_1136.json'))
rep=json.load(open('radial1146_low.json'))+json.load(open('coupled1146.json'))+json.load(open('radial1146_high.json'))
assert len(rep)==8
for i,(v,w) in enumerate(zip(rep,old),2):
 assert (v['k'],v.get('channel',0))==(w['k'],w.get('channel',0))
 assert (m[i],e[i],[c[i] for c in C])==(w['m'],w['error'],w['cols'])
 assert v['error']<w['error'];m[i]=v['m'];e[i]=v['error']
 for j in range(12):C[j][i]=v['cols'][j]
I=(0,1,2,5,6,8,11)
def det(M):
 if not M:return 1
 return sum((-1)**i*x*det([row[:i]+row[i+1:] for row in M[1:]]) for i,x in enumerate(M[0]) if x)
A=[[c[i] for i in I] for c in C[:6]];v=[(-1)**j*det([row[:j]+row[j+1:] for row in A]) for j in range(7)];g=gcd(*v);assert g
n=[0]*15
for i,x in zip(I,v):n[i]=x//g
dot=lambda a,b:sum(x*y for x,y in zip(a,b))
assert all(dot(n,c)==0 for c in C[:6]); a=-G*(n[0]*aj+n[1]*dj);b=G*n[1]*am;z=dot(n,m);S=sum(abs(dot(n,c)) for c in C)+sum(abs(v)*d for v,d in zip(n,e));assert S>0
for (q,p,h),bound in zip(D['lines'],(108,3)):
 x,y=F(p,q)-r,F(h,q)-u;v=a*x+b*y-z
 ratio=max(v/(S+max(0,-a)*K/L**2+max(0,b)*H/L),-v/(S+max(0,a)*K/L**2+max(0,-b)*H/L));assert ratio>bound;print('q',q,'ratio',float(ratio))
Q=10**71;d0=D['A']['d0'];L3=L2=10**8
while L3<=d0*Q*Q/(4*400000):L3*=2
while L2<=Q*Q:L2*=2
print('PASS q>',Q,'windows',float(L3),float(L2))
```

Actual last replay lines:
```
q 62079791971705189204794035436605825930158816418360040693738986967303276 ratio 108.13220234852689
q 93871880411373781997215425136755177131565090239253104802992826618837333 ratio 3.224647122060474
PASS q> 100000000000000000000000000000000000000000000000000000000000000000000000 windows 6.931674235302037e+136 1.8170968107390172e+142
```

## Next

Use tightened fifteen-row system to intersect a new global affine outer section with predecessor section, then enumerate beyond 10^71. Historical quantization payments are no longer the same bottleneck; compare the new full bounded fiber against the next remaining candidates before selecting additional raw moments or stronger correlated analytic residuals. No independent reviewer acceptance, no independent re-proof of inherited Stage46/anchor exit, no unbounded final separation or solution of B_fix,odd(32).
