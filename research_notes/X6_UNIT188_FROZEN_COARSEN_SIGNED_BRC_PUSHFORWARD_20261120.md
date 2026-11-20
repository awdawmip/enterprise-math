# X6 Unit188 — Exact signed native BRC pushforward under the actual frozen A3 weighted-field coarsening operation

2026-11-20. Parent PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905; task RS-X6-LEGACY-PLANE-RECONCILIATION / TP2-B4A441B23DA3159232C2. Research lane `chatgpt-research-onhour-enterprise-math-20260923`; maintenance lane excluded. Status: AUTHOR_PROVED / EXACT_FINITE_BIGINT_EXECUTED / SOURCE_REPRESENTED / UNREVIEWED / NOT_ADMITTED. Native PROGRESS, formal Result, and Driver review are separate operations.

## Immutable source and novelty

Native premise: `enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03:definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md` (Git blob `b4d49a1bbcccad0521618c6d20f6dcfa242b420a`), 12 signed primitive directions, N-step BRC path counts, a chosen Cell anchor (not geometric origin).

Genuine frozen producer/consumer: `enterprise-math@fd2bcff10ca6e147348b6c1236027fc0d2877df3:src/enterprise_math/weighted_relation_field.py` (Git blob `e50bf991e4dc4280063556a7aad1028f9f9404ed`), `weighted_relation_field`, `coarsen_weighted_relation_field`, `merge_weighted_relation_field`, `recover_totals_from_weighted_field`, and `split_two_block_totals_from_internal_relation`. Actual frozen tests: `tests/test_weighted_relation_field.py` (blob `51748dfe340c385907c4f2218fa1ae5ae2260522`). Existing Unit176 (support/fine versus coarse), Unit182 (relative zero returns), and Unit187 (uncoarsened six-block weighted field exact finite-horizon fibers) are consumed and not re-originated. New contribution: the BRC branch-multiplicity **pushforward through an actual source-defined partition**, the precise primitive multiplicities, sharp additive repair rank, and a numerical witness that coarse-field zero is not fine-field zero.

## Model and exact coarsening

Let the six signed native coordinate directions be `±e_i`. Fix positive capacities `m_i` for the *source A3 relation field*; they are relation weights, not native primitive direction counts. Let `P=(A_1,…,A_k)`, `1≤k≤6`, partition the six axis indices into nonempty named groups. Write `r_A=|A|`, `m'_A=Σ_{i∈A}m_i`, `C_A(z)=Σ_{i∈A}z_i`.

For the actual source producer `Z_ij=m_j z_i−m_i z_j`, direct integer expansion proves the exact source consumer identity

```text
Z'_AB = Σ_{i∈A,j∈B}Z_ij = m'_B C_A − m'_A C_B.
```

The frozen `coarsen_weighted_relation_field` implements this sum; the frozen `merge_weighted_relation_field` is its binary special case.

## Theorem A — path-multiplicity preserving pushforward

Let `N_n(z)` denote the number of ordered **length-n** native signed six-axis paths from the chosen anchor chart zero to endpoint `z∈Z^6` (all backtracking included). For any formal coarse endpoint `C∈Z^k`,

```text
Σ_{z:C(z)=C} N_n(z)
    = [y_1^{C_1}…y_k^{C_k}] (Σ_{A=1}^k r_A(y_A+y_A^{-1}))^n.
```

Consequently for any genuine coarse relation observation `W`, the full coarse-field BRC mass is

```text
Σ_{z:F_{m'}(C(z))=W} N_n(z)
    = Σ_{C:F_{m'}(C)=W} [y^C](Σ_A r_A(y_A+y_A^{-1}))^n.
```

*Proof.* Each native event `±e_i` is mapped to `±e_A` for the unique group containing `i`. For any coarse signed event `±e_A`, there are exactly `r_A` different named native events realizing it. For an ordered word, choices multiply, and summing all grouped words gives the Laurent polynomial product. Grouping endpoints by the exact frozen coarsened source field then yields the second formula by disjoint finite rearrangement. No approximation, limiting passage, positivity-for-signed cancellation, or missing trajectory assumption is used. □

The explicit coefficient formula for a fixed `C` is

```text
n! * Σ_{p_A,q_A≥0; p_A−q_A=C_A; Σ_A(p_A+q_A)=n}
       ∏_A [r_A^(p_A+q_A) / (p_A! q_A!)].
```

This is an integer since it counts named native words. **The correct BRC multiplicity is `r_A`, not `m'_A`.** Relation capacities are an independent type. Replacing one with the other is a measurable error when they differ.

## Theorem B — sharp independent repair ranks for future absolute-state operations

The group-total homomorphism `C:Z^6→Z^k` is surjective: choose one representative axis per group. Its kernel has free rank `6-k`. For every positive coarse capacity vector `m'`, the rational rank of `F_{m'}` is `k-1`, with one primitive integer gauge direction `m'/gcd(m')` (Unit187 at k=6, applied to k blocks). Therefore the full coarse-field map `F_{m'} ∘ C` has **free kernel rank `7-k`**.

For any true native endpoint `z`, its coarse field `W`, original capacities and grand total `G=Σ_i z_i` determine the group totals by the *genuine frozen source recovery formula*:

```text
C_A = (m'_A G + Σ_B W_AB) / Σ_B m'_B.
```

Then retaining `6-k` intra-group axis totals (all except a chosen one per group) exactly recovers `z`. Thus `G` plus `6-k` intra-group coordinates constitute an exact additive repair carrier for arbitrary later endpoint-dependent operations. The rank `7-k` is optimal among additive, independent integer-coordinate repairs, by the rational rank of the kernel. This is a **rank** statement; it does not claim a uniform fixed bit count. A single unbounded encoded integer is not excluded by rank alone. Full ordered path history requires richer path provenance.

For a binary merge, the frozen consumer additionally returns the discarded internal relation `Z_ij`; with the merged parent total, `split_two_block_totals_from_internal_relation` exactly reconstructs child totals. Thus source-native lost-relation repair is real rather than merely hypothetical.

## Explicit source-typed BRC counterexamples

Take original unit capacities `m=(1,1,1,1,1,1)` and partition `A={1,2}`, `B={3,4,5,6}`, giving `m'=(2,4)` and `r=(2,4)`. At path length `n=3`, the *coarse* field is zero exactly when `C_B=2C_A`. Reachable coarse totals satisfying this are `(1,2)` and `(-1,-2)`. Each has `3!/(1!2!) × 2^1 × 4^2 = 96` named native paths. The coarse zero-field mass is **192**.

But the *full fine* six-block field is zero only when all six coordinates coincide. At exactly three signed unit steps no such integer endpoint is reachable, so full fine zero-field mass is **0**. This is a direct falsifier of identifying coarse zero relation with original full zero relation or zero native displacement.

If `m=(1,2,1,2,1,2)`, the same group `A={1,2}` has `m'_A=3` but only `r_A=2` signed positive primitive choices. The one-step coarse endpoint `C_A=1,C_B=0` has actual path count 2; substituting source capacity 3 as BRC multiplicity incorrectly returns 3.

## Exact execution (author check; no independent review)

A standalone JavaScript BigInt checker enumerates native ordered length-0 through length-6 endpoint path counts by the 12 primitive directions, and independently computes grouped Laurent-polynomial coefficients using `2k` transitions weighted by group size. It compares the **entire coarse-field support and integer mass** across three positive capacity vectors, six partitions (including all axes separate and one single group), and seven lengths. It also independently recomputes genuine frozen coarsening and total-recovery formulas at each observed native endpoint, tests total mass `12^n`, and checks both explicit counterexamples.

Actual certificate counts: 30619 coarse field comparisons, 34032 grouped endpoint states, 186552 source coarsening comparisons, 186552 source total recoveries; all discrepancies zero. Highest length-6 native endpoint support size 6321. Integer counts use BigInt; no Python `assert` optimization semantics. The checker is an independent source-equivalent implementation, **not an imported frozen module or native benchmark**. The original R063 six-file benchmark already completed its own acceptance and was not rerun.

## Remaining mother objective

LP011 and LP019 exact historical error `commit:path:line` and typed consumer are still unresolved; the source's legitimate integer `max` and signed relation differences are not automatically those errors. Preserve author Units175 onward and historic149–152 Native association debt, the frozen source pin, independent Driver review `UNREVIEWED / NOT_ADMITTED`, and verified native semantic frontier through Unit174 unless current readback changes. Current RUN owner / private writer capability must be verified from the same real research lane; GitHub authorship or Activity is not protected native authorization.

Next exact scientific action: use the source's merge/discarded internal relation with a finite signed-X6 horizon to classify **when preserving only the discarded scalar suffices for a binary split and when branch-provenance or higher internal relations remain necessary for future BRC operations**; derive an explicit counterexample and minimal observer-specific repair. Alternatively pursue LP011/LP019 only from an exact offending source pin.
