# D25: nontrivial second-digit re-coalescence of distinct labelled sources

2026-11-06 | Author-side finite exact certificate | UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CHECKPOINT.

Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; frozen source c47e13e4aba0e006366f989d6334d443f6333ae3.

Retain the same 3-source U_j and weighted W_p from the earlier first-digit and p^3 second-jet notes, with lifted gradient A and Hessian H. For any p=6m+1 prime >=7, any p-local vectors v and delta satisfying A dot delta=0 (mod p), and any p-local scalar lambda:

```text
[W_p(v+lambda*delta)-W_p(v)]/p^2
     = lambda*k + lambda^2*c                    (mod p)
k = (A dot delta)/p + v^T H delta               (mod p)
c = (delta^T H delta)/2                         (mod p)
```

**Theorem:** The formula holds universally under the displayed kernel hypothesis, by substituting lambda*delta into the proved second-jet Taylor expansion. If both k and c are nonzero modulo p, its roots are lambda=0 and lambda=-k/c, two distinct p-adic source parameters with identical weighted scalar through p^3. This is a quadratic fiber law and does not assert all primes satisfy its nonzero hypotheses.

Take the original v*=(-1/3,-1/2,-2/3) and delta=(1,0,1), which is first-digit invisible at the following *exactly checked* primes.

| p | k | c | nonzero lambda=-k/c (mod p) | full W difference (mod p^3) | local labelled j=1 difference divided by p (mod p) |
|---:|---:|---:|---:|---:|---:|
| 13 | 4 | 5 | 7 | 0 | 8 |
| 19 | 10 | 10 | 18 | 0 | 5 |
| 373 | 134 | 67 | 371 | 0 | 187 |

Proof of the final nonzero column: partial_delta U_1(0) = -b*(a+c)/2 = b/2 (mod p). Its changed p^2-level local source coefficient is p*lambda*b/2, nonzero at each listed nonzero lambda. Thus both the first and second scalar digits agree for distinct source inputs, while their labelled local coefficients already disagree modulo p^2. This is an explicit observer-scoped BRC information-loss certificate, not a claim that the authentic LIFT conjecture has failed.

The adjacent program `d25_source_fiber_recoalescence_20261106.py` imports the separately published exact p^3 evaluator and jet routine, checks the displayed k,c,lambda, and independently compares complete weighted sums for all three primes.

**Open:** Prove or refute universal T1+T3=0 for p=1(mod6); derive a source-faithful compensated Theta telescope; obtain original H0/B0, [X]U mod p^2 and genuine Frobenius eta/kappa for the frozen Delta_p-R_p=0 mod p (p=13,19 mod24). No native claim/open/checkpoint or independent mathematical review is claimed for these author-side results.
