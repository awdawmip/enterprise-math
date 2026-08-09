# P024 — Lattice Guard Precision and Score-Lattice Arrangements, Supplement 01

Status: `ACTIVE RESEARCH NOTE`  
Parent: `docs/P024_ACTION_LANGUAGE_PRECISION.en.md`  
Scope: integer lattice translations + full vectors of integer affine threshold guards  
Dependency: P024 reachable-boundary precision and P023 future-compatible quotient discipline

## 1. Why the one-dimensional theorem is not enough

P024 Stage 1 proves that, on the integer line, a threshold boundary pulled backward by the actually reachable future translations cuts the present state space into the coarsest future-safe precision cells.

The first higher-dimensional guess would be:

> replace the one-dimensional action set by a vector action set and count reachable vector residues or translations.

E002 vector actuation already gives a counterexample to that shortcut: correlated vector actions can have few joint residues while a componentwise observable still exposes many independent boundary phases.

The correct higher-dimensional object must separate:

1. **action-side reachability** — which translations are actually available;
2. **observation directions** — which integer linear scores are read by the future task;
3. **state-side score feasibility** — which combinations of those scores can actually come from one lattice state.

This supplement gives that separation for the full vector of affine guard truth values.

## 2. Setup

Let the fine state be

\[
x\in\mathbb Z^n.
\]

Let the finite translation alphabet be

\[
A=\{a_1,\ldots,a_m\}\subseteq\mathbb Z^n,
\qquad
T_a(x)=x+a.
\]

For horizon `h`, let

\[
M_h
\]

be the set of cumulative translation vectors realized by action words of length at most `h`, including the zero word.

Let the declared observable be the **full vector** of `r` integer affine threshold guards

\[
G_j(x)=\mathbf1_{w_j\cdot x\ge\theta_j},
\qquad
w_j\in\mathbb Z^n,
\quad
\theta_j\in\mathbb Z.
\]

No Euclidean norm, real hyperplane distance, or continuum completion is part of the state semantics.

### Primitive guard coordinates

For every nonconstant guard define

\[
d_j=\gcd(|w_{j1}|,\ldots,|w_{jn}|),
\qquad
p_j=w_j/d_j,
\]

and

\[
\tau_j=\left\lceil\frac{\theta_j}{d_j}\right\rceil.
\]

Because `w_j·x` is always a multiple of `d_j`,

\[
\boxed{
G_j(x)=\mathbf1_{p_j\cdot x\ge\tau_j}.
}
\]

Thus the primitive integer score

\[
z_j=p_j\cdot x
\]

is the exact guard coordinate. A zero row is a constant guard and creates no precision distinction.

Define the primitive score map

\[
P:\mathbb Z^n\to\mathbb Z^r,
\qquad
P(x)=(p_1\cdot x,\ldots,p_r\cdot x),
\]

with constant guards omitted when discussing rank. Its image

\[
\boxed{\Lambda=P(\mathbb Z^n)}
\]

is the **guard-score lattice**.

## 3. P024-S1-T01 — Reachable pulled-guard arrangement

For every nonconstant guard `j`, define its horizon-`h` projected action shifts

\[
S_{h,j}=\{p_j\cdot m:m\in M_h\}\subseteq\mathbb Z
\]

and its pulled present-time cut set

\[
\boxed{
C_{h,j}=\{\tau_j-s:s\in S_{h,j}\}.
}
\]

Then after future translation `m`,

\[
G_j(x+m)=1
\iff
p_j\cdot x\ge\tau_j-p_j\cdot m.
\]

Therefore the complete horizon-`h` future guard signature is constant exactly on the integer cells cut out by the affine hyperplanes

\[
\boxed{
p_j\cdot x=c,
\qquad c\in C_{h,j}.}
\]

Equivalently, the one-dimensional P024 boundary orbit is pulled back along every primitive guard score.

### Interpretation

Higher-dimensional future-safe precision need not be rectangular. Its cells are intersections of integer slabs bounded by the reachable pulled guard hyperplanes. Oblique guards naturally produce oblique precision cells without introducing a real-valued metric.

## 4. P024-S1-T02 — Coarsest guard-rank normal form

For a scalar primitive score `z`, define

\[
\rho_{h,j}(z)
=\#\{c\in C_{h,j}:c\le z\}.
\]

For a state `x`, define the vector rank

\[
\boxed{
\rho_h(x)
=
\bigl(\rho_{h,1}(p_1\cdot x),\ldots,
\rho_{h,r}(p_r\cdot x)\bigr),
}
\]

again assigning no nontrivial coordinate to constant guards.

Then for all `x,y in Z^n`,

\[
\boxed{
\rho_h(x)=\rho_h(y)
\iff
G(x+m)=G(y+m)
\quad\text{for every }m\in M_h.
}
\]

Hence `rho_h` is the coarsest deterministic quotient preserving the complete full-guard horizon-`h` future language.

### Proof

If the ranks agree, then for every guard `j`, the two primitive scores lie on the same side of every cut in `C_(h,j)`. Every future word contributes one such cut, so every future guard bit agrees.

Conversely, if the ranks differ in coordinate `j`, some actual cut

\[
c=\tau_j-p_j\cdot m
\]

lies between the two scores. The corresponding reachable translation `m` makes guard `j` differ. Therefore the two states are future-distinguishable. ∎

This is the exact multidimensional analogue of the scalar reachable-boundary theorem for the declared full guard-vector observable.

## 5. P024-S1-T03 — Score-lattice factorization and permanent kernel invisibility

The rank state factors as

\[
\boxed{
\mathbb Z^n
\xrightarrow{P}
\Lambda
\xrightarrow{\rho_h}
\text{future-safe classes}.
}
\]

Therefore

\[
P(x)=P(y)
\Longrightarrow
\rho_h(x)=\rho_h(y)
\]

for every horizon and every translation word.

In particular,

\[
\boxed{x-y\in\ker P}
\]

is permanently invisible to this declared pure-translation/full-guard language.

Thus the relevant dimension is not automatically the ambient dimension `n`; it is bounded by

\[
\boxed{
\operatorname{rank}\Lambda
\le\min(n,r).
}
\]

This is a representational statement, not a claim that the physical state itself has only that many dimensions. A richer observable or operation family may read directions currently lying in `ker P`.

## 6. P024-S1-T04 — Exact class count is score-lattice feasibility, not a product by default

Each nonconstant guard `j` has exactly

\[
|C_{h,j}|+1
\]

formal scalar rank intervals.

If those coordinates were freely independent, the formal rank box would contain

\[
\prod_j(|C_{h,j}|+1)
\]

rank vectors.

But one actual state must produce a score vector in the common lattice `Lambda`. Therefore the exact number of future-safe classes is

\[
\boxed{
N_h
=|\rho_h(\Lambda)|
\le
\prod_j(|C_{h,j}|+1).
}
\]

The defect set

\[
\boxed{
D_h
=
\prod_j\{0,\ldots,|C_{h,j}|\}
\setminus
\rho_h(\Lambda)
}
\]

is the finite set of **formally possible but lattice-unrealizable precision cells**.

### Surjective-score sufficient condition

If the primitive score map is surjective,

\[
P(\mathbb Z^n)=\mathbb Z^r,
\]

then every scalar rank interval contains an integer score and every product combination is realizable. Hence

\[
\boxed{
N_h=
\prod_j(|C_{h,j}|+1).
}
\]

Surjectivity is sufficient, not necessary for equality at one particular guard/cut family.

## 7. P024-S1-T05 — Explicit score-lattice defect: 14 classes instead of 16

Take

\[
x=(x_1,x_2)\in\mathbb Z^2,
\]

with guards

\[
G_1(x)=\mathbf1_{x_1+x_2\ge2},
\qquad
G_2(x)=\mathbf1_{x_1-x_2\ge2},
\]

and the single translation action

\[
a=(1,0).
\]

At horizon `2`, the reachable sums are

\[
(0,0),(1,0),(2,0),
\]

so each guard receives pulled cuts

\[
\{0,1,2\}.
\]

Each guard therefore has four scalar rank intervals and the formal product box has

\[
4\cdot4=16
\]

rank vectors.

But the primitive score lattice is

\[
\Lambda
=\{(u,v)\in\mathbb Z^2:u\equiv v\pmod2\},
\]

because

\[
u=x_1+x_2,
\qquad
v=x_1-x_2.
\]

Rank `1` forces the corresponding score to equal `0`, while rank `2` forces it to equal `1`. Therefore rank cells

\[
(1,2),\qquad(2,1)
\]

violate the parity constraint and are empty.

All other rank cells are realizable, so

\[
\boxed{N_2=14<16.}
\]

This is a strict counterexample to a universal product-of-guard-counts law.

## 8. P024-S1-T06 — Semigroup/group behavior is observable-direction relative

For guard `j`, only the projected action generators

\[
\boxed{
D_j=\{p_j\cdot a:a\in A\}\subseteq\mathbb Z
}
\]

control that guard's future cut orbit.

Therefore the scalar P024 classification applies **separately in every guard direction**:

1. if all projected generators are zero, that guard is action-invariant;
2. if all nonzero projected generators have one sign, the guard sees a one-sided numerical-semigroup problem after sign/gcd normalization;
3. if both signs occur, the projected nonnegative-word monoid is the full gcd subgroup of `Z`.

The same physical action alphabet can therefore be group-complete in one observable direction and one-sided in another.

### Minimal directional example

Let

\[
A=\{(1,1),(-1,1)\}.
\]

For the `x` guard, projected generators are

\[
\{1,-1\},
\]

so the future action language is the full group `Z`.

For the `y` guard, projected generators are

\[
\{1,1\},
\]

so the future language is the one-sided semigroup `N_0`.

Thus there is no task-independent high-dimensional label saying simply “this action system is gcd-like” or “this action system has semigroup holes.” The classification is relative to the score direction actually read by the future language.

## 9. P024-S1-T07 — Exact criterion for global action-monoid group completion

Let

\[
M=\mathbb N_0a_1+\cdots+\mathbb N_0a_m
\]

be the nonnegative-word translation monoid and

\[
G=\mathbb Za_1+\cdots+\mathbb Za_m
\]

its generated abelian group.

Then

\[
\boxed{
M=G
\iff
\exists\lambda_1,\ldots,\lambda_m\in\mathbb Z_{>0}
\text{ with }
\sum_i\lambda_i a_i=0.
}
\]

### Positive zero relation implies group completion

If

\[
\sum_i\lambda_i a_i=0
\]

with every `lambda_i>0`, then for each generator

\[
\boxed{
-a_i
=(\lambda_i-1)a_i
+\sum_{j\ne i}\lambda_j a_j
\in M.
}
\]

So `M` contains the inverse of every generator and hence equals `G`.

### Group completion implies a positive zero relation

If `M=G`, then for every `i`, `-a_i` has a nonnegative-word representation

\[
-a_i=\sum_j\mu_{ij}a_j,
\qquad\mu_{ij}\ge0.
\]

Summing

\[
a_i+\sum_j\mu_{ij}a_j=0
\]

over all `i` yields one zero relation whose coefficient of every generator is at least one. ∎

### Relation to the one-dimensional theorem

In one dimension, the existence of at least one positive and one negative generator automatically gives a positive integer zero relation. In higher dimensions, merely having vectors pointing in several directions is not enough; the exact condition is the positive zero relation above.

## 10. P024-S1-T08 — The one-dimensional finite-hole conductor picture does not globally generalize

P024 Stage 1 uses the fact that a gcd-one numerical semigroup in `N_0` has only finitely many holes. That creates a finite irregular boundary layer before the regular gcd region.

A higher-dimensional affine semigroup can have infinitely many holes in its saturation.

Consider

\[
M=
\langle(2,0),(0,1),(1,1)\rangle_{\mathbb N_0}
\subseteq\mathbb N_0^2.
\]

Its generated group is all of `Z^2`, because

\[
(1,0)=(1,1)-(0,1).
\]

Its rational cone is the first quadrant, so its saturation inside the generated group is `N_0^2`.

Membership is exact:

- if `x` is even, `(x,y)` is generated by `(2,0)` and `(0,1)`;
- if `x` is odd and `y>=1`, use one `(1,1)` plus even horizontal and remaining vertical generators;
- if `x` is odd and `y=0`, membership is impossible because every use of `(1,1)` raises the second coordinate.

Hence the holes are exactly

\[
\boxed{
(2k+1,0),
\qquad k\in\mathbb N_0,
}
\]

an infinite family along a boundary face.

At the same time,

\[
\boxed{
(0,1)+\mathbb N_0^2\subseteq M.
}
\]

So a conductor translate exists even though the hole set itself is infinite.

### Consequence for precision

The one-dimensional statement

> all semigroup irregularity is contained in a finite set of missing cuts

must **not** be promoted unchanged to arbitrary affine action monoids.

For the full independent linear-guard language of this supplement, each individual guard still sees only a one-dimensional projection, so its directional holes retain the scalar P024 conductor behavior. Global affine holes become unavoidable once the future observable depends on **joint simultaneous action-score reachability** rather than independent guard bits.

This is the boundary that the next stage must attack.

## 11. P024-S1-T09 — Full guard-vector theorem does not extend to aggregate observables

T01–T06 assume the future output reports every guard bit independently.

If the task observes only an aggregate such as

\[
G_1(x)\wedge G_2(x),
\]

the guard-rank vector can be strictly over-refined.

Example:

\[
G_1=\mathbf1_{x_1\ge0},
\qquad
G_2=\mathbf1_{x_2\ge0},
\qquad
A=\{(1,1)\}.
\]

The states

\[
(-1,1)
\quad\text{and}\quad
(1,-1)
\]

have different full guard-rank states, but through horizon one the conjunction output is identical:

\[
\text{False}\to\text{True}.
\]

Therefore

\[
\boxed{
\text{full guard-vector precision}
\ne
\text{universal precision for arbitrary guard aggregates}.
}
\]

Aggregate/joint observables must return to P023 or receive a separate P024 arithmetic derivation using joint action-score reachability.

## 12. Relation to E002 vector precision

E002 Supplement 04 proved, for a rectangular centered quotient observable, that the number of future-safe detail classes is controlled by coordinate projections of the reachable residue set rather than by the cardinality of the correlated residue-vector orbit itself.

The present result explains the same structural split in a non-periodic affine-guard language:

- **action-side correlation** is reduced to the projected cut set for each independently reported guard;
- **state-side correlation** survives through the common score lattice `Lambda` and can make formal product cells empty.

E002's periodic rectangular quotient is not claimed here as a literal special case of the finite affine-guard theorem; it has an infinite periodic boundary family and should be bridged in a dedicated periodic-lattice-cell stage.

## 13. Relation to A3 guard-image lattice work

The A3 relation-quotient route already studies integer guard-score lattices, exact reachability of threshold sign patterns inside a coarse fiber, and standard hyperplane-arrangement complexity bounds.

Ownership is deliberately separated:

- **A3** owns hidden guard-image lattice reachability and relation-state retention inside a proposed coarse quotient;
- **P023** owns generic future-safe quotient/minimal-repair theory;
- **P024** owns forward translation action languages and the arithmetic geometry of the precision cells they induce.

This supplement consumes the established score-lattice/hyperplane viewpoint but does not duplicate A3's rank-two feasibility solver or arrangement-count theory.

## 14. Executable audit

Implementation:

- `src/enterprise_math/lattice_guard_precision.py`

Tests:

- `tests/test_p024_lattice_guard_precision.py`

The committed tests cover:

1. exact primitive normalization of nonprimitive integer guards;
2. direct future signatures versus guard-rank equivalence on several bounded 1D/2D systems;
3. permanent invisibility along the score-map kernel;
4. product class count when score coordinates are freely realizable;
5. the exact `14 < 16` parity-lattice defect;
6. direction-relative semigroup/group classification;
7. explicit inverse-word construction from a strictly positive zero relation;
8. the infinite affine-hole family and its conductor translate;
9. a conjunction counterexample showing that aggregate observables can be strictly coarser than the full guard-rank state.

Independent pre-commit reconstruction additionally checked the T02 equivalence over more than five thousand small action/guard systems without finding a mismatch. Those finite checks audit the implementation and theorem statement; they do not replace the proofs above.

## 15. Prior-art boundary

Hyperplane arrangements, integer lattices, affine semigroups, saturation, holes, conductors, gcd/Bezout arguments, and integer linear feasibility are established mathematics. P024 does not claim their invention.

A dedicated prior-art note registers the standard hyperplane-arrangement and affine-semigroup/hole literature used to bound the novelty claim.

Historical novelty of the integrated precision interpretation remains `NOVELTY_UNVERIFIED`.

## 16. Next pressure tests

The highest-value next targets are now sharply separated:

1. **joint/aggregate guard observables:** derive the minimal state from the joint action-score monoid rather than independent projections;
2. **state-dependent action alphabets:** replace the additive action monoid by an actual reachable transition graph and test which parts of the boundary-orbit theorem survive;
3. **periodic lattice-cell observations:** derive a Hermite/Smith-compatible version that can absorb E002 rectangular quotient precision without assuming rectangular cells;
4. **P022 geometry bridge:** only after a lattice geometry declares its actual observable boundaries and motion alphabet, compile its future-safe geometric precision through P024 rather than importing a universal metric resolution.
