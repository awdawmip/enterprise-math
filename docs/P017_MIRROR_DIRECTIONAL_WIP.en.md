# P017 Mirror Certificate — Directional / Finite-Precision Refinement WIP

Status: `ACTIVE PROGRAM RESEARCH / NOT CANONICAL`  
Owner: P017 program layer  
Depends on: canonical mirror MC01–MC06 and P018 finite-precision certificate persistence  
Novelty: `NOVELTY_UNVERIFIED`

## MC07 candidate — retain the two directions of the first moment

For each surviving radius `r`, let

\[
a_r=|\mathcal P_-(r)|,
\qquad
b_r=|\mathcal P_+(r)|.
\]

Instead of immediately collapsing them into

\[
J=\sum_r(a_r+b_r),
\]

retain

\[
J_-:=\sum_r a_r,
\qquad
J_+:=\sum_r b_r.
\]

Let `S=|S_k|` and define

\[
U_-:=J_--S,
\qquad
U_+:=J_+-S.
\]

The existing cross-side slack is

\[
V=E-J_- -J_+ +S
 =\sum_r(a_r-1)(b_r-1).
\]

Under hypothetical prime-free behavior every surviving mirror side is composite, so with

\[
x_r=a_r-1,
\qquad y_r=b_r-1,
\]

we have `x_r,y_r>=0`, hence

\[
U_-\ge0,
\qquad U_+\ge0,
\qquad V\ge0,
\]

and

\[
\boxed{
V=\sum_r x_ry_r
\le
\left(\sum_r x_r\right)\left(\sum_r y_r\right)
=U_-U_+.
}
\]

Therefore prime-free behavior requires

\[
\boxed{
U_-\ge0,
\quad U_+\ge0,
\quad V\ge0,
\quad V\le U_-U_+.
}
\]

Any violation is a sufficient prime certificate.

## MC07 strictly subsumes MC06

The old slack is `U=U_-+U_+`.

- If `U<0`, at least one directional slack is negative.
- If `V<0`, MC07 detects the same contradiction.
- If `4V>U^2` while both directional slacks are nonnegative, then

\[
U_-U_+\le\frac{(U_-+U_+)^2}{4}=\frac{U^2}{4}<V.
\]

Hence every MC06 certificate is automatically an MC07 certificate.

### Bounded pressure test

For `3<=k<=1000`:

- MC06 certifies `733` roots;
- MC07 certifies `740` roots;
- MC07-only roots are

`137, 171, 233, 293, 336, 470, 570`.

At `k=137`, `|S|=43` and `(J_-,J_+)=(45,41)`, so the upper direction already fails coverage although the total slack is zero.

At `k=233`,

\[
U_-=0,
\qquad U_+=4,
\qquad V=1,
\]

so MC06 is silent while MC07 has `1>0*4`.

These are computational witnesses, not a proof for all `k`.

---

## MC08 candidate — dyadic radius precision hierarchy

MC07 uses one block containing every surviving radius. MC08 makes the radius coordinate itself a finite precision axis.

At precision level `m>=0`, split `1<=r<k` into

\[
2^m
\]

nested integer blocks by

\[
\boxed{
\beta_m(r)
=
\left\lfloor
\frac{(r-1)2^m}{k-1}
\right\rfloor.
}
\]

The partitions are nested because

\[
\boxed{
\beta_m(r)
=
\left\lfloor\frac{\beta_{m+1}(r)}2\right\rfloor.
}
\]

For each nonempty surviving-radius block `B`, define local observables

\[
J_-^{(B)}=\sum_{r\in B}a_r,
\qquad
J_+^{(B)}=\sum_{r\in B}b_r,
\]

\[
E^{(B)}=\sum_{r\in B}a_rb_r,
\qquad
S_B=|B|,
\]

and

\[
U_-^{(B)}=J_-^{(B)}-S_B,
\qquad
U_+^{(B)}=J_+^{(B)}-S_B,
\]

\[
V^{(B)}
=E^{(B)}-J_-^{(B)}-J_+^{(B)}+S_B.
\]

If the original square basin were prime-free, every surviving radius would have both mirror sides composite. Therefore **every block separately** would satisfy

\[
\boxed{
U_-^{(B)}\ge0,
\quad U_+^{(B)}\ge0,
\quad V^{(B)}\ge0,
\quad V^{(B)}\le U_-^{(B)}U_+^{(B)}.
}
\]

Thus a violation in any finite-precision block is a prime certificate.

### Coarse-proof persistence under refinement

Suppose a parent block is split into children `B_i` and no child gives a certificate. Put

\[
X_i=U_-^{(B_i)},
\quad Y_i=U_+^{(B_i)},
\quad Z_i=V^{(B_i)}.
\]

Then every child satisfies

\[
X_i,Y_i,Z_i\ge0,
\qquad
Z_i\le X_iY_i.
\]

The parent observables are additive:

\[
X=\sum_iX_i,
\qquad
Y=\sum_iY_i,
\qquad
Z=\sum_iZ_i.
\]

Hence

\[
Z
\le\sum_iX_iY_i
\le\left(\sum_iX_i\right)\left(\sum_iY_i\right)
=XY.
\]

So the parent also cannot be a certificate. Contrapositively:

\[
\boxed{
\text{certificate at level }m
\Longrightarrow
\text{certificate at every finer level.}
}
\]

This is a concrete P017 instance of P018 coarse-certificate persistence.

### Terminal precision and the anti-circularity boundary

Let

\[
m_{\rm term}(k)
=
\left\lceil\log_2(k-1)\right\rceil.
\]

At this level each nonempty radius block is a singleton. For `B={r}`,

\[
U_-^{(B)}=a_r-1,
\qquad
U_+^{(B)}=b_r-1.
\]

Therefore the block certifies exactly when at least one side has no small-prime witness. By the root-factor horizon and anchor survival, that is exactly when that mirror side is prime.

So terminal MC08 is **not a new proof trick**. It is exact small-prime detection in precision language. In particular,

\[
\boxed{
\text{showing that a certificate always appears by terminal precision}
\iff
\text{the target prime-existence problem itself.}
}
\]

The research question is instead to prove a **nontrivial upper bound** on the first certifying precision.

Define diagnostically

\[
m_*(k)
=
\min\{m:\text{MC08 certifies at level }m\},
\]

when such a level is found. Useful future theorems would have to show, for example, that `m_*(k)` is uniformly below terminal precision by a growing margin, or satisfies a subterminal asymptotic bound derived from independent P017 structure.

### Bounded precision-pressure test

For `3<=k<=1000`, the number of roots **first** certified at levels `0,1,2,3,4,5` is

\[
\boxed{740,\ 98,\ 94,\ 51,\ 14,\ 1.}
\]

Equivalently, cumulative coverage at `1,2,4,8,16,32` blocks is

\[
\boxed{740,\ 838,\ 932,\ 983,\ 997,\ 998.}
\]

The unique level-5 case is `k=982`.

This does **not** mean 32 blocks suffice uniformly. A fixed counterexample is

\[
k=2896,
\]

where level 5 does not certify but level 6 does. Random larger-k pressure tests also show the required finite precision continues to grow.

The empirical point is therefore not a bounded-32 theorem. It is that a large fraction of cases terminate at far lower precision than singleton resolution, which makes `m_*(k)` a meaningful research observable.

---

## Negative tests / routes deliberately stopped

1. Same-side second moments plus a Cauchy bound were tested through `k<=1000` and produced no certificates beyond MC07. Do not reopen unstructured moment expansion.
2. A putative least-factor-gated CRT union that covered all MC06 residuals was rejected as circular: after L053-style cofactor ordering, the gate held for every actual divisor pair and reconstructed exact composite-composite detection.
3. Terminal MC08 must never be reported as an independent Legendre proof; it is exact sieve resolution.

## Implementation

Program branch assets:

- `src/enterprise_math/p017_mirror_directional.py`;
- `tests/test_p017_mirror_directional.py`.

MC07 retains exact directional Möbius/CRT formulas. MC08 computes the same support observables on nested radius blocks by exact modular incidence marking, without calling a general integer factorization routine.

The next program task is to connect the required precision `m_*(k)` to canonical L052/L053 cofactor/root separation or another independent square-specific invariant. If that only reproduces terminal sieve resolution, the route must be demoted.
