# P017 Mirror Precision Certificate

Status: `ACTIVE RESEARCH NOTE`  
Scope: directional refinement and finite-precision localization of the canonical mirror certificate  
Depends on: P017 mirror MC01–MC06 and P018 finite-precision certificate persistence  
Novelty: `NOVELTY_UNVERIFIED`

This note preserves only the validated program result. It does **not** prove Legendre's conjecture.

## 1. MC07 — Directional first-moment refinement

For each anchor-surviving radius `r`, let

\[
a_r=|\mathcal P_-(r)|,\qquad b_r=|\mathcal P_+(r)|,
\]

where the two quantities count transverse small-prime supports on the lower and upper mirror states.

The canonical MC06 aggregate collapses the first moment to

\[
J=\sum_r(a_r+b_r).
\]

MC07 retains the two directions:

\[
J_-:=\sum_r a_r,\qquad J_+:=\sum_r b_r.
\]

Let `S=|S_k|` and define

\[
U_-:=J_--S,\qquad U_+:=J_+-S.
\]

The existing cross-side slack is

\[
V=E-J_--J_++S
 =\sum_r(a_r-1)(b_r-1).
\]

If the square basin were prime-free, every surviving mirror side would be composite. Hence

\[
a_r\ge1,\qquad b_r\ge1.
\]

Putting `x_r=a_r-1` and `y_r=b_r-1` gives nonnegative integers and therefore

\[
\boxed{U_-\ge0,\quad U_+\ge0,\quad V\ge0}
\]

and

\[
\boxed{
V=\sum_r x_ry_r
\le
\left(\sum_r x_r\right)
\left(\sum_r y_r\right)
=U_-U_+.
}
\]

Thus any violation of

\[
\boxed{U_-\ge0,\ U_+\ge0,\ 0\le V\le U_-U_+}
\]

is a sufficient prime certificate.

### MC07 strictly refines MC06

The old slack is `U=U_-+U_+`.

- `U<0` forces one directional slack negative.
- `V<0` is unchanged.
- If `4V>U^2` while `U_-,U_+>=0`, then

\[
U_-U_+\le\frac{(U_-+U_+)^2}{4}=\frac{U^2}{4}<V.
\]

So every MC06 certificate is an MC07 certificate.

A bounded pressure test for `3<=k<=1000` produced 733 MC06 certificates and 740 MC07 certificates. The seven additional roots were

`137, 171, 233, 293, 336, 470, 570`.

At `k=233`, for example,

\[
U_-=0,\qquad U_+=4,\qquad V=1,
\]

so the total MC06 inequality is silent while `V>U_-U_+` certifies immediately.

These counts are computational pressure-test evidence, not an all-`k` theorem.

## 2. MC08 — Radius as a finite precision axis

MC07 is a one-block observation of all surviving radii. MC08 makes the radius coordinate itself a finite precision axis.

At level `m>=0`, split the integer coordinate `1<=r<k` into `2^m` nested blocks by

\[
\boxed{
\beta_m(r)
=
\left\lfloor\frac{(r-1)2^m}{k-1}\right\rfloor.
}
\]

The partitions are compatible:

\[
\boxed{
\beta_m(r)=\left\lfloor\frac{\beta_{m+1}(r)}2\right\rfloor.
}
\]

For each nonempty surviving-radius block `B`, define local observables

\[
J_-^{(B)}=\sum_{r\in B}a_r,\qquad
J_+^{(B)}=\sum_{r\in B}b_r,
\]

\[
E^{(B)}=\sum_{r\in B}a_rb_r,\qquad S_B=|B|,
\]

and

\[
U_-^{(B)}=J_-^{(B)}-S_B,\qquad
U_+^{(B)}=J_+^{(B)}-S_B,
\]

\[
V^{(B)}=E^{(B)}-J_-^{(B)}-J_+^{(B)}+S_B.
\]

Prime-free behavior forces **every block separately** to satisfy

\[
\boxed{
U_-^{(B)}\ge0,\quad U_+^{(B)}\ge0,
\quad 0\le V^{(B)}\le U_-^{(B)}U_+^{(B)}.
}
\]

A violation in any block is therefore a prime certificate.

## 3. Refinement persistence

Suppose a parent block is partitioned into children `B_i`, and every child is admissible. Write

\[
X_i=U_-^{(B_i)},\quad Y_i=U_+^{(B_i)},\quad Z_i=V^{(B_i)}.
\]

Then `X_i,Y_i,Z_i>=0` and `Z_i<=X_iY_i`. The observables are additive across disjoint children:

\[
X=\sum_iX_i,\qquad Y=\sum_iY_i,\qquad Z=\sum_iZ_i.
\]

Hence

\[
Z\le\sum_iX_iY_i\le
\left(\sum_iX_i\right)\left(\sum_iY_i\right)=XY.
\]

Thus an admissible collection of children implies an admissible parent. Contrapositively,

\[
\boxed{
\text{certificate at precision }m
\Longrightarrow
\text{certificate at every finer precision.}
}
\]

This is a concrete P017 realization of P018 coarse-certificate persistence: increasing precision can resolve an undecided block, but cannot invalidate a certificate already obtained at lower precision.

## 4. Terminal precision is exact sieve resolution

Let

\[
m_{\rm term}(k)=\left\lceil\log_2(k-1)\right\rceil.
\]

At this level every nonempty radius block is a singleton. For `B={r}`,

\[
U_-^{(B)}=a_r-1,\qquad U_+^{(B)}=b_r-1.
\]

A singleton block certifies exactly when at least one mirror side has no transverse small-prime witness. By anchor survival and the square-basin root-factor horizon, that side is prime.

Therefore terminal MC08 is **not** an independent proof mechanism. It is exact small-prime detection expressed in finite-precision coordinates.

Define diagnostically

\[
m_*(k)=\min\{m:\text{MC08 certifies at level }m\}
\]

when such a level is found. Showing merely that `m_*(k)` exists by terminal precision is equivalent to the original prime-existence target. The mathematically useful problem is to derive a **subterminal bound** on `m_*(k)` from independent square-specific structure.

## 5. Bounded precision pressure test

For `3<=k<=1000`, the numbers first certified at levels `0,1,2,3,4,5` were

\[
\boxed{740,\ 98,\ 94,\ 51,\ 14,\ 1.}
\]

Cumulative coverage at `1,2,4,8,16,32` radius blocks was

\[
\boxed{740,\ 838,\ 932,\ 983,\ 997,\ 998.}
\]

The unique first level-5 case was `k=982`.

This does not imply that 32 blocks suffice uniformly. A fixed counterexample is

\[
k=2896,
\]

for which level 5 gives no certificate while level 6 does. Larger pressure tests likewise require growing precision.

The empirical content is therefore only that many basins resolve far before singleton precision; it motivates studying `m_*(k)` quantitatively.

## 6. Routes deliberately rejected

- Adding same-side second moments and a Cauchy bound produced no new certificates beyond MC07 for `k<=1000`; unstructured moment expansion is not promoted.
- A proposed least-factor-gated CRT union was rejected as circular because, after exact cofactor ordering, it reconstructed complete composite-composite detection.
- Terminal MC08 must never be reported as a Legendre proof; it is exact sieve resolution.

## 7. Implementation

Canonical replay assets:

- `src/enterprise_math/p017_mirror_directional.py`;
- `tests/test_p017_mirror_directional.py`.

MC07 retains the exact directional Möbius/CRT observables from the mirror program. MC08 computes the same support counts on nested radius blocks by modular incidence marking and does not call a general integer factorization routine.

The next hard question is to couple the required precision `m_*(k)` to independent canonical P017 structure such as L052 stable root-channel separation, L053 full-core capacity, or L054 exact cofactor-window separation, while proving an actual subterminal bound rather than rephrasing exact sieve resolution.
