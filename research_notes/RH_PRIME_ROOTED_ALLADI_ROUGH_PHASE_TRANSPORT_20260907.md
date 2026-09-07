# RH prime-rooted Alladi transport and rough-depth law

Status: `RESEARCH FRONTIER / EXACT COMMUTING STRUCTURE + UNCONDITIONAL BOUNDARY-LAYER LAW + NO-GO / NOT A PROOF OF RH`
Date: `2026-09-07`
Project: `Enterprise Math / 进取数论`
Researcher: `EM-RHHR-20260907`
Scope: `RH / Alladi polynomial / rooted factor cones / Dickman delay / Möbius / BRC / X6`
Parents:

- `RH_ALLADI_PASCAL_FRAME_ORDERED_PRIME_EDGE_BRC_20260907.md`
- `RH_HARMONIC_ROUGH_TRANSFER_DUHAMEL_REPAIR_20260907.md`
- `RH_CONTINUUM_DICKMAN_GAMMA_COUNTERTERM_20260907.md`

Public prior-art boundary:

- the Alladi higher-order duality used to define the collective polynomial is
  prior work;
- the Dickman delay equation and its smooth-number interpretation are
  classical;
- Hildebrand's 1984 smooth-number/RH threshold and the later
  Gorodetsky/de la Bretèche--Tenenbaum refinements are prior work.

The exact prime-cutoff jump/Alladi commuting square, the root-weighted
rough-depth law below, and their BRC interpretation are the project
contribution of this note. No generic novelty claim is made without a broader
literature audit.

P000 remains unchanged. Prime order, cutoff and factor depth are arithmetic
provenance coordinates, not native X6 spatial axes.

Tool/interface resolution:

```text
COMPOSE_APPLIED
ALLADI_ORDER_STATISTIC_BRC_TRANSFORM
+ ROUGH_DIVISOR_PHASE
+ DICKMAN_DELAY_CARRIER
```

---

## 1. Collective Alladi polynomial in the `t` chart

Let

\[
t=1+z.
\]

For a prime test function `f`, the collective Alladi polynomial is

\[
A_{n,f}(t-1)
=
\sum_{\substack{1<d\mid n}}
\mu(d)t^{\omega(d)-1}f(p_1(d)),
\]

where `p_1(d)` is the least prime factor of `d`.

Equivalently, if the distinct prime factors of `n` are

\[
P_1(n)>P_2(n)>\cdots>P_r(n),
\]

then

\[
\boxed{
A_{n,f}(t-1)
=
-\sum_{k=1}^r
(1-t)^{k-1}f(P_k(n)).
}
\]

Let `f` be supported on primes `q<=Y`, and define the average

\[
F_{X,Y,f}(t)
=
\frac1X\sum_{n\le X}A_{n,f}(t-1).
\]

---

## 2. Exact prime-rooted factor-cone decomposition

Group a squarefree divisor in the Alladi cloud by its least prime:

\[
d=qa,
\qquad
P^-(a)>q.
\]

Since

\[
\mu(qa)=-\mu(a),
\qquad
\omega(qa)-1=\omega(a),
\]

we obtain, for every integer `n`,

\[
A_{n,f}(t-1)
=
-\sum_{\substack{q\mid n\\q\le Y}}
f(q)
\sum_{\substack{a\mid n/q\\P^-(a)>q}}
\mu(a)t^{\omega(a)}.
\]

For `V>=1`, define

\[
h_q(m)
=
\#\{p\mid m:p>q\}
\]

and the exact rough phase

\[
\Phi(V,q;t)
=
\frac1V\sum_{m\le V}(1-t)^{h_q(m)}.
\]

Squarefree divisor expansion gives

\[
\Phi(V,q;t)
=
\sum_{\substack{a\le V\\P^-(a)>q}}
\mu(a)t^{\omega(a)}
\frac{\lfloor V/a\rfloor}{V}.
\]

Put

\[
V_q=\left\lfloor\frac Xq\right\rfloor.
\]

Averaging the grouped Alladi identity yields

\[
\boxed{
F_{X,Y,f}(t)
=
-\sum_{q\le Y}
f(q)\frac{V_q}{X}\Phi(V_q,q;t).
}
\]

This is exact at every finite `X`.

Interpretation:

- `q` is the retained prime-label root;
- `h_q(m)` is the number of larger-factor arms above that root;
- `Phi` is the positive population carrier for real `0<=t<=1`;
- the Möbius divisor cloud is recovered by expanding `Phi` in `t`.

Freeze:

```text
ALLADI_DIVISOR_CLOUD
=
SUM_OVER_PRIME_ROOTS(ROOT_LABEL x LARGER_FACTOR_CONE)
```

---

## 3. Exact prime-cutoff jump identity

For a real cutoff `y`, define

\[
\Phi_X(y;t)
=
\frac1X\sum_{n\le X}(1-t)^{h_y(n)}.
\]

The function is constant between consecutive primes and jumps when the cutoff
crosses a prime.

For a prime `q`, use `q^-` for a cutoff immediately below `q` (equivalently
`q-1` in the integer implementation). Since

\[
h_{q^-}(n)=h_q(n)+\mathbf 1_{\{q\mid n\}},
\]

we have

\[
(1-t)^{h_{q^-}(n)}
=
(1-t)^{h_q(n)}
\left(1-t\mathbf 1_{\{q\mid n\}}\right).
\]

Therefore

\[
\boxed{
\Phi_X(q;t)-\Phi_X(q^-;t)
=
t\frac{V_q}{X}\Phi(V_q,q;t).
}
\]

Combining with Section 2 gives, for `t!=0`,

\[
\boxed{
F_{X,Y,f}(t)
=
-\frac1t
\sum_{q\le Y}
f(q)\,[\Phi_X(q;t)-\Phi_X(q^-;t)].
}
\]

The value at `t=0` is the continuous polynomial limit.

Thus the averaged Alladi polynomial is the prime-label Stieltjes derivative of
one positive cutoff phase.

This is stronger than a scalar identity: every prime root remains a separate
BRC branch until the final `f` observer.

---

## 4. Prime-scale summation by parts

Let

\[
2=q_1<q_2<\cdots<q_m\le Y,
\qquad
\Phi_i=\Phi_X(q_i;t),
\qquad
\Phi_0=\Phi_X(1;t).
\]

Then

\[
\sum_{i=1}^m f(q_i)(\Phi_i-\Phi_{i-1})
=
f(q_m)\Phi_m-f(q_1)\Phi_0
-
\sum_{i=1}^{m-1}
[f(q_{i+1})-f(q_i)]\Phi_i.
\]

The constant phase cancels exactly, so equivalently

\[
\boxed{
\begin{aligned}
\sum_{i=1}^m f(q_i)(\Phi_i-\Phi_{i-1})
={}&
f(q_m)(\Phi_m-1)-f(q_1)(\Phi_0-1)
\\
&-
\sum_{i=1}^{m-1}
[f(q_{i+1})-f(q_i)](\Phi_i-1).
\end{aligned}
}
\]

For constant `f`, the whole Alladi average telescopes to two cutoff phases.
For increasing `f`, the prime source becomes a one-dimensional transport
pairing against the increments of `f`.

---

## 5. Exact discrete/continuum commuting square

Let `R_t(u)` be the generalized Dickman carrier satisfying

\[
uR_t'(u)=-tR_t(u-1),
\qquad
R_t(u)=1\quad(0\le u\le1).
\]

For fixed `X`, define the continuum cutoff phase

\[
\mathcal R_X(y;t)
=
R_t\!\left(\frac{\log X}{\log y}\right).
\]

Put

\[
u_y=\frac{\log X}{\log y}.
\]

Since

\[
\frac{du_y}{dy}
=
-\frac{u_y}{y\log y},
\]

the Dickman delay equation gives

\[
\boxed{
\frac{d}{dy}\mathcal R_X(y;t)
=
\frac{t}{y\log y}
R_t\!\left(
\frac{\log(X/y)}{\log y}
\right).
}
\]

This is exactly the continuum analogue of the prime jump law:

\[
\boxed{
\begin{array}{ccc}
\Phi_X(y;t)
&\xrightarrow{\quad\text{prime cutoff jump}/t\quad}&
(V_q/X)\Phi(V_q,q;t)
\\[2mm]
\downarrow\text{ continuum}
&&
\downarrow\text{ continuum}
\\[2mm]
R_t(\log X/\log y)
&\xrightarrow{\quad d/dy\,/t\quad}&
R_t(\log(X/y)/\log y)/(y\log y).
\end{array}
}
\]

Accordingly, the continuum rooted Alladi transform is

\[
\boxed{
\mathcal F_{X,Y,f}^{\mathrm{cont}}(t)
=
-\int_2^Y
\frac{f(y)}{y\log y}
R_t\!\left(
\frac{\log(X/y)}{\log y}
\right)\,dy.
}
\]

At `t=0`, the kernel is `1` and this is the ordinary continuous prime
intensity.

At `t=1`, the kernel is the Dickman smooth-number profile for the residual
population below a specified largest prime.

The square is a structural correspondence. It is not a claim that the
discrete phase equals the continuum phase at the RH-critical cutoff.

---

## 6. Positive prime-rooted probability carrier

Assume now that

\[
f(q)\ge0
\]

and is not identically zero on primes `q<=Y`.

Define the exact source mass

\[
S_{X,Y,f}
=
\sum_{q\le Y}
f(q)\frac{V_q}{X}
=
-F_{X,Y,f}(0).
\]

Define a probability law on pairs `(Q,M)` by

\[
\boxed{
\Pr(Q=q,M=m)
=
\frac{f(q)}{X S_{X,Y,f}},
\qquad
q\le Y,\quad 1\le m\le V_q.
}
\]

Let

\[
H=h_Q(M).
\]

Then Section 2 becomes the exact probability-generating identity

\[
\boxed{
-\frac{F_{X,Y,f}(t)}{S_{X,Y,f}}
=
\mathbb E(1-t)^H.
}
\]

Thus the full Alladi source is a positive root-label measure followed by a
single rough-depth observer.

No signed cancellation has been asserted: positivity belongs to the carrier,
while the Möbius signs appear only after expansion in `t`.

---

## 7. Uniform conditional rough-depth estimates

Fix

\[
Y=(\log X)^\kappa
\]

with constant `kappa>0`, and put

\[
L_X
=
\log\left(\frac{\log X}{\log Y}\right).
\]

Condition on `Q=q`. Then `M` is uniform on `1,...,V_q`, and

\[
H
=
\sum_{q<p\le V_q}\mathbf 1_{\{p\mid M\}}.
\]

Its conditional mean is

\[
m_q
=
\sum_{q<p\le V_q}
\frac{\lfloor V_q/p\rfloor}{V_q}.
\]

Prime-harmonic Mertens estimates give, uniformly for `2<=q<=Y`,

\[
m_q
=
\log\log V_q-\log\log q+O(1).
\]

Since `Y` is polylogarithmic,

\[
\log\log V_q=\log\log X+o(1)
\]

uniformly, and hence

\[
\boxed{
m_q
=
L_X+O(\log\log Y)
=
L_X+O(\log\log\log X).
}
\]

For the second moment, put

\[
\lambda_q=\sum_{q<p\le V_q}\frac1p.
\]

The joint divisibility bound

\[
\Pr(p r\mid M)
=
\frac{\lfloor V_q/(pr)\rfloor}{V_q}
\le\frac1{pr}
\]

gives

\[
\mathbb E(H^2\mid Q=q)
\le
\lambda_q+\lambda_q^2.
\]

Also `m_q>=lambda_q-1`. Therefore

\[
\boxed{
\operatorname{Var}(H\mid Q=q)
\ll
1+\lambda_q
\ll
\log\log X
}
\]

uniformly in the root prime.

These estimates do not require independence of prime divisibility.

---

## 8. Prime-rooted rough-depth law of large numbers

Averaging the uniform conditional bounds over any nonnegative root weight
`f` gives

\[
\boxed{
\mathbb E
\left|
\frac{H}{L_X}-1
\right|^2
\ll
\frac1{L_X}
+
\left(
\frac{\log\log Y}{L_X}
\right)^2.
}
\]

Since

\[
L_X\sim\log\log X,
\qquad
\log\log Y\asymp\log\log\log X,
\]

we obtain

\[
\boxed{
\frac{H}{L_X}\longrightarrow1
\quad\text{in }L^2,
}
\]

uniformly over all nonzero nonnegative prime-root weights supported on
`q<=Y`.

A useful refinement holds for the RH weight family

\[
f(q)=q^\beta,
\qquad
\beta>0\ \text{fixed}.
\]

The root law is then concentrated at `log Q=log Y+O_P(1)`. Standard prime
partial summation gives

\[
\mathbb E[\log\log Y-\log\log Q]
\ll_\beta \frac1{\log Y}
\]

and the same bound squared for the corresponding variance. Consequently,

\[
\boxed{
\mathbb E H
=
L_X+
O_\beta\left(
\frac1{\log Y}+\frac1{u_X}
\right),
\qquad
\operatorname{Var}(H)\ll_\beta L_X+1,
}
\]

where `u_X=log X/log Y`.

This separates two different depth scales:

- the **typical rooted factor depth** is
  \[
  L_X\asymp\log\log X;
  \]
- the exact worst-case/high-arity repair depth from the parent frontier is
  \[
  K_X\asymp\frac{\log X}{\log\log X}.
  \]

The first controls the boundary-layer thermodynamic profile; the second is
needed for lossless provenance.

---

## 9. Unconditional discrete boundary-layer profile

Fix `T>0`. Uniformly for real `0<=tau<=T`, set

\[
t=\frac{\tau}{L_X}.
\]

For large `X`, define

\[
a_X(\tau)
=
-L_X\log\left(1-\frac{\tau}{L_X}\right)
=
\tau+O_T(1/L_X).
\]

Then

\[
(1-t)^H
=
\exp\left(-a_X(\tau)\frac{H}{L_X}\right).
\]

Instead of using only a Lipschitz estimate, expand the smooth function
`x -> exp(-a_X x)` to second order about `E(H/L_X)`. Its second derivative
is uniformly bounded for `x>=0`. The linear centered term has mean zero, so

\[
\mathbb E\exp(-a_XH/L_X)
=
\exp[-a_X\mathbb E(H/L_X)]
+
O_T(\operatorname{Var}(H/L_X)).
\]

Therefore, for arbitrary nonnegative root weights,

\[
\boxed{
-\frac{F_{X,Y,f}(\tau/L_X)}{S_{X,Y,f}}
=
e^{-\tau}
+
O_T\left(
\frac1{L_X}
+
\frac{\log\log Y}{L_X}
+
\frac{(\log\log Y)^2}{L_X^2}
\right).
}
\]

For the power root weights `f(q)=q^beta`, the refinement in Section 8 gives

\[
\boxed{
-\frac{F_{X,Y,q^\beta}(\tau/L_X)}{S_{X,Y,q^\beta}}
=
e^{-\tau}
+
O_{\beta,T}\left(
\frac1{L_X}
+
\frac1{\log Y}
+
\frac1{u_X}
\right).
}
\]

At the RH choice `beta=1/2`, `Y=(log X)^2`, this is

\[
\boxed{
-\frac{F_{X,Y,\sqrt{\cdot}}(\tau/L_X)}
       {S_{X,Y,\sqrt{\cdot}}}
=
e^{-\tau}
+
O_T\left(\frac1{\log\log X}\right).
}
\]

In particular, the normalized profile converges uniformly to `e^{-tau}` for
`tau` in compact nonnegative intervals.

This proves the leading boundary-layer attenuation directly for the exact
discrete population carrier. It bypasses the harmonic/floor typing issue
because the rooted probability law uses the original floor-weighted phase.

The reciprocal-Gamma factor from the continuum note contributes only at
lower orders when `t=tau/L_X`; recovering it discretely requires higher
cumulant control and is not claimed here.

---

## 10. Boundary-layer no-go

For every fixed finite `tau`,

\[
e^{-\tau}>0.
\]

Therefore the critical thinning window

\[
t\asymp\frac1{\log\log X}
\]

does not produce a power-scale suppression of the Alladi prime source. It
only multiplies the exact source mass by a nonzero constant.

Freeze:

```text
TYPICAL_DEPTH_BOUNDARY_LAYER
-> CONSTANT_ATTENUATION_e^{-tau}
-> NO_POWER_SAVING_BY_AMPLITUDE_SHRINK_ALONE
```

Hence moving a bounded distance into this shrinking `t` window cannot by
itself eliminate the prime-intensity discrepancy. Any RH-strength mechanism
must act on the centered discrete-versus-continuum source, not merely on the
positive rooted population profile.

Strong suppression occurs only when `t` leaves the typical-depth window and
begins to probe the rare event `H=0`. At `t=1`,

\[
\mathbb E(1-t)^H=\Pr(H=0),
\]

which is the largest-prime/smooth-number endpoint. The classical
Hildebrand threshold and later smooth-number explicit formulas show why that
endpoint is already sensitive to zeta-zero information near
`Y=(log X)^2`.

---

## 11. Geometric meaning for primes, semiprimes and multifactor composites

For a squarefree integer with ordered prime factors

\[
p_1>p_2>\cdots>p_r,
\]

the rooted Alladi representation places one rooted Cell at every ordered
rank:

\[
p_1:\ H=0,
\qquad
p_2:\ H=1,
\qquad
\ldots,
\qquad
p_r:\ H=r-1.
\]

Thus:

- a prime has one rooted vertex;
- a semiprime `pq`, `p>q`, has a terminal vertex at `p` and one rooted edge
  at `q`;
- a three-prime squarefree composite has rooted depths `0,1,2`, ending in a
  two-arm simplex;
- an `r`-prime squarefree composite carries the complete rooted-depth chain
  `0,...,r-1`.

Prime powers do not create new ordered-prime vertices because the Alladi
carrier reads `rad(n)`. Their exponent multiplicity remains in the separate
Factor-BRC depth fiber.

This is a relation geometry, not a primality classifier: `H=0` means that a
selected root is the largest prime of that integer, not that the integer has
no smaller factors.

The boundary-layer law says that, under the natural positive
prime-rooted source measure, the typical selected root has about

\[
\log\log X
\]

larger-factor arms. Semiprime edges are therefore low-depth special cases,
while the full exact carrier must still retain the much deeper rare tail.

---

## 12. Relation to the harmonic repair note

The rooted phase has the exact decomposition

\[
\Phi(V,q;t)
=
H_{q,t}(V)
+
\sum_{\substack{a\le V\\P^-(a)>q}}
\mu(a)t^{\omega(a)}
\left(
\frac{\lfloor V/a\rfloor}{V}-\frac1a
\right).
\]

Thus the prime-rooted carrier absorbs both components identified previously:

1. the harmonic Dickman transfer;
2. the floor sawtooth repair.

The law of large numbers controls their **combined leading normalized
effect** in the shrinking boundary layer. It does not separately bound the
signed floor repair at RH scale.

This is why the result can prove the universal `e^{-tau}` profile while
still leaving the centered prime-intensity problem open.

---

## 13. Exact checker

Task-local checker:

`experiments/rh_prime_rooted_alladi_rough_phase_check.py`

It verifies with exact rational arithmetic:

- direct averaged Alladi polynomial
  `= prime-rooted factor-cone sum`;
- exact prime-cutoff jump identity;
- Stieltjes jump representation;
- prime-scale summation by parts;
- `t=0` full prime-source endpoint;
- `t=1` largest-prime/smooth endpoint.

The checker is finite algebraic regression, not evidence for the asymptotic
law or for RH.

---

## 14. New smallest unresolved unit

The total positive boundary-layer profile is now solved to leading order.
The remaining RH-relevant object is the **centered rooted transport defect**

\[
\mathcal D_{X,Y,f}(t)
=
F_{X,Y,f}(t)
-
\mathcal F_{X,Y,f}^{\mathrm{cont}}(t).
\]

At `t=0`, this contains the discrete prime-intensity discrepancy. At `t=1`,
it contains the critical smooth-number discrepancy. The exact prime-cutoff
jump law shows that these are endpoints of one provenance-preserving
transport family.

The next admissible target is not another positive law of large numbers.
It is a signed estimate for the centered cutoff-phase measure

\[
\frac1t\,d\left[
\Phi_X(y;t)
-
R_t\!\left(\frac{\log X}{\log y}\right)
\right]
\]

paired with `f(y)=sqrt(y)`.

A genuine advance must obtain cancellation in this signed measure without:

- replacing it by total variation;
- suppressing the exact floor/population source;
- assuming an RH-strength smooth-number estimate;
- erasing the prime-root labels;
- mistaking the universal `e^{-tau}` attenuation for a bound on the
  discrete prime discrepancy.

No RH proof is claimed.
