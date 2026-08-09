# P022 — Checkpoint Objectives as Different Functionals of One Collision Polynomial

Status: `ACTIVE RESEARCH NOTE / P022 SPECIALIZATION`  
Owner: `program/p022-geometry-v2`  
Generic dependency: P011 collision polynomial identities relayed to A1/P011  
Cross-route relevance: P011 complete fiber statistics; P023/P024 objective-relative precision

## 1. One complete state, several incompatible objectives

P011's collision polynomial is

\[
K_O(t)
=
\sum_y\left((1+t)^{m_y}-1\right)
=
\sum_{k\ge1}J_k(O)t^k,
\]

where the positive integers `m_y` are the microscopic fiber sizes of an observation quotient `O`.

During P022 checkpoint scheduling, several apparently different precision objectives appeared:

- number of represented coarse states;
- pair collisions;
- largest microscopic ambiguity block;
- number of largest ambiguity blocks;
- residual checkpoint-order repair after keeping the complete collision state.

They can now all be read from the same complete collision polynomial, although they are **different functionals** of it.

---

## 2. Generic P011 identities consumed by P022

The following algebraic identities do not depend on Barlow geometry and were relayed upstream to P011/A1.

### Image cardinality

Every positive fiber contributes

\[
(1-1)^{m_y}-1=-1
\]

at `t=-1`.  Hence

\[
\boxed{
K_O(-1)=-|\operatorname{im}O|.
}
\]

Thus

\[
\boxed{
|\operatorname{im}O|=-K_O(-1).
}
\]

### Maximum fiber size

The largest exponent appearing in `K_O` is exactly the largest fiber size:

\[
\boxed{
\deg K_O=\max_y m_y.
}
\]

### Number of maximum fibers

If

\[
d=\deg K_O,
\]

then every fiber of size `d` contributes leading coefficient one and every smaller fiber contributes zero at degree `d`. Therefore

\[
\boxed{
[t^d]K_O
=
\#\{y:m_y=d\}.
}
\]

These are generic P011 consequences. P022 does not claim their mother-theorem ownership.

---

## 3. P022-CO01 — five checkpoint objectives from the complete collision state

For a Barlow selected-layer quotient, the following finite objectives are now available:

### A. Image capacity

\[
\boxed{
I(O)=-K_O(-1).
}
\]

### B. Pair ambiguity

\[
\boxed{
P_2(O)=[t^2]K_O=J_2(O).
}
\]

### C. Worst microscopic fiber

\[
\boxed{
W(O)=\deg K_O.
}
\]

### D. Number of worst fibers

\[
\boxed{
C_{\max}(O)=[t^{\deg K_O}]K_O.
}
\]

### E. Post-aggregation checkpoint-order repair

The complete P022 inverse recovers the segment multiset from `K_O`, so if its value multiplicities are `t_ell`,

\[
\boxed{
M_{\rm ord}(O)
=
\frac{m!}{\prod_\ell t_\ell!}.
}
\]

Unlike A–D, the last quantity uses the structured P022 inverse from collision state back to unordered checkpoint geometry.  It is not a generic P011 functional for arbitrary finite maps.

---

## 4. P022-CO02 — the minimal coefficient/degree conflict

Take total length four with two final-observing checkpoints.

### Balanced segments `(2,2)`

The microscopic fiber profile is

\[
\{1\times4,\ 2\times4,\ 4\times1\}.
\]

Hence

\[
\boxed{
K_{bal}(t)
=16t+10t^2+4t^3+t^4.
}
\]

It has

\[
I=9,
\qquad
J_2=10,
\qquad
\deg K=4.
\]

### Unbalanced segments `(1,3)`

The fiber profile is

\[
\{1\times4,\ 3\times4\},
\]

so

\[
\boxed{
K_{unbal}(t)
=16t+12t^2+4t^3.
}
\]

It has

\[
I=8,
\qquad
J_2=12,
\qquad
\deg K=3.
\]

Therefore

\[
\boxed{
I_{bal}>I_{unbal},
\qquad
J_2^{bal}<J_2^{unbal},
\qquad
\deg K_{bal}>\deg K_{unbal}.
}
\]

The schedule that is better for image capacity and pair ambiguity is strictly worse for the largest single ambiguity block.

This is one polynomial-level restatement of the earlier higher-collision phase conflict.

---

## 5. P022-CO03 — complete-state order repair creates another conflict

At

\[
N=10,\qquad m=4,
\]

compare

\[
(2,2,3,3)
\]

with

\[
(1,3,3,3).
\]

The ordinary balanced schedule has

\[
I=144,
\qquad
J_2=6688,
\qquad
M_{\rm ord}=6.
\]

The concentrated-multiplicity schedule has

\[
I=128,
\qquad
J_2=7488,
\qquad
M_{\rm ord}=4.
\]

Thus

\[
\boxed{
\text{balanced improves }I\text{ and }J_2,
\quad
\text{but worsens }M_{\rm ord}.
}
\]

Even the **complete** collision state therefore does not produce a universal scheduling optimum.  Which functional matters depends on the declared future cost.

---

## 6. The precision lesson is not “choose another scalar”

One might try to replace `J_2` by degree, or degree by image size, and call that the new precision score.  The exact examples above show why that is structurally wrong.

The complete collision polynomial already contains all of them, but different downstream questions apply different functionals:

\[
\boxed{
K_O
\xrightarrow{-K(-1)}I,
\qquad
K_O\xrightarrow{[t^2]}J_2,
\qquad
K_O\xrightarrow{\deg}W,
\qquad
K_O\xrightarrow{\text{P022 inverse}}M_{\rm ord}.
}
\]

A future language that asks “how many states remain distinguishable?” and one that asks “what is the largest hidden ambiguity?” are not the same language even though they share one sufficient collision state.

So the correct architecture is

\[
\boxed{
\text{complete finite state}
+\text{declared future functional},
}
\]

not a universal scalar precision ranking.

---

## 7. Ownership boundary

The generic identities

\[
K(-1)=-|\operatorname{im}|,
\quad
\deg K=\max\text{ fiber},
\quad
\text{leading coefficient}=\#\text{max fibers}
\]

belong to P011/A1 and have been relayed there.

P022 owns only:

- their use on checkpoint geometry;
- the explicit schedule tradeoffs;
- the structured order-repair inverse from the complete collision state.

This preserves Architecture-v2 mother-theorem ownership.

---

## 8. Executable assets

Added on the P022 owner:

- `src/enterprise_math/p022_barlow_collision_objectives.py`;
- `tests/test_p022_barlow_collision_objectives.py`.

The tests reconstruct image/degree/leading coefficient from the independently inverted fiber profile and encode the exact `(2,2)` versus `(1,3)` and `N=10,m=4` objective conflicts.
