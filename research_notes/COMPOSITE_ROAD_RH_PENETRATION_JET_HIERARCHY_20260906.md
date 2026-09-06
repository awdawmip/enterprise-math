# Composite-road RH penetration barrier and all-order jet hierarchy

Status: `RESEARCH FRONTIER / PROVED DERIVATIONS + EXACT METHOD BOUNDARY / NOT FOUNDATION / NOT RH PROOF`
Date: `2026-09-06`
Researcher: `EM-FREE-C4A91D / FREE_AXIOM_DISCOVERY / ANCHOR_EXPOSED`
Progress-Event-ID: `EM-FREE-C4A91D-ROAD-PENETRATION-JET-HIERARCHY-20260906`
Global journal source: `journal/enterprise-math/2026-09-06/20260906T162500+0800-em-free-c4a91d-road-penetration-jet-hierarchy.md`
Parents:
- `research_notes/COMPOSITE_ROAD_RH_COMPLETED_SCHUR_PICK_20260906.md`
- `research_notes/COMPOSITE_ROAD_RH_BOUNDARY_SLOPE_CLOSURE_20260906.md`
Highest constraint: `definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json`

## 1. Centered positive-road formula with explicit finite tail

For `a>0`, let

\[
\mathcal R_a(n)=\sum_{d\mid n}\frac{\mu(d)}{d^a}
=\prod_{p\mid n}(1-p^{-a})>0,
\]

\[
S_a(x)=\sum_{n\le x}\mathcal R_a(n),
\qquad c_a=\frac1{\zeta(1+a)},
\qquad E_a(x)=S_a(x)-c_ax.
\]

Divisor summation gives

\[
S_a(x)=\sum_{d\le x}\frac{\mu(d)}{d^a}\Big\lfloor\frac xd\Big\rfloor
\]

and hence the exact centered identity

\[
\boxed{
E_a(x)=
-x\sum_{d>x}\frac{\mu(d)}{d^{1+a}}
-\sum_{d\le x}\frac{\mu(d)}{d^a}\left\{\frac xd\right\}.
}
\]

For `0<a<1`, set

\[
B_a=2+\frac1a+\frac1{1-a}.
\]

Absolute values alone give

\[
\boxed{|E_a(x)|\le B_ax^{1-a}\qquad(x\ge1).}
\]

For

\[
Z_a(s)=\frac{\zeta(s)}{\zeta(s+a)},
\]

Abel summation initially for `\Re s>1` yields

\[
Z_a(s)=c_a\frac{s}{s-1}
+s\int_1^\infty E_a(x)x^{-s-1}\,dx.
\]

The explicit road bound makes the centered integral absolutely convergent in

\[
\boxed{\Re s>1-a.}
\]

Since `\zeta(s+a)` is zero-free there, analytic continuation gives the same identity throughout this half-plane.

Let

\[
G_a(s)=\pi^{a/2}\frac{\Gamma(s/2)}{\Gamma((s+a)/2)}.
\]

The completed road transfer therefore has the exact representation

\[
\boxed{
\frac{\xi(s)}{\xi(s+a)}
=G_a(s)\frac{s^2}{(s+a)(s+a-1)}
\left[
 c_a+(s-1)\int_1^\infty E_a(x)x^{-s-1}\,dx
\right].
}
\]

For `\sigma=\Re s>1-a`, truncating the road integral at `X` has the explicit unconditional remainder

\[
\boxed{
\left|\int_X^\infty E_a(x)x^{-s-1}\,dx\right|
\le
\frac{B_a X^{1-a-\sigma}}{a+\sigma-1}.
}
\]

Thus the completed Schur transfer admits a genuinely finite, all-integer, road-inclusive certified approximation in its absolute-control domain.

## 2. Absolute-penetration blind-zone theorem

For `0<a<1/2`, the preceding finite absolute control reaches only

\[
\Re s>1-a,
\]

or, in the centered coordinate `z=s-1/2`,

\[
\Re z>1/2-a.
\]

Suppose RH is false and `\rho=\beta+i\gamma` is a nontrivial zero with `\beta>1/2`. Whenever `a<\beta-1/2`, the denominator `\zeta(s+a)` creates an RH-sensitive potential pole at

\[
s_\rho=\rho-a,
\qquad \Re s_\rho=\beta-a>1/2.
\]

But every nontrivial zero has `\beta<1`, so

\[
\beta-a<1-a.
\]

Therefore the shifted zero pole lies strictly outside the entire half-plane controlled by the elementary positive-road absolute tail. The gap is exactly

\[
(1-a)-(\beta-a)=1-\beta,
\]

independent of `a`.

Hence:

\[
\boxed{
\text{POSITIVE ROAD + ABSOLUTE TAIL CONTROL ALONE}
\text{ CANNOT REACH AN RH-FALSIFYING SHIFTED ZERO.}
}
\]

This is a method boundary, not a reason to delete composites. The missing capability is cancellation/analytic continuation inside the centered composite road.

## 3. All-order contact hierarchy

Let `\omega(n)` be the number of distinct prime divisors of `n>1`. Since

\[
\mathcal R_a(n)=\prod_{p\mid n}(1-e^{-a\log p}),
\]

one has

\[
\left.\frac{d^k}{da^k}\mathcal R_a(n)\right|_{a=0}=0
\qquad(k<\omega(n)),
\]

and

\[
\boxed{
\left.\frac{d^{\omega(n)}}{da^{\omega(n)}}\mathcal R_a(n)\right|_{a=0}
=\omega(n)!\prod_{p\mid n}\log p>0.
}
\]

So `\omega(n)` is exactly the zero-road contact order.

The first jet is

\[
\mathcal R'_0(n)=\Lambda(n),
\]

so prime powers are only the order-one hole layer. The second jet first activates integers with two distinct prime factors; order `k` first activates the `\omega=k` joint-composite layer. Every finite `K`-jet is blind to all integers with `\omega(n)>K`.

For the transform

\[
Z_a(s)=\frac{\zeta(s)}{\zeta(s+a)},
\]

\[
Z'_0(s)=-\frac{\zeta'}\zeta(s)=\sum_n\frac{\Lambda(n)}{n^s},
\]

and

\[
Z''_0(s)=\left(\frac{\zeta'}\zeta\right)^2
-\left(\frac{\zeta'}\zeta\right)'.
\]

Coefficientwise,

\[
\boxed{
\mathcal R''_0(n)
=(\Lambda*\Lambda)(n)-\Lambda(n)\log n.
}
\]

For `n=pq` with distinct primes this is `2\log p\log q`, the first explicit two-factor joint-road interaction.

More generally the `k`th transform jet is the complete exponential Bell polynomial in

\[
-\frac{d^j}{ds^j}\log\zeta(s),\qquad1\le j\le k.
\]

Finite positive road thickness retains all these layers simultaneously. Differentiating to any finite order is therefore a typed information-reducing observer, not a proof that the omitted higher-composite layers are redundant.

## 4. Dyadic completed-road scan

Let

\[
a_j=2^{-j},
\qquad C_j(z)=\frac{X(z)}{X(z+a_j)}.
\]

The completed Schur theorem gives

\[
\boxed{
RH\iff C_j\text{ is Schur on }\Re z>0
\text{ for infinitely many }j\to\infty.
}
\]

Under RH every level passes.

If RH is false, choose an off-critical zero `z_0` of `X` with `\Re z_0>0`. For sufficiently fine levels the denominator vanishes at `z_0-a_j`. Removability would require `X(z_0-a_j)=0`. This can happen for only finitely many `j`, since infinitely many such zeros would accumulate at `z_0`. Thus all sufficiently fine dyadic levels, except at most finitely many cancellation accidents, have a genuine pole and fail the Schur test.

Each genuine pole produces arbitrarily nearby scalar `1x1` Pick violations `|C_j(z)|>1`.

## 5. Research consequence

The current bottleneck is no longer vague. An RH proof by this route requires a **centered composite-road cancellation estimate** that pushes finite certified control from the elementary frontier `\Re s>1-a` toward `\Re s>1/2` for a sequence `a\downarrow0`, without assuming an RH-equivalent zero bound.

Positive total mass alone cannot provide that continuation. The composite road must be retained, but its internal signed/phase/relational cancellation has to be controlled rather than recoalesced away.

## Reuse resolution

- positive Weighted-BRC: `REUSE_APPLIED` to `a>0` road weights;
- signed/phase BRC boundary: `REUSE_APPLIED` as the exact reason absolute positive mass is insufficient;
- `T6_OPERATION_SAFE_QUOTIENT`: `REUSE_APPLIED`; finite road jets are not full-road safe without a future-observer certificate;
- completed Schur/Pick plus spectral-tail Feshbach: `COMPOSE_APPLIED`; finite values are certifiable in the absolute-control domain, but the RH-sensitive region lies beyond it.
