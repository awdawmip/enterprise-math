# EC49BR — Finite-axis-group BRC rank and horizon-dependent count recovery

**2026-10-30. AUTHOR_ANALYTIC_PROOF / EXACT_NATIVE_BRC_FINITE_CHECK_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED.** This is an author-side continuation of EC49BQ, not a formally admitted research Result.

## Carrier and observer semantics

Keep the original six signed X6 axes, all 12 native directions, the ordered steps and positive-rational BRC weights. For even n >= 4r >= 4, U_n is the set of ordered length-n zero-displacement words. For t in U_n, write P_r(t), S_r(t) for the signed ordered length-r prefix and suffix, and chi_w(t) for its exact product of positive/negative step weights. Let q_i=w_i^+ w_i^->0. The selected ensemble mu:U_n -> Q_{>=0} retains word identity and multiplicity. A filter returns the sum of mu(t)chi_w(t) over the selected words. **This selected-ensemble/filter facility is an auxiliary extension; native endpoint_weight aggregates all compatible paths and does not implement it.**

Allow finite sequences of prefix and suffix filters and a finite subgroup H <= S6 of sign-preserving axis permutations. The **fixed-weight-instrument** family observes chi_w(sigma t) 1[P_r(t)=p,S_r(t)=s] for every sigma in H and every ordered end pair (p,s). Relabeling the selector as well only reindexes these complete rows. In the separate **covariant-instrument** family the weight table is relabeled along with the path; chi_{sigma w}(sigma t)=chi_w(t). “Minimal” below means least rational-linear additive dimension valid for arbitrary nonnegative rational selected ensembles, not arbitrary bit encoding.

## Theorem 1 — General rational count-character matrix

For each end pair (p,s), let a_i^+ and a_i^- be the counts of signed axis i in the concatenated ends, b_i=max(a_i^+,a_i^-), and

K_{p,s}={k in Z_{>=0}^6: sum_i k_i=n/2, k_i>=b_i for all i}.

Define a finite exact rational matrix with rows sigma in H and columns k in K_{p,s}:

M_{p,s}(sigma,k)=product_{i=1}^6 q_{sigma(i)}^{k_i}.

Then the minimum number of rational-linear additive coordinates sufficient for all fixed-instrument composed end filters is EXACTLY

**R_fixed(n,r,H,q) = sum_{p,s in D^r} rank_Q M_{p,s}, with D={±E_1,...,±E_6}.**

If the original unweighted total path count is also observable, exactly one coordinate is added iff for some (p,s) the all-ones row is NOT in row_Q(M_{p,s}). Under covariant action, the rank instead remains 12^(2r); count adds one iff not all q_i are equal (EC49BQ).

**Proof.** Every closed word contains k_i positive and k_i negative occurrences of axis i, with sum k_i=n/2. Fixed end steps force k_i>=b_i. Conversely, for any such k place k_i-a_i^+ positive and k_i-a_i^- negative steps in the middle: these are nonnegative, total n-2r, and arbitrary middle orderings yield real native signed words in this exact cell. Thus K is the complete set of possible interior count configurations. A fixed-instrument weight on these words is product q_{sigma(i)}^{k_i}, independent of their internal order; the observer rank on this fibre is rank_Q M. Different end pairs have disjoint supports, hence the total is the direct sum of fibre row spaces. Count is in that direct sum iff its restriction to every cell is in the corresponding span. The rank lower bound uses the finite-ensemble lemma of EC49BP: if a rational-linear proposed statistic kills z while some output does not, choose a sufficiently large nonnegative rational ensemble a so both a and a+z are admissible, giving identical proposed state but distinct output. The displayed observations span the required row space, so the bound is attained. In the covariant case, relabeling of the instrument cancels relabeling of the path, and the prior complete end-pair/count theorem applies. QED.

This is an exact finite computation method for fixed n,r,H,q. Prime valuations can encode positive rationals but **the rank of the valuation vectors is not interchangeable with the rational rank of the monomial evaluation matrix**.

## Theorem 2 — Exact n=4,r=1 group orbit

Put V_H(q)=span_Q{(q_{sigma(1)},...,q_{sigma(6)}):sigma in H}, rho=dim V_H(q). Then

**R_fixed(4,1,H,q)=132+12rho.**

The original count adds exactly one iff 1_6 is NOT in V_H(q).

**Proof.** There are 144 signed end pairs. Twelve have s=-p, and each such cell contains two orders of a middle roundtrip on any of six axes. For external axis a and inner axis j, the weight after sigma is q_{sigma(a)}q_{sigma(j)}. The first factor is nonzero, so its row span on six j choices has dimension rho. In the other 132 end pairs, the middle signed-step multiset is fixed; one or two internal orders have equal strictly positive weights under every sigma, hence each contributes rank one and already determines its count. On the opposite-end cells the unweighted count is the six-vector 1_6. QED.

For H=S6 and positive q, rho=1 if q is constant, else rho=6: the orbit average has a nonzero constant component, and swapping unequal entries generates the zero-sum subspace under the full permutation group. Thus ranks are 144 and 204, respectively, and count needs no additional coordinate in either case.

For H generated by swapping axes 1 and 2, three exact cases are:

| Roundtrip weights q | rho | weighted rank | weighted + count |
| --- | ---: | ---: | ---: |
| (2,3,3,2,1,1) | 2 | 156 | **157** |
| (2,4,3,3,3,3) | 2 | 156 | **156** |
| (3,3,3,3,3,3) | 1 | 144 | **144** |

In the second case q+(12)q=6·1_6, so even though q is nonconstant the two observed weighted group channels recover count. In the first case entries (3,2,1,1) fixed by the transposition prevent 1_6 from belonging to the two-row span. An exact information-loss witness for the first case is A=(+E3,+E1,-E1,-E3) and B=(+E3,+E4,-E4,-E3). These two single-word ensembles have the same ends, count and original weighted filter outputs (weight 6), but their weights after swapping E1/E2 become **9 versus 6**.

## Theorem 3 — Sharp horizon jump

Let H be generated by swapping axes 1 and 2 and suppose q_1 != q_2. For every even n >= 4r+2,

**R_fixed(n,r,H,q)=2·12^(2r).**

**Proof.** The 2r end steps impose sum_i b_i <= 2r, whereas n/2 >= 2r+1 leaves at least one free roundtrip in every end cell. Allocate this extra roundtrip to axis 1 versus axis 2, keeping other roundtrips identical. The ratio of swapped to unswapped weights changes by (q_2/q_1)^2 !=1, so the two group rows are linearly independent in EVERY cell. There are exactly two group members, so the per-cell rank is two. QED.

Consequently n=6,r=1 has rank **288**, versus 156 when n=4,r=1. For q=(2,4,3,3,3,3), the original count is recoverable at n=4 but **not** n=6. On the opposite-end cell (+E3,-E3) choose two free roundtrips on E1, E2 or E3. After factoring out the common external q_3=3, the two weight rows on these choices are (4,16,9) and (16,4,9). If a row combination were constantly 1, its first two coordinates force a=b=1/20, while the third equals 9/10 !=1. Thus count is independent, and the rank is **289** when count is included. This is a horizon-dependent failure of a valid shorter-horizon compression.

## Actual exact native audit

The executed checker VERIFY_EC49BR.py imports unchanged native signed_brc.py at Git Blob 300a96e3dc24bf6fff73743037a0347a8bc83176, and checks the SHA-1 Git blob of that source. It exhausts all **396** closed length-four signed-X6 words and all **144** end-pair fibres. It checks **288 native BRC weighted fibre identities per weight table (864 total)**, compares exact SymPy rational ranks, verifies the two-word counterexample, and evaluates all n=6,r=1 count-character matrices for the three tables. Both executions yielded identical JSON.

The original native BRC at n=6 has 19920 closed paths and whole-ensemble weight 152640, 532800, 537840 for q=(2,3,3,2,1,1), (2,4,3,3,3,3), and (3,3,3,3,3,3), respectively. All fixed-instrument row calculations use positive-rational weighted native X6 word carriers; the filter itself remains auxiliary. Analytic proofs, not finite sample extrapolation, support the general theorems. No physical heartbeat time, signed/complex cancellation, rotation dynamics, or project acceptance follows.

## Exact continuation EC49BS

Design a typed native selective-ensemble operator that preserves source word, sign, multiplicity and filter order, with an explicitly proved reduction to original endpoint_weight when mu=1 and no filter. Then study the character matrices for general groups/lengths and exact resource growth, distinguishing statistical rank from bit complexity. Obtain truly independent review under current Source owner/CLAIM authority, without treating this manuscript as an admitted task Result.