# D25: weighted reversed 4F3 has an exact nonzero p² terminal source

Date 2026-11-05. TASK_RESEARCH author-side; exact algebraic result plus finite integer checks, UNREVIEWED / NOT_ADMITTED / NATIVE_NOT_EXECUTED.
Logical conversation: `chatgpt-research-onhour-enterprise-math-20260923` (NOT maintenance).
Mother task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; immutable scientific source pin `c47e13e4aba0e006366f989d6334d443f6333ae3`.

## Consumed results; new unfinished question

The prior research note `20261105_onhour_d25_reversed_shell_homogeneous_4f3.md` proved for p=6n+1>=7:
`T_A=-2 U_p (3 theta+2)G_n(1/2) mod p`,
where U_p is the nonzero ORIGINAL last upper-shell term, G_n(t)=sum_{k=0}^{n-1}g_k t^k and
`g_k=(1)_k(5/6)_k(7/6)_k/(3/2)_k^3`, theta=t*d/dt.
The prior unweighted G_n solves a homogeneous fourth-order equation MOD p only. This unit determines the more relevant weighted observer's behavior at the next p-adic digit. Do not lift that shell transport beyond mod p without a separate proof.

## New exact finite-truncation theorem

Set H_n=(3 theta+2)G_n and define noncommutative differential operators (theta*t=t*(theta+1)):

```
A(theta)=theta*(theta+1/2)^3
B(theta)=(theta+1)^2*(theta+5/6)*(theta+7/6)
D_obs=(3*theta-1)*A(theta)-t*(3*theta+5)*B(theta)
```

For all integers n>=1 there is an **exact characteristic-zero rational polynomial identity**:

```
D_obs H_n(t)
= -(3*n+2)*(3*n-1)*n^2*(n-1/6)*(n+1/6)*g_(n-1)*t^n .
```

Proof: g_k/g_(k-1)=(2/9)*k*(6k-1)*(6k+1)/(2k+1)^3 for 1<=k<n. Put h_k=(3k+2)g_k. The coefficient of t^k, 1<=k<n, is
`(3k-1)k(k+1/2)^3 h_k - (3k+2)k²(k-1/6)(k+1/6) h_(k-1)`, which is identically zero. The constant term is zero. The ONLY terminal t^n coefficient is `-(3n+2)n²(n-1/6)(n+1/6)h_(n-1)`, as claimed. There are no terms of greater degree. QED.

For prime p=6n+1>=7 the coefficients g_k through n-1 are p-integral, and g_(n-1) is a p-unit. Using n+1/6=p/6 and n=-1/6 modulo p, the exact source reduces to

```
D_obs H_n(t) = -p*g_(n-1)/288 * t^n       (mod p²)
D_obs H_n(1/2) = -p*g_(n-1)/(288*2^n)   (mod p²).
```

Both terminal values have EXACT p-adic valuation 1. In particular, the weighted reversed 4F3 observer's MOD-p homogeneous equation **does not extend homogeneously to mod p²**. This is a new nonzero signed terminal source, NOT a counterexample to the frozen LIFT theorem.

## Independent integer validation and BRC observer

Executed Python standard-library integer checker `d25_weighted_4f3_p2_terminal_lift_20261105.py` computes original rational g recurrence modulo p², all interior polynomial coefficients, terminal, evaluation t=1/2; no floats or hidden coefficient drops. The coefficient identity is verified via integer scaling:

`72*[t^k]D_obs H_n = 9(3k-1)k(2k+1)^3 h_k -2(3k+2)k²(6k-1)(6k+1) h_(k-1)`.

All 611 primes p=6n+1 <=10000 pass, failures 0. (p, terminal mod p², terminal at 1/2)=(7,42,21),(13,156,39),(19,266,304),(139,17097,973),(373,98472,138010). Proof is the recurrence, not extrapolation. BRC reuse: COMPOSE_APPLIED; carrier includes 216 source, original index, valuation-two shell, nonzero signed U_p, derivative jet and t=1/2 evaluation. The new terminal cannot be erased by unweighted homogeneous reduction or scalar norm.

## Limits, original experiment, next exact action

Frozen mother objective remains OPEN: prove/disprove `Delta_p-R_p=0 mod p` for p=13,19 mod24, equivalently original W_p=p mod p³ under already sourced UR/port alignment. This lemma DOES NOT prove it, does not automatically lift T_A's mod-p factor, and is NOT the original H0/B0 experiment.

At p373 original fixed H0/B0 divided-power `[X]U mod 139129`, actual module rank, semilinear Frobenius/eta, signed odd Hesse-Green, same-definition kappa/Delta-R and independent replication remain NOT_EXECUTED / PENDING_OWNER under existing support issue #1559. Ordinary Hesse norm 122102 is CONDITIONAL only.

Next: seek a terminating adjoint/WZ evaluation of the *weighted* H_n(1/2) in which the above nonzero p² source and original unit U_p remain visible. Pair that with the independently sourced 216 half-sum p³ correction. In parallel, only an authorized original-class native executor may fulfill #1559.

Source operational continuity: fresh Source continuation `onhour11-20261105-0358-current-cont` SUCCEEDED with execution_authorized=false. Research-only service session `MCP-491afa3ba2b94ec9b900ed3df6e345a3`, researcher `EM-ENTERPRISE-4B19D8`, activity `RA-C67296253D0A2C07E11842EF` registered; its native Task CLAIM/open/run/Source checkpoint/Result have NOT been established. Prior inherited Source results and older staging have distinct authorship and are not silently admitted.
