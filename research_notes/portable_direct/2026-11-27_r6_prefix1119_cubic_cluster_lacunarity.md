# PREFIX-1119 — cubic lacunarity of triple near-hit clusters

2026-11-27. Continuing the directed independent Stage46 frontier of EM-DIRECT-780BBE, TASK_RESEARCH, own RA-0ABD84561C86E53067DB0322; original session-start request r6-20261123-2358-session-start-own-v1 returned SUCCEEDED. Author proof, NOT_REVIEWED; no new CLAIM or shared Task mutation. Current owner query r6-20261127-0548-leased-read was RUNNING at the observation before this note. Frozen P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d and joint observer/time companions. Same Stage46 X6 signed BRC carrier as PREFIX-1118 (chart O, incoming -e1, signed reversal -5 with phase cover 5q, other weights 1, next incoming -d, both orientations Link{O,e1} blocked without renormalization, exactly two negatives). Retain cell, port, sign/phase, branch order and multiplicity. This is auxiliary arithmetic on the inherited signed BRC boundary certificate, not a new native propagation or a native spatial plane. d in this note is the inverse-scale coefficient.

Parent: 5041d0cc7e9c5a990f19fa0937b8b2dbdd75d6c2:research_notes/portable_direct/2026-11-27_r6_prefix1118_determinant_collinearity.md. Parameter input: 897771dcc60212121f1e222bf139da189cce0078:research_notes/portable_direct/2026-11-27_r6_prefix1117_root_8800_result.json. Inherited lattice implementation: 2ec540692bf1ba695b60416903db654f797f3e67:research_notes/portable_direct/2026-11-27_r6_prefix1116_convergent_lattice.py. Previous 8400/8800 anchor command exits remain unconfirmed. This run verifies auxiliary arithmetic only.

## 1. Cubic lacunarity theorem

Let f(m)=rho*m+c+d/m, d>0, E>0. A true near hit is an integer (m,j) with |f(m)-j|<=E/m^2. Assume the PREFIX-1118 collinearity condition d/10+2E/L<1, 2E/L^2<1, and consider a half-open dyadic window [L,2L). A triple window has at least three distinct true hits. Let p/q be its primitive line slope (q>0). Assume q>16E/d for every triple window under consideration. Put C=16E/d, K=9d/8, B=KC=18E.

Then:
(a) q^2<=CL, and d/(8L^2)<rho-p/q<K/L^2.
(b) If another triple window starts at L'>=L with the SAME slope, L'<3L. In a fixed doubling grid, each slope appears in at most two windows.
(c) If the later triple window has a DISTINCT slope p'/q', then L'>=L^3/B^2. In particular the normalized starts y=L/B of distinct consecutive slope groups obey y_next>=y^3.

Proof: By PREFIX-1118 all true hits in the window lie on one integer relation line qj-pm=h. For three distinct scales a<b<z, the inherited PREFIX-1117 curvature inequality gives (b-a)(z-b)<=16EL/d, and both gaps are multiples of q, so q^2<=CL. For any two hits the signed relation identity from PREFIX-1118 gives delta=rho-p/q=d/(ab)+(e_b-e_a)/(b-a), where e_m=f(m)-j_m. Therefore |delta-d/(ab)|<=2E/(qL^2). Since q>16E/d, the error is strictly less than d/(8L^2), giving (a). Equal slopes at two scales have equal positive delta, and d/(8L^2)<delta<K/L'^2 gives L'<3L, proving (b). For distinct reduced slopes, rational separation gives 1/(qq')<=|p/q-p'/q'|=|delta-delta'|<=K/L^2, since both deltas are positive and L'>=L. Thus q'>=L^2/(Kq)>=L^(3/2)/(K sqrt(C)); q'^2<=CL' implies L'>=L^3/(KC)^2. This proves (c). The integer relation coordinates retain the primitive slope, intercept and residual; this proof does not identify different native states.

For a fixed doubling grid with starts >=L0>B and q>16E/d, the number of DISTINCT triple slopes with starts <=X is at most 1+floor(log_3(log(X/B)/log(L0/B))) for X>=L0 (and 0 if X<L0). Indeed, distinct first starts in chronological order satisfy the cubic recursion; each slope contributes at most two starts. In particular triple windows are O(log log X), with no irrationality-exponent hypothesis. The result limits clusters, not isolated hits or pairs, and does not establish eventual separation.

For fixed real rho,c,d>0,E>0 the small-denominator hypothesis holds eventually, even without a quantitative certificate. For q bounded, the pair estimate forces p/q->rho along unbounded windows. Only finitely many reduced p/q of bounded denominator lie in a bounded neighborhood of rho; hence a persistent such slope must equal rho. The intercept h/q then approaches c by the signed two-hit identity, and with fixed q it must eventually equal c. The residual is then d/m, which exceeds E/m^2 for m>E/d. This rules out unbounded small-q pairs; no new assumption on rho is required. The collinearity condition holds eventually whenever d<10. If d>=10, no such general claim from this dyadic argument is made.

## 2. Explicit Stage46 small-denominator certificate

Let R=[rho_l,rho_u], T=[d_l,d_u] be the frozen 8800 output. Set L0=10^8, E=400000, Q0=floor(16E/d_l)=660415. Use reduced rational P/Q=127377638/5941111, a convergent of the midpoint of R, Q>Q0. For each reduced p/q with q<=Q0, |P/Q-p/q|>=1/(Qq). Let eta=max_{r in R}|r-P/Q|. Then q|rho-p/q|>=1/Q-Q0*eta. A pair of true hits instead requires q|rho-p/q|<=(d_u Q0+2E)/L^2. The exact positive margin
1/Q-Q0*eta-(d_u Q0+2E)/L0^2 > 1.6257e-7
excludes ALL such q for ALL L>=L0, not only a sampled set. Also 1-d_u/10-2E/L0>0 and 2E/L0^2<1, so the cubic theorem applies to every Stage46 dyadic window L>=10^8 in the inherited parameter model. B=7200000 exactly. No new high-order anchor needed. Moreover q^2|rho-p/q|<=18E/L<1/2 for L>=10^8, so by the usual Legendre continued-fraction criterion every triple slope is a convergent of rho; the cubic gap proof itself does not depend on that criterion.

## 3. Finite exact sweep and consequence beyond it

The attached PREFIX-1118 execution archive's six manifest entries passed SHA256 verification. Reused the exact lattice sweep and all rational intervals, now rerunning ALL 107 consecutive dyadic windows [10^8,M), M=16225927682921336339157801028812800000000. The union is exactly the previous 122 candidate pairs, no new pairs. Recomputed all threshold intervals and strict adjacent separation. Thus at most ONE true near hit in this whole finite range for any fixed true parameter triple in the box, although the individual candidate signs remain uncertified. In particular no triple window on this doubling grid before M. If a first triple window occurs at a start >=M, the next DISTINCT triple slope must occur at a start >=M^3/(7200000)^2 = approximately 8.240690725003511e106. Up to 10^106 at most one slope group (at most two dyadic triple windows) can occur beyond M; up to 10^1000 at most four slope groups (eight triple windows). These are conditional upper bounds, not evidence of any actual triple window. Continuous certified endpoint for the integer formula stays 4265326180744162387203315935318273935179 exclusive; 122 individual signs remain open. No new anchor, CT, or native propagation ran.

Exact verification log:
small_q 660415 witness 127377638 5941111 margin 1.625764833215643e-07 B 7200000
full_windows 107 pairs 122 M 16225927682921336339157801028812800000000 next_min 8.240690725003511e+106
groups from L0 {'40': 4, '100': 5, '200': 5, '1000': 7} groups from M {'40': 0, '41': 1, '100': 1, '106': 1, '107': 2, '200': 2, '1000': 4}
result sha256 dbc79c79600e17212042d945cf909ac02adebe9fb04058d6c9c660199132b579

Actual executed verifier follows. Inputs from PREFIX-1118 execution archive, with manifest preserved. root_8800_result.json and prefix1116_lattice.py also have the immutable GitHub paths above.

```python
from fractions import Fraction as F
from math import floor, gcd
from pathlib import Path
import hashlib,json
from prefix1116_lattice import load,convergent,E,sweep,expand
R,C,T=load('root_8800_result.json'); L0=10**8; B=18*E
Q0=floor(F(16*E)/T[0])
p,q=convergent(sum(R)/2,10**7)
assert q>Q0 and gcd(p,q)==1
eta=max(abs(v-F(p,q)) for v in R)
margin=F(1,q)-Q0*eta-(T[1]*Q0+2*E)/L0**2
assert margin>0
assert 1-T[1]/10-F(2*E,L0)>0 and F(2*E,L0**2)<1
assert L0>36*E
prev=json.loads(Path('prefix1117_result.json').read_text()); old=json.loads(Path('prefix1118_result.json').read_text())
# Full inherited dyadic-window auxiliary sweep; no anchor replay.
M=prev['end']; w=sweep((R,C,T),L0,M)
pairs=sorted(p for x in w for p in expand(x)); assert len(pairs)==122
assert pairs==sorted((a['m'],a['j']) for a in old['ordered'])
z=sorted(((F(j)-C[1]-T[1]/m-F(E,m*m))/m,(F(j)-C[0]-T[0]/m+F(E,m*m))/m,m,j) for m,j in pairs)
assert all(a[1]<b[0] for a,b in zip(z,z[1:]))
assert w[0]['L']==L0 and w[-1]['H']==M-1
assert all(a['H']+1==b['L'] for a,b in zip(w,w[1:]))
# Every true hit is among pairs; disjoint thresholds imply at most one hit in the entire range.
# If first triple window starts >=M, a distinct later slope must start >= M^3/B^2.
next_min=F(M**3,B**2)
assert next_min>10**106
# A bound on number of distinct triple slopes for dyadic starts <= X.
def group_bound(X, start):
    if X<start:return 0
    k=1; y=F(start,B); Y=F(X,B)
    while y**3<=Y:
        y=y**3;k+=1
    return k
out={'Q0':Q0,'rational_witness':[p,q],'rho_approx_error':str(eta),'small_q_exclusion_margin':str(margin),'determinant_margin':str(1-T[1]/10-F(2*E,L0)), 'B':B,'full_windows':len(w),'full_pairs':len(pairs),'full_range_end':M,'next_distinct_triple_slope_min_L':str(next_min),'group_bounds_from_L0':{str(k):group_bound(10**k,L0) for k in [40,100,200,1000]},'group_bounds_from_M':{str(k):group_bound(10**k,M) for k in [40,41,100,106,107,200,1000]},'input_sha256':{name:hashlib.sha256(Path(name).read_bytes()).hexdigest() for name in ['root_8800_result.json','prefix1117_result.json','prefix1118_result.json','prefix1116_lattice.py']}}
Path('prefix1119_result.json').write_text(json.dumps(out,indent=2)+'\n')
print('small_q',Q0,'witness',p,q,'margin',float(margin),'B',B)
print('full_windows',len(w),'pairs',len(pairs),'M',M,'next_min',float(next_min))
print('groups from L0',out['group_bounds_from_L0'],'groups from M',out['group_bounds_from_M'])
print('result sha256',hashlib.sha256(Path('prefix1119_result.json').read_bytes()).hexdigest())
```

## 4. Next

Refine the rho-only root interval by the PREFIX-1118 target factor >=24209 to resolve the 122 individual candidates (at most one remains under the gap criterion); verify actual anchor completion, not merely a narrowed display. Investigate two-hit windows and isolated hits, and a structural lower bound on coupled approximation from the actual signed BRC spectrum. The mother B_fix,odd(32), all-scale separation, exact zero classification and independent review remain open. No Task claim or protected runtime write made. Activity observation audit remains distinct from file readback.
