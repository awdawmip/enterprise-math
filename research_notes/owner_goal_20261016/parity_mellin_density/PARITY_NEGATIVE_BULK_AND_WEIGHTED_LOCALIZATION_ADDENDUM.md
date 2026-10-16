# All-residue leading term, negative bulk, and weighted localization

Author: **EM-PARITYREV-12B648**, same **RA-EB0794CB61621CB6E90B4730**.
Status: **UNREVIEWED_AUTHOR_PAPER**, separate addendum. The frozen 14049-byte
`PARITY_MELLIN_DENSITY_AND_ODD_ENDPOINT_OBSTRUCTION.md`, SHA256
`fe399bbdfa9b18a651f36f0c6b8819ac9a1c4ccc0762558fb74ecea734671779`,
is unchanged. No scientific program, enumeration, threshold evaluation, new
Native claim or run was used. This is not an independent review or a new Task.

All variables, observer-preservation restrictions and author/contribution
disclosures of that manuscript apply. In particular a=c=1, integer m>=3,
n=m-1, r=m(S+1)>=m, s=r+m, and H_(m,r) is exactly its fixed complete
residue–Beta density. The integral identity continues to hold for m=2, but the
asymptotic claims of this addendum exclude that value.

## 1. Every one of the m residues has the same leading term

Fix k in {0,...,n}, without deleting any residue. Use the parent notation
V,P,L,T and put

\[
\nu_{m,k}(r)=V(-r-k),\quad \tau_{m,k}(r)=(TV)(-r-k),\quad
d_{m,k}=(-1)^k k!(n-k)!,
\]
\[
\pi_{m,k}=\left.T_u(m-k+u)_m\right|_{u=0},
\]
\[
\Phi_{m,k}(r)=\left.T_uT_v
\frac{V(-r-k+u)(m-k+v)_m-(m-k+u)_mV(-r-k+v)}{u-v}
\right|_{u=v=0}.
\tag{1.1}
\]

The consistent finite polynomial extension of T is exactly the one justified
in parent Section 4.1. Since P_r(-r-k)=0 and

\[
P'_r(-r-k)=\prod_{0\le j\le n,\ j\ne k}(j-k)=d_{m,k},
\]

the same polynomial-diagonal calculation, with no extrapolation from k=0,
gives

\[
\boxed{
Z_s(-r-k)=\Phi_{m,k}(r)+d_{m,k}\nu_{m,k}(r)
+\frac{\nu_{m,k}(r)^2}{L_r}
-\frac{(\tau_{m,k}(r)-\pi_{m,k})^2}{L_s}.}
\tag{1.2}
\]

Here Phi_(m,k) is a polynomial of r-degree <=m, and pi_(m,k) is independent
of r. For each k in this fixed finite set,

\[
\nu_{m,k}(r)=(-1)^m r^m(1+O_m(r^{-1})),\qquad
\frac{\tau_{m,k}(r)}{\nu_{m,k}(r)}
=1+\frac{m^2}{2r}+O_m(r^{-2}).
\]

The coefficient of 1/r in the latter ratio does not depend on k. Applying
the parent rank-term calculation to (1.2), while retaining the
O(r^m) diagonal terms, proves

\[
\boxed{Z_s(-r-k)=-(m-1)r^{2m-2}+O_m(r^{2m-3}),\quad 0\le k\le n.}
\tag{1.3}
\]

The error is uniform in k because the index set is finite for fixed m. No
uniformity as m tends to infinity is asserted.

Substituting (1.3) into all m coefficients of H and applying the exact binomial
identity gives the coefficientwise, hence uniform-on-[0,1], limit

\[
\boxed{
r^{-(2m-2)}H_{m,r}(z)
\longrightarrow\frac{(-1)^m(m-1)}{n!}(1-z)^n.}
\tag{1.4}
\]

The sign (-1)^m includes the (-1)^n prefactor of the complete residue
formula. Its omission would reverse the odd-m conclusion.

## 2. An exact coefficient bound and uniform negative bulk

Define the polynomial

\[
\Psi_{m,k}(r)=L_rL_s(\Phi_{m,k}+d_{m,k}\nu_{m,k})
+L_s\nu_{m,k}^2-L_r(\tau_{m,k}-\pi_{m,k})^2.
\]

By (1.2) it equals L_r L_s Z_s(-r-k); by (1.3) its degree is 2m and
its leading coefficient is -m^2(m-1), for every k. Form

\[
\widehat H_m(\epsilon,z)
=(-1)^n\sum_{k=0}^{n}\frac{(-1)^kz^k}{k!(n-k)!}
\epsilon^{2m}\Psi_{m,k}(1/\epsilon).
\tag{2.1}
\]

This is an actual rational-coefficient polynomial in epsilon,z, not an
infinite series. For epsilon>0 it is exactly

\[
\widehat H_m(\epsilon,z)
=\epsilon^{2m} L_{1/\epsilon}L_{1/\epsilon+m}H_{m,1/\epsilon}(z).
\]

Put

\[
A_m=\frac{m^2(m-1)}{n!}>0,\qquad
\widehat H_m(0,z)=(-1)^m A_m(1-z)^n,
\]
\[
B_m=\sum_{j\ge1,\ell\ge0}
\left|[\epsilon^jz^\ell]\widehat H_m(\epsilon,z)\right|.
\tag{2.2}
\]

For 0<=epsilon<=1 and 0<=z<=1,

\[
\left|\widehat H_m(\epsilon,z)-(-1)^m A_m(1-z)^n\right|
\le B_m\epsilon.
\tag{2.3}
\]

Thus for odd m>=3, every real delta in (0,1) has the explicit threshold

\[
R_m^{\rm bulk}(\delta)
=\max\left\{m,\frac{2B_m}{A_m\delta^n}\right\},
\]

and

\[
\boxed{
r\ge R_m^{\rm bulk}(\delta),\quad 0\le z\le1-\delta
\quad\Longrightarrow\quad H_{m,r}(z)<0.}
\tag{2.4}
\]

Indeed the right side of (2.3), added to -A_m(1-z)^n, is at most
-A_m delta^n/2. The factors used to recover H from its normalized polynomial
are positive. This strengthens a negative endpoint interval to **every fixed
compact subinterval away from the right endpoint**, for all sufficiently
large r. It does not establish a single zero, an ordering of the zeros, or
pointwise positivity of H in the remaining right interval.

## 3. The negative bulk carries exponentially small weighted mass

Let delta in (0,1) be fixed and q=(1-delta)^(1/m). Equations (2.2)–(2.3)
and L_r L_s>=m^2 r^2 imply the global bound, for every m>=3 and r>=m,

\[
\sup_{0\le z\le1}|H_{m,r}(z)|
\le K_m r^{2m-2},\qquad K_m=(A_m+B_m)/m^2.
\]

The absolute contribution of t in [0,q] to the exact trace integral is
therefore at most

\[
\boxed{
\frac{m^m}{n!}K_m r^{2m-2}
\frac{q^{mr+1}}{mr+1}.}
\tag{3.1}
\]

This uses only (1-t)^n<=1 and the exact integral of t^(mr). Since
q^(mr)=(1-delta)^r, (3.1) is
O_(m,delta)(r^(2m-3)(1-delta)^r). It is an explicit exponentially decaying
bound for fixed m,delta, despite the negative density itself having polynomial
size on the left.

The previously proved complete trace tail is

\[
G_m(r)=\frac{m(m^2-1)}r+O_m(r^{-2}).
\]

Consequently the complementary right interval has the same leading positive
weighted integral after removing the exponentially small left contribution.
For odd m and r above both the bulk and positive-tail thresholds, H must have
a positive point in (1-delta,1), in addition to its negative left bulk. This
localization is of the **signed integral's necessary compensation**; it is
not a pointwise sign theorem for the entire right interval and supplies no
new compact-strip trace positivity.

The result explains why a large negative density on most fixed z-ranges is
compatible with a positive complete trace. A later comparison proof should
control the right-end weighted layer and the negative bulk separately with
their exact weights. Replacing the signed density by a uniformly nonnegative
one, or dropping its negative part without a proved bound, is not justified.

## 4. Review and continuation boundary

This addendum is independently frozen after the original manuscript, and any
review of the original manuscript alone does not cover it. A nonauthor review
should check the derivative d_(m,k), exact earlier-kernel subtraction in
(1.2), all-k parity and binomial constant in (1.4), polynomial degree and
positive denominator in (2.1), and the original t-weight in (3.1).

No numeric B_m, K_m, R_m^bulk or sampled zero was computed. No new tool,
Native vote, Result, Task completion or mother closure is claimed. This is
author-side progress within the original equal-block paper scope; the
all-S/all-gap problems remain open.

Researcher-ID: EM-PARITYREV-12B648 / TASK_RESEARCH
