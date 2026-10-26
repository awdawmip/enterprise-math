# Stage162 — exact full-real optimum, ternary iid N14 (R1 author-side)

**Evidence class:** AUTHOR EXACT-RATIONAL COMPUTATION-ASSISTED PROOF. Not independently reviewed, not an authenticated Enterprise Math CLAIM/Result, not a native P000/X6 theorem.

**Frozen inputs:** GLOBAL_KNOWLEDGE_V1 `main@11c141acc178d3b6cd5f478ee97751535d61108e` (same-snapshot bootstrap/manual, project router, P000, ACTIVE worldview, BRC/mathematics policy). Enterprise Math Source `main@d6d0d2c623691df7c323f6609339bcf5dc8d3cbe` (P000, X6/world constraints, portable research protocol and Stage161 author proof). Upstream first candidate: `research_notes/n14_aux_iid_affine_161_20261026/candidate162.json` at this EM input pin. GitHub connector identity `awdawmip`. Native task/owner listing: `CONTROL_QUOTA`; native session start `STATIC_READONLY_SCOPE_DENIED, operation_sent=false`. A separate R2 author activity concerning Stage162 was visible; neither R2 nor this writer had an authenticated active CLAIM. This document deliberately uses a distinct author-only path and asserts no independent review.

## Exact problem and claim

Observe at most 14 ordered iid symbols with
[
P=(1/8,1/24,5/6),qquad Q=(1/12,1/12,5/6).
]
Behavioral stopping tests may depend on full ordered history and randomized stopping/decision coins. Let `eP=P(decide Q)`, `eQ=Q(decide P)`, `tP=E_P tau`, `tQ=E_Q tau`, and `V14(alpha)=min max(tP,tQ)` subject to `eP,eQ <= alpha`.

Take the previously author-proved (not Driver-accepted) left endpoint
[
\alpha_{161}=\frac{440625016346358918245}{1265046575011281764352},
\qquad V_{161}=\frac{2138967403739208846181}{180720939287325966336}.
]

**Theorem within this exact finite external model.** For **every real**
[
0\leq\delta\leq\eta_{162}:=\frac{29431075655}{2510013045657305088},
]
the exact optimum is
[
\boxed{V_{14}(\alpha_{161}+\delta)
=V_{161}-\frac{10482543508472}{17658645393}\delta.}
]
The right endpoint is
[
\boxed{\alpha_{162}=\frac{440625031179621048365}{1265046575011281764352}},
\qquad
\boxed{V_{162}=\frac{2138966145833987829541}{180720939287325966336}.}
]
This support is **sharp on the right**: it is strictly lower than the true optimum at every `alpha > alpha162`. This conclusion is computation-assisted (author checker below), not a purely unverified numerical fit.

## Universal exact dual

For the count state `s=(n,a,b)`, `n<=14`, the likelihood `Q/P` of any ordered prefix is
[
\ell(s)=2^{a+b}/3^a.
]
With
[
K_{162}=\frac{1776538556208}{5886215131},
\qquad L_{162}=\frac{5152927839848}{17658645393},
]
the Bellman recurrence under `P` is
[
H(s)=\min\{K\ell(s),\,L,\,1+\sum_{i=0}^2P_iH(s+e_i)\},
]
where continuation is available only if `n<14`, and `e_i` increases the observation depth and corresponding letter count. All 680 finite states are enumerated exactly with rational arithmetic. There are precisely two nontrivial action ties:
[
R=(10,0,1):Q/C;\qquad X=(7,3,3):Q/C.
]
All 1,238 other nonminimal action gaps are strictly positive; smallest:
[
\frac{1055356088281}{183084835434624}.
]
The root value is
[
H(0,0,0)=\frac{211461038972875305263848856447}{967349797503719726804631552}.
]
By conditional Bellman induction on each complete ordered history and exact change of measure,
[
H(0)\leq t_P+K e_Q+L e_P
\leq\max(t_P,t_Q)+(K+L)\alpha,
]
with
[
K+L=\frac{10482543508472}{17658645393}.
]
Thus the support `H(0)-(K+L) alpha` is a universal lower bound even for all full-history randomized policies.

## BRC ordered provenance, independent recursion/DFS observations

The carrier consists of distinct ordered prefixes with positive rational `P/Q` masses, first-hit labels, and the two decision-dependent future laws. The observer is exactly `(eP,eQ,tP,tQ)`; only under the declared iid suffix operations do equal-count histories admit a four-observer quotient. Nothing implies a native P000/X6 quotient or signed cancellation.

The strict Bellman actions are fixed except at the two ties. The true *first-reach* ordered histories, counted by literal, unmerged integer-weight prefix DFS, are:

| tie | histories | P mass | Q mass |
|---|---:|---:|---:|
| R=(10,0,1) | 10 | 9765625/120932352 | 9765625/60466176 |
| X=(7,3,3) | 56 | 35/5308416 | 35/2239488 |

No X-history can lead to R because the count `a` cannot decrease from 3 to 0. No R-history can reach X because its depth is 10 rather than 7. Their first-hit cones are disjoint. Therefore the four-observer map is exactly affine in the two stopping coins: `r=P(immediately Q at R)`, `x=P(immediately Q at X)`.

Writing `M=(eP,eQ,tP,tQ)`, separate count-suffix Fraction recurrence and literal ordered integer DFS agree at all four deterministic corners:
[
M(r,x)=M_{00}+r\,d_R+x\,d_X,
]
where
[
\begin{aligned}
M_{00}&=(608980370270800655/1752976676930715648,\
 &\quad7002931380335/20061226008576,\
 &\quad2600664590463380201/219122084616339456,\
 &\quad153523688266399/13374150672384);\\
d_R&=(4521484375/1486016741376,\
 &\quad-3232421875/1253826625536,\
 &\quad-61181640625/557256278016,\
 &\quad-20751953125/104485552128);\\
d_X&=(34732355/300578991243264,\
 &\quad-6118315/80244904034304,\
 &\quad-1206850085/112717121716224,\
 &\quad-143514245/6687075336192).
\end{aligned}
]
The exact mixed difference `M11 - M10 - M01 + M00` equals `(0,0,0,0)`.
The four integer DFS traversals visited respectively 483664, 473080, 483424, 472840 nodes for coin assignments `(r,x)=(0,0),(0,1),(1,0),(1,1)`. Both P and Q terminal masses are exactly 1 in every run.

## Feasible balanced interval and sharp endpoint

Solving `eP=eQ` exactly yields the compensation law
[
\boxed{r(x)=\frac{353413318165451}{1182361600000000}
       -\frac{3602311339}{105568000000000}\,x,\quad 0\leq x\leq1.}
]
Every coin is legal throughout this real interval. Common error strictly increases from
`alpha161` at `x=0` to `alpha162` at `x=1`.
The corresponding `tP-tQ` is strictly positive at both endpoints:
[
\frac{526231060559760430495}{1265046575011281764352},
\qquad
\frac{526240831439401052735}{1265046575011281764352}.
]
At both endpoints, exact rational checking gives
`tP + K eQ + L eP = H(0)`; by affinity both equalities hold for every intermediate real coin, and `max(tP,tQ)=tP`. Thus the lower bound is attained at every real alpha in the theorem's interval.

For strict right sharpness, the entire finite-history randomized policy space is a finite product of compact action simplices; an optimum exists. Equality with this same support would force both error constraints to saturate (since `K,L>0`), `max(tP,tQ)=tP`, and strictly Bellman-optimal choices at every reached positive-mass prefix. The 1,238 exact strict gaps leave only R/X as possible nontrivial randomization. Suffix-law identity and same-state likelihood ratio permit averaging any full-history tie coins into `r,x` without changing the four observables. Disjoint first-hit cones give the affine law above. Equal-error saturation forces `r=r(x)`, and `x<=1` gives common error `<=alpha162`, a contradiction for any greater alpha. Therefore the same support is strictly unattainable to the right.

## Verification boundary and continuation

Executed locally with exact `fractions.Fraction`: a 680-state Bellman census, all four count-suffix corners, **separate literal integer-weight ordered-prefix DFS**, first-hit P/Q rational masses, mixed-zero equality, dual equalities, legal balanced coins, exact endpoint inheritance and strict right-support contradiction. The observed run printed `PASS Stage162 author exact interval + sharpness`; see `certificate162.json`, `VERIFY_STAGE162.py` and attached local full execution evidence. This is an author mathematical proof backed by finite exhaustive exact check, NOT independent Driver acceptance.

A further **dual-only** author scan along `dK=-1,dL=-10592/12501`, keeping R Q/C tied while X becomes strict Q, yields Stage163 candidate:
[
K_{163}=\frac{163900037061}{554150611},
\quad L_{163}=\frac{476600779976}{1662451833},
]
with new `Y=(8,4,1)` P/C tie and old R Q/C tie; 1,238 positive gaps, minimum `1577397669610597/79424873185738752`. **Stage163 primal attainment and right sharpness are open**. Recompute its first-hit masses, compensation and exact feasibility before promoting any claim. Neither Stage162 nor Stage163 is a theorem about native X6 Cell dynamics absent an explicit lossless observer/operation bridge.
