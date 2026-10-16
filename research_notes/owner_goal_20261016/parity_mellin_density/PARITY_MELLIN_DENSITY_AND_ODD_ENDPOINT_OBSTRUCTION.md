# Exact residue–Beta density and an odd-order endpoint obstruction

Author: **EM-PARITYREV-12B648**, same actual session and
**RA-EB0794CB61621CB6E90B4730**. Status: **UNREVIEWED_AUTHOR_PAPER**.
This is new author-side paper work after the earlier nonblind partial review;
that historical review is not an independent vote on this paper. Shared control
context and all prior Parity/Public129/T6/P11 contributions are retained.
No new enumeration, scientific program, checker, Native claim or Native run was
used. Activity/persistence permission is not official Task execution authority.

## 1. Scope, retained observer, and source inputs

Work only in the original equal-block specialization **a=c=1**, with integer
m>=2, real S>=0, n=m-1, r=m(S+1)>=m and s=r+m. Write

\[
G_m(r)=\operatorname{tr}(B^{-1}A)-n.
\]

The actual forms A and B, their transfer direction and their transposes are
exactly those of the frozen source beta-kernel reduction. This paper adds a
representation of that complete scalar; it does not redefine A or B. The exact
source inputs are the immutable whole-unit partial capsule at Source
`b46c77b64f5f42ed98a14f94dda29d4e2dc2cfac`, especially
`author_support/BETA_ADAPTED_TRACE_KERNEL.md` and
`author_support/BETA_KERNEL_SELF_AUDIT_ADDENDUM.md`. The latter's (4.1) is the
residue identity used below. Original beta/inverse/normalization authors and
direction/scope contributors retain their credit, as enumerated in the input
manifest. The separately published author theorem at Source
`df5869771ff760a0b57a5d757934f0ab9f56f07e` supplies only the positive large-r
trace conclusion used in Section 6.

P000/Heartbeat X6 remains the native research basis: no native plane or change
of spatial dimension is introduced. The real variables x,y,z,t,r,S below are
external algebraic/integral variables for a declared scalar observer, not
native coordinates, native spatial axes or physical time. The exact signed
residue–integral identity certifies preservation of the **complete trace gap**.
It does not certify reconstruction, redundancy or positivity of the original
branch masses, nor replacement of their joint provenance. No future operation
on the original branches is authorized by this scalar equality.

The exact density identity holds for every m>=2 in this scope. The endpoint
asymptotic and its threshold below are asserted for **m>=3**; the obstruction to
pointwise nonnegative density is asserted for **odd m>=3**. No statement here
extends to unequal a,c or to all original gaps.

## 2. Frozen polynomial kernel and the complete residue sum

Use

\[
\theta_i=(i+1)/m,\qquad
V(x)=\prod_{j=0}^{n}(x-\theta_j),\qquad P_t(x)=(t+x)_m,
\]
\[
R_t=P_t-V,\qquad L_t=mt+\beta_m,\qquad \beta_m=(m^2+1)/2.
\]

The reduced Bezout polynomial from the fixed input is

\[
\mathcal B_t(x,y)=
\frac{V(x)R_t(y)-R_t(x)V(y)}{x-y}
-\frac{R_t(x)R_t(y)}{L_t}.
\tag{2.1}
\]

Both quotient expressions in this paper are polynomial divided differences,
including on the diagonal. The frozen degree cancellation gives degree at most
m-2 in each variable in (2.1). Let E_m f(x)=f(x+m) and

\[
T=2(I+E_m)^{-1},\qquad
Z_s(x)=\left[T_xT_y\mathcal B_s(x,y)-\mathcal B_r(x,y)\right]_{y=x}.
\tag{2.2}
\]

The source transfer is T g_(2m)=g_m, not the reverse; its two-variable action
in (2.2) retains both matrix-side transposes of the full trace contraction.
The source residue identity, with all m terms present, is

\[
b_k=\frac{(-1)^k Z_s(-r-k)}{k!(n-k)!},\qquad
G_m(r)=(-1)^n\sum_{k=0}^{n}
\frac{b_k}{\prod_{j=0}^{n}(r+k+\theta_j)}.
\tag{2.3}
\]

In the source derivation, the polynomial part of Z_s/P_r is annihilated by the
n-th finite difference. We reuse that exact, observer-specific annihilation;
we do not discard an untested signed component of the scalar.

Define the **fixed residue–Beta density polynomial**

\[
H_{m,r}(z)=\sum_{k=0}^{n}h_k(r)z^k,
\qquad h_k(r)=(-1)^n b_k.
\tag{2.4}
\]

The following obstruction concerns this particular polynomial and this
particular Beta representation. It does not rule out other integral
representations or the source's different finite-difference derivative
integrand.

## 3. Exact Mellin/Beta representation

For every k=0,...,n, the elementary beta integral gives

\[
\int_0^1 t^{m(r+k)}(1-t)^n\,dt
=\frac{n!}{\prod_{a=1}^{m}(m(r+k)+a)}.
\]

Since the denominator on the right is m^m times the denominator in (2.3),

\[
\boxed{
G_m(r)=\frac{m^m}{n!}
\int_0^1 t^{mr}(1-t)^n H_{m,r}(t^m)\,dt .}
\tag{3.1}
\]

This exchanges a finite sum with an absolutely convergent integral; r>=m
ensures all exponents and beta factors are admissible. The prefactor is
positive. All residues and all signs in (2.3) are retained. Pointwise
H_(m,r)>=0 would be a sufficient condition for nonnegative G, but is stronger
than positivity of the complete integral.

## 4. Exact endpoint identity and its asymptotic

We prove the following statement without evaluation at any sampled m or r.

**Endpoint lemma.** For each fixed integer m>=3,

\[
\boxed{Z_{r+m}(-r)=-(m-1)r^{2m-2}+O_m(r^{2m-3})}
\qquad(r\longrightarrow+\infty).
\tag{4.1}
\]

### 4.1 The polynomial operator extension is legitimate

For each d>=0, E_m preserves the polynomials of degree <=d and has triangular
diagonal 1 in the monomial basis. Thus I+E_m has diagonal 2 and an inverse on
that space. These inverses agree on nested degree spaces by uniqueness.
Consequently T has a consistent action on every polynomial. Using that action
on separated terms of (2.1), and then adding them, agrees exactly with the
original action on its degree <=m-2 sum. No new functional inverse, convergence
assumption or extension to arbitrary functions is being used.

On any one of these finite degree spaces, with D=d/dx,

\[
T=\frac{2}{I+\exp(mD)}
=I-\frac m2D+D^2 A_m(D),
\tag{4.2}
\]

where A_m is a fixed polynomial after truncation to degree <=m. This is a
nilpotent polynomial identity; the displayed remainder is sufficient and need
not be interpreted as an infinite analytic series.

### 4.2 Separate the low-r-degree term from the rank-one terms

The V(x)V(y) terms cancel in the numerator of (2.1). Set

\[
F_t(x,y)=\frac{V(x)P_t(y)-P_t(x)V(y)}{x-y},
\qquad \mathcal B_t=F_t-R_t(x)R_t(y)/L_t.
\]

Use independent auxiliary shifts u,v, both with r held fixed, and define

\[
\nu_m(r)=V(-r),\quad \tau_m(r)=(TV)(-r),\quad
\pi_m=\left.T_u(m+u)_m\right|_{u=0},
\]
\[
\Phi_m(r)=\left.T_uT_v
\frac{V(-r+u)(m+v)_m-(m+u)_mV(-r+v)}{u-v}
\right|_{u=v=0}.
\tag{4.3}
\]

Here pi_m is constant in r. The divided difference in (4.3) is a polynomial
in r,u,v and has degree at most m in r: its numerator has that degree, and
division by the monic u-v, independent of r, cannot increase it. T_u,T_v do
not act on r. Hence Phi_m is a polynomial in r of degree at most m.

At x=-r, P_r(x)=0 and P'_r(x)=n!, so the polynomial diagonal of F_r is

\[
F_r(-r,-r)=-n!\nu_m(r).
\]

Also P_s(-r+u)=(m+u)_m, and therefore
T R_s(-r)=pi_m-tau_m(r). Substitution in (2.2) gives the **exact identity**

\[
\boxed{
Z_s(-r)=\Phi_m(r)+n!\nu_m(r)
+\frac{\nu_m(r)^2}{L_r}
-\frac{(\tau_m(r)-\pi_m)^2}{L_s}.}
\tag{4.4}
\]

In particular the minus sign in the earlier coalescent kernel of (2.2) has
not been changed to a later-kernel subtraction.

### 4.3 Leading cancellation and a controlled remainder

The monic degree-m polynomial V satisfies

\[
\nu_m(r)=(-1)^m r^m(1+O_m(r^{-1})),\qquad
\frac{V'(-r)}{V(-r)}=-\frac m r+O_m(r^{-2}),
\]

and each higher derivative obeys V^((j))(-r)/V(-r)=O_m(r^(-j)). Since T on
V is finite, (4.2) yields

\[
\frac{\tau_m(r)}{\nu_m(r)}
=1+\frac{m^2}{2r}+O_m(r^{-2}).
\tag{4.5}
\]

Using L_r=mr+beta_m and L_s=mr+m^2+beta_m, expand only to first relative
order:

\[
\begin{aligned}
\frac{\nu_m^2}{L_r}-\frac{\tau_m^2}{L_s}
&=\frac{\nu_m^2}{mr}
\left[1-\frac{\beta_m}{mr}
-\left(1+\frac{m^2}{r}
-\frac{m^2+\beta_m}{mr}\right)+O_m(r^{-2})\right]\\
&=-(m-1)r^{2m-2}+O_m(r^{2m-3}).
\end{aligned}
\tag{4.6}
\]

The pi_m cross term 2*pi_m*tau_m/L_s is O_m(r^(m-1)); pi_m^2/L_s is
O_m(r^(-1)). The remaining Phi_m+n!*nu_m is O_m(r^m). For m>=3, all these
orders are at most 2m-3. Equations (4.4)–(4.6) prove (4.1).
For m=2 the O(r^m) term has the same order as the proposed leading term;
discarding it would be invalid. This paper makes no such m=2 endpoint claim.

## 5. A finite coefficient threshold, with no enumeration

The endpoint sign can be made effective entirely within polynomial algebra.
Define the rational-coefficient polynomial

\[
\Psi_m(r)=L_rL_s(\Phi_m(r)+n!\nu_m(r))
+L_s\nu_m(r)^2-L_r(\tau_m(r)-\pi_m)^2.
\tag{5.1}
\]

Its equality to L_rL_s Z_s(-r) is exact. By (4.1), for m>=3 its degree is
exactly 2m and its leading coefficient is -m^2(m-1). In particular the nominal
degree-(2m+1) coefficient of the last two terms cancels. The first term has
degree <=m+2<=2m-1. Put

\[
W_m(\epsilon)=\epsilon^{2m}\Psi_m(1/\epsilon),\qquad
c_m^{\rm dens}=m^2(m-1),
\]
\[
C_m^{\rm dens}=\sum_{j\ge1}|[\epsilon^j]W_m|,\qquad
R_m^{\rm dens}=\max\left\{m,\frac{2C_m^{\rm dens}}{c_m^{\rm dens}}\right\}.
\tag{5.2}
\]

These are finite rational polynomial definitions, not a numerical estimate or
a reported calculation. W_m(0)=-c_m^dens. If r>=R_m^dens, epsilon=1/r<=1 and

\[
W_m(1/r)\le-c_m^{\rm dens}+C_m^{\rm dens}/r
\le-c_m^{\rm dens}/2<0.
\]

Because r and both L factors are positive,

\[
\boxed{r\ge R_m^{\rm dens}\quad\Longrightarrow\quad Z_s(-r)<0.}
\tag{5.3}
\]

No coefficients in (5.2) were evaluated by a program; the threshold is a
computable formula, not a claim that its size is practical or uniform in m.

## 6. Negative density on an interval, with a positive complete trace

At z=0, (2.4) gives

\[
H_{m,r}(0)=\frac{(-1)^n}{n!}Z_s(-r).
\tag{6.1}
\]

For odd m>=3, n is even. Thus every r>=R_m^dens has h_0<0. This is not
merely a value at a zero-weight endpoint: with

\[
C_H=\sum_{k=1}^{n}|h_k|,\qquad
\delta=\frac{|h_0|}{2(C_H+|h_0|)}\in(0,1/2],
\]

one has for 0<=z<=delta

\[
H_{m,r}(z)\le h_0+C_H z<h_0/2<0.
\tag{6.2}
\]

Consequently the actual integrand of (3.1) is negative on
0<t<=delta^(1/m), a nonempty interval of positive measure.

The separate effective-tail theorem proves G_m(r)>0 for r>=R_m^tail, where
R_m^tail is its explicit N/D coefficient threshold. Therefore, for each odd
m>=3 and every

\[
r\ge\max\{R_m^{\rm dens},R_m^{\rm tail}\},
\]

the **same** representation (3.1) has a negative left interval and a strictly
positive complete integral. Since its weight is positive on (0,1), it also
must have a positive-density point in (0,1); by continuity the density changes
sign. In particular the canonical residue–Beta density is not pointwise
nonnegative on the whole domain, even within a proven positive-trace tail.

This disproves that one stronger proof route. It is not a counterexample to
the trace inequality, not a statement about all possible densities, and not
the old m=3 entrywise comparison obstruction. Odd m>=5 are included without
using, rerunning or extending any old finite fixture.

## 7. A cancellation-aware sufficient condition and a bounded next question

Negative left density means that a successful proof using (3.1) must retain
the weighting and the compensating signed terms. The following scalar test is
one exact sufficient condition; its validity as a general inequality for the
actual coefficients is **not** asserted.

Let

\[
M_k(r)=\int_0^1t^{mr+mk}(1-t)^n\,dt,\qquad
\rho_k(r)=\frac{M_k}{M_0}
=\prod_{a=1}^{m}\frac{mr+a}{mr+mk+a}.
\]

Then rho_0=1 and 0<rho_k<=1. In particular

\[
\frac{n!}{m^m M_0}G_m(r)
=\sum_{k=0}^{n}h_k\rho_k
=H_{m,r}(1)-\sum_{k=1}^{n}h_k(1-\rho_k).
\tag{7.1}
\]

Write (h)_+=max(h,0). Since the omitted negative-h terms in the following
bound are beneficial, the elementary implication

\[
\boxed{
H_{m,r}(1)>\sum_{k=1}^{n}(h_k)_+(1-\rho_k)
\quad\Longrightarrow\quad G_m(r)>0}
\tag{7.2}
\]

is rigorous, including when h_0<0. The product inequality
1-product(1-u_a)<=sum u_a, 0<=u_a<=1, additionally gives

\[
0\le1-\rho_k\le\frac{mk}{r}.
\]

Thus H_(m,r)(1)>(m/r) sum_(k>=1) k(h_k)_+ is an even stronger sufficient
condition, with no conclusion asserted about whether it holds.

The next proposed **single paper unit**, not an authorized scientific run, is
to prove or refute the exact endpoint-defect condition (7.2) for the actual
kernel coefficients on the remaining equal-block compact strips
m<=r<R_m^tail, first retaining m symbolically and all k terms. Its output must
be either a proved, explicitly delimited nonempty parameter subclass or a
strict algebraic obstruction to that sufficient condition. It must not count
the prior positive tail as new coverage. The conservative positive-part bound
may be too strong; if it loses the cancellations needed by the actual kernel,
that is a kill condition for this proposed route, not a trace counterexample.

Budget and termination boundary: one symbolic derivation, no parameter scan,
no new certificate/checker, no new Task, no unregistered claim. Do not append
an unbounded search for a different criterion if the sufficient condition
fails. A later execution, if actually useful, requires its own exact task and
current authority; this paper does not provide them.

## 8. Status and independent-review boundary

New claims requiring nonauthor review are the constant in (3.1), the finite
operator extension and exact identity (4.4), the asymptotic (4.1), the effective
threshold (5.2)–(5.3), and the carefully scoped obstruction (6.2). The
elementary sufficient implication (7.2) is a proved conditional, not a proof
that its premise holds for any unresolved compact strip.

The author has not issued a Native review vote, Result, Tool promotion,
SATISFIED, Task completion or mother closure. The all-m/all-S equal-block sign
and all-gap parity domination remain open outside the already proved and
separately delimited tail. The input manifest records the prior paper review
as reviewer-observed provenance; this paper does not counterfeit a fresh
independent Source/API read of that review or extend its verdict to this unit.

Researcher-ID: EM-PARITYREV-12B648 / TASK_RESEARCH
