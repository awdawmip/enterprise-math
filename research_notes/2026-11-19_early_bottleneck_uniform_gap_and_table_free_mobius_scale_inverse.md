# 2026-11-19 早期瓶颈重访：零阶粗因子矩的统一分离界、免全表反演与未来保真边界

Evidence: AUTHOR_SIDE_SYMBOLIC_PROOF / HIGH_PRECISION_FINITE_RECALCULATION / UNREVIEWED / NOT_NATIVE_RESULT_ADMISSION / NOT_V2_TASK_PUBLICATION.  
Date: 2026-11-19 (+08). Scope: RH auxiliary first-cosine arithmetic observer; **not** a Heartbeat native-X6 or BRC–Shor arithmetic attribution. This note does not alter P000, an immutable task pin, an old negative result, a CLAIM, or an owner.

## 0. Fixed history, actual sources, and question

Account rules read at `awdawmip/chatgpt-global-knowledge@58d5ff6f17af598b8f17c6df72554b1fabfa8755`: `00_BOOTSTRAP.md`, `OPERATING_MANUAL.md`, Enterprise Math project bootstrap, P000 and ACTIVE worldview, mathematics and BRC/residual policy. The starting Enterprise Math control/research reading was at `awdawmip/enterprise-math@3ba73bb040cd0cadd5580d80b3dcf9603b91b9bc`; original science references keep their own immutable versions.

Early/negative provenance:
- `research_tasks/R019_P018_PRECISION_OBJECT_SEMANTIC_REAUDIT_20260811.md`: precision quotient and full future-operation state require distinct typing; no blanket dynamic closure from static representation.
- `research_notes/RH_SQUAREFREE_ALPHA_GRAM_RANK_ONE_BOTTLENECK_20260908.md`: positive Gram/alpha-integral route has a large positive pole ground mode; its failed L2 estimate is preserved.
- `research_notes/RH_CRITICAL_ROUGH_ARITY_POSITIVE_HISTOGRAM_GAUGE_20260908.md`: exact finite Euler gauge produces a positive rough-factor histogram with parity readout, but does not prove RH.
- `research_notes/RH_ROOTED_FACTORIAL_DEPTH_SHARPNESS_20260907.md`: critical positive path-capacity depth is power-sharp; not signed cancellation.
- 2026-10-29 historical lower-bound draft `awdawmip/enterprise-math@9bce0563395c812cf1bb92dff8d991ffba1f51f2:research_notes/early_bottleneck_revisit_20261029_c5a31e/REVIEW_AND_CANDIDATE.md`: fixed low-degree **linear**, scale-independent moments do not recover the rough-parity observer on all subscales. Its scope is retained.
- `research_notes/2026-11-05_early_bottleneck_rough_moment_scale_fingerprint_and_cost.md`: first proved the zero moment is injective in the scale T with `M0(T+1)-M0(T)>1/(T+1)^3`, and described a naive O(N²)-work precomputed table. That result is the direct parent of this note.
- `research_notes/early_bottleneck_revisit_20261112_c6_rational_precision.md` plus `research_notes/driver/2026-11-12_x6_cyclic_phase_transfer_sharp_four_start_tomography.md`: a **different** six-phase full-boundary BRC observer permits bounded-rational recovery, with an exact three-origin collision. Native X6 realization is still an independent requirement.
- `research_notes/BRC_FIXED_RESIDUE_WHEEL_COMPLEXITY_BOUNDARY_20260906.md`: nonempty fixed finite residue wheels retain Theta(T) candidates, so a fixed wheel does not reduce the search exponent.
- `research_notes/BRC_RESIDUAL_CLASSIFICATION_NUMERIC_SORT_COMPLEXITY_20261105_b0e94005.md`: residual-first ordering and numeric reconstruction have a stated root-extraction cost; distribution-specific speed is not a general sorting lower-bound breakthrough.

Existing immutable V2 scopes checked on 2026-11-19: `RS-ROUGH-PARITY-LOCAL-STATE-UPDATE-20261101` (publication `TP2-13B36639D27B58C98C02`), `RS-BRC-FUTURE-FAITHFUL-INTEGRATION-20261028` (`TP2-8FD66B1B48BE87DA1AC1`), `RS-P018-TERNARY-CARRY` (`TP2-674C46ECF01DD1D3E6F4`), and `RS-BRC-SORT-SCALING-ROBUSTNESS-20261111` (`TP2-EA4165D1BAD15EE8DDC3`). Static publications do not establish live owner/claim; native exact control requests are tracked independently.

This work asks two narrower questions left untested by the November 5 note: **Is the numerical scale-fingerprint gap actually uniform in T? Can the inversion be performed without enumerating all scales?** These are auxiliary arithmetic/algorithmic questions, not another RH equivalent criterion or a native time law.

## 1. A uniform absolute separation theorem

Let `mu` denote the ordinary Möbius function. For each positive integer `T`, set

```
M0(T) = sum_{1 <= n <= T, mu(n)^2=1} cos(pi*n/(2*T)).
```

**Theorem (scoped, author proof).** For all integers `T >= 1`,

```
M0(T+1) - M0(T) > 2^(-24).
```

**Proof.** Each old summand is nondecreasing as `T` increases: for `1<=n<=T`, `cos(pi*n/(2s))` has positive derivative in real `s>=T`. The new endpoint `n=T+1` contributes zero. Thus no summand has a negative increment.

For `1<=T<=255`, use the previously established bound `M0(T+1)-M0(T)>1/(T+1)^3 >= 1/256^3 =2^(-24)`.

Now assume `T>=256` and let `I={ceil(T/2),...,T}`, `L=|I|>=T/2`. Any nonsquarefree n in I is divisible by some `d^2`, `2<=d<=sqrt(T)`. The union bound gives
```
#non-squarefree in I
 <= sum_{2<=d<=sqrt(T)} (L/d^2+1)
 <= (3/4)*L + sqrt(T).
```
Indeed `sum_{d=2}^infinity d^(-2) <= 1/4+integral_2^infinity x^(-2)dx=3/4`.
Consequently,
```
#squarefree in I >= L/4-sqrt(T) >= T/8-sqrt(T) >= T/16
```
because `sqrt(T)<=T/16` for `T>=256`.

For each squarefree `n in I`, consider `f_n(s)=cos(pi*n/(2s))` for `s in [T,T+1]`. Then
```
f_n'(s) = [pi*n/(2*s^2)] sin(pi*n/(2*s))
         >= [pi*T/(4*(T+1)^2)] sin(pi/8),
```
since `n>=T/2`, `s<=T+1`, and `pi*n/(2s)>=pi/8`. The fundamental theorem of calculus and the `T/16` surviving terms imply
```
M0(T+1)-M0(T)
 >= [pi*sin(pi/8)/64]*(T/(T+1))^2
 >= pi*sin(pi/8)/256
 > 2^(-24).
```
Here the last inequality is elementary (the left constant is about 0.004696). The claim follows for all T. QED.

Thus, **unlike the 2026-11-05 inverse-separation estimate, the needed absolute comparison gap is independent of N**. This says nothing about the integer part of M0, evaluation precision, information required for parity, or cost of generating observations.

## 2. Exact Möbius-sieve/finite-cosine reduction: no N-row table

Use the classical squarefree-divisor identity `mu(n)^2=sum_{d^2|n}mu(d)`. With `m_d=floor(T/d^2)` and `theta_d=pi*d^2/(2T)`, the following **finite equality** holds for each positive integer T:
```
M0(T)
 = sum_{d=1}^{floor(sqrt(T))} mu(d) * sum_{k=1}^{m_d} cos(k*theta_d)
 = sum_{d=1}^{floor(sqrt(T))} mu(d)
     * sin(m_d*theta_d/2)*cos((m_d+1)*theta_d/2)
       / sin(theta_d/2).
```
All denominators are nonzero because `0<theta_d<=pi/2`. This is a standard finite trigonometric-series identity after exact Möbius inversion, **not** a BRC-native phase computation and not claimed as a new classical identity. It removes explicit summation over every `n<=T` from the scalar evaluation interface; there are `floor(sqrt(T))` outer terms.

The right-hand side is exact as a real expression. A floating evaluation is *not* automatically an interval certificate. Near d=1 and large T, denominator and cancellation demand internal guard precision depending on T, plus rigorous trig and pi error bounds.

## 3. Finite-scale inverse without a table: conditional certified algorithm

Fix an integer bound `N>=1`. Suppose an input `z` is supplied with **certified** `|z-M0(T_*)|<=delta/8` for an unknown integer `T_* in [1,N]`, where `delta=2^-24`. Precompute or on demand sieve `mu(d)` through `floor(sqrt(N))`. At each binary-search midpoint `t`, use the formula in §2 and externally directed, rigorously bounded real arithmetic to compute `v_t` with `|v_t-M0(t)|<=delta/8`. Then:

- if `|z-v_t|<=delta/2`, output t: equality gives at most `delta/4` error, while a different integer scale gives at least `3delta/4`;
- otherwise the sign of `z-v_t` selects the larger/smaller half because `M0` is increasing.

This recovers `T_*` with `O(log N)` certified evaluations of the finite formula, each `O(sqrt(N))` transcendental subexpressions. In a variable-bit-cost model, write the total as
```
O( sqrt(N) log N * C_trig(B(N)) + C_sieve(sqrt(N)) )
```
where `C_trig(B)` is the bit cost to certify each elementary trig expression at sufficient precision B, including argument reduction and errors, and `B(N)=O(log N)` guard bits are **a planned sufficient scale**, not an executed rigorous interval implementation. Output scale and every M0 value require `O(log N)` integer bits. For stored nearest-fixed-point scalar readouts, **26 fractional bits** suffice in theory (`2^-27=delta/8` maximum rounding error), provided the underlying calculation is itself certified to that absolute accuracy. This includes no full N-row table.

If the original input already contains T, running this inverse is redundant. If the goal is to evaluate the signed rough-parity observable, the procedure does not compute it; its generation, BRC provenance and output recovery must be accounted for separately. This algorithm is sublinear in N in the *number of exact-formula summands* and still exponential in the bit length `log N`. It is not a general RH algorithm.

## 4. Small exact future-safety witness (parity is not in M0)

At T=4, compare two prime cutoffs, y=2 and y=3. Squarefree numbers are 1,2,3, so the positive M0(4) is identical for either cutoff. The parity observation differs by the exact nonzero quantity
```
P_3(4)-P_2(4) = 2*cos(3*pi/8) = sqrt(2-sqrt(2)) > 0.
```
Here `P_y(T)=sum_{n<=T,mu(n)^2=1}(-1)^{#{p|n:p>y}}cos(pi*n/(2T))`. Changing y is an explicitly declared observer-operation change, not an automatic native-X6 operation. The witness shows that a scale-only M0 state, even perfectly inverted, is not sufficient for the family of parity observations indexed by y. A genuinely future-safe quotient needs a suitable prime-label/residual repair; it is not supplied by scale injection.

This is an elementary *finite* exact obstruction within the chosen future-operation/observer family, not a blanket impossibility for every nonlinear representation.

## 5. Reproduction performed and evidence limits

On 2026-11-19, an independently written high-precision Python `mpmath` implementation (65 decimal digits, but **not a directed-rounding proof**) compared the direct squarefree cosine sum against the Möbius closed formula for
`T=1,2,3,4,9,11,30,63,128,256,999,2000`. Maximum observed absolute discrepancy was about `1.22e-63`. Sample numerical gaps: T=9, 0.3033003837; T=255, 0.3909820267; T=256, 0.3872294826; T=512, 0.3915952313. The symbolic proof in §1 is the universal evidence; these finite checks only help detect formula mistakes. The precision-certified bisection of §3 **was not executed**; its availability is a proposed implementation and proof obligation.

## 6. Restart decisions, distinct directions, costs and kill criteria

A. **RH / non-linear scale observer.** 2026-11-05 gave a separation of order `N^-3` and an expensive full table. The new uniform separation and closed-form oracle change the **numerical representation/decoder** feasibility judgment. Small experiment: implement outward-rounded or interval-certified trigonometric sums with target `delta/8`, run scales through `N=10^5` with hidden T and compare to direct summation; account for all sieve, trig, guard-bit, binary-search, input-observation and final output costs. PASS only for certified reconstruction with the stated cost; FAIL for an explicit unsound interval, missed boundary, or full-table dependence. For RH parity improvement require a separate proven parity-labelled state and full future-operation/cost comparison. This work is most naturally a scoped **addition to the existing 2026-11-05 note and/or existing rough-parity task**, not a renamed new RH Task.

B. **P018/P023 and future-safe quotient.** Historical semantic mismatch remains real for an observer used as a future state. Available type-safe and finite-operation quotient tools can express the distinction, but the T=4 counterexample forbids discarding y-parity state for that observer family. Small experiment: retain y and the smallest useful labelled residual, then test one and two prime-insertion operations and all declared subscales, with counterexample preservation and per-update cost. Existing `RS-ROUGH-PARITY-LOCAL-STATE-UPDATE-20261101`, `RS-P018-TERNARY-CARRY`, and `RS-BRC-FUTURE-FAITHFUL-INTEGRATION-20261028` already cover adjacent formal scope; no duplicate task from this note.

C. **BRC fixed wheel and residual sorting.** The fixed-wheel Theta(T) negative result remains true, and scaling/total-cost tasks are already registered. Separate possible future gain: an adaptive **nonperiodic, provenance-retaining** multi-point certificate with measured end-to-end amortization. A fixed wheel or a different label is not a valid exponent improvement. Existing owner and prior-art checks must precede any successor publication.

D. **C6 X6 finite-precision observer.** Four registered full boundary matrices do identify six bounded-rational phase weights with logarithmic precision in H at the algebraic layer; the three-origin collision is exact. The substantive still-open question is native typed BRC construction and future concatenation fidelity, already overlapped by the X6 rotation/port tasks. Do not claim the algebraic decoder is native physical dynamics.

**Publication decision at this scientific boundary:** no new formal Task is justified on the present evidence without a distinct target beyond the existing scopes and full current owner/dependency reconciliation. A research note is a reusable, *non-executable* evidence artifact. Any later independent publication needs a genuine new information gap, an actual true service-issued publisher identity, current claim/owner checks, full canonical V2 preflight and a single immutable taskbook/publication record transaction. No task claim or review is asserted here.

The scoped significance of the new result is: `uniform O(1) numerical gap + no-full-table scale inverse` is a better representation and finite arithmetic algorithm for the RH auxiliary **scale fingerprint**, while the signed-parity bottleneck remains a separate problem.
