# R005-A — Continuous p=2 Three-Factor Residual Range through k=894,427,190

Status: `EXACT PREFIX + EXTERNAL EXHAUSTIVE GAP TRANSFER / PROVED R005 CONSEQUENCE / NOT CANONICAL`  
Date: `2026-08-10`

## 1. Stronger goal

The earlier coarse p=2 transfer used the single global gap bound 1328 and therefore started only at k=440232. The maximal-prime-gap record table tells us where each larger record gap first appears. Using the scale-dependent maximal gap instead of the final 1328 constant lowers the analytic/computational handoff to k=11990. The remaining finite prefix can then be verified exactly.

The result is a continuous finite statement from k=2.

## 2. Exact identity for the fourth-root core

For a square basin `U=k^2+2k=(k+1)^2-1`,

`floor(U^(1/4))=floor(sqrt(k))`.

Thus the fourth-root core changes only when k crosses a perfect square. If `C4=floor(sqrt(k))`, the narrowest e=1 cofactor interval among fourth-root-core witnesses has width `2k/C4`.

## 3. Scale-dependent maximal gap bound

Let G(x) be the largest externally computed consecutive-prime difference whose first prime is at most x. For a fourth-root-core witness q, the cofactor point is `x_q=k^2/q`, and the largest such point occurs at q=2: `x_max=k^2/2`.

Therefore it is enough to have

`G(k^2/2)*C4 <= 2k`.

If this holds, every q in the fourth-root core has a prime cofactor inside its available interval and is forced.

## 4. Why only finitely many discontinuities need checking

Define `M(k)=2k-G(k^2/2)*floor(sqrt(k))`.

This can decrease only at two kinds of points:

1. core jumps `k=c^2`;
2. a new maximal prime-gap record becoming relevant, when `k=ceil(sqrt(2*P_record))`.

Between these points both G and `floor(sqrt(k))` are constant, so M(k) strictly increases.

Consequently the entire interval up to 894 million requires only about thirty thousand core-jump checks plus the finite maximal-gap record jumps, not hundreds of millions of basin evaluations.

## 5. Exact prefix 2 <= k < 11990

A deterministic verifier checks every fourth-root-core prime witness for every `2<=k<11990`: 237,774 exact witness checks.

There is exactly one basin in this prefix whose fourth-root core is not fully forced:

`k=121, q=11`.

This does not generate a residual. The verifier exhaustively factors every composite in the k=121 basin and checks the complete forced witness set; the residual fiber is empty.

Therefore every actual residual in the full exact prefix still satisfies `Omega=3`.

This is an important boundary example: failure of the fourth-root sufficient condition does not imply a residual exists.

## 6. Record-gap transfer 11990 <= k <= 894427190

For the upper portion, the certificate consumes two explicit external computational inputs:

- Oliveira e Silva et al. report all consecutive-prime gaps below `4*10^18` computed and double-checked through `4*10^17`;
- the maximal-gap first-occurrence table supplies the scale-dependent record gaps; below the chosen `4*10^17` boundary the largest relevant actual prime difference is 1328.

The executable checks every discontinuity of M(k) in `11990<=k<=894427190`: 29,845 points. All margins are nonnegative; the minimum margin is exactly zero at k=11990, where `C4=109` and the relevant maximal prime difference is 220.

The upper endpoint is the exact conservative solution of `k^2/2+1328<=4*10^17`. The next k leaves the selected double-checked range; it is not a mathematical counterexample.

## 7. Continuous consequence

Combining the exact prefix and the record-gap transfer:

`for every 2<=k<=894,427,190`,

under the stated external exhaustive-gap premise,

**every square-basin residual composite, if one exists, has `Omega(n)=3`.**

This does not say every basin has a residual and does not say every basin lacks a least witness basis.

## 8. Consequence for p=2 research

Within this finite range, residual arity is settled. The p=2 problem reduces to the exact three-factor shell from T-A23:

`n=abc`, `U^(1/4)<a<=U^(1/3)`,

with a and b non-forced candidate prime witnesses.

Therefore the meaningful remaining questions are: when do two non-forced witness coordinates coexist in the root annulus; when can they close a product with a third prime inside the width-2k square shell; and what distinguishes the repeated-prime and squarefree exact certificate sectors.

The search variable should now be non-forced witness pairs and reciprocal prime gaps, not basin composites.
