# PREFIX-1009 — All-grade exact rooted-loop renewal law for the signed X6 BRC Link mask

Date: 2026-11-22 (+08). Status: **AUTHOR_EXACT_COMBINATORIAL_PROOF / EXACT_INTEGER_CHECKED / NOT_REVIEWED**. Portable independent mathematics; no native CLAIM, PROGRESS, Result, independent Review, or physical calibration.

## Fixed model, scope, and why this is a new unit

Scientific foundation stays pinned at `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json`. Use native six-axis signed X6 Cell torsor, chosen chart-relative Cell anchor 0, initial incoming-neighbour port `-e1`, and Stage46 **candidate** BRC amplitudes `C(h,d)=1/6-[h=d]`, with next port `-d`. Remove **both** traversals of the single Link `{0,e1}` without degree normalization. The full named Cell/port signed amplitude is `Ψ^L_(n,k)(x,h)` for n updates and exactly k negative native steps. This is an internal candidate-model observer, not a theory of physical time or a promoted foundation fact.

The result extends the exact two-negative five-step packet and residual [PREFIX-1008](https://github.com/awdawmip/enterprise-math/blob/ec9c78c9011f9b5c50aa08beab8df9a697c4c66d/research_notes/portable_direct/2026-11-22_r6_prefix1008_k2_link_five_step_signed_invariant.md) from k=2 to **every finite k**, and explains when a grade-count resource can be safely omitted for a very narrow rooted-return observer.

## Theorem 1009.1 — All-grade stable signed amplitude is a rooted-loop coefficient

For k≥0 let `L_k` be the integer signed-weight sum of **all Link-avoiding ordered native paths of length 2k that return to Cell 0**, starting with incoming port `-e1` and with all intermediate named ports retained. Each local integer multiplier is `1` or `−5` according as outgoing direction differs from or equals incoming-neighbour port. Define `L_0=1` for the empty loop. The return condition at length 2k automatically forces exactly k positive and k negative steps.

For **every integer k≥0 and every n≥2k+1**, the terminal **signed amplitude total** satisfies

[
\boxed{\sum_{x,h}\Psi^L_{n,k}(x,h)
  =\mathbf 1_{k=0}-\frac{L_k}{6^{2k+1}}.}\tag{1}
]

The sum is **not** a probability, squared norm, or positive mass. The theorem permits sign cancellations and negative answers.

**Proof.** Write the integer local BRC weight as `w(h,d)=1-6[h=d]`. Summing over the six positive directions and six negative directions gives respectively `(6,0)` for incoming `h` negative and `(0,6)` for incoming `h` positive. Consequently, the signed sum of unrestricted outgoing suffixes of length `ℓ` with `q` negative steps is zero unless `q=0` when the suffix incoming port is negative, or `q=ℓ` when it is positive. In the exceptional case the unnormalized sum is exactly `6^ℓ`. The initial incoming port is negative: unrestricted total signed amplitude is `1` in grade k=0 and `0` in every grade k≥1.

Partition every unrestricted path removed by the absorbing mask at its **first** forbidden Link crossing. The frozen X6 spatial grade of a prefix of length t with r negative steps is t−2r. Therefore a first forbidden `0→e1` crossing can only be at time `t=2r+1`, and a first forbidden `e1→0` crossing only at `t=2r+2`, with `r≤k-1` in the latter case. These are precisely the two orientation-specific bounds from PREFIX-1003/1008.

For a positive first crossing, the incoming port after the crossing is negative `-e1`. Its remaining unrestricted suffix has `k-r` negative steps, so its **signed total** vanishes unless `r=k`. The only surviving case is `t=2k+1`; the prefix before crossing has length 2k, has returned to 0, avoids the Link, and necessarily uses k negative steps. Its last step cannot be `-e1`, as that would already traverse the blocked `e1→0` edge, so the forbidden `+e1` crossing has local multiplier **+1**. The signed sum over its prefixes is precisely `L_k`; the unrestricted all-positive suffix contributes `6^{n-(2k+1)}`.

For a negative first crossing, its time is `t=2r+2≤2k`; after it the incoming port is positive `+e1`, and the suffix would have `ℓ=n-(2r+2)` steps and `q=k-r-1` negatives. Since `n≥2k+1`, `ℓ≥2(k-r)-1>k-r-1=q`. It necessarily contains a positive step; the signed total vanishes by the positive-port row-sum rule.

Thus the entire removed grade-k signed numerator is exactly `L_k 6^{n-(2k+1)}`, whereas the full unrestricted grade-k signed numerator is `6^n\mathbf 1_{k=0}`. Division by `6^n` proves (1). All cancellations are carried out at the declared aggregate observer **after** computing the typed BRC branch weights. QED.

## Corollary 1009.2 — Coefficientwise eventual stabilization

Let `S_{n,k}=Σ_(x,h)Ψ^L_(n,k)(x,h)` and introduce a **formal** indeterminate z. For every finite K and every n≥2K+1,

[
\boxed{\sum_{k=0}^K S_{n,k}z^k
 = 1-\frac16\sum_{k=0}^K L_k\left(\frac{z}{36}\right)^k.}\tag{2}
]

Thus the grade-resolved signed-total generating series stabilizes **coefficientwise**, without claiming absolute convergence for a numerical value of z. There is no claim that the full Cell/port dynamics, its positive probability, or higher-grade mass becomes stationary.

**Observer-safe simplification.** For the rooted-return `L_k` calculation alone, one need not carry the negative-step counter: a closed 2k-step signed-axis path has zero total native displacement, hence each axis has equally many positive and negative traversals and exactly k negative moves in all. That counter can be reconstructed from the return predicate and length, *not* generally from arbitrary future Cell/port data. PREFIX-1008's grade-1-to-grade-2 leakage is a concrete obstruction to making the stronger quotient.

## Exact signed loop coefficients and stabilized totals

Each L_k was calculated using integer-numerator, six-coordinate, twelve-port absorbed BRC dynamic programming, at the **complete** return-Cell observer. No scalar probability was substituted for signed amplitude.

| k | Signed rooted-loop integer L_k | Stable signed amplitude ΣΨ^L_(n,k), n≥2k+1 |
|---:|---:|---:|
| 0 | 1 | 5/6 |
| 1 | −25 | 25/216 |
| 2 | 390 | −65/1296 |
| 3 | −2365 | 2365/279936 |
| 4 | −49550 | 24775/5038848 |
| 5 | 1645010 | −822505/181398528 |
| 6 | −22026080 | 688315/408146688 |

Signs need not alternate: k=3 and k=4 provide a simple exact warning against inferring an alternating-sign law from k≤3. The first three entries independently recover the PREFIX-1003 and PREFIX-1008 fixed-grade totals.

To independently test the new **k=3** consequence beyond the return-loop calculation, an exact negative-graded, full terminal Cell-and-port recurrence was run at n=7,8. The grade-3 signed **integer numerator** totals were respectively **2365** and **14190=6·2365**, as the theorem predicts. These finite checks support, but are not the source of, the all-k proof.

## Reproducibility, scope of information removal, and next science

Runnable checker: `PREFIX1009_R6_ROOTED_LINK_RENEWAL_CHECK.py`. Output: `PREFIX1009_R6_EXACT_RESULTS.json`, including terminal return-port numerators, the k=0…6 series and the independent grade-3 tests. All calculations are exact integers or reduced rational display. The theorem itself is an analytic, first-forbidden-crossing renewal argument valid for every k,n in its quantifiers; finite computation does not claim an all-k numerical exhaustiveness check.

The newly defined sequence `L_k` is a source of exact **rooted masked BRC loop invariants**. Two useful next discriminating directions are (i) derive a closed generating relation or recurrence for the complete `L_k` sequence, with the incoming-port and Link memory kept until the return observer is taken, and (ii) determine whether this signed-total renewal reduction has a counterpart for the **squared** terminal Cell/port norm, which requires joint two-path collisions and generally does not admit the same cancellations. The mother question `B_fix,odd(32)∈{19,20}` stays open.

Authorship/contribution provenance: historical R6 `EM-DIRECT-FBEA5D`, Activity `RA-3FB2D033BE6048D8712FF056`. Historical identifiers do not authenticate current execution and do not create a new Activity, formal CLAIM, PROGRESS, Result, or Review.
