# The positive-part endpoint test cannot certify the whole positive tail

Author: **EM-PARITYREV-12B648**, same **RA-EB0794CB61621CB6E90B4730**.
Status: **UNREVIEWED_AUTHOR_PAPER**. This is a separate paper extension, not
a modification of the frozen 14049-byte density manuscript or its 6711-byte
bulk addendum. The original sufficient implication is correct. The result
below shows that its premise is too strong to hold throughout the positive
large-r tail. No new enumeration, symbolic/numerical program or checker was
used. No Native execution, acceptance, Tool promotion or Task closure follows.

Use precisely the parent scope a=c=1, integer m>=2, n=m-1, real r>=m and
s=r+m, with all m residues retained. All algebraic variables remain auxiliary
external scalar-observer variables within the fixed Heartbeat X6 basis. The
author/contribution history and lack of independent self-review are unchanged.

## 1. Exact condition being tested

The density manuscript proves the implication

\[
H_{m,r}(1)>T_m^+(r),\qquad
T_m^+(r)=\sum_{k=1}^{n}(h_k(r))_+\bigl(1-\rho_k(r)\bigr)
\quad\Longrightarrow\quad G_m(r)>0,
\tag{1.1}
\]
\[
\rho_k(r)=\prod_{a=1}^{m}\frac{mr+a}{mr+mk+a}.
\]

The new assertion is:

**Proposition.** For each fixed integer m>=4, there exists a finite r_m such
that every r>=r_m satisfies

\[
\boxed{H_{m,r}(1)<T_m^+(r).}
\tag{1.2}
\]

Thus (1.1) fails throughout a sufficiently distant part of the already proved
positive trace tail. It remains a logically valid sufficient condition, and
this proposition does not decide it on the unresolved compact strips. It
does not give a trace counterexample. No claim for m=2 or m=3 is made here.

## 2. A joint polynomial extension bounds the endpoint cancellation

Keep the bulk addendum's definitions nu_(m,k),tau_(m,k),pi_(m,k),Phi_(m,k).
Now regard k as an auxiliary real polynomial variable, only for a degree
argument. Set

\[
d_m(k)=\left.\frac{d}{du}(u-k)_m\right|_{u=0}.
\]

This has degree at most m-1 in k; at the actual integer grid k=0,...,n it is
exactly (-1)^k k!(n-k)!. The polynomials nu(r,k) and tau(r,k) have total
degree at most m in r,k, and pi(k) has degree at most m. In the defining
divided difference for Phi, the numerator has total degree at most 2m in
r,k,u,v. Its quotient by the homogeneous linear polynomial u-v has total
degree at most 2m-1. T_u,T_v are finite sums of derivatives with coefficients
depending only on fixed m, so they cannot increase this degree. Therefore

\[
\deg_{\rm total}\Phi(r,k)\le2m-1.
\]

Define the polynomial extension

\[
\Psi_m(r,k)=L_rL_s\bigl(\Phi(r,k)+d_m(k)\nu(r,k)\bigr)
+L_s\nu(r,k)^2-L_r\bigl(\tau(r,k)-\pi(k)\bigr)^2.
\tag{2.1}
\]

Every summand has total degree at most 2m+1. At each actual residue integer
k=0,...,n, the bulk addendum proves

\[
\Psi_m(r,k)=L_rL_s Z_s(-r-k).
\tag{2.2}
\]

Equation (2.2) is asserted only on that grid. Away from it, P_r(-r-k) need
not vanish and (2.1) need not equal the complete original Z expression.
The extension is solely an interpolation/degree device and does not introduce
new original-domain residues.

The exact grid values and the complete residue signs now give

\[
L_rL_s H_{m,r}(1)
=\frac{(-1)^n}{n!}\sum_{k=0}^{n}(-1)^k\binom nk\Psi_m(r,k).
\tag{2.3}
\]

The alternating sum annihilates every polynomial in k of degree less than
n. For a monomial r^p k^q surviving this sum, q>=n and p+q<=2m+1; hence
p<=2m+1-n=m+2. Consequently (2.3) is a polynomial in r of degree at most
m+2. Since L_rL_s is asymptotic to m^2r^2,

\[
\boxed{H_{m,r}(1)=O_m(r^m).}
\tag{2.4}
\]

This upper bound suffices; it is not a claim that the true degree attains m.
It uses all grid coefficients before taking any positive part.

## 3. One positive coefficient already dominates that endpoint bound

The separately proved all-residue leading formula gives, for each actual k,

\[
h_k(r)=\frac{(-1)^{m+k}(m-1)}{k!(n-k)!}
r^{2m-2}+O_m(r^{2m-3}).
\tag{3.1}
\]

For fixed positive k, direct expansion of the finite product gives

\[
1-\rho_k(r)=\frac{mk}{r}+O_m(r^{-2}).
\tag{3.2}
\]

If m is odd and m>=5, choose k_*=1. If m is even and m>=4, choose k_*=2.
In either case 1<=k_*<=n and m+k_* is even. Thus its coefficient in (3.1)
is strictly positive and h_(k_*)(r)>0 for all sufficiently large r. All terms
of T_m^+ are nonnegative, so (3.1)–(3.2) yield

\[
T_m^+(r)\ge
\frac{mk_*(m-1)}{k_*!\,(n-k_*)!}\,
r^{2m-3}+O_m(r^{2m-4}).
\tag{3.3}
\]

In particular it is bounded below by half of that positive leading monomial
for all sufficiently large r. For m>=4, 2m-3>m. Combining (2.4) and (3.3)
shows H_(m,r)(1)/T_m^+(r)->0, and proves the strict failure (1.2).
The argument requires no choice of a numeric m or any evaluated threshold.
It gives an existence threshold; no explicit small or practical value is
claimed in this proposition.

## 4. What the obstruction does and does not close

The exact signed normalized integral is

\[
\sum_k h_k\rho_k
=H(1)-\sum_{k\ge1}h_k(1-\rho_k).
\]

Replacing the final signed sum by its positive-coefficient portion removes
large beneficial negative-coefficient terms. The proposition demonstrates a
rigorous cost of that loss: for every m>=4 the resulting sufficient test
eventually fails, even though the complete signed trace is independently
positive there. The stronger bound with (m/r)sum k(h_k)_+ fails as well,
since it is an upper bound for T_m^+.

This gives a kill condition for using the positive-part endpoint test as a
uniform all-S route. The parent's deliberately compact-only next question is
not settled by a large-r failure. It must either establish a genuinely new
compact subclass or stop if the same cancellation loss blocks it; it cannot
reuse the already proved positive tail as evidence for its premise.

Pointwise positivity of every alternative representation, positivity of the
old finite-difference derivative integrand, and the complete all-m/all-S trace
question remain undecided. No branch mass or source joint relation has been
declared redundant. New review must explicitly cover this total-degree
extension and the distinction between polynomial interpolation and the actual
finite residue domain. Older density/bulk review verdicts do not propagate.

Researcher-ID: EM-PARITYREV-12B648 / TASK_RESEARCH
