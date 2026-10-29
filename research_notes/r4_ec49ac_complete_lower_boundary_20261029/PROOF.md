# EC49AC — Complete exact lower boundary of causal positive-BRC observation region

Date: 2026-10-29. Status: AUTHOR_PROVED / EXACT_FRACTION_CHECK_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED. Predecessor: EC49AB Draft PR #1684, commit 5750222242eab5d017f9f512f8f7e25d3daf81b9. This is an auxiliary positive-probability source-labelled BRC model, not native signed-BRC/X6 dynamics.

## Theorem (every real fresh-coin behavioral strategy)

Three histories w=0,1,2 have prior 1/3. At history w choose STOP or sensor A0,A1 (first cost 1), B0,B1 (first cost 2), with x_wc>=0 and sum_c x_wc<=1. The two-valued signal has t_w(u)=1/2+(2u-1)(1-w)/200. Source P(w,u,z)=t_w(u)*(1/6 if w=z else 1/12) and Q(w,u,z)=t_w(u)/9 for z=0,1,2. Both have 18 strictly positive normalized leaves with identical (w,u) marginals. History w is erased before optional S purchase with conditional probability s_cu; terminal acceptance probabilities are a_cuz after S and a0_cu without S. All action/acceptance coins are fresh and no retained common seed exists. Fix C1=43/48 and C2=7/8 in BOTH sources. Let alpha=P(accept), beta=Q(accept), delta=alpha-beta.

The universal maximum delta is 59/576. The exact minimum alpha at every real delta in [0,59/576] is the continuous piecewise-affine interpolation of six rational knots:

| index | delta | alpha_min |
|---|---:|---:|
| 0 | 0 | 0 |
| 1 | 17/288 | 17/96 |
| 2 | 3047/38400 | 3641/12800 |
| 3 | 19/192 | 25/64 |
| 4 | 1939/19200 | 3067/6400 |
| 5 | 59/576 | 109/192 |

Successive exact slopes are 3, 12369/2341, 1359/251, 567/13, 5097/83. All are strictly increasing. The first new kink beyond EC49AB occurs precisely at delta=3047/38400, with right slope 1359/251 instead of left slope 12369/2341 (jump 76800/587591). All points are realized by genuine fresh-coin causal strategies, with rational probabilities for rational delta. This characterizes the entire LOWER boundary; full vertical filling of the two-dimensional (alpha,beta) feasible set remains open.

Furthermore define m=sum_(w,c,u) x_wc*t_w(u)*(1-s_cu), the unnormalized first-purchase mass skipping S. For EVERY real legal strategy and EACH of four slopes lambda, the following universal inequality holds:

alpha >= lambda*delta - E1(lambda) + gamma(lambda)*m,

with exact triples (lambda,E1,gamma):
(12369/2341, 5049/37456, 297/2341);
(1359/251, 583/4016, 133/753);
(567/13, 1633/416, 29/39);
(5097/83, 15199/2656, 1/3).

Every gamma is strictly positive. All lower-boundary optimizers for delta in [17/288,59/576] therefore buy S after each first-stage paid observation of positive probability (m=0). Optional early abandonment cannot improve that sharp graph.

## Universal supporting inequalities and full 288-endpoint reduction

Write T=sum_wc x_wc and b=sum_(w,c in B) x_wc. Source-identical first-stage marginals imply C1=(T+b)/3 and C2=(T-m)/3, hence T+b=43/16, T-m=21/8, b+m=1/16, and 0<=b<=1/16. Put h_w=1-sum_c x_wc and b_w=sum_(c in B) x_wc. Then sum h_w=5/16+b and sum b_w=b. Since sum(h_w+b_w)=5/16+2b<=7/16, every needed row capacity h_w+b_w<=1 is automatic.

At fixed b decompose the h and b_w simplex weights into their three single-history vertices; independently decompose the conditional A0/A1 and B0/B1 choices into pure labels. Every feasible prefix is consequently in the convex hull of 3 STOP histories times 3 B histories times 2^3 A-label assignments times 2 B labels = 144 prefixes. Each prefix is affine in b, itself interpolating the endpoint b=0 and b=1/16. Every real feasible prefix is therefore in the convex hull of 288 explicit rational endpoints. This representation is an ANALYTICAL BOUND ONLY: it never grants a retained random seed to the actual observer.

For sensed atom (c,u,z), set v=x_zc*t_z(u), r=sum_(w!=z) x_wc*t_w(u), and p=P(c,u,z), q=Q(c,u,z), d=p-q. Directly,
p=(2v+r)/12, q=(v+r)/9, d=(2v-r)/36, 3q-2p=r/6>=0.
Hence p>=3d. All STOP/skip-S acceptance uses equal P and Q marginal, contributing nonnegative alpha and zero delta. For sensed outcomes the legal combined acceptance is y_cuz=s_cu*a_cuz in [0,1]. Consequently for any real slope lambda,

lambda*delta-alpha <= sum_(c,u,z) y_cuz*(lambda*d-p)
                    <= E_lambda(x):=sum_(c,u,z) max(0,lambda*d-p).

E_lambda is convex in prefix x. The actually EXECUTED Fraction verifier checks its exact endpoint maxima in the following complete 144+144 table for each slope:

| lambda | E0 maximum at b=0 | E1 maximum at b=1/16 | equality vertices E0,E1 |
|---|---:|---:|---:|
| 12369/2341 | 297/2341 | 5049/37456 | 72,48 |
| 1359/251 | 101/753 | 583/4016 | 72,24 |
| 567/13 | 4841/1248 | 1633/416 | 72,24 |
| 5097/83 | 45431/7968 | 15199/2656 | 72,48 |

For fixed b, E_lambda(x)<=(1-16b)*E0+16b*E1 = E1-16m(E1-E0). This yields all four gamma=16(E1-E0) coefficients and universal supporting inequalities, for ALL real policies. For the first segment p>=3d implies alpha>=3delta with no enumeration. At every knot the corresponding neighboring supporting lines agree with alpha_min. The universal discrimination bound follows separately from delta<=sum max(0,d) and its convexity in x: the same 288 endpoints each obey max sum max(0,d)=59/576 (both 144-element groups attain this maximum). Thus no legal strategy exists with larger delta.

## Exact causal witness attains all five segments

Fix one prefix for every segment: w0 buys A0 surely; w1 buys A1 surely; w2 buys A0 with 9/16, B0 with 1/16, STOP with 3/8. For every paid c,u, buy S surely, so m=0. Direct sums give C1=43/48, C2=7/8.

The four source-pure acceptance atoms (A1,0,1), (A1,1,1), (B0,0,2), (B0,1,2) have aggregate alpha=17/96 and delta=17/288. For delta up to 17/288 give each of these four atoms an independent fresh acceptance probability delta/(17/288).

For later segments accept all four pure atoms surely and add four single atoms IN ORDER, accepting earlier atoms completely and the current atom with fresh probability (delta-delta_start)/(delta_end-delta_start):

| added observation atom (c,u,z) | P | Q | P-Q | P/(P-Q) |
|---|---:|---:|---:|---:|
| (A0,1,0) | 4123/38400 | 2507/28800 | 2341/115200 | 12369/2341 |
| (A0,0,0) | 1359/12800 | 277/3200 | 251/12800 | 1359/251 |
| (A0,0,2) | 567/6400 | 277/3200 | 13/6400 | 567/13 |
| (A0,1,2) | 1699/19200 | 2507/28800 | 83/57600 | 5097/83 |

These increments produce precisely the six knots, and every intermediate real point with no persistent strategy coin. For example, delta=1/12 yields (alpha,beta)=(1229/4016,2683/12048), and at the maximum delta=59/576 it yields (alpha,beta)=(109/192,67/144).

Each claimed segment therefore has both a universal dual bound and a valid causal primal witness, proving the exact entire lower graph. The proof is by analytic convex-endpoint reduction plus exhaustive exact finite certificate, not real-grid sampling or numerical approximation.

## Verification, type scope and next question

VERIFY.py is the executed self-contained standard-library Fraction checker. It checks 18 strictly positive normalized leaves per source, all four slopes against 144 endpoints at each budget endpoint (1,152 exact envelope checks), strict gamma coefficients, 288-endpoint discrimination cap, all knot/support incidences, witness observation mass ratios, many interior rational witness points and both stage costs. EXACT_REPORT.json records its true output. No independent peer review, Lean proof or canonical mathematical admission is inferred from execution. The model is positive P/Q-mass BRC; no native signed/phase BRC, six-dimensional X6 embedding or Heartbeat World operator-preservation theorem is asserted. P000 and ACTIVE worldview are unchanged.

EC49AD next asks whether the vertical set above this lower graph and below known upper alpha=1-3delta is completely filled by fresh-coin strategies, or exhibits an exact nonconvex gap. First discriminating case: delta=1/12 and alpha between 1229/4016 and 3/4. Keep all causal products, finite budgets and history-erasure constraints.
