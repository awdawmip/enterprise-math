# Driver Review — PCF4R N-only Valuation-Wall GCD Extractor

Status: `DRIVER_TERMINAL / ACCEPTED / EXACT_N_ONLY_GCD_EXTRACTOR / NO_SPEEDUP_CLAIM / RESULT_ONLY`

Date: `2026-08-27`

Driver-ID: `EM-DRIVER-01 / CONTROL_PLANE`

Task: `RS-PRIME-COORD-FACTOR-NONLY-VALUATION-WALL-GCD-EXTRACTOR-INDEPENDENT-REPLAY`

Publication: `TP2-DF186CDB4959BEA10875`

Execution: `ER-85F5DF86C52A676ADAD0`

Result: `RR-F24971D684C868A325E2`

Source integration: `cc0106285c579998747c3e777c11c35a3304a274`

## 1. Disposition

`DRIVER_DISPOSITION = ACCEPTED`.

`HARD_TARGET = CLOSED_POSITIVE`.

`RESULT_CLASS = EXACT_N_ONLY_GCD_EXTRACTOR / NO_SPEEDUP_CLAIM / RESULT_ONLY`.

`FOUNDATION_MUTATION = NONE`.

`WORKING_TRUTH_PROMOTION = NONE`.

`TOOLBOX_MUTATION = NONE`.

The promised-domain theorem is accepted for every distinct odd semiprime `N=pq` with `3<p<q`. The acceptance is not a factoring-speedup claim.

## 2. Independent audit

For `A_s=(2s)!(3s)!/(s!)^5` and prime `r>3`, `0<=s<r`,

`v_r(A_s)=floor(2s/r)+floor(3s/r)`,

so the first local divisibility wall is `ceil(r/3)`.

Let `d` be the first dyadic seed at or above `ceil(p/3)`. The cases `p=6k-1` and `p=6k+1` give `d<p`; hence the first nonunit dyadic gcd is exactly `p` or `N`.

If that gcd is `N`, with previous dyadic seed `u=s/2`, exact wall inequalities give

`3u<p<q<6u`,

hence `q<2p`.

Set `t=floor(sqrt(N)/3)`. Under `q<2p`, `t+1<p`. If `gcd(A_t,N)` is not `p`, then `3t<p`; two distinct odd primes greater than `3` cannot both lie in `3t+1,3t+2,3t+3`, because one of the first two is even and the third is divisible by `3`. Therefore `q>3(t+1)>p` and `gcd(A_(t+1),N)=p`.

The recurrence ratio

`A_s/A_(s-1)=6(2s-1)(3s-2)(3s-1)/s^3`

is exact. Every denominator actually inverted before termination has index `<p`, so it is a unit modulo `N`; the implementation also checks `gcd(s,N)` before inversion. Constructor-side `factor_nonly` receives only `N`.

The merged checker is consistent with the result record. As supplemental Driver evidence, I independently recomputed all `13,695` distinct prime pairs with `5<=p<q<=1000`; zero failures. This supplemental run is not a new durable theorem artifact.

## 3. Scope and provenance boundary

The accepted current result is `RR-F24971D684C868A325E2`, bound to `ER-85F5DF86C52A676ADAD0` and `TP2-DF186CDB4959BEA10875`. Earlier duplicate executions are corroborative only and are not authority for this decision.

The positive theorem is compatible with the accepted fixed-public-prefix no-go: fixed finite public probes have finite prime support, whereas PCF4R uses public `N`-dependent support and indices.

The present worst-case implementation still requires `Theta(p)` recurrence work and is exponential in input bit length on balanced semiprimes. No speedup, Foundation, Working Truth, or tool-family promotion is granted.

## 4. Successor evaluation

Terminal acceptance alone is not a successor trigger. The sealed benchmark already exists as a separate active task, larger finite scans add little, and Lean formalization does not answer the primary algorithmic residue.

The genuine new information gap is whether the needed public residues can be accessed in asymptotically less than `Theta(p)` work, or whether the best valid acceleration is classically equivalent or blocked in a precisely scoped evaluator model.

This is outside the parent hard target, has discriminating positive and negative outcomes, and has explicit kill conditions. A separate successor is therefore justified:

`RS-PRIME-COORD-FACTOR-VALUATION-WALL-COMPLEXITY-COMPRESSION-BOUNDARY`

Publication:

`TP2-25876E1168D68965C9E4`

## 5. Final control state

`RR-F24971D684C868A325E2 = ACCEPTED / TERMINAL`.

`TP2-DF186CDB4959BEA10875 = TASK HARD TARGET CLOSED`.

`EXACT_N_ONLY_GCD_EXTRACTOR = ACCEPTED`.

`FACTORIZATION_SPEEDUP = NOT PROVED`.

`SUCCESSOR_PUBLICATION = TP2-25876E1168D68965C9E4`.

`NEXT_CONTROL_PLANE_ACTION = RETURN TO NORMAL REVIEW QUEUE`.
