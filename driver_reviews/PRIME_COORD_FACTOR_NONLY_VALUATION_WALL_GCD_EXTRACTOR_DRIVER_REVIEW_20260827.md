# Driver Review — PCF4R N-only Valuation-Wall GCD Extractor

Status: `DRIVER_TERMINAL / ACCEPTED / EXACT_N_ONLY_GCD_EXTRACTOR / NO_SPEEDUP_CLAIM / RESULT_ONLY`

Date: `2026-08-27`

Driver-ID: `EM-DRIVER-01 / CONTROL_PLANE`

Task: `RS-PRIME-COORD-FACTOR-NONLY-VALUATION-WALL-GCD-EXTRACTOR-INDEPENDENT-REPLAY`

Publication: `TP2-DF186CDB4959BEA10875`

Execution: `ER-85F5DF86C52A676ADAD0`

Researcher-ID: `EM-PCF4R-D74517`

Result: `RR-F24971D684C868A325E2`

Source integration: `cc0106285c579998747c3e777c11c35a3304a274`

## 1. Driver disposition

`DRIVER_DISPOSITION = ACCEPTED`.

`HARD_TARGET = CLOSED_POSITIVE`.

`PRIMARY_TASK_VERDICT = N_ONLY_GCD_EXTRACTOR_VERIFIED`.

`RESULT_CLASS = EXACT_N_ONLY_GCD_EXTRACTOR / NO_SPEEDUP_CLAIM / RESULT_ONLY`.

`FOUNDATION_MUTATION = NONE`.

`WORKING_TRUTH_PROMOTION = NONE`.

`TOOLBOX_MUTATION = NONE`.

The canonical writer-conformant result proves the task's exact promised-domain target. I accept it as a terminal theorem-level research result for distinct odd semiprimes

\[
N=pq,\qquad 3<p<q.
\]

The acceptance is deliberately narrower than a factoring-speedup claim. The current constructor still uses a worst-case \(\Theta(p)\) streaming recurrence, which is exponential in input bit length on balanced semiprimes.

## 2. Independent mathematical audit

The load-bearing argument was reconstructed independently from the frozen return rather than accepted from finite regression.

For

\[
A_s=\frac{(2s)!(3s)!}{(s!)^5},
\]

and prime \(r>3\) with \(0\le s<r\), Legendre valuation gives

\[
v_r(A_s)=\left\lfloor\frac{2s}{r}\right\rfloor+\left\lfloor\frac{3s}{r}\right\rfloor.
\]

Because \(r\not\equiv0\pmod3\), the first local divisibility wall is exactly \(s=\lceil r/3\rceil\).

Let \(d\) be the least dyadic seed at or above \(\lceil p/3\rceil\). For every prime \(p>3\), the two residue classes \(p=6k\pm1\) give \(d<p\). Hence the first nonunit dyadic seed lies below both hidden factors and its gcd is exactly either \(p\) or \(N\).

If the first nonunit is \(N\), writing the previous dyadic seed as \(u=s/2\) gives

\[
3u<p<q<6u,
\]

so \(q<2p\). This synchronization inequality is exact.

Set

\[
t=\left\lfloor\frac{\sqrt N}{3}\right\rfloor.
\]

Under \(q<2p\), one has \(t+1<p\). The larger factor does not divide \(A_t\). If \(p\) also does not divide \(A_t\), then \(3t<p\); placing both \(p<q\) inside the three integers immediately above \(3t\) is impossible because one of the first two is even and the third is divisible by \(3\). Therefore \(q>3(t+1)\) while \(p<3(t+1)\), and

\[
\gcd(A_{t+1},N)=p.
\]

This closes the synchronized fallback without hidden-factor constructor input.

## 3. Constructor and modular-division audit

The exact ratio

\[
\frac{A_s}{A_{s-1}}=\frac{6(2s-1)(3s-2)(3s-1)}{s^3}
\]

is correct. Every recurrence index actually reached before theorem termination is \(<p\); in the synchronized branch \(t+1<p\) as well. Thus every denominator inverted on the theorem path is a unit modulo \(N=pq\).

The implementation also tests `gcd(s,N)` before inversion, so a nonunit denominator cannot be silently inverted. Constructor-side `factor_nonly` receives only `N`; prime generation appears only in the regression oracle.

The frozen checker digest and counts in the result record match the merged artifact. As supplemental Driver evidence, I independently recomputed the constructor on all `13,695` distinct prime pairs with `5<=p<q<=1000`; there were zero failures. This additional run is review evidence only and is not promoted to a new durable theorem artifact.

## 4. Provenance and duplicate-execution boundary

The accepted result is the current owner result `RR-F24971D684C868A325E2`, bound to execution `ER-85F5DF86C52A676ADAD0` and publication `TP2-DF186CDB4959BEA10875`.

Earlier supplemental executions are not used as authority for this terminal decision. Their agreement is corroborative only. The clean replay froze its Phase-A derivation and checker before source comparison, then disclosed Phase-B agreement.

No second result record for the non-authoritative duplicate is present in the current task generation on `main`, so the immutable result reducer remains a single-result Driver-review flow rather than a parallel-evidence synthesis case.

## 5. Compatibility with the parent no-go

This positive result does not contradict the accepted fixed-public-prefix obstruction.

The parent no-go says a fixed finite public prefix collapses to gcds against fixed integers and therefore has finite prime support. PCF4R escapes that theorem by allowing the queried observable support and seed schedule to grow with public input `N`.

Both statements are retained:

\[
\boxed{\text{fixed public prefix: no universal splitter}}
\]

and

\[
\boxed{\text{N-dependent valuation wall: exact universal splitter on the promised domain}}.
\]

## 6. Successor evaluation

Terminal acceptance does not by itself justify more research. I evaluated the remaining portfolio options separately.

The sealed factor-blind benchmark is already a distinct published program task and has an active owner, so opening another benchmark would duplicate work. Larger finite scans would add little after the universal proof. Lean formalization is useful but does not answer the main algorithmic question.

The genuine new information gap is complexity: can the public residues needed by the exact valuation-wall splitter be evaluated in asymptotically less than \(\Theta(p)\) sequential work, or does the best valid acceleration collapse to a known deterministic factorial-factorization method or a rigorously scoped barrier?

This gap is explicitly outside the parent hard target, has discriminating positive and negative outcomes, and can be killed by classical-equivalence or lower-bound evidence. It therefore passes continuation review.

I publish the separate successor:

`RS-PRIME-COORD-FACTOR-VALUATION-WALL-COMPLEXITY-COMPRESSION-BOUNDARY`

under immutable publication

`TP2-25876E1168D68965C9E4`.

The new task must not call a memory reduction or constant-factor improvement a factoring speedup. Any positive compression verdict must prove an asymptotic improvement and fully account for arithmetic over the composite modulus.

## 7. Final control state

`RR-F24971D684C868A325E2 = ACCEPTED / TERMINAL`.

`TP2-DF186CDB4959BEA10875 = TASK HARD TARGET CLOSED`.

`METHOD_HARVEST = RESULT_ONLY`.

`EXACT_N_ONLY_GCD_EXTRACTOR = ACCEPTED`.

`FACTORIZATION_SPEEDUP = NOT PROVED`.

`SUCCESSOR_TASK = RS-PRIME-COORD-FACTOR-VALUATION-WALL-COMPLEXITY-COMPRESSION-BOUNDARY`.

`SUCCESSOR_PUBLICATION = TP2-25876E1168D68965C9E4`.

`NEXT_CONTROL_PLANE_ACTION = RETURN TO NORMAL REVIEW QUEUE AFTER IMMUTABLE REVIEW AND PUBLICATION RECORDS ARE MATERIALIZED`.
