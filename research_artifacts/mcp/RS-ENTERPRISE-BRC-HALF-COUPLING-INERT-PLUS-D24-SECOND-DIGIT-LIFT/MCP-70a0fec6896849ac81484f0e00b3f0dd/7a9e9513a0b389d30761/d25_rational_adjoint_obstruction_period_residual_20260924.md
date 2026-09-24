# D25 LIFT — uniform rational first-order adjoint obstruction and the exact period residual

Status: PROVED_STRICT_NEGATIVE_CERTIFICATE / PORTABLE_D25_MATH_ONLY / LIFT_NOT_YET_CLOSED / NOT_A_RESULT / UNREVIEWED
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT
Publication: TP2-B6F4FC938FF94941C1B7
Date: 2026-09-24

## 0. Consumed frontier

Consume the durable cutoff-jet bridge

    Z_T = [a_parent Psi-1]/p + a_parent H_1^{<=m}/6 + Psi F_2^{<=2m}/72  (mod p),

and the exact three-layer transport for p=6m+1, with q0=T_k(0), q1=T'_k(0)/6, q2=T''_k(0)/72,

    J_{k+1}=M_k J_k,
    M_k=[[r0,0,0],[r1/6,r0,0],[r2/36,r1/6,r0]],

    r0=(k-m)(k-2m)/(2(k+1)^2),
    r1=(3k-4m)/(2(k+1)^2),
    r2=1/(k+1)^2.

The two typed zero edges k=m and k=2m must remain explicit. The Driver diagnostic proposed testing a rational first-order adjoint/telescoper for the live cutoff jet and returning failure as a typed residual rather than replacing it by a larger prime census. This unit gives that exact negative certificate.

## 1. The q2 adjoint equation is forced and decoupled

Let lambda_k=(x_k,y_k,z_k)^T be a row-adjoint written as a column, so a first-order telescoping identity for weight w_k=(w0,w1,w2)^T requires

    M_k^T lambda_{k+1}-lambda_k = w_k.

Because the third column of M_k is (0,0,r0)^T, its q2 coordinate is independent of x and y:

    r0(k,m) z(k+1,m)-z(k,m)=w2(k,m).                 (A)

For the current cutoff derivative scalar, w2=Psi on the interior of the F_2^{<=2m}/72 support. Thus any uniform rational first-order adjoint over a coefficient field containing nonzero Psi would, after division by Psi, give a rational solution of

    r0(k,m) z(k+1,m)-z(k,m)=1.                      (B)

Lower-layer coupling cannot remove this necessary equation.

## 2. Theorem: (B) has no rational solution in Q(m)(k)

Write

    A(k)=(k-m)(k-2m),    B(k)=2(k+1)^2.

Then (B) is

    A(k) z(k+1)-B(k) z(k)=B(k).                     (C)

Work over K=Q(m), with m an indeterminate. Suppose z is rational. We first prove that z has no finite pole.

Fix one integer-translation orbit of poles in an algebraic closure of K. Since a rational function has finitely many poles, choose a rightmost pole beta in that orbit, so beta+1 is not a pole. At k=beta, z(k) has a pole but z(k+1) does not. The right side of (C) is polynomial. Therefore the pole of -B(k)z(k) can disappear only if B(beta)=0. Hence beta=-1.

Likewise choose a leftmost pole gamma in the same orbit, so gamma-1 is not a pole. Evaluate (C) at k=gamma-1. Then z(k+1)=z(gamma) has a pole while z(k) does not, so cancellation is possible only if A(gamma-1)=0. Therefore

    gamma=m+1   or   gamma=2m+1.

But beta and gamma belong to one integer-translation orbit. Thus for some integer N,

    -1 = m+1+N   or   -1 = 2m+1+N,

which is impossible in Q(m) because m is transcendental over Q. Hence z has no finite poles and therefore z is a polynomial in k.

Now let deg_k z=d. If d>0 with leading coefficient c != 0, then r0(k,m)=1/2+O(1/k), so

    r0 z(k+1)-z(k) = -c k^d/2 + O(k^{d-1}),

which cannot equal the constant 1. If d=0, z=c, then c(r0-1) is nonconstant in k (or zero when c=0), so it also cannot equal 1. Contradiction.

Therefore

    BOXED: no z(k,m) in Q(m)(k) satisfies (B).

The same proof works over any purely transcendental coefficient extension K containing m, in particular Q(m,Psi,a_parent), and for any nonzero constant right side C by rescaling.

## 3. Zero-edge and finite-cutoff robustness

This is not invalidated by allowing the certificate to treat k=m or k=2m as explicit boundary defects. A single rational formula valid on either regular wedge 0<=k<m or m<k<2m for all positive integer m would satisfy (B) as a rational identity: each wedge supplies a Zariski-dense set of (k,m) points. The same applies to separate rational formulas on the two regular sectors. Thus a source-faithful WZ proof may have typed zero-edge handoffs, but it cannot make the nonzero q2 interior weight disappear through a purely rational first-order adjoint.

This is a generic/uniform obstruction. It does not rule out a prime-specific accidental simplification when Psi vanishes modulo one prime, nor does it rule out higher-order, non-rational, or coupled certificates.

## 4. Exact residual carrier by variation of constants

The failure has a precise one-dimensional residual form on every regular interval. Fix a base index a not crossing a zero edge and define the homogeneous forward carrier

    H_{a,a}=1,
    H_{a,k+1}=r0(k,m) H_{a,k}.

Write z_k=U_k/H_{a,k}. Then

    r0 z_{k+1}-z_k=C

is equivalent exactly to

    U_{k+1}-U_k=C H_{a,k}.

Hence every solution in a difference-field extension has

    z_k = [U_a + C sum_{j=a}^{k-1} H_{a,j}] / H_{a,k}.

So the typed obstruction is not an unspecified failure: the missing coordinate is the partial hypergeometric period

    Pi_{a,k}=sum_{j=a}^{k-1} H_{a,j}.

On the first regular sector with a=0, H_{0,k}=q0_k because q0_0=1. The no-rational-adjoint theorem says precisely that this period quotient cannot be eliminated inside Q(m)(k). Across k=m and k=2m the interval constants and off-diagonal injections must be glued source-faithfully; this unit does not claim that the resulting period coordinates are globally independent.

## 5. BRC information audit

Population: the transported colored jet ports (q0,q1,q2), with k, derivative order and the two zero edges retained.

Observer: the live cutoff scalar entering the D25 divided second digit.

Safe conclusion: the q2 interior channel has an unavoidable non-rational first-order residual in any uniform rational-adjoint attempt.

Preserved residual/provenance: the hypergeometric period Pi, interval base, m/2m zero-edge handoffs, Psi coefficient, and the separate absolute product digit [a_parent Psi-1]/p.

Forbidden compression: do not report CAS failure as the theorem; do not delete Psi or the q2 layer; do not identify Pi with a Frobenius scalar without an exact source bridge; do not infer that all higher-order or non-rational certificates are impossible.

BRC_REUSE_RESOLUTION=COMPOSE_APPLIED.

## 6. Consequence / next action

The previous next action can now be narrowed. Do not continue searching for a pure uniform rational first-order adjoint of the full three-layer cutoff scalar: its q2 equation is already impossible. Instead seek the smallest source-faithful extension in one of two directions:

1. adjoin the explicit hypergeometric period Pi on the regular sectors and derive the exact zero-edge gluing at m and 2m, then test whether the actual weighted q1/off-diagonal injections collapse the residual against the divided product digit; or
2. derive a genuinely higher-order contiguous/WZ relation for the coupled cutoff scalar.

Any Frobenius coordinate remains admissible only after proving equality to this explicit period/cutoff source, not by analogy. LIFT/JT2 remains open.
