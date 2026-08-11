# R022 Eleventh-Pass Deepening — Distinction-Cover Duality for Future Bases and Branch Signatures

**Researcher-ID:** `EM-R022-HC7B4A`  
**Task:** `RS-R022-HASHCLASH-BRC-TOOL-MINING`  
**Taskbook base:** `89fb6c99fa2a00e42f58c1fc11ea016b7421f3be`  
**Owner PR:** `#497`  
**Status:** `ELEVENTH_PASS / RESEARCH ADDENDUM / NOT CANONICAL`

## Executive result

Pass 8 defined the coarsest precision required by a future language. Pass 9 quantified the abstract side information needed to refine an old runtime partition to that target. Pass 11 now separates a third cost:

> how many permitted **probes/features** are needed to *extract or justify* the required distinctions?

For a current equivalence `E` and a target refinement `F`, define the required distinction universe

`P(E,F) = {{x,y} : x E y and not x F y}`.

Two different minimization problems become the same incidence-cover problem on `P(E,F)`:

1. **Future Distinction Basis (FDB):** choose the smallest sublanguage of future programs whose terminal observations separate every pair that the full future language requires separated.
2. **Raw Feature Signature Basis (RFSB):** choose the smallest permitted state features/coordinates whose values separate every required pair.

Both are Set-Cover/Test-Cover-shaped problems over required pair distinctions. In a pair-block construction they realize arbitrary Set Cover exactly.

This explains a repeated R022 phenomenon: an abstract compiled token may require only a few bits while selecting enough permitted raw coordinates or future tests to compute/certify it can be combinatorially larger.

Recommended classification:

`BRC_DISTINCTION_COVER_DUALITY_FOUND / MINIMAL_FUTURE_BASIS_SET_COVER_HARD / MINIMAL_RAW_FEATURE_SIGNATURE_SET_COVER_HARD / INFORMATION_VS_EXTRACTION_COST_SEPARATED / PROOF_CARRYING_DISTINCTION_VERIFIER_FOUND / NOT_CANONICAL`.

---

## 1. Required pair universe

Let `E` be the current runtime equivalence and `F subseteq E` the desired stronger equivalence.

Define unordered required pairs

`P(E,F) = {{x,y} : x E y and not x F y}`.

These are exactly the distinctions absent from the current token but required by the stronger semantics.

Pass 9 measured the maximum number of `F` subclasses inside an `E` class and obtained the minimum arbitrary side-label alphabet. That is an information-cardinality question.

Pass 11 asks instead which available observations/features can witness all pairs in `P(E,F)`.

## 2. Minimal future distinction basis

Let the declared full future language be `U`, with observable `o`, and let

`F = E intersection K(U)`.

For `u in U`, define its distinction set

`D_u = {{x,y} in P(E,F) : o(u(x)) != o(u(y))}`.

Because `F` includes the full future kernel, every pair in `P(E,F)` belongs to at least one `D_u`.

### Future Distinction Basis Theorem

For `W subseteq U`:

`E intersection K(W) = F`

iff

`union_{u in W} D_u = P(E,F)`.

### Proof

Since `W subseteq U`, `K(U) subseteq K(W)`, hence `F subseteq E intersection K(W)`.

Equality fails exactly when some pair in the same `E` class that full `U` separates remains unseparated by every future in `W`. That is exactly an uncovered element of `P(E,F)`.

Therefore minimum-cardinality sublanguage preserving the same required precision is exactly minimum set cover on the distinction columns `{D_u}`.

The entire Galois closure `Safe_o(K(U))` is unchanged by replacing `U` with any exact FDB, because it depends only on the resulting kernel.

## 3. Minimal raw feature signature basis

Suppose permitted extractor features are

`a_j : X -> Z_j`.

For each feature define

`D_j = {{x,y} in P(E,F) : a_j(x) != a_j(y)}`.

For selected coordinates `J`, let

`s_J(x)=(a_j(x))_{j in J}`.

### Raw Feature Correctness Theorem

The combined encoding `(E-token,s_J)` never merges any pair that target `F` requires separated iff

`union_{j in J} D_j = P(E,F)`.

Thus minimum correct raw-coordinate signature is also a Set-Cover instance on required pairs.

If every selected feature is constant on each `F` class, the resulting equivalence equals `F`. Without that compatibility condition, the raw signature may over-refine `F` while remaining semantically exact.

This formalizes the representation-class warning from md5collgen: minimum raw coordinates and minimum arbitrary compiled label are different optimization problems.

## 4. Exact arbitrary Set-Cover realization

For any set-cover instance with universe elements `1,...,m`, construct `m` independent coarse pair cells

`C_i={p_i,q_i}`.

Let target `F` split each pair.

For every input set `S_j`, define either:

- a future test whose observable separates `p_i,q_i` exactly when `i in S_j`; or
- a binary raw feature that differs on `p_i,q_i` exactly when `i in S_j`.

Other coarse classes can be singleton/fixed context so cross-cell distinctions are irrelevant.

Then selecting futures/features that realize the target refinement is literally selecting sets that cover all universe elements.

Therefore both minimum FDB and minimum raw-feature signature are NP-hard in the general explicit finite model.

This is close to classical Test Cover / discernibility/reduct problems; R022 does not claim generic novelty for the covering hardness.

## 5. Exhaustive finite evidence

Artifact:

`experiments/r022_distinction_cover_duality.py`.

For a four-pair required-distinction universe, all `15` nonempty subset columns exist. R022 enumerated all

`2^15 - 1 = 32,767`

nonempty column families.

Of these, `32,297` cover all four required pairs. For every coverable family:

`minimum Set Cover width = minimum future-basis width = minimum raw-feature-basis width`.

Mismatches: **0**.

Optimum-width distribution among coverable families:

- width 1: `16,384`;
- width 2: `15,696`;
- width 3: `216`;
- width 4: `1`.

Focused pass-11 tests: **4/4 PASS** in the research execution environment.

## 6. Information debt is not extraction complexity

The pair-block construction gives a sharp separation.

Each old coarse class contains only two target subclasses. Therefore pass-9 future precision debt says a shared side alphabet of cardinality 2, i.e. **one abstract bit**, is enough to name the new subclass locally inside every old class.

But if the available future/feature columns are the four singleton masks, all four probes/features are required to distinguish all four pair cells.

Hence:

`minimum abstract side bits = 1`

while

`minimum permitted probe/feature count = 4`.

There is no contradiction. The first assumes an arbitrary ideal side encoder; the second charges the restricted mechanism available to compute/witness that encoder.

This is the same structural distinction seen in md5collgen:

- 9 raw route-relevant coordinate bits are all necessary in the raw-coordinate subset class;
- 5 route labels require only 3 fixed-width bits once the routing function has already been computed.

So BRC resource accounting should distinguish **information width** from **extractor/probe complexity**.

## 7. Semantic and representation covering are dual

Pass 7 produced a canonical **output-side frontier**:

- semantic atoms/frontier facts must be covered by executable branch macros.

Pass 11 produces an **input-side distinction universe**:

- required state-pair distinctions must be covered by future tests or extractor features.

The BRC compiler therefore has two covering planes:

`input distinctions <- probes/features`

and

`output semantic frontier <- executable macros`.

Both may be Set-Cover hard, but they optimize different objects and cannot be merged into one width statistic.

## 8. Proof-carrying basis selection

As with pass 5, semantic safety need not trust the optimizer.

### Future basis verifier

Given a proposed `W subseteq U`, verify either:

- `E intersection K(W) = E intersection K(U)` directly; or
- every pair in `P(E,F)` is covered by some `D_u`, `u in W`.

### Feature basis verifier

Verify every required pair is separated by at least one selected feature.

Thus a heuristic/greedy basis proposer may be suboptimal while a small exact verifier preserves correctness.

## 9. New resource quantities

R021/R014 should distinguish:

- `required_distinction_pairs`;
- `future_probe_basis_size/cost`;
- `raw_feature_basis_size/cost`;
- `abstract_side_alphabet/bits` from pass 9;
- `extractor_compute_cost`;
- `feature/probe incidence density`;
- `basis_optimality_status`;
- `distinction_verifier_cost`.

A small abstract token is not cheap if computing it requires many expensive probes/features.

## 10. Prior-art/rooting boundary

Minimum Test Cover asks for a minimum test subcollection separating required item pairs; related discernibility/reduct formulations likewise select attributes that preserve distinctions. Set Cover/hitting-set reductions are standard.

The Enterprise Math residue is the alignment of these ideas with BRC's future-kernel calculus and precision debt:

`future language -> required pair distinctions -> future probe basis / feature extractor basis -> abstract side-information lower bound -> executable carrier`.

## 11. R021 feedback

Recommended additions:

1. Introduce `P(E,F)` as the required distinction universe for on-demand refinement.
2. Define Future Distinction Basis and Raw Feature Signature Basis as pair-cover problems.
3. State their exact cover equivalences and general Set-Cover hardness.
4. Distinguish minimum side-label information from minimum probe/feature extraction complexity.
5. Interpret md5collgen's 9 raw bits vs 3-bit compiled route label through this representation-class separation.
6. Add proof-carrying basis verification rather than trusting minimum-basis solvers.
7. Keep input-side distinction cover separate from pass-7 output-side semantic-frontier macro cover.

No correction is requested to R023. This pass sharpens the compiler/extractor layer around its future-equivalence semantics.

## 12. Eleventh-pass classification

`BRC_DISTINCTION_COVER_DUALITY_FOUND / FUTURE_BASIS_AND_RAW_SIGNATURE_COVER_CLASSIFIED / GENERAL_MINIMUM_BASIS_HARD / INFORMATION_VS_EXTRACTION_COST_SEPARATED / INPUT_OUTPUT_DUAL_COVERING_PLANES_FOUND / R021_FEEDBACK_READY / NOT_CANONICAL`.
