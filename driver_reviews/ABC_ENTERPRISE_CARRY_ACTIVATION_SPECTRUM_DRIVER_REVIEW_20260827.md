# Driver Review — ABC Enterprise Carry-Activation Spectrum

Status: `DRIVER_FINAL / ACCEPTED / EXACT_PRIME_POWER_CARRY_OBSTRUCTION / RESULT_ONLY`

Date: `2026-08-27`

Driver-ID: `EM-FREE-C19420 / CONTROL_PLANE`

Task: `RS-ABC-ENTERPRISE-CARRY-ACTIVATION-SPECTRUM`

Publication: `TP2-216D433F311CA5D7AFAC`

Execution: `ER-5AABB74CE655D57893D6`

Researcher-ID: `EM-ABC2-1C96B2`

Result: `RR-E623A0364F580D6D1C0F`

Source PR: `#714`

Current-main integration: `15a1deddb2c5c1c53d61432f4f859370812d6c79`

## 1. Final disposition

`DRIVER_DISPOSITION = ACCEPTED`.

`HARD_TARGET = MET_BY_EXACT_OBSTRUCTION`.

`RESULT_CLASS = EXACT_INFINITE_OBSTRUCTION / RESULT_ONLY`.

`FOUNDATION_MUTATION = NONE`.

`TOOL_PROMOTION = NONE`.

`SUCCESSOR_TASK = NONE_FROM_ABC2`.

The Driver accepts the theorem-level prime-power obstruction. The finite checker is regression only and is not load-bearing.

## 2. Accepted theorem

For every prime `p` and every integer `k>=1`, put `P=p^k` and take the primitive abc triple

`(a,b,c)=(1,P-1,P)`.

For the task-frozen carry statistic

`h_p(n)=v_p(binomial(n*c,n*a))-v_p(c)`, 

the result proves

`h_p(n)=0` for every `1<=n<=P`,

while

`h_p(P+1)=k`.

Equivalently,

`tau_p=P+1=p^k+1=c+1`,

and therefore every cumulative activation energy restricted to a window `W<=P` is zero:

`E_p(W)=0`.

This is an infinite exact family, not a bounded-search pattern.

## 3. Consequence boundary

The theorem refutes every unqualified claim that each support prime must contribute positive carry activation within `n<=c` for all primitive abc triples.

It also refutes every per-support-prime window `W(p)` bounded independently of `v_p(c)`, including any fixed-power window `W(p)=p^A`: choosing `k>A` gives `W(p)<p^k=tau_p-1`.

The obstruction does **not** refute:

- aggregate energy over several support primes;
- genuinely interior- or balance-conditioned activation theorems;
- windows with explicit dependence on the support exponent `v_p(c)`;
- other observables not forced to pay locally prime-by-prime.

Any future ABC energy theorem must state one of those additional structures explicitly rather than silently reusing the killed local-payment claim.

## 4. Deduplication with ABC4

ABC4's family `(1,p-1,p)` is exactly the `k=1` specialization of this theorem. Accordingly, the ABC4 carry observation is retained only as bounded/adversarial regression evidence and receives no separate theorem-frontier promotion.

## 5. CI and evidence boundary

The original and refreshed PR runs do not justify a claim that the whole repository quality surface is green. The reference-integrity failure is inherited from the pre-existing P022 publication fork. Full-repository Python quality encounters pre-existing `FoundationBackflowValidationTests` errors and later hosted-runner shutdown/cancellation. No ABC2-specific failure was observed before cancellation.

The accepted mathematical conclusion rests on the exact valuation proof frozen in the return plus the task-local exact Legendre checker. The checker exercises finite instances only and does not replace the universal argument.

## 6. Final freeze

`RS-ABC-ENTERPRISE-CARRY-ACTIVATION-SPECTRUM = TERMINAL / ACCEPTED`.

`RR-E623A0364F580D6D1C0F = ACCEPTED`.

`DESTINATION = RESULT_ONLY`.

`UNQUALIFIED_PER_SUPPORT_PRIME_SHORT_WINDOW_ACTIVATION = REFUTED`.

`EXPONENT_INDEPENDENT_WINDOW_FAMILY = REFUTED`.

`AGGREGATE_OR_CONDITIONED_ENERGY_FRONTIER = OPEN_BUT_NOT_AUTO_DISPATCHED_FROM_ABC2`.

`FINITE_SCAN_SUCCESSOR = NONE`.
