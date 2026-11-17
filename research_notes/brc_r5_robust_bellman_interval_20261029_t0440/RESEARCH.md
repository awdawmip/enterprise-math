# R5 — exact robust signed Bellman-gap interval for a source-sensitive diamond

Date: 2026-10-29 Asia/Shanghai. Status: **AUTHOR_PROVED / EXACT_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED**. Portable finite two-law model result; no authenticated native CLAIM, Result, independent Driver review or native X6 embedding.

## Frozen provenance and question

GLOBAL_KNOWLEDGE_V1 canonical read: main@c88ec5d4011b5af2318582b2c9da17de93ae1e59. Original P000 Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc matched its startup projection. Read ACTIVE worldview, TASK router, code/math/BRC/activity policies, and project joint-observer and X6 contracts. Enterprise Math source: main@943658634314612424dd7b004ed59eff4afe0bbc. Predecessor: research_notes/brc_r5_sensitive_tail_bellman_20261029_t0337/RESEARCH.md at this SHA.

The predecessor found a single signed cost direction exhibiting a strict convex-hull gap. The present independent unit computes the **entire robust parameter interval** for the fixed origin-sensitive two-route diamond, including the optimal gap and an all-real distance bound.

## Exact model and observer

Terminal likelihood ratios S=(1/2,1,3/2,5/2), origin parent likelihood ratio r=3/2; origins A,B each have initial Q mass 1/4. A forced terminal Q mass 1/2 has signature 1/2. The conditional Q kernels (ordered by S) are:

| Kernel | s=1/2 | s=1 | s=3/2 | s=5/2 |
|---|---|---|---|---|
| mu_A | 7/50 | 11/75 | 1/2 | 16/75 |
| mu_B | 17/200 | 23/150 | 3/5 | 97/600 |
| nu_A,L | 1/2 | 1/6 | 1/4 | 1/12 |
| nu_B,L | 5/12 | 1/3 | 1/6 | 1/12 |
| nu_A,R | 17/100 | 23/75 | 1/5 | 97/300 |
| nu_B,R | 31/120 | 5/18 | 1/15 | 143/360 |
| eta_A | 1/8 | 1/4 | 3/8 | 1/4 |
| eta_B | 5/32 | 3/16 | 13/32 | 1/4 |

The P transition on a Q kernel from parent LR r0 to child LR s is s/r0 times the Q probability. All rows strictly positive, normalized under both laws. At time 1 origins may stop or continue. At time 2 only states L=1 and R=3/2 may continue. At time 3 both paths merge at r=3/2, where they may continue via source-sensitive eta to time 4. Complete-history policies know origin and path; seedless LR policies use only (time,LR) and fresh independent action/declaration coins, with no persistent correlated seed. Their observer is O=(e_P,e_Q,T_P,T_Q), P/Q erroneous declaration probabilities and P/Q expected stopping times, all behavioral probabilities in **all real [0,1]**.

Preserve the BRC positive source/path Q masses: v=(11/1200,23/3600) from left and w=(1/40,1/100) from right, giving merged origin masses x_A=41/1200, x_B=59/3600. The current likelihood ratio does not determine this source composition.

## New theorem (all real behavioral policies)

For every real theta in [1/8,5/32] and signed linear objective L_theta=2e_P+2e_Q+theta*T_Q:

V_full(theta) = 155161/115200 + (6719/3600)*theta.

V_LR(theta) = min{2429/1800 + (37/20)*theta, 154669/115200 + (3421/1800)*theta}.

Hence the gap is exactly

Delta(theta) = V_LR - V_full
= min{(41/1200)*(theta-1/8), (59/3600)*(5/32-theta)}.

It is strictly positive at every interior theta. The unique maximal gap in this entire interval is **2419/6988800**, attained at **theta*=787/5824**.

A full-history minimizer in the interior continues at the root and both time-2 states, stops origin A and continues origin B at time-3 merged r, declaring P iff final signature s>1. Its fixed observer is

O*=(98731/230400, 627/2560, 5429/2400, 6719/3600).

For the optimized direction (2,2,0,787/5824), every real seedless LR observation satisfies

||O-O*||_infty >= **2419/28899600**.

This **excludes** the fixed experiment from the mother target requiring equal convex hulls but unequal actual observer sets; it is not a positive mother counterexample.

## Exact proof

At any terminal (t,s) the two errors contribute 2+sum Q_mass*declareP*(2-2s), so after extracting the total constant 2 the optimal local terminal signed cost is

f_t(s) = t*theta + min(0,2-2s).

The optimal declaration is P for s>1 and Q for s<1 (arbitrary at s=1). At merged r, the difference 'continue minus stop' for origin i is

D_i(theta)=E_eta_i f_4-f_3(r) = theta-I_i,

where I_i = min(0,2-2r)-E_eta_i min(0,2-2s). Direct rational substitution yields I_A=1/8, I_B=5/32. Full history therefore stops A and continues B for every strict interior theta.

It remains to prove that no upstream stopping alternative can improve either full or LR optimum. Temporarily fix **any real** merged continuation coin gamma∈[0,1]. At each origin i the merged value is m_i=f_3(r)+gamma*(theta-I_i). The sourcewise time-2 continuation value for route d=L,R is the nu_i,d expectation of f_3 at off-r endpoints and m_i at r. Set the sourcewise stop-minus-continue margin at route d to f_2(s_d) minus that expectation. Set the root margin to f_1(r) minus the mu_i expectation of the two continuing route values plus f_2 at the remaining time-2 endpoints.

Each margin is affine in theta for fixed gamma and affine in gamma for fixed theta. A separately affine (bilinear) function on [1/8,5/32]×[0,1] attains its minimum at one of four corners. Exact corner substitution gives **universal real-domain strict minima**:

| Source | left margin | right margin | root margin |
|---|---:|---:|---:|
| A | 43/128 | 3/400 | 353/9600 |
| B | 25/96 | 49/480 | 431/14400 |

Thus all three upstream actions continue for every theta in the interval and for all possible subsequent gamma, under either policy class. The sourcewise positivity also enforces the same decision for LR-shared upstream actions. Under complete history, independently choosing gamma_A and gamma_B gives merged contribution x_B*(theta-5/32). Under seedless LR the **single** gamma gives min(0,x_A*(theta-1/8)+x_B*(theta-5/32)). Their difference is the displayed triangular Delta(theta).

The switch between LR gamma=1 and gamma=0 occurs at

theta*=(x_A/8+5*x_B/32)/(x_A+x_B)=787/5824.

The two affine pieces' slopes are x_A>0 and -x_B<0, so the switch uniquely maximizes Delta with exact value 2419/6988800. Summing all terminal masses yields the stated V_full and V_LR affine formulas and O*. Finally the support inequality for all real LR policies gives (2,2,0,theta*)·(O-O*) >= Delta_max; Holder with L1 norm 4+theta* proves the L-infinity bound. QED.

## Actual verification and precise scope

VERIFY.py is standalone Python Fraction exact-rational code; EXACT_OUTPUT.txt is **the actual stdout**. It checks eight strictly positive kernel rows and their first moments; 4-corner minimum margins (the universal analytical certificate); 251 rational theta test points, each with all 16 deterministic LR upstream/merge action assignments; full Bellman values and exact optimized witness arithmetic. The 251 finite test points are regression, not the reason the theorem holds for **all real theta**: that follows from the separately affine corner proof and sourcewise Bellman optimization.

BRC reuse: positive source/path mass, origin-specific future laws and P/Q likelihood-ratio readout, with origin residuals retained until observer-relevant tail operations. The finite model has no asserted native X6 state embedding, physical calibration or general all-signed support-equality theorem.

Native control observation 2026-10-29: em_status showed research_authority_granted=false and control active-job quota 5/5; bounded native owner listing returned CONTROL_QUOTA. The current Source owner and task claim were therefore not authenticated; author-side GitHub artifact is **UNREVIEWED / NOT_ADMITTED**. No security-denied action is retried through a different channel.

## Next proof obligation

For symbolic origin-sensitive two-route mergers, obtain a finite **all-signed** support-equality test, rather than sampling directions. Multi-affinity implies that convex hulls of both policy images equal convex hulls of their finite deterministic-policy observation vectors. Hence for rational kernels, every full-history deterministic observer must belong to the exact rational convex hull of seedless LR deterministic observers; use rational linear feasibility / Farkas separation, maintaining distinct full-history and seedless policy classes. If a new kernel passes that test, investigate actual observer-image nonconvexity by an exact semialgebraic real-membership certificate, not by source-flow nonconvexity alone.
