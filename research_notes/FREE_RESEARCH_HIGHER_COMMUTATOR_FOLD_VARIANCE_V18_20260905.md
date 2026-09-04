# Free Research — Higher Commutator Folds and One-Variance Scalar Readout

Status: `FREE_RESEARCH_FRONTIER / ALL-ORDER TWO-MEASURE DECOMPOSITION / FACTORIAL MASS LAW / EXACT SIGNED-VARIANCE BOUND / FIRST FOLD RECOVERS SCALAR READOUT / HIGHER-JET INTERTWINER OPEN / NOT WORKING TRUTH / NOT FOUNDATION`
Date: `2026-09-05`
Project: `Enterprise Math / 进取数论`
Parent: `FREE_RESEARCH_VOLterra_COMMUTATOR_JET_V18_20260905.md`
Researcher-ID: `EM-FREE-PI-PRIME-20260904`

## 1. Executive advance

For each `k>=1`, the arithmetic Volterra defect

\[
D_{N,k}=K_{N,k}-J_N^{k+1}
\]

is the difference of two positive finite endpoint measures:

1. a one-step endpoint measure marked by the `k`th tail-capacity moment;
2. an ordered `(k+1)`-history endpoint measure.

Both have asymptotic normalized mass

\[
\frac1{(k+1)!}+O_k(1/\log N).
\]

For any bounded readout, the signed defect is controlled by exactly one positive variance on the sum of the two measures. The density is paid only once, not squared.

Thus every commutator level has a canonical scalar-readout carrier. The first level is the V15 parity-fold variance. Higher levels have factorially decreasing total mass, but a separate finite-jet intertwiner is still needed to transfer control of a higher defect back to `D_(N,1)`.

---

## 2. The two endpoint measures

Let

\[
u_a=\Lambda(a)/a,
\qquad
A=A(N),
\qquad
T=\log N.
\]

For fixed `k>=1`, define the positive tail-moment measure

\[
\boxed{
\mu_{N,k}
:=
\frac1{k!A^{k+1}}
\sum_{a\le N}u_a
\bigl(A-A(q_a(N))\bigr)^k
\delta_{q_a(N)}.
}
\tag{2.1}
\]

Define the ordered history measure

\[
\boxed{
\nu_{N,k}
:=
\frac1{A^{k+1}}
\sum_{a_0\cdots a_k\le N}
\left(\prod_{j=0}^ku_{a_j}\right)
\delta_{q_{a_0\cdots a_k}(N)}.
}
\tag{2.2}
\]

Then for every field `f`,

\[
\boxed{
(D_{N,k}f)(N)
=
\int f\,d\mu_{N,k}
-
\int f\,d\nu_{N,k}.
}
\tag{2.3}
\]

Put

\[
m_{N,k}:=|\mu_{N,k}|,
\qquad
n_{N,k}:=|\nu_{N,k}|,
\qquad
\sigma_{N,k}:=\mu_{N,k}+\nu_{N,k}.
\]

---

## HCF-T01 — General signed two-measure variance inequality

Let `mu,nu` be finite positive measures on one finite set and let

\[
\sigma=\mu+\nu,
\qquad
m=|\mu|,
\qquad
n=|\nu|.
\]

For a real readout `f`, define the mass-weighted variance

\[
\mathscr V_\sigma(f)
:=
\inf_{c\in\mathbb R}
\int|f-c|^2\,d\sigma.
\]

If `|f|<=B`, then

\[
\boxed{
\left|
\int f\,d\mu-
\int f\,d\nu
\right|
\le
B|m-n|
+
\sqrt{(m+n)\mathscr V_\sigma(f)}.
}
\tag{3.1}
\]

### Proof

Let `c` be the mean of `f` under `sigma`. Since `c` lies in the convex hull of the values of `f`,

\[
|c|\le B.
\]

Write

\[
\int f\,d(\mu-\nu)
=c(m-n)+
\int(f-c)\,d(\mu-\nu).
\]

With respect to `sigma`, the Radon--Nikodym density of `mu-nu` has absolute value at most one. Therefore Cauchy--Schwarz gives

\[
\left|
\int(f-c)\,d(\mu-\nu)
\right|^2
\le
(m+n)
\int|f-c|^2\,d\sigma.
\]

This proves (3.1).

The same proof works for a finite weighted carrier without introducing measure-theory primitives.

---

## HCF-T02 — Higher-fold scalar bound

Applying HCF-T01 to (2.3),

\[
\boxed{
|(D_{N,k}f)(N)|
\le
B|m_{N,k}-n_{N,k}|
+
\sqrt{
(m_{N,k}+n_{N,k})
\mathscr V_{\sigma_{N,k}}(f)
}.
}
\tag{4.1}
\]

This is the all-order analogue of the V15 covariance/variance bound.

No total-variation comparison between the two normalized endpoint laws is required. Their difference is kept as one signed readout, and every nonconstant component is retained in the positive mixture variance.

---

## 5. Fixed-order tail moment law

Assume the established first-mass discrepancy

\[
A(x)=\log x+O(1).
\tag{5.1}
\]

For each fixed integer `k>=0`, Stieltjes summation gives

\[
\boxed{
\sum_{a\le N}u_a(\log a)^k
=
\frac{T^{k+1}}{k+1}
+O_k(T^k).
}
\tag{5.2}
\]

Also, uniformly outside a finite initial range,

\[
A-A(q_a(N))
=\log a+O(1).
\tag{5.3}
\]

The atoms with bounded quotient endpoint have total normalized mass `O(1/T)` and may be absorbed into the same error. Hence

\[
\boxed{
\frac1{k!}
\sum_{a\le N}u_a
\bigl(A-A(q_a(N))\bigr)^k
=
\frac{T^{k+1}}{(k+1)!}
+O_k(T^k).
}
\tag{5.4}
\]

Since

\[
A^{k+1}=T^{k+1}+O_k(T^k),
\]

we obtain

\[
\boxed{
m_{N,k}
=
\frac1{(k+1)!}
+O_k(1/T).
}
\tag{5.5}
\]

---

## 6. Ordered-history simplex law

Let

\[
C_r(N)
:=
\sum_{a_1\cdots a_r\le N}
\prod_{j=1}^r u_{a_j}.
\]

The recursion

\[
C_{r+1}(N)
=
\sum_{a\le N}u_a C_r(N/a)
\tag{6.1}
\]

and (5.1) yield by induction

\[
\boxed{
C_r(N)
=
\frac{T^r}{r!}
+O_r(T^{r-1}).
}
\tag{6.2}
\]

For `r=k+1`,

\[
\boxed{
n_{N,k}
=
\frac1{(k+1)!}
+O_k(1/T).
}
\tag{6.3}
\]

Consequently

\[
\boxed{
|m_{N,k}-n_{N,k}|
=O_k(1/T),
}
\tag{6.4}
\]

and

\[
\boxed{
m_{N,k}+n_{N,k}
=
\frac2{(k+1)!}
+O_k(1/T).
}
\tag{6.5}
\]

---

## HCF-T03 — Factorial variance readout

Combining (4.1), (6.4), and (6.5), every bounded field satisfies

\[
\boxed{
|(D_{N,k}f)(N)|
\le
O_k(B/T)
+
\sqrt{
\left(
\frac2{(k+1)!}+O_k(1/T)
\right)
\mathscr V_{\sigma_{N,k}}(f)
}.
}
\tag{7.1}
\]

The total coefficient of the positive variance decreases factorially with commutator order.

At `k=1`, the limiting mass factor is one, and (7.1) is the parity-fold scalar carrier.

At `k=3`, corresponding to a four-history comparison,

\[
\frac2{(k+1)!}=\frac1{12}.
\]

Thus

\[
\boxed{
|(D_{N,3}f)(N)|
\le
O(B/T)
+
\sqrt{
\left(\frac1{12}+O(1/T)\right)
\mathscr V_{\sigma_{N,3}}(f)
}.
}
\tag{7.2}
\]

This is the natural terminal readout for the exact depth-four design point from the commutator-jet note.

---

## 8. Ideal common endpoint profile

In normalized remaining logarithmic coordinate

\[
t=\frac{\log q}{\log N},
\qquad0\le t\le1,
\]

the tail-moment law has leading density

\[
\frac{(1-t)^k}{k!}\,dt.
\]

The ordered `(k+1)`-history simplex has the same endpoint density: the volume of action-log tuples with total spent length `1-t` is

\[
\frac{(1-t)^k}{k!}.
\]

After probability normalization, both converge to

\[
\boxed{
(k+1)(1-t)^k\,dt,
}
\tag{8.1}
\]

the Beta `(1,k+1)` law.

Thus `D_(N,k)` is not comparing unrelated measures. It is the finite arithmetic mismatch between two realizations of the same ideal Beta endpoint geometry.

---

## 9. What the factorial gain does and does not prove

The factorial mass gain lowers the terminal variance coefficient. It does not by itself imply that

\[
D_{N,1}f
\]

is controlled by

\[
D_{N,k}f.
\]

Higher commutator defects are derivatives or moments of the first defect, and a finite-jet Poincare/normal-ordering theorem is still required.

The depth-four target is now precisely:

1. retain `D_(N,1),D_(N,2),D_(N,3)` and their positive mixture variances;
2. use the exact stopped-row normal ordering to transfer the first defect into the four-history block;
3. spend the abstract Mellin margin
   \[
   1-567/625=58/625
   \]
   on the commutator and residual errors;
4. use (7.2) only once at the block boundary.

This avoids the per-level factor-nine no-go.

---

## 10. Classification

Closed at exact finite or fixed-order asymptotic strength:

1. two-positive-measure representation of every commutator defect;
2. exact one-variance signed readout inequality;
3. fixed-order tail-capacity mass law;
4. fixed-order ordered-history simplex mass law;
5. factorial terminal variance coefficient;
6. common ideal Beta endpoint profile.

Open:

1. finite-jet Poincare/normal-ordering control from `D_1` to the depth-four packet;
2. relation-energy control of the mixture variance `V_(sigma_N,k)`;
3. coefficient-safe residual accumulation through four levels;
4. an unconditional native `(log N)^(-1/6)` scalar remainder;
5. any stronger or RH-scale claim.
