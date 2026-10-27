# R5 — Isolated single-LR-collision: exact hull/image dichotomy from terminal kernels

Date: 2026-10-27 (Asia/Taipei). **NONBLIND / PORTABLE / HAND-PROVED / FRACTION-TESTED / UNREVIEWED / NOT_ADMITTED**. This is an author-level new deduction from the published R5 external two-law stopping-tree work; **not** a native Driver Review, official Task, frozen Result, independent clean-blind verification, or native heartbeat/X6 dynamics theorem.

Source basis: Enterprise Math main at `d3512bf729f1bee813a17b74a12a8e1d26985030`, and global-knowledge canonical main at `2bd7359370f9619cdad452c21b7e1855fee07363` (P000 full V4 Git blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`). Exact predecessors: `research_notes/brc_r5_two_level_critical_price_gate_20261027_t11/PROOF.md`, `research_notes/portable_direct/20261027_r5_eight_leaf_strict_hull_separator_nonblind.md`, and the original R5 author model `research_notes/brc_r5_general_hinge_zonotope_causal_8leaf_20261027/PROOF.md`. All original author/contribution attribution remains unchanged. The result answers a narrower *structural impossibility* question and does not repeat the previously excluded individual tree.

## Exact finite-tree class

There are `k>=2` hidden source histories `h_i` arriving at the same time `t` and with **the same observed likelihood ratio** `r>0`. Their *conditional* Q masses `q_i>0` sum to 1 and the corresponding P masses are `r*q_i`. This is a normalized **subtree contribution**: when `r!=1`, do not mistake its conditional P mass `r` for normalization of a standalone global P probability law. Identical external branches outside the subtree can be added without changing any separation.

At time `t`, each source may stop and declare `P` or `Q`, or continue directly to terminal time `t+Δ` (`Δ>0`), without intermediate actions. Conditional on continuing from `h_i`, the finite positive Q distribution of terminal ratios `u_j>0` is `μ_i(j)>0`, with
`Σ_j μ_i(j)=1`, `Σ_j u_j μ_i(j)=r`.
Terminal actions only declare `P` or `Q`. Full-history policies can distinguish `h_i` and their terminal descendants; **seedless likelihood-ratio policies** use only `(time, LR)` with fresh local randomization and no persistent common random seed. Both classes permit all real local action probabilities.

The four-vector (subtree contribution) is
`O=(P[D=Q], Q[D=P], E_P[τ], E_Q[τ])`.
Use ordinary finite *positive* P/Q weights, retaining provenance until the explicitly scoped observer calculation. Signed support gaps are dual observer quantities, **not signed BRC masses**. This theorem is external stochastic mathematics: it asserts no embedding or native transition-law correspondence to P000's X6+time.

## Theorem — exact one-collision dichotomy

Under precisely the above assumptions:

**(A) Identical conditional terminal LR kernels.** If every `μ_i` is equal, then
`O_full = O_seedless-LR` **as actual attainable four-vector sets**, not just as convex hulls.

**(B) Distinct conditional terminal LR kernels.** If two `μ_i` differ, a linear support functional of the restricted form
`J_{s,η}(O)=O_1+s*O_2+η*O_4`, with `s>0, η>=0`, strictly separates the full and seedless-LR observation hulls:
`min_full J_{s,η} < min_seedless-LR J_{s,η}`.
For rational `r,u_j,q_i,μ_i,Δ`, both parameters and the gap can be chosen rational.

Consequently **this isolated single-collision/terminal class cannot realize**
`conv(O_seedless-LR)=conv(O_full)` but `O_seedless-LR != O_full`.
A candidate for the general R5 mother question must escape at least one explicit hypothesis (for example interacting further nonterminal decisions or distinct cross-time LR-signature collisions). This is *not* a no-go statement for general trees.

## Proof of (A): construct a single seedless policy reproducing any full policy

For each `i`, let `a_i,b_i,c_i>=0` be probabilities of stop-declare-P, stop-declare-Q and continue, with `a_i+b_i+c_i=1`. On continuing, let `z_{ij}∈[0,1]` be the terminal probability of declaring Q at `u_j`. Assume `μ_i=μ`.

Set
`ā=Σ_i q_i a_i`, `b̄=Σ_i q_i b_i`, `c̄=Σ_i q_i c_i`.
If `c̄>0`, define the common terminal action
`z̄_j=(Σ_i q_i c_i z_{ij})/c̄`; if `c̄=0`, set `z̄_j=0` arbitrarily. This specifies valid seedless probabilities. In Q measure, every stop outcome and terminal ratio is preserved because `μ_j` is shared; in P measure, the factors `r` on stopping and `u_j` on terminal leaves are shared. Time is either `t` or `t+Δ`, so both expected stopping times are preserved as well. Thus all **four** coordinates agree exactly. Conversely seedless policies are full policies with tied decisions, proving equality of the entire attainable sets.

This is direct constructive aggregation, not an assertion that terminal ratios determine the full history or that discarding provenance is harmless for other observers or future operations.

## Proof of (B): one separating price from finite call transforms

For `s>=0` define the conditional terminal Bayes gain
`G_i(s)=min(r,s)-Σ_j μ_i(j)min(u_j,s)`.
It is nonnegative by concavity of `min(x,s)` and `E_{μ_i}[u]=r`. Equivalently,
`G_i(s)=Σ_j μ_i(j)(u_j-s)_+-(r-s)_+`.

For any `η>=0`, write `δ=ηΔ`. The optimal stop declaration at `t` costs `min(r,s)` per Q mass, while continuing and choosing the Bayes declaration at every terminal ratio costs `Σ_j μ_i(j)min(u_j,s)+δ`, ignoring the common time baseline `η t`. It follows by exact Bellman linearity for *all real local randomizations* that

`V_full(s,η)=min(r,s)+η*t - Σ_i q_i (G_i(s)-δ)_+`,
`V_LR(s,η)=min(r,s)+η*t -(Σ_i q_i G_i(s)-δ)_+`.

The seedless terminal Bayes choice `min(u_j,s)` is the same at every source, so no source-dependent terminal action can improve a *linear* support minimum; this is why the displayed `V_LR` is exact.

Subtracting gives
`V_LR-V_full=Σ_i q_i (G_i(s)-δ)_+ -(Σ_i q_i G_i(s)-δ)_+ >=0`.

For finite probability laws on positive support, the call transform `C_i(s)=Σ_j μ_i(j)(u_j-s)_+` uniquely determines `μ_i`: its piecewise-linear slope changes at `u_j` by exactly the probability mass of that ratio. Since all `μ_i` have the same mean `r`, two distinct kernels must have `G_i(s)!=G_l(s)` at some `s>0`. Take `δ` strictly between the minimum and maximum of the `G_i(s)`. Then both strictly positive and strictly negative values of `G_i(s)-δ` occur with positive `q_i`, making the preceding positive-part Jensen gap **strictly positive**. Set `η=δ/Δ>=0`. For rational data, evaluate at a rational breakpoint or within a rational open interval of nonzero transform difference and choose rational `δ`. QED.

## Exact reproducible rational sanity checks (not a substitute for the proof)

**Earlier eight-leaf R5 model.** Use `r=1`, `Δ=2`, `q=(1/2,1/2)`, `u=(1/4,3/4,5/4,7/4)`,
`μ_A=(9,5,11,7)/32`, `μ_B=(8,8,8,8)/32`.
At `s=3/4` the gains are `G_A=9/64`, `G_B=1/8`. With `δ=17/128` (so `η=17/256`), the exact Jensen separation is `1/256`. This **recovers** the previously published one-tree certificate; it is not credited as a fresh independent numerical discovery.

**A three-hidden-history check.** Use `r=1`, `u=(1/10,99/100,101/100,19/10)` and the strictly positive normalized mean-one kernels `K(p)=(p,1/2-p,1/2-p,p)` with `p=(1/10,1/4,2/5)`, `q=(1/4,1/2,1/4)`. At `s=1`:
`G=(47/500,91/400,361/1000)`, `δ=91/400`, `V_LR-V_full=267/8000>0`.
A separately run Python standard-library `Fraction` checker verified all normalizations, both separation calculations and **375** rational randomized-policy cases of the constructive four-coordinate reduction for a common kernel. There was no approximation, floating-point optimization, new axiom, `sorry` or `admit`. Local reproducer: `EM_R5_SINGLE_COLLISION_DICHOTOMY_CHECK_20261027.py`; exact output: `EM_R5_SINGLE_COLLISION_DICHOTOMY_CHECK_20261027.json`. These local file references are auxiliary, not evidence of native Source publication of those two local files.

## Research routing and admissibility

Method resolution: `REUSE_APPLIED` to the existing exact positive-mass BRC two-law carrier and source-provenance tracking, `COMPOSE_APPLIED` to the R5 Bellman/hinge support method, `PROVED_NEW_SCOPED_DIFFERENTIATION` for the call-transform injectivity plus four-observer exact image construction. No general-purpose tool or native dynamics claimed.

This entire note is **SOURCE-EXPOSED / NONBLIND / UNREVIEWED / NOT_ADMITTED**. The present Chat/connected Site has only `source:read/control:read`, no Source-active Driver DA, no independent clean review of these mathematical claims and no native CLAIM/open. A GitHub commit of this evidence does not create a Driver Review, Reference pass, Synthesis, Follow-up, V2 Task, Research Activity registration or Working Truth. Author-led/previous R5 conclusions and existing formal review records retain their original status. If this conditional theorem is later used to filter candidates, preserve the one-stage/one-collision/terminal restriction and the full four-observer assumption.

Smallest next discriminating mathematical unit: classify **interacting intermediate LR-signature merges** in which multiple future decisions couple source-weight aggregation; seek an exact equal-hull witness surviving all unrestricted four-direction support tests before attempting all-real nonattainability. Deduplicate against existing R5 owner work and retain the original parent mother question.
