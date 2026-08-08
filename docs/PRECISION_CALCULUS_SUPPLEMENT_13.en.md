# P018 — Finite-Precision Proof Calculus: Supplement 13

Status: `ACTIVE RESEARCH NOTE`  
Scope: 2x2 typed critical grids, strict endpoint-pair composition, exact finite signed-holonomy rectangle identities, local-defect cancellation, and the boundary of foundational interchange  
Depends on: P003, P005, P009, P010, P018-T99–T118, P020  
Discipline: this stage proves only finite-state and endpoint identities. Rewriting critical pairs, finite differences, kernel pairs, and double-category/interchange language have mature prior art. Similar formulas do not by themselves establish a new 2-category or a new calculus.

---

## 1. Why attack the 2x2 grid now

P018 Supplement 11 established exact finite response

\[
\mathscr R_F(x,h)=F(x+h)-F(x),
\]

with strict composition

\[
\mathscr R_{G\circ F}(x,h)
=
\mathscr R_G(F(x),\mathscr R_F(x,h)).
\]

Supplement 12 then showed that signed difference is not the weakest structure. For an arbitrary state set `X`, State Pairs already exist:

\[
(x,y)\in X\times X,
\]

and every deterministic map `F:X→Y` acts by

\[
(x,y)\mapsto(F(x),F(y)).
\]

The correct next step for P018-Q97 is therefore not to assume a 2-category, but to build the smallest typed 2x2 rectangle and ask:

1. whether the two decompositions agree strictly at the endpoint-pair layer;
2. how that agreement appears after adding integer Difference coordinates;
3. whether zero outer holonomy forces every local defect to vanish;
4. where P003 commutation, P009 nonconfluence, and P010 confluence sit in this hierarchy.

---

## 2. The typed 2x2 rectangle

Let

\[
F_0,F_1:X\to Y,
\qquad
G_0,G_1:Y\to Z.
\]

For a fixed `x∈X`, write

\[
a=G_0(F_0(x)),
\quad
b=G_0(F_1(x)),
\quad
c=G_1(F_0(x)),
\quad
d=G_1(F_1(x)).
\]

The proof uses only the four explicit endpoints:

- `(a,b)` along the upper comparison;
- `(b,d)` down the right side;
- `(a,c)` down the left side;
- `(c,d)` along the lower comparison.

---

## 3. P018-T119 — Strict composition of adjacent State Pairs

Status: `PROVED / LEAN-CHECKED TARGET`

For adjacent endpoint pairs

\[
(a,b),\qquad(b,c),
\]

define

\[
(a,b)\star(b,c):=(a,c).
\]

No subtraction, addition, order, metric, precision, or numeric state space is required.

This says only that when two path pieces share an intermediate endpoint, comparison of the whole composite keeps the two outer endpoints.

The operation is represented as `composeAdjacent` in

`EnterpriseMath/State/CriticalGrid.lean`.

---

## 4. P018-T120 — Strict rectangle interchange at the endpoint-pair layer

Status: `PROVED / LEAN-CHECKED TARGET`

For arbitrary types `X,Y,Z`, arbitrary maps

\[
F_0,F_1:X\to Y,
\qquad
G_0,G_1:Y\to Z,
\]

and arbitrary `x∈X`,

\[
\boxed{
(a,b)\star(b,d)
=
(a,d)
=
(a,c)\star(c,d).
}
\]

Equivalently,

\[
\boxed{
(G_0F_0x,G_0F_1x)\star(G_0F_1x,G_1F_1x)
=
(G_0F_0x,G_1F_1x)
}
\]

and

\[
\boxed{
(G_0F_0x,G_1F_0x)\star(G_1F_0x,G_1F_1x)
=
(G_0F_0x,G_1F_1x).
}
\]

### Proof

By definition, both decompositions retain the common outer endpoints `a` and `d`. ∎

### Meaning

This is the weakest current sense of interchange:

- no local square is assumed to commute;
- `b=c` is not required;
- no Difference object is required;
- no Abelian group is required;
- no order, metric, or topology is required;
- the state spaces need not be numeric.

Thus **endpoint-pair path composition is more primitive than numeric holonomy**.

This still does not justify declaring a full double category. General 2-cells, all horizontal/vertical composites, units, and global interchange axioms remain unconstructed.

---

## 5. Adding integer coordinates

Now specialize to natural-number states and allow signed differences as comparison coordinates.

Let

\[
h=F_1(x)-F_0(x),
\]

and define the pointwise difference between the second-stage operation family by

\[
\delta_G(y):=G_1(y)-G_0(y).
\]

The outer signed holonomy is

\[
\Omega(x)
:=
G_1(F_1(x))-G_0(F_0(x)).
\]

The State Pair `(a,d)` is simply coordinatized as

\[
(a,d-a).
\]

Numeric holonomy is therefore not a new foundational object; it is an integer coordinate on an endpoint pair.

---

## 6. P018-T121 — Two exact finite decompositions of outer holonomy

Status: `PROVED / EXECUTABLE`

Exactly,

\[
\boxed{
\Omega(x)
=
\mathscr R_{G_0}(F_0(x),h)
+
\delta_G(F_1(x)).
}
\]

Also,

\[
\boxed{
\Omega(x)
=
\delta_G(F_0(x))
+
\mathscr R_{G_1}(F_0(x),h).
}
\]

### First proof

By definition,

\[
\mathscr R_{G_0}(F_0x,h)
=G_0(F_1x)-G_0(F_0x),
\]

while

\[
\delta_G(F_1x)
=G_1(F_1x)-G_0(F_1x).
\]

Adding cancels the middle endpoint `G_0(F_1x)` and yields

\[
G_1(F_1x)-G_0(F_0x)=\Omega(x).
\]

The second decomposition is symmetric. ∎

The first route transports the first-stage displacement through `G_0` and then switches `G_0→G_1` at `F_1(x)`. The second route switches the operation family at `F_0(x)` and then transports the same displacement through `G_1`.

---

## 7. P018-T122 — Exact finite rectangle-variation identity

Status: `PROVED / EXECUTABLE`

Subtracting the two T121 decompositions gives

\[
\boxed{
\delta_G(F_1x)-\delta_G(F_0x)
=
\mathscr R_{G_1}(F_0x,h)
-
\mathscr R_{G_0}(F_0x,h).
}
\]

with

\[
h=F_1x-F_0x.
\]

The left side measures how the pointwise defect between `G_0` and `G_1` changes across the first-stage displacement. The right side measures how differently `G_1` and `G_0` transport that same displacement.

They are exactly the same integer.

This is an exact finite rectangle-variation law. We do not call it a curvature theorem because no additional geometric structure has been established.

---

## 8. P018-T123 — Common-suffix propagation is a degenerate rectangle

Status: `PROVED / EXECUTABLE`

If

\[
G_0=G_1=G,
\]

then

\[
\delta_G\equiv0
\]

and T121 reduces to

\[
\boxed{
\Omega(x)
=
\mathscr R_G(F_0x,F_1x-F_0x).
}
\]

This is exactly Supplement 11 T102 common-suffix holonomy propagation.

---

## 9. P018-T124 — Common-prefix degeneration

Status: `PROVED / EXECUTABLE`

If

\[
F_0=F_1=F,
\]

then `h=0`, hence both responses to the displacement vanish and

\[
\boxed{
\Omega(x)=\delta_G(F(x)).
}
\]

The rectangle reduces to a pointwise comparison of two second-stage operations at one intermediate state.

---

## 10. P018-C10 — Outer flatness does not imply local flatness

Status: `COUNTEREXAMPLE / DESIGN WARNING`

For any natural state `x≥1`, take

\[
F_0(x)=x,
\qquad
F_1(x)=x+1,
\]

\[
G_0(y)=y,
\qquad
G_1(y)=\max(y-1,0).
\]

Then

\[
G_0(F_0(x))=x
\]

and

\[
G_1(F_1(x))=x,
\]

so

\[
\boxed{\Omega(x)=0.}
\]

Yet

\[
F_1(x)-F_0(x)=1\ne0
\]

and

\[
\delta_G(F_1(x))=-1\ne0.
\]

The two nonzero local defects cancel exactly.

Therefore

\[
\boxed{
\text{outer confluence / zero holonomy}
\not\Rightarrow
\text{every local square is flat}.
}
\]

This is a hard boundary for future confluence arguments.

---

## 11. P018-T125 — P003 collapse commutation is a zero-outer-holonomy classification

Status: `DERIVED FROM P003`

Fix positive exponents `p,q` and take

\[
F_0=C_q,
\qquad
F_1=C_p,
\]

\[
G_0=C_p,
\qquad
G_1=C_q.
\]

Then

\[
\Omega_{p,q}(n)
=
C_q(C_p(n))-C_p(C_q(n)).
\]

P003 proves

\[
\boxed{
\Omega_{p,q}(n)=0\ \forall n
\iff
p\mid q\ \text{or}\ q\mid p.
}
\]

Thus P003 can be restated exactly as: the perfect-power collapse family is globally outer-flat on this operation rectangle exactly when the exponents are comparable in divisibility order.

This is a reinterpretation, not a change to P003.

---

## 12. P018-T126 — P009 nonconfluence is a non-diagonal outer pair, not failure of pair composition

Status: `STRUCTURAL REINTERPRETATION`

P009 proves that mixed collapse/project scheduling is generally nonconfluent.

Supplements 12–13 separate two facts:

- State Pair composition itself remains strict;
- nonconfluence means the outer endpoint pair is not on the diagonal:

\[
(a,d)\notin\Delta;
\]

or, in integer coordinates,

\[
\Omega=d-a\ne0.
\]

So path composition may remain strict while path endpoints fail to coincide.

---

## 13. P018-T127 — P010 confluence is outer-pair entry into the diagonal

Status: `DERIVED FROM T110–T118 / P010`

Two historical paths have merged exactly when their current endpoint pair lies on the diagonal:

\[
\boxed{(a,d)\in\Delta\iff a=d.}
\]

A common deterministic suffix maps diagonal pairs to diagonal pairs. Hence P010's irreversible history merge becomes:

> once an outer pair enters the diagonal, every later common deterministic suffix keeps it on the diagonal.

C10 requires a strict distinction between outer diagonality and local flatness; the first does not imply the second.

---

## 14. P018-T128 — P020 stabilization supplies canonical diagonal sinks but does not erase path history

Status: `DERIVED CONNECTION / NOT A NEW P020 THEOREM`

P020 constructs finite stabilization for a monotone reductive map on a well-founded partial order:

\[
\operatorname{stabilize}_F.
\]

Applying the same stabilization suffix to a State Pair gives

\[
(\operatorname{stabilize}_F(x),
 \operatorname{stabilize}_F(y)).
\]

If both states have the same greatest fixed point below them, the pair lands on the diagonal. This gives a canonical deterministic merging mechanism.

But C10 prevents the converse inference that a diagonal final pair means every intermediate square commuted or every local defect vanished.

P020 supplies canonical sinks/normal forms, not a local path-flatness theorem.

---

## 15. The substrate is now more sharply layered

### Layer 1 — Path / Pair

Only types and deterministic functions are needed:

\[
\boxed{
\text{typed State}
+\text{parallel endpoint Pair}
+\text{adjacent-pair composition}.
}
\]

This already expresses path comparison, kernel/diagonal structure, deterministic merging, and 2x2 outer endpoint interchange.

### Layer 2 — Difference coordinates

When integer coordinates are available,

\[
(a,d)\leftrightarrow(a,d-a).
\]

This adds signed holonomy, finite response, the rectangle-variation identity, and carry/borrow transport.

### Layer 3 — Precision / operation structure

Add P005 typed scales, P008 adjunction/projection, operation families, the carry cocycle, and atlas/representation obstruction.

### Layer 4 — Global certificates / time

Add P010 history merging, P011 irreversibility spectra, P017 global certificates, and P019/P020 stabilization.

A more stable current ordering is therefore

\[
\boxed{
\text{typed State}
\to
\text{Path Pair / kernel}
\to
\text{optional Difference coordinate}
\to
\text{response/holonomy}
\to
\text{precision/operation atlas}
\to
\text{global irreversibility/certificate/stabilization}.
}
\]

---

## 16. Why this still is not a declaration of a 2-category

T120 proves a strict rectangle endpoint interchange, but a full categorical claim still requires answers to:

1. whether a 2-cell is an endpoint pair, path pair, rewrite witness, or defect class;
2. whether horizontal and vertical compositions are closed for all typed arrows;
3. what the unit 2-cells are;
4. what information is irreversibly lost if intermediate paths are quotiented away;
5. whether numeric defects are natural under representation change;
6. whether the same interchange survives after nondeterministic relations/spans are introduced.

The strongest justified statement is therefore:

> **We have proved a subtraction-free endpoint-pair rectangle interchange and its exact finite shadow in integer Difference coordinates.**

---

## 17. Executable and formal verification

Added:

- `src/enterprise_math/critical_grid.py`
- `tests/test_critical_grid.py`
- `EnterpriseMath/State/CriticalGrid.lean`

The pressure tests cover:

1. both generic State Pair rectangle decompositions equal the same outer pair;
2. both numeric outer-holonomy decompositions agree exactly;
3. the finite rectangle-variation identity;
4. common-prefix and common-suffix degenerations;
5. a zero-outer/nonzero-local cancellation counterexample;
6. P003 comparable exponents producing zero outer holonomy;
7. P003 incomparable exponents producing an explicit nonzero outer holonomy.

Lean targets T119/T120 in a fully non-algebraic form and the integer telescoping shadow of the rectangle.

---

## 18. Next questions

### P018-Q100 — Can rectangles extend to finite cell complexes?

Do not assume topology first. Study whether finite path networks admit canonical outer endpoint-pair comparisons and whether different cell decompositions preserve the same pair/kernel information.

### P018-Q101 — Kernel partitions under grid refinement

When a coarse rectangle is subdivided, determine which kernel/diagonal facts remain invariant and which numeric local defects are redistributed.

### P018-Q102 — Certificates for local-defect cancellation

C10 shows that local defects can cancel. Seek a fully integer certificate distinguishing genuine local flatness, exact cancellation of nonzero defects, and defects that disappear only after coarse projection.

### P018-Q103 — P011 higher-order irreversibility from the Pair layer

Reconstruct higher-order fiber combinatorics from kernel pairs so that Pair/kernel is the substrate while P011 spectra remain higher-order integer statistics rather than being discarded.

### P018-Q104 — P020 coalescence time

For common deterministic dynamics, define the first finite time at which two initial states enter the diagonal. Study canonical bounds under P020's well-founded reductive hypotheses and their relation to `stabilizationSteps`.

---

## 19. Current conclusion

The key result is not a new label but a finite fact that is almost impossible to weaken further:

\[
\boxed{
(a,b)\star(b,d)
=
(a,d)
=
(a,c)\star(c,d).
}
\]

As soon as two composite paths have explicit endpoints, the outer pair of a 2x2 rectangle is independent of which internal decomposition is used.

Integer structure then yields two exact finite holonomy decompositions and the rectangle-variation identity.

The current hierarchy is therefore more precise:

\[
\boxed{
\text{Pair/kernel is path logic;}
\quad
\text{Difference/holonomy is its numeric coordinate;}
\quad
\text{nonconfluence means the outer pair is off the diagonal.}
}
\]

This simultaneously contains P003, P009, P010, and P020 without deleting their more specific structures.
