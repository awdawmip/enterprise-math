# P018 — Finite-Precision Proof Calculus: Supplement 12

Status: `ACTIVE RESEARCH NOTE`  
Scope: subtraction-free State Pair layer, difference coordinates, kernel/diagonal calculus, and minimization of the foundational logic  
Depends on: P005, P008, P009, P010, P011, P018-T99–T109  
Discipline: Cartesian products, diagonal relations, kernel equivalence, pair dynamics, and function composition are elementary established mathematics. This note does not claim them as new mathematics; the research question is whether they form the weakest common logical layer beneath Enterprise Math precision, defect, and irreversibility routes.

## 1. The minimality question left by T99–T109

Supplement 11 defines

\[
\mathscr R_F(x,h)=F(x+h)-F(x).
\]

It connects State evolution with Difference evolution and rewrites P010 history merging as a zero-response relation.

But that expression still assumes:

1. state coordinates admit subtraction;
2. the base state `x` is retained, because the same `h` can respond differently at different bases.

The deeper question is therefore:

> Without assuming subtraction, group completion, or even integer coordinates, what object is already sufficient to express joint evolution of two states, their merging, and propagation of a path difference?

The answer is the elementary state pair.

---

## 2. P018-T110 — Every deterministic map strictly induces State Pair evolution

Status: `PROVED / ESTABLISHED PRODUCT CONSTRUCTION`

For any state set `X`, define

\[
\boxed{
\operatorname{Pair}(X)=X\times X.
}
\]

For any deterministic map

\[
F:X\to Y,
\]

define

\[
\boxed{
\operatorname{Pair}(F)(x,y)
=(F(x),F(y)).
}
\]

Then

\[
\boxed{
\operatorname{Pair}(id_X)=id_{\operatorname{Pair}(X)},
}
\]

and for

\[
X\xrightarrow{F}Y\xrightarrow{G}Z
\]

one has

\[
\boxed{
\operatorname{Pair}(G\circ F)
=
\operatorname{Pair}(G)\circ\operatorname{Pair}(F).
}
\]

These are immediate properties of the Cartesian product map. ∎

Thus simultaneous tracking of two states requires no additional algebraic axiom; every deterministic state evolution automatically gives strict pair evolution.

---

## 3. P018-T111 — The diagonal is absorbing under deterministic evolution

Status: `PROVED`

Define the diagonal of `X` by

\[
\boxed{
\Delta_X
=\{(x,x):x\in X\}.
}
\]

For every

\[
F:X\to Y,
\]

one has

\[
\boxed{
\operatorname{Pair}(F)(\Delta_X)
\subseteq
\Delta_Y.
}
\]

### Proof

If the input pair is `(x,x)`, then

\[
\operatorname{Pair}(F)(x,x)
=(F(x),F(x))
\in\Delta_Y.
\]

∎

Once two histories become the same state, every later deterministic map keeps them on the diagonal.

This recovers P010 irreversible merging at a level using **no integer difference at all**.

---

## 4. P018-T112 — The kernel relation is exactly the set of pairs sent to the diagonal

Status: `PROVED / ESTABLISHED`

For

\[
F:X\to Y
\]

define kernel equivalence by

\[
\boxed{
x\sim_F y
\iff
F(x)=F(y).
}
\]

Then

\[
\boxed{
(x,y)\in\sim_F
\iff
\operatorname{Pair}(F)(x,y)\in\Delta_Y.
}
\]

If one further composes with

\[
G:Y\to Z,
\]

then

\[
\boxed{
\sim_F\ \subseteq\ \sim_{G\circ F}.
}
\]

because `F(x)=F(y)` implies `G(F(x))=G(F(y))`. ∎

The P010 monotone coarsening of kernel partitions is therefore, at the lowest level, simply:

> deterministic composition may send more pairs to the diagonal but can never move a pair already on the diagonal away from it.

---

## 5. P018-T113 — On `N`, State Pair and `(base, signed difference)` are losslessly equivalent coordinates

Status: `PROVED`

Let

\[
\mathcal E
=\{(a,h):a\in\mathbb N,
\ h\in\mathbb Z,
\ a+h\ge0\}.
\]

Define

\[
\boxed{
\Theta:\mathbb N\times\mathbb N\to\mathcal E,
\qquad
\Theta(a,b)=(a,b-a).
}
\]

Its inverse is

\[
\boxed{
\Theta^{-1}(a,h)=(a,a+h).
}
\]

Hence

\[
\boxed{
\mathbb N\times\mathbb N
\cong
\{(a,h):h\in\mathcal D_a\}.
}
\]

Under this coordinate change, T110 pair evolution

\[
(a,b)
\mapsto
(F(a),F(b))
\]

becomes exactly the Supplement 11 rule

\[
\boxed{
(a,h)
\mapsto
(F(a),\mathscr R_F(a,h)).
}
\]

because `b=a+h`.

Exact finite response is therefore not a mysterious new operation appended to the foundation. It is ordinary state-pair evolution expressed losslessly in integer difference coordinates.

---

## 6. P018-C09 — A signed defect alone loses information needed for later propagation

Status: `COUNTEREXAMPLE / DESIGN WARNING`

Even when two pairs have the same signed difference, the same nonlinear or coarse operation can produce different difference responses.

### Quotient counterexample

Take

\[
Q_2(n)=n//2,
\qquad h=1.
\]

At base `0`,

\[
\mathscr R_{Q_2}(0,1)
=Q_2(1)-Q_2(0)
=0.
\]

At base `1`,

\[
\mathscr R_{Q_2}(1,1)
=Q_2(2)-Q_2(1)
=1.
\]

The value `h=1` does not determine its own transport.

### Collapse counterexample

For square collapse,

\[
\mathscr R_{C_2}(1,1)
=C_2(2)-C_2(1)
=0,
\]

whereas

\[
\mathscr R_{C_2}(3,1)
=C_2(4)-C_2(3)
=3.
\]

Therefore

\[
\boxed{
\text{a defect value alone is not a complete state of difference dynamics.}
}
\]

One must retain at least base + defect, or equivalently the full state pair.

This gives a hard design constraint: holonomy cannot be compressed to a global scalar detached from its base state and still be expected to evolve autonomously.

---

## 7. P018-T114 — A parallel-path 2-cell can first be defined as an endpoint pair, without subtraction

Status: `PROVED / DEFINITIONAL MINIMIZATION`

Let

\[
\gamma,\eta:X\to Y
\]

be parallel deterministic paths.

For input `x`, define the weakest path-comparison object by

\[
\boxed{
\mathfrak C_{\gamma,\eta}(x)
=(\gamma(x),\eta(x))
\in Y\times Y.
}
\]

If both paths are followed by the same suffix

\[
S:Y\to Z,
\]

then

\[
\boxed{
\mathfrak C_{S\gamma,S\eta}(x)
=
\operatorname{Pair}(S)
\bigl(\mathfrak C_{\gamma,\eta}(x)\bigr).
}
\]

No addition, order, or group completion on `Y` is needed.

When

\[
Y=\mathbb N,
\]

one may then use T113's `Theta` coordinates, whose second coordinate is the signed holonomy of T102:

\[
\eta(x)-\gamma(x).
\]

Thus

\[
\boxed{
\text{path pair / endpoint pair}
}
\]

can be treated as a more primitive 2-cell candidate than signed holonomy, while signed holonomy is a compressed coordinate representation when integer coordinates exist.

This note still does not claim that a strict 2-category has been constructed.

---

## 8. P018-T115 — The weakest defect of a critical square is its endpoint pair; numerical `Delta` is a coordinate

Status: `PROVED`

For an operation/projection square consisting of

\[
X_e
\xrightarrow{F_e}
X_e
\]

and

\[
X_e
\xrightarrow{\pi}
X_d
\xrightarrow{F_d}
X_d,
\]

define its endpoint pair by

\[
\boxed{
\mathfrak C_F^{e:d}(x)
=
\bigl(
\pi(F_e(x)),
F_d(\pi(x))
\bigr).
}
\]

The square commutes at `x` if and only if

\[
\boxed{
\mathfrak C_F^{e:d}(x)\in\Delta_{X_d}.
}
\]

When `X_d=N`, the signed critical-square defect of T103 is exactly the difference coordinate of this pair:

\[
\boxed{
\Delta_F^{e:d}(x)
=
\operatorname{second}(\mathfrak C)
-
\operatorname{first}(\mathfrak C).
}
\]

Whether a square commutes therefore requires no signed arithmetic; signed defect only gives a more efficient measurement of direction and size when noncommutation occurs.

---

## 9. P018-T116 — P005 precision fibers, collapse basins, and P010 history merging are all kernel-pair problems

Status: `PROVED STRUCTURAL UNIFICATION`

The following structures can all be written as “which state pairs are sent to the diagonal by a map.”

### Precision projection

For a coarse projection

\[
Q_m:\mathbb N\to\mathbb N,
\]

its kernel pair is

\[
\boxed{
(x,y):Q_m(x)=Q_m(y).
}
\]

These are exactly pairs in the same coarse fiber.

### Collapse basin

For

\[
C_p:\mathbb N\to\mathbb N,
\]

its kernel pair is

\[
\boxed{
(x,y):R_p(x)=R_p(y),
}
\]

namely pairs in the same perfect-power basin.

### Deterministic time

For cumulative evolution

\[
\mathcal F_t,
\]

its kernel pair is

\[
\boxed{
(x,y):\mathcal F_t(x)=\mathcal F_t(y),
}
\]

which is the P010 history-merging relation.

The physical meanings differ, but the underlying relational structure is shared:

\[
\boxed{
\text{many-to-one map}
\longleftrightarrow
\text{nontrivial kernel pair}
\longleftrightarrow
\text{off-diagonal pairs sent to diagonal}.
}
\]

This is weaker and more precise than calling all three the same kind of “entropy” or “collapse.”

---

## 10. P018-T117 — P010 multiplicity is a one-base fiber cardinality of the kernel pair

Status: `PROVED`

For cumulative evolution `F_t` and state `x`, P010 defines

\[
[x]_t
=\{y:F_t(y)=F_t(x)\}.
\]

In pair language, this is exactly the fiber of the kernel relation with first coordinate fixed at `x`:

\[
\boxed{
[x]_t
=
\{y:(x,y)\in\kerpair(F_t)\}.
}
\]

Therefore, whenever finite,

\[
\boxed{
M_t(x)
=|[x]_t|
=\left|
\{y:(x,y)\in\kerpair(F_t)\}
\right|.
}
\]

The zero-response count of T107 is identical after the T113 coordinate change from pair to difference coordinates.

P010 irreversibility multiplicity can therefore be defined at a foundation using **no subtraction at all**, with integer difference coordinates added later only when useful.

---

## 11. P018-T118 — Kernel relations grow monotonically under deterministic composition

Status: `PROVED`

Let

\[
X\xrightarrow{F}Y\xrightarrow{G}Z.
\]

Then

\[
\boxed{
\kerpair(F)
\subseteq
\kerpair(G\circ F).
}
\]

For a sequence

\[
F_t=T_{t-1}\circ\cdots\circ T_0,
\]

this gives

\[
\boxed{
\kerpair(F_t)
\subseteq
\kerpair(F_{t+1}).
}
\]

This is the pair-level form of P010's statement that equivalence classes can only persist or merge.

The important point is that this theorem needs only function composition—no natural numbers, order, addition, distance, or probability.

If Enterprise Math is searching for the deepest logical layer of **deterministic irreversibility**, kernel-pair monotonicity is therefore more primitive than any particular integer entropy formula.

---

## 12. Entry point for P011: define spectra on kernel pairs before choosing difference coordinates

P011 already studies:

- fiber multiplicity;
- collision polynomial;
- multiplicity spectrum;
- comparison with entropy.

T117–T118 suggest a more foundational organization:

1. treat the cumulative map's kernel pair / equivalence classes as the primitive combinatorial object;
2. define integer spectra on those finite fibers;
3. switch to `(base,h)` difference coordinates only when direction, local boundaries, or operation response are needed;
4. continue to treat logarithmic entropy only as an external derived comparison.

This reduces the risk of mistaking a coordinate choice for the ontology of irreversibility.

---

## 13. Further minimization of the foundational logic

Status: `RESEARCH SYNTHESIS / NOT FROZEN`

Supplement 11 proposed

\[
\text{typed finite State}
+
\text{state-dependent Difference fibers}
+
\text{exact response}.
\]

This stage separates an even weaker layer.

### Layer -1 — Pair / kernel logic

Require only:

- typed state sets/objects;
- deterministic maps;
- parallel state pairs;
- diagonal;
- kernel pair;
- pair evolution under functions.

This already expresses:

- merging;
- inability to split after merging;
- many-to-one behavior;
- equality of path endpoints;
- the set-theoretic basis of P010 multiplicity.

### Layer 0 — Numeric difference coordinates

Only when a state object has useful cancellative/additive coordinates do we compress

\[
(a,b)
\]

to

\[
(a,h=b-a).
\]

Then signed response, carry/borrow, holonomy magnitude, and the exact finite chain law become available.

### Layer 1+ — Precision/order/operation enrichment

Only after that do we add P008 order adjunction, P005 precision atlas, operation defect/obstruction, P017 certificates, and related structure.

Pair/kernel logic does not replace the integer-first ontology. It says only that **the logical skeleton required for irreversibility and path comparison can be weaker than integer arithmetic itself.**

---

## 14. Why this helps preserve all research routes

When two research routes end in different representation objects, they should not immediately be forced into one signed coordinate system.

First compare whether they define the same:

- state pair;
- kernel relation;
- diagonal-hit event;
- partition of states.

If those weakest structures agree, different numerical defects may only be coordinate differences.

If even the kernel pair / endpoint pair differs, then the routes are making genuinely different predictions about the underlying state structure.

Route comparison therefore acquires a hierarchy:

\[
\boxed{
\text{pair/kernel}
\to
\text{difference coordinate}
\to
\text{defect transformation law}
\to
\text{higher certificate/invariant}.
}
\]

The left side is weaker and more representation-independent; the right side carries more information but also requires stronger assumptions.

---

## 15. Executable pressure tests

Add:

- `src/enterprise_math/state_pair.py`
- `tests/test_state_pair.py`

Priority checks:

1. T110 Pair(id) and Pair(G∘F);
2. T111 diagonal absorption;
3. T112 kernel relation = diagonal preimage;
4. T113 pair ↔ base/difference coordinate inversion;
5. C09 same defect / different base response counterexamples;
6. T114 common-suffix pair propagation;
7. T116 quotient/collapse/time kernel-pair instances;
8. T118 kernel monotonicity under composition.

---

## 16. Next open questions

### P018-Q100 — Is Pair/kernel the weakest irreversibility substrate?

Search for a deterministic many-to-one structure whose merging irreversibility cannot be represented by a kernel pair. If none appears, then consider promoting this layer as the shared foundation of P010/P011.

### P018-Q101 — Evolution by relations rather than functions

A future natural foundation may require nondeterministic transition. Ordinary function kernels will then be insufficient. Determine how diagonal and pair evolution should be rewritten for relations/spans/correspondences.

### P018-Q102 — At which layer should 2x2 critical-grid interchange be proved?

Prefer to prove strict pasting/coherence first at the endpoint-path-pair layer; only map to signed defect coordinates when quantitative information is needed. This avoids making numerical 2-cell composition artificially complicated by state-dependent response.

### P018-Q103 — Compatibility of kernel partitions with the precision atlas

Mixed-radix chart changes preserve the underlying total detail. Prove whether legitimate chart transitions also strictly preserve the relevant kernel pairs / ambiguity partitions.

### P018-Q104 — Pair layer and P012 geometry

The most primitive geometric question may be which pairs are connected by primitive steps and by how many steps, rather than assuming a numerical distance first. Investigate whether the P012 graph metric is a shortest-path observable on the pair layer.

---

## 17. Current conclusion

This stage decomposes the State/Difference system of Supplement 11 one level further:

\[
\boxed{
\text{State Pair}
\quad\text{is more primitive than}\quad
\text{signed Difference}.
}
\]

For any deterministic map, the rule

\[
\boxed{
(x,y)\mapsto(F(x),F(y))
}
\]

already expresses merging, diagonal, kernel, and the P010 irreversibility monotonicity.

In natural-number coordinates,

\[
(a,b)
\leftrightarrow
(a,b-a)
\]

then produces exact finite response. Signed defect is therefore an efficient coordinate on pair evolution, not an object the foundation must assume first.

The weakest current candidate foundation becomes

\[
\boxed{
\text{typed finite State}
+\text{Pair/kernel logic}
+\text{optional numeric Difference coordinates}
+\text{precision/order/operation enrichments}.
}
\]

This step matters because it does two things at once: **it preserves the integer-first mathematical ontology while lowering the logical axioms needed for irreversibility to a layer even weaker than integer arithmetic.**