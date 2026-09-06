# X6 triadic force-quantum multiplicity lift V2: exact completion defects for apparent unequal forces

Status: `FREE_RESEARCH / EXACT INTEGER DERIVATION / NOT_FOUNDATION`
Date: `2026-09-06`
Task: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`
Consumes:
- P000 primitive force quanta and triadic closure;
- V1 equal-unit triadic decomposition theorem.

## 1. Why multiplicity comes before a new magnitude primitive

P000 defines `PRIMITIVE_FORCE_QUANTUM` and the minimum stable nonzero primitive event as a triadic closure. It does not yet supply an independent native real-valued force-magnitude field.

Therefore the strongest currently justified first model of an apparent stronger/weaker force is an **integer population of primitive force quanta**. A continuous/effective force magnitude may later be calibrated to this population, but that calibration is not assumed here.

Let

`d=(d_1,...,d_6) in N_0^6`

record the number of force-quantum occurrences carried by each underlying native axis. Signed occurrence labels remain provenance; the existence criterion depends only on underlying-axis degree because one restricted equal-unit triad may use any sign pattern but may use one underlying axis at most once.

## 2. Recalled exact decomposition criterion

A population `d` can be decomposed into `m` restricted equal-unit triadic closures, each using three distinct underlying axes, iff

`sum_i d_i = 3m`

and

`max_i d_i <= m`.

This is the degree-sequence theorem from V1.

## 3. Minimal global augmentation theorem

Suppose additional primitive force quanta may be supplied on any of the six axes. Define

`S=sum_i d_i`,

`M=max_i d_i`,

and

`m_* = max(M, ceil(S/3))`.

Then the minimum number of additional quanta needed to reach a triad-decomposable population is

`h_* = 3 m_* - S`.

### Proof

Any completed population decomposed into `m` triads has total `3m`, so `m>=ceil(S/3)`. It must retain every original degree, hence `m>=M`. Therefore `m>=m_*` and at least `3m_*-S` additions are necessary.

For sufficiency choose `m=m_*`. Every coordinate has spare capacity `m-d_i >=0`; total spare capacity is

`sum_i(m-d_i)=6m-S`.

The required number of additions is only

`h=3m-S <= 6m-S`.

Hence distribute the `h` added occurrences among the coordinate capacities so the final degree of every axis is at most `m`. The completed total is `3m`, so the V1 criterion supplies a triadic decomposition. QED.

This defines an exact integer completion defect

`DEFECT_3(d)=3*max(max_i d_i,ceil(sum d_i/3))-sum d_i`.

`DEFECT_3(d)=0` iff the population is already triad-decomposable.

## 4. Hidden-axis lift when at most three axes are visible

Let an observer expose only a set `V` of `q<=3` native axes, with visible degree counts `d_i`, while additions are allowed only on the `6-q` hidden axes. Put

`S_V=sum_{i in V} d_i`,

`M_V=max_{i in V} d_i`.

Because `q<=3`, `S_V<=3M_V`. Any triadic completion must use at least `m=M_V` triads. At exactly this value the required hidden count is

`H_min = 3M_V - S_V`.

The hidden axes have enough capacity because there are at least three of them and each can occur at most once in each of the `M_V` triads.

Therefore

`HIDDEN_TRIADIC_LIFT_COST(V,d)=3M_V-S_V`.

This is a native integer count of missing primitive quanta, not a Euclidean force-vector residual.

## 5. Exact apparent two-force formula

For two visible force populations with counts `a,b>0`, let `M=max(a,b)` and `m=min(a,b)`.

The minimum hidden primitive-quanta count is

`H_2(a,b)=3M-a-b=2M-m`.

If `a=b=M`, then

`H_2(M,M)=M`.

Exactly one hidden underlying-axis family can carry all `M` hidden occurrences, yielding `M` parallel triads of type `{visible_i,visible_j,hidden_k}`.

If `a!=b`, then

`H_2(a,b)>M`.

No one hidden axis can appear more than once in each of the `M` triads, so one hidden axis has capacity only `M`. Hence an unequal apparent two-force pair requires **at least two hidden axis families** in this unit-quantum lift model.

Conversely two hidden axes suffice because `H_2<=2M`.

Thus:

- equal apparent pair -> minimum hidden axis-family count `1`;
- unequal apparent pair -> minimum hidden axis-family count `2`.

This sharpens the earlier one-quantum witness, where `a=b=1` gave one hidden quantum on any of 4 hidden axes and two signs, hence 8 lifts for the fixed signed observer.

## 6. Apparent three-force formula

For three visible counts `a,b,c>0`, let

`M=max(a,b,c)`.

The minimum hidden count is

`H_3(a,b,c)=3M-a-b-c`.

Therefore

`H_3=0`

iff

`a=b=c=M`.

So within the present equal-primitive-quantum semantics, a three-axis apparent force configuration closes using only those three visible axis families exactly when the three multiplicities are equal.

If they are unequal, at least one hidden-axis force population or a stronger interaction/magnitude law is required.

The minimum number of hidden axis families required is

`ceil(H_3/M)`

for `H_3>0`, hence at most two because `H_3<=2M`.

## 7. Single visible-force population

For one visible axis carrying `a` primitive quanta,

`H_1(a)=2a`.

At least two hidden axis families are necessary and sufficient: every one of the `a` primitive events must be completed by two distinct hidden-axis occurrences.

This is the integer triadic-lift counterpart of P000's statement that one primitive nonzero force is unstable.

## 8. Constructive lift algorithm

For a global degree vector `d`:

1. compute `m_*` and `h_*`;
2. add `h_*` quanta greedily to axes whose current degree is below `m_*`;
3. apply the V1 greedy triad decomposition, repeatedly selecting the three currently largest positive degrees.

The first phase terminates because the total coordinate capacity is at least `h_*`; the second phase is guaranteed by the exact degree criterion.

The output should preserve occurrence signs/token provenance rather than only the six degree totals when later operations can inspect them.

## 9. Nonuniqueness remains BRC data

Minimal completion need not be unique:

- the added hidden quanta can often be distributed among several hidden axes;
- a completed degree vector can have multiple triadic decompositions;
- signed occurrence assignments and temporal grouping can differ.

Therefore `DEFECT_3` or `H_min` is only a scalar completion cost. It is not a complete lift object.

A provenance-safe result is the family of minimal augmented populations together with their triadic decompositions, carried by Path-formal/BRC or another declared exact combinatorial carrier.

## 10. Boundary: continuous magnitude is still open

Nothing here defines a real-valued native force magnitude. The theorem covers integer multiplicity of primitive force quanta.

An external continuous force value may be mapped to quantum multiplicity only after a precision/unit calibration is supplied. Different resolutions may then correspond to different integer populations under P000 finite-resolution semantics.

Thus:

`INTEGER_FORCE_QUANTUM_MULTIPLICITY != CONTINUOUS_FORCE_MAGNITUDE_DEFINITION`.

If future evidence requires an intrinsic amplitude carried by one primitive quantum, that is a new typed layer and must not be backfilled into this theorem.

## 11. Current consequence

A large class of apparent unequal-force questions can already be translated without adding a new primitive magnitude:

`APPARENT FORCE COUNTS -> INTEGER QUANTUM DEGREE VECTOR -> TRIADIC COMPLETION DEFECT -> FAMILY OF HIDDEN/COMPOSITE TRIADIC LIFTS`.

The next hard step is physical calibration: relate observed force/impulse/stress quantities at declared resolution to these primitive quantum populations and event-time layers.
