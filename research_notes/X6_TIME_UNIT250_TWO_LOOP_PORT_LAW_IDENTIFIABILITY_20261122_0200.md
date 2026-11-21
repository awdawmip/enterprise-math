# X6 Native Time — Unit250: sharp C24 Port-law identifiability from two additional BRC loops

Date: 2026-11-22. Task: `RS-X6-NATIVE-TIME-DYNAMICS`; parent `PO-X6-UPPER-STRUCTURE-20260906`.
Status: **AUTHOR-PROVED / EXACT-FINITE-EXECUTED / UNREVIEWED / NOT_ADMITTED**.
Model: frozen P000 X6 six-axis signed Cell torsor and selected three-dimensional slice; time is chronological event order, not an extra spatial axis. All signed BRC primitive events, labelled intact triads, occupancy and Port source provenance are retained. Precision projection is only the declared observer, not a quotient of the physical state.

## Frozen inputs and genuine unresolved physical experiment

Scientific pin: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. Reuse Unit245 36 directed ingress/egress shortest two-triad chronological certificates, Unit248 additive centre-precision law, and Unit249 exact 36-case endpoint observer certificate at `c0116bf2ee4970493fcb6e7c55da4692202c4547:research_checks/X6_TIME_UNIT249_ORIGINAL_BRC_PRECISION_LAW_REPLAY_RESULTS_20261122.json`, Git blob `1d822a82adaa899c72a7d206d8407a713aec0ad5`. The ring has twelve conditional OUTER cells `x0,...,x11`; six even-index centre ingress `x_i -> P` and egress `P -> x_j`. Ring precision increments `g5=g10=3`, all other `g_r=0`, inverse steps negate increments, and the precision sensor reads an additive register in `C24`.

The physical signed Port update, triad/environment permission, and independent measured C12/C24 register remain unsourced. All conclusions below are **conditional model-internal exact results**, and cannot certify the original native experiment.

## Theorem 250A — 36 original shortest terminal readouts have 18 inequivalent Port laws

Write the six ingress weights as `alpha_k`, six egress weights as `beta_k` for `k=0..5` (Port cell `x_{2k}`), all modulo 24. A full centre passage `x_{2k}->P->x_{2l}` changes the calibrated precision by `alpha_k+beta_l`. The original Unit249 shortest route for pair `(k,l)` makes exactly
[
 c_{kl} = \frac{12}{\gcd(12,2(l-k))}
]
such passages, with the convention `gcd(12,0)=12`; its per-label terminal readout is the known ring contribution plus `c_{kl}(alpha_k+beta_l) mod24`. The exact 36 source rows have been re-read and checked against this integer formula.

Suppose two entire 12-Port laws give identical terminal C24 readouts in **all 36 original labelled shortest paths**. Let their parameter differences be `a_k,b_l`. The diagonal `c_{kk}=1` forces `b_k=-a_k`; all remaining conditions are
[
 c_{kl}(a_k-a_l)=0\pmod {24}.
]
For shifts of indices `l-k=±1,±2,3` modulo six, these become, respectively,
[
 a_k=a_{k+1}\pmod4,qquad
 a_k=a_{k+2}\pmod8,qquad
 a_k=a_{k+3}\pmod{12}.
]
By CRT `C24=C8 x C3`: modulo 8, all even-index `a_k` agree, all odd-index values agree, and their difference may be 0 or 4; modulo 3, opposite index pairs `{0,3},{1,4},{2,5}` may take three independent values. After quotienting only the legitimate global centre gauge `a_k=t,b_l=-t`, the remaining fibre has size
[
 \boxed{2\cdot 3^2=18}.
]
Thus the full 36-route terminal-observer map has exactly `24*18=432` parameter differences in its kernel, of which 24 are ordinary centre gauge; **18 physically distinct additive laws survive modulo gauge**. The result concerns these terminal precision observers; it does not declare the BRC histories themselves redundant.

**Concrete counterlaw.** Relative to the compensated baseline of Unit248 set `a=(0,16,0,0,16,0)` and `b=(0,8,0,0,8,0)` in `C24`. Every original shortest terminal reading is unchanged, but the directed centre loop `x0->P->x2->x1->x0` changes its C24 readout by `8`. In particular, agreement of the 36 original terminal measurements would not establish universal centre compensation.

## Theorem 250B — exactly two extra elementary loops, eight signed events total, repair the observer

Keep the same calibrated ring and an additive Port law common to all 36 contexts. Measure the **single-triad** ordered closed loops

[
\begin{aligned}
T_1:&\quad x_0\to P\to x_2\to x_1\to x_0,\\
T_2:&\quad x_2\to P\to x_4\to x_3\to x_2.
\end{aligned}
]

Each uses two explicitly directed centre steps plus two signed reverse ring steps: four native primitive events per loop, eight in total. Subtract the known ring increment to obtain the centre sums `alpha_0+beta_1` and `alpha_1+beta_2`.

Within the original 36-trace collision fibre, these impose `a0=a1` and `a1=a2` modulo 24. The three formerly independent mod-3 components are thereby identified, and the one remaining mod-8 parity difference is removed. Every `a_k` becomes equal modulo 24; equivalently, only the 24-element physically unobservable centre gauge survives. Exact counts from the independent finite checker: 18 normalized laws before extra measurements, **3** after `T1`, **1** after both. The full-star centre parameters are therefore reconstructed up to gauge from the original 36 terminal readouts plus these two additional scalar readouts.

**Sharp restricted event cost.** Under the class of additional elementary one-triad, single-centre-passage same-Cell loops with one terminal scalar reading each, at least two new readouts are required: the original fibre has a `C3^2` factor, whereas a single `C24` scalar has only one `C3` factor. A same-entry/exit two-event centre loop repeats an already observed original diagonal and adds no rank. Any informative off-diagonal loop requires at least two extra signed ring steps, hence at least four primitive events. Consequently the `T1,T2` total cost `8` is minimal **in this declared experiment class**. No lower bound is asserted for a different apparatus that measures several independent internal coordinates at once.

## Actual reproducible check and experimental handoff

The standalone JS checker embeds all 36 exact original `(ingress,egress,centre-passages)` rows, verifies them against `12/gcd`, enumerates the 18 normalized CRT ambiguity classes, checks all 36 original C24 endpoint equations, tests each possible single additional loop, and certifies the two-loop repair and explicit counterlaw. It executed in the present V8 environment with **800 exact integer assertions, zero mismatch**. It is algebraic source-certificate replay, not a native Port benchmark or physical precision measurement.

**Next physically decisive action:** source-admit a genuine signed intact-triad Cell/Link/Port rule, guard/occupancy and independent C24 precision sensor. If the 36 Unit249 source routes can actually be executed with one stable Port law, measure their labelled endpoint deltas; then execute `T1,T2` with original signed BRC chronological step receipts and measure the two additional C24 deltas. Evaluate the additive-law assumption against the full 36 joint contexts and report any environment-dependent residual rather than forcing it into a centre gauge. Native protected semantic PROGRESS still requires this Research lane's actual winning CLAIM/run; issue #2903 is separate from mathematics.

Prior Units233–249, Unit249 hash repair, original Unit245 36-route benchmark and the separate R063 six-file native benchmark remain preserved and are not rerun here.
