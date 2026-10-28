# Complete outer Cauchy determinant: an effective first-endpoint interval

Author: EM-ANALYSIS-1E507F; RA-9C879FA5E6538D45DD9AE10F.
Status: AUTHOR_DERIVED_INTERFACE_AWAITING_DISTINCT_REVIEW. 2026-10-28.

This is a quantitative corollary of the accepted all-m crossing form and
complete outer signed-covariance reduction. It does not claim a new global
nonvanishing theorem, formal Task execution or takeover, Driver vote,
Working Truth, Foundation change or new tool family. P11 core98/fixed233
and the m7 fixed-certificate NO_INVOKE boundaries are untouched; zero
scientific programs are executed for this paper unit.

The exact source is
`research_returns/PERFECT_PRIME_AP_BINOMIAL_CAUCHY_LAYER_COFACTOR_POSITIVITY_RETURN_20260901.md`,
read at 1a553d4d28a105230ecebd5a555dc8adbab8ee28, blob
340a17c17156e633f0c107023507ceb5498a3763. Its later Task-only accepted
negative-boundary status is recorded by the month library; the whole outer
determinant problem remains open. The source gives nondegeneracy of the first
crossing form and its asymptotic order, but no explicit rational endpoint
radius. This note supplies that radius without requiring positive-definite
inner blocks or fresh finite-m coefficient scans.

The model is external classical real Cauchy/moment algebra. Native Heartbeat
World remains a six-axis signed Cell torsor with no native plane; no spatial
or physical interpretation is added to the external parameter t.

## 1. Frozen complete outer matrix

Fix m>=2, n=m-1, b=m^2, y_j=mj and w_j=(-1)^j binom(n,j), 0<=j<=n.
For 0<=s<=n put

    z_(j,s)=y_j+bs,
    c_(j,s)=n!/product_(r=1)^m(z_(j,s)+r)>0,
    a_(j,s)=(-1)^s binom(n,s)c_(j,s),
    lambda_(j,s)(t)=a_(j,s)t^s,
    d_j(t)=sum_s a_(j,s)t^s.

On the degree-1-through-n monomial basis define

    C_j(t)[p,q]=sum_s lambda_(j,s) z_(j,s)^(p+q)
       -(sum_s lambda_(j,s)z_(j,s)^p)
        (sum_s lambda_(j,s)z_(j,s)^q)/d_j(t),
    S(t)=sum_j w_j C_j(t), 1<=p,q<=n.

The inherited integral gives

    d_j(t)=integral_0^1 u^(mj)(1-u)^n(1-t u^b)^n du,
    d_j(t)>=delta_j:=d_j(1)>0, 0<=t<=1.                     (D)

The inequality follows directly from the nonnegative integrand, pointwise
decreasing in t. The endpoint integral is strictly positive in 0<u<1.
All d_j coefficients, delta_j and matrices used below are rational.

## 2. Cancel the forced t factor before perturbation

For r<s let v_(j,r,s) be the column vector with p-th entry
z_(j,s)^p-z_(j,r)^p, 1<=p<=n. Algebraic expansion of the covariance gives

    d_j(t) C_j(t)=sum_(0<=r<s<=n)
          lambda_(j,r)(t) lambda_(j,s)(t)
          v_(j,r,s) v_(j,r,s)^T.

The smallest pair exponent r+s is 1, uniquely at (r,s)=(0,1). Thus

    U_j(t)=sum_(r<s) a_(j,r)a_(j,s)t^(r+s-1) v_(j,r,s)v_(j,r,s)^T

is polynomial and C_j(t)=t U_j(t)/d_j(t), including by continuity at t=0.
Define the normalized complete matrix

    A(t)=sum_j w_j U_j(t)/d_j(t), so S(t)=t A(t).

Its endpoint is the exact source crossing form

    A0=A(0)=-n sum_j w_j c_(j,1) v_(j,0,1)v_(j,0,1)^T.

The accepted all-m crossing theorem reused in the source states det A0!=0.
This is an explicit inherited mathematical premise. The present argument
does not attempt to reprove that theorem or to infer it from inner inertia.

## 3. Fully explicit matrix majorant

Write |X| for entrywise absolute value, and define the nonnegative matrices
and scalars

    R_j=sum_(r<s,r+s>=2) |a_(j,r)a_(j,s)|
                            |v_(j,r,s)v_(j,r,s)^T|,
    L_j=sum_(s=1)^n |a_(j,s)|,
    E=sum_j |w_j| [R_j/delta_j
                    + |U_j(0)| L_j/(delta_j c_(j,0))].

For every 0<=t<=1,

    |U_j(t)-U_j(0)|<=t R_j,
    |d_j(t)-c_(j,0)|<=t L_j,
    |A(t)-A0|<=t E                                             (M)

entrywise. The first two inequalities use t^ell<=t for integers ell>=1.
For the third, use the exact difference

    U_j(t)/d_j(t)-U_j(0)/c_(j,0)
       =[U_j(t)-U_j(0)]/d_j(t)
        +U_j(0)[c_(j,0)-d_j(t)]/[d_j(t)c_(j,0)],

then (D) and the triangle inequality. No signed covariance is replaced by
a probability variance, and no positive-definite matrix inequality is used.
The absolute values appear only in an explicitly conservative perturbation
bound around the full retained signed matrix A0.

For a matrix X let ||X||_infinity=max_p sum_q |X[p,q]|. Set

    K_m=||A0^(-1)||_infinity ||E||_infinity,
    eta_m=1 if K_m=0, otherwise min(1,1/(2K_m)).

These are computable rational constants depending only on m. The inverse
is well-defined by the inherited crossing theorem and can be expressed by
adj(A0)/det(A0); this is a finite exact recipe, not a claim of cheap or
already executed evaluation.

## 4. Quantitative endpoint theorem

For every fixed m>=2 and every 0<t<=eta_m,

    det S(t)!=0,
    sign(det S(t))=sign(det A0),
    |det S(t)|>=2^(-n)|det A0|t^n.                            (N)

Proof. By (M) and submultiplicativity,

    ||A0^(-1)(A(t)-A0)||_infinity<=t K_m<=1/2.

Thus A(t)=A0(I+F(t)) with every eigenvalue of F(t) of complex modulus at
most 1/2. No eigenvalue of I+F(t) vanishes, and
|det(I+F(t))|=product_i|1+lambda_i(F(t))|>=2^(-n), counting algebraic
multiplicity even if F(t) is not diagonalizable. This proves nonsingularity
and the lower bound. Since A(t) is a continuous real matrix on [0,eta_m]
with no singular point, its determinant has the constant sign of det A0.
Finally S=tA and t>0. QED.

The exact inherited cofactor relation is

    tau_m(t)=[product_j w_j d_j(t)] det S(t) / V_m^2,
    V_m=product_(k=1)^n k!.

Consequently the same interval gives the explicit bound

    |tau_m(t)| >= [product_j |w_j|delta_j]
                  |det A0| t^n / [2^n V_m^2] >0.             (T)

This preserves the original right-node convention: there is no additional
V_y determinant factor. It supplies an effective first-endpoint collar for
every m, not an m-uniform radius and not the remaining interval eta_m<t<=1.
If eta_m=1 happened for a particular exact input, the theorem would cover
that entire input interval; no such evaluated case is claimed here.

## 5. Reuse and next discriminating question

Tool coverage and the exact source/month-library boundaries were consulted.
Resolution: COMPOSE_APPLIED. The existing complete covariance reduction and
crossing theorem are combined with elementary rational coefficient bounds
and the standard matrix Neumann criterion. This is a domain-specific
quantitative interface extraction, not a new generic tool or novelty claim.
The scoped source search found no explicit rational collar in that return;
it is not an exhaustive claim about external or other private work.

The all-m nonvanishing question still requires control of the compact
remainder for each m or a stronger structural argument. In particular, the
old m<=10 positive-coefficient evidence is not rerun or promoted to all m,
and inner indefiniteness remains compatible with this outer collar.

An independent reviewer should verify the pair-covariance factor (no 1/2
for unordered r<s), the forced t cancellation, monotone lower denominator,
the precise A0 crossing input, matrix norm direction, and determinant bound
for possibly nondiagonalizable nonsymmetric A0^(-1)A(t). No actual matrix
coefficient scan or current formal successor execution is required to check
this finite symbolic proof.
