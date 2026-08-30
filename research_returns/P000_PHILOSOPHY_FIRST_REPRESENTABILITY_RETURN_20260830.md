# P000 Philosophy-First Q6 — Observation Profile Representability / Virtual Cell Boundary Return

Task: `RS-P000-PHILOSOPHY-FIRST-REPRESENTABILITY`  
Publication: `TP2-99EFD9FD80BE4C6457AD`  
Researcher: `EM-P000Q6-C31A72`  
Execution branch: `research/p000-philosophy-representability-em-p000q6-c31a72`  
Hard target: `P000_OBSERVATION_PROFILE_REPRESENTABILITY_BOUNDARY_CLASSIFIED`

## Terminal verdict

`SUCCESS / NONREPRESENTABLE_PROFILE_EXACTLY_WITNESSED / REPRESENTABLE_IMAGE_EXACTLY_CLASSIFIED`

On the exact radius-one probe shadow frozen by Q2 for the declared finite simple 2-regular native-Cell class `U_2REG`, formal compatibility does **not** imply native realizability.

Write the radius-one count profile as

\[
\Phi(X)=(t,p),
\]

where `t` is the number of roots whose native `N_1` response is a rooted triangle and `p` is the number whose response is a rooted three-vertex path. All `SLICE`, `ROT`, and `PF10` data are the uniform Q2 decorations and therefore restrict to the same radius-zero local type.

The exact native image is

\[
\operatorname{Im}(\Phi)
=
\{(3a,p): a\ge 0,\ p=0\text{ or }p\ge4\}.
\]

Equivalently,

`REPRESENTABLE(t,p) <=> (t mod 3 = 0) AND (p = 0 OR p >= 4)`.

Thus the support-aware formal profile

\[
(t,p)=(0,3)
\]

is the smallest pure nonrepresentable profile: each of its three local responses is individually the Q2-legal rooted path type, and every retained local restriction agrees, but no three-Cell finite simple 2-regular graph realizes it. The unique such graph is `C3`, whose three roots all return the triangle type.

Combined with Q2, the restricted observation map is therefore **two-sided incomplete**:

1. it is not injective on actual states: `C8` and `C4 disjoint_union C4` both map to `(0,8)`;
2. it is not surjective onto the declared formal profile completion: `(0,3)` is formal but virtual.

This is the requested actual/virtual boundary at an exact finite scope.

## 1. Frozen scope inherited from Q2

Q2 froze a declared toy class `U_2REG` consisting of:

1. finitely many opaque native Cell identities;
2. a finite simple 2-regular native-adjacency graph;
3. the six tagged native axis types `E1,...,E6` at every Cell;
4. uniform accepted carrier star readouts;
5. uniform accepted carrier generators
   `a_xi=(E1 E2 E3)(E4 E6 E5)` and
   `b_xi=(E2 E4)(E3 E5)`;
6. one uniform opaque PF-10 local token;
7. typed radius-one native-neighborhood probe `N_1`.

The present task does not enlarge P000 or identify carrier readout with native identity. It reuses only this already-declared finite probe substrate.

Q2 proved that in this class every variable radius-one output is one of exactly two rooted graph types:

- `T`: rooted triangle, occurring precisely at roots in a `C3` component;
- `P`: rooted three-vertex path, occurring at roots in every cycle `C_k` with `k>=4`.

## 2. What “formal compatibility” means here

A formal profile at support size `n>=3` is the count vector

\[
F_{n,t}=(t,n-t).
\]

It is **restriction-compatible at the retained Q2 probe strength** when:

- each root is assigned one of the two legal `N_1` output types `T` or `P`;
- all `SLICE`, `ROT`, and `PF10` restrictions agree with the common frozen local decoration;
- every `N_1` type restricts to the same radius-zero decorated root type.

Crucially, this profile does **not** retain opaque overlap identities telling us that a neighbor appearing in one rooted ball is the same native Cell appearing in another rooted ball. Hence this is a pointwise/restriction-compatible completion, not full descent data.

That distinction is essential. The theorem below says exactly that the current restriction maps are too weak to force global gluing; it does not say a fully glued atlas would remain nonrepresentable.

## 3. Exact representability theorem

**Theorem.** A formal profile `(t,p)` is represented by some actual state in `U_2REG` if and only if

\[
t\equiv0\pmod 3
\quad\text{and}\quad
(p=0\text{ or }p\ge4).
\]

### Necessity

Every finite simple 2-regular graph is a disjoint union of cycles of length at least three.

A `C3` component contributes exactly three `T` roots. Therefore the total triangle-root count is

\[
t=3a
\]

for some `a>=0`.

Every cycle of length at least four contributes only `P` roots. If there is at least one such component, it contributes at least four roots; hence

\[
p=0\quad\text{or}\quad p\ge4.
\]

### Sufficiency

If `t=3a` and `p=0`, take the disjoint union of `a` copies of `C3`.

If `t=3a` and `p>=4`, take

\[
aC_3\ \sqcup\ C_p.
\]

The triangle components supply exactly `t` triangle-root responses, and `C_p` supplies exactly `p` path-root responses. Thus every vector satisfying the criterion has an explicit native realization.

So the criterion is complete, not merely a necessary obstruction.

## 4. The representability monoid

Under disjoint union, profile counts add. Therefore the exact native image is the additive monoid

\[
M=\{(3a,p): a\ge0,\ p=0\text{ or }p\ge4\}.
\]

A finite generating set is

\[
(3,0),(0,4),(0,5),(0,6),(0,7).
\]

Indeed, every integer `p>=4` is generated by `4,5,6,7`: values `4..7` are generators, and every larger value can repeatedly subtract four until one of these residues is reached.

This gives a concrete answer to the task’s “which formally compatible profiles are actual?” question: native profiles are not all of the ambient count lattice `N^2`; they occupy a strict arithmetic submonoid.

## 5. Exact obstruction certificate

Define

\[
\chi(t,p)
=
\bigl(t\bmod 3,\ s(p)\bigr),
\]

with

\[
s(p)=
\begin{cases}
p,&1\le p\le3,\\0,&p=0\text{ or }p\ge4.\end{cases}
\]

Then

\[
(t,p)\text{ is representable}
\iff
\chi(t,p)=(0,0).
\]

The two coordinates isolate two distinct global constraints:

1. `triangle-component integrality`: triangle roots must assemble in packets of three;
2. `nontriangle-cycle mass shortage`: a path-root sector cannot close into a simple 2-regular component with only one, two, or three roots.

Both constraints are invisible to the retained radius-zero restrictions of the local responses. They are therefore genuine local-to-global gluing obstructions at this probe strength.

## 6. Minimal virtual profile

Because every radius-one response in `U_2REG` contains three distinct native Cells, support-aware comparison begins at `n=3`.

At `n=3`, the pure profile

\[
F_{3,0}=(0,3)
\]

assigns the legal path response to all three roots. That rooted path occurs in actual models such as `C4`, so the local response itself is not malformed.

Nevertheless no actual three-Cell state realizes the triple: the only finite simple 2-regular graph on three vertices is `C3`, and its radius-one rooted ball is a triangle at every root.

Hence

`MINIMAL_PURE_VIRTUAL_PROFILE = (t=0,p=3)`.

The obstruction is not “a bad local object”; it is failure of the local objects to glue to a global native state.

## 7. Bounded profile space and image size

At fixed support size `n>=3`, the count-valued formal completion contains

\[
|\mathcal F_n|=n+1
\]

profiles `(t,n-t)`.

The representability theorem gives exactly

\[
|\operatorname{Im}(\Phi)_n|=\lfloor n/3\rfloor.
\]

Therefore the virtual sector has size

\[
|\mathcal V_n|
=n+1-\lfloor n/3\rfloor.
\]

This count is not a probability statement. It shows structurally that the formal completion is much larger than the native image even in this minimal count shadow.

## 8. Two-sided failure of the restricted probe map

The Q2 result and the present Q6 result fit together exactly.

### Noninjectivity — Q2

At `n=8`,

\[
C_8
\quad\text{and}\quad
C_4\sqcup C_4
\]

are nonisomorphic actual native-adjacency states but both have profile

\[
(0,8).
\]

The probe language forgets global gluing information.

### Nonsurjectivity — Q6

The formal profile `(0,3)` satisfies all retained local restriction rules but belongs to no actual state.

Thus the same restricted probe language simultaneously:

- identifies distinct native states;
- invents formal states that have no native realization.

In symbols, for the declared completion target,

`ACTUAL --Obs_1--> FORMAL_PROFILE`

is neither injective nor surjective.

This is stronger diagnostic information than either failure alone.

## 9. Does the virtual completion help?

Yes, but only if it remains explicitly typed as formal.

The virtual completion is useful as an **analysis ambient space**:

- equations can be solved before imposing global realizability;
- the representability obstruction becomes a separate exact predicate;
- counterexamples such as `(0,3)` expose which global constraint is missing;
- successor probes can be tested by asking whether they shrink the virtual sector or split noninjective fibers.

But the completion must not be interpreted as an enlargement of native ontology without a separate theorem. The safe rule is:

`FORMAL_PROFILE + REPRESENTABILITY_CERTIFICATE -> MAY_HAVE_NATIVE_SEMANTICS`.

Without the certificate:

`FORMAL_PROFILE != NATIVE_CELL_STATE`.

So virtual profiles increase reasoning convenience, not native existence.

## 10. Relation to classical representability language

The classical lens is only orientation. The Stacks Project defines a presheaf as a contravariant functor and a representable presheaf as one isomorphic to a functor of points `h_U`; representability requires the existence of an actual representing object. Yoneda then controls maps from representables and uniqueness of a representing object when one exists. It does not state that every formal presheaf is representable.

References:

- Stacks Project, Section 7.2, `Presheaves`: https://stacks.math.columbia.edu/tag/00V1
- Stacks Project, Section 4.3, `Opposite Categories and the Yoneda Lemma`: https://stacks.math.columbia.edu/tag/001L

The current theorem is not claimed as a new theorem about presheaf categories. It is a project-specific exact finite representability computation for the Q2 probe shadow.

## 11. Deterministic checker

Checker:

`research_checks/P000_PHILOSOPHY_FIRST_REPRESENTABILITY_CHECK_20260830.py`

It verifies:

1. accepted carrier relations `a^3=b^2=(ab)^4=1` on the six tagged axis types;
2. exhaustive cycle-partition enumeration for every `3<=n<=64`;
3. equality between the enumerated actual image and the closed-form representability criterion;
4. exact image cardinality `floor(n/3)` at each bounded size;
5. the obstruction certificate on every formal count profile in that range;
6. minimal pure virtual profile `(0,3)`;
7. Q2 noninjective fiber `(0,8)` with exactly the cycle partitions `(8)` and `(4,4)` through `n=8`;
8. finite generation of the nontriangle mass sector by `4,5,6,7` through mass `128`.

Executed output:

`PASS P000_REPRESENTABILITY_BOUNDARY; checks=2403; scope=U_2REG_P1; minimal_pure_virtual=(t=0,p=3); representable_iff=t_mod_3_zero_and_p_zero_or_ge_4; image_size=floor(n/3)_for_n_ge_3; Q2_noninjective_fiber=(0,8):C8_vs_C4_plus_C4; carrier_S4_regression=PASS`

## 12. Control-plane recommendation

Accept the hard target at the declared `U_2REG / P_1` count-profile scope with terminal state:

`NONREPRESENTABLE_PROFILE_EXACTLY_WITNESSED_AND_IMAGE_CLASSIFIED`.

Freeze three rules for downstream work:

1. any “completion” of observation profiles must carry an explicit `REPRESENTABLE` predicate;
2. a virtual profile cannot serve as a native existence witness;
3. the next probe upgrade should target the exact lost gluing data, then be tested against **both** defects: it should reduce virtual profiles and split known noninjective fibers.

The natural continuation is therefore not “add more abstraction” in the abstract. It is to test whether Q3/Q4 path-groupoid or descent/gluing data can recover enough overlap identity to make the representability map closer to bijective on a controlled finite class.

## Boundary / non-claims

- P000 remains unconditional and unchanged.
- Six native spatial dimensions remain primitive.
- Carrier `S4` remains carrier readout, not the full native P000 rotation group.
- The theorem is for the declared Q2 toy class and radius-one count-profile shadow only.
- “Compatible” here means compatibility under the retained local restriction maps, not full overlap/descent compatibility.
- The theorem does not claim every presheaf-like object in any broader category is nonrepresentable.
- No novelty claim is made for classical Yoneda or representability theory.
- The virtual completion is an analysis device, not a native ontology extension.

Execution-Record-ID: `ER-945FAC8D6CAF174D6B2B`  
Pending Result-ID: `RR-4B0C6E0CAEE305D5B844`
