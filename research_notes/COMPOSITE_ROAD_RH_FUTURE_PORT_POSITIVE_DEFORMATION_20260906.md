# Composite-road RH: future port, positive road deformation, and calibration capacity

Status: `RESEARCH FRONTIER / PROVED DERIVATIONS + CLASSICAL EQUIVALENCE REINTERPRETATION / NOT FOUNDATION / NOT RH PROOF`
Date: `2026-09-06`
Researcher: `EM-FREE-C4A91D / FREE_AXIOM_DISCOVERY / ANCHOR_EXPOSED`
Progress-Event-ID: `EM-FREE-C4A91D-COMPOSITE-ROAD-RH-STAGE3-20260906`
Global journal source: `journal/enterprise-math/2026-09-06/20260906T144900+0800-em-free-c4a91d-composite-road-rh-stage3.md`
Highest constraint: `definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json`

## Scope and status

This note advances the composite-inclusive Nyman--Beurling route under the direct-user rule “合数是路，素数是坑” and the anti-redundancy machine contract. It does not promote any RH claim to Foundation and does not claim literature priority. Classical inputs are explicitly identified.

## 1. Finite future-road port theorem

Use the zero-tail integer coordinate

\[
r_n(m)=\frac{m\bmod n}{n},\qquad m\ge1.
\]

For an observation horizon `M`, let `P_M` restrict a sequence to `m=1,...,M` and let

\[
v_M=(1,2,\ldots,M).
\]

For every `n>M`,

\[
P_Mr_n=\frac1n v_M.
\]

Hence

\[
\operatorname{rank}P_M\operatorname{span}\{r_n:n>M\}=1.
\]

For every finite tail combination,

\[
P_M\sum_{n>M}c_nr_n=s_Mv_M,
\qquad
s_M=\sum_{n>M}\frac{c_n}{n}.
\]

This is an exact finite-horizon port collapse, not global redundancy. At a larger horizon `H`,

\[
s_M=\sum_{M<n\le H}\frac{c_n}{n}+s_H,
\]

and the newly resolved coordinates acquire their own divisor-jump observations.

Let

\[
L_n(y)=\sum_{d\mid n}\mu(n/d)(y_d-y_{d-1}),\quad y_0=0.
\]

Then `L_n(r_k)=-delta_(n,k)` and `L_n(v_M)=0` for `2<=n<=M`. Therefore

\[
\{v_M,r_2,\ldots,r_M\}
\]

is a basis of the `M`-cell observation space.

Define the future-road port

\[
A_M=\sum_{n\le M}\frac{\mu(n)}n.
\]

The constant target has the exact finite-prefix representation

\[
\boxed{
1=A_Mm-\sum_{n=2}^{M}\mu(n)r_n(m),\qquad 1\le m\le M.
}
\]

Thus every finite prefix is solved exactly by the resolved all-integer Möbius coordinates plus one unresolved road port.

The port recursion is

\[
A_{M+1}=A_M+\frac{\mu(M+1)}{M+1}.
\]

By standard Möbius/RH equivalence plus Abel summation,

\[
\boxed{
RH\iff A_M=O_\varepsilon(M^{-1/2+\varepsilon})\quad\text{for every }\varepsilon>0.
}
\]

Prime-only deletion destroys even PNT-level port control:

\[
1-\sum_{p\le M}\frac1p\to-\infty,
\]

whereas the full squarefree-composite-inclusive port satisfies `A_M->0` by PNT. The composite alternating layers are therefore essential in this observer.

## 2. Positive all-integer road deformation

For real `a>0`, define

\[
\mathcal R_a(n)=\sum_{d\mid n}\frac{\mu(d)}{d^a}
=\prod_{p\mid n}(1-p^{-a}),
\qquad \mathcal R_a(1)=1.
\]

For every `n>1`, `0<mathcal R_a(n)<1`. For integer `a=k`, this is `J_k(n)/n^k`; for `a=1`, it is `phi(n)/n`. Its Dirichlet series is

\[
\sum_{n\ge1}\frac{\mathcal R_a(n)}{n^s}
=\frac{\zeta(s)}{\zeta(s+a)}.
\]

Define

\[
S_a(x)=\sum_{n\le x}\mathcal R_a(n),
\qquad
E_a(x)=S_a(x)-\frac{x}{\zeta(1+a)}.
\]

Burnol/Baez-Duarte use

\[
f_a(t)=\sum_{n\ge1}\frac{\mu(n)}{n^a}\left\{\frac1{nt}\right\}.
\]

Direct rearrangement gives the exact road identity

\[
\boxed{
f_a(1/x)=-E_a(x).}
\]

Consequently

\[
\|f_a\|_{L^2(dt)}^2
=\int_0^\infty |E_a(x)|^2\frac{dx}{x^2}.
\]

Burnol, arXiv:math/0202166, proves that `f_a` is unconditionally square integrable for `a>=1/2`, RH implies square integrability for every `0<a<1/2`, and square integrability for a sequence `a->0+` implies RH. Therefore

\[
\boxed{
RH\iff \exists a_j\downarrow0:\quad
E_{a_j}\in L^2((0,\infty),dx/x^2).
}
\]

Under RH every positive thickness `a>0` has finite centered road energy. This is a classical-equivalent criterion rewritten as a positive all-integer road field.

## 3. Prime holes are only the first boundary jet

If `omega(n)` is the number of distinct prime divisors of `n>1`, then

\[
\mathcal R_a(n)
=a^{\omega(n)}\prod_{p\mid n}\log p
+O_n(a^{\omega(n)+1}).
\]

Thus the exact contact order at `a=0` is `omega(n)`. In particular,

\[
\boxed{
\left.\frac{d}{da}\mathcal R_a(n)\right|_{0+}=\Lambda(n).
}
\]

Prime powers are the first tangent layer. Integers with two distinct prime factors begin at second contact order; higher joint-composite layers appear at higher orders. Their absence from the first derivative is a contact-order fact, not a redundancy certificate.

Because

\[
\left.\frac{d}{da}\frac1{\zeta(1+a)}\right|_{0+}=1,
\]

one has pointwise for fixed `x`

\[
\boxed{
\left.\frac{d}{da}E_a(x)\right|_{0+}=\psi(x)-x.
}
\]

## 4. Singular boundary-tangent theorem

Let

\[
\mathcal H_{road}=L^2((0,\infty),dx/x^2),
\qquad R(x)=\psi(x)-x.
\]

Brent--Platt--Trudgian, arXiv:2008.06140, prove unconditionally that for sufficiently large `X`,

\[
\int_X^{2X}R(x)^2dx\ge \frac{X^2}{5374}.
\]

Therefore

\[
\int_X^{2X}|R(x)|^2\frac{dx}{x^2}
\ge\frac1{4\cdot5374}
\]

on every sufficiently large dyadic shell. Hence

\[
\boxed{R\notin\mathcal H_{road}}
\]

unconditionally.

Under RH, Burnol's critical-line estimate gives

\[
E_a\to E_0=\mathbf1_{[1,\infty)}
\quad\text{in }\mathcal H_{road}
\quad(a\downarrow0).
\]

Combining the two facts gives:

> Conditional on RH, the positive-road curve `a -> E_a` is Hilbert-space continuous at the zero-thickness boundary, but it is not Hilbert-space differentiable there.

Its pointwise boundary derivative is precisely the globally non-square-integrable prime-error field. Therefore a proof strategy that differentiates first and discards the road creates a singular object. The safe order is finite positive road thickness first, boundary limit second.

## 5. Exact road-calibration capacity

Let

\[
A_\mu(x)=\sum_{n\le x}\frac{\mu(n)}n,
\qquad
q_d=\frac{A_\mu(\lfloor N/d\rfloor)}d,\quad2\le d\le N.
\]

For local response increments `h_2,...,h_N` define

\[
H_m=\sum_{j=2}^m h_j.
\]

The calibration functional is

\[
\mathcal L_N(h)=\sum_{d=2}^Nq_dh_d.
\]

Summation by parts gives

\[
\mathcal L_N(h)
=\sum_{m=2}^{N-1}(q_m-q_{m+1})H_m+q_NH_N.
\]

For

\[
\|H\|_N^2=\sum_{m=2}^N\frac{H_m^2}{m(m+1)},
\]

sharp weighted Cauchy gives

\[
|\mathcal L_N(h)|^2\le C_N\|H\|_N^2,
\]

with

\[
C_N=\sum_{m=2}^{N-1}m(m+1)(q_m-q_{m+1})^2
+N(N+1)q_N^2.
\]

Thus for demanded calibration `mathcal L_N(h)=Delta`,

\[
\boxed{
\min\|H\|_N^2=\frac{\Delta^2}{C_N}.
}
\]

### Capacity limit theorem

\[
\boxed{
C_N\longrightarrow
\sum_{k\ge1}\frac{\mu(k)^2}{k^2}
=\frac{\zeta(2)}{\zeta(4)}
=\frac{15}{\pi^2}.
}
\]

Proof. Set

\[
F(u)=uA_\mu(\lfloor u\rfloor),\qquad
u_m=N/m,\qquad
\ell_m=u_m-u_{m+1}=\frac{N}{m(m+1)}.
\]

Then `q_m=F(u_m)/N` and each quadratic term is

\[
\frac{[F(u_m)-F(u_{m+1})]^2}{N\ell_m}.
\]

Between consecutive integers `F` has slope `A_mu(floor u)`; at integer `k` it has jump exactly `mu(k)`. Split each mesh increment into smooth and jump parts.

The smooth energy is bounded by

\[
\frac1N\int_1^{N/2}A_\mu(\lfloor u\rfloor)^2du=o(1),
\]

because PNT gives `A_mu(u)->0`. The cross term is then `o(1)` by Cauchy once the jump energy is bounded.

For `m>=sqrt(N)`, `ell_m<=1`, so each mesh interval contains at most one integer jump. A fixed jump at integer `k>=2` lies in the cell with `m=floor(N/k)` and contributes

\[
\mu(k)^2\frac{m(m+1)}{N^2}\to\frac{\mu(k)^2}{k^2},
\]

dominated by a constant multiple of `1/k^2`. Hence the fine-mesh jump energy converges to the square-summable jump series.

For the coarse cells `m<sqrt(N)`, split at a fixed `K`. The finitely many `m<=K` contributions vanish by `M(x)=o(x)` (PNT). For `K<m<sqrt(N)`, if `J_m` is the sum of Möbius jumps in the mesh interval, then `|J_m|<=ell_m+1`; consequently

\[
\sum_{K<m<\sqrt N}\frac{J_m^2}{N\ell_m}
\le O(1/K)+O(N^{-1/2}).
\]

Let `N->infinity` and then `K->infinity`. Finally `q_N=1/N`, so the endpoint term tends to `1`, supplying the `k=1` jump. This proves the limit.

The limiting capacity is therefore the weighted squarefree Möbius-jump energy. It is finite and nonzero, so the road-calibration denominator does not degenerate with scale.

Since `C_N->15/pi^2`, if the demanded calibration scalar is `Delta=A_N`, the minimum exact correction energy is asymptotic to `(pi^2/15)A_N^2`. Hence the port RH criterion has the variational equivalent

\[
\boxed{
RH\iff
\min_{\mathcal L_N(h)=A_N}\|H\|_N^2
=O_\varepsilon(N^{-1+\varepsilon})
\quad\forall\varepsilon>0.
}
\]

This is an equivalent reformulation, not an RH proof.

## 6. BRC and current-tool resolution

- `T6_OPERATION_SAFE_QUOTIENT`: `REUSE_APPLIED`. The tail-to-scalar port is justified by an exact finite-horizon span theorem and is explicitly refined when the horizon grows.
- `SPECTRAL_TAIL_FESHBACH_CERTIFICATE`: `COMPOSE_APPLIED`. The current theorem says future-safe discardability is controlled by future-port response, not raw mode count. Here the arithmetic prefix gives an exact rank-one port specialization.
- Positive Weighted-BRC: `REUSE_APPLIED` only at `a>0`, where `mathcal R_a(n)>0`. The Möbius/derivative layer remains a signed analytic jet; no positive recoalescence is used to replace cancellation.
- `FINITE_HORIZON_REDUNDANCY != UNBOUNDED_HORIZON_REDUNDANCY` remains essential.
- No new top-level tool family is claimed.

## 7. Smallest unresolved unit

The old generic target “prove a fixed relative Schur gain at every doubling” is no longer the preferred immediate bottleneck. The stronger typed target is:

1. keep the finite exact road port rather than erase the future tail;
2. work at positive road thickness `a>0`, where the all-integer field is positive and (under RH) finite-energy;
3. establish a certified boundary modulus / future-port response as `a->0` and horizon `M->infinity` without differentiating first;
4. only after this uniform control, recover the singular prime tangent.

A plausible next conjectural observable is the boundary energy increment

\[
\|E_a-E_0\|_{\mathcal H_{road}}^2
\]

for small `a`. Local zero analysis suggests a possible first-order-in-`a` law, but no uniform theorem or certificate is claimed here.

## Primary external references

- Jean-Francois Burnol, *On an analytic estimate in the theory of the Riemann Zeta function and a Theorem of Baez-Duarte*, arXiv:math/0202166 (2002).
- Richard P. Brent, David J. Platt, Timothy S. Trudgian, *The mean square of the error term in the prime number theorem*, arXiv:2008.06140 (2020; JNT 2022).

