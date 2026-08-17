# R059D Stage AP REISSUE — Signed-Origin One-Step Segment Sweep Proof

Researcher: `EM-R059D-APR-7E4C2B`

Task: `RS-R059D-STAGE-AP-REISSUE-SIGNED-ORIGIN-ONE-STEP-SEGMENT-COLLAPSE-CLOSURE`

Source taskbook: `398e6a466ca87c78a8d9e2aed639e3964d1769c4`

The old length-2 task is superseded and is not used as a theorem premise.

## 1. Signed-origin one-step class

The native origin is one glued state `O_E=[+1]=[-1]`; native coordinate `0` does not exist.

Use the allowed auxiliary chart only for proof bookkeeping:

`ENC(0)=O_E`,

`ENC(k)=sign(k)(|k|+1)` for `k!=0`,

with inverse `DEC`.

For an auxiliary channel state `d=(u,v,w)` define the AP primitive channel budget

`B(d)=|u|+|v|+|w|`.

This is a target operational budget, not source Euclidean distance. A one-step AP endpoint has `B(DEC(P))=1`.

Hence the one-step endpoint class is exactly the six channel units

`d0=(1,0,0)`,

`d1=(0,-1,0)`,

`d2=(0,0,1)`,

`d3=(-1,0,0)`,

`d4=(0,1,0)`,

`d5=(0,0,-1)`.

Encoding gives the native cycle

`(2,1,1)`, `(1,-2,1)`, `(1,1,2)`, `(-2,1,1)`, `(1,2,1)`, `(1,1,-2)`.

Define the 60-degree target rotation on the auxiliary channel scaffold by

`R6(u,v,w)=(-w,-u,-v)`.

Then `R6(d_k)=d_(k+1)`, `R6^3=-Id`, and `R6^6=Id`.

## 2. Source compatibility sweep

Source geometry is used only to expose the competition fiber after the target one-step class is fixed.

In the first sector from `d0=+u` to `d1=-v`, write a unit source direction as

`X(theta)=A(theta)d0+B(theta)d1=(A,-B,0)`

for `0<=theta<=pi_source/3`, where

`A(theta)=cos(theta)-sin(theta)/sqrt(3)`,

`B(theta)=2 sin(theta)/sqrt(3)`.

This is the exact two-axis decomposition of a source unit direction between adjacent 60-degree axis rays.

At the endpoints:

`(A,B)=(1,0)` and `(0,1)`.

For every open-sector orientation,

`0<A<1`, `0<B<1`.

Therefore the complete adjacent integer box is exactly

`{0, d0, d1, d0+d1}`.

There are no internal transition boundaries: the box is constant throughout the open source arc. D6 transport gives the same statement in all six sectors.

Thus hidden competition is not a small-probability event under continuous angular measure. It occupies every open sector; only the six axis directions are noncompeting boundaries.

## 3. Mandatory M_UP correction

The coherent all-upper completion of the first-sector input is

`d0+d1=(1,-1,0)`.

Its native encoding is `(2,-2,1)`.

D6 transport gives the actual upper sextet

`(2,-2,1)`,

`(1,-2,2)`,

`(-2,1,2)`,

`(-2,2,1)`,

`(1,2,-2)`,

`(2,1,-2)`.

By contrast the user-specified sextet decodes to

`2(d_k+d_(k+1))`.

That requires auxiliary channel magnitudes `2`, but every active one-step source coefficient has magnitude strictly less than `1` in the open sector. An adjacent integer completion can therefore never reach magnitude `2`.

Hence the mandatory `M_UP` sextet has empty source fiber and zero probability under every source measure. It is neither a positive-measure event nor an isolated tie.

The qualitative upward-inflation idea survives, but the magnitude is one native level too high.

## 4. Coherent UP and DOWN

The full componentwise integer box has four corners. To formalize a single collapse *direction*, define the coherent coupled class: all active noninteger channels share one branch bit.

- `DOWN`: every active magnitude chooses the lower value toward the signed origin.
- `UP`: every active magnitude chooses the upper value away from the signed origin.

Therefore on every open sector:

`DOWN_raw=0`,

`UP_raw=d_k+d_(k+1)`.

The two axis corners `d_k` and `d_(k+1)` are preserved as a broader componentwise-policy control but are not coherent all-lower/all-upper results.

The primitive budgets are

`B(DOWN_raw)=0`,

`B(d_k)=B(d_(k+1))=1`,

`B(UP_raw)=2`.

The one-step class is `B=1`.

Thus coherent UP immediately leaves the one-step class. The user `M_UP`, if manually inserted, has budget `4` and is even farther outside the one-step class, but it is not a reachable AP competitor.

## 5. Axis completion

Axis completion is defined before the closure proof.

After collapse let `raw` have budget `B(raw)`. The missing one-step budget is

`m=1-B(raw)`.

Completion is allowed only for `m>=0`; it can fill a deficit but cannot delete overlength budget.

The target turn state already contains the sector `k` and turn orientation. Therefore the encountered axis is local target data:

- forward sector `k`: exit axis `d_(k+1)`;
- reverse sector `k`: entry axis `d_k`.

Define

`COMPLETE(raw,k,eps)=raw+m*axis_encounter(k,eps)`.

For coherent DOWN, `raw=0`, `m=1`, so forward completion is exactly `d_(k+1)`.

For coherent UP, `B=2`, so `m=-1`; completion is undefined. Repairing UP would require a new contraction rule, not axis completion.

The auxiliary zero is an internal precompletion chart state only. The composed turn stores the completed native anchor; native coordinate zero is never stored.

## 6. Full orbit

Starting from `d0`, the composed forward turn is

`d_k -> DOWN_raw=0 -> COMPLETE -> d_(k+1)`.

Therefore the stored endpoint cycle is

`d0,d1,d2,d3,d4,d5,d0`.

Every stored endpoint has budget `1`. The six states are distinct and `R6` has order six, so there is no premature return and the minimal positive period is `6`.

Reverse orientation uses `R6^{-1}` and gives the inverse cycle.

After signed encoding, the endpoint orbit is exactly `A1`. There are no additional legitimate one-step endpoint states.

This answers the user question precisely: the visible endpoint orbit really is only six axis points, but the hidden source competition/collapse fiber is nontrivial.

## 7. Necessity scope

Within the coherent coupled collapse class, DOWN plus axis completion is necessary and sufficient.

Necessity: at the first coherent UP sector the budget jumps from the required `1` to `2`; deficit-only axis completion cannot repair it.

Sufficiency: coherent DOWN always gives budget `0`, and the unique missing unit is completed along the encountered target axis, producing the next one-step anchor.

However this necessity does not hold in the larger independent componentwise completion class. The axis corner `d_(k+1)` is itself in the full adjacent integer box and already has budget `1`. A direct-forward-axis policy can choose that corner each sector and traverse the same six-cycle without a raw DOWN state.

Therefore the exact missing axiom for unqualified necessity is:

`COHERENT_COUPLED_COLLAPSE_DIRECTION`.

The final theorem must always state this scope.

## 8. Radius-1 legacy conjugacy

Define

`Psi(u,v,w)=(u-w,w-v)`.

Then

`Psi(d0..d5)=((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1))`,

the accepted auxiliary radius-1 AK D6 endpoint cycle.

Moreover

`Psi(R6 d)=R(Psi(d))`,

where `R(a,b)=(-b,a+b)` is the legacy AK rotation.

Thus endpoint graph, turn order, D6 action, reversal, one-step/radius-1 label, and period 6 are conjugate.

The source competition box, raw DOWN origin, coherent UP mixed state, and axis-completion factorization are new AP-reissue semantics. They are not present as hidden states in the legacy AK runtime.

## 9. Final status

Proved:

- hidden non-axis competition exists on every open source sector;
- the actual coherent UP sextet has native magnitude `±2` in its active channels and primitive budget `2`;
- user `M_UP` with `±3` active channels is not reachable and has zero fiber;
- coherent UP causes one-step length inflation;
- coherent DOWN plus local axis completion produces the exact six-axis one-step orbit;
- DOWN+completion is necessary and sufficient inside the coherent coupled class;
- unqualified necessity is false in the broader independent componentwise branch class;
- visible signed-origin orbit is conjugate to legacy auxiliary radius 1.

No later stage is consumed.
