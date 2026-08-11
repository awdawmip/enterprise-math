# Long-Horizon Prefix Semantic Information: Finite Entropy amid Growing Class Count

Status: `RESEARCH BRIDGE / NONCANONICAL`

Researcher-ID: `R-8F3K`

For fixed generator count k, the number of full-timing semantic classes at exact word length H grows polynomially with H. Under a **uniform random literal-word workload**, however, the probability mass concentrates on early coupon-collector discovery histories.

The resulting Shannon entropy of the timing semantics converges to a finite constant.

This gives a sharp separation between worst-case semantic state count and workload-weighted semantic information.

## 1. Random-word model

Let literal actions be iid uniform on k generator labels.

At exact length H:

`H_literal = H log2 k`.

Let H grow with k fixed.

## 2. Terminal-set entropy vanishes

The probability that one particular generator has not appeared by time H is

`((k-1)/k)^H`.

By a union bound,

`P(any generator missing) <= k ((k-1)/k)^H`.

This decays exponentially to zero.

Therefore the terminal semantic state converges in probability to the deterministic full set, and

`H_terminal -> 0`.

So a terminal semantic algebra may have `2^k` possible states while the long-run workload entropy tends to zero.

## 3. Discovery order converges to a uniform permutation

Conditional on all k generators eventually appearing, symmetry makes the first-appearance order uniform over the `k!` permutations.

The probability of incomplete discovery vanishes, so

`H_discovery -> log2(k!)`.

Thus discovery-order information remains finite and nonzero: long random words almost surely reveal every generator, but the random order in which they first appear remains semantic data.

## 4. Coupon-collector waiting times

Suppose i distinct generators have already been discovered, with `1<=i<k`.

The next action is:

- already seen with probability `q_i=i/k`;
- a new generator with probability `p_i=(k-i)/k`.

Therefore the duration R_i of discovery phase i converges to a positive geometric variable

`P(R_i=r)=q_i^(r-1) p_i`, `r>=1`.

These waiting times are independent across coupon-collector stages, and the identity of the next new generator is uniform among the unseen labels independently of the waiting duration.

## 5. Entropy of one positive geometric phase

For success probability p and `q=1-p`:

`H(Geom(p))`

`= -sum_(r>=1) q^(r-1)p log2[q^(r-1)p]`

`= -log2 p - (q/p) log2 q`.

This finite value measures uncertainty in how long the prefix state stutters before the next new generator appears.

## 6. Full timing entropy has a finite limit

For fixed total horizon H, once all k generators have appeared, the final phase duration is determined by H and the preceding `k-1` waits.

As H grows, incomplete coupon collection becomes negligible. Hence

`H_timing -> C_k`,

where

`C_k = log2(k!)`

`      + sum_(i=1)^(k-1) H(Geom((k-i)/k))`.

Equivalently,

`C_k = log2(k!)`

`+ sum_(i=1)^(k-1) [`

`    -log2((k-i)/k)`

`    -(i/(k-i)) log2(i/k)`

`]`.

This is finite for every fixed k.

## 7. Sharp k=2 limit

For k=2:

- discovery order limit = `log2(2!)=1` bit;
- the only pre-completion waiting time is geometric with success1/2;
- `H(Geom(1/2))=2` bits.

Therefore

`H_timing -> 3 bits`.

The executable layer verifies numerically that by H=20:

- terminal entropy is near zero;
- discovery entropy is near1;
- timing entropy is near3.

## 8. Yet k=2 timing class count keeps growing

For k=2 and H>=2, exact timing semantic class count is

`N_timing(2,H)=2H`.

Thus

`log2 N_timing ~ log2 H + 1`

diverges.

At the same time workload entropy converges to3 bits.

So the worst-case index size and the Shannon average information move in qualitatively different directions.

## 9. Why the extra timing classes become negligible

Late discovery events correspond to unusually long runs of already-seen generators before a missing generator finally appears.

The number of possible late-discovery timings grows with H, but their total probability decays geometrically.

Class-count growth therefore measures reachable **possibility space**, while entropy weights that space by the actual workload.

Both are valid resources, but they answer different questions.

## 10. Literal provenance eventually dominates information

Literal entropy grows linearly:

`H_literal=H log2 k`.

Timing entropy tends to constant `C_k`.

Hence

`H_literal-H_timing`

`= H log2 k - C_k + o(1)`.

This is exactly the stutter-action provenance information from the parent decomposition.

As horizon grows, almost all new literal information records **which already-seen action label was chosen during semantically invisible stuttering**, not new prefix-state timing.

## 11. Discovery and duration information saturate separately

The parent decomposition gives

`H_timing-H_discovery = duration information`.

Therefore in the long-horizon limit:

- discovery-order information tends `log2(k!)` because terminal entropy vanishes;
- duration information tends the finite geometric-entropy sum;
- stutter provenance absorbs the remaining linearly growing literal entropy.

This gives an asymptotic semantic-information allocation by observation layer.

## 12. k=1 boundary

With one generator there is exactly one literal word at each fixed H.

All entropies are zero, and the asymptotic constant is0.

Across **different horizons** the prefix semantic operations remain distinct by duration, but the current probability model conditions on one exact H. This distinction between cross-horizon semantic cardinality and fixed-horizon workload entropy is essential.

## 13. Stage131 coding consequence

A table that must index every possible timing semantic class through a horizon may need polynomially many entries.

A workload-aware entropy code for exact-H random words may need only O_k(1) expected semantic bits in the long-horizon limit.

Neither replaces the other:

- table cardinality is a worst-case reachability/storage resource;
- Shannon entropy is a distribution-relative average coding resource.

Resource claims must say which one is being optimized.

## 14. Broader precision lesson

“More future horizon” can simultaneously:

- increase the set of mathematically possible semantic histories;
- decrease uncertainty of a coarse terminal state;
- leave a finite amount of discovery/timing uncertainty;
- create linearly more literal provenance information.

Therefore horizon is not a scalar proxy for semantic information.

Its effect depends on the observation layer and workload measure.

## Owner-local assets

- `src/enterprise_math/prefix_information_asymptotic.py`;
- `tests/test_prefix_information_asymptotic.py`;
- this bilingual theorem note.

## Prior art / status

Coupon collector waiting times, geometric entropy and occupancy convergence are standard prior probability/information theory. P023/A2 retains future-signature/precision ownership. This Draft owns only the fixed-k prefix-semantic information asymptotic specialization.

No repository strict CI, `EXECUTABLE_CHECKED`, or canonical claim. `CI_NOT_REQUIRED_FOR_RESEARCH`. Hard block: `NONE`.
