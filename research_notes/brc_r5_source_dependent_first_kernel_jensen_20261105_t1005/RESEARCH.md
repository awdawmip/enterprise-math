# R5 — Source-dependent first-kernel Jensen separation with strictly positive second experiments

Date: 2026-11-05 Asia/Shanghai. Evidence class: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

**Mother question.** Find a finite strictly positive P/Q lawful BRC stopping model whose full four-observer convex hull is identical under history-sensitive FULL and seedless likelihood-ratio (LR) policies while their actual real-behavior observation images differ. Here `O4=(eP,eQ,TP,TQ)` with error coordinates `eP=P(declare Q)`, `eQ=Q(declare P)`, and expected stopping times under P and Q. The present note identifies and certifies a strict-separation subclass of the source-dependent-first-kernel family, the next unexplored family in `299faa2130280f39be3d0cb14008c7be81366e67`. The R5 mother question remains open. Scientific pins: GLOBAL `a01383f825ef9d43b4b754254303298c64041568`, EM `86149263e38c22292c9def1e0f69092efa1be77e`; contemporary behavioral norms are read independently.

## I. Model and exact positive-part theorem

Let `H` be a finite hidden source set with `w_h>0`, `sum_h w_h=1`, where at time 1 both Q and P assign source probability `w_h` (so all source likelihood ratios are 1). At time 1 a source may STOP and freely declare P/Q or CONTINUE. On continuation, at time 2 key `j` with likelihood ratio `r_j>0`, the conditional **Q** kernel is `K_h(j)>0`, `sum_j K_h(j)=1`, and `sum_j r_j K_h(j)=1` for each source. The conditional P kernel is `r_j K_h(j)`; every source visits the same finite set of keys. At time 2 STOP/P, STOP/Q, CONTINUE are all legal. If the agent continues, its time 3 terminal likelihood ratio is `s in S`, with a **source-independent** positive Q kernel `M_j(s)>0` satisfying `sum_s M_j(s)=1`, `sum_s s M_j(s)=r_j`. Conditional P probabilities are `s M_j(s)/r_j`. Terminal P/Q declarations are free. FULL conditions on the actual history `(h,j,...)`; seedless LR sees only the observable `(time,likelihood ratio)` and independently randomizes actions using arbitrary real probabilities.

For `k>0`, put `C_k(r)=-min(r,k)`, the best conditional normalized signed payoff for free declarations in direction `n=(-1,-k,-c,0)`. Define the **first-gate classification gain**

`A_h(k)=sum_j K_h(j) C_k(r_j)-C_k(1)`

and **second-gate gain**

`B_j(k)=sum_s M_j(s) C_k(s)-C_k(r_j)`.

Convexity of `C_k` and the likelihood-ratio moment constraints give `A_h>=0`, `B_j>=0`. Write `Abar=sum_h w_h A_h` and `x_+=max(x,0)`.

**THEOREM (conditional first-gate support formula).** If `c>=0` and `B_j(k)<=c r_j` for **every** second-stage key `j`, the complete real-policy support functions in the above direction satisfy

`h_FULL(n)=C_k(1)-c+sum_h w_h (A_h(k)-c)_+`,

`h_LR(n)=C_k(1)-c+(Abar(k)-c)_+`.

Hence their exact gap is

`Delta(k,c)=sum_h w_h (A_h(k)-c)_+ - (Abar(k)-c)_+ >=0`.

If `min_h A_h(k)<c<max_h A_h(k)`, then `Delta(k,c)>0`; equality of the **entire** four-coordinate convex hulls is therefore excluded for this parameter region. This is a *sufficient separation criterion*, not a universal classification for all first kernels.

**Proof.** Under direction `n`, STOP at ratio `r` at time `t` has local Q-scaled payoff `C_k(r)-ct r`. CONTINUE at time 2 followed by optimal terminal declaration has local payoff `sum_s M_j(s)C_k(s)-3c r_j`, since `sum_s sM_j(s)=r_j`. STOP at time 2 has payoff `C_k(r_j)-2c r_j`. Their difference (continue minus stop) is exactly `B_j(k)-c r_j<=0`. Therefore stopping at every time-2 key is an optimal action for both FULL and seedless LR, irrespective of hidden-source posterior. For source `h`, STOP at time 1 pays `C_k(1)-c`, whereas CONTINUE followed by optimal time-2 declarations pays `sum_j K_h(j)(C_k(r_j)-2c r_j) = C_k(1)+A_h(k)-2c`. FULL selects their maximum independently for each `h`, producing the displayed formula. LR uses a single time-1 stop/continue action and, conditional on continuation, the pooled kernel `Kbar_j=sum_h w_h K_h(j)`; all time-2 optimal declarations depend only on the shared `r_j`. Taking the maximum after pooling gives its displayed formula. Behavioral randomization does not enlarge support maxima, since a finite tree's directional payoff is multi-affine in behavioral action probabilities. Jensen yields nonnegative gap, and the inequality is strict whenever positive source weight occurs on both sides of the kink `A_h-c=0`. QED.

## II. Strictly positive continuum of counter-candidates

Take two sources `A,B` of Q and P weights `w_A=w_B=1/2` and time-2 keys

`R=(1/2,1,3/2)`,

`K_A=(1/4,1/2,1/4)`, `K_B=(3/8,1/4,3/8)`.

All first-gate P/Q probabilities are strictly positive with mean likelihood ratio 1. At time 3 take common support `S=(1/4,1/2,1,3/2,7/4)` and three positive-probability reference laws

`V_low=(11,1,1,1,1)/15`,

`V_mid=(1,1,1,1,1)/5`,

`V_high=(1,1,1,1,11)/15`.

Their mean likelihood ratios are, respectively, `1/2,1,3/2`. For any **real** `epsilon` with `0<epsilon<=5/8`, set

`M_j(epsilon)=(1-epsilon) delta_(r_j) + epsilon V_j`.

Each `M_j` assigns strictly positive probability to **every** point of `S`. The resulting P terminal kernels `s M_j(s)/r_j` are also strictly positive and normalized. For `k=1`, exact algebra gives

`A_A=1/8`, `A_B=3/16`, `Abar=5/32`; and

`B_low=epsilon/12`, `B_mid=epsilon/4`, `B_high=epsilon/12`.

Thus `max_j B_j/r_j=epsilon/4 <= 5/32=c`, so the theorem applies **uniformly** throughout this continuous real-parameter family. Choose `n=(-1,-1,-5/32,0)`. The support difference is exactly

`h_FULL=-73/64`, `h_LR=-37/32=-74/64`, `Delta=1/64>0`,

independent of `epsilon` throughout `0<epsilon<=5/8`. In the open interval `0<epsilon<5/8`, all time-2 gates strictly prefer STOP for this normal; at the endpoint one time-2 node is indifferent, without changing the support.

An explicit FULL maximizer stops at time 1 for source A, declaring P; source B continues at time 1 and at time 2 stops at all three keys, declaring Q at `r=1/2` and P at `r=1,3/2`. Its exact observation is

`W=(3/32,13/16,3/2,3/2)`;

`n · W=-73/64`. Since `||n||_1=69/32`, duality supplies the strict rational geometric distance certificate

`dist_infinity(W,conv O4(seedless LR)) >= (1/64)/(69/32)=1/138`.

The witness does not use the terminal declarations, but every terminal edge is legal with strictly positive mass, so this is a genuine two-decision-gate model. The theorem classifies an *open interval of nontrivial terminal perturbations*, rather than relying on a deterministic pass-through terminal construction.

## III. Independent exact verification and coverage

`VERIFY.py` uses only Python 3 standard-library `fractions.Fraction` and `itertools`. At `epsilon=1/16` it independently checks Q and P transition normalization and likelihood-ratio first moments for every source and gate; derives `A_h`/`B_j`; calculates the signed supports analytically; explicitly computes `W`; enumerates **all 2,592 deterministic seedless LR policies** (`3` first-key actions × `3^3` time-2 action assignments × `2^5` terminal-label assignments), independently evaluates their complete four coordinates, and matches the maximal signed payoff with the Bellman value. It also checks FULL and LR Bellman recursions separately and five epsilon values including the endpoint `5/8`. `EXACT_OUTPUT.txt` is actual captured execution output, ending `PASS_EXACT_R5_SOURCE_DEPENDENT_FIRST_KERNEL_JENSEN`.

The universal theorem and the entire real epsilon interval are proved by the displayed symbolic identities. Enumerations establish the finite exact-instance certificate and check implementation consistency; they are not used as evidence of a general multi-gate classification or R5 completion. The work is an author-side mathematical derivation, awaiting independent project review and formal task authority.

## IV. Relationship to existing theory and research progress

The `C_k` support geometry uses the classical error-tradeoff/statistical-experiment perspective associated with D. Blackwell, *Equivalent Comparisons of Experiments*, Ann. Math. Statist. 24(2), 265–272 (1953), DOI `10.1214/aoms/1177729032`. Occupancy-based behavioral Markovization has general precedents such as R. Laroche and R. Tachet Des Combes, *On the Occupancy Measure of Non-Markovian Policies in Continuous MDPs*, ICML/PMLR 202 (2023), pp.18548–18562, `https://proceedings.mlr.press/v202/laroche23a.html`. These sources give methodological context; the explicit first-kernel Jensen formula, probabilities, and certificate above are derived here and do not claim a new general Blackwell theorem. The LR key is an observation quotient; sufficiency of that quotient must be proven, not inferred from ordinary Markovization at the full state.

**BRC interface applied:** source and branch identity, positive Q occupation, induced P via `rQ`, free declarations, time-indexed observer, and positive-part Jensen residual. P000 native X6 ontology and the protected ACTIVE residual-fidelity worldview remain untouched; this is a scoped stochastic BRC observation theorem, not a physical/X6 motion assertion.

## V. Next discriminating problem

The present exact obstruction exposes early source-dependent information gains whenever the downstream continuation reward is weak enough that the second gate can be made inactive by a legal four-observer normal. The remaining source-dependent-first-kernel route should attempt **strong second-gate compensation**, where for every useful threshold `k` and candidate first-gate Jensen-splitting `c`, some reachable second key has `B_j(k)>c r_j`; the current suppression argument then cannot be applied. Construct a minimal strictly positive rational candidate with common and/or source-sensitive second kernels and compute complete four-dimensional hull inclusion certificates; if a hull-equality candidate exists, then test actual real-behavior observation-set membership. Alternative route: derive a necessary condition on the joint Bellman advantages for all signed `(TP,TQ)` tilts before searching. Retain all free declarations, true times and original source pins.