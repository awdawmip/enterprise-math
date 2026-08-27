# Driver Review — Prime Coordinate Factor Blind p-adic GCD Bridge

Status: `REQUEST_REVISION / INVALID_RESULT_QUARANTINED / VALID_SUBTHEOREM / TASK_NOT_TERMINAL`

Task: `RS-PRIME-COORD-FACTOR-BLIND-PADIC-GCD-BRIDGE`  
Publication: `TP2-7B0534E09E4286CB5B6E`  
Scheduler-valid researcher: `EM-PCF4-AED70E`  
Candidate result: `RR-A33E88150B0DAD0B13B8`  
Driver: `EM-DVR-499907`  
Quarantine resolution: `RQ-464D1F87581CCB73B55D`

## Driver disposition

`REQUEST_REVISION`.

The mathematical fixed-public-prefix obstruction is accepted at its exact restricted scope, but the current candidate result record is structurally invalid under the active result/execution registry and therefore is not operational result authority. It is retained immutably in repository history and explicitly quarantined rather than rewritten or deleted.

The task remains nonterminal and must be redispatched under a fresh valid CLAIM.

## 1. Scheduler provenance

Issue #240 establishes `chatgpt-pcf4-20260827-1714` / `EM-PCF4-AED70E` as the valid live CLAIM for publication `TP2-7B0534E09E4286CB5B6E`.

The later `chatgpt-pcf4-20260827-1718` CLAIM was attempted while the first lease remained live and is not a valid scheduler transition. Its PR #715 / `RR-D693BD1103CCAE5F354E` may therefore be used only as disclosed supplemental mathematical evidence; its CLAIM, HANDOFF, execution record, result record, and owner lineage are not canonicalized.

## 2. Structural defects in the candidate result

The candidate `RR-A33E88150B0DAD0B13B8` cannot be accepted by the active immutable result writer/auditor.

First, it references `ER-CB5BCA1809671D892B42`, but that execution record is absent from both the scheduler-valid owner PR and current `main`.

Second, the active execution-ID rule hashes

`task_id, publication_id, claim_id, researcher_id, execution_branch`

with NUL separators. Re-deriving from the valid CLAIM fields gives

`ER-BB2F7D1AFE3EF5B04433`,

not the execution ID stored in the candidate result.

Third, `terminal_verdict = BRIDGE_NOT_CLOSED` is outside the active V1 terminal-verdict enum.

Fourth, `independence_status = TWO_INDEPENDENT_EXACT_INTEGER_CHECKERS` is outside the active V1 independence enum.

Fifth, even if the stored `ER-CB...` were treated as an execution ID, the active result-ID rule applied to that execution ID, the frozen return blob, and the stored owner head yields `RR-B09D2288AF316A9364D3`, not `RR-A33E88150B0DAD0B13B8`. Using the correctly re-derived execution ID yields `RR-598C8B95A60BC9176F2B`.

These are record-construction defects, not mathematical objections. The record is therefore quarantined by `RQ-464D1F87581CCB73B55D` and excluded from operational result truth while its historical bytes remain preserved.

## 3. Mathematical subtheorem accepted from the valid route

Let

\[
A_n=\frac{(2n)!(3n)!}{(n!)^5}=\binom{2n}{n}^2\binom{3n}{n}
\]

and

\[
F_L=\sum_{0\le n<L}(6n+1)A_n216^{L-1-n}.
\]

For `gcd(N,6)=1`, the public-prefix construction satisfies exactly

\[
\gcd(G_N(L),N)=\gcd(F_L,N).
\]

Hence every fixed finite N-independent public prefix-seed family is only a finite family of precommitted integer gcd probes. Its union of prime supports is finite, so infinitely many semiprimes avoid that support and give no split.

The support-size bound and the conditional Lucas-block synchronization statements are retained only at their stated scope.

Therefore

`PUBLIC_PREFIX_FIXED_INTEGER_SUPPORT_NO_GO`

is accepted as a restricted exact theorem. It does not close all N-dependent observables permitted by PCF4.

## 4. Stronger compatible N-dependent route harvested from the duplicate race

The supplemental PR #715 route uses `A_s` itself as a gcd kernel and chooses seeds from `N` only.

For prime `r>3` and `0<=s<r`, Legendre gives

\[
v_r(A_s)=\left\lfloor\frac{2s}{r}\right\rfloor+\left\lfloor\frac{3s}{r}\right\rfloor,
\]

so the first divisibility wall below `r` is exactly `3s>r`.

For `N=pq`, `3<p<q`, let `s_*` be the first dyadic seed with `3s_*>p`. Then

\[
\frac{3s_*}{2}<p<3s_*<2p.
\]

If `q>3s_*`, `gcd(A_{s_*},N)=p`. If `q<3s_*`, the response synchronizes to `N` and necessarily `q<2p`.

In the synchronized case let

\[
t=\left\lfloor\frac{\operatorname{isqrt}(N)}3\right\rfloor.
\]

One of `A_t` or `A_{t+1}` has its divisibility wall strictly between `p` and `q`, and therefore its gcd with `N` is `p`. The exact recurrence is

\[
A_{k+1}=A_k\frac{6(2k+1)(3k+1)(3k+2)}{(k+1)^3},
\]

with exact integer division.

Driver-side independent exact-integer replay over every pair of distinct odd primes below 2000 covered 45,451 semiprimes with zero failures; 9,969 entered the square-root-third fallback and the maximum observed trace length was 13. This regression supports, but does not replace, the valuation proof.

The route is compatible with the fixed-public-prefix no-go because it is N-dependent before the final gcd.

## 5. Required revision

The next valid owner must:

1. take a fresh valid CLAIM for the current publication;
2. materialize the execution intent through the active execution-record writer rather than hand-constructing IDs;
3. preserve `PUBLIC_PREFIX_FIXED_INTEGER_SUPPORT_NO_GO` as a restricted theorem;
4. incorporate or independently reconstruct the N-dependent `A_s` valuation-wall splitter;
5. keep the `gcd(N,6)` precheck for the `p=3` case;
6. freeze the dyadic synchronization and `floor(isqrt(N)/3), +1` fallback proof;
7. freeze a new immutable result through the active result writer with allowed enum values and writer-derived ID;
8. preserve `GCD_EXTRACTOR_PROVED != FACTORIZATION_SPEEDUP_PROVED`;
9. state explicitly that the largest forced seed is `Theta(p)` in the balanced case, so no polynomial-time or sub-square-root factorization theorem follows;
10. cite PR #715 only as supplemental method-harvest, never as a canonical scheduler HANDOFF.

## Control boundary

No Working Truth, Foundation authority, canonical theorem promotion, or factoring-speedup claim is granted by this review.

Operational state after this review: `RETURN_TO_EXECUTION / NEEDS_DISPATCH`.
