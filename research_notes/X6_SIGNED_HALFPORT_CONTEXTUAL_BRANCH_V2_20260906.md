# X6 signed half-port and contextual branch selection V2

Status: `FREE_RESEARCH / EXACT EXTENSION / NOT_FOUNDATION`
Date: `2026-09-06`
Researcher: `EM-FREE-PI-PRIME-20260904 / FREE_AXIOM_DISCOVERY`
Task: `RS-X6-CELL-CHANNEL-INTERNAL-STATE`
Extends, without replacing:
- `X6_CELL_CHANNEL_INTERNAL_STATE_V1_20260906.md`;
- `X6_CHANNEL_FRAME_GAUGE_V1_20260906.md`;
- `X6_TRIADIC_ATOMIC_SCATTER_V1_20260906.md`;
- `X6_ROTATION_PATH_GROUPOID_V2_20260906.md`.
Checker: `experiments/x6_cell_internal_state_v2_20260906/check_signed_halfport_context.py`.

## 1. Why V2 is needed

V1 closed the finite 960/1920 triadic internal fiber and the 720-fold channel-frame gauge. Two exact interfaces remained implicit:

1. PF-10 has six abstract channels, but signed X6 has twelve primitive spatial neighbour directions;
2. the same rotation macro-edge has INNER and OUTER BRC lifts selected differently by the triadic-closure and nonzero-phase operation contexts.

V2 closes those two interfaces only. It does not duplicate the V1 state enumeration.

## 2. Signed half-port repair

Let `C={c0,...,c5}` be the PF-10 channel set. Under an admitted axis-channel frame `phi:C->A`, define

`P_hat := C x {+1,-1}`

and

`phi_hat(c,sigma)=sigma E_{phi(c)}`.

Then `phi_hat` is a bijection from the twelve signed half-ports to the twelve signed primitive X6 directions.

The polarity bit has spatial meaning: it selects which side of the Cell along one native axis family contains the adjacent Cell. It is not another channel and not another dimension.

For a primitive step

`x -> x + sigma e_i`,

with `c=phi^-1(E_i)`, the source uses egress side `(c,sigma)` and the target uses ingress side `(c,-sigma)`.

## 3. Channel-only PF-10 is a coarse observer, not exact signed adjacency

The channel-only map

`q:P_hat -> C`, `q(c,sigma)=c`

has fibers

`{(c,+),(c,-)}`.

Therefore any operation asking for the exact next signed X6 neighbour distinguishes states merged by `q`.

Consequently:

`PF10_CHANNEL_ONLY_PORT != EXACT_SIGNED_X6_HALFPORT`.

`SIGNED_SPATIAL_FUTURE -> RETAIN_PORT_POLARITY`.

The minimal repair for one signed port occurrence is exactly one polarity bit.

The original PF-10 counts remain correct coarse observers when polarity is outside the declared future language:

`I[c]=I_hat[c,+]+I_hat[c,-]`,

`O[c]=O_hat[c,+]+O_hat[c,-]`,

and similarly for passage totals.

This is an Operation-Safe Quotient statement, not a mutation of PF-10.

## 4. Signed lift of the triadic passage kernel

For one oriented active 3-cycle

`kappa=(c0 c1 c2)`,

define

`Q_kappa(c_r,sigma)=(c_{r+1},-sigma)`.

Then

`Q_kappa^3(c_r,sigma)=(c_r,-sigma)`,

`Q_kappa^6=1`.

Its unsigned PF-10 passage support is the partial 3-cycle

`M[c0,c1]=M[c1,c2]=M[c2,c0]=1`.

Thus the V1 directed passage support and the signed-X6 generator fit exactly:

`unsigned channel 3-cycle + polarity sheet -> signed C6 port dynamics`.

The unsigned matrix alone cannot reconstruct the polarity sheet.

## 5. Contextual branch theorem

Fix one triadic rotation macro-edge relative to pivot Cell `c`:

`a -> b=Q_S a`.

The signed-X6 shortest-path theorem gives exactly two two-step lifts:

`INNER: a -> c -> b`,

`OUTER: a -> c+a+b -> b`.

They have the same macro endpoints and frame action but different intermediate Cells.

### 5.1 Atomic triadic closure selects INNER

For three simultaneous force-token macro-edges on one canonical signed triad, the joint shortest population has `2^3=8` branch combinations.

P000 `TRIADIC_CLOSURE_E` requires one common atomic action node. Exhaustive exact checking for all `20` three-axis selections and all `8` sign sheets gives:

`exactly one joint shortest combination has a common midpoint Cell`,

namely

`INNER x INNER x INNER`,

with common midpoint `c`.

### 5.2 Nonzero phase refinement selects OUTER

For the existing local C6/C12 phase interface, the intermediate phase must be represented by a nonzero spatial Cell relative to the pivot. INNER passes through the pivot and has no nonzero radial phase; OUTER passes through `c+a+b != c` and supplies the existing outer C12 phase Cell.

Hence the nonzero-phase operation selects OUTER.

## 6. No context-free endpoint/frame branch selector

Suppose a deterministic selector depends only on the macro endpoint/frame data `(a,b,Q_S)`.

The same macro data occurs in both operation contexts above.

- atomic triadic closure requires INNER;
- nonzero phase refinement requires OUTER.

Therefore no such context-free selector can satisfy both.

Freeze the research theorem:

`BRANCH_SELECTION_IS_OPERATION_CONTEXT_TYPED`.

`TRIADIC_CLOSURE_CONTEXT -> INNER`.

`NONZERO_PHASE_CONTEXT -> OUTER`.

`ENDPOINT_FRAME_ONLY_BRANCH_SELECTOR = NO_GO`.

The correct upper state must retain an operation/event-context type at least until the branch-sensitive future is resolved.

This is not a contradiction between the two prior research lines. They ask different native operations of the same multipath fiber.

## 7. Internal-state consequence

The V1 intrinsic triadic fiber remains the correct finite interaction carrier. V2 adds one typing requirement:

`INTERNAL_STATE_FOR_MIXED_UPPER_OPERATIONS`

must not be reduced to

`spatial Cell + rotation frame`

alone.

At a branch-sensitive interface it also needs the declared event/operation context, or an equivalent future signature that determines whether closure or phase propagation is being executed.

The branch bit itself is not a universal permanent state variable: once the operation context is known, the two current contexts deterministically select opposite branches.

Thus the stronger conclusion is

`CONTEXT CAN REPLACE BRANCH_MEMORY WHEN A UNIQUE CONTEXTUAL SECTION IS PROVED`.

This is an exact example of operation-safe compression.

## 8. Scope and next target

Closed here:

- six abstract channels versus twelve signed spatial half-ports;
- one-bit polarity repair per signed port occurrence;
- signed lift of the PF-10 triadic passage kernel;
- exact contextual INNER/OUTER selection;
- endpoint/frame-only branch-law no-go.

Next upper problem:

combine the V1/V2 Cell fiber with the event-dependency time poset across multiple interacting pivot Cells, and classify when channel-frame transport around spatial/event loops has nontrivial holonomy.

No Foundation promotion is claimed.
