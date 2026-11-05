# D25 second unit — two-stage third-digit Clausen observer

2026-11-05 · Research author-side conditional exact reduction and finite exact evidence. UNREVIEWED / NOT_ADMITTED. Frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3, Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Consumes preceding new checkpoint commit 446215ae2cb7c84c08d09da7b00de15ff29e1d02. Research lane chatgpt-research-onhour-enterprise-math-20260923 (no maintenance identity).

## Exact theorem: two p-adic digit equations

Let p=6n+1>=7 prime, q_k=(1/6)_k(1/3)_k/(k!)², Q_p(z)=sum_{k=0}^{p-1}q_k z^k, theta=z*d/dz. Consume the preceding proved exact original-216 signed boundary identity
W_p = Q_p(1/2)[Q_p(1/2)+12(theta Q_p)(1/2)] - p² T_p (mod p³),
where T_p is the explicit double-sum boundary/p² in F_p. When Q_p(1/2)=0 mod p, choose residues a,b,d,e,T_p in [0,p-1] such that
Q_p(1/2) = p a+p² b (mod p³), (theta Q_p)(1/2)=d+p e (mod p²).

Then **W_p=p (mod p³) is equivalent to these two equations together:**
(A) 12 a d = 1 (mod p);
(B) (12 a d - 1)/p + a² + 12 a e + 12 b d - T_p = 0 (mod p).
The quotient is an integer when (A) holds, with the displayed canonical residues. To prove this equivalence, expand the exact preceding expression:
W_p = 12p a d + p²(a²+12ae+12bd-T_p) (mod p³).
This exact conditional identity isolates two finite observers and preserves the original nonzero-in-general signed boundary. It is not yet a proof of (A),(B) for all target primes.

For every prime p=6n+1, the unconditional finite-field identity
Q_p(1/2) = sum_{k=0}^n binom(n,k)binom(2n,k)2^{-k} (mod p)
follows from 1/6=-n and 1/3=-2n modulo p, with q_k=0 modulo p beyond n. Thus the vanishing of this explicitly given binomial sum for p=13,19 mod24 is a precise, separately testable next lemma; it is not silently assumed proven.

## Exact finite experiment and discriminant

The independent integer-binomial and hypergeometric checker from checkpoint 446215a was re-used, without recomputing older 216-shell results. Across **all 80 primes** p=6n+1 from 7 to 997, the finite binomial sum vanishes modulo p on all 45 target-class primes p=13,19 (mod24) and is nonzero on all 35 complementary primes p=1,7 (mod24). Both (A) and (B) pass at all 45 target primes; zero failures. In this finite coverage the observed split matches quadratic character (2/p)=-1 versus +1. All-prime residue-character vanishing is a **conjecture** (finite observation), not established here.

Anchor residues (p,a,b,d,e,T_p, 12ad modp, observer B): (13,11,5,7,6,0,1,0), (19,8,4,1,9,12,1,0), (139,82,54,38,53,91,1,0), (373,24,176,294,291,196,1,0). Integer carries in (B) use the canonical residue representatives, not an unspecified p-adic lift.

## Next action and Source boundaries

Prove finite binomial vanishing for target primes, preferably by an explicit finite-field symmetry/quadratic-character or source-valid CM argument, then construct a p-dependent terminal WZ/adjoint proof of (A),(B), retaining T_p. A merely finite sample is not an all-prime proof. Frozen mother target Delta_p-R_p=0 mod p; original interface retained. Native original-class p373 H0/B0 [X]U mod139129, true rank, semilinear Frobenius/eta/kappa and signed odd Green/Hesse independent replication remain NOT_RUN under existing #1559 OPEN/UNASSIGNED. Old own Source request onhour11-20261105-0856-d25-cont read SUCCEEDED with execution_authorized=false. Own native CLAIM/run/checkpoint NOT_ESTABLISHED; no formal Result/review asserted.