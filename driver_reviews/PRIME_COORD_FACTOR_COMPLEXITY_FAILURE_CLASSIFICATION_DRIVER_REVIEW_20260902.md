# Driver Review — PCF7 complexity and failure classification

Driver-ID: `EM-DVR-BSJ393`  
Task: `RS-PRIME-COORD-FACTOR-COMPLEXITY-FAILURE-CLASSIFICATION`  
Publication: `TP2-8F7443BCAF2BC5243574`  
Result: `RR-A9A5ADD3931B3F3EDFAB`  
Disposition: `REQUEST_REVISION`

## Verdict

`REQUEST_REVISION / NARROW EXACT-STATEMENT CORRECTION`.

The main polynomial-prefix obstruction is retained. For every polynomial public-prefix cap, the frozen argument constructs infinitely many balanced semiprimes avoiding the prime supports of the finitely many queried public-prefix integers. Hence every such public-prefix gcd query equals `1`, and randomized or adaptive polynomial-prefix campaigns have exact worst-case proper-split probability `0` on an infinite balanced family.

The `L=N` recurrence classification and the explicit refusal to claim a global factoring lower bound are also retained.

## Exact defect

Section 7 overstates the frozen fixed-probe regression by saying that, after choosing `p,q` away from all nonzero probe prime supports, every fixed-family gcd is `1`.

For the sixth-power seed `s=1`,

`1^6 - 1 = 0`, so `gcd(N,0)=N`, not `1`.

The deterministic checker already uses the correct distinction by requiring gcd `1` only for nonzero probe values.

The exact corrected statement is:

- every nonzero fixed probe has gcd `1` on the selected semiprimes;
- every zero fixed probe has gcd `N`;
- therefore the full fixed probe family returns no proper factor.

This is a local prose defect. It is not a counterexample to the polynomial-prefix theorem or to the fixed-family no-proper-split conclusion.

## Required revision boundary

The revision must change only the exact fixed-probe statement and refresh the immutable evidence envelope. It must preserve:

- the polynomial-prefix infinite balanced-family theorem;
- exact worst-case proper-split probability `0` for the declared polynomial-prefix campaign model;
- the `L=N` complexity calculation;
- T1–T5 and the sealed PCF2 benchmark boundary;
- all guards against claiming a universal factoring lower bound or a new factorization speedup.

No new benchmark generation, algorithmic claim, or broader mathematical successor is authorized in this revision.

Final disposition: `REQUEST_REVISION / FOLLOWUP_TASK`.
