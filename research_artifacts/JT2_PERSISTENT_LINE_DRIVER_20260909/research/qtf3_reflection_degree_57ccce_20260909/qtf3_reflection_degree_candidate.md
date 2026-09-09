# QTF3 fixed point: finite reflection and degree candidate

Status: **DRIVER-AUTHORED PAPER CANDIDATE / NONAUTHOR REVIEW PENDING**.

Author: EM-DVR-57CCCE. This is a new argument developed after the bounded review of the older p² candidate. It is not a formal Task Result, new CLAIM, completed QTF3 task, accepted LIFT proof or Foundation theorem. This author cannot supply its decisive non-author review.

## Declared input

Consume the exact finite polynomials from [candidate 9e3a41dc](https://github.com/awdawmip/enterprise-math/blob/9e3a41dc9909ad98c789bb8d53a27addd0649eaa/research_artifacts/JT2_PERSISTENT_LINE_DRIVER_20260909/reviews/ur_reuse_20260909/driver_authored_transport_candidate.md), with the qualified paper support recorded by [reference review 8bb5790f](https://github.com/awdawmip/enterprise-math/blob/8bb5790f3ae1f49cfdb780e94eea78d0192c59c3/research_artifacts/JT2_PERSISTENT_LINE_DRIVER_20260909/reviews/advisory_ef9380_20260909/reference_review.md).

For a prime p=6m+1, p>3, put R=Z_(p),

\[
c_k=\frac{(1/6)_k(1/3)_k}{(k!)^2},\quad
b_k=\frac{(1/3)_k(2/3)_k}{(k!)^2},\quad
F_p(z)=\sum_{k=0}^{p-1}c_kz^k,\quad
L_p(u)=\sum_{k=0}^{p-1}b_ku^k.
\]

All displayed coefficient denominators are p-units. Let
\[
\phi(u)=4u(1-u),\qquad D_p(u)=L_p(u)-F_p(\phi(u)).
\]

The consumed Q2 proof supplies **two distinct facts**:

1. D_p belongs to p² R[u].
2. The coefficients of D_p in every degree below p are exactly zero over R, before reduction.

The second fact is the finite-prefix identity in that proof, not a consequence of the congruence alone. It must remain in the input contract. Also deg(D_p)<=2p-2 because both original truncations stop at p-1. No older prime experiment or p² bridge proof is rerun here.

## Finite reflection-degree lemma

Let p be an odd prime. Suppose F,L in R[u] have degrees at most p-1. Define D(u)=L(u)-F(4u(1-u)). Assume D is in p² R[u] and its coefficients below degree p vanish exactly. Then

\[
L(1/2)\equiv F(1)\pmod {p^3}.
\]

**Paper proof.** The divisibility and exact prefix give a well-defined coefficientwise quotient
\[
E(u)=D(u)/p^2=u^p r(u),\qquad r\in R[u],\quad \deg r\le p-2.
\]

The composition F(4u(1-u)) is exactly invariant under u↦1-u. Consequently
\[
E(u)-E(1-u)=\frac{L(u)-L(1-u)}{p^2}
\]
is a polynomial of degree at most p-1. Its integrality follows from the left-hand side; exact evenness of L is not assumed.

Only now reduce coefficients modulo p. Write bars for this reduction and use the characteristic-p identity (1-u)^p=1-u^p. Then
\[
\bar E(u)-\bar E(1-u)
=u^p\bigl(\bar r(u)+\bar r(1-u)\bigr)-\bar r(1-u).
\]

The last term has degree at most p-2. For every j=0,...,p-2, the coefficient of u^(p+j) on the left is zero. It therefore equals the coefficient of u^j in \(\bar r(u)+\bar r(1-u)\), which must also vanish. Hence
\[
\boxed{\bar r(u)+\bar r(1-u)=0\quad\text{in }\mathbb F_p[u].}
\]

At u=1/2, the two summands coincide and 2 is a unit, so \(\bar r(1/2)=0\). Thus E(1/2) is in pR, and D(1/2) is in p³R. Since φ(1/2)=1, the assertion follows.

This proof uses Frobenius only after factoring p² and reducing modulo p. It does not use a Frobenius identity modulo p², a square-root evaluation, an infinite-series limit or a numerical cancellation.

## Application to the existing QTF3 target

The declared finite F_p,L_p satisfy every hypothesis. The candidate conclusion is therefore

\[
\boxed{
\sum_{k=0}^{p-1}\frac{(1/3)_k(2/3)_k}{(k!)^2\,2^k}
\equiv
\sum_{k=0}^{p-1}\frac{(1/6)_k(1/3)_k}{(k!)^2}
\pmod {p^3}
}
\]

for every prime p≡1 mod6, p>3. This includes the line's p≡13,19 mod24 classes. CM0, SIMPLE, Chisholm's weighted theorem and Borwein's CM coefficient are not needed for this fixed-point argument; their scopes are not widened by it.

The residual's homogeneous reflection component is killed directly by the finite degree compatibility. In particular \(r_p(0)+r_p(1)=0\pmod p\). No differential equation or Hasse-basis normalization is required. This is the shorter finite-invariant route allowed by the current QTF3 taskbook. It does not independently validate every separate differential-equation claim in the older handoff.

Relative to the six current QTF3 outputs, the proposal supplies an alternative exact residual invariant, its fixed-point zero and the displayed truncated congruence, with the broader prime scope justified by the consumed Q2 input. A non-author must check this new proof before any formal Task Result disposition. The exact-degree and exact-prefix hypotheses must not be weakened to low-precision approximations.

## Information retained, and what stays open

The decisive retained information is the cutoff p-1, the exact zero prefix, the degree bound 2p-2, the sign D=L-F∘φ and the exact symmetry of φ. An ODE-only view can discard the finite degree compatibility that kills a possible reflection component. This is an application of the existing operation-safe quotient discipline; no new tool family or unavailable capability is claimed.

The conclusion is a p³ statement at the fixed point only. It is not a p³ polynomial congruence at every u. At the CM ports u=(1±t)/2, the quadratic address is 1/2, whereas the fixed point used above has address1. The weighted old LIFT/Clausen target at address1/2 remains a separate arithmetic/transport obligation. No implication from this fixed-point certificate to old LIFT is asserted.

Sun output3's adjacent-value elimination and its conditional exact-obstruction alternative remain open. Neither parent objective, the final audit, nor final integration is closed.

## Bounded review request within the existing line

Check only: the two consumed Q2 facts; coefficientwise p² division and degree bounds; exact reflection cancellation; the high-coefficient comparison after reduction; fixed-point specialization and prime scope; and separation from weighted LIFT. Do not reprove the old p² bridge, rerun the 77-prime record, construct a new generic tool or use this author's own memo as independent acceptance.

No mathematical program or native BRC arithmetic was executed. Runtime quotient/remainder/digit materialization, if later needed, must use the existing facade and actual reconstruction traces; the divisions above are justified symbolic algebra.

Driver-ID: EM-DVR-57CCCE / CONTROL_PLANE

Global-Knowledge-Sync: main@5f14819 / GLOBAL_KNOWLEDGE_V1
