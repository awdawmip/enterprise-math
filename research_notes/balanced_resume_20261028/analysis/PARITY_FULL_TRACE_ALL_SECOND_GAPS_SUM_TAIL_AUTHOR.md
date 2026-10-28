# Full Parity trace: an effective sum tail uniform over every second gap

Author: EM-ANALYSIS-1E507F; RA-9C879FA5E6538D45DD9AE10F.
Status: NEW_AUTHOR_PAPER_CANDIDATE_AWAITING_DISTINCT_REVIEW. 2026-10-28.

## 1. The stronger theorem and exact unresolved boundary

For each fixed integer m>=2 there is a computable rational R_m>=1,
independent of a,c,S, such that the ORIGINAL complete normalized secant trace
satisfies

    Gap(S,a,c)=tr(B^(-1)A)-(m-1)
      >= (m-1)/4 * [(1+c/(S+a))^(m+1)-1]
      >= (m^2-1)c/[4(S+a)] >0                            (1)

for ALL real

    S>=0, a>0, c>0, S+a>=R_m/m.                        (2)

There is no upper bound on the relative second gap c/(S+a), and no positive
lower bound on either gap. This advances the previous bounded-relative-gap
tail by removing its C parameter entirely. It still does not cover the
compact total-scale region S+a<R_m/m, does not give a threshold uniform
in m, and does not establish coefficientwise P1/higher-face positivity or
the complete mother objective.

This is direct source-exposed research, not formal Task execution/takeover,
Result/Driver acceptance, Working Truth, Foundation or new tool-family
admission. No scientific program, numerical matrix/parameter scan, symbolic
package or stopped P11/m7 certificate was executed. The native basis remains
Heartbeat World's signed six-axis Cell torsor, no native plane, with time
separately typed when relevant. The present forms and parameters are
explicit external classical algebra; no native/physical inference is added.

## 2. Complete normalization and exact inputs

Put n=m-1, r0=mS, L=ma, N=m(a+c), r=m(S+a), s=r+mc,
epsilon=1/r, lambda=L/r in(0,1], nu=mc/r>0, v=1+nu and
lambda'=(lambda+nu)/v. For i=0,...,n put

    theta_i=(i+1)/m, w_i=(-1)^i binom(n,i),
    D_r[i,i]=(n!/m) w_i / product_(h=0)^(m-1)(r+theta_i+h).

With phi_j(x)=(x)_j/j!, 1<=j<=n, rising factorials, define

    G_b[i,j]=[phi_j(r0+theta_i+b)-phi_j(r0+theta_i)]/b,
    A=G_L^T D_r G_L, B=G_N^T D_s G_N.

No signs, branches, secant frames or normalization factors are dropped.
The exact formulas are from the complete unequal-gap source, read at
1a553d4d28a105230ecebd5a555dc8adbab8ee28:

`research_notes/owner_goal_20261016/parity_tail_independent_review/PARITY_UNEQUAL_GAPS_UNIFORM_BOUNDED_SECTOR_TAIL_AUTHOR.md`,
blob f05b0b5be5c7d78c7faf58ae1f818bc67cea103c,
author EM-PERFECT-9821E2.

The analytic centered metric and its limiting parity signature are reused
from EM-DVR-BFF6DC's metric proof in
`research_notes/owner_goal_20261016/p11_independent_native_driver/parity_all_m_c1_uniform_sum_tail_addendum_v2_author/PARITY_ALL_M_C1_POSITIVE_TOP_HOMOGENEOUS_FACE_AND_UNIFORM_SUM_TAIL_AUTHOR_V2.md`,
same commit, blob c94088a17f4a09dd2d16171162c09ed13807a8bf. The original
scalar-boundary contribution is attributed there to EM-DVR-F73673.

This author's immediately preceding full-trace bounded-relative-gap theorem
is an explicit mathematical dependency:
`PARITY_FULL_TRACE_BOUNDED_RELATIVE_GAP_TAIL_AUTHOR.md`,
SHA256 129cad117292b1e90f3f0f8eb6c2791c2e5a050adff386c9e4a0b4c6e0d55c5e.
Its distinct paper review checks that stronger full-trace scope; neither its
vote nor the older c1 vote automatically reviews the new uniform perturbation
argument here. Only its proved C=1 case will be needed below.

## 3. Exact common-centered pair and positive reference forms

Let J be differentiation on polynomials of degree<=n-1, with J^n=0. Define

    E_z=sum_(2h<n) (zJ/2)^(2h)/(2h+1)!,
    D_v=diag(v^(j-m+1/2)), 0<=j<=n-1.

The exact same-input-center derivation in the preceding paper uses
F_L=exp(LJ/2)E_L and the COMMON input basis (theta+r0/2)^j. It gives

    A_* = E_lambda^T M(epsilon) E_lambda,
    B_* = D_v E_lambda'^T M(epsilon/v) E_lambda' D_v,
    tr(B^(-1)A)=tr(B_*^(-1)A_*).                          (3)

Here M(epsilon) is a real symmetric analytic matrix germ at epsilon=0,
independent of lambda, and M0=M(0) is block diagonal in even/odd degree:
its even block is positive definite and its odd block negative definite.
All E_z are unipotent even polynomials in J, so they preserve these blocks;
D_v preserves them as well. No such parity block decomposition is asserted
for M(epsilon) at positive epsilon.

Let Sigma be +I on the even block and -I on the odd block. Then

    Sigma^2=I, Sigma^T=Sigma,
    P=Sigma M0=M0 Sigma >0.

For the given lambda,nu set the positive reference forms

    P_A=E_lambda^T P E_lambda,
    V_B=E_lambda' D_v,
    P_B=V_B^T P V_B.

Both commute with Sigma. The limiting signed forms are

    A0=Sigma P_A, B0=Sigma P_B.

Write T0=tr(B0^(-1)A0). The preceding paper's full limiting comparison,
or its same positive-block argument, gives

    T0 >= n(1+nu)^(m+1).                                  (4)

Its determinant input is det A0/det B0=(1+nu)^(m^2-1).
This bound holds for EVERY nu>=0, not merely a bounded interval.

## 4. An effective metric error bound independent of the gap ratios

The centered metric can be written directly in the same normalization as (3):

    M(epsilon)[j,k]=(n!/m) epsilon^(-n)
        sum_(i=0)^n w_i (epsilon theta_i+1/2)^(j+k)
           /Q_i(epsilon),
    Q_i(epsilon)=product_(h=0)^(m-1)[1+epsilon(theta_i+h)],
    Q(epsilon)=product_i Q_i(epsilon)>=1 for epsilon>=0.     (5)

Indeed Q_r in the monomial theta basis has the inherited factorization
C_r A_r C_r, C_r[j,j]=r^(j-m+1/2). Translating the output basis to
(theta+r/2)^j gives exactly (5). Its limiting matrix is the same M0.

Let W(epsilon)=Q(epsilon)M(epsilon). Finite-difference divisibility in the
metric proof makes W a rational-coefficient polynomial matrix despite the
displayed epsilon^(-n): the lower epsilon coefficients vanish. Since
Q(0)=1, W(0)=M0. Therefore

    V(epsilon)=[W(epsilon)-M0 Q(epsilon)]/epsilon

is a polynomial matrix. It is symmetric. If V=sum_l V_l epsilon^l, define

    E=sum_l |V_l|                 (entrywise absolute values),
    k_m=||P^(-1)||_infinity ||E||_infinity,
    Rpert_m=max(1,5 k_m).                                    (6)

All coefficients and constants in (5)-(6) are explicit rational finite
algebra. P is positive definite by the inherited parity Gram proof, so its
inverse exists. No spectral infimum or unknown optimization is hidden in
this recipe. No numerical value is evaluated here.

For 0<=epsilon<=1,

    |M(epsilon)-M0| <= epsilon E,
    ||P^(-1/2)[M(epsilon)-M0]P^(-1/2)||_2 <= k_m epsilon.     (7)

The first inequality uses Q>=1 and epsilon^l<=1. For the second,
||P^(-1/2)||_2^2=||P^(-1)||_2<=||P^(-1)||_infinity and
||M(epsilon)-M0||_2<=||M(epsilon)-M0||_infinity
<=epsilon||E||_infinity; these spectral/infinity comparisons apply because
the matrices are real symmetric. Although E uses absolute values, the
actual signed perturbation remains intact in (7).

In particular if epsilon<=1/Rpert_m, both endpoint errors, at epsilon and
epsilon/v, have relative norm at most eta:=k_m epsilon<=1/5. This bound
is independent of nu>=0 because v>=1. Congruence by E_lambda and V_B
preserves the corresponding two-sided quadratic inequalities. Thus there
exist real symmetric R_A,R_B with ||R_A||_2,||R_B||_2<=eta such that

    A_*=P_A^(1/2)(Sigma+R_A)P_A^(1/2),
    B_*=P_B^(1/2)(Sigma+R_B)P_B^(1/2).                     (8)

For example this follows from -eta P <= M(epsilon)-M0 <= eta P
in the Loewner order, followed by congruence. It makes NO assertion that
Sigma+R_A or Sigma+R_B is positive definite. Their cross-parity blocks are
included in R_A,R_B.

## 5. A relative TRACE perturbation bound for indefinite forms

Put C_*=P_B^(-1/2)P_A^(1/2). Since both positive reference forms commute
with Sigma, their square roots and inverses do too; hence C_* Sigma=Sigma C_*.
From (8), cyclicity of trace gives

    T:=tr(B_*^(-1)A_*)
      =tr[(Sigma+R_B)^(-1) C_* (Sigma+R_A) C_*^T].          (9)

Also

    T0=tr[Sigma C_* Sigma C_*^T]
       =tr(C_*C_*^T)=||C_*||_F^2.                          (10)

For eta<1, the inverse in (9) exists, and

    H_B:=(Sigma+R_B)^(-1)-Sigma,
    ||H_B||_2 <= eta/(1-eta).                              (11)

To see (11), factor Sigma+R_B=Sigma(I+Sigma R_B), use the Neumann bound,
and ||Sigma||_2=1. The exact inverse difference is not being replaced by a
positive matrix. H_B is symmetric because both inverse and Sigma are.

Expanding (9) around (10) and using trace/nuclear-norm bounds gives

    |T-T0| <= [eta + eta(1+eta)/(1-eta)] ||C_*||_F^2
            = [2eta/(1-eta)] T0.                           (12)

For completeness, the three error terms are

    tr[Sigma C_* R_A C_*^T],
    tr[H_B C_* Sigma C_*^T],
    tr[H_B C_* R_A C_*^T].

Their magnitudes are bounded respectively by eta||C_*||_F^2,
||H_B||_2||C_*||_F^2, and ||H_B||_2 eta||C_*||_F^2.
One may use ||C_* X C_*^T||_*<=||X||_2||C_*||_F^2 and
|tr(YZ)|<=||Y||_2||Z||_*; the middle term also follows directly from
||Sigma||_2=1. These estimates include arbitrary cross-parity perturbations.

For eta<=1/5, 2eta/(1-eta)<=1/2. Therefore

    T >= (1/2)T0 >= (n/2)(1+nu)^(m+1)                    (13)

uniformly over ALL lambda in [0,1] and nu>=0. The uniform relative bound
is essential: an additive O(epsilon) estimate with a constant growing with
nu would not remove the bounded-C restriction.

## 6. Join the genuinely different small-nu and large-nu controls

For nu>=1, (13) yields

    Gap=T-n >= (n/2)(1+nu)^(m+1)-n
             >= (n/4)[(1+nu)^(m+1)-1].                    (14)

The last inequality is equivalent to (1+nu)^(m+1)>=3; here it is at
least 2^3=8 because m>=2. The relative trace estimate alone would not
give positivity uniformly as nu tends to zero.

For 0<nu<=1, consume the preceding paper's effective C=1 threshold
Rbounded_m(1)>=1. Its exact nu-factor argument proves

    Gap >= (n/2)[(1+nu)^(m+1)-1]

whenever r=m(S+a)>=Rbounded_m(1). Define

    R_m=max(Rpert_m,Rbounded_m(1)).                         (15)

Both constants are computable rational finite coefficient expressions.
Combining the two complementary regions proves (1)-(2). The endpoint
nu=1 belongs to both and causes no gap. Bernoulli's inequality gives the
second lower bound in (1).

## 7. Reuse, scope integrity and stopping rule

Coverage lookup was run before developing the perturbation argument.
Resolution: COMPOSE_APPLIED to the existing centered metric/secant interface,
standard congruence, Neumann inverse and trace-norm inequalities. Lexical
tool suggestions concerning positive support do not apply to these signed
forms; no such support-compression tool was invoked. There is no new global
T family or claim of external historical novelty.

The mathematical advance is the relative bound (12), uniform in an
unbounded scale ratio, and its use with the exact small-nu theorem. A large
second-gap multiplier is kept inside the positive reference Frobenius norm
rather than hidden in an uncontrolled error constant. No signed information
or cross-parity error has been erased.

The first-round small cone and second-round bounded-relative domains are
retained as provenance and proof dependencies; after integration their nested
domains should not be counted as independent discoveries. The final usable
frontier is one all-second-gaps effective total-scale tail.

The remaining compact-total-scale problem is genuine and not paid by this
tail. Do not automatically derive further constant variants or manufacture
new formal Tasks after a review PASS. A distinct review must first check
the exact metric numerator/divisibility, signature-reference congruence,
commutation of C_* with Sigma, trace error norm estimates and the two-region
join. Accepted earlier scopes do not review this new one.
