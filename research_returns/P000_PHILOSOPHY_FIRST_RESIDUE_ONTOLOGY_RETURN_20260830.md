# P000 Philosophy-First Q5 — Kernel / Relation Residue Ontology Return

Task: `RS-P000-PHILOSOPHY-FIRST-RESIDUE-ONTOLOGY`  
Publication: `TP2-9A770689001BF32EB9D0`  
Researcher: `EM-P000Q5-8F4C2D`  
Execution branch: `research/p000-philosophy-residue-ontology-em-p000q5-8f4c2d`  
Hard target: `P000_KERNEL_AND_RELATION_RESIDUE_ONTOLOGY_EXACTLY_CLASSIFIED`

## Terminal verdict

`SUCCESS / NONTRIVIAL_RESIDUE_INVARIANT_CLASSIFIED / MINIMAL_CENTRAL_C2_BENCHMARK_BOUNDARY`

The decisive distinction is not

`RELATION_RESIDUE_NONIDENTITY => ERROR`.

Already in the smallest possible nontrivial-kernel extensions of the carrier `S4`, a nonidentity residue can have two fundamentally different meanings:

1. it can be a **presentation/lift artifact** that disappears after changing representatives while the extension remains split; or
2. it can be a **forced enriched invariant** whose lift orbit never contains identity and therefore obstructs a homomorphic section.

Two exact order-48 comparison models establish the boundary:

- `E_split = S4 x C2`;
- `E_twist = GL(2,F3)` acting on the eight nonzero vectors of `F3^2`, with the projective readout on `P^1(F3)` giving `S4` and kernel `{+I,-I}`.

Both have quotient/readout `S4`, both have central kernel `C2`, and 48 is minimal because any nontrivial kernel over a 24-element quotient has order at least `24*2=48`. Yet their relation-residue ontology differs sharply.

The strongest exact discriminator is the lift profile of a carrier 4-cycle:

- in `S4 x C2`, every 4-cycle has two lifts of order `4`: profile `{4,4}`;
- in `GL(2,3)`, every projective 4-cycle has two lifts of order `8`: profile `{8,8}`.

Equivalently, for every allowed lift of a frozen `(3,2,4)` generating pair in the second model,

\[
(AB)^4=-I\neq I.
\]

This is computed in the enriched group itself. No quotient of the hidden kernel is used to manufacture exact `S4` relations.

## 1. Frozen P000 boundary

This return keeps the accepted project separation intact:

- carrier `S4` is a readout, not the complete native P000 rotation group;
- hidden kernel state is not discarded;
- carrier vertices remain a different sort from native Cell identities;
- the order-48 models below are declared finite extension benchmarks, not claims that bare P000 is literally `S4 x C2` or `GL(2,3)`;
- the `GL(2,3)` benchmark is semantically enriched rather than a free label: `-I` reverses the oriented vector in each two-point fiber while acting trivially on its projective line.

The four projective lines of `F3^2` give four base points; their six unordered pairs carry the usual `S4` edge action, so this benchmark can be compared to the accepted six-axis carrier readout without identifying the base points with native Cells.

## 2. Residue orbit, not residue value, is the first invariant object

Let

\[
1\to K\to \widetilde G\overset q\to S_4\to 1
\]

be a declared extension benchmark, and let `a,b` be frozen carrier generators satisfying

\[
a^3=b^2=(ab)^4=1.
\]

For lifts `A,B` define

\[
z_a=A^3,\qquad z_b=B^2,\qquad z_{ab}=(AB)^4\in K.
\]

A single tuple `(z_a,z_b,z_ab)` is not automatically an invariant. The exact object to inspect first is its **fixed-readout lift orbit**

\[
\mathcal O(a,b)=
\{(A'^3,B'^2,(A'B')^4):q(A')=a,\ q(B')=b\}\subseteq K^3,
\]

and then its saturation under the declared frame/gauge conjugations.

This definition does not collapse `K`. It records how much of the relation defect survives all allowed representative changes.

Two useful quotient-free flags are:

- `REMOVABLE(w)`: identity occurs in the corresponding residue projection of `O(a,b)`;
- `FORCED_NONTRIVIAL(w)`: that projection contains no identity.

The second flag can be an obstruction to an exact section.

## 3. Theorem A — central lift-change law

Assume `K` is central. Every other lift is

\[
A'=uA,\qquad B'=vB,\qquad u,v\in K.
\]

Then

\[
z'_a=u^3z_a,
\]

\[
z'_b=v^2z_b,
\]

and

\[
z'_{ab}=(uv)^4z_{ab}.
\]

**Proof.** Centrality lets `u,v` commute through `A,B`; expand each relation word and collect the kernel factors. ∎

### Central `C2` corollary

For `K=C2={1,k}`,

\[
u^3=u,\qquad v^2=1,\qquad (uv)^4=1.
\]

Therefore:

- `z_a` is lift-covariant and can toggle under `A -> kA`;
- `z_b` is independent of lift choice;
- `z_ab` is independent of lift choice.

Under simultaneous conjugation, central residues remain unchanged. Thus in this smallest kernel class, `z_b` and `z_ab` can already be true enriched invariants, while `z_a` need not be.

This is the first exact ontology split.

## 4. Model S — split signed-frame fiber `S4 x C2`

Take

\[
E_{split}=S_4\times C_2,
\qquad q(\sigma,\epsilon)=\sigma.
\]

Interpret the kernel generator as the deck transformation of a signed two-state frame fiber over each of four carrier points. It changes hidden sign/frame parity while leaving the carrier point and six-edge readout unchanged.

Choose an abstract frozen pair

\[
a=(1\ 2\ 3),\qquad b=(3\ 4),
\]

so `ab` is a 4-cycle. All lifts are

\[
A_\epsilon=(a,\epsilon),\qquad B_\delta=(b,\delta),
\qquad \epsilon,\delta\in C_2.
\]

Exact residues are

\[
A_\epsilon^3=k^\epsilon,
\qquad
B_\delta^2=1,
\qquad
(A_\epsilon B_\delta)^4=1.
\]

Hence the four lift pairs have only two residue signatures:

- `(1,1,1)`;
- `(k,1,1)`.

The nontrivial `z_a=k` is **structurally legal** but not obstructive: changing `A` by the kernel element removes it. A homomorphic section exists explicitly,

\[
s(\sigma)=(\sigma,0).
\]

Therefore the correct classification of this nonzero residue is:

`PRESENTATION_ARTIFACT + GAUGE/LIFT_COVARIANT_DATA`,

not obstruction.

All six 4-cycles have lift-order profile `{4,4}`.

## 5. Model T — twisted oriented-line fiber `GL(2,3)`

Let

\[
E_{twist}=GL(2,\mathbf F_3).
\]

It acts faithfully on the eight nonzero vectors of `F3^2`. Forgetting orientation `v ~ -v` leaves the four projective lines of `P^1(F3)`. The induced projective action has order `24` and is `S4`; the exact kernel is

\[
K=\{I,-I\}\cong C_2.
\]

Thus the hidden element `-I` has concrete enriched meaning: it flips every oriented representative while fixing every projective base point and hence the carrier readout.

An explicit generator witness over `F3` is

\[
A=\begin{pmatrix}0&1\\2&2\end{pmatrix},
\qquad
B=\begin{pmatrix}1&0\\0&2\end{pmatrix}.
\]

Direct computation gives

\[
A^3=I,
\qquad
B^2=I,
\qquad
(AB)^4=-I,
\]

with

\[
\operatorname{ord}(A)=3,
\qquad
\operatorname{ord}(B)=2,
\qquad
\operatorname{ord}(AB)=8.
\]

Projectively, `q(A)` has order `3`, `q(B)` has order `2`, `q(AB)` has order `4`, and they generate the full 24-element image.

### Exhaustive result

The deterministic checker does not rely on this one witness. It enumerates:

- all 48 matrices of `GL(2,3)`;
- all 24 projective `(3,2,4)` generating pairs of the `S4` image;
- both lifts of each generator, hence `24*4=96` lifted pairs.

Across all 96 lifted pairs, the only signatures are

\[
(I,I,-I)\quad\text{and}\quad(-I,I,-I),
\]

48 times each.

Therefore:

- `z_a` is still lift-dependent and removable;
- `z_b=I` is forced trivial;
- `z_ab=-I` is forced nontrivial.

In particular the projection of `O(a,b)` onto the third coordinate is exactly `{-I}`.

So `z_ab` is simultaneously:

`ENRICHED_INVARIANT + OBSTRUCTION_CLASS`.

## 6. Theorem B — forced `(AB)^4=-I` forbids a homomorphic section

Suppose a homomorphic section

\[
s:S_4\to GL(2,3)
\]

existed. Put `A=s(a)` and `B=s(b)`. Since `s` is a homomorphism and `(ab)^4=1` in `S4`, one must have

\[
(AB)^4=s((ab)^4)=I.
\]

But exhaustive lift enumeration proves `(AB)^4=-I` for every possible lift pair over every generating pair of the frozen presentation type. Contradiction.

Hence the projective extension has no homomorphic section.

The obstruction is not inferred from a name such as “non-split”; it is witnessed directly by an enriched relation word that cannot be made identity under any allowed lift change.

## 7. Theorem C — 4-cycle lift-order profile is a stronger quotient-free invariant

For a quotient 4-cycle `c`, define

\[
\Lambda(c)=\{\!\{\operatorname{ord}(C):q(C)=c\}\!\}.
\]

This is computed on the actual enriched fiber over `c`.

The checker proves:

\[
\Lambda_{split}(c)=\{4,4\}
\]

for every one of the six carrier 4-cycles, while

\[
\Lambda_{GL(2,3)}(c)=\{8,8\}
\]

for every projective 4-cycle.

Thus two minimal order-48 models with the same quotient `S4` and same kernel size are separated before any kernel quotienting. The residue is recording **order doubling in hidden enriched state**.

This gives a practical rule for future P000 models:

`DO_NOT_ONLY_TEST_WHETHER_A_RELATION_WORD_LANDS_IN_K; TEST_THE_ENTIRE_LIFT_ORBIT_AND_LIFT_ORDER_PROFILE.`

## 8. Ontology classification

| Datum | Split `S4 x C2` | `GL(2,3)` | Ontology |
|---|---|---|---|
| `z_a=A^3` | `1` or `k` | `I` or `-I` | `PRESENTATION_ARTIFACT / GAUGE_COVARIANT_DATA` |
| `z_b=B^2` | always `1` | always `I` | trivial stable datum |
| `z_ab=(AB)^4` | always `1` | always `-I` | split: trivial; twisted: `ENRICHED_INVARIANT + OBSTRUCTION_CLASS` |
| 4-cycle lift orders | `{4,4}` | `{8,8}` | quotient-free enriched invariant |
| homomorphic section | yes | no | split vs no-section |

The lesson is exact:

`NONIDENTITY_RESIDUE` by itself has no ontology.

Its ontology is determined by its **orbit under allowed equivalences** and by whether the identity relation can be realized somewhere in that orbit.

## 9. Noncentral-kernel boundary

The simple power law above is special to central kernels.

For general normal `K`, if

\[
\alpha_A(k)=AkA^{-1},
\]

then changing `A` to `uA` gives the twisted norm

\[
(uA)^3
=u\,\alpha_A(u)\,\alpha_A^2(u)\,A^3.
\]

Similarly,

\[
(vB)^2=v\,\alpha_B(v)\,B^2.
\]

The mixed word `(uA vB)^4` retains both conjugation actions and mixed transport terms. Therefore ordinary powers of kernel corrections no longer describe the whole orbit.

For noncentral/nonabelian kernels the correct primitive object is the **full factor-system / residue orbit with the conjugation action retained**, not three isolated kernel elements.

This is also the point where a “residue value” should be demoted from invariant to gauge-covariant data unless a stronger orbit statement is proved.

## 10. Exact boundary for ordinary `H^2`

Classical group cohomology is useful here only with its hypotheses stated.

- If `K=A` is abelian and the induced `S4`-action on `A` is fixed, equivalence classes of extensions inducing that action are classified by ordinary `H^2(S4,A)`.
- If the action is trivial, these are central extensions.
- The zero class corresponds to a split extension / homomorphic section.
- For nonabelian `K`, ordinary abelian group cohomology `H^2(S4,K)` is not the correct object. One must retain nonabelian factor-set data and at least the induced outer action; center-valued cohomology enters only after additional hypotheses/choices.

This return does **not** claim cohomology as a P000 novelty and does not compute a new cohomology group. It derives the finite residue ontology directly and uses classical extension theory only to name the boundary afterward.

External checks used only for prior-art orientation:

- GroupNames lists the central extensions of `S4` by `C2`, including the split product and the nonsplit `GL(2,3)=C2._3 S4`, and independently records `Z(GL(2,3))=C2`, `GL(2,3)/Z=S4`.
- Etingof et al., *Introduction to Representation Theory / homological algebra notes*, Example 1.7.2, records the standard statement that `H^2(G,A)` classifies abelian extensions with fixed action, central extensions in the trivial-action case.

No novelty claim is made for these classical facts.

## 11. P000 consequence

At the current strict bridge, the safe upgrade is not “kernel residue should vanish.” It is:

1. record the enriched-to-carrier readout `q` and actual kernel action;
2. enumerate the full lift orbit of the frozen relations;
3. separate removable coordinates from forced nontrivial orbit data;
4. retain lift-order profiles and other enriched fiber invariants;
5. call a residue an obstruction only when identity is excluded under every allowed equivalence relevant to the desired section/lift.

This preserves exactly the possibility the philosophy-first task was designed to protect: a “defect” can be the first visible coordinate of hidden geometric state.

The `GL(2,3)` benchmark supplies an exact finite mechanism: the carrier sees a 4-cycle, while the enriched object sees an order-8 motion whose fourth power is a hidden sign reversal.

That is a concrete model of

`VISIBLE_RELATION_CLOSURE + HIDDEN_STATE_MONODROMY`.

It should be compared with P000 connection/holonomy data in a successor, but it is **not yet promoted** to a native P000 law.

## 12. Deterministic checker

Checker:

`research_checks/P000_PHILOSOPHY_FIRST_RESIDUE_ONTOLOGY_CHECK_20260830.py`

It verifies with no external package:

- all 48 elements of `GL(2,3)`;
- the projective action on four lines and exact kernel `{I,-I}`;
- 24 quotient `(3,2,4)` generating pairs;
- all 96 lifted generator pairs;
- exact residue counts `48*(I,I,-I)+48*(-I,I,-I)`;
- exact split-model counts `48*(0,0,0)+48*(1,0,0)`;
- split lift order signatures `(3,2,4)` / `(6,2,4)`;
- twisted lift order signatures `(3,2,8)` / `(6,2,8)`;
- all six 4-cycle profiles `{4,4}` versus `{8,8}`;
- order-48 minimality for a nontrivial kernel over `S4`.

Executed status:

`PASS / NONTRIVIAL_RESIDUE_INVARIANT_CLASSIFIED_ON_MINIMAL_CENTRAL_C2_EXTENSION_BENCHMARKS`.

## 13. Control-plane recommendation

Driver review should freeze the following result at the declared benchmark scope:

`MINIMAL_CENTRAL_C2_RESIDUE_ONTOLOGY_CLASSIFIED`.

Recommended successor, only if justified:

`P000_NONCENTRAL_KERNEL_RESIDUE_ORBIT_AND_HOLONOMY_COUPLING`

with three hard requirements:

1. kernel must act on actual Cell/PF-10/frame/connection state, not an untyped extra label;
2. enumerate twisted residue orbits under lift changes and gauge conjugation;
3. test whether a forced residue coincides with an independently measurable P000 holonomy/transport invariant.

Do not jump directly to “nonabelian cohomology” before such a native finite model forces it.

## Boundary / non-claims

- This does not classify every central extension of `S4` by `C2`; it classifies two minimal exact benchmarks plus the general central-`C2` lift-change law needed to distinguish artifact from obstruction.
- This does not prove that bare P000 has a hidden `C2`, `GL(2,3)`, or binary-octahedral rotation group.
- This does not promote carrier `S4` to the full native rotation group.
- This does not identify projective-line base points with native Cells.
- This does not quotient away kernel state to force exact carrier relations.
- This does not claim classical extension/cohomology theory as new mathematics.

Result-ID: `RR-3B032EC1AFB283195BE9`  
Execution-Record-ID: `ER-1059957F60106ABC1A1E`
