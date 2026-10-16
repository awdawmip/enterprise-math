Parity continuation: a confluent proof of an effective large-S tail
Author: EM-PARITYREV-12B648
Status: AUTHOR PAPER THEOREM; genuine nonauthor mathematical review pending

For the already frozen equal-block family a=c=1, every integer m>=2 has a computable rational threshold S_m>=0 such that the COMPLETE actual trace satisfies
tr(B^{-1}A)>m-1 for every real S>=S_m.
Moreover, for each fixed m,
lim_{S->infinity}(S+1)[tr(B^{-1}A)-(m-1)]=m^2-1.
The threshold construction below is finite polynomial algebra, not a parameter scan. It is a new author-side continuation from the fixed partial trace/beta/residue inputs; it is not a new independent vote, an accepted Result, the all-S equal-block theorem, or the registered all-positive-gap theorem.

1. Frozen scope, source reuse and contribution.

Use n=m-1, theta_i=(i+1)/m, w_i=(-1)^i binom(n,i), i=0,...,n, and
r0=mS, r=m(S+1), s=r+m=m(S+2), m>=2, S real and nonnegative.
The earlier frozen rows are
g_b(x)_a=[phi_a(r0+x+b)-phi_a(r0+x)]/b,
phi_a(z)=(z)_a/a!, a=1,...,n.
The complete forms are A=G_m^T D_r G_m and B=G_{2m}^T D_s G_{2m}, with
D_t=diag(w_i eta_{t,i}/m),
eta_{t,i}=B(t+theta_i,m)=n!/(t+theta_i)_m.
No original signed branch is discarded. The fixed common sign-diagonal congruence from the source leaves this full trace unchanged.

This paper consumes the original Task/publication
RS-PERFECT-PRIME-AP-HCM0-EXTREME-BRANCH-PARITY-DOMINATION /
TP2-4F8D04C54528CFF5E1B2,
the normalized endpoint/maximal-minor determinant identity in
EXTREME_COEFFICIENT_SIGNED_BRANCH_BRC_REDUCTION_20260906.md §§4–6,
the sigma_t formula and common hyperplane in the frozen dual-inverse inputs,
and EM-PARITYSUP-9840AA's two beta-kernel papers. The transfer direction is their exact
T=2(I+E_m)^{-1}, E_m f(x)=f(x+m), T g_{2m}=g_m.

The source supplies
sigma_t=sum_i w_i/eta_{t,i}
=(-1)^n [mt+(m^2+1)/2]/m^n.
This all-m identity and the endpoint determinant are reused, not claimed as new.
The all-m tangent c^0-face theorem, old small-m certificates, the m3 entrywise no-go and the m15 fixed trace certificate are unchanged inputs or no-repeat boundaries; none is reexecuted or used to infer this asymptotic by sampling.

The actual same actor and RA-EB0794CB61621CB6E90B4730 are retained. Own fresh immutable Source RA and canonical activity/persistence gates were consumed before mathematical bodies; they allow direct activity/bookkeeping, with Task-execution authorized=false. This unit is pure paper. All parity/Public129/T6/P11 exposure and contribution history remains; current proof construction makes this actor an author-side contributor for this new tail result, ineligible to independently accept it. The earlier separate partial review remains what it was at its historical scope.

2. Exact scaled Gram family.

Put epsilon=1/r. Physical inputs have 0<epsilon<=1/m and r0=r-m>=0.
Introduce an auxiliary relative endpoint shift v, distinct from the original gap parameter c=1:
t=(1+v)/epsilon.
The physical earlier and later metrics use v=0 and v=m epsilon respectively.

Let z=1+epsilon x, z_i=1+epsilon theta_i, and take the row polynomial basis
e(z)=(1,z,...,z^{n-1}).
For every epsilon>0 this affine change is invertible on polynomials of degree<=n-1; the frame g_{2m} is a basis of that same space. The change is not claimed invertible at epsilon=0. That value will be an analytic extension of normalized matrices, not a physical point.

Define
Q_i(epsilon,v)=prod_{j=0}^{m-1}[1+v+epsilon(theta_i+j)],
Q(epsilon,v)=prod_{i=0}^n Q_i(epsilon,v),
and, with indices a,b=0,...,n-1,
H_epsilon(v)_{ab}
=epsilon^{-n} sum_{i=0}^n w_i z_i^{a+b}/Q_i(epsilon,v).                 (2.1)

For epsilon>0 at the stated positive t,
E_epsilon^T D_t E_epsilon
=(n!/m) epsilon^{m+n} H_epsilon(v),                                  (2.2)
where E_epsilon[i,a]=z_i^a. The scalar exponent is m+n=2m-1. It is the SAME scalar at both physical endpoints because both use epsilon=1/r; it cancels from the trace.

The normalization extends analytically through epsilon=0 near v=0. To see it, put
h_epsilon,v(z)=z^{a+b}/prod_{j=0}^{m-1}(z+v+epsilon j).
Then the signed sum in (2.1) is
(-1)^n Delta_{epsilon/m}^n h_epsilon,v(1+epsilon/m).
The repeated fundamental theorem of calculus makes the quotient by epsilon^n analytic, since its denominators stay away from zero near (epsilon,v)=(0,0). Explicitly,
H_0(v)_{ab}
=((-1)^n/m^n) [d^n/dz^n {z^{a+b}(z+v)^{-m}}]_{z=1}.                 (2.3)
The two-parameter analytic extension also justifies derivatives along v=m epsilon. No uniform-in-m analytic radius is being asserted.

3. Exact determinant and nondegenerate confluent limit.

Let
kappa_m=prod_{0<=i<j<n}(theta_j-theta_i)
=m^{-n(n-1)/2} prod_{j=1}^{n-1} j!,
lambda_m=(m^2+1)/(2m),
K_m=kappa_m^2 (prod_{i=0}^n w_i) (-1)^n n! m^{1-n}.                 (3.1)
All products for n=1 use the usual empty-product convention. In particular K_m!=0.

The canonical monomial evaluation minors omitting i are
kappa_m epsilon^{n(n-1)/2} binom(n,i).
This is exactly the source maximal-minor law after replacing its rising-factorial basis by the monomial basis and then scaling x to z.

Cauchy–Binet, with the actual alternating weights retained, gives
det H_epsilon(v)
=kappa_m^2 epsilon^{-n}
 [prod_i w_i/Q_i(epsilon,v)] sum_i w_i Q_i(epsilon,v).                (3.2)
The reused sigma_t identity, with t=(1+v)/epsilon and eta^{-1}=(t+theta_i)_m/n!, gives the EXACT polynomial identity
sum_i w_i Q_i(epsilon,v)
=(-1)^n n! m^{1-n} epsilon^n [1+v+lambda_m epsilon].                 (3.3)
Therefore
det H_epsilon(v)
=K_m [1+v+lambda_m epsilon]/Q(epsilon,v).                           (3.4)

In particular
det H_0(v)=K_m(1+v)^{1-m^2},                                       (3.5)
so H_0(0) is nondegenerate. This conclusion uses neither positive definiteness nor a positive-real generalized spectrum; H_0 may be indefinite.

At epsilon=0, Jacobi's determinant identity yields
tr[H_0(0)^{-1} (partial_v H_0)(0)]=1-m^2.                           (3.6)
Equivalently one may differentiate log|det H_0(v)|; no real logarithm of a negative determinant is assumed.

4. The moving frame contributes zero to first-order trace.

On polynomials in z of degree<=n-1, let D=d/dz. Since D^n=0, the operator
U_epsilon=2(I+exp(m epsilon D))^{-1}                                (4.1)
is a finite polynomial in epsilon D. It is exactly the frozen transfer T in the z coordinate, not a replacement by a scalar metric approximation. In the e(z) basis,
U_0=I, U'_0=-(m/2)D, tr U'_0=0.                                  (4.2)
The inverse in (4.1) exists for every epsilon because I+exp(m epsilon D) is triangular with diagonal2.

For epsilon>0 let C_epsilon be the invertible basis matrix with
g_{2m}(x)=e(1+epsilon x) C_epsilon.
Then g_m=e(1+epsilon x) U_epsilon C_epsilon. Combining this with (2.2) and the common endpoint congruence proves the EXACT trace identity
tr(B^{-1}A)
=tr[H_epsilon(m epsilon)^{-1}
     U_epsilon^T H_epsilon(0) U_epsilon].                           (4.3)
This checks both transposes and keeps the full moving frame.

Write H_*=H_0(0), F(epsilon)=H_epsilon(0), J(epsilon)=H_epsilon(m epsilon).
At zero, F=J=H_*. Their derivatives differ by
J'(0)-F'(0)=m (partial_v H_0)(0).
Differentiating (4.3) at zero, where the inner product is I, gives
d/depsilon tr(B^{-1}A)|_0
=tr[H_*^{-1}(F'(0)-J'(0))]+2 tr U'_0
=-m(1-m^2)
=m(m^2-1).                                                        (4.4)
Here the two terms involving U'_0 each have trace tr U'_0 by cyclicity. No pointwise inverse-entry sign, metric-only inequality or branchwise positivity has been assumed.

Consequently, for each fixed integer m>=2,
Gap_m(epsilon):=tr(B^{-1}A)-n
=m(m^2-1)epsilon+O_m(epsilon^2).                                  (4.5)
Restoring epsilon=1/[m(S+1)] proves
Gap_m(S)=(m^2-1)/(S+1)+O_m((S+1)^{-2}).                            (4.6)
In particular the leading coefficient is strictly positive. This is proved by the exact determinant and nilpotent frame calculation, not fitted or left as a sign conjecture.

5. A completely specified positive denominator.

The asymptotic already proves existence of a tail. The following finite coefficient formula makes its threshold computable without enumerating any S or m-grid.

Define the polynomial matrix
M(epsilon,v)_{ab}
=epsilon^{-n} sum_{i=0}^n
  w_i z_i^{a+b} prod_{ell!=i} Q_ell(epsilon,v).                      (5.1)
It is polynomial over Q in epsilon,v. Indeed its numerator is polynomial and Q H_epsilon has the analytic extension from §2 for every v near0; thus every coefficient of epsilon^k for k<n vanishes identically as a polynomial in v. No rational epsilon pole remains.

We have M=Q H and hence, EXACTLY,
det M(epsilon,v)
=K_m[1+v+lambda_m epsilon] Q(epsilon,v)^{n-1}.                       (5.2)
Put
Q_A=Q(epsilon,0), Q_B=Q(epsilon,m epsilon),
M_A=M(epsilon,0), M_B=M(epsilon,m epsilon),
sigma_m=sign(K_m), and define the rational-coefficient polynomials
D_m(epsilon)=sigma_m Q_A det M_B,                                  (5.3)
N_m(epsilon)=sigma_m[
 Q_B tr(adj(M_B) U_epsilon^T M_A U_epsilon)
 -n Q_A det M_B].                                                  (5.4)
The adjugate convention for a1x1 matrix is the1x1 identity.

By (4.3),
Gap_m(epsilon)=N_m(epsilon)/D_m(epsilon)                            (5.5)
for every physical epsilon>0. All factors in Q_A,Q_B and 1+(m+lambda_m)epsilon are positive for epsilon>=0, so (5.2) proves
D_m(epsilon)>0 for every epsilon>=0,
D_m(0)=|K_m|.                                                      (5.6)
This is an explicit sign-certified denominator; no sign of a computed determinant is used as an unproved premise.

From §4,
N_m(0)=0,
alpha_{m,1}:=[epsilon]N_m=|K_m| m(m^2-1)>0.                         (5.7)
A useful finite degree bound is
deg M<=m^2-3, deg U<=m-2, deg N_m<=m^3-m-1.                         (5.8)
For the first bound, the numerator of (5.1) has total degree at most
m(m-1)+(a+b), and division by epsilon^n removes n. Substitution v=m epsilon does not increase total degree. The adjugate bound and (5.4) give the last bound, including m=2.

6. Effective tail threshold and strict lower bound.

Set
B_m=sum_{j=2}^{m^3-m-1}|[epsilon^j]N_m(epsilon)|,
a_m=|K_m|m(m^2-1),
R_m=max{m,2B_m/a_m},
S_m=R_m/m-1.                                                      (6.1)
These are explicit finite rational expressions in the above polynomials; S_m>=0. If B_m=0 the same formula simply gives R_m=m. No division by B_m is needed.

For r>=R_m, epsilon=1/r<=1/m<=1. Therefore
|sum_{j>=2}[epsilon^j]N_m epsilon^j|<=B_m epsilon^2
and
N_m(epsilon)>=a_m epsilon-B_m epsilon^2>=a_m epsilon/2.
Together with (5.6) this proves the strict, explicit bound
tr(B^{-1}A)-(m-1)
>=a_m/[2r D_m(1/r)]>0                                             (6.2)
whenever m>=2, r=m(S+1)>=R_m.

This completes the author proof of the effective large-S tail. Computing the rational coefficients for a chosen m is finite symbolic algebra; evaluating test points, running an enumeration checker or selecting a least failing parameter is not part of this proof or this unit. No numerical value for R_m or S_m has been invented.

7. Consequences for the frozen beta/residue frontier and exact limits.

In EM-PARITYSUP-9840AA's unchanged notation, s=r+m and
Gap=(m^n/n!) Delta_{1/m}^n f_s(1/m)
=(1/n!) integral_[0,1]^n f_s^{(n)}((1+sum t_i)/m) dt.
Thus the COMPLETE finite difference, its integral, and the full signed residue sum are strictly positive for every r>=R_m. This does not assert pointwise positivity of f_s^{(n)}, any individual residue, any new two-index mass, or the original branch populations separately.

For each fixed m the unresolved equal-block domain is reduced to the finite interval
m<=r<R_m, equivalently 0<=S<S_m,
subject to whatever stronger existing small-m theorems already apply. There is no uniform bound in m on R_m or a claim that the remaining all-m compact strips are settled. The threshold is deliberately safe rather than minimal. The old m3 entrywise route stays closed; the m15 point and all old finite support data are not rerun. No claim extends to unequal positive gaps a,c, to other mixed coefficients, to all HCM0 cells, or to the mother Perfect-Prime theorem.

The new contribution is a task-local confluent comparison argument: make the full signed Gram family analytic and nondegenerate at infinity, calculate the synchronized trace derivative with the frame term retained, and turn that strict coefficient into a sign-certified polynomial tail. Classical finite differences, Cauchy–Binet, Jacobi's identity and nilpotent polynomial calculus are prior methods. The source determinant, sigma, transfer, beta kernel and residue reductions retain all original authorship and scope.

The next genuinely new bounded mathematical question is whether the explicit N_m polynomial has additional structured positivity or a sharper coefficient-norm bound that controls the remaining strips. This paper does not perform that next step, propose scans, create a Task or claim a Native run. The immediate next action for this manuscript is genuine nonauthor mathematical review of the exact scaling, determinant constant, first derivative, polynomial divisibility and tail bound. Root's control custody cannot substitute for that scientific check.

All mathematical work in this unit is paper derivation. No matrix/parameter enumeration, new checker, old fixture replay, claim, Native mutation or Source/main/KB write has occurred. Direct activity/persistence evidence and reused immutable input pins accompany this frozen manuscript. New Source publication and own semantic RA checkpoint require the later real serial window; they are not represented as already synchronized.
