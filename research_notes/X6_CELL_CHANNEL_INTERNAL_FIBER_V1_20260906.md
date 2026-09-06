# X6 Cell/channel internal fiber V1: signed half-ports, triadic passage kernels, and operation-safe internal state

Status: `FREE_RESEARCH / EXACT DERIVATION + FINITE CHECK / NOT_FOUNDATION`
Date: `2026-09-06`
Researcher: `EM-FREE-PI-PRIME-20260904 / FREE_AXIOM_DISCOVERY`
Task: `RS-X6-CELL-CHANNEL-INTERNAL-STATE`
Consumes:
- `PACKET_PATH_FOUNDATION.md` PF-10 six-channel relational state;
- `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md`;
- `research_notes/X6_TRIADIC_ROTATION_GENERATORS_V1_20260906.md`;
- `research_notes/X6_TRIADIC_ATOMIC_SCATTER_V1_20260906.md`;
- `research_notes/X6_NATIVE_EVENT_TIME_V1_20260906.md`.

## 1. Question and type boundary

PF-10 admits an ideal six-channel relation state `I_x[0..5]`, `O_x[0..5]`, `M_x[a,b]` at a packet. X6 independently has six native spatial axis families and twelve signed primitive spatial directions `+/-E_i`.

The equality of the two cardinalities `6` does not identify the semantic types.

Freeze for this research:

`PF10_CHANNEL != NATIVE_SPATIAL_AXIS BY CARDINALITY ALONE`.

`INTERNAL_CHANNEL_STATE != ADDITIONAL_SPATIAL_DIMENSION`.

## 2. Axis-channel frame is a 720-element torsor

Let `C={0,...,5}` be the abstract PF-10 channel labels and `A={E_1,...,E_6}` the native unsigned spatial axis families.

An axis-channel frame is a bijection

`phi:C -> A`.

The frame set is

`Fr_CA = Bij(C,A)`

with cardinality

`|Fr_CA|=6!=720`.

Independent relabeling of axes and channels acts by

`(g,h): phi -> g o phi o h^-1`.

Thus `Fr_CA` is an `S6`-`S6` bitorsor. With no extra relation datum there is no distinguished physical frame merely from the fact that both sets have six labels. A chosen frame is interface/gauge data unless another admitted law makes it observable.

This is an application of the existing finite-symmetry/canonical-choice interface `T7_FINITE_SYMMETRY_EQUIVARIANCE`; no new symmetry tool family is introduced.

## 3. Six channels are insufficient for twelve signed spatial half-ports

For exact spatial adjacency define the signed half-port set

`P_hat = C x {+1,-1}`.

Given `phi`, lift it to

`phi_hat(c,sigma)=sigma*e_{phi(c)}`,

which is a bijection from the twelve signed half-ports to the twelve signed primitive X6 directions.

A primitive transition

`x -> x + sigma e_i`

uses at the source the egress half-port `(phi^-1(E_i),sigma)` and at the target the ingress half-port `(phi^-1(E_i),-sigma)` when half-port polarity denotes the side of the Cell on which the adjacent Cell lies.

The PF-10 channel-only observer forgets polarity:

`(c,+) -> c`, `(c,-) -> c`.

Therefore it merges twelve signed ports into six channels. Any future operation that asks which signed X6 neighbour is next distinguishes the two members of such a fiber. Hence the channel-only quotient is not operation-safe for exact signed-spatial dynamics.

Minimal repair per port occurrence is one spatial-polarity bit. This polarity is not a seventh channel and not a new spatial axis.

Coarse PF-10 counts remain valid observers, e.g.

`I[c]=I_hat[c,+]+I_hat[c,-]`,

and similarly for `O` and `M`, when the declared future operation language is insensitive to the erased polarity.

## 4. Canonical triadic passage kernel on signed half-ports

Choose three distinct channel labels with one cyclic orientation

`kappa=(c0 c1 c2)`.

There are

`2*binom(6,3)=40`

such oriented channel 3-cycles.

Define the signed half-port triadic generator

`Q_kappa(c_r,sigma)=(c_{r+1},-sigma)`

with indices modulo three and all non-active channels fixed when the map is extended to the full frame.

Then

`Q_kappa^3(c_r,sigma)=(c_r,-sigma)`,

`Q_kappa^6=1`.

This is the channel/port realization of the current signed-X6 triadic C6 generator.

The PF-10 coarse passage matrix for one equal-quantum atomic scatter is the partial permutation matrix

`M_kappa[c_r,c_{r+1}]=1`

on the active channels and zero elsewhere. It records the oriented 3-cycle but not the signed polarity sheet.

## 5. Exact finite internal-state hierarchy

A full token/occurrence-anchored signed triad frame is

`F=((c0,s0),(c1,s1),(c2,s2))`

with three distinct channels, ordered occurrence positions, and `s_r in {+1,-1}`.

Number of frames:

`6*5*4*2^3=960`.

Define the full update

`R(F)=((c1,-s0),(c2,-s1),(c0,-s2))`.

Then

`R^3(F)=-F` on the same ordered channel anchor and

`R^6(F)=F`.

Every full frame has exact orbit length six, giving

`960/6=160`

C6 frame orbits.

For the local atomic interaction clock introduce event parity

`epsilon in {SHELL,CLOSURE}`

and update

`(F,SHELL) -> (F,CLOSURE) -> (R(F),SHELL)`.

This produces

`960*2=1920`

local event states, partitioned into exactly

`1920/12=160`

C12 interaction cycles.

These are relation/internal states centered on a chosen interaction Cell; they do not create 1920 spatial Cells or any extra spatial dimension.

## 6. Quotient hierarchy and exact information loss

The 960 full triad frames admit the following natural observer hierarchy.

### 6.1 Full occurrence/phase frame: 960

Keeps:
- active signed channels;
- chirality/oriented 3-cycle;
- a C3 occurrence/phase anchor.

### 6.2 Triadic predictive kernel: 320

Forget cyclic anchor but retain the oriented 3-cycle and the sign attached to each active channel.

Count:

`40 oriented 3-cycles * 8 polarity sheets = 320`.

This is enough to determine the next unlabeled signed triad support under the declared triadic passage law.

### 6.3 Static signed triad support: 160

Forget the 3-cycle orientation/chirality and retain only the unordered signed active ports.

Count:

`binom(6,3)*2^3=160`.

This is not globally Markov for the triadic update: among these 160 supports, 120 mixed-polarity supports admit the two chiralities with different next signed supports. The 40 sign-coherent supports happen to have the same one-step signed-support image for both chiralities, but their passage kernels are still distinct.

### 6.4 Unsigned active triad support: 20

Forget polarity and chirality, leaving only the three active channel families.

This is a static support observer only.

The existing BRC and operation-safe quotient discipline applies: each downward map is safe only for a declared future-operation horizon.

## 7. Full local predictive signature and a 1920-state lower bound

Consider a future language that asks all of:

1. exact signed next-shell neighbours;
2. exact oriented passage kernel `M_kappa`;
3. labeled/cyclic occurrence phase;
4. whether the process is at SHELL or CLOSURE.

A signature supporting these four observables must retain:

- 40 oriented kernels;
- 8 polarity sheets;
- 3 cyclic anchors;
- 2 event parities.

Hence it must distinguish at least

`40*8*3*2=1920`

local relation states.

Each factor has a concrete future witness:

- drop kernel orientation -> a future outgoing channel differs;
- drop polarity -> a future signed X6 neighbour differs;
- drop C3 anchor -> labeled occurrence/phase provenance differs;
- drop event parity -> shell-neighbour configuration is confused with a common-pivot closure event.

Thus 1920 is a scope-typed minimality result for this exact future language, not a universal lower bound for every observer.

## 8. Contextual INNER/OUTER theorem: there is no universal endpoint-only branch law

For one triadic macro edge `a -> b=Q_S a`, current signed-X6 BRC gives exactly two shortest native Cell lifts:

- `INNER: a -> c -> b`, where `c` is the interaction pivot;
- `OUTER: a -> c+a+b -> b`, whose intermediate Cell is nonzero relative to `c`.

Two existing operation contexts select opposite branches:

### Atomic triadic closure context

For three simultaneous force tokens on one selected triad, P000 requires one common atomic action node. Among the `2^3=8` joint shortest branch combinations, only

`INNER x INNER x INNER`

has one common midpoint Cell for all three tokens.

### Nonzero phase-refinement context

For the local rotation/Viète phase interface, requiring a defined nonzero intermediate phase excludes the pivot branch and uniquely selects OUTER on each macro edge.

Therefore no branch selector depending only on the macro endpoints/frame can satisfy both operation contexts.

Freeze the exact conclusion:

`BRANCH_SELECTION_IS_OPERATION_CONTEXT_TYPED`.

`TRIADIC_CLOSURE_CONTEXT -> INNER`.

`NONZERO_PHASE_CONTEXT -> OUTER`.

`ENDPOINT_OR_FRAME_ONLY_BRANCH_SELECTOR = INSUFFICIENT`.

This is not a contradiction. INNER and OUTER are different native realizations used by different admissible operations. The event/context type is genuine internal/relational information.

## 9. Relation to PF-10 port collapse

The current positive-rational recurrent-port tools remain valid for their declared nonnegative recurrent contexts, but they do not by themselves encode signed spatial polarity or the phase/chirality information above.

For triadic signed dynamics, the minimal exact port data before safe collapse is therefore richer than a bare `6x6 M`:

`(axis-channel frame if needed, oriented M_kappa, active polarity sheet, occurrence anchor if provenance is queried, event/context type)`.

If a downstream observer asks only channel-level transfer and has no hidden-state access, existing port-collapse machinery may be applied after proving fiber constancy for the omitted factors.

## 10. Current closure and next target

Closed in this stage:

- exact relation between 6 PF-10 channels and 12 signed X6 half-ports;
- axis-channel frame as a 720-element bitorsor rather than a canonical identity;
- canonical signed triadic passage kernel;
- 960 full triad frames, 160 C6 orbits;
- 1920 event states, 160 C12 interaction cycles;
- exact quotient hierarchy `960 -> 320 -> 160 -> 20` with scope boundaries;
- contextual INNER/OUTER branch-selection theorem.

Still open above this stage:

1. decide which axis-channel frame data is physical versus gauge in specific applications;
2. attach general PF-10 multiplicities/weights beyond equal-unit deterministic triads;
3. combine multiple interacting Cells and classify frame/port holonomy;
4. integrate the event/context state with the native dependency-time partial order;
5. determine the coarsest operation-safe internal state for each target application.

No Foundation promotion is claimed.
