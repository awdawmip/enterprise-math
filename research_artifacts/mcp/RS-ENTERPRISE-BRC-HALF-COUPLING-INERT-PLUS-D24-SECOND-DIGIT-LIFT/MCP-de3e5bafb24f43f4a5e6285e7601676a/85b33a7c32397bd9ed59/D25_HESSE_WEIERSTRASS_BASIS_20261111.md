# D25 native Hesse to Weierstrass isomorphism and explicit de Rham basis (2026-11-11)

TASK_RESEARCH / original active D25 run RUN-d3deee35d5e9e40b9358ebbb, Researcher EM-ENTERPRISE-9C9163, claimed as MCP-6de695b532e654210160c52c. Source scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. This new exact model-unit follows the same author's already staged all-target Hesse W2 curve and finite coefficient bridge. AUTHOR-PROVED / UNREVIEWED / NOT_ADMITTED, not a native [X]U Frobenius computation.

## Exact projective isomorphism, both p=13 and p=19 mod 24

Let p>=13 with p mod24 in {13,19}. Over R_r=(Z/p^r)[T]/(T^2-2), choose one of the three Hensel-lifted roots a with a^3=t=4+2T (proved to exist by Norm(t)=8). Set d=a^3-1=t-1; N(d)=1, so d is an R_r unit. On the smooth original Hesse cubic
  F_H(x,y,z)=x^3+y^3+z^3-3a xyz=0,
put w=x+y+a z, b=x-y, and c=12d. Define linear projective coordinates
  X' = c*z - 9a^2*w,
  Y' = 3c*b,
  Z' = w.
A direct polynomial expansion, valid over the integer polynomial ring Z[a,x,y,z], gives the exact identity
  (Y')^2 Z' -(X')^3 - A X'(Z')^2 - B (Z')^3
  = 1728*(a^3-1)^2 * F_H(x,y,z),
where A=-27*a*(a^3+8), B=54*(a^6-20a^3-8).
The 3x3 coordinate-change determinant is 864*(a^3-1)^2, a unit at every stated p. Hence this is an actual invertible projective transformation of the original curve over every R_r, not merely a j-matching curve or a twist guess. It carries the Hesse flex (1:-1:0), where w=0, to the Weierstrass point at infinity (0:1:0).

On the affine chart w ne 0 the same map is
  X=12(a^3-1)*z/w - 9a^2,   Y=36(a^3-1)*(x-y)/w,
and the native original-class Weierstrass equation is
  Y^2=X^3-27a(a^3+8)X+54(a^6-20a^3-8).
Its j invariant is exactly 27t(t+8)^3/(t-1)^3 = 2417472-1707264T, agreeing with the frozen D=-24 Hesse CM input. The source conjugate is retained separately by sigma(T)=-T.

## Integral differential/basis and its verified normalization

For the smooth Weierstrass model over R_r with 2,3 and its discriminant invertible, use the standard rank-two algebraic de Rham basis
  e0=[dX/(2Y)] (holomorphic),   e1=[X dX/(2Y)] (second kind).
It is a full rank-two de Rham module over the base, not a rank-one unit-root hypothesis. On the Hesse chart z=1, the Poincare residue differential is omega_H=dx/F_y=dx/[3(y^2-a x)]. Let w=x+y+a, b=x-y. Implicit differentiation on F_H=0 gives
  dw = (F_y-F_x)/F_y dx = -3 b w /F_y dx.
With X=12d/w-9a^2 and Y=36d b/w, this yields
  dX/(2Y)= -dw/(6 b w) = dx/(2F_y),
and therefore the exact source-model normalization
  omega_H = 2 e0.
This identifies a genuine geometric holomorphic basis vector and a concrete scalar, before any Gauss-Manin or crystalline Frobenius transport. The original target omega+6*nabla_lambda omega still needs its own parameter/connection identification; the Hesse parameter a here must not silently be equated with the frozen lambda=1/2.

## Exact p=373 witness over W_2

In R_2=(Z/139129)[T]/(T^2-2), retain a=91441+93269T with a^3=4+2T.
Then
  c=12(t-1)=36+24T,
  A=90958+42667T,
  B=135673+137833T,
  discriminant -16(4A^3+27B^2)=121889+20133T (mod139129).
Its residue discriminant norm is 221 mod373, nonzero. The projective isomorphism determinant is 864*(t-1)^2, which is a unit because N(t-1)=1. Every coefficient was computed using exact integers in the declared quadratic ring. The polynomial projective identity was also symbolically factored: its exact common factor is 1728*(a^3-1)^2.

## Scientific dependency now narrowed

The original D25/LIFT remains OPEN. Previously accepted CM0/SIMPLE and UR/JT0 are consumed; previously staged ordinary Hesse norm and Hilbert90 notes are not recredited. This new explicit projective equivalence resolves the algebraic original-curve model and produces a full de Rham basis with holomorphic normalization. It does not construct the source's fixed divided-power H0/B0 model, calculate its [X]U modulo p^2, or identify its semilinear Frobenius, kappa, and Delta_p-R_p. These remain required, with both source ports and information-loss guards intact.

Precise next action: on this same W2 curve and e0,e1, determine the original source H0/B0 basis convention, Gauss-Manin parameter and Frobenius lift, then construct/verify a true crystalline 2x2 sigma-semilinear [X]U at p373 (not just coefficient Frobenius); transport it to the declared omega+6*nabla_lambda omega and kappa observers and compare to Delta_p-R_p. If a source-required different basis is found, explicitly compute the basis-change matrix. No native Frobenius experiment has yet been run.
