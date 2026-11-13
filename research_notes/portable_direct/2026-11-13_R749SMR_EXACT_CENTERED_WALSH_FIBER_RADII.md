# R749SMR — Exact centered Walsh-moment fiber radii for five-circuits and their complements

Date: 2026-11-13 (Asia/Shanghai). Research line: R749SMQ, PR #2233, frozen scientific input `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. Independent direct abstract mathematical continuation, no shared CLAIM asserted. Native Heartbeat World / P000 typing remains unchanged; the finite binary character dimension here is an auxiliary observer dimension, **not** native X6 spatial dimension. Source/activity registration request: `research2-20261113-1413-r749smr-session`, status pending when this note was prepared.

## 1. The centered fiber as a minimax problem

Let `G=F_2^d`, `N=2^d`, `chi_a(x)=(-1)^(a dot x)`. Given a retained nonzero character family `U`, define `F_0(U)={mu in Delta(G): sum_x mu_x chi_a(x)=0 for every a in U}`. The observer returns exactly these retained Walsh moments, and its prediction target is the identity distribution. The centered-fiber Chebyshev risk is
`rho_0(U)=inf_{q in Delta(G)} sup_{mu in F_0(U)} TV(q,mu)`.

**Lemma 1 (translation center).** Whenever `F_0(U)` is nonempty, `rho_0(U)=max_{mu in F_0(U)} TV(u,mu)`, where `u_x=1/N`.

Proof: translating `mu` by any `g in G` changes each moment only by the sign `chi_a(g)`, so `F_0(U)` is translation invariant. The function `f(q)=max_{mu in F_0}TV(q,mu)` is convex and translation invariant. Averaging the translates of any `q` gives `u`, hence `f(u)<=f(q)`. Compactness ensures attainment.

## 2. A dimension-independent exact theorem when the zero fiber has a two-dimensional support witness

Let `h(U)=min{dim H:H<=G, H^perp intersect U=empty}`, as in R749SMQ. **Theorem 2:** If `d>=3` and `h(U)=2`, then
`rho_0(U)=1-4/2^d`.

Proof: By `h(U)=2`, there is a two-dimensional `H` with every retained character nontrivial on `H`. Uniform mass on `H` has all retained moments zero, and its TV from `u` is `1-4/N`.

For the converse, `h(U)>1` means that no nonzero `g` has `a dot g=1` for every `a in U`. Thus for any two distinct states `x,y` some retained character takes the **same** sign on both. Under any `mu in F_0(U)`, each sign class of each retained character has mass exactly `1/2`, hence `mu_x+mu_y<=1/2` for all distinct `x,y`. Consequently any subset `S` of size 1 or 2 has `mu(S)<=1/2`; any subset of size 3 has `mu(S)<=3/4` by adding the three pairwise inequalities; all larger sets have `mu(S)<=1`. Now `TV(mu,u)=max_S [mu(S)-|S|/N]`. For `N>=8` each of these four cardinality ranges is bounded by `1-4/N` (for size >=4 immediately, and for sizes 1,2,3 by the displayed bounds). Therefore `rho_0(U)<=1-4/N`, completing the proof.

This is exact for arbitrary retained Walsh sets `U` with `h(U)=2`, irrespective of whether `U` itself is a character subspace. It is a theorem about **the centered fiber**, not the full moment-dependent nonlinear estimator.

## 3. The canonical five-circuit: exact centered risk 3/4

In `G=F_2^4`, put `C={1,2,4,8,15}`. This is the full-rank five-element XOR-zero circuit from R749SMQ; `h(C)=2`. For example, `H_C={0,1,14,15}` is a two-dimensional source subgroup on which every character in `C` is nontrivial. Hence Theorem 2 applies:
`rho_0(C)=1-4/16=3/4`.
There is no assumption of a linear prediction decoder in this statement: the center ranges over all probability distributions.

## 4. The ten-character complement: exact centered risk 1/2

Let `B=G\({0} union C)={3,5,6,7,9,10,11,12,13,14}`. Fourier inversion shows that **every** member of `F_0(B)` has unique coordinates
`mu_t(x)=[1+sum_(a in C)t_a chi_a(x)]/16`,
where `t in R^5` satisfies exactly sixteen inequalities
`1+sum_(a in C)t_a chi_a(x)>=0` for `x in G`.
Call this compact, full-dimensional polytope `P`. The centered TV objective is convex in `t`, so its maximum occurs at a vertex.

**Theorem 3 (26-vertex exact polytope certificate).** The vertices of `P` are precisely:
(a) the ten signed unit vectors `t=+e_i` or `-e_i` for `1<=i<=5`; and
(b) the sixteen vectors `t=s/3`, where `s in {+1,-1}^5` has sign product `+1`.
There are no others.

A finite-exhaustive proof: Every vertex of a full-dimensional five-dimensional polytope has five linearly independent tight inequalities. Enumerate all `binom(16,5)=4368` five-subsets of the displayed constraint rows. Solve every nonsingular `5x5` system exactly over the rationals, discard candidates violating any of the sixteen inequalities, and deduplicate. The accompanying complete, standard-library checker finds `3008` nonsingular active sets; the feasible candidates comprise exactly the 26 vectors above, confirmed by exact equality of the two sets. This is a finite rigorous certificate, not a floating-point sample. It can be independently rerun from the attached source.

At `t=±e_i`, `mu_t` is uniform on an eight-state character halfspace, so `TV(mu_t,u)=1/2`. At `t=s/3`, the even-parity sign patterns contribute masses `1/6` once, `1/12` ten times and `0` five times; hence `TV(mu_t,u)=5/16`. Convexity over the exact complete vertex set yields
`rho_0(B)=1/2`.
The lower bound is also witnessed by uniform mass on `H_B={0,1,2,3,4,5,6,7}`, a three-dimensional subgroup for which every `a in B` is nontrivial.

## 5. Research significance, evidence and open objective

For the two exceptional `d=4` families in R749SMQ, the earlier unrestricted minimax bounds are
`3/4 <= R_C(I) <= 5/6` and `1/2 <= R_B(I) <= 5/8`.
This result determines the exact Chebyshev risk **at the zero retained-moment observation**: `rho_0(C)=3/4` and `rho_0(B)=1/2`. Therefore any strict gap above these values in the full minimax problems must come from a nonzero moment fiber; alternatively a globally defined nonlinear decoder meeting these values would close both open problems. The centered-fiber result by itself does not choose between these alternatives.

Evidence: `R749SMR_CENTERED_FIBER_EXACT_CHECK.py` and `R749SMR_CENTERED_FIBER_RESULTS.json`; all rational arithmetic uses `fractions.Fraction`, the 120 state pairs and 4368 candidate active sets are exhaustively covered, and the run returned `PASS`. Theorem 2 and the translation center are proved algebraically. All 168 GL(4,2)-equivalent five-circuits and corresponding complements inherit the centered-fiber values.

Next discriminating question: optimize a **nonzero** retained-moment fiber (first a one-parameter symmetric family) and construct a certified nonlinear decoder or a rational witness whose radius exceeds the centered value. Preserve source, path and joint-moment provenance in later feedback-controller compositions. Actual V29/V39 native Cell/Link/Port licensing remains an independent unresolved bridge; no native event or mathematical promotion is claimed.
