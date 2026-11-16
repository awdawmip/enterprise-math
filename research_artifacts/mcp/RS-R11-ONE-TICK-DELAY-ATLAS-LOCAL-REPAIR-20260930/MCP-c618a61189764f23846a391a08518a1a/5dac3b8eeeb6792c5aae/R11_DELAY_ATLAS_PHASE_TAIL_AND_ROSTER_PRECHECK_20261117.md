# R11 one-tick delay atlas: exact roster and phase/tail invariants

Status: AUTHOR-SIDE CONDITIONAL PRECHECK / NOT SOURCE-PUBLISHED / NOT INDEPENDENTLY REVIEWED
Task: RS-R11-ONE-TICK-DELAY-ATLAS-LOCAL-REPAIR-20260930
Publication: TP2-D90E968EA0178B9BD0DE
Frozen scientific source: awdawmip/enterprise-math@88e814717bd60144e6a5add07fc4ab596d483b62
Inputs: research_notes/HEARTBEAT_ACTIVE_CYCLE_CCBF9335_20260930_R11.md and research_notes/HEARTBEAT_RELEASE_FEEDBACK_CCBF9335_20260930_R10.md; immutable taskbook.
Date: 2026-11-17 (Asia/Shanghai)

## Explicit labeled injection roster

Let phase a=0,...,5 correspond to the six states at t=1,...,6; let v range over the eight distinct closed-material nodes, represented below by their actual original node identities once the original state/code package is reloaded. Denote a pending slot by (port, type, remaining), with one positive unit moved to (port, type, remaining+1), leaving every other field fixed.

For a=0,2,4 (A phases), use slots:
 (E5,1,1), (E6,2,2).
For a=1,3,5 (B phases), use slots:
 (E6,2,1), (E4,0,1), (E5,1,2), (E6,2,3).

The formal labeled family has 3*8*2+3*8*4=144 distinct (a,v,s) inputs, preserving total positive mass 48. This is an exact *candidate* count. Label generation alone does not establish validator legality.

Legality subcounts to test explicitly against the frozen *original* validator:
- If it imposes a single remaining<=3 bound, all 24 B-phase (E6,2,3)->(E6,2,4) edits exceed that bound, leaving at most 120 legal candidates.
- If it imposes per-port remaining<=emission-delay, with delays δ(E4)=1, δ(E5)=2, δ(E6)=3, three of the four B slots exceed their respective bounds after editing. Then 3*8*3=72 candidate labels violate this stricter rule, leaving at most 72.
- Either is a conditional count, not evidence that such a bound actually exists. If the original state schema admits arbitrary positive pending times, all 144 can be legal. Compare original code and serialized state before selecting any outcome.

## Proposition 1: background-phase restriction

Assume the 5824 unmixed background nodes are dynamically independent of the closed eight-node material loop under the frozen F, and the background field has primitive period 3; the original full prepared field C has period 6. If at true time n the perturbed *complete* state Y_n equals C_{n+s} for some integer phase offset s, then s=0 or 3 modulo 6.

Proof: the background coordinate projection of Y_n equals that of C_n, since the injection is confined to the closed material loop and background evolution is unchanged. Equality to C_{n+s} therefore implies B_n=B_{n+s}. Primitive background period 3 forces 3|s, hence modulo 6 the two classes 0,3. This conclusion concerns equality of complete states, not hash or only material-node similarity.

## Proposition 2: cumulative-observation tail after exact recovery

Let F be deterministic and autonomous on complete states; let C_i be any orbit with C_{i+L}=C_i. For an additive observable J_i=φ(C_i,F(C_i)) determined by the frozen transition (may be a vector of node/port/type release, commitment and delivery counts), compare a perturbation Y_i with C_i at the *same true clock*. Suppose that Y_n=C_{n+s} and therefore Y_{n+j}=C_{n+s+j} for all j>=0. Define the cumulative difference D(n+k)=sum_{i<n+k}[φ(Y_i,F(Y_i))-φ(C_i,F(C_i))] from a common start.

Then
 D(n+k)-D(n)=sum_{j=0}^{k-1}[φ(C_{n+s+j},C_{n+s+j+1})-φ(C_{n+j},C_{n+j+1})].
For k=L the sum is zero because the two index sets are the same complete orbit, permuted. Consequently D(n+k+L)=D(n+k): after exact entry into a phase-shifted original cycle, the *incremental* cumulative-observation residual is L-periodic and has zero long-run linear drift. The earlier absolute offset D(n) may remain nonzero. If s=0 modulo L, D is constant from n onward. The result holds separately for each conserved or measured port/type tally when it depends on the frozen full state/transition; it need not hold for an observable with explicit absolute-time dependence or off-model external input.

For the R11 six-cycle the tail period divides 6. This is a conditional finite-cycle lemma, not a claim that a specific injection has recovered.

## Proposition 3: exact difference-cone recomputation

Suppose the complete local output at node v on tick t+1 is a deterministic function of the previous fields in a specified finite dependency neighborhood N^-(v), including pending deliveries, port labels, gate and feedback. Let D_t be the set of nodes at which the perturbed and reference *full fields* differ. If N^-(v) intersects D_t trivially, their next fields at v are equal. Hence D_{t+1} is contained in D_t union the one-step causal Out(D_t), with Out defined by *actual* source dependencies, including pending delivery. To reproduce Y_{t+1}, recompute the exact nonlinear F for all nodes in this closure and reuse reference bytes elsewhere, compare exact full fields and all transition observers. Induction gives identical histories at every verified tick. Positive delay forbids same-tick infinite transport cascades. A small |D_t| alone does not bound dependency indexing, certificate cost, full-state comparison or output length.

## Open input and validation points

The original full R11 source bundle and its exact validator/state schema remain to be fetched and hash-checked; published summary cites test_cycles.py sha256 49d1c6ed0be596b82fa8bfa963df934fc1702cf91feda1680fb7f8d8e961c6d7. The exact eight native node identities, all 144 materialized original states, and all per-case tick/cost tests are not asserted here. The task's mandated classification is RECOVERED/NEW_CYCLE/UNKNOWN_BUDGET with separate NOT_RUN/INPUT_UNAVAILABLE; no case has been executed in this precheck.