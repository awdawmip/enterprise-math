# X6 concrete rotation paths: dagger-category correction and exact third-order tensor-jet threshold for shortest triadic branch provenance

Status: `FREE_RESEARCH / TYPE CORRECTION + EXACT FINITE JET THEOREM / NOT_FOUNDATION`
Date: `2026-09-06`
Researcher: `EM-FREE-7D3C9A / FREE_AXIOM_DISCOVERY`
Parent issue: `#1255`
Consumes:
- `research_notes/X6_TRIADIC_ROTATION_GENERATORS_V1_20260906.md`
- `research_notes/X6_ROTATION_PATH_GROUPOID_V2_20260906.md`
- `research_notes/X6_TRIADIC_ATOMIC_SCATTER_AND_BRC_CORRELATION_V1_20260906.md`
- `research_notes/X6_NATIVE_EVENT_TIME_AND_MARKOV_MEMORY_V1_20260906.md`
- `research_notes/X6_NATIVE_EVENT_TRACE_PARTIAL_ORDER_V2_20260906.md`
- `research_notes/VIETE_X6_EQUIVARIANT_OUTER_ROOT_LAW_SELECTION_20260906.md`
Checker: `experiments/x6_rotation_path_tensor_jet_20260906/check_x6_rotation_path_tensor_jet.py`
Checker source commit: `4e06f5d656a943221176f14c2a9ca8cc29604476`
Current source frontier consumed: `main@4e06f5d656a943221176f14c2a9ca8cc29604476`

## 1. A necessary type correction: concrete paths with raw concatenation are not a groupoid

The parallel V2 rotation-path result correctly insists that concrete native path history is additional information above the frame endpoint.  It defines path composition by literal concatenation and deliberately retains nonempty return loops.

Those requirements are incompatible with calling raw concrete paths a groupoid whose inverse is path reversal.

Let

\[
\gamma=(s_1,\ldots,s_M)
\]

be a nonempty concrete primitive-step path and let

\[
\gamma^\dagger=(-s_M,\ldots,-s_1)
\]

be its immediate reversal.

Under literal concatenation,

\[
\gamma;\gamma^\dagger
\]

is a concrete path of length `2M`.  It is not the empty path.

But if `gamma^dagger` were a categorical/groupoid inverse, one would require

\[
\gamma;\gamma^{-1}=\mathrm{id},
\]

i.e. equality with the empty identity path.

Therefore the raw object used for BRC provenance has the exact type

\[
\boxed{
\operatorname{PATHCAT}_{X6}
=\text{free concrete path category with a reversal dagger},
}
\]

not a raw-concatenation groupoid.

The reversal satisfies

\[
(\gamma^\dagger)^\dagger=\gamma,
\qquad
(\gamma;\eta)^\dagger=\eta^\dagger;\gamma^\dagger,
\]

but generally

\[
\gamma;\gamma^\dagger\ne\mathrm{id}.
\]

### Rotation-decorated version

Retype the parallel object as

\[
\boxed{
\operatorname{ROT\_PATHCAT}_{X6}.
}
\]

An arrow is still `(g,gamma):x->gx`, composition still multiplies frame elements and concatenates concrete paths, and the dagger is

`(g,gamma)^dagger=(g^-1,gamma^dagger)`.

All finite branch counts, path-length gradings, and the 64-lift theorem survive unchanged.  Only the categorical inverse claim is corrected.

### True groupoid alternative

One may construct a genuine groupoid only after imposing a path-reduction equivalence which identifies immediate retracing with identity.  That quotient is **not** operation-safe when the future observer asks for exact path length, retracing multiplicity, or concrete BRC provenance.

Thus the dagger category is the correct source type for the current full-provenance horizon.

Freeze:

`CONCRETE_PATH_REVERSAL = DAGGER_INVOLUTION`.

`CONCRETE_PATH_REVERSAL != CATEGORICAL_INVERSE_UNDER_RAW_CONCATENATION`.

## 2. Exact noncommutative integer path jets

Let a concrete primitive-step path have ordered steps

\[
\gamma=(s_1,\ldots,s_M),
\qquad
s_r\in\{\pm e_1,\ldots,\pm e_6\}.
\]

Define

\[
S_0(\gamma)=1
\]

and, for `k>=1`,

\[
\boxed{
S_k(\gamma)
=\sum_{1\le r_1<\cdots<r_k\le M}
 s_{r_1}\otimes\cdots\otimes s_{r_k}
\in(\mathbf Z^6)^{\otimes k}.
}
\]

The order-`K` truncated path jet is

\[
\mathcal J_{\le K}(\gamma)
=(S_0,S_1,\ldots,S_K).
\]

Equivalently it is the degree-`<=K` truncation of the ordered noncommutative product

\[
\prod_{r=1}^M(1+s_r).
\]

No continuum path integral is used.

## 3. Exact composition law

For literal concatenation `gamma;eta`, every increasing subsequence splits uniquely into a prefix chosen from `gamma` and a suffix chosen from `eta`.

Therefore

\[
\boxed{
S_n(\gamma;\eta)
=\sum_{p+q=n}S_p(\gamma)\otimes S_q(\eta).
}
\]

This is an exact integer identity.

Hence truncated jets compose inside the truncated tensor algebra:

\[
\boxed{
\mathcal J_{\le K}(\gamma;\eta)
=\mathcal J_{\le K}(\gamma)\star
 \mathcal J_{\le K}(\eta).
}
\]

Associativity is inherited from concatenation/tensor multiplication.

If exact primitive path count is part of the observer, adjoin the additive grade

\[
M(\gamma;\eta)=M(\gamma)+M(\eta).
\]

Thus a finite composition-safe summary is

\[
\boxed{
\mathsf{PJ}_K(\gamma)
=(M,S_1,\ldots,S_K).
}
\]

For a rotation-decorated arrow retain the frame label as well:

\[
(g;M,S_1,\ldots,S_K).
\]

## 4. Reversal/dagger descends exactly

Let `R_k` reverse tensor-factor order:

\[
R_k(v_1\otimes\cdots\otimes v_k)
=v_k\otimes\cdots\otimes v_1.
\]

Reversing the path order and negating every primitive step gives

\[
\boxed{
S_k(\gamma^\dagger)
=(-1)^kR_kS_k(\gamma).
}
\]

The path-count grade is unchanged.

Therefore every finite tensor jet is closed under the concrete reversal dagger even though that dagger is not a categorical inverse.

## 5. Signed-permutation covariance

Every signed X6 frame automorphism `g` acts linearly on primitive steps.  Hence

\[
\boxed{
S_k(g\gamma)=g^{\otimes k}S_k(\gamma).
}
\]

The path jet is therefore compatible with the current signed triadic frame algebra and does not depend on one special coordinate triad.

## 6. Two-step INNER/OUTER order first appears at degree two

Take one triadic macro edge

\[
a\to b,
\]

with `a,b` distinct signed unit axes.

The two shortest step words are

\[
I=(-a,b),
\qquad
O=(b,-a).
\]

They have the same path count

\[
M=2
\]

and the same first jet

\[
S_1=b-a.
\]

Thus every commutative displacement summary loses the branch order.

At degree two,

\[
S_2(I)=(-a)\otimes b,
\]

\[
S_2(O)=b\otimes(-a),
\]

which are distinct.

Their difference is the antisymmetric tensor

\[
\boxed{
\Delta(a,b)
=a\otimes b-b\otimes a.
}
\]

So degree two is exactly the first jet level which can distinguish the local INNER/OUTER diamond.

The antisymmetric projection is the native ordered-area two-form

\[
A(\gamma)
=\sum_{r<t}s_r\wedge s_t.
\]

For the two branches,

\[
A(I)=-a\wedge b,
\qquad
A(O)=+a\wedge b.
\]

This gives a compact branch-sign observer, although the full second tensor contains more backtracking information than its antisymmetric projection alone.

## 7. Full shortest Q_S cycle: degree one collapses all 64 branch words

Fix one oriented triad and its six signed unit phases

\[
a_0,\ldots,a_5,
\qquad a_{r+3}=-a_r.
\]

A complete shortest lift is one word

\[
\beta=(\beta_0,\ldots,\beta_5)\in\{I,O\}^6.
\]

All 64 words use the same endpoint sequence and the same primitive signed-step multiset; only the order inside each adjacent two-step block changes.

Every complete cycle is closed, so

\[
S_1=0.
\]

Therefore order one has exactly

\[
\boxed{1}
\]

observer class on this population.

## 8. Exact degree-two quotient: 27 classes

Write

\[
b_r=1_{\{\beta_r=O\}}\in\{0,1\}.
\]

Changing block `r` from INNER to OUTER swaps two adjacent primitive steps, so all degree-two contributions involving other blocks remain unchanged.  The degree-two increment is

\[
\Delta_r
=a_r\otimes a_{r+1}-a_{r+1}\otimes a_r.
\]

Because

\[
a_{r+3}=-a_r,
\qquad
a_{r+4}=-a_{r+1},
\]

one has

\[
\Delta_{r+3}=\Delta_r.
\]

The three tensors

\[
\Delta_0,\Delta_1,\Delta_2
\]

are independent in the selected three-axis exterior/tensor sector.

Hence

\[
\boxed{
S_2(\beta)
=S_2(I^6)
+\sum_{r=0}^2 n_r\Delta_r,
}
\]

where

\[
\boxed{
n_r=b_r+b_{r+3}\in\{0,1,2\}.}
\]

Thus the complete second-order state is exactly the triple of antipodal OUTER counts

\[
(n_0,n_1,n_2)\in\{0,1,2\}^3.
\]

Therefore the number of distinct degree-two branch classes is

\[
\boxed{3^3=27.}
\]

### Matched-fiber witness

The branch words with one OUTER occurrence on edge `0` and one OUTER occurrence on the antipodal edge `3` have identical `S_1,S_2` but different branch history and different third jet.

Hence order two is **not** operation-safe for a future observer which asks which member of an antipodal edge pair carried the OUTER root branch.

## 9. Outer/inner cycle area holonomy

The antisymmetric degree-two projection gives a compact law-level distinction.

For the all-INNER cycle,

\[
\boxed{A(I^6)=0.}
\]

For the all-OUTER cycle on the canonical oriented triad `S=(i,j,k)`,

\[
\boxed{
A(O^6)
=-4\,(e_i-e_k)\wedge(e_j-e_k),
}
\]

with the sign reversed when the sweep orientation is reversed.

Thus the root-refining OUTER law carries a nonzero oriented second-order path holonomy, whereas the pivot-returning INNER spatial law has zero antisymmetric area.

This is a path-order invariant; it is not an additional spatial axis or a force-balance equation.

## 10. Degree three resolves the antipodal placement ambiguity

Because each macro block contains only two primitive steps, its internal third jet vanishes.  The full `S_3` of the six-block concatenation is therefore affine-linear in the six branch bits.

Let

\[
d_r=a_{r+1}-a_r
\]

be the fixed macro displacement and let

\[
p_r=\sum_{t<r}d_t=a_r-a_0,
\qquad
q_r=\sum_{t>r}d_t=a_0-a_{r+1}.
\]

Then changing branch `r` from INNER to OUTER changes the full third jet by

\[
\boxed{
C_r
=p_r\otimes\Delta_r
+\Delta_r\otimes q_r.
}
\]

Hence

\[
\boxed{
S_3(\beta)
=S_3(I^6)+\sum_{r=0}^5b_rC_r.
}
\]

Unlike the degree-two tensors, the six `C_r` remember where around the oriented Q cycle the branch swap occurred.

## 11. Exact linear-independence certificate

Use the local ordered basis `(e_i,e_j,e_k)` and inspect the following six tensor coordinates of the six contribution vectors `C_r`:

\[
(i,i,j),
(i,i,k),
(i,j,i),
(i,j,k),
(i,k,i),
(j,j,k).
\]

The resulting `6x6` integer minor is

\[
\begin{pmatrix}
0&0&0&2&0&0\\
0&0&-1&0&0&-1\\
-1&0&0&-3&0&0\\
0&1&0&0&1&0\\
0&0&3&0&0&1\\
0&1&0&0&-1&0
\end{pmatrix}
\]

with determinant

\[
\boxed{8\ne0.}
\]

Therefore

\[
C_0,\ldots,C_5
\]

are linearly independent over `Q`.

Consequently the affine map

\[
\{0,1\}^6\to(\mathbf Z^6)^{\otimes3},
\qquad
\beta\mapsto S_3(\beta)
\]

is injective.

Thus degree three has exactly

\[
\boxed{64}
\]

classes on the 64 shortest branch words.

## 12. First lossless jet order

Combining the exact class counts:

\[
\boxed{
\begin{array}{c|c}
\text{jet depth}&\text{classes on the 64 shortest Q-cycle lifts}\\
\hline
1&1\\
2&27\\
3&64
\end{array}}
\]

Therefore

\[
\boxed{
\operatorname{FIRST\_LOSSLESS\_PATH\_JET\_ORDER}=3
}
\]

for the complete shortest six-edge triadic branch population.

This is verified identically on all twenty selected triads by signed-permutation covariance and finite exhaustive check.

The appearance of the number three here is a theorem about ordered path provenance; it must not be identified with P000 `TRIADIC_CLOSURE_E` without a separate bridge.

## 13. Composition-safe finite signature and its exact lease

Define the third-order graded path state

\[
\boxed{
\mathsf{PJ}_3(\gamma)
=(M,S_1,S_2,S_3).
}
\]

It has three exact structural properties:

1. **composition:** computed from the convolution/tensor product law;
2. **dagger:** computed by tensor-factor reversal with the sign `(-1)^k`;
3. **frame covariance:** signed axis permutations act tensorwise.

On one complete shortest Q-cycle population it is also injective, so it preserves every future operation that depends only on the six-bit branch word in that finite scope.

However no claim is made that third-order jets recover arbitrary unbounded concrete X6 path words.  Parallel native-time work already proves that no fixed finite memory can preserve unrestricted exact Path-formal provenance under all future history queries.

Therefore the exact lease is:

`PJ3 = COMPOSITION-SAFE TRUNCATED PATH OBSERVER`.

`PJ3 = LOSSLESS ON ONE COMPLETE SHORTEST TRIADIC Q-CYCLE BRANCH POPULATION`.

`PJ3 != GLOBALLY LOSSLESS FOR UNBOUNDED PATH-FORMAL HISTORY`.

## 14. Parallel force/time rebase: INNER and OUTER are observer-law relative

Same-day triadic force research gives an important correction to any universal branch-selection slogan.

For three labeled force tokens undergoing one triadic scatter, each token separately has INNER/OUTER shortest choices.  Requiring the three force occurrences to meet at one common atomic action Cell selects uniquely

\[
\boxed{III}
\]

among the eight joint branches.

Moreover the six atomic closure phases can be retained as six distinct **relation labels** over the same pivot spatial Cell, producing a decorated INNER C12 relation clock.

By contrast the Viète root observer asks for a twelve-state **spatial Cell** phase lift with nonzero balanced half-turn roots, and under Q-equivariant deterministic shortest laws this selects uniquely

\[
\boxed{OOOOOO}.
\]

Thus:

\[
\boxed{
\text{VIETE SPATIAL ROOT LAW}=\text{OUTER},
\qquad
\text{ATOMIC TRIADIC FORCE-CLOSURE LAW}=\text{JOINT INNER}.
}
\]

There is no contradiction because the consumed relations and observer horizons differ.

This is positive evidence for the BRC rule:

`BRANCH_PROVENANCE_MUST_SURVIVE_UNTIL_THE_TYPED_CONSUMING_LAW_IS_FIXED`.

## 15. Relation to event traces

The same-day event-time work uses free event words modulo only explicitly certified independent swaps, i.e. a trace monoid rather than a blanket path-inverse quotient.

That structure is compatible with the dagger-category correction here:

- concrete spatial/path histories retain order unless a safe relation authorizes collapse;
- reversal is available as a typed operation without automatically erasing the history;
- independent event serializations may be quotiented only under an observer-safety certificate.

This keeps P000 time-as-order, BRC provenance and rotation path composition in one consistent categorical direction.

## 16. New frontier

The local spatial/root selection and the finite one-cycle provenance compression are now sharp.

The next hard problem is to determine how much of `PJ3` remains necessary under **arbitrary compositions of triadic rotation arrows**.

Candidate tasks:

1. classify the kernel of `PJ3` on two-cycle and multi-generator composed populations;
2. determine whether a lower typed signature suffices once the all-OUTER root law is fixed;
3. couple path jets to the event-trace dependency quotient without erasing dependent branch order;
4. determine whether a duration/time cocycle factors through any finite jet;
5. classify which loop invariants of `ROT_PATHCAT_X6` are visible to root, force and channel observers respectively.

No Foundation promotion is made here.
