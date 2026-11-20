# R284CG — Stable modular-fiber signatures and early six-coordinate recovery

Date: 2026-11-21 (Asia/Shanghai). Status: **AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED**. Portable, unclaimed continuation of R284CF; no change to P000, frozen Port parameters, other owners or formal Task state.

## Frozen observer and circular carriers

For every unknown binary matrix `C in {1,2}^{4x4}` use the frozen 34-bit observer

`M(C) = diag(1120832,6,13,1651128) - C - 390139 E_01 - 394465 E_02 - 1497639 E_03`,

`F(C) = det M(C) (mod p)`, `p = 17179869143`, with zero-based indices. The six **critical coordinates** are, in key order, `S = (C10,C11,C12,C20,C21,C22)`. Let `k in {0,...,63}` encode their binary values, in that order (MSB first).

R284CE established real-coordinate monotonicity and therefore the exact shortest containing unwrapped determinant interval for each fixed key `k`. Compute its endpoints by assigning the remaining ten entries all `2` (lower determinant `b_k`) or all `1` (upper determinant `t_k`), respectively. Set `a_k=b_k mod p` and `w_k=t_k-b_k`. The corresponding circular arc is `A_k = {a_k+s (mod p): 0<=s<=w_k}`. Exactly 64 arcs exist, and `307592214 <= w_k <= 450181375 < p/2`. This representation retains the discrete 64-key provenance instead of replacing it by one saturated continuous interval.

For any exact codeword `x=F(C)`, define its **modular-fiber signature** `Sigma(x)={k: x in A_k}`. For a real circular observation `y` with uncertainty radius `rho>=0`, define `Sigma_rho(y)={k: dist_circle(y,A_k)<=rho}`; an open strict observation bound uses `dist_circle(x,y)<rho`.

## Theorem R284CG

Over **all** 65,536 matrices of the frozen model:

1. Every codeword lies in between one and four arcs, with exact histogram `1:23178, 2:23094, 3:16964, 4:2300`. There are exactly 114 distinct signatures.
2. The **smallest positive circular separation of any codeword from an arc not containing it** is exactly `1183`. One attaining witness is `x=4781788058` and key `k=25`, whose arc starts at `4471172719` and has width `310614156`: its right endpoint is `4781786875`, giving distance `1183`.
3. For **every** codeword `x`, **every real** `y` with `dist_circle(x,y)<rho`, and **every** `0<=rho<1183/2`, the signature is invariant: `Sigma_rho(y)=Sigma(x)`. The threshold `1183/2=591.5` is a sharp supremum for this uniform same-radius arc-screening guarantee: for every `rho>1183/2`, the midpoint between the witness codeword and its excluded arc gives a counterexample.
4. A critical bit is called *forced by the signature* when all keys in `Sigma(x)` agree on its value. The exact forced-bit histogram (number of forced bits : number of matrices) is `0:4696, 1:17702, 2:7734, 3:10426, 4:1532, 5:268, 6:23178`. Consequently **60,840/65,536 matrices have at least one critical bit forced** and **23,178/65,536 have all six forced** by the arc signature. By coordinate order `S`, individual forced counts are `(38486,34564,41552,34442,30026,31914)`, totaling `210984` forced-bit incidences.
5. The union of all 64 uninflated arcs has exactly 15 connected components in the **linear fundamental interval** `[0,p]` and total circular length `14,595,332,646` out of `p=17,179,869,143`. It therefore excludes a nonempty open set of modular observations even before a critical bit is fixed.

The deterministic statistics in (1), (2), (4) and (5) follow from the **complete exact finite enumeration** in the companion checker. The universal quantifiers over real observations in (3) follow analytically from the separation certificate. This is a strengthened, explicitly typed discrete-residual response to R284CF's five-coordinate obstruction for a *single continuous interval*: the representation here retains a **union of modular fibers**.

### Proof of noise invariance

Let `delta=1183`. For any `k` in `Sigma(x)`, `dist_circle(y,A_k)<=dist_circle(y,x)<rho`, so `k` is included in `Sigma_rho(y)`. If `k` is not in `Sigma(x)`, the exact full-domain certificate gives `dist_circle(x,A_k)>=delta`. By the metric triangle inequality, `dist_circle(y,A_k)>=delta-dist_circle(y,x)>delta-rho>rho` whenever `2*rho<delta`. Hence no other key enters. For the witness in (2), the midpoint has distance `delta/2` from both the codeword and the excluded arc, so every radius strictly greater than `delta/2` admits a counterexample. A forced bit is read directly from the common digit across retained keys; a singleton signature fixes the complete six-coordinate key. QED.

The original full-matrix codeword minimum distance remains `59`, so its guaranteed **full-matrix** correction radius remains `<29.5`. The larger `<591.5` bound concerns only **coarse modular-fiber signatures and the critical bits actually forced by them**.

## Verification and reproducibility

The standalone standard-library script `R284CG_modular_fiber_signature_checker.py` evaluates all `2^16=65536` binary matrices exactly; checks the unchanged frozen SHA-256 of the original ordered 8-byte codeword serialization `b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4`; independently crosschecks 128 determinant endpoints using the 24-term Leibniz formula; regenerates all 64 arcs; and performs exactly `65536*64=4,194,304` word-versus-arc classification and separation checks. It also verifies the full code minimum distance `59`, the signature and forced-bit histograms and exact union length. All are integer operations; no sampling, floating-point approximation or simulation of real noise is used in the proof.

Companion certificate: `research_notes/portable_direct/R284CG_modular_fiber_signature_verification.json`. Run `python research_notes/portable_direct/R284CG_modular_fiber_signature_checker.py` to print a semantically equivalent JSON certificate.

Inputs are inherited from frozen R284BZ (34-bit gap 59), R284CE (monotone exact arcs) and R284CF (continuous-relaxation saturation). No formal Claim, Result/Review or P000 status is changed; independent review remains `NOT_REVIEWED`. Historical contribution trail `EM-DIRECT-20B766` is provenance only until the present runtime's own Activity capability is established.

## Next unit

Find a hierarchical, exact modular-fiber filter that avoids generating/checking all 64 arcs on every query. Compare average and worst-case preprocessing, persistent bytes, number of determinants, circular interval tests and downstream candidate calculations against R284CE/R284CD. In particular, use the 114 finite signature types and coordinate-forcing histograms to test whether a small certified decision tree can recover the first critical bit under radius `<29.5` without giving up zero-prestored-arc reconstruction.
