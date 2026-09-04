# Post-#1161 free research — the S4 diamond-memory bundle and section-independent scalar AGM transport

Status: `FREE_RESEARCH_SUCCESSOR_RESULT / S4-NATURAL MEMORY BUNDLE + ORIENTATION-SECTION NO-GO / NOT WORKING_TRUTH / NOT FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-G61R8`
Predecessors:
- `research_notes/FREE_RESEARCH_POST1161_BRANCH_MEMORY_LATTICE_20260904.md`
- `research_notes/FREE_RESEARCH_POST1161_HIDDEN_FIBER_CAPACITY_AND_INTERFACE_INDEPENDENCE_20260904.md`
Consumed current P000/FCC results:
- Gen12 existential framed Full-Cell faithful `S4` common-model lift;
- Gen13 lift/kernel/section classification;
- Gen18 full-lift-fiber local-to-global transparency criterion.

## 0. Question

The AGM first-return reconstruction has two memory layers:

- branch-resolved memory `M_D = Z^D / Z1` on a two-witness commuting-diamond fiber `D`;
- scalar predictive memory `d=|z| in N_0`, the swap-orbit quotient of `M_D`.

The P000/FCC line has independently established a framed Full-Cell `S4` action in one common model and has shown that lift sections can be nonunique or nonsplit when hidden kernels are present.

The present question is narrower and does not overlap active Gen19 PF10/connection moduli work:

> Does transport of the local diamond memory require a canonical global orientation/section, or does the scalar AGM observer descend naturally through the `S4` action and hidden lift ambiguity?

The answer splits exactly:

\[
\boxed{\text{branch-resolved global orientation section: impossible}}
\]

but

\[
\boxed{\text{scalar imbalance / first-return AGM observer: canonical and section-independent}.}
\]

## 1. Twelve geometric diamonds in the K4/FCC star atlas

Use the frozen K4 presentation of the six FCC line families. A three-line star is the set of the three K4 edges incident to one vertex.

Inside one star, a commuting diamond uses a pair of distinct active line families. Therefore a diamond position is exactly an unordered pair of incident K4 edges, equivalently

\[
\Delta=(v,\{u,w\}),
\]

where `v,u,w` are three distinct K4 vertices and `v` is the common star center.

There are

\[
4\binom32=12
\]

such unordered diamond positions. Let the set be `D_12`.

The carrier `S4` action on K4 vertices acts transitively on `D_12`.

## 2. Ordered axis pair = one of the two concrete diamond witnesses

For a fixed unordered diamond

\[
\Delta=(v,\{u,w\}),
\]

the two concrete commuting path witnesses are represented by the two ordered active-axis words

\[
X_{vu}X_{vw},
\qquad
X_{vw}X_{vu}.
\]

Thus choosing one of the two concrete witnesses is equivalent to ordering the two leaves:

\[
\widetilde\Delta=(v,u,w)
\quad\text{or}\quad
(v,w,u).
\]

The total ordered-witness set has

\[
4\cdot3\cdot2=24
\]

elements. Call it `D_24`.

The `S4` action on `D_24` is regular: it is transitive and has trivial stabilizer. Hence

\[
\boxed{D_{24}\cong S_4}
\]

as a left `S4`-set.

For an unordered diamond, the stabilizer has order two. Its nontrivial element fixes the common star center and exchanges the two leaves; consequently it exchanges the two concrete path witnesses.

Therefore

\[
\boxed{D_{12}\cong S_4/C_2,}
\]

and

\[
D_{24}\to D_{12}
\]

is the natural two-witness orientation cover.

## 3. No S4-equivariant global witness orientation

Suppose an `S4`-equivariant section

\[
s:D_{12}\to D_{24}
\]

existed.

Fix a diamond `Delta` and let `h` be the nontrivial element of its `C2` stabilizer. Equivariance would require

\[
h\cdot s(\Delta)=s(h\cdot\Delta)=s(\Delta).
\]

But `h` exchanges the two ordered witness lifts over `Delta`, so it fixes neither one. Contradiction.

Hence

\[
\boxed{\text{NO }S_4\text{-EQUIVARIANT GLOBAL ORIENTATION SECTION}.}
\]

The task-local checker exhausts all

\[
2^{12}=4096
\]

possible choices of one witness over each diamond and finds zero equivariant sections.

This is a genuine canonical-choice obstruction. A global naming of the two branch witnesses as `A/B`, `positive/negative`, or `first/second` cannot be made `S4`-equivariantly from the diamond geometry alone.

## 4. The branch-memory lattice is the associated sign local system

For one diamond fiber `D={two witnesses}`, the previously derived branch memory is

\[
M_D=\mathbb Z^D/\mathbb Z\mathbf1.
\]

Its nontrivial witness swap acts by inversion. Relative to a temporary coordinate, this is

\[
z\mapsto-z.
\]

Thus the branch-resolved memory over the 12 diamond positions is naturally the associated rank-one sign local system

\[
\boxed{
\mathcal L
=
S_4\times_{C_2}\mathbb Z_{\rm sgn}
\longrightarrow
S_4/C_2.
}
\]

No global positive generator is selected.

For any fixed magnitude `d>0`, the two signed values over each of the 12 diamonds give `24` total states. The checker verifies that these `24` states form one regular `S4` orbit.

So the failure of a global orientation section is not failure of the signed memory object itself; it is exactly the statement that the rank-one local system is not canonically trivialized.

## 5. The scalar counter is the trivial orbit bundle

The scalar AGM observer retains only the witness-swap orbit

\[
d=|z|\in\mathbb N_0.
\]

The stabilizer `C2` acts trivially on `N_0`, so the associated orbit bundle is

\[
\boxed{
\mathcal Q
=
S_4\times_{C_2}\mathbb N_0
\cong
(S_4/C_2)\times\mathbb N_0.
}
\]

Thus the scalar counter bundle **is canonically trivial**, even though the signed lattice bundle is not.

Equivalently, for any bijection of two-witness fibers

\[
\phi:D\to D',
\]

the induced map on branch memory satisfies

\[
\boxed{
d_{D'}(\phi_*m)=d_D(m).}
\]

A temporary coordinate sees the only two possibilities as

\[
z\mapsto z
\quad\text{or}\quad
z\mapsto-z,
\]

and both preserve `|z|`.

## 6. Section-independence under hidden structural kernels

Gen13 shows that a structural readout

\[
q:\widetilde G\to S_4
\]

may have nontrivial hidden kernel and may admit several, one, or no homomorphic sections depending on the model.

For the scalar AGM counter, section nonuniqueness is not an obstruction provided a structural lift preserves the declared two-witness diamond object. Any two lifts over the same visible `S4` motion can differ on the local two-element witness fiber only by a witness-fiber bijection. The scalar counter is invariant under the entire `S2` of that fiber.

Hence every such hidden-kernel action is transparent to `d=|z|`:

\[
\boxed{
\text{hidden lift difference may flip signed memory, but cannot change scalar }d.
}
\]

This is exactly the kind of full-lift-fiber transparency demanded by the accepted Gen18 local-to-global criterion. One chosen generator section is unnecessary for the scalar observer: the full lift fiber preserves the counter automatically at the two-witness level.

Boundary: this statement is conditional on the lift preserving/transferring the retained diamond witness fiber as a two-element object. It does not claim that arbitrary opaque hidden state acts on undeclared path data.

## 7. S4-natural first-return mass and chord loss

The first-balance predicate and all first-return counts depend only on equal multiplicity of the two witnesses. They are invariant under every bijection of the witness fiber.

Therefore the coefficients

\[
f_n=\frac{C_{n-1}}{2^{2n-1}}
\]

and the return generating mass

\[
F(s)=\sum_{n\ge1}f_ns^{2n}
\]

are the same in every transported diamond fiber.

The post-#1161 identity

\[
F(s)=2\ell
\]

therefore defines an `S4`-natural scalar chord-loss readout. The exact AGM shape map

\[
s^+=\frac{F(s)}{2-F(s)}
\]

is also invariant under all branch-witness relabelings and under noncanonical choice of signed local trivialization.

Freeze:

\[
\boxed{
\text{SCALAR AGM FIRST-RETURN/CHORD RG DOES NOT REQUIRE A CANONICAL }S_4\text{ SECTION}.}
\]

What fails canonically is only the extra signed statement “which concrete witness is currently in excess”.

## 8. Relative minimality of the equivariant Markov augmentation

For one fixed diamond, the all-horizon unlabeled first-return observer has coarsest predictive state `d in N_0`; distinct `d` have different earliest return times.

Therefore, relative to the given 12-diamond geometric base, the fiber `N_0` is minimal for exact scalar first-return prediction. Transport by `S4` does not enlarge it because all fibers are related by bijections preserving `d`.

The minimal scalar predictive augmentation over the diamond orbit is therefore

\[
\boxed{
D_{12}\times\mathbb N_0.
}
\]

The branch-resolved minimal augmentation is the nontrivial sign local system `L`, not a globally oriented product `D_12 x Z`.

This separates two notions that should not be conflated:

- minimal **predictive information** for the scalar AGM observer;
- global **orientation trivialization** of branch-resolved history.

Only the second is obstructed by the local `C2` stabilizer.

## 9. Native-semantics strength

The framed Full-Cell `S4` geometry consumed here is an accepted downstream/existential model, not a theorem that bare P000 canonically forces `S4`.

The branch-memory lattice/counter remains history-derived N1 state. This result proves equivariance/naturality of that N1 state over the derived geometric action; it does not reclassify the counter as an instantaneous G0/N0 spatial primitive.

Strongest justified architecture:

\[
\boxed{
\text{framed Full-Cell }S_4\text{ geometry}
\to
\text{N1 sign memory local system }\mathcal L
\to
\text{canonical orbit counter }D_{12}\times\mathbb N_0
\to
\text{N2 first-return/chord AGM RG}.}
\]

Thus the earlier current-cell collision no-go remains valid for bare instantaneous Cell state, while the section/canonicality problem is now resolved for the scalar derived observer.

## 10. Executable audit

Task-local checker:

`scripts/check_free_research_agm_s4_diamond_memory_bundle.py`

It verifies:

- unordered diamond count `12`;
- ordered concrete-witness count `24`;
- unordered stabilizer order `2`;
- ordered stabilizer order `1`;
- exhaustive equivariant orientation-section count `0` over all `4096` sections;
- fixed nonzero signed-memory orbit size `24`;
- fixed scalar-memory diamond orbit size `12`;
- `514` exact identity/swap naturality checks for `|z|` over `z=-128..128`.

The file was fetched back from `main`; the exact checker logic was replayed and produced the frozen expected output.

## 11. Tool / prior-art boundary

The orbit-stabilizer and equivariant-section obstruction are standard finite group-action mathematics. Existing Enterprise finite-symmetry machinery is reused conceptually; no new global tool family is claimed.

The project-specific contribution is the exact identification of:

1. the 12 FCC/K4 commuting-diamond positions as `S4/C2`;
2. the 24 concrete diamond witnesses as the regular `S4` cover;
3. the post-#1161 branch-memory lattice as its associated sign local system;
4. the AGM scalar counter as the section-independent trivial orbit bundle.

No historical novelty claim is made for associated bundles, sign representations, or homogeneous-space sections.

## 12. Next smallest independent question

The active P000 Gen19 task studies PF10/connection moduli and should not be duplicated here.

For the AGM successor itself, the next independent mathematical question is now narrower:

> Can the **RG update itself**, not only its scalar observer, be expressed as an `S4`-equivariant finite-state skew-product on the diamond-counter bundle, with finite return-depth truncations composing naturally under Cell/star transport and with an exact observer-relative quotient law?

A positive result would complete the derived equivariant Markov architecture. It would still not promote the counter to bare P000 G0 state, but it would remove the remaining dynamical rather than representational ambiguity.
