# R181 — Source-presence observer quotient and optimal rational affine dimension

Date: 2026-11-15. Status: **AUTHOR_PROVED / EXACT_CHECKED / NOT_REVIEWED**.
Scientific input pin retained: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. This is independent portable research, not a change to P000 or native heartbeat dynamics.

## Sources and precise scope

This extends R180, [complete-atom lossless tagged history](https://github.com/awdawmip/enterprise-math/blob/37ed0dded2613391926e9a56ad49b8a687694975/research_notes/portable_direct/R180_UNBOUNDED_SOURCE_ID_FIXED_RADIX_AFFINE_LIFT_20261115.md), and is related to R177's simplex representation of the *full transformation monoid*. The native interface read is `src/enterprise_math/brc_transport.py`, Git blob `be1debe367263931bd5e93fd750be3ed54624fe1`.

An atom is `(branch_id, source_id, ordered_signed_X6_path)`, with nonnegative integral IDs and a finite ordered path over 12 primitive signed directions of the six spatial axes. Let `A*` be the free monoid of **complete atoms**, including the empty history. Metadata and atomic histories are not extra native axes or physical time.

Fix any integer `k >= 1` and distinct target source IDs `T=(t_1,...,t_k)`. The declared observer reads, for each **separate positive BRC branch history**, whether source `t_j` occurred anywhere. Allowed future operations: append/prepend complete histories; positive rational-weight packet alternatives and serial composition. The observer does not request the exact source ID outside T, original branch ID, full path, or order of events.

## R181A — Exact two-sided contextual quotient

Define `b_T(w) in {0,1}^k`: bit j equals 1 iff a complete atom in `w` has source `t_j`. Then, for all `u,v`,

```
b_T(uv) = b_T(u) OR b_T(v),       b_T(empty) = 0.
```

This is a **surjective monoid homomorphism** onto `B_k = ({0,1}^k, OR, 0)`: every bit mask is realized by concatenating one atom for each selected source.

**Theorem.** Two histories agree under all left/right complete-history contexts followed by this observer iff their masks are equal; hence the exact observer quotient has `2^k` classes.

**Proof.** For every context `x,y`, `b_T(xuy)=b_T(x) OR b_T(u) OR b_T(y)`. Equal masks are therefore indistinguishable. Conversely take both contexts empty; unequal masks are distinguished. Surjectivity gives `2^k`. QED.

## R181B — Faithful k-dimensional affine lift and dimension lower bound

For `b in B_k`, define an affine action on `Q^k` by

```
F_b(x)_j = (1-b_j)*x_j + b_j .
```

That coordinate remains unchanged if its source is absent and resets to 1 if present. Direct substitution gives `F_b.then(F_c)=F_(b OR c)` (chronological order), and `F_b(0)=b` proves faithfulness.

**Theorem.** Every faithful representation of the full join-semilattice `B_k` by total rational affine transformations on `Q^d` has `d >= k`. The formula above attains the bound. The bound also holds when the empty-set map is not the ambient identity.

**Proof.** The image `E` of the semilattice identity is idempotent. Every image `G_b` satisfies `G_b=G_b E=E G_b`. Restrict all maps to the affine image of `E`; restriction is faithful because equal restrictions imply `G_b E=G_c E`. Its affine dimension is at most `d`, and its unit acts as identity.

Let `Z=G_full` be the image of the full mask. For any point `x`, `p=Z(x)` is fixed by every `G_b`, since `G_b Z=Z`. Translate this common fixed point to zero. The resulting linear maps commute, and each is idempotent; over `Q` their minimal polynomials divide `X(X-1)`, so they can be simultaneously diagonalized. Each diagonal entry is a multiplicative character `chi:B_k -> {0,1}` with `chi(empty)=1`.

Writing `e_i` for a singleton mask gives `chi(S)=product_{i in S} chi(e_i)`. To distinguish `full` from `full minus {j}`, one diagonal character must satisfy `chi(e_j)=0` and `chi(e_i)=1` for all `i!=j`. These required characters are different for the `k` distinct indices. Therefore at least `k` diagonal coordinates are necessary. QED.

This is a project-specific exact observation result; R177 considered a different transformation monoid and does not itself imply this bound.

## R181C — Exact positive BRC packet projection

Represent each fine packet as a finite multiset of `(positive rational weight, complete atom word, positive integer multiplicity)`. Its alternatives are multiset sum and serial product is the pairwise Cauchy product, with weights/multiplicities multiplied and words concatenated.

Let `Phi_T` replace each history `w` by `F_(b_T(w))` and sum multiplicities **only for coincident pairs (exact weight, affine effect)**. Then

```
Phi_T(H alternatives K) = Phi_T(H) alternatives Phi_T(K)
Phi_T(H then K)         = Phi_T(H) then Phi_T(K).
```

**Proof.** Multiset sum commutes with key coalescence. For each serial pair, exact weight and count multiplication agree on both sides, and `b_T(uv)=b_T(u) OR b_T(v)` makes the coarse affine effect equal to `F_b.then(F_c)`. Associative key accumulation gives equality of the resulting weighted multisets. QED.

This is exactly the declared source-presence query quotient under allowed future operations. It is not a safe quotient for queries retaining source names outside T, branch IDs, paths, ordered events or hidden native port state. Whole-atom parsing is essential: arbitrary fragments inside source-ID binary expansions do not form this monoid.

## R181D — One-dimensional encoding of full *counts*: a contrasting tradeoff

Let `c_T(w) in N^k` count the exact number of atoms from each queried source. Counts satisfy `c_T(uv)=c_T(u)+c_T(v)`. Choose `k` distinct rational primes `p_j` and define a one-dimensional affine **linear scaling**

```
H_c(z) = (product_j p_j^(c_j)) * z.
```

Unique factorization makes `c -> H_c` injective; chronological composition multiplies slopes, hence `H_c.then(H_d)=H_(c+d)`. Thus `N^k` has a faithful **one-dimensional rational affine representation** for any finite k, and zero dimensions cannot faithfully represent a nontrivial monoid.

The contrast is algebraic: exact Boolean presence has 2^k semantic states yet requires k rational affine dimensions because its transformations are idempotent, whereas unbounded additive count vectors admit a 1D prime-product encoding. Prime-product bit size grows as `sum c_j log_2 p_j`; decoding full counts by factoring and constructing the product have actual costs. This is **not** a claim of constant-bit storage or improved runtime.

## Verification and reproducibility

Reference program: `R181_source_query_affine_check.py`; exact output: `R181_verification.json`.
Run: `python R181_source_query_affine_check.py`. Python integers and `fractions.Fraction`, no floating point.

Selectors: `0, 2^65+17, 991, 2^128+99`. With k=4 the script checked all 256 ordered affine mask composites; identified each of four indispensable singleton characters; checked 1200 seeded complete-atom concatenation contexts including multiple signed X6 axes; compared 360 exact positive histogram alternative/serial operations; injected all 256 count vectors from `{0,1,2,3}^4` into prime products; and checked 250 random count product laws. All checks passed (`R181_EXACT_REFERENCE_PASS`). The proof is for every finite `k>=1`; the finite computations are illustrative tests, not the universal proof.

The GitHub `brc_transport` code was read and its `Affine.then`, `EffectHistogram.from_terms`, `.alternatives` and `.then` signatures checked. The repository package was not importable in the local compute environment; these exact histogram tests run an **independent reference**, not the original Python module. Native integration remains `LOCAL_VALIDATION_PENDING`, independent review `NOT_REVIEWED`.

## Control and next research frontier

The original control request `em-r1-20261115-1900-r181-s23-continuation-read` returned `FAILED / CANONICAL_REJECTED: unknown current immutable task publication` for `RS-S23-AV`. The result provides no verified formal CLAIM or full active-owner projection. This work follows independent portable research, preserving the R180 frozen scientific input. The known historical research identity and Activity are provenance only; no new execution authority is asserted.

Next scientific units: (1) native installed-package integration using reset affine maps and `EffectHistogram`; (2) minimum sufficient actions for joint source presence and **last-occurrence order**, or for typed port selectors; (3) bit and operation complexity, including source-index preprocessing, packet conversion, future composition and query recovery, compared with R180 full-history encoding.