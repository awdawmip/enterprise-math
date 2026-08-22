# Native Graded Scale Valuation Calculus — Tool Discovery Report

Status: `RESEARCH_CHECKPOINT / TOOL_DISCOVERY_COMPLETE / DRIVER_REVIEW_REQUIRED`  
Date: `2026-08-22`  
Researcher-ID: `EM-TDEV-8A73F1`  
Task: `RS-TD-EV-NATIVE-VALUATION-EHRHART-BRION-CALCULUS`  
Taskbook: `research_tasks/TOOL_DISCOVERY_NATIVE_VALUATION_EHRHART_BRION_CALCULUS_20260822.md`  
Owner branch: `research/tool-native-valuation-ehrhart-brion-calculus`

## Leading verdict

`NATIVE_VALUATION_CALCULUS_DISCOVERED`

This is a researcher verdict under the taskbook gate, not a Foundation promotion. No current Foundation definition is modified.

The discovered tool is named here:

`NATIVE_GRADED_SCALE_VALUATION_CALCULUS` (`NGSVC`).

Its core is not a claim that every Enterprise object has an Ehrhart polynomial. The core is a reusable calculus for **locally finite typed witness sets equipped with an integer native scale**, with exact valuation laws, shell/cumulative transforms, finite-difference certificates, rational-series/recurrence certificates when available, local-to-global overlap correction, additive-scale product convolution, and an exact quotient information-loss defect.

The same interface is used without refitting on:

1. the current three-positive-axis canonical address atlas; and
2. the current component-typed Path-formal/N-BRC/Boolean-BRC multipath family.

The first application is polynomial/Ehrhart-like. The second deliberately violates polynomiality at the full witness level (`2^d`) while remaining rational-generating-function controlled. This is the principal pressure-test result: the calculus survives the failure of polynomiality instead of forcing every family into an Ehrhart-polynomial template.

---

## 1. Semantic layer and assumptions

### 1.1 Native premises actually used

The task obeys the frozen Foundational Logic principle:

`CLASSICAL_DEFINITION_NOT_INHERITED_AS_NATIVE_PREMISE`.

The tool uses only finite discrete witness identity, task-declared typing, integer scale/refinement data, set union/intersection, integer counting, and formal generating functions as a derived readout.

For the two demonstrations:

- spatial source objects use current canonical addresses
  `(a,b,c) in N_0^3, min(a,b,c)=0`
  and the three glued sector charts;
- path source objects use the current component-typed transition skeleton and
  `PATH_FORMAL_BRC -> N_BRC -> BOOLEAN_BRC`.

No Euclidean volume, classical convex polytope, classical cone, or classical vertex is imported as an N0 premise.

### 1.2 Tool semantic typing

`NGSVC` is a **derived operational counting tool**. It does not retype its input objects.

- source witness identity / transition identity: whatever native type the source definition already declares;
- grading `sigma`: task-declared integer observable derived from source semantics;
- `b_X`, `F_X`, finite differences, generating functions: derived counting/readout layer;
- quotient-collapse defect: derived certificate of information forgotten by a declared quotient;
- growth degree: property of the enumerator, **not automatically native geometric dimension**.

This separation is essential. In particular:

`ENUMERATOR_GROWTH_DEGREE != NATIVE_DIMENSION`

unless a separate theorem for a specific object family proves such an identification.

---

## 2. Definition: locally finite graded Enterprise object

A **graded Enterprise witness object** is a pair

`X = (W_X, sigma_X)`

where:

1. `W_X` is a typed set of discrete witnesses/states/events/packets accepted by the source semantics;
2. `sigma_X : W_X -> N_0` is a declared native scale or birth index;
3. `X` is **locally finite in scale**:

   `#{w in W_X : sigma_X(w) <= d} < infinity`

   for every finite `d`.

Optional finite or monoid-valued tags may be added:

`tau_X : W_X -> M`.

A tag refines the readout but is not required by the base calculus.

Define:

`X[d] := {w in W_X : sigma_X(w) <= d}`

(the cumulative visible object at scale `d`),

`Shell_X(d) := {w in W_X : sigma_X(w) = d}`,

`b_X(d) := #Shell_X(d)`,

and

`F_X(d) := #X[d] = sum_{k=0}^d b_X(k)`.

Set `F_X(-1)=0`.

The exact shell/cumulative relation is therefore

`b_X(d) = Delta F_X(d) := F_X(d)-F_X(d-1)`.

This is the first cross-scale operator: a single cumulative count hides births by scale; one finite difference recovers the entire shell sequence.

---

## 3. Generating-function transform

Define the exact-shell series

`B_X(z) := sum_{d>=0} b_X(d) z^d`

and cumulative series

`H_X(z) := sum_{d>=0} F_X(d) z^d`.

As formal power series,

`H_X(z) = B_X(z)/(1-z)`

and

`B_X(z) = (1-z) H_X(z)`.

With an additive tag `tau` in `N_0^r`, define

`B_X(z; y_1,...,y_r)
 = sum_{w in W_X} z^{sigma(w)} y^{tau(w)}`.

The tagged series is a compression of scale plus the declared tag only. It does not recover witness identity unless the tag itself is injective.

---

## 4. The valuation theorem

### Theorem 4.1 — coefficientwise native valuation

Let `A` and `B` be compatible graded subobjects of one typed ambient witness universe, carrying the **same inherited scale function**. Then for every `d`:

`F_{A union B}(d) + F_{A intersection B}(d)
 = F_A(d) + F_B(d)`.

The same equality holds shellwise:

`b_{A union B}(d) + b_{A intersection B}(d)
 = b_A(d) + b_B(d)`.

Therefore it also holds coefficientwise for `B(z)` and `H(z)`.

#### Proof

At every fixed scale `d`, `A[d]` and `B[d]` are finite sets. Ordinary finite-set cardinality gives

`|A[d] union B[d]| + |A[d] intersection B[d]|
 = |A[d]| + |B[d]|`.

Compatibility of the inherited grading implies

`(A union B)[d]=A[d] union B[d]`

and similarly for intersection. Shellwise equality is the same finite-set identity on exact-grade fibers. Summing coefficients gives the generating-function version. QED.

This theorem is genuinely reusable and does not require convexity, Euclidean geometry, or polynomiality.

---

## 5. Local-to-global decomposition with overlap provenance

### Corollary 5.1 — finite cover inclusion-exclusion

For a finite compatible cover

`X = U_1 union ... union U_m`,

the cumulative and shell enumerators satisfy exact inclusion-exclusion:

`F_X(d)
 = sum_{empty != I subseteq {1,...,m}}
   (-1)^{|I|+1} F_{intersection_{i in I} U_i}(d)`,

and identically for `b`, `B`, and `H`.

Equivalently, one may group equal intersections into the finite intersection poset and use its Möbius coefficients.

This is the Enterprise **Brion-role local-to-global mechanism** discovered in this task:

`GLOBAL SCALE COUNT
 = LOCAL PIECE COUNTS + EXPLICIT OVERLAP CORRECTION`.

It is intentionally not called “Brion's theorem.” Classical Brion theory is substantially stronger and more geometric: for lattice polytopes it expresses a lattice-point generating function through rational functions associated with vertex cones. Here there are no native classical vertices or cones in the premise. The recovered mechanism is the operational principle of exact local contribution plus provenance-preserving overlap correction.

A local decomposition without its intersections/provenance is invalid under this tool.

---

## 6. Composition laws

### 6.1 Formal/disjoint union

For typed disjoint union:

`B_{X disjoint_union Y}(z)=B_X(z)+B_Y(z)`,

and likewise for cumulative series.

### 6.2 Additive-scale product / concatenation

Suppose the product witness is a pair `(x,y)` and scale is additive:

`sigma_{X tensor Y}(x,y)=sigma_X(x)+sigma_Y(y)`.

Then exact shells convolve:

`b_{X tensor Y}(d)
 = sum_{i+j=d} b_X(i)b_Y(j)`,

hence

`B_{X tensor Y}(z)=B_X(z)B_Y(z)`.

Using `B=(1-z)H`:

`H_{X tensor Y}(z)=(1-z)H_X(z)H_Y(z)`.

The same law applies to typed concatenation when concatenation is bijective with a composable pair and transition count is additive.

### 6.3 Refinement / fiber transport

For a scale-preserving refinement map

`r : Y -> X`

with `sigma_Y(y)=sigma_X(r(y))`,

`b_Y(d)
 = sum_{x in Shell_X(d)} #r^{-1}(x)`.

There is **no universal refinement-invariance of count**. Count is preserved exactly only under a separately declared unit-fiber/bijection condition. This respects the current Foundation rule that refinement does not introduce fractional native packet weights merely to preserve a continuum measure.

### 6.4 Quotient

A quotient

`q : W_X -> Q`

is scale-compatible only when `sigma_X` is constant on each quotient fiber, so that `sigma_Q([w])` is well-defined.

The quotient enumerator counts quotient classes, not source witnesses.

Define the shellwise **quotient-collapse defect**

`D_q(d)
 := b_X(d)-b_Q(d)
 = sum_{C in Shell_Q(d)} ( #q^{-1}(C) - 1 ) >= 0`.

Cumulatively,

`D_q^{<=}(d)=F_X(d)-F_Q(d)`.

This is an exact cross-scale certificate of multiplicity/provenance loss caused by the quotient.

---

## 7. Sharp quotient boundary: valuation does not automatically commute with quotient image

The base valuation theorem applies to compatible subobjects in a common witness universe. It does **not** say that taking quotient images preserves intersection.

Counterexample:

- `A={p}`;
- `B={q}`;
- `p != q`;
- quotient identifies `q(p)=q(q)=C`.

Then:

`#q(A union B)=1`,

but

`#q(A)+#q(B)-#q(A intersection B)=1+1-0=2`.

Thus naive post-quotient inclusion-exclusion fails.

A sufficient compatibility condition is saturation: if `A` and `B` are unions of whole quotient fibers, then

`q(A intersection B)=q(A) intersection q(B)`

and valuation descends.

Freeze for this tool:

`QUOTIENT_IMAGE_IS_NOT_AUTOMATICALLY_A_VALUATION_MORPHISM`.

`SATURATION_OR_EQUIVALENT_INTERSECTION_COMPATIBILITY_IS_REQUIRED`.

This boundary is directly relevant to BRC/support/trace quotients, where cross-piece witness identifications are common.

---

## 8. Finite-difference and rationality classifier

Polynomiality is an output class, not a premise.

### 8.1 Polynomial / eventual-polynomial certificate

For an integer sequence `F(d)`, if

`Delta^{r+1} F(d)=0`

for all sufficiently large `d`, then the tail is a polynomial in `d` of degree at most `r` (Newton finite-difference expansion). Conversely, every eventual polynomial of degree at most `r` has eventually vanishing `(r+1)`-st difference.

Define when finite:

`GDEG(X)
 := min { r : Delta^{r+1} F_X(d)=0 eventually }`.

This is the **scale-growth degree of the enumerator**, not a native dimension theorem.

### 8.2 Quasi-polynomial certificate

A period-`m` eventual quasi-polynomial of degree at most `r` is detected by applying the polynomial finite-difference test separately to every residue-class subsequence

`F(j+mn)`, `0<=j<m`.

Equivalently, an eventual annihilator is a power of the step-`m` difference. Its generating function has, after a finite transient numerator, denominator dividing a power of `(1-z^m)`.

### 8.3 Rational-series / recurrence certificate

A more general and crucial class is finite linear state evolution.

If shell-state vectors satisfy

`c_{d+1}=M c_d`

with finite integer matrix `M`, and

`b_X(d)=u^T c_d`,

then formally

`B_X(z)
 = u^T (I-zM)^{-1} c_0`.

Since the inverse is `adj(I-zM)/det(I-zM)`, `B_X` is rational. Consequently `b_X(d)` obeys a finite constant-coefficient linear recurrence.

This includes many non-polynomial discrete languages.

### 8.4 Exact negative boundary: rationality is not universal

Local finiteness alone does not imply rationality.

Construct a valid graded witness set with

`b_X(d)=2^{d^2}`

distinct witnesses born at scale `d`.

Each finite scale still contains finitely many witnesses, so the base interface is admissible. But `b_X(d)` grows faster than every fixed exponential. Coefficients of a rational generating function over characteristic zero satisfy a finite linear recurrence and therefore have at most exponential-polynomial growth. Hence this example is not rational-generating-function controlled.

Therefore:

`LOCAL_FINITE_GRADED != RATIONAL_GENERATING_FUNCTION`.

The base valuation calculus survives; only the rational compression subtool is unavailable.

---

## 9. Reciprocity status

No generic reciprocity theorem is justified.

The base interface contains scale, witnesses, and optional tags. It contains no canonical “interior,” complement, orientation, duality, or negative-scale semantics. Two objects can have the same `F_X(d)` while carrying different independently declared boundary/interior structures.

Therefore an Ehrhart-Macdonald-style reciprocity law cannot be inferred from `NGSVC` alone.

Freeze:

`RECIPROCITY_REQUIRES_ADDITIONAL_NATIVE_DUALITY_OR_INTERIOR_SEMANTICS`.

This is a kill boundary, not an unfinished proof obligation.

---

# 10. Cross-domain demonstration A — three-positive-axis address atlas

Use the current canonical address set

`A_E = {(a,b,c) in N_0^3 : min(a,b,c)=0}`

with its three glued sector charts:

`S_12={(a,b,0)}`,
`S_23={(0,b,c)}`,
`S_31={(a,0,c)}`.

Declare the counting horizon

`sigma(a,b,c)=max(a,b,c)`.

This is an integer coordinate horizon. It is **not** declared to be Euclidean radius, native length, area, or volume.

Then

`A_E[d]={min(a,b,c)=0, max(a,b,c)<=d}`.

Each sector contributes `(d+1)^2` states.

Each pairwise sector intersection is one positive axis and contributes `d+1`.

The triple intersection is the origin and contributes `1`.

By the valuation theorem:

`F_A(d)
 = 3(d+1)^2 - 3(d+1) + 1
 = 3d^2+3d+1`.

Exact shells are:

`b_A(0)=1`,

`b_A(d)=6d` for `d>=1`.

The shell calculation is itself local-to-global. For `d>=1`, each square sector has `2d+1` newly visible states, each pairwise axis has one, and the triple origin has none:

`b_A(d)=3(2d+1)-3=6d`.

Generating functions:

`B_A(z)
 = 1 + 6z/(1-z)^2
 = (1+4z+z^2)/(1-z)^2`,

`H_A(z)
 = (1+4z+z^2)/(1-z)^3`.

Finite differences give:

`Delta^2 F_A = 6` eventually,

`Delta^3 F_A = 0` eventually,

so:

`GDEG(A_E,sigma)=2`.

Again, this is a scale-enumerator invariant only.

### New compression/certificate

The raw visible set has `Theta(d^2)` states. The exact count at arbitrary `d` is compressed to a fixed formula/rational signature plus the three-chart overlap provenance.

The certificate is not merely the pointwise formula: it records **why** the formula is valid under gluing:

`3 sector contributions - 3 axis overlaps + 1 triple overlap`.

This remains auditable if chart pieces are changed or refined.

---

# 11. Cross-domain demonstration B — component-typed BRC multipath

Fix a translated native sector and two component-typed generators `X_i,X_j` on the current Path-formal BRC skeleton.

Let `W` be all finite typed monotone generator words from the chosen start placement. Use native transition count as scale:

`sigma(w)=word_length(w)`.

This is an event count from the path substrate. It is not automatically geometric length.

Add the tag

`tau(w)=(#X_i(w), #X_j(w))`.

The exact tagged shell series is:

`B_path(z;u,v)
 = sum_w z^{|w|}u^{#X_i(w)}v^{#X_j(w)}
 = 1/(1-z(u+v))`.

Therefore at exact transition scale `d`:

`b_path(d)=2^d`.

Cumulatively:

`F_path(d)=2^{d+1}-1`.

The full path family is therefore **not polynomial, not eventual polynomial, and not quasi-polynomial**. No finite order of ordinary finite difference vanishes.

Nevertheless it is rational-generating-function controlled:

`B_path(z)=1/(1-2z)`,

`H_path(z)=1/((1-z)(1-2z))`,

with exact recurrence:

`b_path(d)=2 b_path(d-1)`.

This is the decisive cross-domain test: the same interface survives outside the Ehrhart-polynomial class.

### 11.1 Endpoint multiplicity as coefficient extraction

For terminal component counts `(a,b)` with `a+b=d`:

`[z^d u^a v^b] B_path
 = binom(d,a)`.

Hence the current BRC bridge examples are recovered without enumerating words:

- `(1,1)` -> `binom(2,1)=2`;
- `(3,4)` -> `binom(7,3)=35`.

The single rational tagged series compresses all terminal multiplicities simultaneously.

### 11.2 Boolean/trace-support quotient

Now quotient words by their component-count terminal `(a,b)`.

At exact scale `d`, quotient classes are:

`(0,d),(1,d-1),...,(d,0)`,

so

`b_support(d)=d+1`.

Thus:

`B_support(z)=1/(1-z)^2`,

`F_support(d)=(d+1)(d+2)/2`,

`H_support(z)=1/(1-z)^3`.

The quotient-collapse defect is:

`D_q(d)
 = 2^d-(d+1)`.

Cumulatively:

`D_q^{<=}(d)
 = 2^{d+1}-1 - (d+1)(d+2)/2`.

This is a new exact certificate of the information lost when exponentially many path witnesses collapse to polynomially many typed support/trace terminals.

For the fixed `(a,b)` fiber, the richer coefficient is `binom(a+b,a)` while Boolean support keeps only nonemptiness. The current frozen `35 -> 35 -> 1` bridge is therefore one coefficient-level instance of this global quotient-collapse profile.

### 11.3 A useful negative comparison

The spatial atlas has cumulative growth degree `2`.

The BRC endpoint-support quotient also has cumulative growth degree `2`.

They are semantically very different objects.

Therefore:

`SAME_GDEG_DOES_NOT_IMPLY_SAME_NATIVE_DIMENSION_OR_GEOMETRY`.

This directly blocks a tempting but invalid “finite-difference degree = world dimension” inference.

---

## 12. Historical mechanism comparison

The historical theories are used only as mechanism references.

### Ehrhart role

Classically, integer dilations of an integral lattice polytope have polynomial lattice-point counts, with degree tied to polytope dimension. Rational polytopes lead naturally to quasi-polynomial behavior, and generating functions organize the scale sequence.

`NGSVC` retains the operational questions:

- what is the scale sequence?
- does a finite difference terminate?
- is the series rational?
- what recurrence or growth signature results?

It does **not** inherit “convex polytope,” Euclidean volume, or classical dimension as native premises.

### Valuation role

Classical valuations encode additivity with overlap correction.

`NGSVC` recovers this mechanism exactly from finite typed witness sets:

`count(A union B)+count(A intersection B)=count(A)+count(B)`

at every scale, hence simultaneously across all scales.

### Brion role

Classical Brion theory decomposes lattice-point generating functions into local rational contributions attached to vertex cones.

`NGSVC` does **not** claim that its native local pieces are classical vertex cones. Its validated native analogue is:

- choose declared local pieces;
- count each piece;
- retain their exact intersections/provenance;
- reconstruct the global series by valuation/Möbius correction.

For the Enterprise address atlas the local pieces are the three sector charts, their axis overlaps, and the origin stratum.

### Novelty boundary

No claim is made that graded sets, valuations, formal generating functions, finite differences, inclusion-exclusion, or rational recurrences are new mathematics.

The supported novelty claim is project-internal and architectural:

> one native-compatible interface has been rebuilt from finite discrete semantics and reused unchanged on two current Enterprise domains, including one exponential non-polynomial path family, while exposing an exact quotient-collapse defect and an exact quotient/valuation compatibility boundary.

That is the tool-discovery result.

Historical references used for mechanism comparison:

- E. Ehrhart, lattice-point enumeration under integer dilation;
- M. Beck and S. Robins, *Computing the Continuous Discretely*;
- P. McMullen, valuation theory for polytopes;
- M. Beck, C. Haase, F. Sottile, expository proofs of Brion/Lawrence/Varchenko rational generating-function formulas;
- C. Haase, *Polar decomposition and Brion's theorem*.

---

## 13. Counterexamples and kill conditions

The tool must be rejected or weakened in the following exact cases.

1. **Not locally finite at finite scale.**  
   If `X[d]` is infinite, the integer cardinality enumerator is not defined by this API.

2. **Incompatible scales across glued pieces.**  
   If the same witness receives different grades in `A` and `B`, coefficientwise valuation is not typed.

3. **Quotient is not grade-compatible.**  
   If one quotient class contains witnesses of different birth scales, no quotient grade is canonically inherited.

4. **Non-saturated quotient decomposition.**  
   Quotient image need not preserve intersections; naive valuation can fail exactly as in Section 7.

5. **Polynomiality is inferred from a finite fit.**  
   Forbidden. Use finite-difference/recurrence proof or a family theorem.

6. **Rationality is assumed from local finiteness.**  
   False; `b(d)=2^{d^2}` is a counterexample.

7. **Growth degree is promoted to geometric dimension.**  
   Invalid without an independent semantic theorem.

8. **Reciprocity is asserted without interior/duality semantics.**  
   Unsupported by the base interface.

9. **Enumerator is treated as lossless.**  
   False. `F` and `b` forget all identity within equal-grade shells; tagged series forget everything except declared tags; quotient enumerators additionally forget within-class provenance.

These are hard negative boundaries of the current tool.

---

## 14. Exact information forgotten

The forgetful chain is explicit.

For the untagged enumerator:

`witness structure
 -> shell cardinalities b_X(d)
 -> cumulative counts F_X(d)`.

`F` and `b` are equivalent to each other through one finite difference / cumulative sum, but neither determines the witness set, adjacency, generator word, placement, correlation, or quotient-fiber structure.

For a tagged series:

`witness structure
 -> histogram by (scale, declared tags)`.

It preserves only that histogram.

For a quotient enumerator:

`source witnesses
 -> quotient classes
 -> class counts by scale`.

The exact integer `D_q(d)` reports how many witness occurrences beyond one representative per class were discarded at shell `d`, but it still does not reconstruct which witnesses were merged.

---

# 15. TOOL API

## Inputs

Required:

- typed witness set `W_X`;
- native/task-declared grade `sigma_X : W_X -> N_0`;
- proof/guarantee of finite `X[d]` for finite `d`.

Optional:

- additive tags `tau`;
- finite compatible local cover `{U_i}`;
- additive-scale product/concatenation;
- scale-compatible quotient `q`;
- finite-state transition representation for rational compression.

## Outputs

Base:

- `Shell_X(d)`;
- `b_X(d)`;
- `X[d]`;
- `F_X(d)`;
- `Delta^k F_X`;
- `B_X(z)` and optional tagged `B_X(z;y)`;
- `H_X(z)`.

Certificates when applicable:

- finite-difference growth degree `GDEG`;
- rational generating-function / recurrence certificate;
- finite-cover valuation decomposition with overlap provenance;
- product-convolution certificate;
- quotient-collapse defect `D_q(d)`;
- quotient saturation/compatibility verdict.

## Laws

1. `b=Delta F`.
2. `H=B/(1-z)`.
3. Compatible union/intersection valuation at every scale.
4. Finite-cover inclusion-exclusion / intersection-poset Möbius correction.
5. Additive-scale products -> shell convolution / generating-function multiplication.
6. Scale-preserving refinement -> explicit fiber sum.
7. Scale-compatible quotient -> exact nonnegative collapse defect.
8. Quotient images preserve valuation only under intersection-compatible conditions such as saturation.

## Failure modes

- infinite finite-scale fibers;
- conflicting scale semantics;
- cross-grade quotient fibers;
- non-saturated quotient pieces;
- arbitrary non-rational shell sequence;
- no native reciprocity structure;
- unjustified promotion of growth degree to dimension.

## Cross-domain demonstrations

### Demo A — address atlas

Input:
`A_E`, `sigma=max(a,b,c)`.

Output:

`F(d)=3d^2+3d+1`,
`b(0)=1`,
`b(d)=6d` for `d>=1`,
`H=(1+4z+z^2)/(1-z)^3`,
`GDEG=2`.

Local decomposition:
three sectors minus three axis overlaps plus origin.

### Demo B — typed BRC path family

Input:
two-generator typed path words,
`sigma=transition count`,
tag `(a,b)`.

Output:

`B_path(z;u,v)=1/(1-z(u+v))`,
`b_path(d)=2^d`,
`F_path(d)=2^{d+1}-1`,
endpoint multiplicity `binom(a+b,a)`.

Quotient support:

`b_support(d)=d+1`,
`F_support(d)=(d+1)(d+2)/2`,
`D_q(d)=2^d-(d+1)`.

This is rational but non-polynomial at full witness level.

---

## 16. Executable finite evidence

Checker:

`tools/tool_discovery_native_valuation_ehrhart_brion_calculus_check.py`

Frozen output:

`research_notes/TOOL_DISCOVERY_NATIVE_VALUATION_EHRHART_BRION_CALCULUS_CHECK_OUTPUT_20260822.json`

The checker uses standard-library Python and integer arithmetic only.

Coverage:

- spatial scales `d=0..24`;
- direct cube enumeration vs closed form;
- cumulative sector inclusion-exclusion;
- shell inclusion-exclusion;
- third finite-difference vanishing;
- path scales `d=0..16`;
- explicit enumeration of all binary generator words;
- `153` endpoint/binomial multiplicity checks;
- commuting diamond `(1,1)=2`;
- `(3,4)=35`;
- support shell `d+1`;
- path recurrence `2^d`;
- `21` independent convolution coefficient checks;
- explicit non-saturated quotient valuation counterexample.

Result:

`status = PASS`

`mismatch_count = 0`

`structural_checks = 168`

`payload_sha256 = 9d7a2c8f9143cf2ef09e9b6ef9e83711881a7afad1777f7467cc4c2bfb2a86d3`

Finite checking is evidence for the concrete demonstrations. It is not substituted for the general set-theoretic proofs in Sections 4–7.

---

## 17. Acceptance-gate audit

Taskbook gate:

- explicit reusable input/output interface: **PASS**;
- nontrivial algebraic law: **PASS** — coefficientwise valuation, cover Möbius correction, additive-scale convolution;
- invariant/certificate across scales: **PASS** — `GDEG`, rational recurrence signature, quotient-collapse defect;
- successful reuse on two distinct Enterprise families: **PASS** — spatial atlas and typed BRC multipath;
- at least one non-restatement compression/certificate: **PASS** — rational tagged path series compresses all `2^d` witnesses and exposes global quotient-collapse profile; spatial local-to-global provenance compresses `Theta(d^2)` enumeration;
- explicit kill conditions and negative boundaries: **PASS**;
- no Foundation modification: **PASS**.

Researcher leading verdict remains:

`NATIVE_VALUATION_CALCULUS_DISCOVERED`.

Driver review is still required before any canonical theorem/tool promotion.
