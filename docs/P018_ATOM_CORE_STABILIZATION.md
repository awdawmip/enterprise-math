# P018 — Eventual atom-core stabilization of the powered quotient-root atlas

Status: `ORDINARY MATHEMATICS PROVED / NOVELTY UNRESOLVED / LEAN NOT YET VERIFIED`

Scope: P018 quotient-root atlas specialization. Generic numerical-set / atom-monoid facts are prior art; this note records the powered-floor arithmetic theorem obtained after transporting that theory into P018.

## 1. Setup

Fix an integer `r >= 2`. For `n >= 1` put

\[
b_d(n):=R_r\!\left(\left\lfloor\frac nd\right\rfloor\right),\qquad
B_{r,n}:=\{b_d(n):1\le d\le n\},\qquad
M_n:=b_1(n).
\]

Let `K(B_{r,n})` be the minimal boundary with the same safe-translation atom monoid, as defined in `P018_POWER_ATLAS_ATOM_MONOID_BRIDGE.md`, and define the removable operation-neutral redundancy

\[
\rho_r(n):=|B_{r,n}\setminus K(B_{r,n})|.
\]

The previous checkpoint proved `rho_1(n)=0` for every `n`, while `rho_r(n)>=1` eventually for every fixed `r>=2`.

This note sharpens the higher-order statement to an exact eventual constant.

## 2. Generic top-shell lemma

Let `B` be a finite positive boundary set with maximum `M`, and let `sigma` be its second-largest element. Then

\[
\boxed{B\setminus K(B)\subseteq B\cap(M-\sigma,M).}
\]

Indeed, if `b <= M-sigma`, then the reflected shift `a=M-b` satisfies `a>=sigma`. The only boundary strictly larger than `a` is then `M`, and its translate is `M-a=b in B`. Hence `a` is safe and `b` belongs to the operational core.

Thus operation-neutral deletion can occur only in the additive top shell cut out by the second-largest boundary state.

## 3. Powered top-shell scale

For fixed `d`,

\[
\frac{b_d(n)}{n^{1/r}}\longrightarrow d^{-1/r}.
\]

For all sufficiently large `n`, `b_2(n)<M_n`, so `b_2(n)` is the second-largest atlas state. Therefore

\[
\frac{M_n-b_2(n)}{n^{1/r}}
\longrightarrow
\alpha_r:=1-2^{-1/r}>0.
\]

Define

\[
L_r:=\alpha_r^{-r}=(1-2^{-1/r})^{-r}.
\]

### Lemma — `L_r` is irrational

Let `x=2^{1/r}`. Then

\[
L_r=\frac{2}{(x-1)^r}.
\]

By Eisenstein at `2`, `X^r-2` is irreducible, so `1,x,...,x^{r-1}` are linearly independent over `Q`. The expansion of `(x-1)^r`, after replacing `x^r` by `2`, has nonzero `x^{r-1}` coefficient. Hence `(x-1)^r` is irrational, and so is `L_r`.

Put

\[
m_r:=\lfloor L_r\rfloor,
\qquad
J_r:=m_r-1.
\]

The integer denominator labels lying strictly inside the limiting top shell are exactly

\[
2,3,\ldots,m_r,
\]

and there are exactly `J_r` of them.

## 4. Upper bound — no redundancy outside the finite denominator shell

Since

\[
(m_r+1)^{-1/r}<\alpha_r,
\]

we have, for all sufficiently large `n`,

\[
b_{m_r+1}(n)\le M_n-b_2(n).
\]

Because `d -> b_d(n)` is nonincreasing, every atlas state whose first denominator label is at least `m_r+1` also lies at or below `M_n-b_2(n)`. By the generic top-shell lemma it belongs to the operational core.

Consequently

\[
\boxed{\rho_r(n)\le J_r\qquad(n\gg_r1).}
\]

This already proves that, for fixed root order, operation-neutral redundancy is a bounded top-shell effect rather than a quantity that grows with raw precision `n`.

## 5. Radical no-resonance lemma

The lower bound requires showing that each candidate denominator `2<=d<=m_r` really becomes redundant.

### Lemma

For integers `r>=2`, `d>=2`, and `k>=1`, there is no equality

\[
\boxed{
d^{-1/r}+2^{-1/r}-1=k^{-1/r}.
}
\]

### Proof

For a positive integer `a`, the algebraic number `a^{-1/r}` has one of two forms:

1. it is rational, in which case `a=c^r` for an integer `c`, and if `a>=2` then `a^{-1/r}=1/c<=1/2`;
2. it is irrational, in which case its minimal polynomial is a binomial `X^m-q` with `m>1`, after extracting the maximal common power from the prime valuations of `a`; hence its field trace to `Q` is zero.

Let

\[
u=d^{-1/r},\qquad v=2^{-1/r},\qquad w=k^{-1/r},
\]

and let `K/Q` be a finite field containing `u,v,w`. Normalize the field trace by

\[
\tau(y)=\frac{\operatorname{Tr}_{K/\mathbb Q}(y)}{[K:\mathbb Q]}.
\]

The number `v` is irrational, so `tau(v)=0`. Moreover `tau(u)` is either `0` or the rational number `u<=1/2`, while `tau(w)` is either `0` or the positive rational number `w`.

Applying `tau` to `u+v-1=w` gives

\[
\tau(u)-1=\tau(w).
\]

The left side is at most `-1/2`, while the right side is nonnegative, contradiction.

Thus no radical resonance is possible.

## 6. Lower bound — every candidate top-shell state is eventually removable

Fix `d` with `2<=d<=m_r`. Since `d<L_r`,

\[
\gamma_{r,d}:=d^{-1/r}+2^{-1/r}-1>0.
\]

Define

\[
z_d(n):=b_d(n)+b_2(n)-M_n.
\]

Then

\[
\frac{z_d(n)}{n^{1/r}}\longrightarrow\gamma_{r,d}>0.
\]

Suppose `z_d(n)` belonged to `B_{r,n}` for infinitely many `n`. Choose denominator labels `k_n` such that

\[
z_d(n)=b_{k_n}(n).
\]

Because `z_d(n)/n^{1/r}` stays bounded away from zero, the inequalities defining the integer root force `k_n` to remain bounded. Passing to a subsequence gives a fixed `k`, and dividing by `n^{1/r}` yields

\[
\gamma_{r,d}=k^{-1/r},
\]

contradicting the radical no-resonance lemma.

Hence eventually

\[
z_d(n)\notin B_{r,n}.
\]

At the same time `z_d(n)>0`, equivalently

\[
b_2(n)>M_n-b_d(n).
\]

Therefore the reflected shift `a=M_n-b_d(n)` is unsafe, witnessed by the boundary `b_2(n)`, because

\[
b_2(n)-a=z_d(n)\notin B_{r,n}.
\]

Thus `b_d(n)` is eventually absent from the operational core.

The finitely many values `b_2(n),...,b_{m_r}(n)` are pairwise distinct for all sufficiently large `n`, since their normalized limits `d^{-1/r}` are distinct. Therefore

\[
\boxed{\rho_r(n)\ge J_r\qquad(n\gg_r1).}
\]

## 7. Exact stabilization theorem

Combining the upper and lower bounds:

\[
\boxed{
\rho_r(n)
=
J_r
=
\left\lfloor(1-2^{-1/r})^{-r}\right\rfloor-1
\qquad(n\gg_r1,\ r\ge2).
}
\]

Together with the classical `r=1` result,

\[
\boxed{
\rho_1(n)=0\quad\forall n,
\qquad
\rho_r(n)=J_r>0\quad(n\gg_r1,\ r\ge2).
}
\]

First constants:

\[
J_2=10,\qquad J_3=112,\qquad J_4=1559,\qquad J_5=27509.
\]

The theorem is an existence-of-threshold statement. No small or uniform stabilization threshold in `n` is claimed.

## 8. Core cardinality and genus corollaries

Let

\[
N_r(n):=|B_{r,n}|.
\]

Then eventually

\[
\boxed{|K(B_{r,n})|=N_r(n)-J_r.}
\]

Hence the operational core has exactly the same growth order as the raw quotient-root atlas and differs from it by only a root-order-dependent constant.

Let `T_{r,n}=T_{B_{r,n}}` be the reflected numerical set and `S_{r,n}=A(T_{r,n})` its safe-translation semigroup. Since

\[
g(T_{r,n})=M_n-N_r(n),
\]

and the core is the reflection of `S_{r,n}` below `M_n`,

\[
\boxed{
\rho_r(n)=g(S_{r,n})-g(T_{r,n}).
}
\]

Therefore eventually

\[
\boxed{
g(S_{r,n})=M_n-N_r(n)+J_r.}
\]

This identifies operation-neutral deletion exactly with the genus increase caused by passing from the raw numerical set to its atom monoid.

## 9. Vanishing removable fraction

The exact P018 cardinality localization gives

\[
N_r(n)\asymp_r n^{1/(r+1)}.
\]

Since `rho_r(n)=J_r` eventually,

\[
\boxed{
\frac{\rho_r(n)}{N_r(n)}\longrightarrow0
\qquad(n\to\infty,\ r\text{ fixed}).
}
\]

Thus higher-order collapse necessarily creates some operation-neutral distinctions, but asymptotically almost every observed quotient-root state remains necessary for the maximal safe translation language.

This corrects the discarded conjectural direction that `rho_r(n)` might be unbounded in `n`.

## 10. Large-order behavior

Write `a=log 2`. Since

\[
1-2^{-1/r}
=1-e^{-a/r}
=\frac ar\left(1-\frac{a}{2r}+O(r^{-2})\right),
\]

we obtain

\[
L_r
=\sqrt2\left(\frac r{\log2}\right)^r\left(1+O(r^{-1})\right).
\]

Therefore

\[
\boxed{
J_r\sim\sqrt2\left(\frac r{\log2}\right)^r
\qquad(r\to\infty).
}
\]

So there are two sharply different limits:

- fixed `r`, increasing raw precision `n`: removable redundancy stabilizes to a finite shell;
- increasing collapse order `r`: the capacity of that eventual shell grows extremely rapidly.

No joint asymptotic in `r,n` is asserted.

## 11. Latent neutral refinement is large even though actual redundancy is small

Generic numerical-set theory gives, for a numerical semigroup `S`,

\[
S\subseteq T\subseteq S^*,
\qquad
|S^*\setminus S|=2g(S)-F(S)-1
\]

for every numerical set `T` with atom monoid `S`.

Let `P_{r,n}` be the largest integer such that `[1,P_{r,n}] subseteq B_{r,n}`. The safe semigroup conductor is

\[
c(S_{r,n})=M_n-P_{r,n},
\]

so `F(S_{r,n})=M_n-P_{r,n}-1`.

At eventual stabilization, the already-present removable neutral detail is `rho_-=J_r`. The still-addable neutral capacity up to the maximal associated numerical set is therefore

\[
\boxed{
\rho_+(r,n)
=M_n+P_{r,n}-2N_r(n)+J_r.
}
\]

Because `P_{r,n}<=N_r(n)=O_r(n^{1/(r+1)})` while `M_n~n^{1/r}`, we get

\[
\boxed{
\rho_+(r,n)\sim n^{1/r}.
}
\]

Hence the natural powered atlas is highly asymmetric inside its same-language anti-atom fiber:

\[
\boxed{
\text{distance to minimal operational core}=O_r(1),
\qquad
\text{distance to maximal neutral envelope}\asymp n^{1/r}.
}
\]

The natural atlas is therefore **near-minimal for its future translation language**, even though that same language permits a very large neutral refinement envelope.

## 12. Computational sanity checks

Independent exact-integer calculations were used only as sanity checks, not proofs.

Examples along `n=10^k`:

- `r=2`: redundancy reaches the predicted value `J_2=10` by `n=10^15` in the tested sequence and remains `10` through larger tested powers;
- `r=3`: at `n=10^40`, redundancy is `111`, already one below the predicted eventual value `112`;
- `r=4`: at `n=10^40`, redundancy is `1058`, still below the predicted eventual value `1559`, illustrating that the stabilization threshold can be very large.

These observations are consistent with, but are not used in, the proof.

## 13. Prior-art boundary

Generic facts used here are prior art:

- atom monoid / associated semigroup of a numerical set;
- the anti-atom problem;
- `S subseteq T subseteq S^*` for `A(T)=S`;
- the void size `|S^*\setminus S|=2g(S)-F(S)-1`.

Relevant source: Chen–Kaplan–Lawson–O'Neill–Singhal, *Enumerating numerical sets associated to a numerical semigroup*, arXiv:2211.17090 (with earlier results cited there).

The powered-floor exact cardinality is also prior-art-equivalent via the previously recorded Heyman–Miraj bridge.

A targeted search at this checkpoint did not locate the specific powered-floor/quotient-root theorem

\[
\rho_r(n)\to \left\lfloor(1-2^{-1/r})^{-r}\right\rfloor-1,
\]

nor the near-minimal / large-latent-envelope asymmetry above. This is not a novelty proof. Keep these claims at `NOVELTY_UNRESOLVED` until a dedicated literature review is completed.

## 14. Next theorem units

1. Formalize the generic finite-boundary top-shell lemma in the shared operation-quotient layer rather than duplicating numerical-set theory in P018.
2. In P018, formalize the fixed-denominator root scaling and the finite-shell upper bound.
3. Isolate the radical trace no-resonance lemma as a reusable arithmetic theorem.
4. Prove the exact eventual stabilization theorem after those units are kernel-checked.
5. Only then study effective stabilization thresholds in `n`; do not conflate the existence theorem with a practical small threshold.
