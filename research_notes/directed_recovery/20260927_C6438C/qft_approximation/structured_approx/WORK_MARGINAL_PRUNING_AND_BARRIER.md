# Certified work-label pruning: a constructive criterion and an exact barrier

Status: AUTHOR_SYMBOLIC_DERIVATION / SHARED_CONTEXT / NOT_ADMITTED.
Activity RA-CAAAC604CB513AEA8BBC1DFC. Current intake enterprise-math
671530e485921a9eeed91c1635decd60cc195dc3; GK f44ed5959c92e6e088c61c102951d1ab2c5e98d4.
This note introduces no new executed approximate propagation. The parent
verified the current startup guard and lease. All D internal coordinates,
signs and native feedback order remain in the mathematical interface.

The positive result is an implementable *conditional* pruning scheme whose
error certificate can be tested without an amplitude, order or factor oracle.
The negative result is sharp for collision-free prefixes: even a
history-dependent explicit sparse-row approximation needs nearly the entire
work support to satisfy the published global L2 contract. Neither statement
is a general dequantization algorithm or a lower bound on implicit encodings.

## 1. Exact preparation marginal needs no row oracle

Use the frozen actual instrument, with raw rows v_h(w) in R^D and branches

    v_(h,sigma)(z) = [v_h(z) + sigma T_h v_h(P_i^-1 z)]/2.

P_i is the typed work permutation and T_h is the complete orthogonal native
feedback in its actual temporal order. T_h may depend on the measured prefix
h and need not commute with any other feedback. The standard initial state
is v_empty(1)=e0. Define the unconditional work-label marginal

    mu_i(z) = sum_(|h|=i) ||v_h(z)||^2.

For each h, sum both signs before summing histories. The cross term cancels,
and orthogonality preserves the other-arm norm. Consequently

    mu_(i+1)(z) = [mu_i(z) + mu_i(P_i^-1 z)]/2.                 (1)

Thus mu_i is exactly the endpoint law of a classical preparation walk:
start at 1, and at each step independently keep the label or apply P_i with
equal probability. It can be sampled by actual typed column calls and fair
bits. No phase propagation, row query, hidden order or factor is involved.
Equation (1) concerns the work marginal after summing *all* measured histories;
it does not give the conditional work law at a selected h.

## 2. A concrete history-consistent approximation

Before sampling the quantum readout, freeze finite sets A_i of work labels,
for 1<=i<=t-1. They may be chosen by independent training randomness, but
must not depend on the later private walker trajectory. A_0 contains 1.
Let Pi_i project onto these work labels while keeping every internal
coordinate. Define the entire family of raw approximations recursively:

    u_empty=v_empty,
    u_(h,sigma) = Pi_(i+1) K_(h,sigma) u_h.                   (2)

K_(h,sigma) is the same actual branch map as above. This is a defined linear
approximation, not an assertion that projected evolution is the original
unitary dynamics. Missing work rows are exactly zero in u_h. Retained rows
keep all D residual coordinates; there is no internal-mode truncation.

On the one selected measured history, maintain u_h as a sparse dictionary.
To advance, add u_h(w)/2 at w and sigma T_h u_h(w)/2 at P_i w, combine signed
collisions, and retain only A_(i+1). A round has at most 2|A_i| candidate
labels before projection. Using this dictionary in the frozen approximate
single-walker kernel gives constant-time row lookups after its construction.
Use the required fair fallback when both queried approximate rows are zero.
Do not rescale by the latent trajectory or modify u_h using that trajectory.

Projection breaks the norm-complete instrument for u. In particular, the
approximate walker is NOT claimed to have latent law proportional to
||u_h(w)||^2. Correctness uses the published reference-weighted kernel error
contract, not an incorrect invariant for the projected process.

## 3. Orthogonal error accounting

Let V_i and U_i be the direct sums of all exact and approximate depth-i
history fields. Let F_i be the exact adaptive instrument from this direct
sum to the next one. Summing both outcomes makes F_i an isometry, even
though its T_h blocks differ across h. Projection Pi_i acts on the work
coordinate of every history block. Put

    E_i = ||U_i-V_i||^2,
    delta_i = sum_(z not in A_i) mu_i(z).

Then

    U_i-V_i = Pi_i F_(i-1)(U_(i-1)-V_(i-1))
                 - (I-Pi_i) F_(i-1)V_(i-1).

The two displayed vectors have orthogonal work support. Since F is an
isometry and Pi a contraction,

    E_i <= E_(i-1) + delta_i,
    E_i <= sum_(j=1)^i delta_j.                              (3)

This is stronger than a triangle-inequality sum of square roots. The audit
coauthor supplied and cross-checked the orthogonality improvement. It is
shared mathematical review, not independent admission.

The already published mass-weighted approximation theorem therefore gives

    TV(final exact joint(h,W), approximate joint(h,W))
      <= sum_(i=1)^(t-1) sqrt(sum_(j=1)^i delta_j)            (4)
      <= sqrt[(t-1) sum_(j=1)^(t-1) (t-j) delta_j].

The t-th projection is unnecessary if only readout/terminal latent sampling
is requested. Any common deterministic postprocessing preserves this TV
bound. The fair zero-pair fallback makes all divergence paths total.

For example, a uniform certified delta_j<=d suffices with
sqrt(d) sum_(i=1)^(t-1) sqrt(i)<=epsilon. A looser entirely rational choice
is d=epsilon^2/[(t-1)^2 t] for t>=2; (4)'s second bound is then at most
epsilon/sqrt(2), hence at most epsilon. These are certificate allocations,
not assertions that such small sets exist.

## 4. Testing the missing mass without the circular row oracle

Generate candidate A_i from a training sample of preparation walks using
(1), or from another declared construction. Freeze the sets before drawing
an independent validation sample. One length-(t-1) preparation walk yields
one observation for every depth. Correlation across depths is harmless for
a union bound; different validation walks must be independent.

A simple exact one-sided test for a declared threshold d_i in (0,1) is:
accept depth i only if none of m validation labels lies outside A_i. If
delta_i>d_i, the probability of this false acceptance is at most

    (1-d_i)^m.

Choose m so that this rational power is at most zeta_i, with
sum_i zeta_i<=zeta. No numerical logarithm is required to verify this
inequality. The approximate sizes, m, typed column work and random-bit
contract are part of the cost. A test with misses is simply inconclusive
for this zero-miss rule; it is not evidence of a hidden order or failure
of the exact instrument. More general one-sided binomial intervals could
be substituted, but none is executed or assumed here.

The logical probability statement is

    Pr(validation accepts AND some delta_i>d_i) <= zeta.     (5)

It is NOT the same bound conditional on acceptance. One must not keep
regenerating sets/tests until something passes with the same zeta budget.
For a completed sampler, define one outer attempt: if validation fails, use
the exact original sampler; if it passes, use (2). Combining (4) and (5)
gives unconditional output TV at most epsilon+zeta. The fallback may be
expensive, and no polynomial expected runtime is claimed without bounding
its probability and cost. A run that instead stops as PARTIAL must report
that outcome; it is not a complete approximate sampler of the target law.

An artifact from a passed test is a statistical certificate under this
random-source contract, not a deterministic proof that its unknown delta_i
is small. Training, validation and eventual walker randomness are separated.
Condition on the former seeds when applying (2)--(4); charge (5) only in the
outer distribution, without silently postselecting the seed.

## 5. Cost criterion and limits of any claimed improvement

If the certified sets have size at most K, construction of one approximate
history uses O(t K) typed modular-column requests and O(t K) complete
feedback-vector actions, plus membership, signed sums and exact bit cost.
Stored numerical rows need O(KD) slots; retained sets need O(tK) labels.
Native admissions, training/validation, column caches, traces and exported
certificates are charged separately. In particular these are not a claim
that *total* memory is O(KD). No full-domain table is needed for the test.

This genuinely reduces the executed row-field size when an independently
frozen small envelope captures almost all mu_i mass. It assumes neither
polynomial K nor a cheap successful certificate. The following exact barrier
shows why the criterion need not help ordinary large-order Shor prefixes.

## 6. Even history-dependent row sparsity fails before collisions

Suppose the first i preparation addresses give 2^i distinct work labels.
For the standard square schedule their labels are

    a^[2^(t-i) j] mod N,       0<=j<2^i.

For analysis only, the exact condition is
ord_N(a)/gcd(ord_N(a),2^(t-i)) >= 2^i. It is not an input or a free
certificate provided to the algorithm. Under this condition every address
has one unique label, and at every measured prefix h its internal row is
2^-i times an ordered product of signed orthogonal T matrices applied to e0.
Every occupied row therefore has squared norm 4^-i, irrespective of h.
All 2^i prefixes have mass 2^-i. No ideal scalar phases or commuting claim
is used in this calculation.

Let an arbitrary approximation u_h have at most K nonzero work rows per h;
the selected rows may now depend on h. At least 2^i-K exact rows are omitted.
Their errors cannot be canceled by errors at retained labels, so

    ||u_h-v_h||^2 >= max(0,2^i-K) 4^-i,
    sum_(|h|=i) ||u_h-v_h||^2 >= max(0,1-K/2^i).              (6)

Consequently satisfying the published sufficient contract
sum_i sqrt(E_i)<=epsilon<1 requires, at this one layer,

    K >= (1-epsilon^2) 2^i.                                 (7)

The same result with unequal K_h charges their uniform average over h.
For the weaker fixed-envelope case, even after collisions each preparation
label has mass at most ceil(2^i/r_i)/2^i, where
r_i=ord_N(a)/gcd(ord_N(a),2^(t-i)). Hence a set of K labels misses at least
max(0,1-K ceil(2^i/r_i)/2^i) mass. These are analysis bounds; no order is
revealed to the algorithm.

Equation (6) is an exact obstruction to explicit sparse-work approximations
under this L2 certificate, including adaptive choices of their support.
It is NOT a lower bound on implicit row-query representations, on the actual
TV error of every pruning method, or on all possible samplers. A sufficient
norm contract can fail even when a special kernel has a separate exact
shortcut. The previously certified Jacobi last-bit shortcut is one such
reason not to confuse representation error with necessary sampling error.

## 7. Research continuation

The constructive test can establish whether a concrete input has a cheap
work envelope, without assuming one or invoking a circular amplitude oracle.
The collision-free barrier predicts that successful general compression
must retain the omitted work information implicitly, exploit an independently
proved weaker observable contract, or allow structured cancellations within
a representation that is not simply a short list of work labels.

This is symbolic research only. No projected native execution, empirical
missing-mass certificate or new scientific BRC receipt is claimed. Existing
complete native operations and the frozen mass-weighted theorem are the
dependencies; implementation and bounded validation would be a separate
evidence unit. No ideal-QFT propagation is used or proposed as a substitute.

Source: the already read local/ published
`sep27-qft-research/point_queries/MASS_WEIGHTED_APPROXIMATION_BOUND.md`, with
its BGL 2022 antecedent and independently derived native-kernel constants.
This note makes no worldwide-priority claim for projection or statistical
holdout methods. All new algebra is displayed above.
