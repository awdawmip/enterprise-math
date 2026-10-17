# Actual Student Ae parity-cut factors and full-trace prefix feasibility

Status: LOCAL_AUTHOR_FEASIBILITY_COMPLETE_UNREVIEWED. Sole new mathematical
author: EM-PUBLIC-7CDA51. This is one bounded original-model structural
interface, RESULT_ONLY / COMPOSE, not a general Tool or independent paper.
Root supplied direction/control permission and zero mathematics. BFF, CF
and 4A have not received this new proof or supplied construction/repair
before the external freeze. Their genuine older Student/COMMON work and
all warm NONBLIND history remain credited; classical facts are not new
priority claims here.

## 1. Different method, finite discriminator, and exact scope

The preceding metric feasibility result excludes fixed or polynomial-
conditioned positive spectral reductions of actual Z on its stated real
window. We do not attempt to repair that method. Instead we retain the
ORIGINAL positive Student inner product and use only an orthogonal sign
change of basis. The question is whether the actual dense Ae has exact
low-rank CROSS-DEGREE-CUT structure, sufficient to recast the literal
Ae-weighted trace as signed weighted-prefix contractions with all matrix
entries and cross terms present.

The finite discriminator is explicit actual-m factors and their true cut
rank, together with an identity for the complete weighted C term. A generic
rank statement without this caller would be REUSE. A change of Student
space, a missing pole factor, or a lost boundary/full-frame term would be
HOLD. Even a successful factorization does not prove a quantitative
complex bound: if only entrywise positivity or absolute HS inequalities
remain, quantitative Ae/fullPsi stays HOLD.

We obtain an exact rank-at-most-two cross-cut factorization in EACH parity,
with explicit positive Gamma factors, and an exact full-C prefix identity.
Nontrivial two-by-two cross-cut minors have rank exactly two. This is not
the older GLOBAL rank-two positive leakage R_leak, and it does not make
Ae itself rank two or positive. We give a real negative direction to
prevent the latter false inference. Quantitative signed-prefix control
is not obtained; the exploration stops at that precise interface.

## 2. Original carrier, actual Ae, and polynomial basis

Let m>=7 be an integer. On the SAME space V=C[v]_(degree<=m-2), use

 rho_m(v)=(1+4v^2)^(-m),
 <f,g>_m=integral_R conjugate(f(v)) g(v) rho_m(v) dv.

Let P_j be the actual monic orthogonal polynomials, h_j their positive
squared norms, and p_j=P_j/sqrt(h_j), for j=0,...,m-2. Thus the dimension
is m-1; no even/odd top vector has been deleted. Reflection is v->-v.
The original accepted Ae compression is

 Ae=Pi a(v) Pi,    a(v)=(1/4-v^2)/(v^2+1/4)^2
                   =8/(1+4v^2)^2-4/(1+4v^2).                 (A1)

Pi is the genuine orthogonal projection onto this SAME V, not a trace-only
substitution or a different m+a model. In the real p_j basis its entries
are integral p_i a p_j rho_m. They are real symmetric and vanish for
opposite parities. Daggers are the actual positive adjoints; # below means
coefficient transpose, so analytic squares are retained off the real axis.

The literal model and (A1) are already genuine inputs of the accepted wide
partial whole: primary62848 SHA256
460c8a0feae8689f7a993b27eb5cd783ca79776b97255337ff54ea4aa2633a87,
Source92496320c34767dc1f63b6e18d76170cb6b59f47, with genuine independent
review Sources43f967f750443f688a0c421aae1252f0f576341b and
c07678e240aace68ec3bc4a9493c5fffa69e5a0a. We use its original Ae/model
interface, not its unproved quantitative Ae target. The old Student
Pearson/basis facts have actual A/BFF upstream history. For this new
interface all pole evaluations, signs, constants, and contractions are
proved in full below; no new unpublished lemma is an axiom. The new
metric result motivates avoiding metric distortion but is not a logical
premise for any formula in this note. No new repository/library search
or external primary was used.

Put sigma(v)=v^2+1/4 and xi=i/2, so sigma=(v-xi)(v+xi). Define

 nu_j=j(2m-1-j),                  0<=j<=m-2.                   (A2)

The following actual-m Rodrigues identity will also establish all needed
normalizations:

 P_j(v)=c_j sigma(v)^m D_v^j sigma(v)^(j-m),
 c_j=(-1)^j/(2m-2j)_(j,rise).                                 (A3)

Indeed Leibniz expansion after factoring sigma shows this is a polynomial
of degree j. Its leading coefficient is
c_j(2j-2m)_(j,fall)=1. Multiplying by rho_m gives
c_j 4^(-m)D_v^j sigma^(j-m). Integrating j times against a polynomial of
degree below j proves orthogonality. All boundary terms vanish: their
worst power at infinity is at most 2j-2m<=-4. This identifies the ORIGINAL
monic P_j, not a different measure's polynomial. Its actual norm is also
explicit: integrate (A3) j times against P_j and use D_v^j P_j=j! to obtain

 h_j = sqrt(pi) j! Gamma(m-j-1/2)
       /[2*4^j Gamma(m-j)(2m-2j)_(j,rise)].                    (A5)

Here integral sigma^(-(m-j))
 =2^(2(m-j)-1)sqrt(pi)Gamma(m-j-1/2)/Gamma(m-j), a convergent real beta
integral. Thus all h_j in the following factors are the ORIGINAL norms,
not undetermined normalization constants or another Student energy.

For later derivatives the self-adjoint Pearson operator is

 L=-sigma D_v^2+2(m-1)v D_v,
 L p_j=nu_j p_j.                                               (A4)

One can verify this without importing another basis theorem: L preserves
polynomial degree, has leading coefficient nu_j on v^j, and integration by
parts makes it symmetric under rho_m. Its boundary term has power at most
-3 in the degree range here. Orthogonality then forces (A4). All shifted
Gamma arguments below have m-j>=2.

## 3. Actual Cauchy factors at the two fixed poles

For zeta outside R let

 r_j(zeta)=integral_R p_j(v)rho_m(v)/(v-zeta) dv.                (P1)

There is no factor 1/(2pi i) in this definition. Polynomial division and
orthogonality give, for 0<=i<=j<=m-2,

 integral_R p_i(v)p_j(v)rho_m(v)/(v-zeta) dv
                  =p_i(zeta) r_j(zeta).                       (P2)

The discarded quotient has degree i-1<j; hence (P2) is exact even when
i=j. Differentiation in zeta gives the double-pole integral
p_i'(zeta)r_j(zeta)+p_i(zeta)r_j'(zeta). The derivative sign is positive
because d_zeta (v-zeta)^(-1)=(v-zeta)^(-2).

Here are explicit ORIGINAL-m factors. Define positive numbers

 alpha_j = [(m-j)_(j,rise)/(2m-2j)_(j,rise)]/sqrt(h_j),
 beta_j  = sqrt(pi) j! Gamma(m-j+1/2)
                   /[4^j Gamma(m+1) sqrt(h_j)].               (P3)

Then

 p_j(xi)=i^j alpha_j,          r_j(xi)=i^(1-j) beta_j.          (P4)

To check the first formula directly in (A3), multiply out the factors
(v-xi) and (v+xi). At v=xi only the term with all j derivatives on
(v-xi)^(j-m) survives; it is
c_j(j-m)_(j,fall)(2xi)^j
 =i^j (m-j)_(j,rise)/(2m-2j)_(j,rise).

For the second formula, j integrations by parts in the UNNORMALIZED
P_j Cauchy integral give

 integral_R P_j(v)rho_m(v)/(v-xi) dv
 =c_j 4^(-m) j! integral_R
          (v-xi)^(-m-1)(v+xi)^(j-m) dv.                       (P5)

The signs from the two differentiations cancel before the factor c_j.
Close the real line by the counterclockwise upper semicircle. The arc
vanishes since the integrand is O(|v|^(j-2m-1)). Its sole upper pole is
xi, order m+1. The residue is

 (-1)^m (m-j)_(m,rise) (2xi)^(j-2m)/m!.

Multiplying by 2pi i, by c_j 4^(-m)j!, and using 2xi=i gives

 i^(1-j) 4^(-m) 2pi j! Gamma(2m-2j)
                          /[Gamma(m-j)Gamma(m+1)]
 =i^(1-j) sqrt(pi) j! Gamma(m-j+1/2)
                          /[4^j Gamma(m+1)].                 (P6)

The last equality is the classical Gamma duplication identity. Dividing
by sqrt(h_j) proves (P4); no probability or positive-complex-phase
interpretation has been used. This residue evaluation is a hand identity,
not a numerical integration or a new primary lookup.

## 4. Pole derivatives, parity, and exact rank-two cuts

At sigma(xi)=0, (A4) implies

 p_j'(xi)=nu_j p_j(xi)/[2(m-1)xi].                            (C1)

Moving the symmetric L through the integral in (P1) gives

 sigma(zeta)r_j''(zeta)+2(m+1)zeta r_j'(zeta)
                              +(nu_j+2m)r_j(zeta)=0.          (C2)

For completeness, L_v(1/(v-zeta)) equals
-sigma(zeta)*2/(v-zeta)^3
-2(m+1)zeta/(v-zeta)^2-2m/(v-zeta).
The same integration-by-parts boundary vanishes. Thus at xi,

 r_j'(xi)=-(nu_j+2m)r_j(xi)/[2(m+1)xi].                       (C3)

Now a(v)=-1/2[(v-xi)^(-2)+(v+xi)^(-2)]. Parity gives
p_i(-xi)=(-1)^i p_i(xi), r_j(-xi)=(-1)^(j+1)r_j(xi), with
corresponding differentiated signs. Consequently, for i<=j,

 (Ae)_(ij)=0                       if i+j is odd,
 (Ae)_(ij)=-[p_i'(xi)r_j(xi)+p_i(xi)r_j'(xi)]
                                      if i+j is even.         (C4)

Use the orthogonal diagonal sign matrix

 U_(jj)=(-1)^floor(j/2),       U^T U=I,       U^(-1)=U.

This basis change has condition number exactly1 in the ORIGINAL norm.
For Atilde=U Ae U, (P4),(C1),(C3) give the exact real formula

 Atilde_(ij)=alpha_i beta_j (T_j-S_i),        i<=j, i+j even,
 S_i=nu_i/(m-1),              T_j=(nu_j+2m)/(m+1),              (C5)

with symmetry below the diagonal and zero opposite-parity entries.
All i factors have canceled; no absolute value has replaced a signed
matrix entry. Moreover

 T_j-S_i=(nu_j-nu_i)/(m+1)
                     +2(m-i)(m-i-1)/(m^2-1)>0                (C6)

for i<=j<=m-2. Thus both parity blocks have positive ENTRIES in this
orthogonal sign convention. This is not a positive-semidefinite claim.

For any cross-degree cut in one ordered parity block, rows i are all
below columns j. Formula (C5) is the two-column factorization

 Atilde_(ij) = alpha_i*(beta_j T_j)
                              -(alpha_i S_i)*beta_j.          (C7)

Every such rectangular block has rank at most2. If it has two distinct
rows i1<i2 and two distinct columns j1<j2, its two-by-two determinant is

 alpha_i1 alpha_i2 beta_j1 beta_j2
                  *(S_i2-S_i1)*(T_j2-T_j1)>0.                 (C8)

Indeed nu_j is strictly increasing on0,...,m-2. Therefore every cut with
at least two rows and two columns has rank EXACTLY2. A one-row/one-column
cut has the corresponding smaller rank. This is a statement about
separated cuts, not the rank of an entire parity block or of Ae. Neither
Pi nor the top carrier vector was omitted in its derivation.

## 5. Why entrywise positivity cannot replace signed cancellation

The original Ae is indefinite for m>=7. Its constant-polynomial Rayleigh
quotient is

 <1,Ae1>/<1,1>=(4m-2)/(m+1)>0.                                (S1)

The also-actual polynomial f(v)=v^(m-2) has quotient

 <f,Aef>/<f,f>=6(4-m)/[m(m+1)]<0.                             (S2)

Here is an exact check of these two elementary integral evaluations. For
any r=0,...,m-2, normalize v^(2r)rho_m to a probability measure solely on
the REAL line. The ratios obtained by a beta integral, or by its single
integration-by-parts recurrence, are

 E_r[(1+4v^2)^(-1)]=(m-r-1/2)/m,
 E_r[(1+4v^2)^(-2)]
             =(m-r-1/2)(m-r+1/2)/[m(m+1)].                    (S3)

For example substitute x=4v^2 in each real integral: the common factor
cancels and the beta arguments are r+1/2,m-r-1/2. Insert (S3) into the
actual a=8/(1+4v^2)^2-4/(1+4v^2). At r=0 this is (S1); at r=m-2 it is
(S2). These are identities in the ORIGINAL quadratic form, not energy
bounds imported from a shifted Student carrier.

In particular (C6) is no basis for a probability shortcut, positivity of
all analytic contractions, or an Ae-positive-operator route. For complex
vectors even a positive operator would not make x^T Atilde x a Hermitian
positive form. This note retains analytic squares and their signed sums.

## 6. Two actual weighted prefixes and the complete weighted trace

Work separately on each full parity index set I_p={p,p+2,...,<=m-2}.
For any real or complex vector x on I_p define the actual weighted prefixes

 X_j(x)=sum_(i<j,i in I_p) alpha_i x_i,
 Y_j(x)=sum_(i<j,i in I_p) alpha_i S_i x_i,
 d_j=alpha_j beta_j (T_j-S_j),
 B_p(x)=sum_(j in I_p) d_j x_j^2
       +2 sum_(j in I_p) beta_j x_j [T_j X_j(x)-Y_j(x)].        (T1)

Equation(C5) gives EXACTLY B_p(x)=x^T Atilde_p x. These are the two genuine
Cauchy/Pearson weighted prefixes, not unweighted HS norms or a bound that
can be differentiated. Their upper limit is the actual degree cut and
all diagonal/top terms are retained.

For any parity-preserving actual matrix W, put Wtilde=U W U. Let c_j and
r_i denote, respectively, its entire jth column and ith row, restricted
to that parity block. Define

 K(W)=sum_p [sum_(j in I_p) B_p(c_j)
                            -sum_(i in I_p) B_p(r_i)],
 L_A(W)=sum_p {sum_(i in I_p) d_i Wtilde_(ii)
       +sum_(i<j in I_p) alpha_i beta_j(T_j-S_i)
                                      (Wtilde_(ij)+Wtilde_(ji))}.

Then the literal complete trace identities are

 tr(Ae[W,W^#])=K(W),
 tr(Ae(W+W^#))=2 L_A(W).                                      (T2)

For the first identity simply expand WW^T as the sum of column squares
and W^T W as the sum of row squares. U is orthogonal, so it preserves the
actual transpose/# and trace. For the second use the symmetry of Atilde.
No commutator sign or lower/upper boundary term has been discarded.
These identities hold for COMPLEX entries as bilinear analytic-square
identities; no conjugate is inserted into B_p.

Apply them to the FULL original finite frame

 Z_lambda=uJ-(m-1/2)I+gamma_lambda(J),       J=d/du=-iD_v,
 gamma_lambda(J)=J/2+sum_(k=1)^(n/2)
                  B_(2k)lambda^(2k-1)J^(2k)/(2k)!,
 n=max EVEN<=m-2,  t=m-n in{2,3},  ell=n-1.                    (T0)

The B_(2k) are the ordinary Bernoulli coefficients of s/(exp(s)-1).
Equivalently gamma=(exp(lambda J)f(lambda J)^(-1)-I)/lambda,
f(s)=(exp(s)-1)/s, with the removable lambda=0. It commutes with parity
after u=-1/2+iv: the J/2 term centers uJ and the remaining terms have even
J powers. Thus this is the actual caller, not an invented surrogate.
For the literal COMMON quantities R=Z+Z^#, tau=(m^4-1)/(24m),

 C(lambda)=2tau tr(Ae[Z,R])-4tau tr(Ae R)
          =2tau K(Z_lambda)-8tau L_A(Z_lambda).                (T3)

This formula includes the complete original Z0 and every finite
Bernoulli/zeta correction and ALL quadratic cross terms: W in (T2) is Z,
not just a selected pole, row, or principal corner. It does not claim the
separate positive rank-two R_leak equals Ae or replace any of its terms.

The raw readout can also be kept literally. Keep the ORIGINAL
Hn=n!sqrt(h_0/h_n), Cxi=Hn/(2pi)^n and Chat=pi^ell Cxi. For lambda!=0,
with u=1/lambda define V_rev(u)=u^ell Z_(1/u)/Cxi and c(u)=Cxi u^(-ell), so
Z_lambda=c(u)V_rev(u). Coefficient# leaves this SAME scalar c(u), without
moving conjugation. Consequently

 C(lambda)=2tau c(u)^2 K(V_rev(u))
                                -8tau c(u)L_A(V_rev(u)).       (T4)

At u=w/pi, c(u)=Chat w^(-ell). This keeps both distinct raw factors; they
are not silently canceled against the leading fullPsi term. The physical
lambda=pi/w here is distinct from the older lens growth parameter z^2/m.

## 7. Finite outcome and the missing quantitative bridge

This round proves the complete actual-m pole evaluations, orthogonal sign
convention, exact rank-two parity cuts, and the full weighted-C prefix
caller. Generic Cauchy polynomial division, residues and finite rank
factorization are classical tools reused explicitly. No standalone general
Tool or new-paper priority claim is attached. The original Student basis
and Ae compression have their real upstream credits; the new bounded
construction above is A alone, not a repair supplied by an earlier reviewer.

The exact prefix reformulation is a different structural input from the
old four shifted-weight moments and positive global rank-two leakage.
It identifies the actual two signed transforms whose ROW-versus-COLUMN
cancellation must be controlled. It supplies no bound for those transforms
on a complex lens. Entrywise positivity from(C6), or taking absolute values
in(T1)-(T3), returns the same kind of unclosed norm loss; (S2) explicitly
blocks a false Ae-positive interpretation.

Thus the finite structural task is complete at author level, while the
quantitative status is HOLD_MISSING_SIGNED_CAUCHY_PREFIX_CONTROL. One
sufficient future target would be a joint bound for the complete normalized
K(V_rev) and its raw/linear corrections relative to the already positive
real L(z), with all coefficients in(T4) retained. This is not a necessary
or exclusive condition and is not proved here. No fullPsi, functional,
binomial coefficient margin,4/5 window, originaltrace/no-go, or original
Goal conclusion follows from this note.

The exploration stops at this interface until a genuine new quantitative
input for these signed actual prefixes is available. It does not reopen
the killed metric route, the old origin-disk/Theta aggregate, allsubset
KILL, signed-probability shortcut, or termwise Ae-HS rebranding. No new
scientific program, numerical integral, solver, sample, matrix/coefficient
generation, external lookup, Native Task, formal authority, Source write,
activity helper, new identity or budget reset was used. Current same warm
execution49/176; cumulative formal/product/session budgets UNKNOWN.
Parent Goal OPEN.
