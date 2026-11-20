# OAI7-155-E: joint-legality bridge for an X6 three-axis slice

Date: 2026-11-21 (Asia/Shanghai). Mode: TASK exploration / conditional theorem / exact finite counterexample. Scientific status: NOT_REVIEWED. Publication and native acceptance are separate.

## Source and scope
Task: RS-OAI7-155-E-20261007-6F2A81, publication TP2-3198E64C2F8284D6A8DC.
Frozen external draft: openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a, preprints/A-translational-tile-with-no-fully-periodic-tiling-in-dimension-three-September-23-2026/build/sections/05-common-solution.tex and 07-three-dimensions.tex. The draft is external research, not canonically admitted as an Enterprise Math theorem.
P000: the native world has six spatial signed axes plus time; a research slice is 3D within X6, not an independent plane; the omitted third coordinate must not silently equal zero; off-axis apparent segments are composite native paths; legal primitive stable balance remains triadic. Preserve actual typed BRC events and residual/provenance.

## Explicit typed interface
Let C6 denote a six-axis integer displacement *chart* relative to a chosen Cell, not yet an independently certified event algebra. Choose three distinct named native axes j1,j2,j3, and a declared base chart address b. The proposed chart injection is
  iota: Z^3 -> C6, iota(u1,u2,u3)=b+u1 e_j1+u2 e_j2+u3 e_j3.
Its remaining coordinates are deliberately fixed by the chosen b. The third slice coordinate u3 is free, NOT an omitted zero. The chart identity iota(u+e_k)=iota(u)+e_jk does not alone establish that a corresponding physical/native update is a legal typed BRC event, nor that a Euclidean line is primitive.

Let N be the as-yet-unconstructed set of lawful *joint* native states with declared provenance, ports, and admissible transitions. Specify a single joint readout
  rho: N x iota(Z^3) -> {0,1}
with translation compatibility when required. Put a_n(u)=rho(n,iota(u)). For one external finite tile T subset Z^3, define
  E_T={a in {0,1}^{Z^3}: for every v in Z^3,
       sum_{t in T} a(v-t)=1}.
Here a is ONE translation-center set for ALL local covering equations. The proposed bridge relation is
  R_T={(n,a): n in N, a=a_n as a complete joint assignment, a in E_T,
       and the declared native readout/source/operation obligations hold}.
This is a typed *condition* for a native realization, NOT a construction of N, a native tiling, or a native aperiodic world. Separate local native witnesses n_v do not imply one n satisfying all v.

## Conditional period-reflection lemma
Assume the six-axis chart has a Z^6 translation action on the relevant lawful joint states, rho is equivariant for the three declared axis translations, and n in N has a finite-index subgroup L of Z^6 as a symmetry group of the *full joint native state*. Then a_n has a finite-index period subgroup in Z^3.

Proof. Let M=|Z^6/L|. In the finite quotient, M e_jk belongs to L for k=1,2,3. By chart embedding and equivariant readout,
  a_n(u+M e_k)=rho(n,iota(u)+M e_jk)=rho(n,iota(u))=a_n(u).
Thus M Z^3 is a full-rank period subgroup. QED.

Corollary (conditional only): if T has no fully-periodic solution a in E_T, and a lawful native joint witness n exists with a_n in E_T and all above equivariance conditions, then n cannot be fully periodic in the six-axis chart sense. The cited external manuscript proposes the no-fully-periodic property for its specific T; its mathematical admission into Enterprise Math and the native witness/typed event construction are independent open obligations. This does not claim an absence of every individual period or nonperiodic temporal dynamics.

## Sharp finite joint-compatibility obstruction
For three external *sites* u,v,w (full 3-coordinate tuples, e.g. u=(0,0,0), v=(1,0,0), w=(0,0,1)), let x_u,x_v,x_w be binary readout variables. Consider R1: x_u=x_v, R2: x_v=x_w, R3: x_w!=x_u.
Each relation holds for 4 of the 8 joint assignments. Every pair of relations holds for exactly 2 assignments, and all individual-site projections are {0,1}. Yet the triple intersection is empty: the first two require x_u=x_v=x_w, contradicting the third. All 8 assignments were checked exactly by check_oai155e_joint_legality.py.
Consequently neither individually satisfiable local equations nor nonempty pairwise joins/single-site marginals suffice for a global shared-state bridge. This is a counterexample to a *candidate inference rule*, NOT a counterexample to the external paper's actual jointly solved tiling system.

## Needed next native witness/certificate
1. Identify a current *actual* typed BRC event/state carrier N and provenance fields for this declared 3D slice; distinguish raw chart addresses from legal events.
2. Supply one global n and rho, or a precise obstruction, for the particular external tile T. For any proposed compression, check future-relevant joint-source fibers rather than only per-channel marginals.
3. Prove or refute the translation-equivariance/period-reflection premises under the real native event algebra. Preserve the external manuscript's exact quantifiers and non-admission status.

The verified result here is the conditional group-theoretic period lemma plus the finite joint-compatibility no-go. The complete native transfer remains OPEN.