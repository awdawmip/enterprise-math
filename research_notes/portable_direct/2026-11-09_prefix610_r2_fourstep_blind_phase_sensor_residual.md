# PREFIX-610-R2 — Four-step single-phase residual removes unknown BRC gate-free tail

Date: 2026-11-09 (Asia/Shanghai). Status: AUTHOR-SIDE EXACT DERIVATION + EXECUTED RATIONAL CERTIFICATES; independent Driver review pending.
Frozen scientific input: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Direct predecessors: PREFIX-602 common native-derived 16D tail (PR #1826); PREFIX-604 exact 12+4 split (PR #1828); PREFIX-605 four residue classes (PR #1830); PREFIX-609 paired controlled source recovery (PR #1838).

## 1. Precise BRC carrier and observer

Keep the frozen native X6 STAR source, its 48 phases, 96 two-bit ports and 576 individually tagged actions. Fix the source-axis weights `(1,1,1,1,0,0)`. The native-derived 48×48 phase-sum operator `Q(q)` is exactly defined in PREFIX-602 (nonnegative gate q), with marked phase g=4, zero-based. This note observes only the single phase-sum coordinate with zero-based index **3**. All branch provenance, port history and joint relations remain in the frozen source; the 16D reduction is used only for this exact linear observation under future gate operations.

After any two native-derived nonnegative gate updates, write the 48-phase state as `y_0 ∈ V=im(Q(1)^2)`; PREFIX-602 proved this shared image is 16-dimensional. PREFIX-604 supplies a fixed exact decomposition of the internal state `v=Wc+f`, `c∈Q^4`, `f∈Z_12`. Under arbitrary ordered gates `q_1,q_2,...,q_n≥0`:
- `c_t=B(q_t)c_(t-1)`, where `B(q)=[[0,0,0,4(q+3)],[1,0,0,0],[0,1,0,0],[0,0,1,0]]`;
- `f_t=T^t f_0`, and `T^4 f_0=16f_0`;
- `y_t=E(Wc_t+f_t)` and `(EW)[3,:]=(2,0,0,0)`.

For any initial state in V and real gates for which the algebra is defined, these identities hold. Nonnegative gates and nonnegative initial 48-phase states are the native positive BRC domain.

## 2. Theorem 610.1 — blind four-step annihilating sensor residual

Write `s_t=y_t[3]` and `r_t=s_(t+4)-16s_t`. For every integer `0≤t≤n-4` and arbitrary gate word (not necessarily constant),
```text
r_t = 8 (q_(t+4)-1) c_(t,0).                  (610.1)
```
The full 12D gate-independent contribution to the phase-3 sensor is canceled **exactly**, without knowing its initial coefficients, the first two gate parameters, or the initial 48-phase source. The formula needs two readings of the *same single physical phase-sum sensor* four transitions apart, within one trajectory.

**Proof.** Set `h_t=(ET^t f_0)[3]`. The common split yields `s_t=h_t+2c_(t,0)` and `h_(t+4)=16 h_t`. The four-cycle transfer identity gives `c_(t+4,0)=4(q_(t+4)+3)c_(t,0)`; the intermediate three gates affect other coordinates and do not enter this equality. Hence
```text
s_(t+4)-16s_t
  =2[c_(t+4,0)-16c_(t,0)]
  =2[4(q_(t+4)+3)-16]c_(t,0)
  =8(q_(t+4)-1)c_(t,0).
```
This is an exact identity for any horizon and all applicable initial states. QED.

For a **nonzero** `c_(t,0)`, `r_t=0 ⇔ q_(t+4)=1`. If `c_(t,0)>0`, the sign of `r_t` determines exactly whether `q_(t+4)` is less than, equal to, or greater than one. In particular, one phase-sum trace gives an unknown-source threshold detector under the stated excitation condition. If `c_(t,0)=0`, this particular residual vanishes for all values of `q_(t+4)`; that is a genuine sensor non-excitation fiber.

## 3. Theorem 610.2 — eight-step observer-only relation and calibrated gate propagation

For `0≤t≤n-8`, write `a=q_(t+4)` and `b=q_(t+8)`. Then
```text
r_(t+4) (a-1) = 4(a+3)(b-1) r_t.              (610.2)
```
**Proof.** Equation (610.1) gives `r_t=8(a-1)c_(t,0)` and `r_(t+4)=8(b-1)c_(t+4,0)`. The same four-step transfer makes `c_(t+4,0)=4(a+3)c_(t,0)`. Eliminating this hidden coordinate gives (610.2), including the zero cases. QED.

If a previously calibrated gate `a≥0` satisfies `a≠1` and `r_t≠0`, the next gate in the same residue class is recovered by
```text
q_(t+8) = 1 + (a-1)*r_(t+4)/(4*(a+3)*r_t).    (610.3)
```
Thus a calibrated nonunit gate in each mod-4 class supports observation-only propagation along that class until a zero residual / non-excitation event calls for new calibration. This is a concrete partial inverse method for unknown sources, different from the fully calibrated paired-probe method of PREFIX-609.

For unknown `f_0`, the constant 16 is also unique (up to scalar multiple) among nontrivial two-reading linear combinations `αs_(t+4)+βs_t` that universally eliminate `h_t`: because `h_(t+4)=16h_t`, one needs `16α+β=0`. Necessity has a nonzero native-derived witness: for the known increment `Q(0)Q(1)ones(48)`, PREFIX-609 computed `h_t=12*2^t`, so `h_t≠0`. This is a uniqueness statement only for the named two-sample linear annihilators, not for every possible sensor design.

## 4. Exact native rational verification

The accompanying stand-alone SymPy checker reconstructs the frozen original STAR phase indexing and `Q(q)`, the 48-to-16 intertwiner, the common 12+4 projector, and the original index-3 phase observer. It tests three nonnegative original source vectors against four gate words (nonnegative integers, exact rationals, zeros, unit gates), with horizons up to 18, and compares complete native-derived 48-phase trajectories with decomposed reconstruction.

Executed checks: **171** instances of (610.1), **123** of (610.2), **10** exact propagated gate recoveries, **10,512** exact original 48-phase reconstruction entries, and **219** nonnegative full phase states. All asserted equalities passed.

A concrete witness uses `y_0=Q(0)Q(1)ones(48)`, the gate prefix `(0,2,1,5)`, and gives
```text
s_0 = 21; s_4 = 480; c_(0,0) = 9/2; q_4 = 5.
r_0 = 480 - 16*21 = 144 = 8*(5-1)*(9/2).
```
The all-real parameter algebra is justified by the earlier exact matrix identities. These finite tests validate this implementation and examples, not a new independent Driver review.

## 5. Research significance, reuse, and next exact unit

This result uses the PREFIX-604 **existing** native-derived BRC linear observer and its gate-free fourth-power relation; reuse decision: `COMPOSE_APPLIED`, not a claim of a novel primitive BRC transport. The new deliverable is a time-shifted one-sensor residual equation that eliminates an unknown 12D nuisance component while retaining the precise 4D excitation factor.

Remaining mother-objective unit: characterize the actual unknown **shared two-step transient** `Q(a)Q(b)` acting on a known controlled source increment. In particular, derive the attainable set of `c_0,f_0` for this two-parameter family, and determine the minimum calibration to recover the *magnitude* of each `q_t` from one fixed sensor when zeros / unit gates occur. A second unit is an end-to-end original-96-port cost comparison with exact bit lengths and input preparation; the single phase-sum residual is not a claim about labeled branch history reconstruction.

Canonical status: independent author-side research note, exact computational checks executed; neither formal Task CLAIM nor Native Result / independent Driver acceptance / Foundation update is asserted. Native session / Owner checks are tracked separately by their actual receipts.
