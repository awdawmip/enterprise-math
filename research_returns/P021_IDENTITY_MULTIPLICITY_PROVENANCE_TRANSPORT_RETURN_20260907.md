# P021 Identity-Sensitive Multiplicity / Provenance Transport

Status: `RESEARCH RETURN / P021-LOCAL FINITE-HORIZON EXACT CONTINUATION / AWAITING DRIVER REVIEW`  
Task: `RS-P021-FOCUSING-DIRECTION`  
Publication: `TP2-B1E5DDBA1F327733882C`  
Researcher-ID: `EM-P021-8F31C2`  
Claim: `chatgpt-p021-20260907-1018-8f31c2`  
Execution branch: `research/p021-identity-multiplicity-provenance-em-p021-8f31c2`  
Execution base: `d83b89b8ce1c2418a804064c034f6c51abffa8ad`  
Owner: `program/p021-causal-focusing-v3`

## 1. Executive verdict

The previous P021 result closed the finite-horizon **endpoint identity** question: after normalizing every one-step unique matching, the endpoint identity remains unique exactly when all noncanonical step edges admit one common topological order.

This continuation studies the strictly stronger observable explicitly left open there: **identity-sensitive path multiplicity and class-level provenance inside the common-order-safe regime**.

The main conclusion is:

> Common-order safety is enough to preserve the unique endpoint identity, but it is not enough to preserve multiplicity or provenance under Boolean support collapse.

There is nevertheless a sharp exact structure.

After choosing one common topological order and relabeling it as `1<...<n`, let `A_r` be the normalized `0/1` support at step `r`; every `A_r` is upper triangular and contains the diagonal. Define the ordinary integer product

`N_h = A_1 A_2 ... A_h`.

Then `N_h(i,j)` is exactly the number of class-level time-respecting direction chains from `i` to `j`, while the old Boolean endpoint support is

`B_h = supp(N_h)`.

For rank distance `d=j-i>=0`,

`N_h(i,j) <= binom(h+d-1,d)`,

and the bound is sharp: equality is attained simultaneously for all `i<=j` by taking every step equal to the full upper-triangular zeta support `Z_n(i,j)=1 iff i<=j`.

Thus for fixed `n` the largest class-level multiplicity in a common-order-safe horizon is at most

`binom(h+n-2,n-1)`,

a polynomial of degree `n-1` in `h`. This does **not** produce an infinite-scale or physical focusing theorem.

The exact information erased by Boolean support is the nonnegative matrix

`D_h = N_h - B_h`.

It satisfies an exact recurrence separating inherited multiplicity from new recoalescence collisions:

`D_{r+1} = D_r A_{r+1} + K_{r+1}`

with

`K_{r+1} = B_r A_{r+1} - supp(B_r A_{r+1})`.

Because every `A_r` contains the diagonal, once an entry of `D_r` becomes positive it cannot disappear at later horizons.

Terminal class:

`P021_COMMON_ORDER_MULTIPLICITY_PROVENANCE_SHARP_BOUND_AND_DEFECT_RECURRENCE_EXACT`.

## 2. Frozen predecessor and non-replay boundary

The durable predecessor is:

`research/p021-multistep-unique-matching-em-p021-4b8e2d@f1aceb2168650248601765dfba410dc45c3215f6`

with return:

`research_returns/P021_MULTISTEP_DIRECTION_IDENTITY_WITNESS_JOIN_RETURN_20260901.md`.

That result is consumed, not restarted. In particular this continuation assumes its normalized common-order theorem:

- every step has a forced normalized diagonal matching;
- one common topological order of all noncanonical support edges is exactly the finite-horizon class-level identity-safety certificate.

The present result does not re-prove matching uniqueness, alternating-cycle theory, or the prior fine-witness safety theorem.

## 3. Declared BRC carrier / observer / future operations

The BRC audit is load-bearing here.

Population:
- all finite class-level time-respecting paths through the declared normalized supports `A_1,...,A_h`.

Branch identity / provenance:
- a branch is the full ordered class sequence
  `(x_0,...,x_h)` with `A_r(x_{r-1},x_r)=1`.

Serial composition:
- append one legal step.

Alternative composition / recoalescence:
- distinct paths with the same endpoint pair `(i,j)` remain distinct branches before observation.

Exact positive weight:
- every class path has weight `1`.

Declared endpoint observations:
1. full labeled class-path provenance `Pi_h(i,j)`;
2. multiplicity `N_h(i,j)=|Pi_h(i,j)|`;
3. Boolean support `B_h(i,j)=1[N_h(i,j)>0]`.

Allowed future operation in this task:
- append further normalized class-support steps and ask for endpoint class support or endpoint class-path multiplicity.

Not included:
- fine witness-token multiplicity below a class edge;
- signed/amplitude cancellation;
- physical focusing, curvature or GR semantics.

### Tool-reuse resolution

`T0_BRC`: `REUSE_APPLIED`.

The exact current Weighted-BRC laws are used with unit path weights:
- serial propagation multiplies `(C,W,M_max)`;
- alternative recoalescence adds counts and total positive mass;
- Boolean support forgets the positive multiplicity state.

At a reachable endpoint pair the resulting CWM state is exactly

`(C,W,M_max) = (N_h(i,j), N_h(i,j), 1)`.

Hence the BRC effective multiplicity is `N_h(i,j)`, while Boolean support retains only whether this state is live. The BRC hard boundary “do not infer erased provenance from Boolean support” is therefore active, not merely cited.

`T8_RELATION_OBSERVABLE_SPECTRUM`: `REUSE_APPLIED`.

The existing relation-observable composition layer supplies the set/support-valued terminal semantics and its hidden-branch warning. This continuation does not replace it; it lifts the declared observable from endpoint support to integer multiplicity / labeled class-path provenance.

No new general Toolbox family is proposed. The matrix/defect formulas below are P021-local consequences of the existing BRC and relation-composition carriers.

## 4. P021-MP-T01 — Exact class-path provenance lift

For `h>=1`, define

`Pi_h(i,j) = { (x_0,...,x_h) : x_0=i, x_h=j, A_r(x_{r-1},x_r)=1 for all r }`.

### Theorem

`N_h(i,j) := |Pi_h(i,j)|`

is exactly the `(i,j)` entry of the ordinary integer matrix product

`A_1 A_2 ... A_h`.

Moreover,

`B_h(i,j) = 1[N_h(i,j)>0]`

is exactly the Boolean/relational product used in the predecessor P021 theorem.

### Proof

For `h=1`, the statement is the definition of the `0/1` support.

Inductively, every path ending at `k` at time `r+1` has a unique penultimate class `j`; therefore the provenance family is the disjoint union

`Pi_{r+1}(i,k) = disjoint_union_j ( Pi_r(i,j) × {(r+1,j,k)} )`

over `j` with `A_{r+1}(j,k)=1`.

Taking cardinalities gives

`N_{r+1}(i,k) = sum_j N_r(i,j) A_{r+1}(j,k)`,

which is ordinary matrix multiplication. Taking nonemptiness instead of cardinality gives Boolean relation composition. QED.

This identifies the exact quotient chain

`labeled class provenance -> integer multiplicity -> Boolean support`.

Neither arrow is reversible in general.

## 5. P021-MP-T02 — Sharp common-order multiplicity bound

Choose the common topological order promised by the frozen predecessor theorem and relabel it as

`1<2<...<n`.

Then each `A_r` is upper triangular and contains the diagonal.

### Theorem

For every endpoint pair `i<=j`, put `d=j-i`. Then

`N_h(i,j) <= binom(h+d-1,d)`.

For `i>j`, `N_h(i,j)=0`.

The bound is sharp simultaneously for every pair and every horizon: let

`Z_n(i,j)=1 iff i<=j`.

If `A_1=...=A_h=Z_n`, then

`(Z_n^h)(i,j) = binom(h+j-i-1,j-i)`.

### Proof

Along any common-order-safe path, the rank never decreases. For a path from `i` to `j`, define its rank increments

`a_r = x_r - x_{r-1} >= 0`.

They satisfy

`a_1+...+a_h = d`.

The starting rank plus the increment vector uniquely determines the whole class sequence, so the map from legal paths to weak compositions of `d` into `h` parts is injective. The number of such compositions is

`binom(h+d-1,d)`.

For the full upper-triangular support `Z_n`, every weak composition is legal, so the injection is a bijection and equality holds. QED.

### Consequence

At fixed `n`,

`max_{i,j} N_h(i,j) <= binom(h+n-2,n-1)`.

Thus common-order-safe multiplicity may grow without bound in horizon, but only polynomially at fixed direction-class count. No uniform-in-`n` or infinite-state conclusion is asserted.

## 6. P021-MP-T03 — Exact Boolean multiplicity-defect recurrence

Define

`B_r = supp(N_r)`

entrywise, with `N_0=B_0=I`, and define the Boolean-collapse defect

`D_r = N_r - B_r`.

For the next step, form the ordinary integer join count of currently supported endpoints:

`J_{r+1} = B_r A_{r+1}`,

and its newly created collision surplus

`K_{r+1} = J_{r+1} - supp(J_{r+1})`.

Every entry of `K_{r+1}` is nonnegative.

### Theorem

`D_{r+1} = D_r A_{r+1} + K_{r+1}`.

### Proof

Since `N_r=B_r+D_r`,

`N_{r+1} = N_r A_{r+1}`
`          = B_r A_{r+1} + D_r A_{r+1}`.

Because `N_r` and `B_r` have the same support, multiplying by the same nonnegative `0/1` matrix creates the same next support:

`supp(N_r A_{r+1}) = supp(B_r A_{r+1}) = B_{r+1}`.

Subtract `B_{r+1}` and use the definition of `K_{r+1}`. QED.

### Interpretation

- `D_r A_{r+1}` transports already-existing alternative provenance chains;
- `K_{r+1}` counts genuinely new recoalescence collisions created when distinct supported prefix endpoints feed the same next endpoint;
- Boolean support records neither source.

This is the exact P021/BRC repair coordinate for the declared multiplicity observer.

## 7. P021-MP-T04 — Lossless criterion and first-loss semantics

Since

`D_h(i,j)=N_h(i,j)-1`

for reachable endpoint pairs and `0` otherwise,

`D_h=0`

if and only if every reachable endpoint pair has exactly one class-level time-respecting path.

Equivalently, in the layered temporal graph with vertices `(r,i)` and edges

`(r-1,i) -> (r,j)` whenever `A_r(i,j)=1`,

there is at most one directed path from every layer-0 source to every layer-`h` target.

For all prefixes, the recurrence gives the more operational criterion:

`D_r=0 for every r<=h`

if and only if

`K_r=0 for every r<=h`.

Because every step contains the diagonal,

`(D_r A_{r+1})(i,j) >= D_r(i,j)`,

so multiplicity information once lost by Boolean collapse cannot spontaneously reappear at a later horizon.

Therefore

`FIRST_MULTIPLICITY_LOSS = FIRST_PREFIX_WITH_K_r != 0`.

This is a class-path provenance statement, not physical focusing.

## 8. P021-MP-C01 — Minimal common-order-safe information-loss family

Take two normalized direction classes and repeat

`U = [[1,1],`
`     [0,1]]`.

Every horizon is common-order safe; the Boolean product is always

`B_h = U`

for `h>=1`, so the endpoint diagonal identity remains unique forever.

But ordinary integer multiplication gives

`N_h = U^h = [[1,h],`
`               [0,1]]`.

Hence from direction class `1` to class `2` there are exactly `h` class-level paths, while Boolean support stores only one reachable bit. The erased multiplicity is

`D_h(1,2)=h-1`.

At `h=2` this is already strict:

`N_2(1,2)=2`, but `B_2(1,2)=1`.

This is minimal:
- with `n=1` no distinct endpoint branch exists;
- with `h=1` every `0/1` one-step support has multiplicity equal to Boolean support.

Thus the smallest identity-safe multiplicity/provenance failure is exactly `n=2,h=2`.

## 9. P021-MP-C02 — Sharp full-zeta family

For the full upper-triangular support `Z_n`, every path is a weakly nondecreasing rank sequence.

The exact formula

`(Z_n^h)(i,j)=binom(h+j-i-1,j-i)`

shows that the bound of Section 5 is not merely asymptotic or coarse.

For example, with `n=3` and horizon `h=3`,

`N_3(1,3)=binom(4,2)=6`

while the Boolean endpoint support still contains only the single bit `1`.

This family exposes the hierarchy:

`unique endpoint identity`
does not imply
`unique endpoint class path`
does not imply
`recoverable labeled provenance from Boolean support`.

## 10. Fine-witness boundary

The predecessor P021 result distinguished class-level support from exact fine witness joins. That boundary remains frozen.

`N_h(i,j)` counts **class-level sequences allowed by the normalized support envelope**. It does not count hidden fine witness-token realizations of those class edges.

Two fine realizations with the same class supports can still have different exact joined witness sets. Therefore:

`CLASS_PATH_MULTIPLICITY != FINE_WITNESS_MULTIPLICITY`

unless a separate theorem supplies a fiberwise bridge.

The saturated fine realization from the predecessor can realize all class paths, but that is an existence construction, not a universal equality for arbitrary refinements.

Accordingly this return does not infer count-composition completeness from the class matrices.

## 11. Deterministic verification

Checker:

`scripts/check_p021_identity_multiplicity_provenance_transport.py`

Exact locally executed source before persistence:

`sha256:e837c70e0889e210158433265befdf7711c991e372dc591facf0278d1fc4b6f8`

Result:

`PASS`.

The checker verifies:

1. `supp(integer product) = Boolean composition`;
2. the exact recurrence
   `D_{r+1}=D_r A_{r+1}+K_{r+1}`;
3. nonnegativity of all defects;
4. the sharp binomial bound for every sequence of common-order upper-triangular supports through `n<=3,h<=3`;
5. the full-zeta equality through `n<=6,h<=8`;
6. the repeated two-label family through `h<=8`;
7. `D_h=0` iff every endpoint count is at most one.

Exhaustive sequence counts include:
- `n=2,h=3`: 8 step sequences;
- `n=3,h=2`: 64 step sequences;
- `n=3,h=3`: 512 step sequences.

At `n=3,h=3`, the maximum endpoint multiplicity observed is `6`, exactly the sharp bound `binom(4,2)`.

The finite run is regression/certificate evidence; Sections 4–7 are symbolic proofs for arbitrary finite `n,h` within the declared common-order regime.

## 12. Ownership / novelty / tool boundary

Generic ingredients are not claimed as novel:
- integer matrix path counting;
- Boolean support of a nonnegative matrix product;
- weak compositions / stars-and-bars;
- upper-triangular matrix powers;
- layered DAG path counting.

Existing Enterprise machinery is reused rather than renamed:
- BRC owns the typed distinction between Boolean support, multiplicity/mass and provenance;
- relation-observable composition owns the support/set-valued composition boundary.

The P021-local residue is the exact combination:

1. transport the already-frozen direction identity into its common-order labels;
2. lift the endpoint observable from unique identity to class-path multiplicity/provenance;
3. prove the sharp `binom(h+d-1,d)` multiplicity ceiling and its saturating family;
4. isolate the exact Boolean-collapse defect recurrence and first-loss coordinate;
5. preserve the class-vs-fine-witness boundary.

No new top-level tool family is requested. Method-harvest recommendation: `RESULT_ONLY / DOMAIN_OPERATOR_AT_MOST`.

## 13. Frozen nonclaims

This return does **not** prove or claim:

- physical focusing, caustics, curvature, gravity, or a GR model;
- that path multiplicity is a physical probability or amplitude;
- that class-level counts determine fine-witness counts;
- that Boolean support is count-composition complete;
- a uniform infinite-horizon bound independent of `h`;
- a uniform bound independent of the number of direction classes `n`;
- a new generic matrix/path-counting theorem;
- Working Truth, Foundation or canonical status before Driver review.

P000 remains assumed; the three-axis constructions remain research-slice mathematics under the 6D spatial ontology.

## 14. Driver recommendation

Driver review should audit:

1. the exact BRC carrier declaration and the quotient chain
   `provenance -> multiplicity -> support`;
2. the weak-composition proof of the sharp common-order bound;
3. the defect recurrence and the claim that diagonal persistence makes loss irreversible;
4. the strict class-path / fine-witness boundary;
5. scope wording so no combinatorial multiplicity is renamed physical focusing.

If accepted, the old P021 “does endpoint identity compose?” question stays closed, and this stronger multiplicity/provenance continuation can be closed at the finite class-level boundary.

A future P021 task should be opened only if there is a separately declared observable beyond this return, for example a genuinely fine-witness multiplicity carrier with explicit fiber capacities, or a separately validated P016 physical interpretation.
