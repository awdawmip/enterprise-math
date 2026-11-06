# D25: p^3 second-jet repair of an invisible first-digit source direction

2026-11-06 | Author-side exact algebra and exact finite counterexamples | UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_EXPERIMENT.

Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen input c47e13e4aba0e006366f989d6334d443f6333ae3.

Use the three labelled source factors and W_p(v) defined in `20261106_hourly20_d25_source_tangent_first_digit_fibers.md`, now computed modulo p^3, for any prime p=6m+1>=7.

Define the *p^2-lifted* source gradient A and the *p-reduced* full source Hessian H, with weights retained:

```text
A_i  = SUM_{j<p} (6j+1)*partial_i U_j(0)         (mod p^2)
H_ik = SUM_{j<p} (6j+1)*partial_i partial_k U_j(0) (mod p)
T_i  = A_i (mod p)
```

**General theorem** (all p as above; v and delta p-local):

```text
W_p(v+delta)-W_p(v)
  = p*(A dot delta)
    + p^2*(v^T H delta + (delta^T H delta)/2)       (mod p^3).
```

Proof: Expand every binomial coefficient U_j(pv+pdelta) to total Taylor order two over the p-local rational ring; j! and 2 are p-units. The discarded terms have factor p^3. The Hessian includes all regular, one-carry and two-carry source contributions without dividing by a vanishing coefficient.

If T dot delta=0 (mod p), then A dot delta is divisible by p and a well-defined second-digit difference is:

```text
Q_p(v,delta) = (A dot delta)/p + v^T H delta
               + (delta^T H delta)/2              (mod p).
```

The division must occur after lifting A modulo p^2; replacing A by T loses the required digit.

For the original tangent v*=(-1/3,-1/2,-2/3), at each of p=13,19,373 the previously verified first-digit kernel contains delta=(1,0,1). The two independent mod-p^3 and derivative-recursion implementations give:

| p | A=(A1,A2,A3) mod p^2 | H11,H13,H33 mod p | (A dot delta)/p | v*^T H delta | (delta^T H delta)/2 | Q mod p |
|---:|---|---|---:|---:|---:|---:|
| 13 | (75,168,81) | (11,11,3) | 12 | 5 | 5 | **9** |
| 19 | (232,338,110) | (5,12,10) | 18 | 11 | 10 | **1** |
| 373 | (126122,130625,80147) | (175,299,107) | 180 | 327 | 67 | **201** |

For example the complete weighted source sums differ at p=373 by 201*373^2 modulo 373^3. Thus the first-digit scalar fiber quotient fails to preserve the *next* digit on all three exact instances. This is a scoped failure of the auxiliary source family projection, not a counterexample to native LIFT or the frozen Delta-R target.

Companion program `d25_source_second_jet_lift_20261106.py` evaluates A mod p^2 and H mod p using polynomial recurrences (including B'', without dividing by a vanishing B), and independently evaluates the entire source-deformed sum mod p^3. All 207 primes p=1(mod6), 7<=p<=3000 passed these exact checks; the delta second digit was nonzero in 207/207 finite cases. No universal nonzero statement is inferred.

**BRC source/precision accounting:** The first-digit total is not a lossless quotient for an operation that later observes the second digit. For the declared p^3 Taylor operation, retain A mod p^2, H mod p, source tangent, index/weights and carry provenance. The exact minimal repair of the native Frobenius/Delta-R interface remains open. The next portable task is a symbolic proof/counterexample of T1+T3=0 and a link between this labelled second-jet map and the original compensated Theta regular/one-carry port.
