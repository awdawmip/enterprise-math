# Research Return — P000 S4 relational-minimality grammar V15

Task: `RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE`  
Publication: `TP2-3E7A91C5B2406DF814A2`  
Researcher: `EM-P000FCC15-7556C9`  
Claim: `chatgpt-p000fcc15-20260830-1615-11d852`  
Execution: `ER-2460EC8DF672EF785811`  
Result: `RR-9EBCAF7C1C66D8643C35`  
Status: `SUCCESS / RELATIONAL_MINIMALITY_GRAMMAR_EQUIVALENCE_COST_AND_ENVELOPE_FROZEN`

## 0. Terminal theorem

Generation 15 closes its required hard target:

`P000_S4_RELATIONAL_MINIMALITY_GRAMMAR_EQUIVALENCE_COST_AND_PARETO_ENVELOPE_EXACTLY_FROZEN`.

Accepted terminal class returned by this execution:

`RELATIONAL_MINIMALITY_GRAMMAR_EQUIVALENCE_COST_AND_ENVELOPE_FROZEN`.

This execution does **not** claim the optional second target
`P000_PARETO_MINIMAL_FAITHFUL_OR_CANONICAL_S4_PACKAGES_CLASSIFIED_WITHIN_FROZEN_GRAMMAR`.
The taskbook explicitly places that classification after A–G.  The present result makes that later question mathematically well-posed for the first time; it does not invent a premature positive package theorem.

Gen14 exact algebra is consumed as regression and not redone:

\[
Sec(q)\cong Z(q),\qquad
\text{canonical}\iff Sec(q)^{Aut_{prim}(M)}\neq\varnothing.
\]

## A. Zero-cost background is now explicit

The minimization universe is the declared framed/PF-10 downstream model class, never bare P000.

Zero-cost background:

1. `NativeCell` is an opaque sort.
2. `AxisType={E1,...,E6}` is the accepted six-axis sort.
3. `NativeAdj` is already a relation symbol in the accepted framed Full-Cell model language.  Its **valuation is not fixed**: Gen12/13 use `K4`, `P4`, and `K_{2,2,2,2}` valuations.  Therefore a new duplicate Cell–Cell adjacency symbol is excluded from the candidate catalog.
4. When the framed model is declared, `f_x:A->C_x` and the PF-10 `I/O/M` tensor are zero-cost accepted structure.
5. `T_xy=f_y o f_x^-1` is zero-cost frame-derived transport.  An independent connection is zero-cost only in models that declare it.
6. `J_A` is independently established at its accepted strength; `J_B,J_C,J_D` remain downstream derived star data.  They are not promoted to new root primitives.
7. Gen12 star-overlap/gluing data and connection naturality are retained as derived/background laws at their accepted scope.  They are **not duplicated as new candidate predicates**, because doing so would recreate the presentation-dependence defect that Gen15 is meant to remove.

Sources consumed:

- `projects/enterprise-math/P000_REALITY_FOUNDATION.json`;
- `projects/enterprise-math/00_CURRENT_FOUNDATION.md`;
- `projects/enterprise-math/P000_NATIVE_FCC_STRICT_BRIDGE.json`;
- Gen13 Driver review;
- Gen14 Return + Driver review;
- exact Gen15 taskbook.

Frozen boundaries remain unchanged:

`BARE_P000_UNIVERSAL_S4_LIFT_DERIVABLE = FALSE`.

`BARE_P000_CANONICAL_S4_SECTION_DERIVABLE = FALSE`.

`CARRIER_S4 != COMPLETE_NATIVE_P000_ROTATION_GROUP`.

`NO_KERNEL_QUOTIENT`.

`TIME_FIXED`.

## B. Finite candidate relation grammar `G15`

No arbitrary predicate family is allowed.  The entire new-symbol catalog is:

| symbol | signature | arity | role |
|---|---|---:|---|
| `I_CA` | `NativeCell × AxisType` | 2 | intrinsic Cell–Axis incidence |
| `I_HC` | `Hidden × NativeCell` | 2 | hidden-state / Cell incidence |
| `I_HA` | `Hidden × AxisType` | 2 | hidden-state / axis incidence |
| `ADD_H` | `Hidden³` | 3 | parameter-free hidden relational rigidity |

`Hidden` is the only optional new sort and exists iff a selected package uses a hidden relation.

Every enriched automorphism must preserve each selected relation setwise and preserve all background structure.  None of the four relation forms mentions `q`, `Sec(q)`, generator lifts, residues, `R_a`, `R_b`, `K=1`, or a carrier/native identity equation.

The finite global-constraint catalog is:

1. `K4_ADJ`: `|NativeCell|=4` and the **background** `NativeAdj` valuation is complete.
2. `TETRA_CA`: with `I_CA`, `|C|=4`, `|A|=6`, every axis is incident with exactly two distinct Cells and every unordered Cell pair has exactly one axis.
3. `H_C3X3`: with `ADD_H`, the hidden relation is the additive group `C3×C3` of order 9.
4. `PROJECTIVE_HC`: with `ADD_H,I_HC,H_C3X3`, the four Cells are exactly the four 1-dimensional subgroups, represented by incidence with their two nonzero vectors.
5. `PAIR_AXIS_HA`: with `ADD_H,I_HC,I_HA,H_C3X3,PROJECTIVE_HC`, the six axis objects are intrinsically tied to the six unordered pairs of projective Cell lines.

These five templates are intrinsic finite-structure statements.  None refers to a desired `S4` section.

### Independent-meaning test

A new relation form is admissible only if all four conditions hold:

1. its vocabulary does not mention the target section/generator/residue predicates;
2. its sorts, arity and automorphism preservation law are intrinsic;
3. it is not already parameter-free definable from the zero-cost background reduct; otherwise it is deleted as redundant;
4. it introduces no named point/constant.  Any distinguished feature must be internally parameter-free definable.

For `ADD_H`, for example, the additive identity is the unique internally definable identity element; it is not a named constant.

## C. Parameter / tautology firewall

Frozen:

`NO_NEW_DISTINGUISHED_CONSTANTS = TRUE`.

Forbidden as candidate primitives:

- `there exists a section`;
- `R_a`, `R_b`;
- `K=1`;
- a chosen lift pair;
- a residue-zero flag whose meaning is “the desired section exists”;
- carrier/native identity equations;
- pointwise names for Cells or hidden vectors.

This converts Gen14's informal phrase “independently meaningful” into the explicit admissibility test above.

## D. Definitional equivalence is fixed — and the Gen14 ambiguity is resolved

Two packages are in the same `G15` definitional class iff, **on the fixed background sorts**, they are mutually definable by parameter-free first-order formulas over the same background reduct.

No new quotient, parameter, or derived sort is allowed in this equivalence relation.

Bi-interpretability after creating a new sort is recorded separately and does **not** collapse fixed-sort classes.

### D1. Tetrahedral incidence defines K4 adjacency

From `I_CA` satisfying `TETRA_CA`,

\[
Adj(c,d)\;\Longleftrightarrow\;
c\neq d\;\wedge\;\exists e\,
[I_{CA}(c,e)\wedge I_{CA}(d,e)].
\]

The deterministic checker reconstructs all six Cell pairs, hence the induced Cell graph is exactly `K4`.

### D2. K4 adjacency does not define tetrahedral incidence on the preexisting AxisType sort

This is an exact symmetry obstruction.

In the Gen14 `K4` reduct, `Aut(K4)=S4`, order 24.  Even if all six preexisting `AxisType` objects are held pointwise fixed, a nontrivial Cell permutation moves every candidate 2-Cell incidence fiber.  A parameter-free definable `Cell×AxisType` relation would have to be invariant under every automorphism of that reduct.  Tetrahedral incidence is not.

Therefore

\[
K4\text{ adjacency}\not\Rightarrow_{def} I_{CA}
\]

on the fixed `NativeCell,AxisType` sorts.

### D3. Exact classification of the Gen14 pair

`K4` Cell adjacency and tetrahedral Cell–Axis incidence are:

`STRICTLY_DIFFERENT_FIXED_SORT_DEFINITIONAL_CLASSES`.

They become bi-interpretable only after replacing/adding the derived sort

\[
AxisPair=[NativeCell]^2,
\]

with incidence given by membership.

That derived-sort move has nonzero sort cost and is therefore **not** silently free in Gen15.

This is the central specification repair: “one relation” in two different primitive universes is no longer treated as invariantly the same minimum.

## E. Package cost / Pareto order is frozen

For any valid package `P`, define

\[
c(P)=(
s,r,a_1,a_2,a_3,h,g,p
)
\]

with:

- `s`: new-sort count;
- `r`: new relation-symbol count;
- `a_k`: number of new `k`-ary relation symbols;
- `h`: hidden-sort flag;
- `g`: number of extra global constraints;
- `p`: number of distinguished parameters/constants.

In Gen15, `p=0` identically.

Comparison is **strict componentwise Pareto dominance plus exact equality**:

- `P <= Q` if `P=Q`; or
- every coordinate of `c(P)` is at most the corresponding coordinate of `c(Q)` and the vectors are not equal.

Distinct packages with equal cost vectors are deliberately incomparable; no lexical or “naturalness” tie-break is introduced.

Before any future frontier computation, fixed-sort mutually definable packages are first quotiented by the D-policy above.

The checker exhaustively verifies reflexivity, antisymmetry and transitivity on the full valid Gen15 package-feature universe.

## F. Finite search / regression envelope is frozen

Bounds:

- `|NativeCell| <= 8`;
- `|AxisType| = 6`;
- `|Hidden| <= 9`.

Finite grammar size:

- 4 candidate relation symbols;
- 5 global-constraint templates;
- 16 raw relation subsets;
- 32 raw constraint subsets;
- exactly **90 dependency-closed valid package specifications**.

The 90 package-feature specifications are exhaustively enumerable.

This is **not** a claim that all relation valuations on all finite models were exhaustively enumerated.  Gen15 cleanly separates:

1. exhaustive package-subset enumeration;
2. structural theorem/countermodel analysis inside a package;
3. targeted exact finite witness regressions.

All mandatory witnesses fit the envelope:

| witness | Cells | Axis | Hidden | exact regression |
|---|---:|---:|---:|---|
| Gen12 `K=1` canonical | 4 | 6 | 0 | faithful/canonical |
| Gen13 `P4` | 4 | 6 | 0 | `Aut=2`, no lift |
| Gen13 `K_{2,2,2,2}` | 8 | 6 | 0 | `Aut=384`, 16 sections, no kernel-fixed section |
| Gen13 `GL(2,3)` | 4 | 6 | 9 | order 48 -> projective image 24, kernel 2, nonsplit |
| Gen14 `K4` | 4 | 6 | 0 | `Aut=24` |
| Gen14 tetra incidence | 4 | 6 | 0 | sort-preserving `Aut=24` |

## G. Expressivity gate — PASS in all four regimes

The frozen grammar/background envelope distinguishes every required regime before minimization:

### 1. `NO_LIFT`

`P4` Native adjacency:

`|Aut(P4)|=2`.

It cannot contain the frozen `S4` action.

### 2. `SURJECTIVE_NONSPLIT`

Use `Hidden=F_3^2` with `ADD_H`, plus projective Cell incidence.

Exact checker:

`|GL(2,3)|=48`.

Projective image order:

`|PGL(2,3)|=24 ~= S4`.

Kernel:

`{I,-I}`.

For the two lifts of frozen `a` and two lifts of frozen `b`, every one of the four lift pairs has

\[
(AB)^4=-I.
\]

Hence the readout is surjective and nonsplit.

### 3. `SPLIT_NONCANONICAL`

`K_{2,2,2,2}`:

\[
Aut = C_2^4\rtimes S_4=C_2\wr S_4,
\quad |Aut|=384.
\]

The checker independently recovers:

- 16 relation-residue triples;
- 16 homomorphic sections;
- two kernel-conjugacy orbits of size 8;
- zero sections fixed by the whole kernel-conjugation action.

Thus split does not imply canonical.

### 4. `CANONICAL_FAITHFUL`

Both accepted positive regressions fit:

- `K4`: automorphism order 24;
- tetrahedral Cell–Axis incidence: sort-preserving automorphism order 24.

The tetra incidence additionally binds the preexisting six-axis sort; the K4 reduct alone does not.

Therefore the Gen15 expressivity gate is fully open.

## H. Why the optional Pareto theorem is not asserted here

A–G are now exact and checker-backed.  That is the Gen15 hard target.

The optional H-stage requires a **universal sufficiency/necessity classification of positive packages inside this newly frozen grammar**, including one-condition deletion countermodels.  No such theorem is smuggled into this return merely because the grammar now exists.

The correct post-result continuation, if Driver wants the same task to proceed beyond this valid terminal class, is to enumerate the 90 dependency-closed package specifications modulo the fixed-sort definitional quotient, then test universal faithful/canonical sufficiency and deletion countermodels.  The present result is the prerequisite specification theorem for that work.

## Deterministic verification

Checker:

`research_checks/P000_S4_RELATIONAL_MINIMALITY_GRAMMAR_V15_CHECK_20260830.py`

Artifact:

`research_artifacts/P000_S4_RELATIONAL_MINIMALITY_GRAMMAR_V15/GRAMMAR_CERTIFICATE.json`

Observed exact output:

- `PASS`;
- 4 relations;
- 5 constraints;
- 90 valid packages;
- 45 top-level certificate checks;
- `K4` / tetra fixed-sort classification:
  `TETRA_CA -> K4_ADJ; K4_ADJ -/-> TETRA_CA`;
- all four expressivity regimes PASS.

## Tool reuse

`REUSE_APPLIED: T7_FINITE_SYMMETRY_EQUIVARIANCE`.

The accepted finite symmetry/orbit/fixed-point machinery is the matching project tool family.  The task-local checker instantiates exact finite permutation, orbit and fixed-point certificates; no new general tool family is claimed.

## Terminal disposition

`SUCCESS`.

Hard-target disposition:

`P000_S4_RELATIONAL_MINIMALITY_GRAMMAR_EQUIVALENCE_COST_AND_PARETO_ENVELOPE_EXACTLY_FROZEN`.

Terminal class:

`RELATIONAL_MINIMALITY_GRAMMAR_EQUIVALENCE_COST_AND_ENVELOPE_FROZEN`.

No P000 mutation.  No kernel quotient.  No native/carrier identity collapse.  No target section or generator lift was introduced as a primitive.
