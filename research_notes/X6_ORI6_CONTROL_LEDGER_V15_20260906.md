# X6 rotation V15: Ori6 control ledger, chirality recurrence and trigger underdetermination

Status: `FREE_RESEARCH / EXACT CONTROL NORMAL FORM + NO-GO / NOT_FOUNDATION`
Date: `2026-09-06`
Researcher: `EM-FREE-PI-PRIME-20260904 / FREE_AXIOM_DISCOVERY`
Tasks: `RS-X6-NATIVE-ROTATION-DYNAMICS`, `RS-X6-NATIVE-TIME-DYNAMICS`, `RS-X6-UPPER-STRUCTURE-INTEGRATION`
Depends on:
- `X6_ORI6_TRIADIC_PHASE_REVERSAL_V13_20260906.md`;
- `X6_PHASE_CHIRALITY_D12_DYNAMICS_V14_20260906.md`;
- `X6_ORI6_EVENT_CHARGE_AND_OBSERVER_BOUND_V8_20260906.md`.
Checker: `experiments/x6_ori6_control_ledger_v15_20260906/check_ori6_control_ledger.py`.

## 1. The remaining question after V13/V14

V13 supplies an exact structurally compatible charge-one triadic phase-reversal event. V14 supplies the exact local 12-state phase-chirality dynamics once the event kind is declared.

What remains is not representation. It is **trigger law**:

> at a given local event opportunity, why should the process ADVANCE or PHASE_REVERSE?

The current P000/Foundation does not contain a scalar rate, energy threshold, environment variable or other law selecting between them.

This note isolates that missing input as one control bit and proves that current local symmetry/reversibility alone cannot remove it.

## 2. Binary event control

Let

`u_t in {0,1}`

encode the event kind at event time `t`:

- `u_t=0`: ordinary ADVANCE;
- `u_t=1`: V13 PHASE_REVERSAL.

Let local state be

`(r_t,epsilon_t) in Z/6 x {+1,-1}`.

Both event kinds advance to the currently forward shell neighbour, so the exact controlled recurrence is

`r_{t+1}=r_t+epsilon_t mod 6`,

`epsilon_{t+1}=(-1)^(u_t) epsilon_t`.

Thus the event kind changes **future continuation**, not the immediate phase increment.

## 3. Ori6 ledger equals accumulated control parity

Define

`chi_t = sum_{0<=s<t} u_s mod 2`.

Then induction gives

`epsilon_t = epsilon_0 (-1)^(chi_t)`.

V8 defines the global `Ori6` event charge as the parity of charge-one frame events. In the restricted local event language:

- ADVANCE has charge zero;
- PHASE_REVERSAL has charge one.

Therefore `chi_t` is exactly the restriction of the global Ori6 event ledger.

Consequently local sweep chirality relative to its initial value is not an independent conserved variable:

`epsilon_t / epsilon_0 = (-1)^(ORI6_LEDGER_t)`.

For Markov prediction without retaining the entire event word, the one-bit chirality state is precisely the repair coordinate carrying this accumulated charge information.

## 4. Exact phase integral

Substituting the chirality formula gives

`r_t = r_0 + epsilon_0 * sum_{0<=s<t} (-1)^(chi_s) mod 6`.

So local phase is the discrete integral of the charge-controlled chirality.

This distinguishes three types cleanly:

- `u_t`: event/control input;
- `chi_t` or equivalently `epsilon_t`: one-bit accumulated relational state;
- `r_t`: C6 phase state.

None is a seventh spatial coordinate.

## 5. Event word versus finite Markov state

For the restricted future language asking only exact future local phase under future controls, `(r_t,epsilon_t)` is sufficient by V14.

The past control word itself is not reconstructible from the one-bit ledger: many histories have the same parity. If a future operation asks how many reversals occurred or requests exact Path/BRC provenance, the event word/count must be retained separately.

Thus

`CONTROL_PARITY = SAFE FOR FINAL ORI6 / LOCAL CHIRALITY`,

but

`CONTROL_PARITY != FULL EVENT HISTORY`.

## 6. Symmetry does not choose the trigger

Consider deterministic autonomous selectors

`sigma(r,epsilon) in {ADVANCE, PHASE_REVERSAL}`.

Require two natural covariances of the bare local phase carrier.

### Phase-translation covariance

For every `k in Z/6`, shifting the phase origin

`T_k(r,epsilon)=(r+k,epsilon)`

must not change the event kind.

Hence `sigma` cannot depend on `r`.

### Chirality-relabeling covariance

The relabeling

`C(r,epsilon)=(-r,-epsilon)`

reverses the convention for phase orientation but does not change whether the declared event is ADVANCE or PHASE_REVERSAL. Direct calculation shows C commutes with both V14 event maps.

Hence covariance under C identifies the two chirality sheets for the trigger rule.

Together the two symmetries act transitively on the 12 states, so any deterministic symmetric trigger is constant.

There are exactly two such laws:

1. always ADVANCE;
2. always PHASE_REVERSAL.

Both define bijective/reversible maps on the 12-state carrier:

- always ADVANCE gives the V14 A operation with two C6 chirality sheets;
- always PHASE_REVERSAL gives the V14 B involution with six 2-cycles.

Therefore even after imposing local phase homogeneity, chirality-relabelling symmetry and reversible state evolution, current structure does **not** select one law over the other.

This is the exact trigger underdetermination no-go.

## 7. Minimal missing law channel

If both events are to remain admissible possibilities, one binary event-control datum is necessary and sufficient at each local decision point:

`u_t in C2`.

It may later be supplied by:

- another interacting Cell/internal state;
- a force/weight threshold;
- a channel/environment coupling;
- a larger dependency-event pattern;
- a stochastic or signed-amplitude law;
- a future Foundation definition.

This note does not choose among those mechanisms.

The important reduction is that no further local frame algebra is missing: the unresolved local trigger is now one typed binary law channel, not an unknown rotation group.

## 8. D12 normal form of event histories

Every finite local frame/event word in ADVANCE and PHASE_REVERSAL reduces uniquely to one of the 12 elements of D12.

At the state-action level it can be written in a normal form

`A^m B^chi`,

with `m in Z/6` and `chi in C2` under a fixed multiplication convention.

The quotient bit `chi` is exactly the final Ori6 charge, while `m` retains the phase-rotation component.

This group normal form is an endpoint/frame observer only. Different raw event words with the same D12 element remain different histories when event count or Path/BRC provenance is queried.

## 9. Current frontier

V13--V15 now close the **local conditional Ori6 dynamics**:

- charge-one triadic event frame: explicit;
- common-node Cell-path law: explicit;
- four-twist gauge covariance: explicit;
- phase/chirality Markov carrier: exact 12-state D12 torsor;
- accumulated charge/chirality relation: exact;
- remaining trigger input: one binary event-control channel;
- symmetry-only trigger selection: provably underdetermined.

The next high-leverage problem is therefore multi-Cell/event coupling:

> can the binary control `u_t` be derived from interactions between neighboring triadic internal fibers or from a larger dependency-time relation, rather than supplied externally?

No Foundation promotion, physical rate or external novelty claim is made.
