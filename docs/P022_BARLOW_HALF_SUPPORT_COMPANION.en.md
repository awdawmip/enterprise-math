# P022 — Half-Defect Support Avoidance in Companion Coordinates

Status: `ACTIVE RESEARCH NOTE / EXACT COORDINATE REDUCTION + COUNTEREXAMPLE`  
Owner: `program/p022-geometry-v2`  
Depends on: universal midpoint-offset companion; canonical A-elimination; pure Franel defect  
Cross-route relevance: P018 cancellation/defect; P023 minimal repair and future-safe witnesses

## 1. The support-avoidance obstruction

Let `p` be a forced-midpoint prime

\[
p\equiv5,7\pmod8,
\qquad
m=\frac{p-1}{2},
\]

and assume the A-boundary

\[
2m-1=p-2
\]

is composite.

The central-binomial coordinate has a canonical triangular elimination

\[
A_m
=
\prod_{j<m}A_j^{\alpha_{m,j}}.
\]

The associated pure Franel defect is

\[
D_m
=
\frac{F_m}{\prod_{j<m}F_j^{\alpha_{m,j}}}.
\]

Even if `p|F_m`, the same prime can occur in one of the older `F_j` used by the A-elimination and cancel from `D_m`.

This note rewrites that obstruction in the universal midpoint-companion coordinates.

---

## 2. P022-LI30 — exact support/companion equivalence

Let

\[
S_p
=
\{j<m:\alpha_{m,j}\ne0\}
\]

be the canonical A-elimination support.

For every `j in S_p`, define its midpoint offset

\[
d_j=m-j.
\]

The universal companion theorem gives

\[
p\mid F_j
\iff
p\mid N_{m-j}.
\]

Therefore

\[
\boxed{
S_p\cap Z_p=\varnothing
\iff
p\nmid N_{m-j}
\text{ for every }j\in S_p.}
\]

No Franel table remains in the right-hand condition.  The support-avoidance question is now an interaction between two **universal integer constructions**:

1. the central-binomial elimination support `S_p`;
2. the midpoint companion numerators `N_d`.

This is an exact coordinate change, not a conjecture.

---

## 3. Valuation decomposition

For every prime `p` in this scope,

\[
\boxed{
v_p(D_m)
=
v_p(F_m)
-
\sum_{j<m}\alpha_{m,j}v_p(F_j).}
\]

Thus if LI30 certifies support avoidance, then every term in the correction sum is zero and

\[
\boxed{v_p(D_m)=v_p(F_m).}
\]

This is why the earlier one-unit half-defect conjecture was correctly split into two logically independent questions:

- support avoidance;
- simple midpoint lifting modulo `p^2`.

The universal companion solves the **form** of the first question, just as the parameter-transversality theorem solves the **form** of the second.

---

## 4. P022-LI31 — forced midpoint divisibility can cancel completely

The prime

\[
\boxed{p=157}
\]

is the first sharp counterexample to the attractive but false generalization

\[
p\mid F_m
\Longrightarrow
p\mid D_m.
\]

Here

\[
m=78,
\qquad
2m-1=155=5\cdot31.
\]

The canonical A-elimination is

\[
\boxed{
A_{78}
=
A_1^2A_2^{-1}A_3^2A_4^{-1}
A_6A_7^{-1}A_{15}^{-1}A_{16}A_{77}.}
\]

The universal midpoint companion has

\[
157\mid N_{62}.
\]

Since

\[
78-62=16,
\]

LI30 gives

\[
157\mid F_{16}.
\]

Exact valuations are

\[
\boxed{
v_{157}(F_{78})=1,}
\]

\[
\boxed{
v_{157}(F_{16})=1.}
\]

No other index in the canonical A-support contributes a `157`-valuation.  The exponent of `A_16` in the elimination is `+1`.  Hence

\[
\boxed{
v_{157}(D_{78})=1-1=0.}
\]

The forced midpoint witness has been erased exactly by the canonical A-elimination.

---

## 5. Why this counterexample matters

The infinite half-index theorem used the narrower prime classes

\[
p\equiv5,23\pmod{24},
\]

which satisfy `p≡2 mod 3` and force the A-boundary `p-2` to be composite.

The cancellation example

\[
157\equiv13\pmod{24}
\]

lies outside that family.

This does **not** prove that the residue restriction itself guarantees support avoidance.  It does show that the restriction is not cosmetic: among the broader forced-midpoint primes, support cancellation genuinely occurs.

Current exact pressure tests on the target `5,23 mod 24` family have not found a support hit in the tested range, but that remains finite evidence until a theorem is proved.

---

## 6. The new arithmetic frontier

For the target family, the support question is now:

\[
\boxed{
\text{prove or disprove }
 p\nmid N_{m-j}
\text{ for every canonical support index }j.}
\]

The canonical support comes from recursively expressing the integers `m` and `p-2` in the central-binomial prime basis.  The zero side is now the single universal numerator sequence `N_d`.

This exposes the missing theorem much more sharply than the former statement `S_p cap Z_p = empty`:

> **Companion-support avoidance problem.**  Show that, for the target residue family `p=5,23 mod 24`, the offset image of the canonical A-elimination support avoids the `p`-divisor set of the universal midpoint companion numerator sequence.

A counterexample would be equally valuable, because it would identify the first exact cancellation mechanism inside the target infinite family.

---

## 7. Precision interpretation

This is a concrete negative boundary for task-relative repair.

A local witness `p|F_m` is not automatically a stable witness after changing coordinates by a canonical quotient/elimination.  The transformed observable may cancel it against retained lower-level coordinates.

Thus

\[
\boxed{
\text{local visibility}
\not\Rightarrow
\text{quotient-stable visibility}.}
\]

The surviving state depends on the future computation—in this case, the exact A-elimination used to define the pure defect.

This is P022 evidence for the generic A2/P023 principle that witness sufficiency must be checked **after** the declared quotient/operation algebra, not before it.

---

## 8. Executable assets

Added:

- `src/enterprise_math/p022_barlow_half_support_companion.py`;
- `tests/test_p022_barlow_half_support_companion.py`.

The tests cross-check direct Franel support hits against the companion coordinate and retain `p=157` as an exact cancellation counterexample with `v_157(D_78)=0`.
