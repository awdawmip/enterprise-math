# R762BA — S6-equivariant triadic completion: sharp four-source fiber and typed Cell/Link/Port candidate

**Research status:** author-side exact theorems and a candidate-model construction; NOT_REVIEWED; NOT_NATIVE_ADMISSION. Date: 2026-11-15. Task RS-X6-TRIADIC-CLOSURE-DYNAMICS / immutable publication TP2-8B7E13C5904A2D6F1142. Researcher EM-X6-44BACF; Activity RA-2BFD679DF2B3D27CAA0CB7D5. Preserve the frozen scientific input pin; no P000 changes.

## Scope and provenance

P000 V5 fixes a native X6 affine Cell torsor over Z^6, six positive axes and twelve signed directions, pairwise native Enterprise orthogonality at 120 degrees, and the primitive stable nonzero balance condition: exactly three forces and TRIADIC_CLOSURE_E. The existing coordinate action includes an S6 axis-permutation *skeleton*. The current P000 source does not enumerate an admitted full signed TRIADIC_CLOSURE_E event update with Cell/Link/Port incidence. The question here is what this S6 symmetry forces on *candidate* equal-quantum third-leg completions of two distinct positive axis legs.

Current authoritative sources read: p000_reality_foundation.json; definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md; definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md; definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json; definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json; pinned research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md and V2 task publication at immutable source 417b71f7db564a23803308fa82d0218d6d0a805d; predecessor R762AZ at 5cfbada8f0e53aac10f03f760c02c1fb7a17776c. R762AZ's positive X6 path-shuffle bijection is combinatorial; it is not used to assert force closure.

## 1. Sharp equivariant relational completion

Let A={1,...,6}, G=S6, P={(i,j) in A^2 : i≠j} be visible *ordered* positive two-leg source labels, and E={(i,j,k) in A^3 : i,j,k are pairwise distinct}. Let π:E→P forget k. The candidate third-axis fiber F_(i,j)=A\{i,j} has exactly four elements. G acts diagonally.

**Theorem BA1.** Every G-invariant R⊆E with π(R)=P is E itself. No G-equivariant section s:P→E of π exists. The full relational completion E is a sharp four-sheet G-equivariant lift.

**Proof.** For fixed (i,j), K=Stab_G(i,j) fixes i and j pointwise and allows every permutation of the other four axis names; K≅S4. K acts transitively on F_(i,j). Therefore every K-invariant nonempty fiber equals F_(i,j). Since G acts transitively on P, any invariant R surjective onto P is all of E. If s were a G-equivariant section, s(i,j)=(i,j,k) would be fixed under all K. There is no K-fixed remaining axis k, contradiction. The entire E is manifestly equivariant, attaining four branches. QED.

**Theorem BA2 (sharp auxiliary-state cost).** Let U→P be any nonempty finite equivariant bundle of auxiliary states and f:U→E an equivariant map over P. For every (i,j), U_(i,j) contains a K-orbit of size divisible by four and hence at least four. This lower bound is attained by U=E and f=id.

**Proof.** Choose u with f(u)=(i,j,k). Equivariance implies Stab_K(u)⊆Stab_K(k)≅S3. Thus by subgroup index multiplication,

|K·u|=[S4:Stab_K(u)]=[S4:S3]·[S3:Stab_K(u)]=4[S3:Stab_K(u)].

The lower bound is sharp since a third-axis label itself has a four-member K-orbit and stabilizer S3. QED.

**Signed conditional extension.** If a *separately specified* closure model admits both signs for the third axis and the S6 axis-label action preserves sign, the candidate signed fiber consists of two distinct four-element S4 orbits, eight candidates in total. P000 does not automatically give both admissibilities; BA1–BA2 use only positive distinct-axis completions.

## 2. Explicit provisional Cell/Link/Port event

Let C be the fixed native X6 affine Cell torsor. A chosen Cell anchor c allows raw signed coordinates, but is not a global origin. For a positive native axis a, define the oriented half-link L(c,a)=(c,c+e_a) and named port Port(c,a)=(c,a). A force leg F(c,a,q,t,id) has integer q>0, a named source port, event id, and a separately typed ordered time coordinate t.

A **candidate atomic triad event** T(c;i,j,k;q,t,id) has three distinguishable equal-quantum legs incident to c on three distinct positive axes. Define the candidate closure predicate as this complete three-leg incidence relation. Update the decorated history by atomically appending one such relation, preserving its event id and all named ports. The event changes relational state, not the center Cell address; it is not three spatial steps and does not assert e_i+e_j+e_k=0. A two-leg fragment alone is never classified as stable by this candidate model.

The translation group and the S6 axis-permutation skeleton act simultaneously on native Cell coordinates, half-links, ports, leg labels and stored events. Equal quantum, three-leg arity and distinct-axis incidence are invariant, so the proposed atomic relation-update commutes with these actions. This is an explicit typed *consistency witness* for the P000 arity/orthogonality premises. It is a mathematical candidate for subsequent native admission/testing, not the already-established TRIADIC_CLOSURE_E force law, V17 physical rotation, or V29 PASS/TRANSFER transition.

## 3. Apparent two-force readout and exact provenance

For fixed ordered first legs (i,j), the apparent two-force observer O_(i,j) sends T(c;i,j,k;q,t,id) to (c,i,j,q,t), omitting third port k and event id. Its fiber has four distinct candidate triads. Each observer output can therefore arise from a *genuine three-leg event* in the candidate model without introducing a primitive two-force stable event.

**Theorem BA3 (future-observer minimal BRC carrier).** If permitted future operations include named-port tests Q_a(T)=1 when the hidden third axis equals a, for all a∈F_(i,j), then the smallest sufficient residual over O_(i,j)'s fiber has exactly four classes. Positive combinatorial BRC branch multiplicity equals four (one branch per third port). A local two-bit code can index the four classes only after an explicit local label choice; it does not supply a global S6-equivariant deterministic selector.

**Proof.** For k≠l, the test Q_k distinguishes T(c;i,j,k;...) from T(c;i,j,l;...). No future-operation-safe quotient can identify them. Conversely, preserving k computes all four tests. The lower bound and sufficiency match. BA1 prevents eliminating third-source labels through a globally equivariant deterministic choice. QED.

A coarse observer whose *entire* future interface genuinely factors through O_(i,j) may safely use one class instead. This observer-relative distinction preserves the current project's joint-relation and BRC source discipline. The count four is positive branch multiplicity; no signed or phase cancellation is inferred.

## 4. Candidate frame transport and based-pair holonomy

**Theorem BA4 (exact source-fiber transport).** For each axis permutation g in S6, the map β_g:(i,j,k)→(g(i),g(j),g(k)) is a bijection from the four candidate third-axis branches over (i,j) to those over (g(i),g(j)), preserving positive BRC multiplicity and the named third port. For two frame steps g,h, β_h∘β_g=β_(hg). Hence any finite word of axis-permutation frame labels yields a source-preserving transport, without choosing a preferred third axis.

**Proof.** A permutation preserves pairwise distinctness, gives an inverse via g^{-1}, and acts on all three labels by ordinary composition. The group action is functorial and carries all four source records injectively and surjectively. QED.

Suppose a frame path is *based at the visible ordered pair*, i.e. its total permutation g fixes i and j. Its induced holonomy on the hidden four-choice fiber is an element of K≅S4. **Theorem BA5 (sharp loop source-return spectrum).** The number of source branches returning to their original third-axis label is Fix(g|F_(i,j)), and lies in {0,1,2,4}, with exact multiplicities among the 24 possible K elements:

| S4 cycle class on four hidden axes | elements | fixed third axes |
| --- | ---: | ---: |
| identity | 1 | 4 |
| one transposition | 6 | 2 |
| one 3-cycle | 8 | 1 |
| double transposition | 3 | 0 |
| one 4-cycle | 6 | 0 |

In particular, an apparently closed two-leg pair-loop can permute all hidden third-source branches with **zero** full-source returns. The fixed-count histogram across all 30 ordered pairs and their 24 stabilizer elements is 0→270, 1→240, 2→180, 3→0, 4→30.

**Proof.** A hidden source k returns exactly when g(k)=k. The conjugacy-class enumeration of S4 is exhaustive (1+6+8+3+6=24), and cycle decomposition determines fixed points. The 30 visible ordered pairs have conjugate stabilizers, so the aggregate histogram is 30 times the per-pair count. QED.

These are exact results for the candidate S6-labelled transport groupoid. They do not assert that an actual V17 event realizes an arbitrary S6 word, or that a native V39 based loop has this holonomy. Once a typed native β is available, the stabilizer/fixed-point criterion supplies a direct observer-sensitive test.

## 5. Exact reproducible checks

Companion executable: R762BA_EQUIVARIANT_TRIAD_LIFT_VERIFY.js (standard-library Node.js). Its actual output is preserved in R762BA_EQUIVARIANT_TRIAD_LIFT_EVIDENCE.json. Checked domain: all 720 permutations of six axes, 30 ordered distinct visible pairs, 120 ordered positive triads, all four candidate axes per pair; all pair stabilizers have order 24 and point/triple stabilizers order 6. 86,400 covariance instances, 120 four-point K-orbit checks, 11,520 invariant-subset action checks (30 pairs × 16 subsets × 24 stabilizer elements), 180 two-force-projection collision pairs and 720 based-pair holonomy elements passed. The latter have fixed-hidden-source histogram (0:270, 1:240, 2:180, 3:0, 4:30). Assertion execution in Node v22.16.0 completed. BA1–BA5 are mathematical proofs; the finite program independently checks the exact finite S6 base model.

## 6. Scientific boundary and next discriminatory question

An *admitted* native signed Cell/Link/Port closure relation and its actual legal leg triples remain to be specified. It may restrict signs, source incidence, geometry, timing or relation types. When that definition becomes available, compute the actual stabilizer orbits and permitted port tests, and use them to determine whether the four-sheet fiber persists or is refined. Establish the true frame-to-port map β for V17; check V29 sequential-versus-atomic PASS/TRANSFER and V39 based-loop outputs on the same named-source event histories. Any coupling that erases k must carry an observer/future-operation safety proof. Retain all frozen science inputs, existing R762AW–AZ proofs, and author/reviewer separation.

**Verification/admission:** author-side proof, exact finite recalculation and GitHub source retention; independent Driver review, canonical Result admission and full native triadic dynamics remain open.
