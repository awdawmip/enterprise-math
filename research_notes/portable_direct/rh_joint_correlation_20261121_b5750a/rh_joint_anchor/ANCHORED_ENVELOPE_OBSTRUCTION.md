# Anchored phase coherence under a coefficient envelope

## Status and scope

This is an auxiliary analytic theorem derived in this continuation. It concerns
arbitrary bounded divisor-phase coefficients, not the arithmetic coefficients of
the matched Enterprise Math roads. It proves a limitation of estimates that use
only a coefficient envelope. It does not prove a lower bound for an actual road,
for its positive-part energy, or for the unresolved large-divisor source.

The previously proved phase functions are

\[
B_d(n)=\frac{d^2-1}{12d}-\frac{r(d-r)}{2d},\qquad r=n\bmod d,
\]

\[
P_d(n)=\frac nd\bigl(H_n-H_{\lfloor n/d\rfloor}-\log d\bigr)
 -\frac rd+\frac{d-1}{2d}.
\]

They satisfy \(-\Delta^2 B_d=1_{d\mid n}-1/d\) and
\(-\Delta^2P_d(n)=(1_{d\mid n}-1/d)/n\). Their exact definitions, complex
integral representation, and endpoint conventions were proved in Source
`2f355fe56835278452566d769820941702c52bad`,
`research_notes/portable_direct/rh_phase_correlation_20261121_b5750a/rh_correlation_phase/PHASE_HOMOGENIZATION.md`.
All indices here remain ordinary integers; no observation population is removed.

## 1. Uniform first-order approximation

For every integer \(n\ge2,d\ge2\),

\[
\boxed{\left|P_d(n)-\frac{B_d(n)}n\right|\le\frac{d^2}{8n^2}.}
\tag{1}
\]

This estimate is uniform when \(d\) varies with the anchor. It is not an
asymptotic expansion with an unspecified, divisor-dependent remainder.

**Proof.** Put \(u=e^{2\pi i\ell/d}\), for \(1\le\ell<d\). The earlier exact
representations give

\[
P_d(n)=-\frac1d\sum_{\ell=1}^{d-1}u^{n+1}
 \int_0^1\frac{t^n}{(1-tu)^2}\,dt,
\qquad
\frac{B_d(n)}n=-\frac1d\sum_{\ell=1}^{d-1}
 \frac{u^{n+1}}{n(1-u)^2}.
\]

For \(f_u(t)=t/(1-tu)^2\),

\[
f'_u(t)=\frac{1+tu}{(1-tu)^3},\qquad
|1-tu|^2=(1-t)^2+t|1-u|^2\ge t|1-u|^2.
\]

Consequently

\[
|f_u(t)-f_u(1)|\le4(t^{-1/2}-1)|1-u|^{-3},
\]

and integration against \(t^{n-1}\) bounds the corresponding integral
difference by

\[
\frac{2}{n(n-1/2)}|1-u|^{-3}.
\]

If \(k=\min(\ell,d-\ell)\), then
\(|1-u|=2\sin(\pi k/d)\ge4k/d\). Therefore

\[
\sum_{\ell=1}^{d-1}|1-u|^{-3}
\le2\left(\frac d4\right)^3\sum_{k\ge1}k^{-3}
\le\frac{3d^3}{64},
\]

where \(\sum k^{-3}\le1+\int_1^\infty x^{-3}dx=3/2\).
The total error is at most
\(3d^2/[32n(n-1/2)]\le d^2/(8n^2)\), since \(n\ge2\). This proves (1).

## 2. Many divisor phases can align at a prescribed anchor

Let positive integers \(A,H\) satisfy

\[
H\le A/16,\qquad H^2\ge40A.
\tag{2}
\]

These inequalities imply \(H\ge640\). Put \(M=A/H\). For every integer
\(\lceil M\rceil\le k\le\lfloor3M/2\rfloor\), take all integers in

\[
\frac{A}{k+1/8}\le d\le\frac Ak.
\tag{3}
\]

Call their union \(\mathcal D(A,H)\). Its intervals are disjoint, all its
members lie in \((H/2,H]\), and

\[
\{A/d\}\le1/8,\qquad |\mathcal D(A,H)|\ge H/160.
\tag{4}
\]

For completeness, there are at least \(M/4\) allowed values of \(k\).
Each interval (3) has length

\[
\frac{A}{8k(k+1/8)}\ge\frac{H^2}{20A}\ge2.
\]

It therefore contains at least half its length in integers, hence at least
\(H^2/(40A)\). Multiplication gives (4). The lower endpoint is above \(H/2\)
because \(k+1/8\le3M/2+1/8<2M\).

For \(x=\{A/d\}\le1/8\) and \(d\ge4\),

\[
\frac{B_d(A)}d=\frac1{12}-\frac{x(1-x)}2-\frac1{12d^2}
\ge\frac{11}{384}-\frac1{192}=\frac3{128}>\frac1{48}.
\]

The exact discrete first differences of \(B_d\) have absolute value at most
\(1/2\), including the wrap at residue zero. Thus, for
\(0\le t\le\lfloor H/192\rfloor\),

\[
B_d(A+t)\ge\frac d{48}-\frac t2
\ge\frac d{64}.
\]

Applying (1), using \(d/(A+t)\le1/16\), gives

\[
P_d(A+t)\ge\frac d{64(A+t)}-\frac{d^2}{8(A+t)^2}
\ge\frac d{128(A+t)}.
\tag{5}
\]

## 3. An anchored lower bound for bounded coefficients

Set \(c_d=1\) on \(\mathcal D(A,H)\), and \(c_d=0\) on the other indices
\(2\le d\le H\). In particular, \(|c_d|\le1\). For
\(P_H=\sum_{d=2}^Hc_dP_d\), (4) and (5) imply

\[
P_H(n)\ge\frac{H^2}{40960n}
\quad\text{for }A\le n\le A+\lfloor H/192\rfloor.
\tag{6}
\]

For every \(\theta\ge1/2\), it follows that

\[
\boxed{
\sum_{n=A}^{A+\lfloor H/192\rfloor}
 \frac{P_H(n)^2}{n^{2\theta+1}}
\ge
\frac{H^5}{192\cdot40960^2\,(A+H/192)^{2\theta+3}}
\ge C_\theta H^5 A^{-2\theta-3},
}
\tag{7}
\]

where one may take
\(C_\theta=[192\cdot40960^2\cdot2^{2\theta+3}]^{-1}\).
There are at least \(H/192\) terms, and
\(A+H/192\le(3073/3072)A<2A\). All terms in (6) are positive, so the same
lower bound also holds for the positive-part energy of this auxiliary
correction itself.

## 4. Exact meaning of the exponent obstruction

Suppose the only supplied information about the coefficients is
\(|c_d|\le C_H\), with \(C_H\) bounded or growing slower than every positive
power. This includes the class \(|c_d|\le1\) above. The previously derived
anchored upper estimate has, up to logarithms, contributions

\[
H^3A^{-2\theta-2}+H^5A^{-2\theta-3}.
\]

For \(H=\lfloor A^\beta\rfloor\) with \(1/2<\beta<1\), (2) holds eventually. Equation (7)
shows that the second power cannot be improved uniformly over this coefficient
class. If \(\beta>(2\theta+3)/5\), the correction energy can grow as a positive
power of \(A\); an envelope alone cannot imply a uniform subpower bound.

At \(\theta=1/2\), this is precisely the \(4/5\) boundary. For an entirely
explicit infinite family, take \(A_t=2^{24t}\), \(H_t=2^{20t}\), \(t\ge1\),
and the coefficients (3). Here \(\beta=5/6\) and the lower bound is
\(C_{1/2}A_t^{1/6}\).

For every fixed \(\lambda>1\), the short coherent interval is eventually
contained in \([A,A^\lambda]\). Thus its lower bound also applies to the
correction energy on that complete longer window, or on the infinite tail.

The coefficients are allowed to depend on the anchor; this is an obstruction
to a uniform envelope-only assertion. They have not been shown to arise from
the actual Möbius-transformed road coefficients. Improving the exponent for
those roads remains possible, but requires additional arithmetic information
about anchored phases or about the surviving large-divisor source.

## 5. Reproduction and the useful research decision

Run `python rh_joint_anchor/certify_anchor_obstruction.py` from the bundle.
The script checks (1) using directed integer intervals in several structural
regimes, verifies (3)–(6) with exact rational arithmetic, records an actual
small coherent-window energy, and verifies the construction at the first
member of the explicit \(5/6\) family. It does not present those finite checks
as a proof of the universal theorem; Sections 1–4 provide that proof.

Together with the actual-road variance growth theorem in the sibling
`rh_joint_variance` directory, this isolates two distinct obstacles:

1. The actual complete-period variance already contains an uncancellable
   upper-denominator band; mere regrouping of its multiple sums cannot remove
   the leading power.
2. In the larger envelope class, fixed-anchor coherence really can generate
   the second anchored power. A better fixed-window result must exploit more
   than the coefficient envelope.

Neither observation justifies discarding composite indices, resetting the
true endpoints, assuming random phases, or claiming a proof of RH.
