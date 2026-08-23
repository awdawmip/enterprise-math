# Prime Fusion — Independent Replication Driver Review

Status: `DRIVER_ACCEPTED / CLEAN_INDEPENDENT_CORE_REPLICATION / T1-T15_PARTIAL_COVERAGE`
Date: `2026-08-23`
Driver-ID: `EM-DVR-R63A21`
Task: `RS-PRIME-FUSION-INDEPENDENT-REPLICATION`
Researcher: `EM-PFREP-28D707`

## 1. Inputs reviewed

Blind taskbook:

`research_tasks/PRIME_FUSION_INDEPENDENT_REPLICATION_20260823.md@28d707f475a8247d2b77b9ed3c6154278f857198`

Blind packet:

`research_inputs/PRIME_FUSION_BLIND_INDEPENDENT_REPLICATION_PACKET_20260823.md@096d7f4f3a6347b79bee58ae0973cea518780efa`

Independent owner branch:

`research/prime-fusion-independent-replication`

Frozen return:

`research_returns/PRIME_FUSION_INDEPENDENT_REPLICATION_RETURN_20260823.md`

Return blob at review: `e082eebda622de9e056f3251b16ebec699b4289b`.

Independent checker:

`experiments/prime_fusion_independent_replication_checker.py`

Checker blob at review: `fc67f08f146782728b00472ee0156c64bdf7747e`.

Checker commit recorded by the return before final return freeze:

`d82849c725553f4fd177a64e3956b858f8b2b19d`.

Source theorem package under later comparison:

`research/PRIME_FUSION_THEOREM_PACKAGE_20260823.md@e5138e17f8c4009f5e357f43326f2812c9df1359`

Draft review surface: PR `#597`.

## 2. Branch-isolation audit

Relative to taskbook source `28d707f475a8247d2b77b9ed3c6154278f857198`, the independent owner branch was `ahead 2 / behind 0` at review and added exactly:

1. `experiments/prime_fusion_independent_replication_checker.py`;
2. `research_returns/PRIME_FUSION_INDEPENDENT_REPLICATION_RETURN_20260823.md`.

No theorem package, source checker, Driver comparison, journal, Foundation file, or taskbook modification was introduced on the execution branch.

Verdict:

`OWNER_BRANCH_ISOLATION = PASS`.

## 3. Blindness / independence audit

The return freezes:

`BLINDNESS_STATUS = CLEAN`.

It declares that before return freeze the only mathematical repository inputs read were the taskbook, blind packet, and the exact primitive spatial definition permitted by that packet. It explicitly denies reading the theorem package, source-run checker, PR #597 discussion, source-result journals, Driver comparison, original research conversation, source-result commit messages/code search, or external literature.

The execution artifacts are consistent with that claim:

- the independent notation uses `A,B,N` rather than source `N,C,H`;
- the independent marked ratio is `r=+a b^{-1}` rather than source `r=-a b^{-1}`;
- consequently its second channel polynomial is `r^2-r+1` rather than source `r^2+r+1`;
- the return independently organizes its proof as ten theorems plus eight explicit failed-conjecture/counterexample classes rather than mirroring T1–T15;
- several source-only late algebra/phase results were not reconstructed.

These divergences are positive evidence against superficial source copying.

Verdict:

`INDEPENDENCE_STATUS = CLEAN_INDEPENDENT_CONTEXT_ACCEPTED`.

This remains validation evidence at the exact strength independently reconstructed; it is not proof by repetition and it does not validate source statements the independent run did not reach.

## 4. Independent return classification

The researcher's own final classification

`FULL_STRUCTURAL_REPLICATION`

is accepted **relative to the blind task R1–R6**. The return answers all six requested classification families, supplies proofs, preserves negative tests, and freezes an independently authored exact-integer checker.

Do not reinterpret that label as `T1–T15 ALL INDEPENDENTLY REPLICATED`. The blind task intentionally did not reveal or require the hidden theorem count.

Driver-strength classification:

`CLEAN_INDEPENDENT_CORE_REPLICATION_WITH_PARTIAL_SOURCE_PACKAGE_COVERAGE`.

## 5. T1–T15 post-freeze comparison matrix

Comparison labels:

- `EXACT_CONVERGENCE` — same theorem strength, allowing notation/sign convention;
- `EQUIVALENT_REFORMULATION` — independently reconstructed equivalent mathematical object/statement;
- `PARTIAL` — substantial source theorem content recovered, but a source-specific layer is missing;
- `MISSED` — not independently reconstructed;
- `COUNTEREXAMPLE` — source statement contradicted;
- `NEW_INDEPENDENT_RESULT` — independent return adds a theorem not explicitly packaged in T1–T15.

| Source theorem | Driver comparison | Independent evidence | Scope note |
|---|---|---|---|
| T1 simultaneous diagonal coordinates | `EXACT_CONVERGENCE` | Independent Thm 1–2: `2B-A=(a-b)^2`, `3A-2B=(a+b)^2`, exact inverse/image criterion | Same diagonal square data; independent return adds a full image criterion for arbitrary candidate channel pairs. |
| T2 exact common-divisor law | `EXACT_CONVERGENCE` | Independent Thm 1: `gcd(A,B)=gcd(a,b)^2` | Exact same strength. |
| T3 fusion algebra / discriminant 12 | `MISSED` | No independent construction of `Z[X]/((X^2+1)(X^2+X+1)) ~= Z[i] x Z[omega]`; no discriminant computation | Independent run found modulus-12 arithmetic but not the product algebra theorem. |
| T4 primitive pointed quotient | `PARTIAL` | Independent Thm 3 constructs `(Z/ABZ,[a b^{-1}])` and proves one-mark reconstruction | Same cyclic pointed finite carrier is recovered up to sign convention, but the upstream quotient from the product algebra is not independently proved. |
| T5 exact channel recovery | `EQUIVALENT_REFORMULATION` | `A=gcd(AB,r^2+1)`, `B=gcd(AB,r^2-r+1)` for `r=+a b^{-1}` | Exact sign-conjugate form of source recovery formulas. |
| T6 reciprocal-trace Boolean collapse | `MISSED` | No `T=r+r^{-1}` / idempotent `e` collapse in frozen return | Remains source-package-only evidence. |
| T7 unordered reconstruction from `(H,e)` | `PARTIAL` | Independent Thm 2 gives exact square-gate reconstruction from channel pair; Thm 3 reaches it from `(H,r)` | Square reconstruction theorem is independently recovered, but idempotent input `(H,e)` is not. |
| T8 dual-prime finite-quotient characterization | `PARTIAL` | Independent marked cyclic quotient plus exact coprime channel recovery; simultaneous-prime condition supplied | `Z/ABZ ~= F_A x F_B` is an immediate CRT corollary when both are prime, but the return does not explicitly formulate/prove the source product-algebra quotient characterization. |
| T9 mod-8/mod-12 reciprocity lock | `EXACT_CONVERGENCE` | Independent Thm 7 proves `(P mod 8,Q mod 12) in {(1,1),(5,7)}` and the full Legendre-symbol chain | Same theorem strength, independently organized from square identities and reciprocity. |
| T10 four mixed phases / order-12 orbit | `MISSED` | No four-root `(Z/12Z)^x` phase orbit in frozen return | Remains source-package-only evidence. |
| T11 sixth-power phase-blind channel readout | `MISSED` | No `r^6` channel separation in frozen return | Remains source-package-only evidence. |
| T12 local prime-direction classification | `EXACT_CONVERGENCE` | Independent Thm 5 + Cor. 5.1 classify A/B directions and mod-12 divisor classes, including primes 2 and 3 | Independent version is slightly broader at ramified small primes. |
| T13 fixed-corridor local root count | `EXACT_CONVERGENCE` | Independent Thm 6 and Thm 10 give exact per-channel/survivor slice counts | Equivalent and somewhat more explicit at `l=2,3`. |
| T14 sector-local nearest-neighbor matching | `EXACT_CONVERGENCE` | Independent Thm 8 proves max degree 1 / component size <=2 and sharp examples, including `B=3` exceptions | Same source scope; no seam/globalization. |
| T15 finite-sieve corridor mean preservation | `EXACT_CONVERGENCE` | Independent Thm 9 proves the bijection for every function on `(Z/MZ)^2`; Thm 10 gives exact survivor products | Strict generalization of the finite mean identity; no asymptotic promotion. |

Summary counts:

- `EXACT_CONVERGENCE`: 7 (`T1,T2,T9,T12,T13,T14,T15`);
- `EQUIVALENT_REFORMULATION`: 1 (`T5`);
- `PARTIAL`: 3 (`T4,T7,T8`);
- `MISSED`: 4 (`T3,T6,T10,T11`);
- `COUNTEREXAMPLE`: 0.

Thus `8/15` source theorems have direct exact/equivalent independent convergence, `3/15` have substantial partial convergence, and `4/15` remain source-only at this independent-replication stage.

## 6. New / stronger independent results relative to the packaged T1–T15 statements

The following should be preserved as independent additions, not discarded merely because they are not source-package rows:

1. **Exact image criterion for channel pairs.** Independent Thm 2 gives necessary and sufficient square/parity conditions for an arbitrary integer pair `(X,Y)` to arise from nonnegative coordinates.
2. **Zero-mark insufficiency / one-mark sufficiency in the natural cyclic quotient model.** Independent Thm 3 plus the explicit scalar collision proves the unmarked scalar/cyclic modulus does not globally determine the cell while one distinguished residue class does; no bit-optimality claim is made.
3. **Explicit scalar-collision witness.** The return freezes the exact collision `AB=2,950,935` with two distinct primitive unordered cells.
4. **All-function dimensional-reduction identity.** Independent Thm 9 proves the slice-mean bijection for every function on `(Z/MZ)^2`, making T15 a special case.
5. **Exact local survivor/CRT formulas including prime powers.** Independent Thm 10 gives `S_l`, squarefree product, and the prime-power lifting factor `l^{2(e-1)}`.
6. **Sharpness and small-prime handling for the matching theorem.** Independent Thm 8 explicitly exhibits size-2 components and handles the `B=3` vertices.

These are `NEW_INDEPENDENT_RESULT` or stronger-formulation candidates relative to the theorem-package text. They require normal mathematical review before any package amendment.

## 7. Checker review

The independent checker is structurally distinct from the source-run checker and encodes the independent notation/sign convention. It exercises:

- exact identities, gcd and unordered recovery;
- marked carrier and sign-specific channel polynomials;
- scalar collision search rather than a hard-coded sole witness;
- projective roots and slice counts for all primes through 199;
- reciprocity in a positive box through 350;
- adjacency components through 350;
- finite 2D/slice identities for `M=6,30,210,385`;
- mandatory degeneracy tests.

The return records `ALL CHECKS PASS` on those executed ranges. Driver review treats this as finite audit evidence only; the written algebraic proofs remain primary.

## 8. Effect on PR #597

Independent replication materially strengthens the theorem package, but it does **not** justify the statement that all T1–T15 have independent replication.

Current package evidence typing should be read as:

- independently converged core: T1,T2,T5,T9,T12,T13,T14,T15;
- independently supported but source-specific layer still incomplete: T4,T7,T8;
- source-package-only late fusion/phase layer: T3,T6,T10,T11.

No source theorem was contradicted by the clean run.

PR #597 should remain review-gated until the source-only late fusion/phase cluster receives either:

1. independent targeted theorem verification, or
2. explicit package splitting/evidence typing that does not present those four claims as independently replicated.

Do not merge merely because the blind task itself returned `FULL_STRUCTURAL_REPLICATION`.

## 9. Driver verdict

`PRIME_FUSION_CORE_INDEPENDENTLY_RECONSTRUCTED_OR_REFUTED = ACHIEVED`.

`CLEAN_INDEPENDENT_CORE_REPLICATION = ACHIEVED`.

`PRIME_FUSION_T1_T15_FULL_INDEPENDENT_REPLICATION = NOT ACHIEVED`.

`MATERIAL_COUNTEREXAMPLE_TO_PR597 = NONE FOUND`.

Recommended next evidence action, if this package is to advance as one 15-theorem unit:

`TARGETED_INDEPENDENT_VERIFICATION_OF_T3_T6_T10_T11`.

Alternative:

split the package into an independently replicated arithmetic/core layer and a separately reviewed fusion/phase extension.

No automatic successor research program is authorized by this review.