# R059D Stage F — Endogenous Response Closure / System-Spanning Local Propagation

Researcher-ID: `EM-R059D-4C7E21`
Taskbook source: `0aa8353d0c97c6d9944bb8ab04f809a00d323b37`
Frozen Stage-E parent: `26c1a5d6fe6526fbb5fca9e122c064344bb69ddc`

## Disposition

`ENDOGENOUS_LOCAL_SYSTEM_SPANNING_CAUSAL_CLOSURE_FOUND`

Stage F separates a fixed externally supplied response horizon from an endogenously emerging number of stationary update generations.  A fixed local rule can remain identical at every generation and nevertheless require a closure generation that grows with N.

## Frozen stationary construction F-T1

Use the pre-frozen `P2_TOKEN_WALKER_RECRUIT_PLUS` rule.  Its controller-visible signature is only the directly current ingress/event state and the exact local source-lineage sum `L_SELF`.

- `START, L_SELF=1 -> HOLD`
- `START, L_SELF=2 -> H`
- `START, L_SELF>=3 -> V`
- current ingress `H -> H`
- current ingress `H_INV -> H_INV`
- current ingress `V/V_INV -> HOLD`

The rule has no N, q, horizon, timer, round counter, target, branch provenance, programmed inverse, global participant count, global quiescence flag, or selected scheduler order.

Apply frozen intervention `F_I2_ALIGNED_SELF_PLUS1`: add one source-lineage CPBC count token to tag 0 at its aligned source contribution before stationary evolution.

Baseline stays fixed: each tag i is at `X_i` with lineage count 1.

Perturbed process:
1. At generation 0 the seed has `L_SELF=2`; its action differs from baseline HOLD and becomes H.
2. Its two source-lineage count tokens remain recoalesced and move by H at every generation.
3. Because `X_i=H^(q*i)X_0`, the moving seed lineage is at `X_i` exactly at generation `q*i`.
4. There it cooccupies the stationary tag i, so the exact local lineage sum is 3.  Tag i changes current count signature/action and is causally recruited.
5. At the next update tag i moves by V and then HOLDs; the seed lineage continues under H.

Therefore

`NEW_RESP_TAG_e = {i}` exactly at `e=q*i`, `i=0,...,N-1`,

and

`RESP_TAG_CLOSURE = {0,...,N-1}`.

Hence for every integer `q>=2` and `N>=2`:

`RESPONSE_PARTICIPANT_COUNT_CLOSURE : N = N:N`

and the least closure generation is

`CAUSAL_CLOSURE_GENERATION = E_*(N,q) = q*(N-1)`.

The formula extends to N=1 with E*=0, but N=1 is kept as a trivial one-tag case rather than nontrivial evidence.

This does not contradict Stage E.  Stage E fixed T independently of N; Stage F supplies no T to the rule.  The evaluator discovers that the exact closure generation itself grows with N.

## Independent F-I3 construction

The pre-frozen `P3_COOCCUPANCY_WALKER` reads only current ingress and the exact local number `S_SELF` of source lineages occupying the same packet.

Under the well-typed one-H-transition intervention `F_I3_H_STEP`, the seed continues H.  When it reaches a stationary tag, `S_SELF>=2`; that tag changes action from HOLD to H and joins the moving cohort.

For N>=2:

`E_* = q*(N-1)-1`.

After closure all N tags form one H-moving tagged cohort.  The perturbed boundary state is periodic with H-orbit period `q*N`; baseline remains fixed.  This is an exact eventual-periodicity certificate, not a finite quiet-window guess.

The H_INV seed orientation is also system-spanning.  Its exact earliest closure generation is:
- N=1: 0
- N=2: q-1
- N>=3: `q*(floor(N/2)+1)-1`.

## Support-only obstruction for count-token intervention

For `F_I2_ALIGNED_SELF_PLUS1`, adding one token changes multiplicity 1->2 but changes no tagged position, current event state, or support bit.

Therefore every stationary controller in the frozen P1 support-only class sees exactly the same input in baseline and perturbed runs.  By induction it chooses the same actions and preserves equal state/support forever.

Thus exact count magnitude is genuinely needed for the F-I2 construction:

`P1 SUPPORT-ONLY + F-I2 -> NO_CAUSAL_PROPAGATION`.

This is scoped to the frozen intervention/signature class; it is not a global impossibility theorem for all support-based dynamics.

## Scheduler robustness

Both positive constructions pass:

- `S_SYNC`
- `S_ALL_ORDERS_SNAPSHOT`

The source-local boundary states and closure generations are identical.  Only global Cartesian order multiplicity differs.

For F-T1, the all-orders diagnostic contributes a factor `2^(N-1)` across recruitment generations.  For the cooccupancy cohort construction the corresponding order factor is `product_(m=2..N) m!`.  These factors do not recruit tags and are excluded from `RESP_TAG`.

## Large-N first

The frozen registry includes `N=10^36`, its exact neighboring probes, lower enormous values, and q=2..19 plus larger prime/composite probes.

Large-N evaluation uses only the closed forms above.  No O(N), O(qN), or 2^N huge enumeration is used.

For example at N=10^36:
- q=3: F-T1 E* = `2999999999999999999999999999999999997`
- q=5: F-T1 E* = `4999999999999999999999999999999999995`
- q=31: F-T1 E* = `30999999999999999999999999999999999969`

## Scale-down and crossover

After the huge-N theorem, N was scaled down.

For every integer N>=2 and q>=2, all frozen positive stationary constructions remain `SYSTEM_SPANNING_CAUSAL_CLOSURE`.  N=1 is the trivial one-tag endpoint of the same formula.

Only the endogenous generation count changes with N.  There is no closure-class transition.

`INTRINSIC_N_MACRO_MICRO_CROSSOVER = NOT_IDENTIFIED`.

Stage-E `K(N)`, global aggregate and movable step-horizon controls remain negative/resource controls and are not used as Stage-F evidence.

Stage-D q=2,4 count-signature obstruction is not contradicted: that theorem concerned exact branch-recoalescence under a different frozen current-count grammar.  Stage F changes the scientific question and uses local self-count/cooccupancy signatures to study causal closure, not aligned endpoint return.

## Physical firewalls

`PHYSICAL_PROBABILITY_FROM_COUNTING = NOT_ESTABLISHED`

`PHYSICAL_RIGIDITY_INTERPRETATION = NOT_ESTABLISHED`

`PHYSICAL_ELASTICITY_INTERPRETATION = NOT_ESTABLISHED`

`QUANTUM_BRIDGE = NOT_ESTABLISHED`

No line, distance, length, angle, Euclidean geometry, force, energy, stress, strain, elastic modulus, probability, quantum amplitude, or continuum motion is used as a theorem premise.

## Deterministic checker

The checker validates the paired-process formulas on tiny theorem-regression cases only and separately checks huge-N closed-form arithmetic.

Current checker result:

`2186 / 2186 PASS`

Checks digest:

`08dc20ab1f81f0a6b6d98880d44b56846d9d415b0a517df0c0c9a0a9d7cf54ec`

## Stop

`STOP_FOR_DRIVER_REVIEW`
