# D25/LIFT — second-digit normalization fiber and native comparator identifiability

2026-10-26 · TASK_RESEARCH · own logical conversation `chatgpt-research-onhour-enterprise-math-20260923`, **not** CONTROL_PLANE_MAINTENANCE. Original Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific pin **`c47e13e4aba0e006366f989d6334d443f6333ae3`**, unchanged.

**Evidence status: AUTHOR-DERIVED / EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_BENCHMARK / NOT_SOURCE_CHECKPOINT.** Consumes, without recrediting, the previously Source-published author Hilbert–90 rank-one classification, the original Hesse coefficient source, the author raw-Frobenius slope/precision no-go, the frozen signed cutoff and completed UR/JT0/CM0.

## New precise statement: a first-digit normalizer cannot identify a second-digit comparator

For any odd prime p, let q=p², let R₂=(Z/q)[T]/(T²−2), and put sigma(T)=−T and N(x)=x sigma(x). **Only if** native original-class H0/B0 is independently proved to be a free rank-one sigma-semilinear module and source authenticates the coefficient beta=eta*alpha can its square be compared with N(eta)N(alpha).

The already proved **basis change** beta↦beta sigma(z)/z has norm one, hence N(beta) is basis-gauge invariant. It does **not** provide freedom to change its norm.

A *different* parameter is a multiplicative **normalization** eta. Suppose source determines eta only modulo p and imposes no condition on its order-p lift. Fix one possible unit lift eta0 and, for every c∈F_p, form the equally first-digit-compatible scalar lift eta_c=eta0(1+pc). Exactly in R₂,

N(eta_c alpha)=K(1+2pc) mod p², where K=N(eta0)N(alpha).

If alpha and eta0 are units, K mod p is nonzero, so 2K is invertible modulo p. The map c↦K(1+2pc) is therefore a **bijection onto all p second digits having the fixed first digit K mod p**. Thus even an exact measured native normalized square modulo p² cannot meaningfully pass or fail the *second digit* of the suggested comparison while eta remains free at order p. This is an exact conditional **identifiability obstruction**, not a LIFT counterexample.

**Condition boundary.** A source-fixed eta mod p², a separately calibrated N(eta) mod p², or an authenticated norm-one restriction removes this particular ambiguity. Unfixed normalizers cannot be treated as norm-one basis gauges. Moreover, no rank-one model is asserted for the still-unmeasured native H0/B0 object. This refines (but does not re-prove) the prior raw-vs-normalized slope warning.

## Exact p=373 full-fiber witness

Reuse the previously recorded **ordinary/non-native** Hesse source:
alpha=92060+21788T mod139129, N(alpha)=122102 mod139129, N(alpha)=131 mod373 (unit).

Choose eta0=1 and eta1=1+373·187=69752. Both reduce to 1 mod373, but
- N(eta0)=1 and N(eta1)=374 mod139129;
- N(eta0 alpha)=122102 and N(eta1 alpha)=31836 mod139129;
- both predictions have the *same first digit* 131 mod373;
- their distinct second digits differ by 48863=373·131 mod139129.

Exact Python standard-library check performed on all 373 scalar lifts eta_c=1+373c, c=0,…,372: **373 distinct possible second digits, with every result reducing to 131 mod373**. Independent executable local checker delivered as `d25_eta_second_digit_identifiability_check_20261026.py`; the exhaustive finite check supports the elementary all-p proof, not native execution. Minimal reproduced formula:

```python
p=373; q=p*p
K=(92060**2-2*21788**2)%q
assert K==122102 and K%p==131
fiber={(K*(1+p*c)**2)%q for c in range(p)}
assert len(fiber)==p and fiber=={131+p*d for d in range(p)}
assert (K*(1+p*187)**2)%q==31836
```

## Immediate genuine-benchmark consequence

The unchanged hard target is native original-class fixed H0/B0 divided-power [X]U modulo 373², module rank, semilinear direction, operator normalization, original signed odd Green/Hesse ports, kappa and Delta_p−R_p. A proposed comparison with N(eta)*122102 must document **eta or its norm at full p² precision** (or an authenticated invariant normalization condition), *after* checking rank and operator type. If eta is available only modulo p with the above independent lift freedom, classify the second digit as `NORMALIZATION_SECOND_DIGIT_UNDETERMINED`, not PASS/REFUTED. For raw crystalline F²/p a separate previously proved raw p³ precision bound applies. Neither result replaces the frozen [X]U benchmark.

BRC/Enterprise-coordinate audit `COMPOSE_APPLIED`: retain ordered operator/normalization/basis sources, p-adic valuation and both digits, sigma and signed odd branch. The norm quotient erases the odd observer and an unknown independent eta lift. This external quadratic ring is not the native P000 X6 space or a complete native 3D slice.

## Continuation and explicit noncompletion

Mother: prove/refute D25/JT2 Delta_p−R_p=0 for both 13,19 mod24. Highest **Source** evidence stays the separately authenticated pre-existing continuation; this new GitHub author note does not change its Source checkpoint, ownership or formal Result. Do not re-run accepted UR/CM0/JT0, original signed cutoff, Clausen jets, rank-one Hilbert–90, previous slope proof, finite prime scan, or another lane's p733 work. Still missing the **real** original H0/B0 native benchmark, signed kappa and independent review. Support issue #1559 remains PENDING_OWNER / NATIVE_NOT_EXECUTED. Next exact action: source-authenticated original-class evaluator at p373 with two-digit eta, rank and normalized type, then verify real kappa/Delta−R. No executor identified.

This lane's native session/CLAIM/open run were not authenticated in the current client. Original request `research-onhour-20261026-1129-dispatch-v1` returned `CONTROL_REQUEST_NOT_FOUND`; read-only exact task query returned `CONTROL_QUOTA`; Site write relay is disabled. No repeated mutation, no assumed claim or formal checkpoint and no changes to scheduler/notifications.
