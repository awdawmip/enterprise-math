# GEO6 First-Wave Accepted Prior-Art Synthesis — Research Return

Task: `RS-GEO6-FIRSTWAVE-ACCEPTED-PRIOR-ART-SYNTHESIS`  
Publication: `TP2-D5FC77B38C002D9EA868`  
Researcher-ID: `EM-G6PA-9C72F1`  
Claim: `chatgpt-g6pa-20260830-1459-9c72f1`  
Execution branch: `research/geo6-firstwave-prior-art-synthesis-em-g6pa-9c72f1`  
Date: `2026-08-30`  
Terminal verdict: `AUDIT_COMPLETE`  
Hard target: `GEO6_FIRSTWAVE_ACCEPTED_CLAIMS_PRIOR_ART_EXACTLY_CLASSIFIED`

## 0. Executive result

The audit closes the immediate duplication gate for the three accepted GEO6 first-wave Results:

- `RR-EBAF426828157644FB51` — Kissing contact-capacity bridge;
- `RR-36E518770A5FB701B42C` — Falconer relation-distance spectrum;
- `RR-589899C832BA7069520F` — Hadwiger signed-shell cover/illumination.

The decisive finding is that **most of the finite combinatorics is already standard mathematics at exact or strictly more general strength**. The surviving Enterprise value is not a new finite number. It is a sharply isolated family of semantic-selection problems: P000 currently does not canonically determine which contact relation, local adjacency/refinement law, rotation-operation closure, or ambient translation/homothety action is native.

Across 19 separately audited claims/obstructions:

- `EXACT_DUPLICATE`: 3;
- `STRICT_ANTECEDENT`: 10;
- `ADJACENT_METHOD`: 3;
- `NO_MATERIAL_MATCH`: 3.

`NO_MATERIAL_MATCH` is **not** a historical novelty certificate. It means only that, under the searched formal hypotheses, the remaining statement is a P000-specific semantic/interface question rather than an identified classical theorem.

The exact machine-readable matrix is frozen at:

`research_artifacts/GEO6_FIRSTWAVE_ACCEPTED_PRIOR_ART_SYNTHESIS/claim_source_matrix.json`.

The independent finite-comparison checker is:

`research_checks/GEO6_FIRSTWAVE_ACCEPTED_PRIOR_ART_SYNTHESIS_CHECK_20260830.py`.

The checker uses exact integer arithmetic and independently re-verifies the concrete identifications used below: S4/Johnson orbitals, Lee-ball counts, Hamming distance sets, signed-shell separation, the K6 edge-cover reduction, the even-weight code reduction, and the frozen E6 `72/20/720` witness.

---

## 1. Classification semantics

The taskbook requires four labels. They are used here claim-by-claim rather than route-by-route.

- `EXACT_DUPLICATE`: the accepted mathematical statement is an exact specialization or standard named object with the same substantive theorem/data already in the literature.
- `STRICT_ANTECEDENT`: a published/general classical result or elementary general theorem strictly contains the accepted finite claim as a special case.
- `ADJACENT_METHOD`: the external theory supplies essentially the same combinatorial mechanism, but the Enterprise object/hypotheses differ enough that the exact accepted statement is not a theorem instance without an additional identification.
- `NO_MATERIAL_MATCH`: the searched external theory does not resolve the P000-specific semantic statement under equivalent hypotheses. This label never means “novelty proved”.

The audit separates **mathematical duplication** from **P000 admissibility/typing**. A classical theorem may completely subsume a finite calculation while leaving open whether P000 canonically selects the structure to which that theorem applies.

---

## 2. Source backbone

The strongest useful antecedent families located and reconstructed are:

1. **E6 lattice/root system** — G. Nebe and N. J. A. Sloane, Catalogue of Lattices, E6 entry: dimension `6`, minimal norm `2`, kissing number `72`.  
   https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/E6.html

2. **E6 root polytope / 1_22 f-vector** — standard 72-vertex E6 root polytope with 720 edges. A secondary online reference was used only as a bibliographic locator; the `72/20/720` incidence was independently regenerated from the frozen E6 Gram matrix by the task checker.  
   https://www.handwiki.org/wiki/1_22_polytope

3. **Association schemes / Johnson scheme** — J. J. Seidel, introduction to association schemes: `J(v,k)` has vertices the k-subsets of a v-set, with relation `i` determined by intersection size `k-i`; valencies are `C(k,i) C(v-k,i)`.  
   https://www.maths.tcd.ie/EMIS/journals/SLC/opapers/s26seidel.pdf

4. **Johnson graph** — standard definition; `J(4,2)` is the octahedral graph.  
   https://mathworld.wolfram.com/JohnsonGraph.html

5. **Lee metric** — S. W. Golomb and L. R. Welch, *Perfect Codes in the Lee Metric and the Packing of Polyominoes*, SIAM J. Appl. Math. 18 (1970), 302–317.  
   https://epubs.siam.org/doi/10.1137/0118025

6. **Lee-ball cardinality formula** — the standard formula `sum_i 2^i C(n,i) C(r,i)` in the unsaturated/integer-lattice regime; used only to identify the Enterprise `V_6` formula, and independently checked by exact enumeration.  
   https://user.math.uzh.ch/bariffi/2025_07_SIAM.pdf

7. **Hamming scheme / Hamming graph** — words of length `d` over an alphabet of size `q`, distance equal to the number of differing coordinates; `H(d,q)` has diameter `d`.  
   https://aeb.win.tue.nl/drg/graphs/Hamming.html

8. **Minimum edge cover / Gallai identity** — for graphs without isolated vertices, `nu(G)+rho(G)=|V(G)|`.  
   https://mathworld.wolfram.com/MinimumEdgeCover.html

9. **Binary single parity-check code** — the `[n,n-1,2]` SPC code is exactly the even-weight binary code; its coordinate automorphism group is `S_n`.  
   https://errorcorrectionzoo.org/c/parity_check

10. **Covering arrays** — a covering array of strength `t` requires every `t`-column subarray to contain every `t`-tuple. At binary strength `1`, this reduces to requiring both symbols in every column.  
    https://www.sciencedirect.com/science/article/pii/S0020025518304171

11. **Classical Levi–Hadwiger illumination/covering problem** — formulated for convex bodies in `R^n`, translates of interiors / smaller homothetic copies, or equivalent Euclidean illumination; the conjectural general upper bound is `2^n`.  
    https://doi.org/10.1007/s00493-025-00195-7

These sources are antecedent anchors, not claims that every P000 object is one of these classical objects.

---

## 3. Kissing contact-capacity audit

### K1 — external E6 `72/20/720`

**Enterprise claim.** The regenerated E6 witness has 72 roots; pairing `1` defines a 20-regular contact graph with 720 edges.

**Classification: `EXACT_DUPLICATE`.**

The 72-vector part is standard E6 lattice/root-system data. The corresponding 72-vertex root polytope has 720 edges. Once those vertices/edges are fixed, regularity gives

`degree = 2*720/72 = 20`.

The Enterprise reflection-closure computation is valuable as an independent exact regression, but it is not a new E6 theorem.

**Surviving residue:** none for E6 itself. The unresolved question is transfer: what native P000 structure, if any, realizes an E6-like contact graph?

### K2 — seven-Cell axis star capacity `6`

**Classification: `STRICT_ANTECEDENT`.**

The declared object is the elementary star graph `K_{1,6}`: center degree 6, leaf degree 1. The general `K_{1,n}` statement strictly contains it.

**Surviving residue:** whether this star is merely an admissible probe or is canonically forced by P000.

### K3 — four-Cell S4 invariant graphs are empty/K4

**Classification: `STRICT_ANTECEDENT`.**

S4 is transitive on unordered 2-subsets of a four-set. Therefore an S4-invariant simple edge relation is a union of unordered-pair orbits; there is only one non-diagonal orbit. Hence the only possibilities are empty and complete, with degree 0 or 3.

**Surviving residue:** group invariance does not say which invariant relation is *native contact*.

### K4 — six-axis capacities `{0,1,4,5}`

**Classification: `STRICT_ANTECEDENT`.**

The six axis labels are exactly the six 2-subsets of a four-set. This is the Johnson scheme `J(4,2)`. Its two non-diagonal relations are:

- intersection size 1: valency `C(2,1)C(2,1)=4`, 12 unordered edges;
- intersection size 0: valency `C(2,2)C(2,2)=1`, 3 unordered edges.

Taking invariant unions yields degrees exactly `0,1,4,5`. Thus the Enterprise orbital census is a direct `J(4,2)` specialization.

**Surviving residue:** the Johnson scheme classifies all S4-compatible pair relations but does not canonically select one as P000 contact, nor does it supply the missing hidden residual state.

### K5 — finite-readout embedding obstruction and `r>=12`

**Classification: `STRICT_ANTECEDENT`.**

The core proof is generic: an injective faithful graph embedding cannot place 72 distinct vertices into 7, 6, or 4 states, and degree preservation also fails against the declared maxima. If a 72-state transfer factors through `6*r` labels, injectivity forces `6r>=72`, hence `r>=12`.

The number 12 is therefore a pigeonhole lower bound, not a new geometric invariant and not sufficiency.

### K6 — rotation alone cannot canonically select contact

**Classification: `NO_MATERIAL_MATCH`.**

Classical permutation-group/orbital theory explains why several invariant relations can coexist. It does not contain a theorem choosing one as a native P000 contact predicate. This is a semantic underdetermination statement about the P000 interface, not a classical graph theorem.

**Residue frozen:**

`CONTACT_SELECTOR` = derive a canonical native Cell contact/readout law, possibly with an equivariant residual contact state beyond the six-axis projection.

---

## 4. Falconer relation-distance audit

### F1 — connected graph positive distance spectrum is `{1,...,diam}`

**Classification: `STRICT_ANTECEDENT`.**

This is a general graph-metric fact, not a six-dimensional theorem. If `y` is at distance `D` from `x`, a geodesic from `x` to `y` has vertices at every integer distance `0,...,D`. Therefore every connected graph realizes all positive distances through its diameter.

No dimension, lattice, or P000 data are needed.

### F2 — exact `V_6(r)` formula

**Classification: `EXACT_DUPLICATE`.**

`V_6(r)=sum_{j=0}^6 2^j C(6,j) C(r,j)`

is exactly the `n=6` Lee-ball volume formula for `Z^n`/the unsaturated Lee metric. The Enterprise stars-and-bars derivation is an independent reconstruction of a classical formula.

### F3 — `N<=V_6(s)`

**Classification: `STRICT_ANTECEDENT`.**

For connected `A`, F1 gives `s=diam(A)`. Fixing `a in A`, all points of `A` lie in the radius-s Lee ball around `a`; classical Lee volume then yields `|A|<=V_6(s)`.

The inequality itself therefore adds no new finite geometry once the unit-step Lee relation is declared.

### F4 — interval-box inequality and balanced equality

**Classification: `STRICT_ANTECEDENT`.**

For a six-axis box with side cardinalities `n_i`,

`s=sum_i(n_i-1)` and `N=prod_i n_i`,

so

`s+6=sum_i n_i`.

AM–GM immediately gives

`(s+6)^6 >= 6^6 N`,

with equality precisely at balanced side lengths. The Enterprise result is an exact model-local specialization of this elementary inequality.

### F5 — Hamming countermodel `q^6` versus six positive distances

**Classification: `EXACT_DUPLICATE`.**

The complete-fiber relation on `{0,...,q-1}^6` is precisely the Hamming graph `H(6,q)`: vertices differ in one coordinate across an edge, graph distance is Hamming distance, and the diameter is 6. Hence there are `q^6` states while the positive distance set remains `{1,...,6}`.

This is a standard Hamming-scheme object, not a newly discovered counterexample family in finite graph theory.

### F6 — P000 six-axis symmetry does not force an unbounded spectrum law

**Classification: `NO_MATERIAL_MATCH`.**

Hamming theory supplies the countermodel, but the quantified statement is about what follows from the *current P000 axiom package*. External mathematics cannot decide which admissible P000 relation is canonically intended when P000 itself has not fixed locality/refinement.

**Residue frozen:**

`LOCALITY_REFINEMENT_SELECTOR` = derive a canonical adjacency/step granularity/refinement law or another bounded-growth condition strong enough to exclude the Hamming-style coarse relation for the intended theorem.

This is the only reason to continue the Falconer lane. Re-deriving Lee growth or Hamming bounded diameter should be killed as duplication.

---

## 5. Hadwiger signed-shell audit

### H1 — cover/illumination equals coordinate-polarity separation

**Classification: `ADJACENT_METHOD`.**

Encode each allowed sign pattern as a binary row. The condition that every coordinate sees both polarities is exactly a binary strength-1 covering condition. The Enterprise lemma additionally proves that its two task-specific predicates—cover and directional illumination on the signed-shell probe—both reduce to that same incidence condition, while restricting admissible rows to the declared family `Sigma`.

Thus the combinatorial template is standard, while the exact P000 probe-to-array reduction is task-specific.

### H2 — one-step weight-2 family has value `3`

**Classification: `STRICT_ANTECEDENT`.**

Identify a weight-2 negative pattern with an edge of `K6`. To make every coordinate negative at least once, the selected patterns must form an edge cover of `K6`. Gallai's identity gives

`rho(K6)=|V|-nu(K6)=6-3=3`.

A perfect matching of three disjoint edges `(12),(34),(56)` supplies the upper certificate. In this selected triple every coordinate is negative in one row and positive in the other two, so the stronger two-polarity requirement also holds.

The finite value `3` is therefore not new.

### H3 — even composition closure has value `2`

**Classification: `STRICT_ANTECEDENT`.**

The even-sign patterns are exactly the binary even-weight/single-parity-check code after identifying sign flips with bits. At length 6 the all-one bit word has even weight, so the all-minus sign pattern belongs to the closure. Identity and all-minus are an antipodal pair showing both signs in every coordinate; one row cannot do so. Hence the optimum is 2.

The product of the three disjoint weight-2 flips explicitly gives the all-minus word, matching the accepted Enterprise composition certificate.

### H4 — sign-preserving actions give no full cover

**Classification: `STRICT_ANTECEDENT`.**

This is the elementary invariant-subset obstruction: if the operation family preserves the positive half-shell as a set, no operation can reach the negative half-shell.

### H5 — passive block-refinement invariance

**Classification: `ADJACENT_METHOD`.**

Duplicating each polarity/coordinate incidence by a passive multiplicity `m` does not change which rows satisfy the strength-1 column condition. That is standard incidence behavior. However, the assertion that the refinement is *passive*, equivariant, and introduces no new P000 moves is part of the declared probe semantics rather than a classical covering-array theorem.

### H6 — classical `2^6=64` does not transfer

**Classification: `ADJACENT_METHOD`.**

The classical Levi–Hadwiger problem assumes an `n`-dimensional convex body in Euclidean space and uses translates of its interior/smaller homothetic copies, equivalently classical illumination. The signed-axis probe is a finite relational shell with a separately declared operation family and no frozen homothety or translation structure.

Therefore the thematic analogy is legitimate, but the numerical `64` is not an antecedent theorem for the P000 signed-shell object.

### H7 — no P000 translation-cover number yet

**Classification: `NO_MATERIAL_MATCH`.**

This is the sharp semantic remainder. Classical Hadwiger theory presupposes precisely what the current P000 probe lacks: an ambient translation/affine action and compatible notion of smaller copy/interior/boundary transport. External prior art diagnoses the missing hypotheses but cannot manufacture them inside P000.

**Residues frozen:**

- `ROTATION_CLOSURE_SELECTOR` = decide whether current Full-Cell/native rotations canonically contain the necessary composition closure/global inversion;
- `TRANSLATION_ACTION_SELECTOR` = freeze ambient translations/homotheties and translation-compatible boundary transport before defining a native translation-cover number.

---

## 6. Cross-result residue map

After removing standard finite mathematics, four interfaces remain.

### R1 — `CONTACT_SELECTOR`

Need a P000-native rule that selects or derives contact between Cells, rather than merely listing S4-invariant candidate graphs. If external contact is to survive projection, derive an equivariant residual contact state and prove sufficiency; `r>=12` is only a lower pressure bound.

### R2 — `LOCALITY_REFINEMENT_SELECTOR`

Need a native reason to prefer a local/refinable/bounded-growth relation over coarse Hamming/complete-fiber adjacency. Without this, cardinality does not force an unbounded relation-distance spectrum.

### R3 — `ROTATION_CLOSURE_SELECTOR`

Need to determine exactly which native rotations are operations and whether composition closure is part of the semantics. The signed-shell answer changes from `3` to `2` solely because closure introduces global inversion.

### R4 — `TRANSLATION_ACTION_SELECTOR`

Need an ambient Cell action supporting translations/homotheties and compatible boundary transport. Until that exists, a P000 Hadwiger translation-cover number is not well-defined.

These four interfaces are materially different from the classical finite calculations that exposed them. They are the only justified GEO6 first-wave continuation targets identified by this audit.

---

## 7. Continuation kill/reopen rules

### Kill as duplicate or strictly anteceded

Do **not** open successor work whose mathematical target is merely to rediscover:

- E6 `72` roots / degree `20` / `720` contact edges;
- star capacity `6`;
- four-Cell S4 empty/K4 classification;
- six-axis `J(4,2)` capacities `0,1,4,5`;
- the Lee-ball polynomial `V_6(r)`;
- the Hamming `H(6,q)` countermodel with diameter/spectrum size 6;
- the signed-shell numerical values `3`, `2`, or infinity under the same frozen operation families;
- the fact that three disjoint two-axis flips multiply to global inversion in six axes.

These are settled by standard finite mathematics plus the accepted exact regressions.

### Reopen only on native semantic advance

A successor is justified only if it proves or sharply tests at least one of:

1. a canonical P000 contact selector or richer contact-state readout;
2. a canonical locality/refinement/bounded-growth selector;
3. the exact Full-Cell rotation-operation closure and antipode/global-inversion status;
4. a canonical ambient translation/homothety/boundary-transport structure.

Any such successor must cite this audit so it does not spend research budget on the already-classical finite layer.

---

## 8. Exact regression status

The task-local checker independently verifies, without floating point or external network calls:

- S4 transitivity on unordered pairs of four Cells;
- the two non-diagonal `J(4,2)` orbitals have sizes `3` and `12` and valencies `1` and `4`;
- invariant six-axis simple-graph degrees are exactly `0,1,4,5`;
- exact Lee-ball values `V_6(0..4)=1,13,85,377,1289` by direct enumeration and formula;
- `H(6,q)` realizes distances `0..6` for `q=2..5` while carrier size is `q^6`;
- signed-pattern separation numbers: elementary weight-2 family `3`, even family `2`, all signs `2`, sign-preserving family impossible;
- minimum edge-cover size of `K6` is `3`;
- the length-6 all-minus sign word lies in the even-weight code;
- three disjoint weight-2 flips compose to global inversion;
- E6 reflection closure from the frozen integral Gram matrix has exactly `72` norm-2 roots, pairing-1 degree `20`, and `720` edges.

Local execution of the same exact checker logic during this audit passed all assertions.

Bibliography is not machine-certified by the checker; source matching is the research judgment frozen in the claim-source matrix.

---

## 9. Terminal disposition

`AUDIT_COMPLETE`.

The hard target `GEO6_FIRSTWAVE_ACCEPTED_CLAIMS_PRIOR_ART_EXACTLY_CLASSIFIED` is met at the taskbook's declared scope.

The first-wave GEO6 results should be retained as **useful P000 diagnostic reductions**, not promoted as novelty in their standard finite combinatorial content. The audit turns three diffuse geometry analogies into four precise native-semantic interfaces:

`CONTACT_SELECTOR / LOCALITY_REFINEMENT_SELECTOR / ROTATION_CLOSURE_SELECTOR / TRANSLATION_ACTION_SELECTOR`.

That is the surviving research frontier.

## 10. Frozen outputs

- `research_returns/GEO6_FIRSTWAVE_ACCEPTED_PRIOR_ART_SYNTHESIS_RETURN_20260830.md`
- `research_checks/GEO6_FIRSTWAVE_ACCEPTED_PRIOR_ART_SYNTHESIS_CHECK_20260830.py`
- `research_artifacts/GEO6_FIRSTWAVE_ACCEPTED_PRIOR_ART_SYNTHESIS/claim_source_matrix.json`
- execution/result records under `RS-GEO6-FIRSTWAVE-ACCEPTED-PRIOR-ART-SYNTHESIS/`

## 11. Driver recommendation

Accept this audit if output pins and claim binding agree. Freeze duplicate-continuation kills immediately. If Driver opens further GEO6 work, route only to one of the four native semantic selectors above and require the successor taskbook to state which accepted P000/Full-Cell datum could actually resolve that selector.
