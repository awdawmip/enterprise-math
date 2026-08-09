# P024 — Adjoint Boundary Pullback Calculus, Supplement 02

Status: `ACTIVE RESEARCH NOTE`  
Parent: `docs/P024_ACTION_LANGUAGE_PRECISION.en.md`  
Scope: discrete ordered chains, threshold observables, and forward actions whose relevant threshold preimages remain principal  
Depends on: P008 order-adjoint core, P023 future-compatible quotient discipline, and P024 reachable-boundary precision

## 1. Motivation

P024 Stage 1 identifies the future-safe cuts for integer translations as

\[
C_h=B-M_h.
\]

That formula uses the special fact that translation by `a` pulls a threshold `b` back to `b-a`.

The next question is more foundational:

> what property of a forward action makes a one-boundary threshold language close under exact backward boundary propagation?

The answer is order-theoretic rather than metric:

> a forward action preserves principal threshold structure under pullback exactly when it is a **right adjoint** for the relevant ordered state space.

For a declared finite task, the action may satisfy this only on the orbit of the task's actual boundaries; global right-adjoint structure is the clean uniform condition for **all** principal thresholds.

This supplement develops the resulting contravariant boundary calculus.

## 2. Principal threshold observables

Let `X` be a partially ordered state space. For `b in X`, write

\[
\uparrow b=\{x\in X:b\le x\}.
\]

The associated threshold bit is

\[
O_b(x)=\mathbf1_{b\le x}.
\]

Let

\[
F:X\to X
\]

be a forward action.

A boundary map

\[
\lambda_F:X\to X
\]

is an exact principal pullback if

\[
\boxed{
F^{-1}(\uparrow b)=\uparrow\lambda_F(b)
}
\]

for every boundary `b` under consideration.

Equivalently,

\[
\boxed{
\lambda_F(b)\le x
\iff
b\le F(x).
}
\]

## 3. P024-S2-T01 — Principal threshold pullback iff left/right adjunction

Status: `PROVED`.

For a map `F:X->X`, a total boundary map `lambda_F:X->X` satisfies

\[
F^{-1}(\uparrow b)=\uparrow\lambda_F(b)
\quad\text{for every }b
\]

if and only if

\[
\boxed{\lambda_F\dashv F.}
\]

### Proof

By definition,

\[
x\in F^{-1}(\uparrow b)
\iff
b\le F(x).
\]

The pullback is `uparrow lambda_F(b)` exactly when

\[
b\le F(x)
\iff
\lambda_F(b)\le x,
\]

which is precisely the Galois/adjunction law. ∎

Therefore the closure of **all** principal thresholds under exact pullback is not an extra numerical approximation property. It is exactly right-adjoint structure of the forward action.

This theorem is standard order theory viewed through the P024 future-boundary interpretation; P024 does not claim the adjunction theorem itself as new mathematics.

## 4. P024-S2-T02 — Forward composition becomes reverse boundary composition

Status: `PROVED`.

Suppose

\[
\lambda_F\dashv F,
\qquad
\lambda_G\dashv G.
\]

Then

\[
\boxed{
\lambda_F\circ\lambda_G
\dashv
G\circ F.
}
\]

Hence

\[
\boxed{
\lambda_{G\circ F}
=
\lambda_F\circ\lambda_G
}
\]

whenever the chosen adjoints are equality-faithful maps on the state poset.

### Proof

\[
(\lambda_F\circ\lambda_G)(b)\le x
\iff
\lambda_G(b)\le F(x)
\iff
b\le G(F(x)).
\]

∎

Thus forward state dynamics and backward boundary dynamics compose in opposite functional order.

This is the structural reason P024's translation formula contains `B-M`: translation addition is only one concrete realization of a more general contravariant pullback calculus.

## 5. P024-S2-T03 — Finite-horizon adjoint boundary-orbit theorem on a chain

Status: `PROVED`.

Now let the state space be the discrete total order `Z` or `N_0`, and let

\[
F_1,\ldots,F_m
\]

be forward actions with explicit left adjoints

\[
\lambda_i\dashv F_i.
\]

Let the current observable report a finite full vector of ordered thresholds

\[
B=\{b_1,\ldots,b_q\}.
\]

For a forward word

\[
w=(i_1,\ldots,i_k),
\]

meaning that `F_(i_1)` is applied first and `F_(i_k)` last, define the pulled boundary map

\[
\lambda_w
=
\lambda_{i_1}\circ\cdots\circ\lambda_{i_k}.
\]

For horizon `h`, define

\[
\boxed{
C_h
=
\{\lambda_w(b):b\in B,\ |w|\le h\}.
}
\]

Then for `x<y`,

\[
\boxed{
\text{all threshold outputs agree after every word }|w|\le h
\iff
(x,y]\cap C_h=\varnothing.
}
\]

Therefore the coarsest finite-horizon future-safe quotient is again the integer rank among the pulled cuts:

\[
\boxed{
\rho_h(x)=\#\{c\in C_h:c\le x\}.
}
\]

### Proof

For every boundary `b` and word `w`, repeated T02 gives

\[
b\le F_w(x)
\iff
\lambda_w(b)\le x.
\]

So the complete future threshold language is exactly the collection of present-time comparisons against `C_h`. Two states agree on all such comparisons iff no cut lies between them. ∎

This gives a closed-form P023 safe quotient on an infinite ordered state space without enumerating the fine states.

## 6. P024-S2-T04 — Recursive finite compiler and exact stabilization criterion

Status: `PROVED`.

Define

\[
C_0=B
\]

and recursively

\[
\boxed{
C_{h+1}
=
C_h
\cup
\bigcup_{i=1}^{m}\lambda_i(C_h).
}
\]

Then this recursion produces exactly the set of all boundary pullbacks from words of length at most `h+1`.

The naive word-count bound is

\[
\boxed{
|C_h|
\le
|B|\sum_{k=0}^{h}m^k.
}
\]

For `m=1` this is `|B|(h+1)`; for `m>1`,

\[
|C_h|
\le
|B|\frac{m^{h+1}-1}{m-1}.
\]

Boundary collisions can make the exact set much smaller.

Most importantly, if

\[
\boxed{C_{h+1}=C_h}
\]

for some finite `h`, then `C_h` is closed under every generator `lambda_i`, so

\[
\boxed{C_{h+k}=C_h\quad\text{for every }k\ge0.}
\]

Thus arbitrary-future precision is reached after a finite computation whenever the boundary orbit itself becomes finite and closed.

No infinite-state partition refinement is required in that case.

## 7. P024-S2-T05 — Translation is exactly the additive special case

Status: `PROVED`.

For integer translation

\[
F_a(x)=x+a,
\]

define

\[
\lambda_a(b)=b-a.
\]

Then

\[
\lambda_a(b)\le x
\iff
b-a\le x
\iff
b\le x+a=F_a(x),
\]

so

\[
\lambda_a\dashv F_a.
\]

For a word with cumulative translation `s`,

\[
\lambda_w(b)=b-s.
\]

Therefore T03 gives

\[
\boxed{C_h=B-M_h,}
\]

exactly recovering canonical P024 Stage 1.

So `B-M` is not the mother law. It is the additive coordinate form of adjoint boundary pullback.

## 8. P024-S2-T06 — P008 roots, quotients, and collapse are boundary-adjoint actions

Status: `PROVED` on `N_0`.

This stage directly connects P024 to the earlier P008 order core.

### Integer root

P008 gives

\[
k^p\le n
\iff
k\le R_p(n).
\]

Therefore the forward action

\[
F=R_p
\]

has exact boundary pullback

\[
\boxed{
\lambda_{R_p}(b)=b^p.
}
\]

A threshold on the future root state is therefore a perfect-power threshold on the current state.

### Integer quotient

For

\[
Q_d(n)=n//d,
\qquad d\ge1,
\]

we have

\[
db\le n
\iff
b\le Q_d(n),
\]

so

\[
\boxed{
\lambda_{Q_d}(b)=db.
}
\]

### Perfect-power collapse

Let

\[
C_p(n)=R_p(n)^p.
\]

Define the least perfect `p`-th power not below `b` by

\[
N_p(b)=\min\{k^p:k^p\ge b\}.
\]

Then

\[
\boxed{
N_p(b)\le n
\iff
b\le C_p(n),
}
\]

so

\[
\boxed{\lambda_{C_p}=N_p.}
\]

Because `N_p` is idempotent,

\[
N_p(N_p(b))=N_p(b),
\]

the boundary orbit of a single `p`-collapse action stabilizes after one pullback step, exactly dual to collapse idempotence.

This is a concrete bridge from P008's adjoint semantics to P024's future-safe precision semantics.

## 9. P024-S2-T07 — Forward coarse/fine intuition can reverse under future precision

Status: `PROVED` by exact examples.

The forward action's intuitive direction does not determine whether future-safe **initial** precision grows or contracts.

### Floor division: many-to-one forward contraction, expanding boundary hierarchy

For

\[
F_d(x)=x//d,
\qquad d\ge2,
\]

on `Z`,

\[
\lambda_d(b)=db.
\]

With the single boundary `B={1}` and one repeated action,

\[
\boxed{
C_h=\{1,d,d^2,\ldots,d^h\}.
}
\]

Therefore

\[
|C_h|=h+1
\]

and the global chain has `h+2` future-safe intervals through horizon `h`.

The arbitrary-horizon cut orbit is infinite.

So a many-to-one forward coarsening map can demand an ever-growing hierarchy of distinctions in the initial state when the declared future language becomes longer.

The same phenomenon is even faster for repeated integer roots: for `b>=2`, the pulled boundaries are

\[
b,b^p,b^{p^2},\ldots.
\]

### Dilation: forward expansion, contracting boundary hierarchy

For

\[
G_d(x)=dx,
\qquad d\ge2,
\]

we have

\[
\lambda_d(b)=\left\lceil\frac bd\right\rceil.
\]

Every finite set of integer boundaries reaches a finite fixed orbit because positive magnitudes above `1` strictly decrease toward `1`, negative values increase toward `0`, and `0,1` are fixed.

Thus forward expansion can yield finite arbitrary-future boundary precision.

### Consequence

There is no universal dynamical slogan such as

- “coarser forward maps require coarser initial precision”, or
- “expansive forward maps require finer initial precision”.

The exact quantity is the pullback orbit of the declared future boundaries.

## 10. P024-S2-T08 — Action words admit a boundary-transformation quotient

Status: `PROVED` for the full labelled threshold vector.

For a word `w`, define its boundary signature on the declared threshold set

\[
\boxed{
\Sigma_B(w)
=
(\lambda_w(b_1),\ldots,\lambda_w(b_q)).
}
\]

Then two words `u,v` satisfy

\[
\boxed{
\Sigma_B(u)=\Sigma_B(v)
}
\]

if and only if they induce the same full threshold-vector output on **every** current state:

\[
O_B(F_u(x))=O_B(F_v(x))
\quad\text{for all }x.
\]

Thus the future action-word language itself can be quotiented by its action on the declared boundary set.

For translations this collapses all words with the same cumulative displacement. For nonlinear adjoint actions the quotient can be noncommutative and substantially smaller than the raw word tree whenever distinct words induce the same boundary transformation.

This is not claimed as a new automata-minimization principle; it is the exact boundary-side form of the declared P024 chain language.

## 11. P024-S2-T09 — Global right-adjoint structure is stronger than task-relative boundary closure

Status: `PROVED BY COUNTEREXAMPLE`.

T01 characterizes closure of **all** principal thresholds. A declared finite future task may need less.

Define a nonmonotone integer map

\[
F(-2)=-1,
\qquad
F(-1)=-2,
\qquad
F(x)=x\text{ otherwise}.
\]

This map is not a right adjoint, because the preimage of `uparrow(-1)` is not an upper set:

- `-2` maps to `-1` and is accepted;
- `-1` maps to `-2` and is rejected;
- `0` is accepted.

However, for the declared threshold `B={0}`,

\[
F^{-1}(\uparrow0)=\uparrow0.
\]

The same remains true under every iteration because the nonmonotone swap stays entirely below zero.

Therefore a task-specific P024 compiler may operate on a smaller boundary orbit even when the full action has no global adjoint.

The correct hierarchy is:

1. **global right adjoint:** all principal thresholds close under pullback;
2. **orbit-relative principal closure:** only the boundaries actually generated by the declared task need close;
3. otherwise the one-cut calculus fails and a richer P023 state relation is required.

## 12. P024-S2-T10 — Nonmonotone pullback can split one boundary into several components

Status: `PROVED BY COUNTEREXAMPLE`.

Take

\[
F(x)=|x|
\]

on `Z` and threshold `b=1`.

Then

\[
F^{-1}(\uparrow1)
=
(-\infty,-1]\cup[1,\infty),
\]

which is not a principal upper set.

Indeed,

\[
F(-1)\ge1,
\qquad
F(0)<1,
\qquad
F(1)\ge1.
\]

No single integer cut can represent this pullback.

Thus arbitrary state-dependent/nonmonotone dynamics cannot be absorbed into the scalar P024 boundary-rank formula merely by replacing `B-M` with a guessed displacement set.

The correct future state may require multiple boundary components, a higher-dimensional relation, or generic P023 partition refinement.

## 13. Relation to P008, P023, and P024 Supplement 01

### P008

P008 owns the minimal order-adjoint semantics. Supplement 02 does not re-claim Galois connections or adjoint composition. It gives those established structures a new project-side role: **the left adjoint is exactly the reverse-time transport law for future threshold boundaries**.

### P023

P023 remains the generic owner of future-safe quotient/minimal repair. Supplement 02 gives a closed finite compiler when the declared threshold language stays inside principal boundaries.

### P024 Supplement 01

Supplement 01 handles high-dimensional lattice translations and full affine guard vectors. Supplement 02 handles non-translation chain actions through adjoint boundary pullback.

The two directions should not yet be collapsed into a universal nonlinear lattice theorem. A later bridge must specify when each high-dimensional guard score itself evolves through an adjoint chain action and how common score-lattice feasibility interacts with those nonlinear pullbacks.

## 14. Executable audit

Implementation:

- `src/enterprise_math/adjoint_boundary_precision.py`

Tests:

- `tests/test_p024_adjoint_boundary_precision.py`

The executable layer includes:

- explicit action witnesses carrying both forward maps and boundary pullbacks;
- translation, integer dilation, floor division, natural integer root, natural quotient, and perfect-power collapse actions;
- direct future threshold signatures;
- contravariant word pullback;
- finite boundary-orbit compilation;
- stabilization detection;
- finite-box adjunction audits that are explicitly **not** treated as global proofs.

Committed tests cover:

1. exact recovery of canonical `B-M` translation cuts;
2. direct future signatures versus boundary-rank equivalence for mixed translation/dilation/division/piecewise-monotone actions;
3. reverse composition of boundary pullbacks;
4. root/quotient/collapse adjunctions;
5. the infinite floor-division boundary hierarchy;
6. finite dilation stabilization;
7. action-word collapse under equal boundary transformations;
8. the task-relative nonmonotone exception;
9. the absolute-value split-preimage no-go;
10. the finite word-count cut bound.

Independent reconstruction additionally pressure-tested the future-signature/rank equivalence on hundreds of randomly generated monotone cofinal integer maps with plateaus and jumps and found no mismatch. These finite audits support the implementation; T01–T10 are justified by the proofs/counterexamples above.

## 15. Prior-art boundary

Galois connections, left/right adjoints, composition of adjoints, floor/ceiling division adjunctions, and principal upsets are established order theory. P008 already registers the relevant structural neighborhood, including [SRC-MATHLIB-FLOORDIV] and [SRC-MATHLIB-CLOSURE].

P024 does not claim these mathematical tools as inventions.

The project-specific research synthesis being tested is the exact organization

\[
\boxed{
\text{forward right-adjoint action language}
\longleftrightarrow
\text{contravariant principal-boundary pullback language}
\longrightarrow
\text{finite future-safe precision cuts}.
}
\]

Historical novelty of this integrated precision interpretation remains `NOVELTY_UNVERIFIED`.

## 16. Next pressure tests

1. bridge Supplement 01 and Supplement 02: nonlinear right-adjoint evolution in several guard-score directions plus common score-lattice feasibility;
2. formalize T01–T04 in Lean using established Galois-connection APIs rather than re-proving order theory from scratch;
3. push collapse-word families through the boundary side and compare their stable boundary maps with P019/P020 fixed-point stabilization;
4. study orbit-relative principal closure for nonmonotone actions before falling back to arbitrary P023 partitions;
5. measure boundary-orbit collisions as an exact action-language compression observable, without confusing it with historical irreversibility or entropy.
