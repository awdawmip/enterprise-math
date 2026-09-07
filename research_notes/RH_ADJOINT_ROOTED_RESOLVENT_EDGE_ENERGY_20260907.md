# RH adjoint rooted resolvent, edge localization, and critical root-observer tail

Status: `RESEARCH FRONTIER / EXACT ADJOINT PATH LAW + TWO-SIDED NORM BOUNDS + SHARP GLOBAL TAIL / NOT A PROOF OF RH`
Date: `2026-09-07`
Project: `Enterprise Math / 进取数论`
Scope: `RH / prime-rooted Volterra resolvent / Alladi root observer / ordered-prime edge BRC / weighted Hilbert tail`
Parent frontier:

- `RH_ROOTED_FACTORIAL_RESOLVENT_DEPTH_LAW_20260907.md`
- `RH_ROOTED_FACTORIAL_DEPTH_SHARPNESS_20260907.md`
- `RH_ROOTED_VOLTERRA_SOURCE_RESOLVENT_20260907.md`
- `RH_PRIME_ROOTED_ALLADI_ROUGH_PHASE_TRANSPORT_20260907.md`

Tool-reuse resolution: `EXTEND_EXISTING_TOOL`.

The existing prime-rooted Volterra, source-resolvent, and ordered-prime edge carriers are composed. No new top-level BRC family is introduced.

P000 is unchanged. Prime labels, ordered-factor depth, quotient populations, and path products are arithmetic relation/provenance coordinates, not native X6 spatial axes.

BRC discipline:

`PROVENANCE > MULTIPLICITY > BOOLEAN SUPPORT`.

---

## 0. Question

The parent factorial theorem controls the state-space tail of

\[
E=-t(I+t\mathcal K)^{-1}Q,
\]

where

\[
(\mathcal K F)(N,y)
=
\sum_{y<q\le N}
\frac{\lfloor N/q\rfloor}{N}
F(\lfloor N/q\rfloor,q).
\]

The global Alladi/RH observer is not an unweighted state norm. For the critical source weight

\[
f(p)=\sqrt p\,\mathbf 1_{p\le Y},
\]

it reads the child states through

\[
\mathcal L_{X,Y,f}(F)
=
\sum_{p\le Y}
 f(p)\frac{\lfloor X/p\rfloor}{X}
 F(\lfloor X/p\rfloor,p).
\]

The issue is whether the factor `sqrt(p)` destroys the square-root tail obtained in state space. The result below shows that it does not. A path-mass Hilbert factorization preserves the same power exponent, and the threshold remains sharp for positive data.

---

## 1. Exact adjoint/unfolded path law

For `r>=0`, let

\[
\Gamma_r(X,Y)
=
\left\{(p_0,\ldots,p_r):
 p_0\le Y,
 p_0<p_1<\cdots<p_r,
 p_0\cdots p_r\le X
\right\}.
\]

For a path `gamma=(p_0,...,p_r)`, put

\[
P_\gamma=p_0\cdots p_r,
\qquad
N_\gamma=\left\lfloor\frac X{P_\gamma}\right\rfloor,
\qquad
m_\gamma=\frac{N_\gamma}{X}.
\]

Repeated use of

\[
\left\lfloor
\frac{\lfloor A/b\rfloor}{c}
\right\rfloor
=
\left\lfloor\frac A{bc}\right\rfloor
\]

gives the exact identity

\[
\boxed{
\mathcal L_{X,Y,f}(\mathcal K^r Q)
=
\sum_{\gamma\in\Gamma_r(X,Y)}
 f(p_0)m_\gamma
 Q(N_\gamma,p_r).
}
\]

This is the adjoint rooted-face expansion of the final observer. The path is canonical because prime labels increase strictly; no permutation multiplicity is present.

In operator language, the coefficient of the terminal source state reached by one unfolded path is

\[
\boxed{c_\gamma=f(p_0)m_\gamma.}
\]

If different paths recoalesce at the same terminal pair `(N_gamma,p_r)`, they remain distinct BRC provenance branches until the terminal observer is applied.

---

## 2. Exact root-to-edge localization

For every increasing path,

\[
f(p_0)
=
f(p_r)-
\sum_{j=0}^{r-1}
\bigl(f(p_{j+1})-f(p_j)\bigr).
\]

Therefore

\[
\boxed{
\mathcal L\mathcal K^rQ
=
\mathcal T_r(Q)-
\sum_{j=0}^{r-1}\mathcal E_{r,j}(Q),
}
\]

where

\[
\mathcal T_r(Q)
=
\sum_{\gamma\in\Gamma_r}
 f(p_r)m_\gamma Q(N_\gamma,p_r)
\]

and

\[
\mathcal E_{r,j}(Q)
=
\sum_{\gamma\in\Gamma_r}
 \bigl(f(p_{j+1})-f(p_j)\bigr)
 m_\gamma Q(N_\gamma,p_r).
\]

For `f(p)=sqrt(p)`, the edge weight is

\[
\sqrt{p_{j+1}}-\sqrt{p_j}
=
\frac{p_{j+1}-p_j}
{\sqrt{p_{j+1}}+\sqrt{p_j}}.
\]

This is an exact bridge to `ORDERED_PRIME_EDGE_BRC`: the coherent root value is represented by one terminal mode plus adjacent prime-label increments.

Important boundary: the terminal term does not disappear. Dropping it and retaining only edge increments is information loss. For a positive source, both terminal and edge carriers have positive coefficients; the identity by itself is not signed cancellation.

---

## 3. Sup-norm resolvent is bi-Lipschitz up to one logarithm

Let

\[
\Lambda_X=\sum_{q\le X}\frac1q.
\]

The factorial path law gives

\[
\|\mathcal K^r\|_{\infty\to\infty}
\le\frac{\Lambda_X^r}{r!},
\]

hence

\[
\|(I+t\mathcal K)^{-1}\|_{\infty\to\infty}
\le e^{|t|\Lambda_X}.
\]

Since

\[
E=-t(I+t\mathcal K)^{-1}Q
\]

and

\[
Q=-t^{-1}(I+t\mathcal K)E,
\]

we obtain, for `t!=0`,

\[
\boxed{
\frac{|t|}{1+|t|\Lambda_X}\|Q\|_\infty
\le
\|E\|_\infty
\le
|t|e^{|t|\Lambda_X}\|Q\|_\infty.
}
\]

On the boundary layer

\[
t=\frac{\tau}{\log\log X},
\qquad \tau\ne0\text{ fixed},
\]

we have

\[
\boxed{
\|E\|_\infty
\asymp_\tau
\frac{\|Q\|_\infty}{\log\log X}.
}
\]

Thus the Volterra propagation does not create a hidden power saving in the state sup norm. Any RH-scale gain must come from depth truncation and/or the signed final observer, not from generic sup-norm contraction.

Freeze:

`ROOTED_RESOLVENT_SUP_NORM_GAIN = ONE_BOUNDARY_LAYER_FACTOR, NOT_A_POWER`.

---

## 4. Path-mass Hilbert factorization for the square-root root weight

Now take

\[
f(p)=\sqrt p.
\]

Using the positive surviving-population mass `m_gamma`, Cauchy gives exactly

\[
\left|
\sum_{\gamma\in\Gamma_r}
\sqrt{p_0}m_\gamma Q(N_\gamma,p_r)
\right|^2
\le A_r B_r,
\]

where

\[
A_r
=
\sum_{\gamma\in\Gamma_r}p_0m_\gamma,
\qquad
B_r
=
\sum_{\gamma\in\Gamma_r}m_\gamma
|Q(N_\gamma,p_r)|^2.
\]

This is not an arbitrary choice of norm. The same exact path mass is split symmetrically between the adjoint observer and the source.

Because

\[
m_\gamma\le\frac1{P_\gamma},
\]

we have

\[
p_0m_\gamma
\le
\frac1{p_1\cdots p_r}.
\]

For a fixed continuation tuple `(p_1,...,p_r)`, there are at most `pi(Y)` admissible roots `p_0`. Therefore

\[
\boxed{
A_r
\le
\pi(Y)\frac{\Lambda_X^r}{r!}.
}
\]

Also, if `||Q||_infty<=Q_*`, then

\[
B_r
\le
Q_*^2
\sum_{\gamma\in\Gamma_r}m_\gamma
\le
Q_*^2
\frac{\Lambda_X^{r+1}}{(r+1)!}.
\]

Combining the two estimates gives the global rooted-observer bound

\[
\boxed{
|\mathcal L_{X,Y,\sqrt\cdot}(\mathcal K^rQ)|
\le
Q_*
\sqrt{\pi(Y)\Lambda_X}
\frac{\Lambda_X^r}
{\sqrt{r!(r+1)!}}.
}
\]

The critical cancellation in the energy bookkeeping is explicit:

\[
(\sqrt{p_0})^2\times\frac1{p_0}=1.
\]

The square-root prime weight is exactly balanced by the root incidence mass. A heavier root weight would leave a growing prime power in `A_r`; a lighter one would be subcritical.

Freeze:

`ROOT_WEIGHT_EXPONENT_1/2 x ROOT_INCIDENCE_1/p = HILBERT_CRITICAL_BALANCE`.

---

## 5. Unfolded coefficient energy and the Euler-sinh bound

The ordinary squared coefficient energy of the unfolded adjoint path vector is

\[
\mathcal C_r^2
=
\sum_{\gamma\in\Gamma_r}
 p_0m_\gamma^2.
\]

Since

\[
p_0m_\gamma^2
\le
\frac1{p_0p_1^2\cdots p_r^2},
\]

we obtain

\[
\mathcal C_r^2
\le
\sum_{p_0\le Y}\frac1{p_0}
 e_r\left(\left\{q^{-2}:q>p_0\right\}\right).
\]

Euler's product

\[
\prod_{n=1}^{\infty}\left(1+\frac z{n^2}\right)
=
\frac{\sinh(\pi\sqrt z)}{\pi\sqrt z}
=
\sum_{r\ge0}
\frac{\pi^{2r}}{(2r+1)!}z^r
\]

implies, by positivity and subset inclusion,

\[
\boxed{
\mathcal C_r^2
\le
\left(\sum_{p\le Y}\frac1p\right)
\frac{\pi^{2r}}{(2r+1)!}.
}
\]

Thus

\[
\boxed{
\mathcal C_r
\le
\left(\log\log Y+O(1)\right)^{1/2}
\frac{\pi^r}{\sqrt{(2r+1)!}}.
}
\]

This is stronger than the repeated-branch power-sum bound because distinct prime-label provenance is retained. The double factorial scale would be lost if continuation labels were allowed to repeat without repair.

If

\[
r=\alpha\frac{\log X}{\log\log X}
+o\left(\frac{\log X}{\log\log X}\right),
\qquad0<\alpha<1,
\]

then Stirling gives

\[
\boxed{
\mathcal C_r\le X^{-\alpha+o(1)}.
}
\]

This exponent is sharp for the coefficient vector: choose root `p_0=2` and the next `r` smallest primes. Their product is `X^{alpha+o(1)}`, so one surviving coefficient already has magnitude `X^{-alpha+o(1)}`.

Hence

\[
\boxed{
\mathcal C_r=X^{-\alpha+o(1)}.
}

This is an adjoint analogue of the positive factorial-depth law, now at the level of the root observer's unfolded Hilbert coefficient vector.

---

## 6. Critical global tail theorem

Let

\[
Y=(\log X)^2,
\qquad
K=\left\lfloor
\frac{\log X}{2\log\log X}
\right\rfloor,
\qquad
|t|\le\frac c{\log\log X}.
\]

Assume only

\[
\|Q\|_\infty=X^{o(1)},
\]

which is satisfied by the finite one-step discrete/continuum source on this boundary layer using its elementary total-mass bound.

The ratio of consecutive majorants in Section 4 is

\[
\frac{|t|\Lambda_X}{\sqrt{(r+1)(r+2)}}=o(1)
\]

uniformly for `r>=K-1`. Therefore the first omitted layer dominates the tail, and

\[
\boxed{
|t|\sum_{r\ge K-1}|t|^r
|\mathcal L\mathcal K^rQ|
\le X^{-1/2+o(1)}.
}
\]

Equivalently, the prime-rooted global continuation may be truncated after the first `K-1` Volterra layers with an RH-scale absolute remainder.

This closes a gap left by the state-space factorial theorem: the critical root weight `sqrt(p)` does not re-amplify the high-depth tail.

Freeze:

`STATE_TAIL_RH_SCALE + SQRT_PRIME_ROOT_OBSERVER -> GLOBAL_TAIL_RH_SCALE`.

The theorem controls only the high-depth tail. It does not estimate the signed front block of depths `<K-1`.

---

## 7. Sharpness for positive root-observed data

The half-depth threshold remains sharp after the root observer is attached.

Take the positive source `Q=1` and set total path arity

\[
k=K,
\qquad r=K-1.
\]

Because

\[
Y^K\le X,
\]

every `K`-element prime subset of the shell

\[
Y/2<p\le Y
\]

is admissible. The shell contains

\[
M_Y\sim\frac{Y}{2\log Y}
\]

prime labels, and

\[
\binom{M_Y}{K}=X^{1/2+o(1)}.
\]

For every such path,

\[
\sqrt{p_0}m_\gamma
\ge
\frac{\sqrt{Y/2}}X.
\]

Consequently

\[
\mathcal L_{X,Y,\sqrt\cdot}(\mathcal K^{K-1}\mathbf1)
\ge
X^{-1/2+o(1)}.
\]

Section 4 supplies the matching upper exponent, so

\[
\boxed{
\mathcal L_{X,Y,\sqrt\cdot}(\mathcal K^{K-1}\mathbf1)
=X^{-1/2+o(1)}.
}
\]

Thus neither the path-mass Hilbert factorization nor the square-root root weight permits a generic truncation at a smaller fixed fraction of the critical depth. Any shallower result must use the actual signed quadrature source `Q`, not positive capacity alone.

---

## 8. BRC interpretation

The proof uses three different information levels and keeps them typed.

1. **Unfolded path provenance:** `gamma=(p_0,...,p_r)` retains every ordered prime label.
2. **Positive surviving mass:** `m_gamma=floor(X/P_gamma)/X` is used only as a Hilbert measure.
3. **Signed source:** `Q(N_gamma,p_r)` is not replaced by absolute branch capacity until the explicit tail estimate.

Two quotients are safe in the proved scope:

- canonical increasing order removes permutation multiplicity;
- Cauchy splits one positive path mass between observer and source.

The following quotients remain unsafe for the front block:

- prime-label subset to arity only;
- terminal-state recoalescence without multiplicity/provenance repair;
- edge increments without the terminal mode;
- positive path capacity substituted for the signed source.

X6 remains a fixed local port. The critical depth is serial Factor-BRC provenance depth, not an increase in spatial dimension.

---

## 9. Exact checker

Task-local checker:

`experiments/rh_adjoint_rooted_resolvent_edge_energy_check.py`.

It verifies:

- root functional after `r` Volterra steps equals the explicit increasing-prime path sum;
- root-to-terminal edge telescoping;
- the path-mass Cauchy factors and factorial majorants;
- finite nilpotent-resolvent two-sided sup-norm bounds;
- finite critical tables for the weighted pairing.

The checker uses exact rational arithmetic wherever the square-root scalar observer is not required and floating evaluation only for the final finite Cauchy diagnostic. It is not an asymptotic proof and not evidence for RH.

---

## 10. New smallest research unit

The high-depth tail is now closed at the global root-observer level, and the half-depth threshold is known to be sharp for positive data.

The unresolved object is the signed front block

\[
\boxed{
\mathcal R_{<K}(X,t)
=t\sum_{r=0}^{K-2}(-t)^r
\mathcal L_{X,Y,\sqrt\cdot}(\mathcal K^rQ).
}
\]

The exact edge decomposition in Section 2 and the Stieltjes source representation from the parent Green identity should now be composed before any norm is taken.

The next admissible theorem is a prime-scale adjoint summation-by-parts formula in which the cumulative quadrature defect is paired with a discrete derivative of the adjoint Green field. The decisive alternatives are:

1. the derivative field has a subpolynomial Carleson/energy norm, yielding a genuine saving over root intensity;
2. a boundary/terminal mode reproduces the original `J_(1/2)` source, proving that the proposed adjoint normalization is only a reformulation;
3. cancellation occurs only after summing several rooted depths, identifying a new source-specific BRC invariant.

No RH proof is claimed.
