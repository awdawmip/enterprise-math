# P018 — Exact atom-core shape, depth-two safe language, and sparse-to-dense precision fiber

Status: `ORDINARY MATHEMATICS PROVED / NOVELTY UNRESOLVED / LEAN NOT YET VERIFIED`

Scope: P018 powered quotient-root atlas after transport to the prior-art numerical-set / atom-monoid language. Generic numerical-semigroup facts are prior art; the powered-floor specialization below is the P018 content.

## 1. Setup and fixed-order constants

Fix an integer `r >= 2`. Put

\[
b_d(n):=R_r\!\left(\left\lfloor\frac nd\right\rfloor\right),\qquad
B_{r,n}:=\{b_d(n):1\le d\le n\},\qquad
M_n:=b_1(n).
\]

For real

\[
x=n^{1/r},
\]

one has the exact identity

\[
\boxed{b_d(n)=\lfloor x\,d^{-1/r}\rfloor.}
\]

Indeed an integer `m` satisfies `m^r <= n/d` iff `m^r <= floor(n/d)`.

Let

\[
\beta_r:=2^{-1/r},\qquad
L_r:=(1-\beta_r)^{-r},\qquad
D_r:=\lfloor L_r\rfloor,\qquad
J_r:=D_r-1.
\]

The previous stabilization checkpoint proves that `L_r` is nonintegral and

\[
\rho_r(n)=J_r
\]

for all sufficiently large `n`, where `rho_r(n)` is the number of boundary states removable without changing the safe-translation atom monoid.

## 2. Exact eventual core-set theorem

The stabilization result sharpens from a cardinality statement to an exact set statement.

### Theorem — exact top-shell deletion

For every fixed `r>=2`, there exists `N_r` such that for all `n>=N_r`:

1. `b_1(n)>b_2(n)>...>b_{D_r+1}(n)`;
2. the operation-neutral states are exactly

\[
\boxed{
B_{r,n}\setminus K(B_{r,n})
=
\{b_d(n):2\le d\le D_r\};
}
\]

3. equivalently,

\[
\boxed{
K(B_{r,n})
=
B_{r,n}\setminus\{b_2(n),\ldots,b_{D_r}(n)\}.
}
\]

### Proof structure

The generic top-shell lemma gives

\[
B\setminus K(B)\subseteq B\cap(M-\sigma,M),
\]

where `sigma` is the second-largest boundary. Here `sigma=b_2(n)` eventually.

For fixed `d`, define

\[
\gamma_{r,d}:=d^{-1/r}+2^{-1/r}-1.
\]

Then

\[
b_d(n)+b_2(n)-M_n
=
\gamma_{r,d}x+O(1).
\]

Because `L_r` is nonintegral,

\[
\gamma_{r,d}>0\iff d\le D_r,
\qquad
\gamma_{r,d}<0\iff d\ge D_r+1.
\]

Thus the limiting top shell contains exactly the denominator labels `1,...,D_r`; label `1` is the maximum and is always operational, leaving `2,...,D_r` as the only possible neutral states.

For each `2<=d<=D_r`, put

\[
z_d(n):=b_d(n)+b_2(n)-M_n.
\]

Then `z_d(n)>0` eventually and

\[
\frac{z_d(n)}x\to\gamma_{r,d}.
\]

The quotient-root / floor-power drop duality says

\[
z\in B_{r,n}
\iff
\left\lfloor\frac n{z^r}\right\rfloor
>
\left\lfloor\frac n{(z+1)^r}\right\rfloor.
\]

Both real quotients on the right converge, for `z=z_d(n)`, to

\[
\lambda_{r,d}:=\gamma_{r,d}^{-r}.
\]

The radical trace no-resonance theorem from the previous checkpoint implies `lambda_{r,d}` is not an integer: otherwise

\[
\gamma_{r,d}=k^{-1/r}
\]

for an integer `k`, contradicting

\[
d^{-1/r}+2^{-1/r}-1\ne k^{-1/r}.
\]

Hence the two adjacent floor-power values are eventually equal, so `z_d(n)` is eventually not an atlas state. The boundary `b_2(n)` therefore witnesses that the reflected shift `M_n-b_d(n)` is unsafe. This proves every `b_d`, `2<=d<=D_r`, is eventually removed from the core.

## 3. An effective stabilization criterion

The theorem above is asymptotic, but the proof yields a finite computable sufficient threshold.

For `2<=d<=D_r`, define

\[
\eta_{r,d}:=\operatorname{dist}(\lambda_{r,d},\mathbb Z)>0.
\]

Also put

\[
\Gamma_r^+:=\gamma_{r,D_r}>0,
\qquad
\Gamma_r^-:=-\gamma_{r,D_r+1}>0,
\]

and

\[
\Delta_r:=D_r^{-1/r}-(D_r+1)^{-1/r}>0.
\]

Since

\[
z_d(n)-\gamma_{r,d}x
=-\{xd^{-1/r}\}-\{x2^{-1/r}\}+\{x\},
\]

we have the uniform error interval

\[
-2<z_d(n)-\gamma_{r,d}x<1.
\]

On `u>=gamma_{r,d}/2`, the derivative of `u^{-r}` is bounded by

\[
r\,2^{r+1}\gamma_{r,d}^{-(r+1)}.
\]

Consequently one crude sufficient real-scale bound is

\[
X_r^{\rm eff}:=
\max\left\{
\frac4{\Gamma_r^+},
\frac2{\Gamma_r^-},
\frac2{\Delta_r},
\max_{2\le d\le D_r}
\frac{2^{r+3}r}{\eta_{r,d}\gamma_{r,d}^{r+1}}
\right\}.
\]

Then

\[
\boxed{n^{1/r}>X_r^{\rm eff}}
\]

is a sufficient condition for the exact core-set theorem above.

This bound is intentionally not optimized. Its role is conceptual: the stabilization delay is controlled by two finite algebraic margins:

- the **shell margin**, measuring how close `L_r` lies to its neighboring integers;
- the **drop-resonance margin** `eta_{r,d}`, measuring how close `gamma_{r,d}^{-r}` lies to an integer.

Thus very late stabilization is a finite Diophantine-separation phenomenon, not a failure of the eventual theorem.

## 4. Exact eventual multiplicity

Let

\[
S_{r,n}:=A(T_{B_{r,n}})
\]

be the safe-translation numerical semigroup, and let `mu_{r,n}` be its multiplicity (smallest positive safe translation).

Since the only eventual core states between `M_n` and `b_{D_r+1}(n)` are removed, the largest core state below `M_n` is exactly `b_{D_r+1}(n)`. Reflection therefore gives

\[
\boxed{
\mu_{r,n}=M_n-b_{D_r+1}(n)
\qquad(n\gg_r1).
}
\]

Define

\[
\theta_r:=1-(D_r+1)^{-1/r}.
\]

Then

\[
\boxed{
\frac{\mu_{r,n}}{n^{1/r}}\to\theta_r.
}
\]

Because `D_r+1>L_r`,

\[
(D_r+1)^{-1/r}<1-2^{-1/r},
\]

hence

\[
\boxed{
\theta_r>2^{-1/r}>\frac12.
}
\]

So the smallest nontrivial safe translation already consumes more than half of the ambient root scale.

## 5. Eventual depth two

Let `P_{r,n}` be the largest integer with

\[
[1,P_{r,n}]\subseteq B_{r,n}.
\]

The safe semigroup conductor is

\[
c_{r,n}=M_n-P_{r,n}.
\]

Since `P_{r,n}<=N_r(n)` and

\[
N_r(n)=O_r(n^{1/(r+1)}),
\qquad
M_n\sim n^{1/r},
\]

we have

\[
\frac{c_{r,n}}{n^{1/r}}\to1.
\]

Together with the multiplicity theorem,

\[
\frac{c_{r,n}}{\mu_{r,n}}
\to
\frac1{\theta_r}\in(1,2).
\]

Therefore, eventually,

\[
\boxed{
\mu_{r,n}<c_{r,n}<2\mu_{r,n}.
}
\]

In standard numerical-semigroup terminology the depth

\[
q(S):=\left\lceil\frac{c(S)}{m(S)}\right\rceil
\]

is therefore eventually

\[
\boxed{q(S_{r,n})=2.}
\]

Generic consequence from numerical-semigroup theory: a depth-two semigroup has Kunz coordinates over the binary alphabet `{1,2}`. This generic fact is prior art; P018 contributes the powered-floor proof that its safe languages eventually land in that class.

## 6. Exact genus / Frobenius / dual-genus identities

At stabilization, the number of core boundary states is

\[
|K(B_{r,n})|=N_r(n)-J_r.
\]

Reflection identifies these with the elements of `S_{r,n}` below `M_n`, including `0`. Hence

\[
\boxed{
g(S_{r,n})=M_n-N_r(n)+J_r.}
\]

The Frobenius number is

\[
\boxed{
F(S_{r,n})=M_n-P_{r,n}-1.
}
\]

For the classical maximal associated numerical set `S_{r,n}^*`, the dual genus is therefore

\[
\boxed{
g(S_{r,n}^*)
=F(S_{r,n})-g(S_{r,n})+1
=N_r(n)-P_{r,n}-J_r.}
\]

The void size becomes

\[
\boxed{
|S_{r,n}^*\setminus S_{r,n}|
=M_n+P_{r,n}-2N_r(n)+2J_r.
}
\]

These are exact identities after stabilization.

Since `N_r,P_{r,n}=o(M_n)`, they imply

\[
\frac{g(S_{r,n})}{F(S_{r,n})}\to1.
\]

Thus the safe languages are asymptotically near the maximal-genus edge of the numerical-semigroup range rather than near the symmetric edge.

## 7. Same language, asymptotically opposite precision densities

Let

\[
B^-_{r,n}:=K(B_{r,n}),
\]

and let `B^+_{r,n}` be the boundary obtained by reflecting the maximal associated numerical set `S_{r,n}^*` at the same gauge `M_n`.

All three boundaries

\[
B^-_{r,n}\subseteq B_{r,n}\subseteq B^+_{r,n}
\]

have the same safe-translation language `S_{r,n}`.

Their cardinalities are

\[
\boxed{|B^-_{r,n}|=N_r(n)-J_r,}
\]

\[
\boxed{|B_{r,n}|=N_r(n),}
\]

and

\[
\boxed{|B^+_{r,n}|
=M_n+P_{r,n}-N_r(n)+J_r.}
\]

Therefore

\[
\boxed{
\frac{|B^-_{r,n}|}{M_n}\to0,
\qquad
\frac{|B_{r,n}|}{M_n}\to0,
\qquad
\frac{|B^+_{r,n}|}{M_n}\to1.
}
\]

This is a sharp separation between precision realization and future language:

> the **same** safe-translation semigroup admits an asymptotically sparse minimal realization and an asymptotically full maximal realization.

The natural quotient-root atlas sits only `J_r=O_r(1)` states above the sparse operational core, despite belonging to a same-language precision fiber whose total neutral span is asymptotic to `M_n~n^{1/r}`.

## 8. P023 refinement-width consequences

Use the plateau-partition interpretation of boundary insertion from the existing P023 refinement-width bridge.

### Natural atlas over its operational core

At stabilization, all removed states

\[
b_2(n),\ldots,b_{D_r}(n)
\]

lie consecutively in the single top core interval between `b_{D_r+1}(n)` and `M_n`. Restoring the natural atlas therefore splits exactly one core cell into `J_r+1` fine cells and does not refine any other core cell further.

Hence the local refinement width is exactly

\[
\boxed{
w_{\rm nat}(r,n)=J_r+1
\qquad(n\gg_r1).
}
\]

So the natural atlas is not only cardinality-near-minimal; it is locally near-minimal with a root-order-dependent constant refinement alphabet.

### Maximal same-language refinement

Let

\[
w_{\max}(r,n)
:=w_{\Pi_{B^-_{r,n}}}(\Pi_{B^+_{r,n}}).
\]

In numerical-set coordinates, the first interval between consecutive elements of `S_{r,n}` is `(0,mu_{r,n})`. Since `S_{r,n}` has no positive element there, every point of `S_{r,n}^*` in that interval is neutral refinement detail.

The total number of gaps of `S_{r,n}^*` is

\[
g(S_{r,n}^*)=N_r(n)-P_{r,n}-J_r.
\]

Therefore the first interval alone gives

\[
\boxed{
\mu_{r,n}-\bigl(N_r(n)-P_{r,n}-J_r\bigr)
\le w_{\max}(r,n).
}
\]

Conversely, consecutive semigroup elements are never separated by more than the multiplicity, because `s+mu` is again in the semigroup. Hence every refinement block contains at most `mu_{r,n}` fine cells:

\[
\boxed{w_{\max}(r,n)\le\mu_{r,n}.}
\]

Since `N_r,P_{r,n}=o(mu_{r,n})`, the two bounds squeeze to

\[
\boxed{
\frac{w_{\max}(r,n)}{\mu_{r,n}}\to1,
}
\]

and therefore

\[
\boxed{
w_{\max}(r,n)
\sim
\theta_r n^{1/r}.}
\]

Thus one fixed future language supports two radically different refinement costs:

\[
\boxed{
\text{natural same-language detail width}=J_r+1=O_r(1),
}
\]

while

\[
\boxed{
\text{maximal same-language detail width}\sim\theta_r n^{1/r}.
}
\]

This is a direct P018-to-P023 bridge: amount of neutral precision and local alphabet cost are distinct coordinates even inside one fixed operation language.

## 9. Two independent large parameters

The stabilization constant

\[
J_r=\lfloor(1-2^{-1/r})^{-r}\rfloor-1
\]

is fixed in `n` but grows rapidly with `r`:

\[
J_r\sim\sqrt2\left(\frac r{\log2}\right)^r.
\]

The multiplicity coefficient

\[
\theta_r=1-(D_r+1)^{-1/r}
\]

satisfies `theta_r>2^{-1/r}` and tends to `1` as `r->infinity`.

Hence:

- increasing raw state scale `n` at fixed `r` leaves the removable top-shell width frozen;
- increasing collapse order `r` changes the eventual finite shell itself dramatically and pushes the safe semigroup multiplicity toward the full root scale.

These are genuinely different precision axes.

## 10. Prior-art boundary

The following are generic prior art and must not be claimed as P018 discoveries:

- atom monoids / associated numerical semigroups of numerical sets;
- the anti-atom problem;
- `S subseteq T subseteq S^*` and `S^*=S union void`;
- `|void|=2g-F-1`;
- standard depth and Kunz-coordinate language for numerical semigroups, including the binary depth-two class.

Primary references currently used:

- Chen–Kaplan–Lawson–O'Neill–Singhal, *Enumerating numerical sets associated to a numerical semigroup*, arXiv:2211.17090;
- Delgado–Usó i Cubertorer, *Kunz languages for numerical semigroups are context sensitive*, arXiv:2306.03308;
- Heyman–Miraj, *On Some Floor Function Sets*, arXiv:2309.16072, for the powered-floor exact-cardinality side already recorded in the earlier P018 prior-art correction.

Targeted searches so far have not located the powered-floor specialization consisting of the exact eventual core set, its multiplicity/depth-two limit, or the sparse-to-dense same-language precision-fiber asymptotics. This is **not** a novelty proof; retain `NOVELTY_UNRESOLVED`.

## 11. Next theorem units

1. Promote `b_d(n)=floor(n^{1/r} d^{-1/r})` and the finite top-shell classification as the smallest ordinary theorem unit.
2. Reprove candidate neutrality through the already-written floor-power drop duality, using `lambda_{r,d}` nonintegrality; this is cleaner than the earlier bounded-denominator subsequence proof.
3. Formalize the exact core-set theorem before attempting the effective threshold constants.
4. Route generic depth/Kunz and anti-atom facts through shared/P023 interfaces; do not duplicate their engines in P018.
5. After core stabilization is kernel-checked, formalize the exact multiplicity and the constant natural refinement width `J_r+1` as the first P018/P023 executable bridge.
