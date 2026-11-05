# D25 — Clausen finite-square boundary for the original 216 third digit

2026-11-05 · TASK_RESEARCH author-side exact theorem / finite precise computation · UNREVIEWED / NOT_ADMITTED.
Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen scientific Source c47e13e4aba0e006366f989d6334d443f6333ae3. Research logical lane chatgpt-research-onhour-enterprise-math-20260923; maintenance lane excluded.

## New all-prime third-digit identity

For every prime p=6n+1>=7, set
q_k=(1/6)_k(1/3)_k/(k!)², Q_p(z)=sum_{k=0}^{p-1}q_k z^k, theta=z d/dz,
W_p=sum_{k=0}^{p-1}(6k+1) binom(2k,k)^2 binom(3k,k)/216^k,
and B_p=2 sum_{i=1}^n sum_{r=1}^i (6(p+i-r)+1) q_i q_{p-r} 2^{-(p+i-r)}.
All denominators are p-adic units in these ranges. Then the following identity holds exactly modulo p³:

**W_p = Q_p(1/2)[Q_p(1/2)+12(theta Q_p)(1/2)] - B_p (mod p³).** (1)

Moreover p² divides B_p. Set C_p=(q_{p-1}/p²) mod p, a nonzero finite-field residue. With R_r=((r-1)!)²/[(11/6)_{r-1}(5/3)_{r-1}], the explicit boundary is

**B_p/p² = 2 C_p sum_{i=1}^n sum_{r=1}^i (6(i-r)+1) binom(n,i)binom(2n,i) 2^{-(1+i-r)} R_r (mod p).** (2)

All factorial and Pochhammer denominators of R_r are p-units on 1<=r<=n.

**Proof.** Classical Clausen's formal series identity gives
_2F_1(1/6,1/3;1;z)^2 = _3F_2(1/2,1/3,2/3;1,1;z).
The RHS coefficient c_k=(1/2)_k(1/3)_k(2/3)_k/(k!)³ satisfies c_k 2^{-k}=binom(2k,k)^2 binom(3k,k)/216^k. Up to degree p-1 the square of Q_p has precisely these coefficients. Applying (1+6theta) and setting z=1/2, the full finite square is Q_p(Q_p+12theta Q_p). Its difference from W_p is precisely the pairs 0<=i,j<p, i+j>=p. For p=6n+1, valuation v_p(q_k) is 0 on [0,n], 1 on [n+1,2n], and 2 on [2n+1,p-1]. Among omitted pairs, those of valuation <3 are exactly (i,p-r) and (p-r,i) for 1<=r<=i<=n. This proves (1), including the signed factor 2.

For 0<=i<=n the parameters reduce as 1/6=-n and 1/3=-2n modulo p, so q_i=binom(n,i)binom(2n,i) modulo p. The reverse recurrence q_{j-1}/q_j = j²/[(j-5/6)(j-2/3)] yields (q_{p-r}/p²)/C_p = R_r modulo p. Finally 2^{-(p+i-r)}=2^{-(1+i-r)} modulo p by Fermat and 6(p+i-r)+1=6(i-r)+1 modulo p. This proves (2). QED.

## Genuine remaining problem

The exact scalar target W_p=p modulo p³ on both frozen classes p=13,19 mod24 is equivalent in this representation to

Q_p(1/2)[Q_p(1/2)+12(theta Q_p)(1/2)] - p = B_p (mod p³). (3)

Unlike a pure-square shortcut, B_p is genuinely nonzero for some targets. For (p,B_p/p² mod p)=(13,0),(19,12),(139,91),(373,196). This directly exposes a p-dependent endpoint that a terminal WZ/adjoint construction must reproduce, with the original signed coefficient and valuation tiers intact. Previous D25 high-jet, shell, original p4 counterexample, and accepted D24 UR results are consumed, not claimed again.

## Exact executed check

The accompanying standard-library Python program independently evaluates W_p by integer binomial coefficients and Q_p by modular hypergeometric recurrence, checks (1), valuation tiers, reverse coefficient identity, and (2) for all 80 primes p=6n+1 from 7 through 997: 0 failures. At p=7,13,19,139,373 it also verifies each Clausen coefficient by explicit finite convolution against the original binomial formula: 0 failures. Selected (p,W_p mod p³,B_p/p² mod p): (13,13,0), (19,19,12), (139,139,91), (373,373,196). These finite checks are not the universal proof of (3).

## Source separation and continuation

Mother target: Delta_p-R_p=0 mod p on p=13,19 mod24; the frozen scalar source-interface transfer requires its own proof strength. Native original-class p373 H0/B0 divided-power [X]U mod139129, module rank, semilinear Frobenius direction/eta, signed odd Green/Hesse, kappa and independent replication are NOT_RUN, existing #1559 OPEN/UNASSIGNED. This finite Clausen theorem does not substitute native computation. Next exact mathematical action: derive a p-dependent terminal WZ/adjoint certificate for (3) using the signed boundary (2); separately obtain authorized native evaluator for #1559.

Current read of previous exact Source request onhour11-20261105-0856-d25-cont: SUCCEEDED, execution_authorized=false. Previous own registration MCP-491afa3ba2b94ec9b900ed3df6e345a3 is historical; no accessible session key. No own canonical CLAIM/open/run/checkpoint, review or accepted Result is asserted.