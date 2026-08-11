# P018 — Galois polarity, Ferrers conjugacy, and safe-translation bridge

Status: `ORDINARY MATHEMATICS PROVED / LEAN POLARITY UNIT WRITTEN / LEAN NOT YET VERIFIED`

Scope: P018 quotient-root atlas, floor-power duality, finite-collapse safe translations.

## 1. Dual profiles

Fix integers `r >= 1`, `n >= 1`. For positive coordinates define

\[
F(d)=R_r\!\left(\left\lfloor\frac nd\right\rfloor\right),
\qquad
G(t)=\left\lfloor\frac n{t^r}\right\rfloor.
\]

On `1 <= d <= n` and `1 <= t <= R_r(n)`, both profiles are positive and antitone. They satisfy the exact polarity

\[
\boxed{t\le F(d)\iff d\le G(t).}
\]

Both sides are simply equivalent to `d t^r <= n`.

The Lean theorem unit for this polarity and the two strict-drop criteria is written in
`EnterpriseMath/Precision/QuotientRootFloorPowerDuality.lean` on the P018 owner branch. It is not yet kernel-verified.

## 2. Ferrers / conjugate-partition form

Let the positive row lengths be

\[
\lambda_t=G(t),\qquad 1\le t\le R_r(n).
\]

The height of column `d` is

\[
\#\{t:d\le G(t)\}=F(d).
\]

Hence the powered-floor partition and quotient-root partition are conjugate Ferrers diagrams:

\[
\boxed{\lambda'_d=F(d).}
\]

For `r=1`, `F=G`, so the classical floor-quotient Ferrers diagram is self-conjugate. For `r>1`, the region `d t^r <= n` is anisotropic and the conjugate coordinate is the quotient-root profile.

This is a direct application of standard partition conjugacy; no novelty claim is made for the abstract Ferrers mechanism.

## 3. Dual fiber-width / discrete-gradient laws

The exact quotient-root fiber theorem becomes

\[
F(d)=t
\iff
G(t+1)<d\le G(t).
\]

Therefore

\[
\boxed{\#F^{-1}(t)=G(t)-G(t+1).}
\]

By the polarity, the symmetric powered-floor fiber is

\[
G(t)=d
\iff
F(d+1)<t\le F(d),
\]

and hence

\[
\boxed{\#G^{-1}(d)=F(d)-F(d+1).}
\]

Thus collapse multiplicity in one coordinate is the exact discrete derivative of the dual coordinate.

In particular:

\[
t\in \operatorname{Im}(F)
\iff G(t+1)<G(t),
\]

and

\[
d\in \operatorname{Im}(G)
\iff F(d+1)<F(d).
\]

The quotient-root atlas is exactly the support of the discrete gradient of `G`.

## 4. Canonical endpoint closures

Define

\[
C_D(d)=G(F(d)),\qquad C_T(t)=F(G(t)).
\]

On the positive bounded domains these are monotone, extensive, idempotent closure maps.

- `C_D(d)` is the right endpoint of the entire denominator fiber containing `d`.
- `C_T(t)` is the right endpoint of the entire powered-floor plateau containing `t`.

Their fixed-point sets are

\[
\operatorname{Fix}(C_D)=\operatorname{Im}(G),
\qquad
\operatorname{Fix}(C_T)=\operatorname{Im}(F).
\]

The restrictions of `F` and `G` give mutually inverse order-reversing bijections between these two fixed-point sets.

Thus the dual profile does not merely count a collapse quotient: it supplies a canonical maximal representative for every collapse fiber.

## 5. Generic closure criterion for safe endomaps

Let `q` be a collapse with a canonical representative closure `C` such that

\[
q(x)=q(y)\iff C(x)=C(y),
\qquad C^2=C.
\]

An endomap `u` respects the collapse fibers iff

\[
\boxed{C\circ u=C\circ u\circ C.}
\]

Indeed, `x` and `C(x)` lie in the same fiber. Safety gives the displayed absorption identity; conversely the identity makes `C(u(x))` depend only on `C(x)` and hence only on the coarse state.

This is a closure-normal-form version of the safe-operation condition already used elsewhere in the precision calculus.

## 6. Safe translations from the drop set

Now let `q : N_{>0} -> L` be any nonincreasing eventually-constant collapse and let

\[
B_q=\{b\ge1:q(b)>q(b+1)\}
\]

be its finite strict-drop set. Translation by `a >= 0` is safe exactly when

\[
\boxed{
\forall b\in B_q,\quad b>a\Longrightarrow b-a\in B_q.
}
\]

### Proof

If translation by `a` is safe, take a drop `b>a` and put `x=b-a`. If `x` were not a drop, then `q(x)=q(x+1)`; safety would imply `q(b)=q(b+1)`, contradiction.

Conversely, suppose the backward-drop condition holds and `q(x)=q(y)` with `x<y`. If `q(x+a) != q(y+a)`, monotonicity produces a strict drop `b` between `x+a` and `y+a-1`. Then `b-a` is a strict drop between `x` and `y-1`, contradicting equality of the original endpoint values.

Hence translation safety is encoded entirely by the boundary set, not by all pairs of fine states.

## 7. Numerical-semigroup theorem

Let

\[
\mathcal S_q^{\rm tr}
=\{a\in\mathbb N_0:\text{translation by }a\text{ is }q\text{-safe}\}.
\]

The drop criterion immediately gives

\[
0\in\mathcal S_q^{\rm tr},
\qquad
a,b\in\mathcal S_q^{\rm tr}\Rightarrow a+b\in\mathcal S_q^{\rm tr}.
\]

If `B_q` is finite with maximum `M`, every `a >= M` is vacuously safe. Therefore

\[
\boxed{\mathcal S_q^{\rm tr}\text{ is a cofinite additive submonoid of }\mathbb N_0,}
\]

that is, a numerical semigroup (with the constant-collapse case giving all of `N_0`).

This strictly strengthens the statement that safe translations merely form an additive monoid for finite monotone collapses.

## 8. Exact unsafe-shift set and conductor

For `0 < a < M`, translation by `a` is unsafe iff there exist

\[
b\in B_q,\qquad 1\le c<b,\qquad c\notin B_q,
\qquad a=b-c.
\]

Hence

\[
\boxed{
\mathbb N_{>0}\setminus\mathcal S_q^{\rm tr}
=
\{b-c:b\in B_q,\ 1\le c<b,\ c\notin B_q\}.
}
\]

If `B_q={1,2,...,M}`, then every nonnegative translation is safe. Otherwise let

\[
g=\min\{c\ge1:c\notin B_q\}.
\]

Since `M in B_q`, the largest unsafe shift is exactly `M-g`. Thus the numerical-semigroup conductor is

\[
\boxed{c(\mathcal S_q^{\rm tr})=M-g+1.}
\]

## 9. Specialization to P018

For

\[
q(t)=G(t)=\left\lfloor\frac n{t^r}\right\rfloor,
\]

the strict-drop theorem gives

\[
\boxed{B_q=\mathcal A_{r,n}.}
\]

Therefore the complete safe-translation monoid is

\[
\boxed{
\mathcal S_{r,n}^{\rm tr}
=
\left\{a\ge0:
\forall t\in\mathcal A_{r,n},\ t>a\Rightarrow t-a\in\mathcal A_{r,n}
\right\}.
}
\]

The same quotient-root atlas therefore simultaneously records:

1. the positive coarse states of the quotient-root collapse;
2. the strict boundary/corner set of the powered-floor collapse;
3. all legal additive translations of that powered-floor collapse.

Moreover `max A_{r,n}=R_r(n)`, so the conductor is always at most `R_r(n)`.

If the first missing atlas state is `g`, then

\[
\boxed{c(\mathcal S_{r,n}^{\rm tr})=R_r(n)-g+1.}
\]

Using the P018 low-state completeness theorem:

- when the horizon state `H` is absent (`kappa=0`), the first hole is exactly `H`, hence
  \[
  c=R_r(n)-H+1;
  \]
- when `H` is present (`kappa=1`), the first hole lies strictly above `H`, so
  \[
  c\le R_r(n)-H.
  \]

This gives a new operational meaning to the horizon carry: filling the horizon state strictly lowers the eventual safe-translation conductor.

## 10. Generic Ferrers saturation defect

For any nonincreasing eventually-zero integer profile `G`, let `V(G)` be the number of distinct positive values. For every cut `k`,

\[
V(G)+1\le k+G(k).
\]

More exactly, writing `v=G(k)`,

\[
\boxed{
 k+v-(V(G)+1)
 =
 \underbrace{(k-1)-\#\{G(i)>v\}}_{\text{high collision defect}}
 +
 \underbrace{v-\#(\operatorname{Im}G\cap\{1,\ldots,v\})}_{\text{low hole defect}}.
}
\]

Thus

\[
\delta(G):=\min_k(k+G(k))-(V(G)+1)\ge0
\]

is a natural collapse-profile saturation defect.

For the power profile `G(t)=floor(n/t^r)`, P018 proves both defect terms vanish at the relevant horizon cut, so

\[
\boxed{\delta(G)=0.}
\]

This isolates the genuinely special number-theoretic content from the generic Ferrers/Galois duality: the power profile is corner-saturated.

## 11. Validation and novelty boundary

The safe-translation/drop-set equivalence was independently brute-force checked on 5,000 random finite nonincreasing sequences and on representative P018 powered-floor profiles; no counterexample was found. This validation is not a proof; the proof is the elementary argument in Section 6.

The Ferrers conjugacy and abstract Galois/closure mechanisms are standard order/combinatorial structures. The specialization to the P018 collapse and the numerical-semigroup/conductor bridge are recorded as `NOVELTY_UNRESOLVED`; no originality claim is made without a dedicated literature search.

## 12. Next theorem units

1. Kernel-check `QuotientRootFloorPowerDuality.lean` locally when a Lean runtime is available; do not use Draft CI as a research service.
2. Formalize the symmetric fiber-width laws.
3. Formalize the generic safe-translation/drop-boundary theorem independently of P018.
4. Instantiate it with `B_q = rootStateAtlas` to obtain the P018 safe-translation numerical semigroup.
5. Investigate whether the saturation-defect invariant classifies broader collapse profiles beyond powers.
