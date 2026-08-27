# Driver Review — Prime Coordinate Factor Blind p-adic GCD Bridge

Status: `REQUEST_REVISION / PROVENANCE_DEFECT / VALID SUBTHEOREM / TASK NOT TERMINAL`

Reviewed candidate result: `RR-A33E88150B0DAD0B13B8`  
Task: `RS-PRIME-COORD-FACTOR-BLIND-PADIC-GCD-BRIDGE`  
Publication: `TP2-7B0534E09E4286CB5B6E`  
Researcher: `EM-PCF4-AED70E`  
Driver: `EM-DVR-499907`

## Disposition

`REQUEST_REVISION`.

The scheduler-valid route contains a mathematically sound restricted obstruction, but its current result package is not admissible for canonical result registration and its task-level verdict `BRIDGE_NOT_CLOSED` is not accepted as final. The valid owner must repair execution provenance and freeze a new immutable result. The fixed-public-prefix obstruction is retained as a valid exact subtheorem; a concurrently produced scheduler-nonoperational route supplies stronger compatible N-dependent mathematics that should be harvested without validating its duplicate CLAIM.

## 1. Scheduler provenance ruling

Issue #240 ordering makes `chatgpt-pcf4-20260827-1714` / `EM-PCF4-AED70E` the valid live CLAIM. The later `chatgpt-pcf4-20260827-1718` CLAIM occurred while the first lease was live and is not a valid scheduler transition. Its later HANDOFF is likewise nonoperational.

Therefore PR #717 is the only scheduler-valid owner route. PR #715 may be used only as disclosed supplemental mathematical evidence. This review does not validate PR #715's CLAIM, HANDOFF, execution record, result record, or owner lineage.

## 2. Canonical-registration defect in PR #717

PR #717's candidate result `RR-A33E88150B0DAD0B13B8` references execution record

`ER-CB5BCA1809671D892B42`,

but that record is absent both from current `main` and from PR #717. More importantly, under the active execution-record identity rule

`ER- + SHA256(task_id || NUL || publication_id || NUL || claim_id || NUL || researcher_id || NUL || execution_branch)[:20].upper()`,

the scheduler-valid CLAIM fields deterministically produce

`ER-BB2F7D1AFE3EF5B04433`,

not the ID named by the candidate result.

Thus the existing result record cannot be admitted to the canonical result registry by merely adding a missing file. The valid owner must materialize the correct execution intent and issue a new immutable result ID that references it. `RR-A33E88150B0DAD0B13B8` must not be rewritten or retroactively normalized.

## 3. What is accepted mathematically from the valid route

Let

\[
A_n=\frac{(2n)!(3n)!}{(n!)^5}=\binom{2n}{n}^2\binom{3n}{n},
\]

and for a public prefix length `L` define

\[
F_L=\sum_{0\le n<L}(6n+1)A_n216^{L-1-n}.
\]

For `gcd(N,6)=1`, PR #717 proves exactly

\[
\gcd(G_N(L),N)=\gcd(F_L,N).
\]

Consequently every fixed finite N-independent public prefix-seed family has only finite precommitted prime support and fails on infinitely many semiprimes. The size/support estimate for `F_L` is a legitimate quantitative strengthening of this restricted no-go. The Lucas block factorization and synchronization statements are retained only at their explicitly conditional scope.

This closes

`PUBLIC_PREFIX_FIXED_INTEGER_SUPPORT_NO_GO`,

not the full class of N-dependent observables allowed by the task.

## 4. Stronger compatible N-dependent splitter harvested from the duplicate race

The original task permits a deterministic mechanism built from `N` and public parameters; it does not require the seed schedule to be N-independent. The supplemental PR #715 route uses `A_s` itself as the gcd kernel and chooses seeds from `N` alone.

For every prime `r>3` and `0<=s<r`, Legendre's formula gives

\[
v_r(A_s)=\left\lfloor\frac{2s}{r}\right\rfloor+
         \left\lfloor\frac{3s}{r}\right\rfloor.
\]

Hence the first divisibility wall below `r` is exactly `3s>r`.

For `N=pq`, `3<p<q`, let `s_*` be the first dyadic seed satisfying `3s_*>p`. Minimality gives

\[
\frac{3s_*}{2}<p<3s_*<2p,\qquad s_*<p<q.
\]

At `s_*`:

- if `q>3s_*`, then `gcd(A_{s_*},N)=p`;
- if `q<3s_*`, then `gcd(A_{s_*},N)=N`, and synchronization forces `q<2p`.

In the synchronized case put

\[
t=\left\lfloor\frac{\operatorname{isqrt}(N)}3\right\rfloor.
\]

If `3t>p`, then `p<3t<sqrt(N)<q`, hence `gcd(A_t,N)=p`.

If `3t<p`, then `3(t+1)>sqrt(N)>p`. The least multiple of 3 above `sqrt(pq)` is still below `q`: if `q≡1 (mod 3)`, use `p<=q-2` and `sqrt(q(q-2))<q-1`; if `q≡2 (mod 3)`, equality `p=q-2` would make `p>3` divisible by 3, so `p<=q-4` and `sqrt(q(q-4))<q-2`. Thus

\[
p<3(t+1)<q,
\]

and `gcd(A_{t+1},N)=p`.

The exact recurrence is

\[
A_{k+1}=A_k\frac{6(2k+1)(3k+1)(3k+2)}{(k+1)^3},
\]

with exact integer division. The coefficient is 6.

Driver-side independent exact-integer replay over every pair of distinct odd primes below 2000 covered 45,451 semiprimes with 0 failures; 9,969 cases entered the square-root-third fallback and the maximum observed trace length was 13. This regression is supporting evidence only; the preceding valuation argument supplies the universal proof.

## 5. Required revision under the valid owner lineage

The valid owner should now:

1. materialize the scheduler-valid execution intent for `chatgpt-pcf4-20260827-1714` with deterministic ID `ER-BB2F7D1AFE3EF5B04433`;
2. preserve the fixed-public-prefix no-go as a restricted theorem;
3. incorporate or independently reconstruct the N-dependent `A_s` valuation-wall splitter;
4. keep the public precheck `gcd(N,6)` for the `p=3` case;
5. freeze the dyadic synchronization theorem and `floor(isqrt(N)/3), +1` fallback proof;
6. issue a new immutable result ID referencing the correct execution record, without rewriting `RR-A33E88150B0DAD0B13B8`;
7. preserve the boundary `GCD_EXTRACTOR_PROVED != FACTORIZATION_SPEEDUP_PROVED`;
8. state the elementary materialization cost explicitly: the largest forced seed is `Theta(p)` in the balanced case, so the present theorem is not a polynomial-time or sub-square-root factoring result;
9. cite PR #715 only as supplemental method-harvest, never as a canonical scheduler HANDOFF.

## 6. Control boundary

This review grants no Working Truth, Foundation authority, canonical theorem promotion, or factoring-speedup claim.

The task remains nonterminal and returns to the valid owner for revision. The only accepted closure at this checkpoint is `PUBLIC_PREFIX_FIXED_INTEGER_SUPPORT_NO_GO`; PCF4 task-terminal control waits for a provenance-correct new result carrying the stronger N-dependent theorem.
