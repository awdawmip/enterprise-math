# P019 — Directional Focusing, Supplement 08: What Survives, Automorphism Orbits, and an Anisotropy Gate

Status: `ACTIVE RESEARCH NOTE / DIRECTIONAL GATE`
Depends on: P012 intrinsic graph geometry; P019 Supplements 03, 05, 06, 07
Discipline: do not name any quantity in this note physical shear, Ricci curvature, or gravitational clock rate without an additional derivation.

## 1. Retention audit of the new P019 machinery

The previous stages introduced several quantities. They do not deserve equal foundational status.

### Core — retain as structural primitives/primary derived structure

1. `phase / causal boundary`: needed to distinguish causal side and exact boundary structure;
2. `F(A), Xi(A)`: the distinct future section and its exact cardinality change;
3. `B(A), C(A)` with `Xi=B-C`: the minimal branching-versus-focusing decomposition;
4. the full `J_k^out` spectrum: necessary because `C` is not a complete local focusing invariant from three sources onward;
5. P012 graph automorphisms: the correct intrinsic symmetry language for any attempt to define directions without hidden Euclidean coordinates.

### Useful diagnostics — retain, but do not build the ontology around them

- `R_t`: fraction-free ordering of normalized expansion change;
- `H=J2-C`: exact witness for multiplicity at least three;
- `Q=2J2-C`: concentration of multiplicity excess;
- submodularity/diminishing returns: a valuable theorem about `Xi`, but established coverage mathematics rather than a new primitive.

### Research candidates — keep explicitly demoted

- `K_branch`: exact algebraically as `B`, but its interpretation as a clock is unproved;
- any identification of `H`, `Q`, or a directional witness with continuum shear/curvature.

This retention audit prevents P019 from turning every convenient statistic into a new foundational object.

## 2. Why a direction cannot be imported from coordinates

P012 already established that intrinsic geometry begins with primitive adjacency and that exact symmetries are graph automorphisms.

For a finite directed graph `G=(V,E)` and current section `A`, let

`Aut(G;A)`

be the automorphisms that preserve the directed edge relation and preserve `A` setwise.

The outgoing primitive incidences are

`I_A={(v,w) in E : v in A}`.

Define two incidences to have the same **intrinsic direction class at A** when they lie in the same orbit of the action of `Aut(G;A)` on `I_A`.

No Euclidean angle, coordinate axis, or real-valued tangent vector is used.

## 3. P019-DIR-T01 — Orbit direction classes are automorphism-covariant

Status: `PROVED BY DEFINITION / GROUP ACTION`.

The orbit partition of `I_A` is invariant under every element of `Aut(G;A)`. Relabelling the finite graph by an isomorphism transports the whole partition rather than changing the mathematical directional content.

Therefore an observable defined only from the unordered orbit data is graph-isomorphism covariant.

## 4. P019-DIR-N01 — Direction-resolution no-go on transitive structures

Status: `PROVED NECESSITY RESULT`.

If `Aut(G;A)` acts transitively on `I_A`, there is exactly one intrinsic direction orbit.

Consequently no automorphism-covariant observable built solely from the unmarked pair `(G,A)` can distinguish two outgoing incidences inside that orbit.

This is not a failure of the method. It is a resolution theorem:

> symmetry-equivalent directions are not intrinsically distinguishable without additional structure.

In particular, a one-orbit result must not be reported as proof of physical isotropy. It only says the chosen intrinsic structure contains no finer direction information.

This also shows why a bare highly symmetric graph cannot generate a shear-like degree of freedom by notation alone.

## 5. The required extra structure is already available in P019

A black-hole/focusing problem is not normally an unmarked graph. P019 already carries distinguished structure such as:

- the current cross-section `A`;
- causal phase labels;
- zero vertices and sign-crossing boundary edges;
- a horizon/boundary complex.

The correct procedure is therefore to take the automorphism group that preserves the physically/mathematically justified marked structure, not to import an arbitrary external axis.

Adding justified marks can refine the automorphism group and hence refine incidence orbits.

## 6. Direction-channel focusing data

For one intrinsic incidence orbit `D subset I_A`, let

`m_D(w)=# {(v,w) in D}`.

Define

`E_D=|D|`,

`T_D=# {w:m_D(w)>0}`,

`C_D=E_D-T_D=sum_w(m_D(w)-1)`,

and

`J_{k,D}=sum_w binom(m_D(w),k)`.

Thus every intrinsic direction channel inherits the same integer focusing calculus as the total section.

These are not independent new primitives. They are the existing `C` and `J_k` calculus restricted to automorphism-defined incidence orbits.

## 7. P019-DIR-T02 — Pair focusing splits into within-direction and cross-direction terms

Status: `PROVED`.

For disjoint direction channels `D_i`, define

`X_ij=sum_w m_i(w)m_j(w)` for `i<j`.

Then total pair collision satisfies

`J2(total)=sum_i J2(D_i)+sum_{i<j} X_ij`.

This is exact because every colliding incidence pair is either drawn from one direction channel or from two different channels.

The cross term matters. Two individually collision-free directional channels may still focus into the same future targets entirely through cross-direction mixing.

Therefore a shear-like research program cannot inspect each channel independently and ignore cross-channel overlap.

## 8. P019-DIR-T03 — Fraction-free directional collision-rate anisotropy witness

Status: `PROVED INTEGER IDENTITY / PHYSICAL INTERPRETATION OPEN`.

For nonempty direction channels let

`E_i=|D_i|`, `C_i=C(D_i)`.

To compare the rational collision rates `C_i/E_i` without storing fractions, define

`A_C=sum_{i<j}(E_j*C_i-E_i*C_j)^2`.

Then

`A_C>=0`,

and

`A_C=0`

if and only if all resolved direction channels have equal collision rate.

This quantity is invariant under reordering the direction channels and uses only integers.

It is named only a **directional collision-rate anisotropy witness**.

It is not yet physical shear.

### Resolution caveat

If there is only one direction orbit, `A_C=0` vacuously. Therefore

`A_C=0`

means isotropy only **at the directional resolution actually present in the marked graph structure**.

## 9. Small exact example

Let the current section be `{a,b}` with future states `{x,y,z}` and edges

`a->x`, `b->y`, `a->z`, `b->z`.

The section-preserving graph symmetry swaps

`a<->b`, `x<->y`

and fixes `z`.

Hence there are two intrinsic incidence orbits:

`D_private={a->x,b->y}`,

`D_common={a->z,b->z}`.

Their data are

- private channel: `E=2`, `C=0`;
- common channel: `E=2`, `C=1`.

Thus

`A_C=(2*0-2*1)^2=4`.

No coordinate direction was inserted. The distinction arises because the causal graph itself distinguishes private versus common-future incidence structure.

## 10. What this stage changes in the black-hole route

The previous plan said “construct directional overlap and then compare with shear.” Stage 08 sharpens that statement.

The correct sequence is:

`primitive marked causal structure`

`-> section/phase/boundary-preserving automorphism group`

`-> incidence direction orbits`

`-> per-orbit J_k and cross-orbit overlap`

`-> fraction-free anisotropy witnesses`

`-> only then external comparison with shear-like focusing`.

This removes an important hidden assumption: a direction basis cannot be chosen arbitrarily and then called intrinsic.

## 11. Current retained P019 kernel

After the audit, the compact conceptual kernel is

`(marked primitive causal graph, A)`

`-> F(A)`

`-> Xi=B-C`

`-> full J_k overlap/fiber spectrum`

`-> automorphism-defined directional refinement when the structure supports it`.

`H`, `Q`, and `R` remain useful projections of this kernel.

`K_branch` remains a clock-calibration candidate only.

## 12. Next gate

The next useful step is not another scalar. It is to determine which **marking is mathematically justified by the horizon problem itself**.

Priority order:

1. use the existing causal phase / boundary complex as the mark;
2. compute the corresponding stabilizer refinement and directional channels;
3. test whether horizon-crossing versus horizon-tangent channels emerge without coordinates;
4. only if such channels emerge, study whether their anisotropy evolution has a structural correspondence with continuum shear;
5. separately keep the clock bridge as a no-go/derived-observable question.

If phase/boundary marking still leaves a transitive one-orbit structure, P019 should accept the no-go rather than invent a direction axis.

Executable reference layer:

- `src/enterprise_math/directional_focusing.py`
- `tests/test_directional_focusing.py`
