# Nondecisive mathematical review: complete trace for bounded relative gaps

Reviewer: EM-REVIEW-58D6A2. Activity: RA-BALANCE-REVIEW-20261028-58D6A2.
Date: 2026-10-28, Asia/Shanghai.
Finding: the new complete-trace scaling-limit inequality and effective
uniform large-total-scale theorem follow from the exact stated source
interfaces. No unresolved mathematical defect was found. This is a new
independent paper review of this stronger scope, not an inherited verdict
from the c1, bounded-sector or small-cone results.

Reviewed file:
`analysis/PARITY_FULL_TRACE_BOUNDED_RELATIVE_GAP_TAIL_AUTHOR.md`.
SHA256: `129cad117292b1e90f3f0f8eb6c2791c2e5a050adff386c9e4a0b4c6e0d55c5e`.

I read the entire frozen manuscript and the actual selected metric proof
in `analysis/parity_c1_v2_source_actual.json`, blob
`c94088a17f4a09dd2d16171162c09ed13807a8bf`, including its precise normalization,
centered parity residue argument and finite-r limitations. The complete
trace/polynomial interface from blob f05b0b5be5c7d78c7faf58ae1f818bc67cea103c
was already read for the first review; the unchanged formulas are reused
rather than counted as a second proof review. The first-round support
lemma is bound to its final SHA256 f9a9415455b9b004f9e2854e999eaebd4934acd7211084b87bf1bc5c0634e921.

## 1. Common input congruence and matrix order

The derivative polynomials phi'_j(r0+theta) have nonzero triangular leading
coefficients and form an invertible basis on degrees 0..n-1. Thus the same
U(r0) is canceled from G_L and G_N at each fixed physical input. No
moving-frame derivative occurs in this argument.

The finite nilpotent identity
F_L=exp(LJ/2)E_L is exact, with E_L containing only even powers of J and
having diagonal one. Right multiplication by the SAME
T0=exp(r0 J/2) then produces exp(rJ/2)E_L and exp(sJ/2)E_N. This is the
load-bearing common-input identity: unrelated endpoint-dependent input
changes would not preserve the relative trace.

I checked the scaling on the actual derivative-matrix entries:
C_r J C_r^(-1)=J/r, hence C_r exp(rJ/2)=exp(J/2)C_r and
C_r E_L=E_(L/r) C_r. It follows that the common earlier matrix is
C_r E_lambda^T A_c(epsilon) E_lambda C_r. At the later endpoint,
C_s=C_r D_v and N/s=(lambda+nu)/(1+nu), so canceling C_r puts D_v on
both OUTER sides of the later E/A/E product, exactly as equation (8)
states. The order is correct without commuting D_v with E_lambda'.

The physical fractions satisfy 0<lambda<=1 and nu>0. The stated rectangle
lambda in [0,1] is a regular algebraic/analytic extension, not a physical
zero first-gap assumption. Half-integer scale powers are real and positive
because r,v>0.

## 2. Complete limiting spectrum and determinant ratio

The selected old source actually proves that centered M_c has zero
cross-parity blocks, a positive even block and a negative odd block.
Its positive weighted Gram argument includes the empty odd block for m=2.
The new E_lambda, E_lambda' and diagonal D_v preserve those same degree
parities. Congruence therefore makes BOTH limiting endpoint forms definite
with the same sign on each block. Negating the odd block on both sides
reduces the generalized spectrum there to the positive-definite case.
All n limiting generalized eigenvalues are thus positive real numbers.
This conclusion does not assert finite-r definiteness or discard its
cross-parity terms.

The exponent calculation is
2*sum_(j=0)^(m-2)(j-m+1/2)=-(m^2-1). Together with det E=1 this gives
det A0/det B0=v^(m^2-1). AM-GM on the positive limiting eigenvalues gives
trace(B0^(-1)A0)-n >= n*(v^(m+1)-1), uniformly in lambda. The use of
AM-GM would fail for arbitrary indefinite relative forms; the common
parity-definite decomposition pays exactly that obligation here.

## 3. Uniformity as the second gap tends to zero

Bare compact convergence of Gap would not prove positivity for arbitrarily
small nu. The proof retains the exact factor correctly. In the source
numerator, p+q<=j-1 implies that substituting
a=lambda/(m epsilon), c=nu/(m epsilon), then dividing Z by epsilon, leaves
only nonnegative epsilon powers. Therefore P(epsilon,lambda,nu) is a
finite rational polynomial and
Gap=nu*P/(mD) exactly. The H-germ determinant constant K is correctly
kept distinct from the metric coefficient kappa.

D(epsilon,nu) and D(0,nu) are both at least d0>0 on the nonnegative
domain. At nu>0 the exact common-scaled matrices identify F(0)=G0/nu;
continuity of the rational polynomial extension then preserves
F(0)>=m^2-1 at nu=0 as well. This is not division by an actual zero
physical gap.

For fixed rational C, each finite coefficient sum A_C,B_C,H_C is an
effective rational upper bound on the full rectangle lambda in [0,1],
nu in [0,C]. Expanding the quotient difference with the two d0 denominator
bounds gives precisely E_C, including its factor 1/m. The threshold
R_m(C)=max(1,2E_C/(m^2-1)) therefore makes the error at most
(m^2-1)/2. Multiplying by nu and using Bernoulli's inequality converts
the limiting lower bound to the stated half-strength bound. No lower
bound on either physical gap or upper bound on a enters this estimate.

## 4. Scope, proof grade and harvest

The proved new scope is: for each fixed m>=2 and positive rational C,
all S>=0,a>0 with sufficiently large S+a, and every
0<c<=C(S+a), including S=0 and large a. The threshold is explicit by
finite coefficient formulas, but has not been numerically evaluated and
is not claimed practical. No uniform threshold over m or unbounded C,
all-total-scale positivity, coefficientwise positivity, or mother-objective
closure follows.

This review is an independent symbolic paper derivation. No scientific
program, matrix scan, old certificate, NO_INVOKE work or symbolic algebra
package was run; no proof-kernel verification is claimed. The substantive
new bridge is the exact common input center and its complete limiting
generalized-spectrum comparison, then a uniform error retaining nu.
The nilpotent calculus, old metric and polynomial interface, coefficient
majorants and AM-GM are COMPOSE_APPLIED existing methods; this is not a
new global tool family or literature-novelty assertion.

Reviewer did not contribute to the construction and received the complete
proof only after its byte freeze. Shared control and prior source context
are disclosed, so this is nonauthor NONBLIND review, not clean-blind review.
External real matrix algebra remains distinct from native X6 semantics.
No formal Driver disposition, Result acceptance, Task closure, Working
Truth or Foundation promotion is granted by this report.

Researcher-ID: EM-REVIEW-58D6A2 / TASK_RESEARCH
