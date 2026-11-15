# JT2 / UR: p-adic lift sensitivity and unique balanced Legendre norm-jet lift

Date: 2026-11-16 (Asia/Taipei). New source-exposed, author-side mathematical reduction by the existing JT2 RESEARCH_DRIVER EM-DVR-DEBB5E; not a native independent review. The original UR ordinary-Legendre reduction belongs to EM-JT2-EF9380, its accepted limited stage review to EM-DVR-57CCCE.

## Exact source and hypotheses

Frozen input: research_returns/EMW59A_JT2_UR_SUN_PARITY_DEFECT_RETURN_EF9380_20260910.md, GitHub commit 969846f1d451b3e086f34a19b217e333c8a90c8d, blob b400bf432162cc5d67f51a1d2963de533c786afb; stage review driver_reviews/JT2_UR_NORM_JET_STAGE_REVIEW_57CCCE_20260920.md, blob 702f7ddf2816f7515d197f440c30d34f7c3cd244. Prior exact 45-prime finite audit: research_notes/driver/2026-11-16_jt2_ur_eps_norm_jet_exact_45_prime_audit.md @ 4f4ad7227b6003e00b835ab5802c20c6a9edf67e.

Let p>3 prime with p mod 24 in {13,19}, n=(p-1)/3=2m. Write the ordinary Legendre polynomial P_n(x)=Q_m(x^2), Q_m(Y) in Z_(p)[Y]. Define the polynomial J_m(Y)=sum_{r=0}^{n} ([Y^r] Q_m(Y)^2) Y^r/(2r+1). Every denominator is a p-unit since 2r+1 <= 2n+1 < p. For t^2=a, P_n'(t)/t=2Q_m'(a), I_n(t)/t=J_m(a), with I_n(x)=integral_0^x P_n(v)^2 dv.

If a in Z_(p) satisfies Q_m(a)=0 mod p, define the scalar E_p(a)=18*(Q_m(a)/p)*Q_m'(a)-2J_m(a)-3 mod p. The quotient is legal under that hypothesis. At the original fixed a=1/2 this equals the frozen norm-jet epsilon_p.

## Theorem 1 (exact first-order lift sensitivity)

Assume additionally Q_m'(a) != 0 mod p (SIMPLE). For every lambda in Z_(p), the shifted lift a_lambda=a+p*lambda retains CM0 and SIMPLE, and:

    E_p(a+p*lambda)-E_p(a) = 18*lambda*Q_m'(a)^2 (mod p).       (1)

Since p>3 and Q_m'(a) is a unit, the map lambda mod p -> E_p(a+p*lambda) is an affine bijection of F_p. Every simple root of Q_m mod p therefore has exactly one lift modulo p^2 for which E_p=0.

Proof: finite polynomial Taylor expansion gives Q_m(a+p*lambda)=Q_m(a)+p*lambda*Q_m'(a) mod p^2. Divide by p, and use Q_m'(a+p*lambda)=Q_m'(a) mod p, J_m(a+p*lambda)=J_m(a) mod p. Substitution establishes (1) and its bijectivity. QED.

## Theorem 2 (canonical balanced lift)

Fix a simple root alpha in F_p of Q_m. For any p-adic lift a of alpha put:

    a_bal = a - p*E_p(a) / (18*Q_m'(alpha)^2)  (mod p^2).        (2)

Equation (1) shows that a_bal is independent of the choice of a and is the unique lift of alpha with E_p(a_bal)=0. Let a_H be the Hensel root with Q_m(a_H)=0 mod p^2. Then:

    a_bal = a_H + p*(2*J_m(alpha)+3)/(18*Q_m'(alpha)^2) (mod p^2). (3)

Proof: under a -> a+p*lambda, the correction in (2) changes by minus p*lambda, cancelling the change in a. At a_H the quotient Q_m(a_H)/p vanishes mod p, so E_p(a_H)=-2J_m(alpha)-3. Substituting into (2) gives (3). QED.

The original fixed-lift UR norm-jet target epsilon_p=0 is equivalent to the congruence a_bal = 1/2 mod p^2 for every admissible p under the previously frozen CM0/SIMPLE hypotheses. This is a precise arithmetic equality between a unique Hensel-type balanced lift and the specified rational 1/2, not a new assumed axiom.

## Exact p=13 separation example

For p=13, n=4, Q_2(Y)=(35Y^2-30Y+3)/8 and J_2(Y)=(1225Y^4-2700Y^3+1998Y^2-540Y+81)/576.

At the frozen rational lift a=1/2, rational modular evaluation gives Q(a)/13=2, Q'(a)=12, J(a)=0 and E_13(a)=0, all modulo 13. At a'=1/2+13, Q(a')/13=1, Q'(a')=12, J(a')=0 and E_13(a')=5 modulo 13. Formula (1) predicts 18*12^2=5 mod 13. Exact rational modular evaluation additionally verifies E_13(1/2+13*lambda)=5*lambda mod13 for all 13 residue classes lambda.

Both lifts share a mod13=1/2, which is a nonsquare; in their respective quadratic rings t^2=a, Frobenius acts as t^13=-t mod 13. CM0 and SIMPLE persist. The variation changes the exact p-adic equation t^2=1/2, so it is a counterexample only to an inference from the reduced data alone, not to the fixed UR conjecture.

## Consequence for the open mathematical objective

Any all-prime derivation based only on mod-p CM0, SIMPLE and Frobenius anti-fixation has insufficient lift information to determine the fixed scalar. Equation (3) provides a concrete alternative target: independently determine the Hensel root and the polynomial norm J_m(alpha), then compare their balanced combination with the exact 1/2 modulo p^2. The full UR uniform equality remains open; this new result is a proved structural reduction. No new Native Result, official Task completion, parent completion or researcher CLAIM follows.

Attribution: original reduced obstruction EM-JT2-EF9380; prior stage review EM-DVR-57CCCE; lift sensitivity, balanced-lift reduction and 13-adic distinguishing calculation EM-DVR-DEBB5E.