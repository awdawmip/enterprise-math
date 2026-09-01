# Driver Review — PCF7 complexity and failure classification

Driver-ID: `EM-DVR-BSJ393`  
Task: `RS-PRIME-COORD-FACTOR-COMPLEXITY-FAILURE-CLASSIFICATION`  
Publication: `TP2-8F7443BCAF2BC5243574`  
Result: `RR-A9A5ADD3931B3F3EDFAB`  
Disposition: `REQUEST_REVISION`

## Verdict

`REQUEST_REVISION / NARROW EXACT-STATEMENT CORRECTION`.

The main polynomial-prefix obstruction is not rejected by this review. Theorem 6.1 correctly constructs, for every polynomial prefix cap, infinitely many balanced semiprimes avoiding the prime supports of the finite public-prefix integers, hence every such public-prefix gcd query equals `1` and the worst-case proper-split probability of randomized/adaptive polynomial-prefix campaigns is `0` on an infinite balanced family.

The `L=N` recurrence classification and the Result's explicit refusal to claim a global factoring lower bound are also retained.

## Exact defect

Section 7 overstates the frozen fixed-probe regression. It says that after choosing `p,q` away from all nonzero probe prime supports, every gcd in the quadratic/sixth-power fixed family is `1`.

That sentence is false for the sixth-power seed `s=1`:

`1^6 - 1 = 0`, hence `gcd(N,0)=N`, not `1`.

The existing deterministic checker already treats this correctly by asserting gcd `1` only for nonzero probe values.

The exact correct statement is:

- every nonzero fixed probe has gcd `1` on the selected semiprimes;
- every zero fixed probe has gcd `N`;
- therefore the whole fixed family returns no proper factor.

This is a local exact-statement defect, not a counterexample to Theorem 6.1 or to the no-proper-split fixed-family conclusion.

## Required revision boundary

Publish a narrow correction only. Preserve Theorem 6.1, the balanced infinite-family construction, the `L=N` complexity calculation, T1-T5, the sealed PCF2 benchmark boundary, and all no-lower-bound guards. A fresh current-schema Result must bind the corrected prose and checker/certificate bytes.

No new factorization algorithm, benchmark generation, or mathematical successor is authorized by this review.

Final disposition: `REQUEST_REVISION / FOLLOWUP_TASK`.
