# D25 CM(-24): exact second-digit jet residual and a minimal p=5 witness

Date: 2026-11-05. Parent Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. Scope: **auxiliary Legendre/CM Hasse first jet**, not the original native H0/B0 divided-power experiment.

## Statement and exact witness
Define (Q(t)=t^4-140t^3+294t^2-140t+1), (H_p(t)=\sum_{j=0}^{(p-1)/2}\binom{(p-1)/2}{j}^2 t^j), (C_p(t)=16t(1-t^2)H'_p(t)+(1+2t-7t^2)H_p(t)). The accompanying source-verified CM 2-/3-isogeny theorem establishes (Q\mid C_p\pmod p) for every split-class prime (p\equiv5\pmod{24}).

The stronger naive statement (Q\mid C_p\pmod{p^2}) has an explicit **counterexample** at p=5. Here (H_5(t)=1+4t+t^2). Direct integral polynomial division gives

[
 C_5(t)\bmod Q(t)=-5550t^3+11500t^2-5390t+40,
]

hence, in ((\mathbb Z/25)[t]/Q),

[
 \boxed{C_5(t)=15+10t=5(3+2t)\not=0\pmod{25}.}
]

The coefficient vector ((3,2,0,0)\pmod5) is the **defined integral-lift second-digit observer** (T_5=(C_5\bmod Q)/5\pmod5). This is a proved finite counterexample to uncorrected second-digit vanishing, not a no-go for a corrected source-preserving Jacobi/Green relation.

## Finite exact observations
Executed locally using Python stdlib integer arithmetic, exact binomial coefficients and quotient reduction (t^4=-1+140t-294t^2+140t^3), then modulo (p^2). Complete checked population: all 26 primes (5\le p<550), (p\equiv5\pmod8) (13 split, 13 inert). For every split case C is coefficientwise divisible by p; for every inert case H is coefficientwise divisible by p. Each corresponding mod-p second-digit vector is nonzero in this tested population. Examples in basis (1,t,t^2,t^3):

| p | class | exact residue vector |
| --- | --- | --- |
| 5 | split | ((C_p/p)\bmod p=(3,2,0,0)) |
| 29 | split | ((17,8,16,17)) |
| 53 | split | ((49,21,2,24)) |
| 13 | inert | ((H_p/p)\bmod p=(8,11,4,9)) |
| 373 | inert | ((220,60,67,206)) |

The corresponding p=373 entry is **auxiliary Hasse** and is not an original-class native p373 H0/B0 result. Quotient-ring mod-p² arithmetic was executed, not a simulation of the native crystalline experiment.

## Source-preserving interpretation and next exact problem
The proved split zero provides the legitimate division by p, but the second digit requires a correction. Keep the labeled 2- and 3-isogeny tangent branches, their integral lifts, the Jacobi/Green Wronskian sign/port data and the chosen coefficient representation. The smallest next science unit is to write the exact mod-p² derivative identity for these two branches, compute the discrepancy from their common mod-p Frobenius endpoint, and match it to the existing Jacobi-Green-Wronskian source term. The original native p373 H0/B0, [X]U mod p², eta, kappa and Δ_p−R_p remain separate.

BRC resolution: COMPOSE_APPLIED as signed integral coefficient/valuation + branch provenance; the scalar quotient after mod-p cancellation is not inferred from a norm-only observer.

Grade: AUTHOR-EXACT COUNTEREXAMPLE (p=5), FINITE-EXACT 26-PRIME SURVEY, UNREVIEWED, NOT_ADMITTED. No new native CLAIM, OPEN, Source checkpoint, Result or independent acceptance.
