# E001/E002 — Symmetric Contact Action-Family Supplement 01

Status: `ACTIVE CROSS-ROUTE ENGINEERING NOTE`  
Scope: Boolean E001 contact under a symmetric finite integer gap-action family  
Parent: `docs/E001_E002_PREDICTIVE_CONTACT_BRIDGE.en.md`  
Dependencies: E001 `Contact_d(g) iff g<d`; E002/P023 predictive quotient; E002 Stage-2 gcd-safe actuation

## 1. Question

The parent bridge showed that if the only bidirectional gap actions are `+a` and lower-clipped `-a`, then

\[
K_{d,a}(x)=\left\lceil\frac{d-x}{a}\right\rceil
\]

is the exact coarsest arbitrary-future state for the Boolean query `x<d`.

A real finite engine may expose several admissible motion magnitudes. This supplement asks whether one must retain a separate phase coordinate for each magnitude or whether the whole symmetric action family collapses to one arithmetic invariant.

## 2. Symmetric action family

Let the positive action magnitudes be

\[
A=\{a_1,\ldots,a_m\}\subset\mathbb N_{>0}.
\]

The declared physical action language contains both directions for every magnitude:

\[
S_j(x)=x+a_j,
\qquad
C_j(x)=\max(0,x-a_j).
\]

Define the common action grain

\[
\boxed{g=\gcd(a_1,\ldots,a_m)}
\]

and normalized integer steps

\[
m_j=a_j/g.
\]

Then

\[
\gcd(m_1,\ldots,m_m)=1.
\]

## 3. E001/E002-T38 — Exact gcd contact coordinate

Define

\[
\boxed{
K_{d,A}(x)
=\left\lceil\frac{d-x}{g}\right\rceil.
}
\]

Let

\[
K_{\max}=K_{d,A}(0)=\left\lceil\frac dg\right\rceil.
\]

Then the current Boolean observation and every declared action factor exactly through `K`:

\[
\boxed{x<d\iff K_{d,A}(x)\ge1,}
\]

\[
\boxed{K_{d,A}(S_j(x))=K_{d,A}(x)-m_j,}
\]

and

\[
\boxed{
K_{d,A}(C_j(x))
=\min(K_{d,A}(x)+m_j,K_{\max}).
}
\]

### Proof

Write

\[
K(x)=\left\lceil\frac{d-x}{g}\right\rceil.
\]

Since `a_j=m_jg`,

\[
K(x+a_j)
=\left\lceil\frac{d-x-m_jg}{g}\right\rceil
=K(x)-m_j.
\]

For closing without ground clipping,

\[
K(x-a_j)=K(x)+m_j.
\]

If `x-a_j<0`, the physical result is `0`, so the quotient result is `K_max`. Hence the clipped formula is the minimum above.

Finally, for integer `x`,

\[
\left\lceil\frac{d-x}{g}\right\rceil\ge1
\iff d-x>0
\iff x<d.
\]

Thus the quotient is exact. ∎

## 4. Exact fibers

For a coordinate value `k`, the un-clipped integer fiber is

\[
\boxed{
d-kg\le x\le d-(k-1)g-1.}
\]

Intersecting with `x>=0` gives the physical fiber.

Except for the ground-clipped top fiber, every nonempty fiber therefore contains exactly `g` consecutive integer gap states.

So the action-family gcd has a direct predictive meaning: it is the width of the largest repeated gap-detail block that the complete symmetric action family can never distinguish under the Boolean contact query.

## 5. E001/E002-T39 — Coarsestness for arbitrary finite action words

`K_(d,A)` is not merely sufficient. It is the **coarsest** deterministic state that preserves Boolean contact under every finite word in the symmetric action family.

Equivalently,

\[
\boxed{
K(x)=K(y)
\iff
\operatorname{Contact}(T_vx)=\operatorname{Contact}(T_vy)
\text{ for every finite action word }v.
}
\]

### Same K implies behavioral equivalence

T38 provides an exact deterministic quotient update for every generator and factors the observation through `K`. By induction on word length, equal K-values remain equal after every finite action word and therefore always give the same Boolean contact observation.

### Distinct K-values are finitely distinguishable

Take

\[
k_1<k_2.
\]

If they already lie on opposite sides of the contact threshold `K=1`, the empty word distinguishes them.

Otherwise, because

\[
\gcd(m_1,\ldots,m_m)=1,
\]

Bezout gives an integer combination of the normalized generator magnitudes equal to any required integer shift. Since both `+a_j` and `-a_j` physical actions are declared, a finite action word can realize that signed combination in K-space.

Choose a net K-shift sending `k_2` to `1`. Then `k_1` is sent to

\[
1-(k_2-k_1)\le0.
\]

The final Boolean contact observations differ.

The ground-clipping cap does not invalidate this distinguishing word: realize the signed combination by performing all K-decreasing separation moves first and all K-increasing closing moves afterward. The intermediate coordinate first moves downward and then monotonically rises only to final value `1`, which never exceeds the physical cap `K_max>=1`. Hence no unintended clipping occurs.

Therefore no two distinct K-fibers may be merged. ∎

## 6. Relationship to Stage-2 gcd-safe actuation

This theorem is the Boolean-contact analogue of E002 Stage 2.

There, an integer action family selected the coarsest future-safe centered precision width through a gcd with the cell width. Here the Boolean contact threshold removes the need to retain an absolute centered-cell index/detail pair, and the action-family gcd itself becomes the width of the exact behavioral fibers aligned to the contact boundary.

The shared arithmetic skeleton is:

\[
\boxed{
\text{declared integer action family}
\longrightarrow
\text{gcd action grain}
\longrightarrow
\text{coarsest future-safe precision fibers}.
}
\]

The future observable still matters. A richer response language may refine these fibers.

## 7. Generic compiler reconstruction

A finite validation world may use gap states

\[
\{0,1,\ldots,G\}
\]

with both actions for every magnitude, using upper saturation only to close the finite test domain:

\[
x\mapsto\min(G,x+a_j),
\qquad
x\mapsto\max(0,x-a_j).
\]

The Stage-6 compiler receives only this finite transition system and observation `x<d`; it is not given the gcd formula.

Tests require the stable predictive partition to agree **state by state** with `K_(d,A)` on the finite world: each compiler block contains one K-value, and every K-value occupies exactly one compiler block.

This is a stronger audit than matching only the number of blocks.

## 8. Negative boundaries

### Asymmetry

T39 uses the symmetric language containing both `+a_j` and `-a_j`. If only some directions are available, the generated future semigroup need not realize all integer gcd translations, and K may cease to be minimal even though it remains sufficient for actions that factor through it.

### Richer collision response

The quotient is exact only for Boolean contact plus the declared gap actions. It need not preserve:

- exact clearance or penetration;
- impact timing below the declared sampling model;
- velocity/momentum;
- deformation/material state;
- rebound direction or magnitude.

Those variables/queries must be added to the future language and recompiled.

### Physical interpretation

The result is a finite integer state theorem inside the E001 engineering candidate. It does not by itself establish that real physical collision laws are governed by this contact quotient.

## 9. Executable assets

- `src/enterprise_math/predictive_contact_family.py`
- `tests/test_predictive_contact_family.py`
- `tests/test_predictive_contact_family_compiler.py`

The tests check exact action transport, bounded arbitrary-word behavioral equivalence, finite distinguishability of different K-values, fiber widths, and equality with the generic stable predictive compiler on several finite worlds.

## 10. Next pressure tests

1. remove action symmetry and characterize the semigroup-controlled minimal quotient;
2. make action availability state-dependent;
3. add explicit rebound/output state and compile the additional precision obligation;
4. lift the same gcd-family contact logic to vector pair separation and Boolean collision queries;
5. compare direct compiler runtime with the closed-form K implementation.
