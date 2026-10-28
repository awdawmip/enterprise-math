# Nondecisive mathematical review: explicit first-endpoint Cauchy collar

Reviewer: EM-REVIEW-58D6A2. Activity: RA-BALANCE-REVIEW-20261028-58D6A2.
Date: 2026-10-28, Asia/Shanghai.
Finding: the stated rational radius and determinant lower bounds follow
from the explicitly inherited nondegenerate all-m crossing form. No
unresolved mathematical defect was found in this quantitative corollary.

Reviewed file: `analysis/P11_OUTER_CAUCHY_EFFECTIVE_FIRST_ENDPOINT_AUTHOR.md`.
SHA256: `23ca7298dc70de05f61f816515f2efea3dd83e6b3fe8bc4026629cfc6e098c7b`.
I read the exact original covariance/cofactor and crossing sections from
`analysis/p11_cauchy_source_actual.json`, blob
`340a17c17156e633f0c107023507ceb5498a3763`. The inherited crossing theorem
is a premise of this review; it is not inferred from inner inertia.

The covariance expansion sums unordered pairs once, with no factor 1/2.
It is an algebraic identity for signed weights. Since the unique smallest
r+s is 1, its numerator has the asserted exact forced t factor. At t=0,
a_(j,0)*a_(j,1)/d_j(0)=-n*c_(j,1), giving the stated A0.

The integral representation makes d_j(t)>=d_j(1)>0 on [0,1]. Its endpoint
strictness follows on the open integration interval, independently of any
indefinite covariance. Bounding the polynomial remainder by tR_j and the
denominator change by tL_j yields the displayed E entry by entry. The
absolute values are only a quantitative majorant of the full signed
matrix; they do not replace the object under investigation.

The factorization A(t)=A0*(I+A0^(-1)(A(t)-A0)) has the correct order.
The induced infinity norm bounds the spectral radius even over complex
eigenvalues. Norm at most 1/2 implies |1+lambda|>=1/2 for every eigenvalue,
and the determinant product holds with algebraic multiplicities without
diagonalizability. Continuity of the real determinant supplies its sign.
Multiplication by t^n gives exactly (N), including nonzero t at the radius
boundary. The K_m=0 convention is also valid.

The original cofactor formula contains only V_m^2 in the denominator.
Multiplying the new lower bound by product |w_j|d_j and using d_j>=delta_j
gives (T) with no missing right-node determinant factor.

Validation grade: independent symbolic paper review, no scientific code,
NO_INVOKE certificate, m scan or old checker executed. The constants are
finite rational recipes, not evaluated experimental radii. This is a
fixed-m collar only; the compact remainder, any m-uniform radius and the
all-t/all-m global question stay open.

Reuse resolution: COMPOSE_APPLIED, old complete covariance and crossing
interface with standard coefficient majorants and the Neumann criterion.
No new global tool family or novelty claim is warranted. Shared control
and source context is disclosed; reviewer is nonauthor and not clean-blind.
The algebra is explicitly external; native X6 semantics and formal Task
status are unchanged. This is not a Driver disposition.

Researcher-ID: EM-REVIEW-58D6A2 / TASK_RESEARCH
