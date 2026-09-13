# BRC formal algebra / Lean closure — 2026-09-06

Researcher-ID: `EM-BRCWLOG-6F42A1`  
Mode: `TASK_RESEARCH / DIRECT_USER_CONTINUATION`  
Status: `RESEARCH_CANDIDATE / LEAN_WARNING_FATAL_GREEN / NOT_FOUNDATION`

## 1. Scope and authority

This closure formalizes the reusable algebraic layer connecting historical Boolean Branch-Recoalescence Collapse (BRC), framed coordinate summaries, positive multiplicity, exact weight observers, finite CountAtlas normalization, and the derived K4/S4 six-axis atlas.

It enriches the existing Boolean/result-support BRC; it does not replace it and does not infer erased provenance from support. P000 remains unchanged. In particular, no statement here upgrades the derived six-axis atlas to the native Cell-address ontology, a complete native six-dimensional rotation group, or a unique native metric.

## 2. Tool reuse resolution

Current `ENTERPRISE_MATH_TOOL_INVOCATION_POLICY_V2` coverage was checked before extension.

- `T0_BRC`: `REUSE_APPLIED`. The Lean layer reuses the existing typed BRC / observer / `NO_RESURRECTION` semantics rather than creating a new collapse family.
- `T7_FINITE_SYMMETRY_EQUIVARIANCE`: `REUSE_APPLIED`. The concrete S4 action is an instantiation of the existing finite-group action / equivariance method family.
- No new general-purpose tool family is introduced by this closure.

The concrete executable-source alignment is against the frozen derived six-axis package at `research/six-axis-derived-foundation-v1-close-20260905@6d85f1bb53d6750e7085edc42955cf9d63414daa`.

## 3. Framed positive BRC

A framed branch summary is typed by

`(weight, coord, frame, length)`.

For a frame monoid acting additively on coordinates, ordered serial composition is

`(w,n,g,l)(v,m,h,k) = (wv, n + g·m, gh, l+k)`.

Lean proves the monoid laws and lifts this carrier to the positive-multiplicity algebra

`FramedNBRC = MonoidAlgebra ℕ FramedPath`.

For natural multiplicities, Boolean shadow preserves both operations exactly:

- alternative recoalescence -> support union;
- serial convolution -> pointwise support product.

The multiplication statement uses positivity/no cancellation and is intentionally not generalized to signed/amplitude coefficients.

## 4. Observer algebra and information loss

Every multiplicative path observer `FramedPath →* M` lifts canonically to an N-BRC algebra homomorphism. Joint pair observers retain correlation and recover each component.

The negative boundary is formal as well: if a marginal observer merges two path states while another observer distinguishes them, the marginal cannot recover their joint observer. This is a direct `NO_RESURRECTION` consequence and makes observer/provenance loss an algebraic check rather than an informal warning.

## 5. Exact-weight histogram and characters

Exact branch weight is a frame-invariant multiplicative observer. Lean constructs

`FramedNBRC -> MonoidAlgebra ℕ W`

as the exact finite weight histogram. `MonoidAlgebra.lift` then gives the universal multiplicative-character readout.

Formal specializations include:

- exact multiplicity/count character;
- power characters;
- exact power-sum moments;
- zeroth and first moments as multiplicity and total-mass atomic readouts.

These are exact finite positive-weight semantics; they do not silently promote every recurrent/max/CWM observer to the same algebraic type.

## 6. CountAtlas canonical form and common-depth carry

For any finite nonempty axis type `ι`, define the count atlas as `ι → ℕ` and

`commonDepth(n) = min_i n_i`.

Canonical normalization subtracts the common depth coordinatewise. Lean proves:

- some normalized coordinate is zero;
- normalized common depth is zero;
- exact restoration from `(commonDepth n, normalizeAtlas n)`;
- an actual equivalence between arbitrary atlases and `(depth, normalized residue)`;
- normalization idempotence;
- equivariance under axis reindexing;
- common-depth invariance and superadditivity;
- nonnegative common-depth carry;
- exact two-coboundary/cocycle law;
- global frame-relabel invariance.

Thus the common-depth representation is a lossless canonical compression certificate, not only a potential-function heuristic.

## 7. Concrete K4/S4 six-axis instance

The frozen executable source defines four K4 chart vertices, six unordered edges, S4 vertex permutations, edge action, and `rotate_axes`. Lean now instantiates this structurally rather than by a 24×6 table:

- `K4Vertex = Fin 4`;
- `K4Frame = Equiv.Perm K4Vertex`;
- `K4Axis = {s : Finset K4Vertex // s.card = 2}`;
- `Fintype.card K4Axis = 6`;
- `Fintype.card K4Frame = 24`;
- vertex permutations induce a group homomorphism to permutations of K4 edges;
- the induced pullback gives a concrete CountAtlas coordinate action and satisfies `CoordinateReindexing`;
- common depth, canonical normalization, and common-depth carry inherit the generic S4 invariance/nonnegativity laws.

This closes the derived K4-edge label action. It does **not** prove that S4 is the complete native X6 rotation group.

## 8. Exact K4 optimal-extraction closed form

The old K4 atlas compiler used four nonnegative extraction variables and six edge-capacity constraints. Lean now formalizes that integer optimization directly.

For capacities `(AB, AC, AD, BC, BD, CD)`, feasibility is

`a+b≤AB, a+c≤AC, a+d≤AD, b+c≤BC, b+d≤BD, c+d≤CD`.

The objective is `a+b+c+d`. The seven elementary upper bounds are the three opposite-edge pairings and four vertex-star sums. The exceptional pattern is exactly

`n_uv = b_u + b_v + 1`

for four nonnegative vertex bases.

Lean proves:

1. every feasible extraction is bounded by the seven-bound minimum;
2. every feasible extraction can be monotonically shrunk to every smaller integer objective value;
3. each of the four star minima has an explicit integral witness;
4. each opposite-edge matching minimum has an explicit rounded-interval witness unless the capacities themselves yield the exceptional pattern;
5. the other two matching faces follow by K4 vertex relabeling;
6. outside the exceptional pattern the seven-bound minimum is attained;
7. in the exceptional pattern the exact optimum is one less;
8. consequently the executable closed form is exact:

`optimum = min(seven_bounds) - exceptional_bit`.

The exported theorem is `k4ClosedValue_optimal`. A stronger realizability theorem also shows that, in the nonexceptional case, every integer target below all seven bounds is attained.

Finite-box brute checks were used only as sanity checks during proof development; the repository result is the Lean proof, not the enumeration.

## 9. Lean modules

- `EnterpriseMath/Relation/FramedBranchRecoalescence.lean`
- `EnterpriseMath/Relation/BRCPositiveSupport.lean`
- `EnterpriseMath/Relation/BRCFrameSymmetry.lean`
- `EnterpriseMath/Relation/BRCObserverAlgebra.lean`
- `EnterpriseMath/Relation/BRCWeightHistogram.lean`
- `EnterpriseMath/Relation/BRCWeightCharacters.lean`
- `EnterpriseMath/Relation/BRCCountAtlas.lean`
- `EnterpriseMath/Relation/BRCSixAxisS4.lean`
- `EnterpriseMath/Relation/BRCK4OptimalExtractionCore.lean`
- `EnterpriseMath/Relation/BRCK4OptimalExtractionMatching.lean`
- `EnterpriseMath/Relation/BRCK4OptimalExtractionFormula.lean`
- `EnterpriseMath/Relation/BRCK4OptimalExtraction.lean` — stable wrapper/import surface.

## 10. Verification

Verified source head: `e80b45daf91e0e48ff95369953cf5cb02f3035d2`.

GitHub Actions Lean run: `34018354685`; build job: `101446196408`.

The workflow compiled the full umbrella with warnings fatal:

`lake build --wfail -KCI EnterpriseMath`

Result: **success**.

Intermediate failed runs remain provenance; they were used to narrow proof obligations and were not erased or reported as green.

## 11. Frozen boundaries / no-go statements

This closure does not claim:

- native `X6_native` Cell-state/address existence or legality;
- that every `ℕ^6` count vector is a legal native Cell address;
- a complete native six-dimensional rotation group;
- a unique global native metric;
- identification of common-depth carry with the distinct K4 optimal-extraction carry;
- signed/amplitude cancellation semantics;
- recurrent SCC/determinant/Schur-port/root-atom transfer in this Lean layer;
- reconstruction of path/provenance data after an observer has erased it;
- Foundation promotion.

## 12. Next high-leverage frontier

With the finite positive framed/count/S4/K4 layer closed, the next useful formal bridge is the already-motivated finite frame-state lift into ordinary commutative matrix/polynomial semantics, followed by exact determinant/Schur-port identities while retaining frame, grade, endpoint and pole-guard information. Native-X6 or unique-metric questions remain gated on genuinely new native input rather than being inferred from this derived closure.
