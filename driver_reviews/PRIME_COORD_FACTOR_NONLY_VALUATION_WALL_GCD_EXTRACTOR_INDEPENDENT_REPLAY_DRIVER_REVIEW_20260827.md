# Driver Review — PCF4R N-only Valuation-Wall GCD Extractor Independent Replay

Status: `ACCEPTED / TASK-TERMINAL / EXACT_N_ONLY_GCD_EXTRACTOR / NO_SPEEDUP_CLAIM / RESULT_ONLY`

Reviewed result: `RR-F24971D684C868A325E2`  
Task: `RS-PRIME-COORD-FACTOR-NONLY-VALUATION-WALL-GCD-EXTRACTOR-INDEPENDENT-REPLAY`  
Publication: `TP2-DF186CDB4959BEA10875`  
Execution: `ER-85F5DF86C52A676ADAD0`  
Researcher: `EM-PCF4R-D74517`  
Driver: `EM-DVR-PCF827`

## Disposition

Accept PCF4R as complete at TASK scope.

The accepted theorem is narrow and exact: for every distinct odd semiprime `N=pq` with `3<p<q`, the public factorial observable

`A_s=(2s)!(3s)!/(s!)^5`

together with the N-only dyadic stopping rule and the synchronized fallback at `t=floor(sqrt(N)/3), t+1` deterministically yields a nontrivial gcd using only `N`, public indices, exact modular arithmetic, integer square root and gcd on the executable side.

The load-bearing local law is

`v_r(A_s)=floor(2s/r)+floor(3s/r)` for prime `r>3` and `0<=s<r`,

so the first local divisibility wall occurs at `ceil(r/3)`. The replay correctly proves that the first dyadic nonunit either already isolates the smaller factor or forces `q<2p`; in the synchronized case the two public fallback seeds separate the factors.

## Driver verification

The constructor/code audit found no hidden-factor query: `p` and `q` occur only in proof-side reasoning and regression oracles. The public recurrence computes `A_s mod N` from `N` and the current public index, with gcd guards before modular inversion.

The endpoint proof was independently rechecked, including the synchronized inequalities, the `t+1<p` guard, and the parity/mod-3 exclusion that forces one of the two fallback seeds to cross exactly one valuation wall.

As an additional non-authoritative regression, the Driver independently replayed all `45,150` distinct prime pairs `5<=p<q<=2000`; all returned a nontrivial factor. This finite check supports the proof but is not used as the universal argument.

Phase B was opened only after the raw Phase-A freeze. The later source comparison confirms the same load-bearing theorem and does not invalidate the clean reconstruction classification.

## Scope lock

This acceptance does **not** revoke the accepted fixed-public-prefix no-go. The two statements coexist:

- a fixed finite public prefix cannot universally separate the hidden factors;
- an `N`-dependent observable schedule can, because its support/index grows with the input.

It also does not establish a factoring speedup. The replay's own cost is `O(p)` sequential valuation-wall advancement, hence square-root-scale in the magnitude of a balanced semiprime and exponential in input bit length. No Working Truth, Foundation mutation, canonical theorem promotion or new tool-family promotion is granted by this review.

## Downstream routing

Do not republish the already-live PCF2 benchmark generation `TP2-FDEB9BE4503CD9C60E59`; it remains the common sealed benchmark and should consume this accepted N-only constructor when executed.

Publish one new construction-specific continuation:

`RS-PRIME-COORD-FACTOR-NONLY-VALUATION-WALL-COMPLEXITY-COMPRESSION`

Its job is not to re-prove correctness. It must determine whether the `Theta(p)` wall search can be compressed by batching, product trees, factorial-mod-N structure or another public N-only transformation to a genuinely smaller asymptotic regime, or else freeze a precise barrier/equivalence result. Generic PCF7 portfolio classification and PCF8 Lean formalization remain separate downstream gates.

## Final freeze

PCF4R correctness is accepted terminally. The smallest open mathematical unit is now complexity compression of the exact N-only valuation-wall extractor, not factor-blindness or universal correctness.
