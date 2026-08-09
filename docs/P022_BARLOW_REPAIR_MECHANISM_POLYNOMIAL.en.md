# P022 — Bivariate Repair-Mechanism Polynomial

Status: `ACTIVE RESEARCH NOTE / EXACT FINITE REFINEMENT / P011 COMPLETENESS BOUNDARY`  
Owner: `program/p022-geometry-v2`  
Depends on: two-sided event repair; repair polynomial; P011 complete fiber statistics  
Cross-route relevance: P011 semantic boundary; P018/P023/P024 typed/state-dependent repair

## 1. One repair dimension can hide different mechanisms

For one two-sided coordination history `h`, exact repair dimension is

\[
r(h)=E(h)+B(h),
\]

where

- `E(h)` counts zero-departure orientation events;
- `B(h)` counts diagonal side-label split events.

The ordinary repair polynomial

\[
R_N(z)=\sum_h z^{r(h)}
\]

therefore remembers only the **sum** of two semantically different repair mechanisms.

Since the microscopic fiber size is

\[
2^{r(h)},
\]

P011's complete fiber-size statistics also see only `E+B`, not the decomposition into event types.

This note refines that loss exactly.

---

## 2. P022-RM01 — bivariate mechanism polynomial

Define

\[
\boxed{
\mathcal R_N(x,y)
=
\sum_h x^{E(h)}y^{B(h)},
}

where the sum runs over distinct coordination-history quotient states of horizon `N`.

The coefficient

\[
[x^e y^b]\mathcal R_N
\]

is the exact number of coordination histories whose repair state needs

- `e` excursion-orientation bits;
- `b` diagonal side-label bits.

Thus `\mathcal R_N` is the full finite distribution of repair **types**, whereas `R_N` is its total-dimension shadow.

---

## 3. P022-RM02 — weighted chamber recursion

Represent a coordination-history state by the sorted absolute pair

\[
0\le a\le b.
\]

For one legal transition `p->q`, define

\[
e(p)=\#\{\text{zero entries of }p\}
\]

and

\[
b(p,q)=
\mathbf 1_{\{p=(d,d),\ q\text{ unequal}\}}.
\]

Let

\[
F_n(q;x,y)
\]

be the bivariate mechanism polynomial of chamber histories of length `n` ending at `q`.  Then

\[
F_0((0,0);x,y)=1
\]

and

\[
\boxed{
F_{n+1}(q;x,y)
=
\sum_{p\to q}
 x^{e(p)}y^{b(p,q)}F_n(p;x,y).
}
\]

Finally

\[
\boxed{
\mathcal R_N(x,y)=\sum_qF_N(q;x,y).
}
\]

The reachable chamber is finite at fixed `N`, so this is an exact integer recursion.

Initial examples are

\[
\mathcal R_0=1,
\]

\[
\mathcal R_1=x^2,
\]

\[
\mathcal R_2=2x^2+x^2y,
\]

and

\[
\boxed{
\mathcal R_3
=2x^2+x^2y+2x^3y+x^4.
}
\]

---

## 4. P022-RM03 — ordinary repair polynomial is the diagonal shadow

Set

\[
x=y=z.
\]

Then each monomial becomes

\[
z^{E+B}.
\]

Therefore

\[
\boxed{
R_N(z)=\mathcal R_N(z,z).
}

So the ordinary repair polynomial is a literal diagonal specialization of the typed mechanism state.

This identifies exactly what is lost:

\[
\boxed{
(E,B)\mapsto E+B.
}
\]

---

## 5. P022-RM04 — exact finite evaluations and partial repair loads

### Quotient image

\[
\boxed{
\mathcal R_N(1,1)=|\operatorname{im}O_N|.
}

### Microscopic domain

At `x=y=2`, a history with event counts `(E,B)` receives weight

\[
2^E2^B=2^{E+B},
\]

its exact microscopic fiber size. Hence

\[
\boxed{
\mathcal R_N(2,2)=4^N.
}

### Orientation-bit load

Differentiate in `x` and multiply by `x=2`:

\[
\boxed{
2\,\partial_x\mathcal R_N(2,2)
=
\sum_{w\in\Omega_N}E(O(w)).
}
\]

This equals twice the one-sided excursion total, repeated against all microscopic words on the other labelled side.

### Side-label split load

Likewise

\[
\boxed{
2\,\partial_y\mathcal R_N(2,2)
=
\sum_{w\in\Omega_N}B(O(w)).
}
\]

which recovers the exact diagonal-split total.

Adding the two partial loads recovers

\[
2R_N'(2).
\]

Thus the bivariate refinement separates the two sources of the average repair-complexity theorem.

---

## 6. P022-RM05 — the complete P011 collision state does not recover repair mechanism type

P011's complete collision polynomial determines the fiber-size profile.  Here every fiber size is

\[
2^{E+B}.
\]

So two histories with the same total `E+B` but different `(E,B)` are indistinguishable to the complete P011 fiber/collision state.

This failure already occurs at horizon three.

The three repair-four histories split into two mechanism types:

\[
\boxed{(E,B)=(4,0)}
\]

for one quotient history, and

\[
\boxed{(E,B)=(3,1)}
\]

for two quotient histories.

Concretely, chamber histories include

\[
(1,1)\to(0,0)\to(1,1)
\]

with `(E,B)=(4,0)`, while

\[
(1,1)\to(0,2)\to(1,1)
\]

and

\[
(1,1)\to(0,2)\to(1,3)
\]

have `(E,B)=(3,1)`.

All three microscopic fibers have size

\[
2^4=16.
\]

Therefore the univariate repair polynomial records only

\[
3z^4,
\]

and the complete P011 collision state cannot distinguish which boundary mechanism generated the repair.

Hence

\[
\boxed{
\text{complete fiber-size statistics}
\not\Rightarrow
\text{repair-mechanism semantics}.
}
\]

This does **not** contradict P011 completeness: P011 is complete for fiber-size statistics, not for the semantic reason a fiber has that size.

---

## 7. Typed precision consequence

The two hidden repair coordinates are operationally different:

- an `E` bit restores **orientation** after a zero-boundary reset;
- a `B` bit restores **side identity** after a diagonal symmetry split.

A future language may need one type and not the other.  Collapsing them prematurely into a scalar repair dimension can therefore retain the correct total fiber size while erasing which repair coordinate must be supplied to a downstream operation.

The exact information chain is

\[
\boxed{
\text{typed repair }(E,B)
\to
r=E+B
\to
\text{fiber size }2^r
\to
\text{P011 collision statistics}.
}
\]

Every arrow is a legitimate quotient for a correspondingly weaker future language, but none should be inverted without additional structure.

This is a concrete P022 specialization of the broader task-relative precision principle.  Any generic abstraction belongs upstream and must preserve repair **type**, not just repair magnitude, whenever future operations distinguish mechanisms.

---

## 8. Prior-art boundary

Bivariate generating functions and weighted lattice/chamber walks are classical combinatorial tools.  P011 fiber-size completeness is already canonical project mathematics.

The P022-specific content is the identification of the two Barlow boundary-event repair coordinates and the exact proof that their scalar sum/fiber size loses mechanism semantics at horizon three.

Historical novelty of this packaging remains `NOVELTY_UNVERIFIED`.

---

## 9. Executable assets

Added:

- `src/enterprise_math/p022_barlow_repair_mechanism.py`;
- `tests/test_p022_barlow_repair_mechanism.py`.

The executable recursion is checked against direct distinct coordination-history grouping on short horizons, its diagonal specialization is checked against the ordinary repair polynomial, and the two weighted partial loads are checked against the independently derived excursion and diagonal-split totals.
