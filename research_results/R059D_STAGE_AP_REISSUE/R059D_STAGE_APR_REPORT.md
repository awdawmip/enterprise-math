# R059D Stage AP REISSUE — One-Step Signed-Origin Collapse Report

Researcher-ID: `EM-R059D-APR-7E4C2B`

Task: `RS-R059D-STAGE-AP-REISSUE-SIGNED-ORIGIN-ONE-STEP-SEGMENT-COLLAPSE-CLOSURE`

Owner branch: `research/r059d-stage-ap-reissue-one-step-segment-collapse`

Taskbook source: `398e6a466ca87c78a8d9e2aed639e3964d1769c4`

The old length-2 task is superseded and was not executed.

## Primary disposition

`ONE_STEP_HIDDEN_COMPETITION_PROVED__DOWNWARD_AXIS_COMPLETION_NECESSARY_AND_SUFFICIENT_FOR_FULL_ORBIT`

Scope qualifier:

`NECESSARY_AND_SUFFICIENT_WITHIN_APR_COHERENT_COUPLED_COLLAPSE_CLASS`.

Unqualified necessity in the broader independent componentwise branch class is false; the missing axiom is explicitly identified below.

## 1. One-step target class

With the signed origin `+1 ≡ -1 ≡ O_E`, define the allowed auxiliary decoding and primitive channel budget

`B(u,v,w)=|u|+|v|+|w|`.

The one-step target class is `B=1` and therefore consists exactly of six native axis anchors:

`(2,1,1)`, `(1,-2,1)`, `(1,1,2)`, `(-2,1,1)`, `(1,2,1)`, `(1,1,-2)`.

This freezes the segment as one primitive step; native magnitude `2` at an axis anchor is not primitive length 2.

## 2. Exact source sweep

In a first 60-degree source compatibility sector, use

`X(theta)=(A(theta),-B(theta),0)`

with

`A=cos(theta)-sin(theta)/sqrt(3)`,

`B=2 sin(theta)/sqrt(3)`.

On the open sector, exactly

`0<A<1`, `0<B<1`.

Hence the complete adjacent integer box is constant on the whole open sector:

`{0, d_k, d_(k+1), d_k+d_(k+1)}`.

Thus hidden competition exists on every open source sector. Under normalized uniform source angle it has measure 1; the six axis boundaries have measure 0. This is source-measure information, not native probability.

## 3. Mandatory M_UP verdict

The user-specified sextet

`(3,-3,1)`, `(1,-3,3)`, `(-3,1,3)`, `(-3,3,1)`, `(1,3,-3)`, `(3,1,-3)`

decodes to auxiliary states with active channel magnitude `2`.

Because every active one-step precollapse coefficient has magnitude strictly below `1`, adjacent integer completion can only use magnitude `0` or `1`.

Therefore:

`M_UP_SOURCE_FIBER = EMPTY`.

The user sextet has zero exposure, not small positive exposure and not an isolated tie.

The actual coherent UP sextet is one native level lower:

`(2,-2,1)`, `(1,-2,2)`, `(-2,1,2)`, `(-2,2,1)`, `(1,2,-2)`, `(2,1,-2)`.

Its auxiliary primitive budget is `2`, whereas the one-step class has budget `1`.

The user `M_UP`, if manually inserted, would have budget `4` and is even more overlength, but it is not a reachable one-step competitor.

## 4. UP / DOWN

For a single coherent collapse-direction bit shared by every active fractional channel:

- `DOWN` sends every active coefficient toward origin, giving raw auxiliary `0`;
- `UP` sends every active coefficient outward, giving `d_k+d_(k+1)`.

This definition is frozen before any closure argument.

UP immediately changes primitive budget from the required class `1` to `2`, proving one-step length inflation.

## 5. Axis completion

The local completion rule uses only the target deficit and discrete turn state.

For raw state `c`, let

`missing = 1-B(c)`.

Completion is allowed only for `missing>=0` and only adds the missing number of primitive channel units along the encountered target axis:

- forward sector k: exit axis `d_(k+1)`;
- reverse sector k: entry axis `d_k`.

Thus coherent DOWN has raw budget `0`, missing budget `1`, and completes to the next axis anchor. Coherent UP has budget `2`, negative missing budget, and cannot be repaired by a deficit-only completion.

The raw auxiliary zero is internal only; the composed target turn stores no native coordinate zero.

## 6. Full one-step orbit

Starting at `(2,1,1)`, forward DOWN+completion gives exactly

`(2,1,1)`
`-> (1,-2,1)`
`-> (1,1,2)`
`-> (-2,1,1)`
`-> (1,2,1)`
`-> (1,1,-2)`
`-> (2,1,1)`.

Every stored endpoint remains in `L_E=1`, D6 order is respected, there is no premature return, the minimal period is `6`, and reversal gives the inverse cycle.

Therefore the visible endpoint orbit really is exactly the six axis anchors. The more complicated part is hidden in the source competition / raw-collapse / completion factorization.

## 7. Necessity theorem and its boundary

Within `APR_COHERENT_COUPLED_COLLAPSE_CLASS`, DOWN+axis completion is necessary and sufficient:

- first coherent UP immediately gives budget `2`;
- every coherent DOWN has deficit `1`, and the local encountered-axis completion gives the unique next one-step anchor.

However, the full adjacent integer box also contains the two axis corners `d_k` and `d_(k+1)`. If independent per-channel lower/upper decisions are admitted, a `DIRECT_FORWARD_AXIS` policy can choose `d_(k+1)` directly and close the same six-cycle without a raw DOWN state.

Hence unqualified necessity is false in the broader componentwise class.

The exact additional axiom needed for the scoped necessity theorem is:

`COHERENT_COUPLED_COLLAPSE_DIRECTION` — one collapse event has one shared direction bit across all active noninteger channels.

## 8. Radius-1 signed-origin conjugacy

With

`Psi(u,v,w)=(u-w,w-v)`,

the six decoded A1 anchors map to the legacy AK radius-1 cycle

`(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)`.

Moreover `Psi(R6 d)=R(Psi(d))` for `R6(u,v,w)=(-w,-u,-v)` and legacy `R(a,b)=(-b,a+b)`.

Therefore endpoint graph, turn order, D6 action, reversal, one-step/radius-1 label and period are conjugate.

The hidden source competition box and DOWN/axis-completion factorization are new AP-reissue semantics and are not claimed to have been hidden legacy AK runtime states.

## 9. Exact answers to the taskbook questions

1. Non-axis competition states exist: **yes**, on every open source sector.
2. The specified `M_UP` has positive measure: **no; empty fiber**.
3. If the specified `M_UP` were forced, length exceeds one: **yes, budget 4**, but it is unreachable.
4. Exact coherent DOWN competitor: **the signed origin**, auxiliary budget 0.
5. Axis completion: **fill only the missing target primitive budget along the encountered target axis encoded by sector/orientation state**.
6. DOWN+completion closes: **yes**, period 6.
7. Final native endpoint orbit: **exactly A1**, no extra legitimate one-step endpoints.
8. DOWN necessary: **yes within the coherent coupled collapse-direction class; no in the broader independent componentwise branch class**.

## 10. User-hypothesis correction

The qualitative mechanism is substantially right: visible six-axis orbit, hidden nontrivial collapse competition, UP overlength, DOWN plus local completion closes.

Two quantitative parts are false:

- competition is not small-probability under continuous angular sweep; it is full open-sector measure;
- the actual UP competitor is the `±2` mixed sextet, not the `±3` mandatory sextet.

So the strongest theorem is combined with the explicit correction flag:

`USER_M_UP_MAGNITUDE_HYPOTHESIS_FALSE__TRUE_UP_SEXTET_ONE_NATIVE_LEVEL_LOWER`.

## 11. Validation

Independent deterministic replay was frozen after theorem statements:

- dense `4096` subdivision per source sector;
- every A1 anchor;
- actual UP sextet and mandatory M_UP sextet;
- coherent DOWN/UP on identical inputs;
- axis completion;
- forward/reverse cycles;
- broader componentwise direct-axis counterpolicy;
- radius-1 conjugacy regression on a bounded triaxial grid.

Expected frozen checker result before history gate:

`147638/147638 PASS`

digest

`c3d3103f28ee56c69de0ca57f504cc74c0b4e428214c9f3b8183a6f2adeb2647`.

Finite sweep is implementation evidence only; positive-measure, length, closure and necessity statements above are symbolic/finite-state theorems.

Stop for Driver review. No later stage is consumed.
