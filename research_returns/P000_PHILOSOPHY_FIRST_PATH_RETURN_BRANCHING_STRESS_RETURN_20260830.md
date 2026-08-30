# P000 Philosophy-First Q13 — Path-Return Branching Stress Return

Task: `RS-P000-PHILOSOPHY-FIRST-PATH-RETURN-BRANCHING-STRESS`  
Publication: `TP2-77DE9EC34E2633C5A973`  
Researcher: `EM-P000-75EE79`  
Claim: `chatgpt-p000q13-20260830-1945-b7e3c1`  
Execution branch: `research/p000-phil-q13-path-return-branching-stress-em-p000-75ee79`  
Hard target: `P000_PATH_RETURN_BRANCHING_RECONSTRUCTION_OR_FAILURE_EXACTLY_CLASSIFIED`

## Terminal verdict

`SUCCESS / FIRST_BRANCHING_COUNTERMODEL_EXACTLY_CLASSIFIED`

Secondary boundary: `Q9_PERIOD_INTERFACE_NOT_WELL_DEFINED_OUTSIDE_DEGREE_TWO` as a **single-valued class-wide scalar period interface**.

The accepted Q9 rootwise period theorem is complete on finite simple degree-two native-Cell graphs because nonbacktracking continuation is deterministic after choosing the initial direction and every connected component is a cycle. The first branching envelope destroys that uniqueness immediately.

The exact conclusions are:

1. On the smallest possible branching core, four Cells suffice. Both the diamond `K4-e` and `K4` give every root the same legal return-length support `{3,4}`. Hence the Q9 scalar period is not single-valued there, and neither minimum return nor the anonymous **set-valued** return-support packet separates these nonisomorphic states.
2. The first lower-language repair is not another scalar but **return multiplicity**. On the frozen four-Cell branching class, the anonymous rootwise multiplicity packet is injective and has an exact two-point representability image.
3. The support failure is not merely caused by erasing native degree. Two explicit connected ten-Cell **cubic** graphs have identical anonymous return-length support packets and identical minimum-return packets, yet one has two simple `4`-returns globally and the other has three. They are therefore nonisomorphic, while return multiplicity separates this exact collision.
4. No theorem is claimed that multiplicity reconstructs all finite subcubic native-Cell graphs. The positive multiplicity theorem is deliberately restricted to the smallest declared four-Cell branching class; the cubic pair is a failure certificate for support-only semantics, not a global multiplicity-completeness theorem.

This classifies the requested first branching failure without importing Cell identities, adjacency spectra, Ihara zeta, a full cycle basis, or an almost-complete object description.

## 1. Frozen scope and method reuse

Q9 remains frozen on its accepted `U_2REG` scope. Its exact rootwise-period reconstruction theorem is not redone or weakened.

The Q13 stress class keeps:

- finite simple native-Cell adjacency;
- maximum native degree at most three;
- the same uniform local axis/carrier/PF-10 decoration used in Q9;
- Cell relabeling as gauge for the observation packet;
- no Cell name, canonical label, address, or component-membership list in probe output.

### Existing tool coverage

The project toolbox already contains `T8_RELATION_OBSERVABLE_SPECTRUM`. Its exact relevant semantic rule is powerset-valued observation of a branching relation:

\[
\Sigma_{R,O}(x)=\{O(y):(x,y)\in R\}.
\]

Q13 reuses this rule as `REUSE_APPLIED`, rather than inventing a new branching-signature calculus.

Here the raw relation is “root `x` admits primitive native return witness `c`”, and the observation is the integer length `|c|`. Thus the powerset-valued image is exactly the legal return-length support. This reuse also exposes the right hard boundary: a powerset signature records **which lengths occur**, but not **how many distinct returns of each length occur**.

The multiplicity refinement below is task-local. It is not promoted as a new global Enterprise tool family.

## 2. Native branching return semantics

A **primitive return through `x`** is an undirected simple native-adjacency cycle containing `x`, interpreted before classical naming as a simple nonbacktracking path which starts at `x`, does not revisit any Cell before closing, and first returns to `x` at its final step. Orientation and choice of basepoint are quotiented when counting the underlying primitive return.

For a state `X` and root `x`, define the support

\[
\Sigma_X(x)
=\{k\ge 3:\text{there exists a primitive return of length }k\text{ through }x\}.
\]

The weakest scalar continuation of Q9 is

\[
\rho_{\min,X}(x)=\min \Sigma_X(x).
\]

The anonymous set-valued packet is

\[
\mathcal S(X)=\multiset_{x\in Cell(X)}\Sigma_X(x).
\]

The multiplicity refinement is

\[
\mu_X(x,k)
=\#\{\text{unoriented primitive returns of length }k\text{ through }x\},
\]

with anonymous packet

\[
\mathcal M(X)=
\multiset_{x\in Cell(X)}
\bigl(k\mapsto\mu_X(x,k)\bigr).
\]

### Exact single-valuedness criterion

The Q9-style root period remains a single-valued primitive-return coordinate at `x` exactly when `\Sigma_X(x)` is a singleton. In degree two this follows from deterministic continuation around the unique cycle component. At branching it is a theorem to test, not an inherited property.

## 3. Smallest branching core and exact minimal collision

Freeze

\[
\mathcal U_{BR4}
\]

to be connected finite simple native-Cell graphs on exactly four Cells, with minimum degree at least two, maximum degree at most three, and at least one degree-three Cell. All local decorations remain uniform.

### Why four Cells are minimal

A degree-three Cell in a finite simple graph needs three distinct neighbors. Therefore no branching point exists on fewer than four Cells.

So any failure already present in `U_BR4` occurs at the smallest possible support size for simple degree-three branching.

### Exact isomorphism classification of `U_BR4`

Every vertex degree is `2` or `3`, and at least one is `3`. By the handshaking lemma the number of odd-degree vertices is even. On four vertices the only possible sorted degree sequences are therefore

\[
(2,2,3,3)
\quad\text{or}\quad
(3,3,3,3).
\]

The first has five edges, hence is uniquely `K_4` with one edge deleted; call it the **diamond** `D`. The second is uniquely `K_4`.

Thus `U_BR4` has exactly two isomorphism types.

The deterministic checker independently enumerates all `2^6=64` labeled simple graphs on four vertices and finds exactly seven labeled members of `U_BR4`: six labelings of the missing edge of `D`, plus one `K4`.

### Return support in the diamond

The diamond has two triangles and one simple four-cycle. Every Cell lies on at least one triangle and on the four-cycle. Therefore for every root `x`,

\[
\Sigma_D(x)=\{3,4\}.
\]

### Return support in `K4`

Every root in `K4` lies on triangles and Hamiltonian four-cycles, hence likewise

\[
\Sigma_{K_4}(x)=\{3,4\}
\quad\text{for every }x.
\]

Consequently

\[
\mathcal S(D)=\mathcal S(K_4)
=\{\!\{\{3,4\},\{3,4\},\{3,4\},\{3,4\}\}\!\},
\]

and

\[
\multiset_x\rho_{\min,D}(x)
=
\multiset_x\rho_{\min,K_4}(x)
=\{\!\{3,3,3,3\}\!\}.
\]

But `D` and `K4` are nonisomorphic: they have five and six edges, respectively.

This gives the requested first branching countermodel.

### Single-valuedness failure is even sharper than noninjectivity

At every root of either graph there are legal primitive returns of two different lengths, `3` and `4`. Thus the Q9 scalar “the first-return period of the root” is not merely noninjective: without adding a branch-selection convention it is not intrinsically single-valued.

Choosing the minimum repairs single-valuedness but loses information. Replacing the scalar by its canonical powerset semantics repairs branching semantics but still loses information.

## 4. Exact missing information on `U_BR4`

The support packet forgets multiplicity. On the two exact models:

### Diamond multiplicity packet

For each of the two degree-two roots,

\[
\mu(3)=1,\qquad \mu(4)=1.
\]

For each of the two degree-three roots,

\[
\mu(3)=2,\qquad \mu(4)=1.
\]

Therefore

\[
\mathcal M(D)
=
\{\!\{
(3\!:\!1,4\!:\!1),
(3\!:\!1,4\!:\!1),
(3\!:\!2,4\!:\!1),
(3\!:\!2,4\!:\!1)
\}\!\}.
\]

### `K4` multiplicity packet

A root belongs to all three triangles through that root and to all three unoriented Hamiltonian four-cycles of `K4`. Hence every root has

\[
\mu(3)=3,\qquad \mu(4)=3,
\]

so

\[
\mathcal M(K_4)
=
\{\!\{(3\!:\!3,4\!:\!3)^\times4\}\!\}.
\]

The packets differ.

### Injectivity and representability theorem on the declared smallest class

**Theorem.** `M` is injective on `U_BR4`. A formal anonymous multiplicity packet is realizable by a state of `U_BR4` iff it equals exactly one of the two packets displayed above.

**Proof.** `U_BR4` has exactly the two isomorphism types `D` and `K4`, and their packets are distinct. This proves injectivity. Necessity of the two listed packet forms follows from the classification. Conversely, `D` and `K4` explicitly realize the respective packets. ∎

Thus separation and representability are both exact at this bounded first-branching scope. In particular, every other syntactically written multiplicity packet is a virtual sector relative to `U_BR4`.

This is a strict refinement of the weaker support packet: forgetting multiplicities maps both exact packets to the same four copies of `{3,4}`.

## 5. Degree-controlled support collision on ten cubic Cells

The four-Cell collision differs in native degrees, so a local degree readout would split it. That does not rescue the path-return **support** interface itself. The following second witness keeps every Cell degree equal to three.

Let `H` have edge set

```text
01 03 08 14 18 24 26 29 35 39 47 57 58 67 69
```

and let `G` have edge set

```text
03 05 06 12 13 16 26 29 34 45 48 57 78 79 89
```

on vertex set `{0,...,9}`.

Both are connected simple cubic graphs.

The checker verifies that their anonymous support packets are identical. Written by multiplicity of root-support type, both have:

- four roots with support `{3,4,5,6,7,8,9,10}`;
- two roots with support `{3,5,6,7,8,9,10}`;
- four roots with support `{4,5,6,7,8,9,10}`.

Their anonymous minimum-return packets also agree:

\[
\{\!\{3,3,3,3,3,3,4,4,4,4\}\!\}.
\]

Both contain exactly two triangles. However,

\[
\#C_4(H)=2,
\qquad
\#C_4(G)=3.
\]

The number of simple four-cycles is an isomorphism invariant, so `H` and `G` are nonisomorphic.

It follows that set-valued return support remains noninjective even after native degree is fixed uniformly at three.

Moreover the total number of four-cycles satisfies

\[
4\,#C_4(X)=\sum_x\mu_X(x,4),
\]

because each simple four-cycle is incident to exactly four roots. Therefore the different `C4` counts force

\[
\mathcal M(H)\ne\mathcal M(G).
\]

Return multiplicity separates this exact cubic support collision.

No minimality claim is made for ten Cells among all possible degree-controlled countermodels. The minimality proved in this return is the absolute branching-support lower bound `n=4`.

## 6. Lower-language necessity certificate

Suppose an attempted enhanced probe `F` factors only through the anonymous support packet:

\[
F=\bar F\circ\mathcal S.
\]

Since

\[
\mathcal S(H)=\mathcal S(G),
\]

we necessarily have

\[
F(H)=F(G).
\]

Therefore **no support-only refinement** can reconstruct the declared cubic witness pair.

The exact first datum exposed by the witness which is absent from support is multiplicity of equal-length return witnesses. In particular, `#C4=2` versus `#C4=3` is invisible after powerset collapse but visible before multiplicity erasure.

This passes the Q8 lowest-sufficient-abstraction gate:

- it stays in native path/return language;
- it adds integer counts, not Cell identities;
- it does not require a complete cycle basis as output;
- it does not require spectra, zeta functions, groupoids, descent, or a canonical graph labeling;
- its necessity is certified by an explicit equal-support countermodel.

The outcome is therefore a genuine lower-language failure measurement, not an escalation by vocabulary.

## 7. Separation versus representability audit

The task requires both sides to be tested.

### Weak scalar `rho_min`

- **Separation:** fails already on `D` versus `K4`.
- **Representability:** not promoted to a branching reconstruction interface; it is only a minimum of the legal support and therefore discards branch alternatives by construction.

### Powerset support packet `S`

- **Semantics:** canonical first repair of branching nondeterminism by reused T8 powerset semantics.
- **Separation:** fails on `D` versus `K4`, and still fails on the degree-controlled cubic pair `H` versus `G`.
- **Representability on `U_BR4`:** the exact realized support image is a singleton — four copies of `{3,4}` — whose fiber contains both isomorphism types. Thus formal existence at this bounded scope is trivial but reconstruction fails maximally within that fiber.

### Multiplicity packet `M`

- **Separation on `U_BR4`:** exact injectivity theorem proved above.
- **Representability on `U_BR4`:** exact two-packet image proved above.
- **Cubic stress:** separates the explicit `H/G` support collision.
- **Global subcubic completeness:** intentionally unresolved.

This is enough to classify failure exactly without manufacturing a success by moving to an almost-complete graph description.

## 8. Deterministic checker

Checker:

`research_checks/P000_PHILOSOPHY_FIRST_PATH_RETURN_BRANCHING_STRESS_CHECK_20260830.py`

It uses only the Python standard library and:

1. exhausts all 64 labeled simple graphs on four vertices;
2. filters the exact `U_BR4` definition;
3. verifies the seven labeled representatives / two isomorphism types;
4. enumerates simple primitive returns and checks the scalar/support collision;
5. checks the exact two-point multiplicity image;
6. verifies the explicit ten-Cell cubic witnesses, identical support/minimum packets, and `2` versus `3` simple four-cycles.

Deterministic run:

```text
PASS P000_Q13_BRANCHING_PATH_RETURN; checks=22; B4_labeled=7; B4_iso_types=2; scalar_and_set_packet_collision=YES; B4_multiplicity_image=2; cubic10_set_support_collision=YES; cubic10_C4_counts=2_vs_3
```

The exhaustive component supports only the stated four-Cell theorem. The ten-Cell pair is an exact witness check. Universal claims in this return are the short structural proofs above, not extrapolations from enumeration.

## 9. Hard-target disposition

`P000_PATH_RETURN_BRANCHING_RECONSTRUCTION_OR_FAILURE_EXACTLY_CLASSIFIED` is satisfied by the negative branch with a bounded positive repair theorem:

- `FIRST_BRANCHING_COUNTERMODEL_EXACTLY_CLASSIFIED` — **YES**;
- `Q9_PERIOD_INTERFACE_NOT_WELL_DEFINED_OUTSIDE_DEGREE_TWO` — **YES**, as a general single-valued scalar continuation into the first branching envelope;
- `BRANCHING_PATH_RETURN_JOINT_RECONSTRUCTION_PROVED_ON_DECLARED_CLASS` — **YES only for the explicitly frozen smallest class `U_BR4` after multiplicity refinement**, not for the full max-degree-three envelope.

The scientific boundary is sharp:

\[
\text{degree-two deterministic period}
\longrightarrow
\text{branching set-valued support}
\longrightarrow
\text{support collision}
\longrightarrow
\text{return multiplicity as first exact missing datum}.
\]

Q9 completeness is therefore not yet evidence for a universal path-return tomography theorem; its exact inverse relies essentially on the degree-two cycle decomposition. At first branching, path-return remains useful, but the scalar-period interface itself does not survive unchanged.

## 10. Residue and next research question

The unresolved residue is intentionally narrow:

> On what first nontrivial structural subfamily beyond `U_BR4` is the anonymous return-multiplicity packet reconstructive and exactly representable, and where does its first equal-multiplicity collision occur?

That question should be tested before importing stronger classical graph spectroscopy or higher categorical gluing machinery. A successor, if published, should freeze such a subfamily and search for multiplicity collisions first.

No Working Truth, Foundation, canonical ontology, or P000 primitive mutation is requested by this return. No novelty claim is made for classical cycle counting or finite graph enumeration. The project-specific contribution is the exact native-interface boundary and its lower-language failure certificate.
