# R116-S23 — Exact six-phase eligibility verification (supplement)

Dated 2026-11-13. This supplements `PROOF.md` in the same directory by testing all R116 formulas on **the actual R115-SIG auxiliary S23 fractional-arc predicate**, instead of only generic rational half-open eligibility unions.

## Exact model

Fix rational parameter interval `[0,1]`, `j=0`, `x=1/4`, `a=0`, `b=1`. For integer time t and rational parameter theta, let

- `y_t={x+(t-j)theta}`
- `A(theta)={a theta}=0`
- `B(theta)={b theta}={theta}`

where braces indicate fractional part. Eligibility `M_t(theta)` means the directed half-open circular arc from A to B contains y_t; coincident endpoints imply empty arc. This is the same exact predicate implemented by `check_r115.py` in the earlier R115-SIG bundle.

The exact parameter atoms are singleton roots and open gaps of integer intersections for all six rational affine phases `Y_t,A,B,Y_t-A,Y_t-B,B-A` across old and newly introduced time t, including endpoints `0,1`. Fraction arithmetic, including floor/ceil for negative t, is exact.

Old potential times: integers -4..4 (three branches each). The first new time is selected from {-17,-13,-11,-9,9,11,13,17}. For each trial random old F,G, compute old/new signatures; one-sided and common insertion of a new complete identity `(t,b)`; exhaust all actual parameter atoms and directly compare Top-k for k=1..30.

## Reproducibility

The attachment `check_r116_s23.py.gz.b64` is the Python 3 source encoded as gzip+base64. To recover:

`base64 -d check_r116_s23.py.gz.b64 | gzip -dc > check_r116_s23.py`

Then execute `python check_r116_s23.py`. The checker writes `verification_r116_s23.json`. The exact observed file is also preserved compressed as `verification_r116_s23.json.gz.b64`.

Standalone Python source SHA256: `8c5b2be3598b93810ac02c3ab13db8c7b0b9717b210d02433e9d58a00fdeaa59`.
Standalone verification JSON SHA256: `3414ecf64e90bfefbdabd21f2eeb987f95c07080ed4c99b1fe41e96d1dadba8f`.

Observed local result:

`R116_S23_PASS 160 14428 865680 26427 2435 3730`

- 160 randomized actual-S23 history trials
- 14,428 exact rational singleton/open-gap atom evaluations
- 865,680 directly enumerated Top-k comparisons
- 26,427 exact finite-capacity witnesses checked
- 2,435 new distinct abstract-signature child states in aggregate
- 3,730 additional connected parameter boundaries in aggregate

The exact input and counters are held in the accompanying JSON; these are execution measurements for combinatorial checks, **not** runtime speed or complexity improvements.

## Interpretation and next step

This second checker closes the generic-to-historical-auxiliary predicate verification gap for the tested parameters and integer times. The **Theorems A–E** in the main proof establish the exact general finite Boolean result; the new computation exercises those identities on the actual R115-SIG six-affine-phase S23 observer and correct singleton endpoint behavior. The actual predicate is still an auxiliary observer and is not a native Cell/Link/Port licensed event.

For R117: build a true online persistent rational-cut index, maintain multiple newly arriving times and historical reintroduction, and compare bit-operation, memory and witness-recovery costs with full rebuilding.
