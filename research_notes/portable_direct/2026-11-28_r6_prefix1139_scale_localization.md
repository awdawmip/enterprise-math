# PREFIX-1139 — Exact scale localization and sliced integer-coordinate enumeration

Date 2026-11-28. R6 informed direct research; AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_AUXILIARY_COMPUTATION / CONDITIONAL_STAGE46_APPLICATION / NOT_REVIEWED. Frozen science P000 V5 and companions at f42f2906d77f24085c123f3ccfe9667d41caa96d. Continue PREFIX-1138 at 60d471d5de2cf566c263b759725f61eb59b5c816:research_notes/portable_direct/2026-11-28_r6_prefix1138_point_conditioned_section.md. Use its Stage46 analytic/integral and 9600 shared anchor assumptions without redoing them; inherited anchor audit pending. Current global entry verified at a5bf1e4802a2d2b3297144262794bf288d6ed6fa. Own original registration r6-20261123-2358-session-start-own-v1 SUCCEEDED, managed session recovery metadata nonrevoked, no formal run/claim. Owner inventory r6-20261128-0147-owner-read was RUNNING at last observation before this publication, no current owner conclusion inferred. No shared task mutation or ownership acquisition. This is an independent auxiliary calculation from the existing R6 frontier.

## 1. Scale localization theorem

Let P be the nonempty compact convex polygon in auxiliary algebraic (rho,c) coordinates certified by the 43 point-conditioned joint observations of PREFIX-1138. Set q0=544447235321021556325566186117974922693, E=400000, K=d_hi+2E/q0, H=2K. Its necessary relation region for L>=10^100 is
P_L = P + [-K/L^2,0] x [0,H/L].
Every genuine pair must have q0<=q, gcd(p,q)=1, (p/q,h/q) in P_L and gap>=q. These are inherited premises, not independently proved Stage46 conclusions here.

Let N consist of all outward edge normals of P together with +/- coordinate unit directions. For n=(a,b) write z=h_P(n). Then the exact membership test for r=(p/q,h/q) is
a*p+b*h <= q*(z+max(0,-a)*K/L^2+max(0,b)*H/L)
for all n in N. Proof: the support function of a Minkowski sum is additive, and the edge normal directions of a sum of two full-dimensional polygons lie in the union of their edge normal directions (the exposed faces are sums; if neither is an edge, their sum is a vertex). Thus all facet inequalities of P_L appear. Axis normals handle the rectangle. This avoids constructing a new polygon per scale.

Define D_n=a*p+b*h-z*q, A_n=q*max(0,-a)*K, B_n=q*max(0,b)*H. For D_n<=0 the inequality is automatic. For D_n>0 it is exactly D_n L^2 <= B_n L+A_n, with largest allowable real L equal to (B_n+sqrt(B_n^2+4D_n A_n))/(2D_n), including zero if A_n=B_n=0. The minimum of these upper limits is the exact cutoff of this necessary-region model. If there are no D_n>0, the rational point is in P itself and survives every positive L. Integer cutoff can be obtained by monotone rational bisection and certified with neighboring integer tests, without evaluating square roots. This is a scale-independent characterization of the outer relaxation, not actual fixed-spectrum anomaly existence.

## 2. Exact sliced coordinate enumeration

Reuse the unimodular integer transform n=V(q,p,h), W=V^-1 from PREFIX-1138. For each row v=(a,b,f) of V, bound n_i by extrema of q*(a+b*r+f*c) at q=q0,Q and vertices of P_L, then ceil the minimum and floor the maximum. This is complete because the expression is affine in (r,c) for fixed q and affine in q for fixed (r,c). Each inequality of P_L and each q-bound becomes an integer linear inequality A dot n<=B after substitution Wn and positive denominator clearing. Fix the two coordinates with the smallest ranges. For each such pair, all remaining-coordinate constraints reduce to a single closed integer interval: use floor(rhs/A_k) when A_k>0, ceil(rhs/A_k) when A_k<0; when A_k=0 reject iff rhs<0. Intersect with the original interval and enumerate it, then check gcd(p,q)=1. No floating-point exclusion, no dependence on a heuristic LLL result beyond verified unimodularity. Complexity is proportional to outer coordinate pairs times number of inequalities, plus surviving integer points; input transformation, support construction, and output reconstruction are included. An independent full-box verifier uses the support inequalities of section 1 rather than Minkowski hull clipping.

## 3. Exact results

Reconstructed the 43-direction section from prior archived source inputs, not just a saved polygon. Checked all 120 files of the PREFIX-1138 SHA256 manifest. The two scripts extend1139.py and verify1139.py executed successfully. Targeted section: 16 vertices; rho width 4.101624829506882e-101; c width 1.9683738383647722e-100. No new native BRC execution, anchor inverse or moment generation.

L0 | Q | full box | outer pairs | all feasible integer tuples before gcd | primitive
10^104 | 10^68 | 5535 | 135 | 3 | 2
10^114 | 10^68 | 5535 | 135 | 0 | 0
10^114 | 3*10^68 | 167875 | 1343 | 2 | 0
10^114 | 10^69 | 6367124 | 15196 | 29 | 16
10^140 | 10^69 | 6367124 | 15196 | 29 | 16

Independent exhaustive full-box verification of first four rows exactly matched all primitive tuples and counts before gcd. At Q=10^69 the box is [-39,18] x [-111,150] x [1,419]. Sliced enumeration visits 15196 outer pairs rather than 6367124 full tuples; ratio 419 in candidate loop sizes (not a measured wall-clock speedup). All 16 surviving primitive relations lie in the exact targeted base P (zero scale payment), and also in the archived full 13072-direction section of PREFIX-1138. Thus the 16 lines persist for arbitrary L in both declared outer models. Further scale contraction or enumerating the same full facet set cannot exclude them. This is not proof of common-coefficient inner feasibility or true anomalies.

Their ordered n coordinates (recover q,p,h by W):
[[-12,41,134],[6,-41,203],[-3,-3,208],[5,-40,246],[-24,88,189],[-14,43,220],[-4,-2,251],[-25,89,232],[-15,44,263],[-5,-1,294],[-17,52,270],[3,-38,332],[-26,90,275],[-6,0,337],[4,-45,368],[-18,53,313]].
Minimum q = 454053010447038821571844458623342062019806862787921210670980974998864.
Therefore for every L>=10^114 the inherited necessary pair gap satisfies b-a>=q>=that minimum (~4.540530104470388e68). All q<=3e68 strictly excluded.

For the two small-scale survivors at L=10^104,Q=10^68, exact last integer L (first excluded is L+1):
n=[1,-6,23], q=54945820412798735798601167458271601137251709968918317791951377874212:
188419788319406942834004797409641730205717129267942548833863449412177735497081020954897591483589360771920.
n=[-1,2,30], q=88993291512409815343918122685079213911341092656943480027028927720873:
255304843249984920490793599856290545078518005042981576564985498333278828042979454544148055492771718255346.
Both neighboring tests independently checked. In the targeted region model all q<=10^68 are therefore excluded for every integer L>=255304843249984920490793599856290545078518005042981576564985498333278828042979454544148055492771718255347 (~2.55305e104), considerably earlier than 10^114. Cutoffs are for the targeted outer necessary region; full section may exclude earlier.

## 4. Application to inherited dyadic windows

Use inherited q^2<4EL/d for three anomalies and q<=sqrt(L) for close pairs, retaining earlier covered windows. With q bound above and L>=10^114, first non-excluded dyadic starts on 10^8*2^j are
L3=2115379100128795516646128985704867327450894985485699901710876144878098531956196306640605473407088911512291878480074746573619200000000 (~2.1153791001287955e132, 32 times 1138)
L2=277266969412081485957841418414308370343643707537581657517047958061462130780562562303997440610413957809739121096140357182897415782400000000 (~2.772669694120815e137, 16 times 1138).
These are conservative starts, not sharpness. Continuous integer endpoint stays 4.72478e43; endpoint candidate, fixed-spectrum unbounded separation and B_fix,odd(32) open.

## 5. Reproduction and evidence

Input archive PREFIX-1138-execution-evidence.zip with its original manifest; use point_section_targeted1138.py, check_extra_core.py, verify_section.py, extend_targeted1138.json and point_section1138.json; see pinned paper for compact inputs and replay. All prior bytes kept. New exact output and two independent arithmetic programs in PREFIX-1139-execution-evidence.zip. Executed SHA256:
extend1139.py f4c3260cb090dfdfb7dd67c48dec7c896f7472c485d4a670d8ac0830beb8dd60
verify1139.py 568677aa3faa5581dd230d3541d578fd73d778177ff9123bb020978c2d08ac25
extend1139.json 8f917a791d53a8afd5a13a8589694e6cad3641409ad43b3df3347d98649644d8
extend1139.log b6edb31a9abdea3adcc927bee944832ff0928ac6c18d47f2db42cdca7dd0b4e6
verify1139.log 1f2557634fac9dd446254ba5c83a5752f9a380dd11fd03bc5e2684121fd0543d

Compact replay from prior 1138 paper: reconstruct P relative to (r0,u) with the 43-direction loop, add (r0,u) to its vertices; take V in prior cert and exact W as there. Form edge normals plus axes as in section 1, determine integer box via section 2, and loop over it using W. Test q0<=q<=Q, gcd(p,q)=1, all support inequalities. For the small two lines test the displayed adjacent L integers; for the 16 lines test unexpanded P. This reconstructs every reported primitive line.

## Next

Test 16 persistent lines (first minimum) against the full common-coefficient fiber with actual d using the prior Brouwer feasibility route or new coupled-moment residual direction. Their exact base membership rules out mere scale contraction as a way to exclude them within the current outer model. Keep true fixed parameters open. No formal Task/Result closure.
