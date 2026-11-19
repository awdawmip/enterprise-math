# R284AW — Finite-accuracy scalar observations suffice for exact calibrated Port reconstruction

Date: 2026-11-19. Status: **AUTHOR_PROVED / EXACT_FINITE_CHECK_PASSED / NOT_REVIEWED**.
Scientific sources: R284AT `R284AT_SPANNING_TREE_DIRECTED_PORT_COMPLETENESS_20261119.md`, R284AU `R284AU_QUADRATIC_SCALAR_PORT_RECOVERY_20261119.md`, and R284AV `R284AV_DISTANCE_GRADED_SCALAR_PORT_RECOVERY_20261119.md`. R284AU and R284AV were already independently published before this work, and their author contribution/Activity remain intact. This is the **new finite-absolute-error extension** of the already proved distance-graded observation schedule, not a reannouncement of the earlier exact-oracle O(n²) upper bound. Retain frozen source input R284AR `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Auxiliary named Port matrix only, not a native Heartbeat X6 dynamics claim. No CLAIM, formal Result or Review implied.

## AW1. Explicit bounded-error scalar observer

Let `n>=2` and `C=A/Q`, with known integers `Q>=1`, `M>=1`, and unknown `A_ij in {1,...,M}`. All matrices are strictly positive but may be singular. For every requested diagonal configuration `d` and one of the `n-1` oriented tree-edit channels `E_uv`, a **finite-accuracy** oracle returns a rational number `Y` obeying
[
|Y-det(operatorname{diag}(d)-C-zE_{uv})|
le arepsilon,qquad arepsilon=rac1{16Q^n}.
]
The error signs and magnitudes may vary adversarially and independently across requests; no stochastic assumption. An unedited scalar is the case `z=0`. Settings `d_i` are either zero or `T/Q`, and edits `z=1/Q`. The actuation range and error guarantee are **model assumptions**; they are not yet a physical instrument specification.

Let `K=n!2^n(M+1)^n`, and select the common integer
[
oxed{T=8K+3.}
]
The bit lengths of T, query inputs and finite-accuracy oracle outputs remain polynomial in `n,log(M+1),log Q`. Compared with the exact-oracle R284AU/R284AV, the larger T provides an explicit rounding margin that absorbs measured errors.

## AW2. Robust coefficient decoding lemma

For a subset S and the scaled integer matrix `A`, let `f_S(t)=det(diag(x_S(t))-A)`, with `x_i(t)=0` for i in S and t otherwise. Let `h_{S,uv}` use the matrix `A+E_uv`. Their coefficients are bounded in magnitude by K (a conservative permutation-count bound); coefficients of `g=h-f` are bounded by 2K. For `m=n-|S|`, denote their top-degree coefficients by `a_m` and `b_m` respectively.

A noisy *unedited* rational reading `Y_f` scaled by `Q^n` differs from integer `f_S(T)` by at most 1/16. Therefore
[
left|rac{Q^nY_f}{T^m}-a_might|
le rac{K}{T-1}+rac1{16T^m}
<rac18+rac1{16}<rac12.
]
The term K/(T-1) is zero if m=0.

For *two* noisy readings Y_h,Y_f, the scaled difference `Q^n(Y_h-Y_f)` deviates from `g(T)` by at most 1/8. Thus
[
left|rac{Q^n(Y_h-Y_f)}{T^m}-b_might|
le rac{2K}{T-1}+rac1{8T^m}
<rac14+rac18<rac12.
]
Consequently, **nearest-integer extraction recovers both top coefficients exactly from finite-accuracy scalars**, even with worst-case opposing error signs. Positivity is not used in this decoding lemma; it is used in the subsequent directed path divisions. No floating-point rounding is needed: the finite-accuracy readings may be supplied as finite rational numbers and rounded by integer comparisons.

## AW3. Noisy finite-scalar reconstruction theorem

**Theorem AW3.** Under AW1, *every* strictly positive rational n-by-n matrix in the calibrated class is reconstructed exactly from at most
[
oxed{N_{mathrm{AW}}(n)=3inom n2+1}
]
finite-accuracy scalar responses, using the `n-1` directed intervention channels of any chosen oriented spanning tree. The count, input length, output representation length and exact postprocessing are polynomial in the declared parameters. Recovery is deterministic for **every error sequence** satisfying the absolute bound.

**Proof.** Apply AW2 to the singleton, pair, edited-pair and triple coefficients required in R284AV. Since every coefficient is exactly the same integer as in an error-free observation, the entire tree-distance induction of R284AV runs unchanged: the n singleton readings recover diagonals; binom(n,2) pair readings recover directed pair products; n−1 edited-pair readings recover both directed tree entries; for each of the binom(n,2)−(n−1) unordered non-tree pairs, one baseline and one edited triple reading provide the single named two-hop product required by the sorted-distance induction. All divisors are positive and the recovered rational matrix is exact. The call count is `n+binom(n,2)+(n-1)+2(binomial(n,2)-(n-1))=3binom(n,2)+1`. None of the coefficient identities relies on an exact raw scalar once AW2 is established. QED.

**Digital precision/accounting.** At most `O(n^2(log n+log(M+1))+n log Q)` bits suffice to describe each scaled readout's integer magnitude and the declared absolute error budget; full determinant computations and coefficient extraction use polynomially bounded integers/rationals. The theorem trades large diagonal drive magnitude and numerical dynamic range for a quadratic number of scalar observations. It does **not** assert good relative conditioning, hardware feasibility, or that a sensor with a fixed small dynamic range can implement T/Q.

## AW4. Height-free noisy identification obstruction

For a *fixed finite* list of scalar determinant settings and any absolute noise tolerance `epsilon>0`, there is no universally exact entrywise identification on the class of **all strictly positive rational matrices without a common denominator/grid separation**. Choose distinct arbitrarily close rational matrices C,C' in the positive cone. Each finitely many determinant-polynomial response pairs can be made closer than `2epsilon` by continuity. Their permitted noisy reading intervals overlap for every query, so an adversarial sensor can produce the same transcript. This is a scoped impossibility result for fixed finite observation lists, not a statement about arbitrary growing/adaptive precision or oracle-driven exact rational encodings. Calibration in AW1 supplies the finite separation needed for exact decoding.

## AW5. Evidence, source labels and open problems

Companion: `R284AW_noisy_distance_graded_checker.py` and `R284AW_noisy_verification.json`. Standard Python integer Bareiss and `Fraction` simulation, fixed seed `28420261119`, denominator Q=37, alternating opposite errors `+/-1/(16Q^n)`. All 61 simulated full recoveries for dimensions 2..6 passed, including rank-one cases and the R284AR transpose-ambiguous 3x3 witness; 1,330 total finite-accuracy scalar responses, largest T 52 bits. Those are finite implementation checks; the **all-error-sequence** statement follows from the strict inequalities in AW2 and the R284AV algebraic induction, not the sample error signs. Independent Review: NOT_REVIEWED.

BRC/source observation discipline: measured scalars retain exact named channel identity, directed edit, signed cofactor difference and two-hop provenance. Finite-accuracy compression is certified only for the specified observer and precision horizon; no hidden-state equivalence, native X6 plane, or time evolution is inferred.

Next work: bound relative rather than absolute precision for a constrained diagonal drive budget; determine the joint tradeoff between scalar count and bit length/conditioning; reduce the constant `3binom(n,2)+1` using reusable triple witnesses; classify signed/zero-support finite-noise failures and repairs. Also reconcile the native owner inventory on its **original** in-flight read request, attach this exact Source to the legitimate existing Activity if permitted, and keep formal claim/review separate.
