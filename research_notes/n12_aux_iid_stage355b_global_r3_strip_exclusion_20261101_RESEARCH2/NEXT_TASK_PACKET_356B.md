# Stage356-B — off-arc `r0=0` / other chamber competition (portable author handoff)

## Frozen scientific frontier and status

Parent: Enterprise Math N12 double-source 16-label Bernoulli/BRC auxiliary model; previous right-arc Stage353–354 at Enterprise Math PR #1736 HEAD `ad7f7816ca0939c610256f2ad60bfe3b62fec9eb` when this research started. Current author proof Stage355-B excludes the **entire closed tube** `|r3|<=1/2000` from all full two-source global minimizers for every real `0<=E<=11/5000`, without assuming Stage346's sharp global b floor or Stage336/342 Pareto dominance. It proves the auxiliary global absolute TV floor `b>=3779/10^6` with 67 exact Bernstein leaves, and a 73-leaf strict pointwise dominance certificate by `Q=(29/125,349/625)` on the tube under the feasible per-source budget `b<0.00598`. An independent 37-leaf certificate covers `r3=0` itself. Full source/port labels retained. This is author-verified, `UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING`; the native owner query returned `CONTROL_QUOTA` and `research_authority_granted=false`.

GK snapshot `main@c1d957ec4b54c76df0d5ddcecf4b8f6f6f319f1e`; EM baseline `main@f3e38a72335239e95d2b020d782b7e67b98c006e` and original P000 V5. Refresh current authority before role-bound operations; source pins for the mathematics must remain exact. No attempt should reproduce or re-route the Stage352 platform-denied content.

## Exact question

Within the full source-labeled model and `0<=E<=11/5000`, can an unrestricted two-source minimizer have a source on **`r0=0`** or in an additional non-right-arc residual-sign stratum **outside** the already excluded `|r3|<=1/2000` tube? Distinguish exact elimination by a fixed rational point from elimination by a budget-dependent arc point. If direct domination fails, exhibit a strict feasible rational competitor or an exact lower/upper bound that isolates the remaining Pareto region.

Retain definitions `w=(1,3,3,1), m=(61,21,9,9), B_k(z)=z^k(1-z)^(3-k), r_k=(4B_k(x)+B_k(y))/5-m_k/160, b=(5/32)sum w|r|, D3(a,z)=(1/2)sum w|B_k(a)-B_k(z)|, c=(63D3(1/4,x)+D3(3/4,x)+9D3(1/4,y)+7D3(3/4,y))/256`. `q*` is the selected `r0=r1=0` root; `beta*=b(q*)` and two-source `T=33/1024+c(q1)+c(q2)` with budget `b(q1)+b(q2)<=2beta*+E`.

## Reusable proof interface

The exact executable `REPRO_STAGE355B.py` implements the full 16-subset TV dual, degree-3 Bernstein coefficients, sourcewise four-term `D3` dual, rational root bracket, exact pairwise-disjoint closed-cover checks, and root-box beta bound. Import the functions or derive an independent validation; do not lose labels or convert an empirical mesh to a theorem. It is **not** a native P000 BRC–Shor calculator; this is a self-contained external Bernoulli auxiliary observer.

## Success / falsification

Deliver a theorem for every real point on a specified global stratum, plus an exact reproducible certificate and all boundary cases, or a strict rational counterexample for a clearly declared budget. State dependence on any prior non-admitted theorem. Publish all non-sensitive substantive artifacts to the same PR with current-head CAS and verify remote content. A native Session/CLAIM/Result/Review is not inferred from Git storage; formal progression still requires genuine authority. Native X6/three-dimensional slice/time/triadic closure/Cell-address observer transfer remains separate.
