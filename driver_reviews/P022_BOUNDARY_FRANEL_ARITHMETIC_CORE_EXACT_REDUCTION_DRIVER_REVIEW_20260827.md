# Driver Review — P022 Boundary Franel Arithmetic-Core Exact Reduction

Status: `DRIVER_FINAL / ACCEPTED_WITH_NARROWING / EXACT_REDUCTION / P022_PARENT_OPEN / NO_PROMOTION`

Date: `2026-08-27`

Driver-ID: `EM-DRIVER-01 / CONTROL_PLANE`

Task: `RS-P022-OBSERVATION-HISTORY`

Publication: `TP2-DE338F269CA11E9BC01B`

Execution: `ER-E7C2C9107B238D009110`

Researcher-ID: `EM-P022OH-540040`

Result: `RR-8323CFDCB99F7832F51F`

Source result PR: `#712`

Current-main integration: `bbdea1ae2858b861ce0d8e2c1596e1aacfe972c0`

## 1. Final disposition

`DRIVER_DISPOSITION = ACCEPTED`.

`HARD_TARGET = MET_BY_EXACT_REDUCTION`.

`RESULT_CLASS = EXACT_BOUNDARY_REDUCTION / FIXED_TERMINATING_KERNEL / RESULT_ONLY`.

`P022_q=3r-1_BOUNDARY = EXACTLY_REDUCED_NOT_PROVED_NONVANISHING`.

`FOUNDATION_MUTATION = NONE`.

`WORKING_TRUTH_PROMOTION = NONE`.

`TOOLBOX_MUTATION = NONE`.

The taskbook explicitly allowed a task-terminal result when the boundary divisibility was reduced to one explicit residual identity after the elementary and valuation routes were exhausted. That terminal condition is met. The Driver does not accept an all-parameter nonvanishing theorem, an all-P022 observability theorem, or a claim that all hypergeometric transformation machinery has been exhausted.

## 2. Accepted exact reduction

Use the Franel convention

`F_n = sum_{k=0}^n C(n,k)^3`.

At the first dangerous reflection boundary, let `r` be a nontrivial twin center and let `q=3r-1` be prime. A nontrivial twin center is divisible by three, and primality of `q` forces `r` even. Hence

`r=6m`, `q=18m-1`,

with twin boundaries `12m-1` and `12m+1`.

MacMahon's exact Franel expansion gives

`F_(6m) = sum_{k=0}^{3m} 2^(6m-2k) (6m+k)! / ((6m-2k)! (k!)^3)`.

After division by the invertible factor `2^(6m)`, consecutive summands have ratio

`(6m+k+1)(6m-2k)(6m-2k-1) / (4(k+1)^3)`.

Modulo `q=18m-1`, this becomes

`(k-1/6)(k+1/3)(k+4/3)/(k+1)^3`,

which is exactly the ratio of the terminating series

`3F2(-3m,6m,6m+1;1,1;1)`.

Therefore, with

`S_m = sum_{k=0}^{3m} (-1)^k C(3m,k) C(6m+k-1,k) C(6m+k,k)`,

the following equivalence is accepted:

`q | F_(6m)  iff  S_m = 0 (mod q)`.

This is a symbolic equivalence, not an inference from the finite census.

## 3. Accepted fixed-parameter residual

Reverse the terminating sum with `n=3m`, `a=6m`, and `b=6m+1`. The prefactor

`(-1)^(3m) (6m)_(3m) (6m+1)_(3m) / ((3m)!)^2`

is a `q`-unit. Modulo `q`, the remaining parameters satisfy

`-3m = -1/6`, `1-9m = 1/2`, `-9m = -1/2`.

Thus the unresolved divisibility is reduced to the fixed rational-parameter truncated kernel

`R_m(q) = sum_{j=0}^{3m} (-1/6)_j^3 / ((1/2)_j (-1/2)_j j!)`.

The sole arithmetic residue is:

`PROVE_OR_REFUTE R_m(q) != 0 (mod q)`

for the admissible P022 constellation

`q=18m-1`, `12m-1 prime`, `12m+1 prime`,

with complete-escape relevance restricted to `q=17 or 35 (mod 72)`.

## 4. Valuation and transformation audit

For `0<=k<=3m`, the factors occurring in the terminating kernel are bounded by `9m<18m-1=q`. Hence every numerator and denominator factor is nonzero modulo `q`, and every summand is a `q`-adic unit.

Accordingly:

- there is no termwise valuation obstruction;
- there is no unique minimum valuation;
- there is no valuation-positive tail that may be discarded;
- the remaining issue is genuine finite-field cancellation.

The frozen checker also correctly computes a 12-type orbit for the Weber–Erdelyi transformation while keeping the original terminating parameter `-3m` distinguished. That fixed-termination orbit has no direct numerator/denominator cancellation and no Saalschütz-balanced member.

The narrowing is binding: this 12-type calculation does **not** establish exhaustion of every possible hypergeometric, finite-field, contiguous, modular, Cartier, or re-anchored terminating transformation. Only the elementary valuation route and the declared fixed-termination Weber–Erdelyi subroute are closed.

## 5. Independent finite evidence

The Driver independently reconstructed the modular Franel sum and terminating kernel and reproduced the frozen census through `q<50,000`:

- admissible twin-boundary candidates: `90`;
- residue counts modulo `72`: `17:22`, `35:25`, `53:28`, `71:15`;
- candidates in complete-escape survivor classes `17,35`: `47`;
- Franel zeros among all `90`: `0`;
- Franel zeros among the `47` survivors: `0`;
- kernel/Franel congruence mismatches: `0`.

The control `149 | F_50` is also correct and blocks a mod-3-only nonvanishing argument.

All finite results remain `REGRESSION_AND_FALSIFICATION_ONLY`. They do not prove the all-`m` kernel nonvanishing statement.

## 6. Method harvest and routing consequence

Method harvest:

`EXACT_TERMINATING_HYPERGEOMETRIC_REDUCTION / RESULT_ONLY`.

The reusable payload is the conversion of the first dangerous P022 reflection boundary into one fixed-parameter finite-field cancellation kernel. It is not promoted to the general toolbox because no general nonvanishing theorem or reusable algorithmic interface is supplied.

No new finite-scan successor is authorized.

A later active P022 replay publication already exists:

`TP2-2346F5D3E731ED56DB0A`.

The fixed `R_m(q)` kernel is routed as a typed input to that live P022 owner line. A duplicate successor must not be published while that line remains active. After its result is reviewed, a distinct successor is justified only if the fixed-kernel nonvanishing remains the smallest unresolved unit and the successor is restricted to finite-field hypergeometric/Jacobi-sum or modular/Cartier structure rather than a larger census.

## 7. Integration boundary

PR `#712` contained only the execution/result records, frozen return, deterministic checker, and machine-readable certificate. It was merged into current `main` as

`bbdea1ae2858b861ce0d8e2c1596e1aacfe972c0`.

No CI-success claim is made. Acceptance rests on the exact algebraic derivation, source audit, independent modular recomputation, and explicit preservation of the unresolved all-parameter kernel.

## 8. Final freeze

`RR-8323CFDCB99F7832F51F = ACCEPTED_WITH_NARROWING`.

`TP2-DE338F269CA11E9BC01B = EXACT_REDUCTION_TERMINAL`.

`P022_BOUNDARY_FRANEL_ESCAPE_CORE_HARD_TARGET = MET_BY_EXACT_REDUCTION`.

`P022_FIXED_KERNEL_NONVANISHING = OPEN`.

`P022_PARENT_OBJECTIVE = OPEN`.

`FINITE_CUTOFF_SUCCESSOR = FORBIDDEN`.

`NEXT_CONTROL_PLANE_ACTION = CONTINUE_REVIEW_QUEUE; REVIEW THE NEXT VALID UNREVIEWED HANDOFF`.
