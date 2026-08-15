# R059D Stage G — System-Spanning Causal Closure + Exact Aligned Recoalescence

Researcher-ID: `EM-R059D-4C7E21`  
Taskbook source: `383eeb9423e11b00a96f79c88f3bb86ec93df277`  
Frozen Stage-F parent: `a03e9181ddcb17a0971ac7bec8e534693cbd817e`

## Disposition

`ENDOGENOUS_SYSTEM_SPANNING_EXACT_ALIGNED_RECOALESCENCE_FOUND`

The strongest Stage-G conjunction is established within the frozen relational/count grammar using a real tagged adjacency perturbation.

## Mandatory Stage-F replay

The frozen Stage-F walkers were replayed verbatim before evaluating new rules.

- `P2_TOKEN_WALKER_RECRUIT_PLUS/MINUS`: system-spanning causal closure survives, but one persistent H/H_INV messenger remains in V-class 0 while recruited tags are V-settled in another common V-class. For `N>1` no post-span aligned state occurs.
- `P3_COOCCUPANCY_WALKER`: after system-spanning recruitment all tags form one co-moving packet cohort. For `q>=2,N>1`, the q-period aligned evaluator requires pairwise distinct H-orbit positions, so no aligned return occurs.

Freeze: `SYSTEM_SPANNING_WITHOUT_ALIGNED_RECOALESCENCE_CONTROL`.

## New stationary relay rule

`G1_RELAY_H_RECURRENT_ALIGN` uses only `CURRENT_INGRESS + S_SELF`.

Rules:

- `START, S=1 -> HOLD`
- `START, S>=2 -> H`
- `H, S=1 -> H`
- `H, S>=2 -> V`
- `V -> V_INV`
- `V_INV, S=1 -> HOLD`
- `V_INV, S>=2 -> H`

The mirror rule exchanges H with H_INV.

No rule reads N, q, time, horizon, timer, aligned flag, target, participant count, quiescence, provenance, programmed inverse, global oracle, or scheduler order.

## Exact theorem

Apply `G_I3_H_STEP`: before release tag 0 performs exactly one declared H transition.

Let `X_i=H^(q i)X_0`, H-orbit order `qN`.

The unique active tag advances by H while alone. At `e=q i-1`, `i>=1`, it first cooccupies `X_i` with the resident tag. Snapshot `S_SELF=2` makes the incoming active execute V and the resident execute H. One generation later the old active executes V_INV back to `X_i` and becomes a settled V_INV-state tag, while the new active continues.

Hence:

`NEW_RESP_TAG_e={i} iff e=q i-1` for `i=1,...,N-1`, with seed tag 0 already causal at `e=0`.

Therefore:

`E_SPAN=q(N-1)-1`.

After the final recruitment, the last active tag traverses the remaining q H-actions to the unique hole `X_0`. At

`E_ALIGN=qN-1`

the tagged positions are

`tag i -> X_(i+1 mod N)=H^q X_i`.

Thus the first post-span aligned state is an `ALIGNED_OTHER_DECLARED_CLASS`, a common H^q relabeling.

The inequality is exact:

`E_SPAN=q(N-1)-1 < qN-1=E_ALIGN`, with gap q.

## Post-return classification

The first aligned state is not settled: one tag remains active. However it is not merely transient.

For every integer `m>=1`:

`e_m=m q N - 1`

is exactly aligned, with

`tag i -> H^(m q) X_i`.

Hence the post-return class is:

`G-R1 / AUTONOMOUS_ALIGNED_RECURRENCE_RETURN`.

Aligned macrostates recur every `qN` generations. After N aligned returns the positional macrostate returns to the initial common H^(qN)=identity class; the complete event-state pattern repeats after `q N^2` generations.

The H_INV mirror has the same E_SPAN/E_ALIGN laws with common shifts H^(-m q).

## Scheduler robustness

`S_SYNC` and `S_ALL_ORDERS_SNAPSHOT` have identical tagged support, participant closure, E_SPAN, E_ALIGN, endpoint class, and G-R1 recurrence.

The all-orders scheduler adds only diagnostic execution-order multiplicity. Before first aligned return, each of the N-1 collisions and its following V->V_INV settlement boundary has two simultaneous transitions, giving factor `4^(N-1)`. This is excluded from causal recruitment.

## Large-N and scale-down

The theorem is symbolic for all integers `N>=2,q>=2`. Huge-N registry including N≈10^36 is evaluated only through exact formulas.

Tiny enumeration is theorem regression only.

Scale-down preserves the same joint class for every `N>=2,q>=2`. `N=1` is a trivial single-tag aligned degeneracy and is not an intrinsic macro/micro crossover.

`INTRINSIC_N_MACRO_MICRO_CROSSOVER = NOT_IDENTIFIED`.

## Interpretation firewall

Freeze only:

`RIGIDITY_LIKE_INTEGER_STRUCTURE_CANDIDATE = ESTABLISHED_WITHIN_FROZEN_GRAMMAR`.

Continue:

`PHYSICAL_RIGIDITY_INTERPRETATION = NOT_ESTABLISHED`  
`PHYSICAL_ELASTICITY_INTERPRETATION = NOT_ESTABLISHED`  
`PHYSICAL_PROBABILITY_FROM_COUNTING = NOT_ESTABLISHED`  
`QUANTUM_BRIDGE = NOT_ESTABLISHED`

## Checker

The deterministic checker validates exact tiny theorem regressions, full-state recurrence, huge-N formula arithmetic, real-I3 gate, resource leakage gates, and artifact semantics.

Final repository immutability is verified separately by GitHub compare before checkpoint freeze.
