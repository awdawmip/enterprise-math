# PREFIX-595-R6 — Nonnegative 34-class native BRC quotient and an exact four-port full-seven-reward circuit

Date: 2026-11-08 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_NATIVE_INTEGER_AND_RATIONAL_CHECK / UNREVIEWED / NOT_ADMITTED.

Science frozen at `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Model: original PREFIX-565 (`PREFIX565_positive_marginal_certificate.py`, Git blob `7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41`), 48 physical phases, 96 branch ports, six labeled native actions, gate marker and six-axis integer BRC rewards; nine roots `0, ±e1, ±e2, ±e3, ±e4`. PREFIX-591 supplies the exact 33-dimensional invariant observer U, and PREFIX-594 proves universal signature invariance for the triple (T,P0,P1). Explicit ports and transitions in the proof use the original zero-based source indices.

## Theorem A: a genuine nonnegative 34-class strong Markov quotient

Define an equivalence on original ports by `i ~ j` iff `f(i)=f(j)` for every `f in U=W3`. The original 96 ports form **34** distinct classes. For each allowed root r, every class C, each native reward signature `rho=(delta T,delta P0,delta P1)`, and every destination class D, the integer number
`N_r(C,rho,D)=#{a in ACTIONS : signature(i,a;r)=rho and destination(i,a;r) in D}`
is independent of the representative `i in C`. The exact 34-state labeled Markov quotient has transition probabilities `N_r(C,rho,D)/6 >= 0`. It reproduces the full joint law of (T,P0,P1) for every original initial port law, all n>=0 and any externally predetermined sequence of the nine roots. It is *a positive/state-class quotient*, not merely the previously proved signed 33-dimensional linear carrier.

**Proof.** The supplied certificate groups the 96 ports by exact evaluation tuples of the 33 rational U-basis functions. For each of 9 roots it evaluates six original native actions on every one of the 96 ports and checks equality of the complete joint (reward signature, destination class) count vectors within each source class. All 864 exact comparisons pass. The standard one-step strong-lumping condition therefore holds; induct on path length for a fixed root schedule. The 34 distinct classes are exactly the physical-port evaluation types of PREFIX-594. The corresponding 34 row-vectors span dimension 33 over Q, confirmed by exact Gaussian elimination in the certificate.

## Theorem B: a four-port identity retaining all original seven rewards and terminal port

Let `mu_plus=(delta_6+delta_29)/2` and `mu_minus=(delta_7+delta_28)/2` be distinct, legal nonnegative initial-port probability distributions. For each of the **nine frozen roots** r and each pair (j,w) consisting of the *full* seven-component original reward vector `w=(dR1,...,dR6,dK)` and the *exact next original port* j,
`
sum_{i in {6,29}} #{a : edge(i,a;r)=(j,w)}
 =
sum_{i in {7,28}} #{a : edge(i,a;r)=(j,w)}.
`
This equality holds as an exact integer identity, with twelve labeled actions counted on each side before grouping. The alternate pair (30,29) versus (31,28) satisfies the same identity. The certificate verifies **18** complete raw joint next-port/seven-reward counting-measure equalities.

**All-length corollary.** For every n>=1 and any predetermined nine-root schedule, the probability law under `mu_plus` and `mu_minus` of the **entire ordered length-n seven-reward sequence together with the terminal original port X_n** is identical. In particular, the entire joint law of cumulative `(R1,...,R6,K)`, and every moment/cumulant of that vector, is identical for the two start laws at every n. Proof: after the first step the joint distribution of (full original reward, exact next port) is equal; from that point the original Markov kernel and prescribed roots are the same, so condition on this shared pair and iterate. At n=0, the cumulative reward is identically zero but the terminal initial ports retain their stated distinct distributions.

The corresponding 34 class evaluation rows obey the exact four-point **affine circuit**
`
v(class([6,30])) + v(class([29]))
 = v(class([7,31])) + v(class([28])).
`
In certificate order, class indices are 3+15=4+14. Rank 33 on 34 distinct rows implies this relation spans the one-dimensional row-dependence space. Hence the earlier 33-dimensional linear information carrier, this positive 34-state quotient, and the physically distinct port starts are linked by one concrete zero-observer signed contrast.

## Provenance boundary: primitive action identity matters

If the observable also retains the **primitive native action identifier**, the two start mixtures are distinguished already at the first step, even for root zero. Four signed differences survive in the exact (action, original destination port, original seven-reward) counting measure, all at destination port 9 and actions (0,1) or (1,1); they cancel only after action identifiers are forgotten. Thus the equality above is asserted for full reward history and terminal port **without revealing initial port or action labels**. It is observer-/future-language-specific, preserving the project's native branch provenance discipline.

## Verification and reusable interface

Published checker: `research_notes/portable_direct/PREFIX595_R6_native_four_port_and_34class_certificate.py`. It imports the original SOURCE kernel and published W3; on the frozen inputs it must print `ALL_CHECKS_PASS`. During author testing, the same exact kernel/graded-module code copied from the immutable sources was run locally with Python `Fraction`/integer counters: graded dimensions (1,13,32,33); 864 equalities for strong lumping; rank 33; 18 full-seven kernel equalities; four action-label witness terms. No floating point or finite-depth extrapolation is used. Proof extension to all n is ordinary induction over the exact verified one-step identities. The GitHub checker's repository-native imports allow independent rerun against the published underlying source files.

BRC reuse: `REUSE_APPLIED` for PREFIX-565 exact native `edge`, PREFIX-591 exact W3 and PREFIX-594 invariant signature family. This new theorem is about native finite-state observer/reward transfer; P000 spatial dimension and theorem admission remain unchanged.

## Next independent unit

Compute whether the 34 positive-state evaluation types are all vertices of the convex hull of finite-horizon path-law rows, thereby determining the minimal size among *positive realization states* without restricting to deterministic port partitions. Independently characterize the four-port circuit algebraically from the two explicit phases and explain its action-label cancellation directly. Then quantify 34-class vs 33-linear representation update, coefficient/bit complexity and exact startup conversion cost, rather than treating state count as runtime.
