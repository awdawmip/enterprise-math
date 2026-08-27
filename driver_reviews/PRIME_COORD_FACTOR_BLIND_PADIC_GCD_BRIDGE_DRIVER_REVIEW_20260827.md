# Driver Review — Prime Coordinate Factor Blind p-adic GCD Bridge

Status: `REQUEST_REVISION / VALID SUBTHEOREM / TASK NOT TERMINAL`

Reviewed result: `RR-A33E88150B0DAD0B13B8`  
Task: `RS-PRIME-COORD-FACTOR-BLIND-PADIC-GCD-BRIDGE`  
Publication: `TP2-7B0534E09E4286CB5B6E`  
Researcher: `EM-PCF4-AED70E`  
Driver: `EM-DVR-499907`

## Disposition

`REQUEST_REVISION`.

The scheduler-valid result is mathematically sound on the scope it actually proves, but its task-level verdict `BRIDGE_NOT_CLOSED` is not accepted as final. The fixed-public-prefix obstruction is retained as a valid exact subtheorem; the broader PCF4 task must remain nonterminal because a concurrently produced, scheduler-nonoperational route exhibits an explicit N-dependent splitter that lies outside the no-go class and survives Driver pressure review.

## 1. Provenance ruling

Issue #240 ordering makes `chatgpt-pcf4-20260827-1714` / `EM-PCF4-AED70E` the valid live CLAIM. The later `chatgpt-pcf4-20260827-1718` CLAIM occurred while the first lease was live and is not a valid scheduler transition. Therefore `RR-A33E88150B0DAD0B13B8` is the only result under review for control-plane purposes.

The later Draft PR #715 / `RR-D693BD1103CCAE5F354E` is used only as disclosed supplemental mathematical evidence. This review does not validate its CLAIM, HANDOFF, execution record, result record, or owner lineage.

## 2. What is accepted from RR-A33E88150B0DAD0B13B8

The following restricted theorem is accepted:

For
\[
F_L=\sum_{0\le n<L}(6n+1)A_n216^{L-1-n},
\qquad
A_n=\binom{2n}{n}^2\binom{3n}{n},
\]
and `gcd(N,6)=1`, the public-prefix construction reduces exactly to
\[
\gcd(G_N(L),N)=\gcd(F_L,N).
\]

Consequently every fixed finite N-independent prefix-seed family has only finite precommitted prime support and fails on infinitely many semiprimes. The size/support estimate for `F_L` is a legitimate quantitative strengthening of this restricted no-go. The Lucas block factorization is also retained only at its stated conditional scope.

This closes `PUBLIC_PREFIX_FIXED_INTEGER_SUPPORT_NO_GO`; it does not close all N-dependent observables.

## 3. Why the task-level verdict must be revised

The original task hard target permits a deterministic mechanism built from `N` and public parameters. It does not require the seed schedule to be N-independent.

The supplemental route supplies
\[
A_s=\frac{(2s)!(3s)!}{(s!)^5}
\]
itself as the gcd kernel and uses an N-dependent deterministic stopping/fallback rule. This is outside the fixed-public-prefix class proved impossible by the reviewed result.

For every prime `r>3` and `0<=s<r`, Legendre gives exactly
\[
v_r(A_s)=\left\lfloor\frac{2s}{r}\right\rfloor+
         \left\lfloor\frac{3s}{r}\right\rfloor.
\]
Hence the first divisibility wall below `r` is `3s>r`.

For `N=pq`, `3<p<q`, let `s_*` be the first dyadic seed with `3s_*>p`. Then
\[
\frac{3s_*}{2}<p<3s_*<2p,\qquad s_*<p<q.
\]
At `s_*`, either `q>3s_*`, in which case `gcd(A_{s_*},N)=p`, or `q<3s_*`, in which case the response is `N` and necessarily `q<2p`.

In the synchronized case put
\[
t=\left\lfloor\frac{\sqrt N}{3}\right\rfloor.
\]
If `3t>p`, then `p<3t<sqrt(N)<q` and `gcd(A_t,N)=p`. If `3t<p`, then `3(t+1)>sqrt(N)>p`. The least multiple of 3 above `sqrt(pq)` is still below `q`: for `q=1 mod 3`, use `p<=q-2` and `sqrt(q(q-2))<q-1`; for `q=2 mod 3`, `p=q-2` is impossible for `p>3`, so `p<=q-4` and `sqrt(q(q-4))<q-2`. Thus `p<3(t+1)<q` and `gcd(A_{t+1},N)=p`.

The exact recurrence used by the independent implementation is
\[
A_{k+1}
=
A_k\frac{6(2k+1)(3k+1)(3k+2)}{(k+1)^3},
\]
with exact integer division. The coefficient is 6.

Driver-side independent exact-integer replay over every pair of distinct odd primes below 2000 covered 45,451 semiprimes with 0 failures; 9,969 cases entered the square-root-third fallback and the maximum observed trace length was 13. This regression is supporting evidence only; the proof above carries the universal theorem.

## 4. Required revision

The valid owner should issue a new immutable result, without rewriting `RR-A33E88150B0DAD0B13B8`, that:

1. preserves the fixed-public-prefix no-go as a restricted theorem;
2. incorporates or independently reconstructs the N-dependent `A_s` valuation-wall splitter under the valid owner lineage;
3. keeps the precheck `gcd(N,6)` for the `p=3` case;
4. freezes the exact dyadic synchronization theorem and `floor(isqrt(N)/3), +1` fallback proof;
5. keeps the boundary `GCD_EXTRACTOR_PROVED != FACTORIZATION_SPEEDUP_PROVED`;
6. states the elementary materialization cost explicitly: the largest forced seed is `Theta(p)` in the balanced case, so this theorem does not establish polynomial-time or sub-square-root factoring;
7. uses a new result ID and preserves all source/provenance distinctions. Draft PR #715 may be cited as supplemental method-harvest only, never as a valid scheduler HANDOFF.

## 5. Control boundary

This review grants no Working Truth, Foundation authority, canonical theorem promotion, or factoring-speedup claim.

The task returns to execution. The only accepted closure at this checkpoint is the restricted `PUBLIC_PREFIX_FIXED_INTEGER_SUPPORT_NO_GO`; PCF4 task-terminal control waits for the stronger N-dependent theorem to be frozen under valid provenance.
