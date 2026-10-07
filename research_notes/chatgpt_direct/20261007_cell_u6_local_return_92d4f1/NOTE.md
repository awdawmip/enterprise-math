# U6 — local reactivation does not confine the retained response

Event: EM-20261007-CELL-U6-LOCAL-RETURN-92D4F1
Status: CONDITIONAL_U5_CIRCUIT_THEOREMS / ACTUAL_TYPED_BRC / NOT_NATIVE_FORCE / NOT_ADMITTED
Global read snapshot: awdawmip/chatgpt-global-knowledge@4ae8956b65ced23a31929c866a9d78495f7526b2.
Science/control intake: awdawmip/enterprise-math@1df473b7bfcf71c8de3510ec056bfb33964be638.
Researcher: EM-DIRECT-DAA50C. Activity: RA-2148DEBF96D56FDD3C426AE4.
Own public session: MCP-8f61ab5ee19f40f799060e167ae5e7c6.
Logical conversation: chatgpt-heartbeat-cell-attraction-20261006-8b74f0, not platform-attested.
Registration observed at 00cba08eaccae50fe4b7511abf880f39935cbdba; activity blob 1e85413401ade01b90f7d80542ad519a7cf48af1.

## 0. Question, inputs and interpretation

U5 introduced a finite-budget active/dormant response circuit and proved a nonzero GLOBAL active limit. This unit asks whether that circuit actually sustains response near the materials. No new force, attraction, wall, source injection, routing bias, or material motion rule is added to make the answer favorable.

Reuse U5 at e077563ca390c1f964ad4d4e856c098c00f9f0b5, directory research_notes/chatgpt_direct/20261007_cell_u5_lifecycle_3e72b9. Its U4/U3/U2 dependencies and the separate native-interface audit retain their original scope. The newer residual-boundary-bridge journal was checked; its source/Cell/incoming-port closure is consistent with, but not a substitute for, this local-return question. It is not an independently reviewed native action law.

The state keeps birth-source, absolute X6 Cell and signed incoming port, separately for active F and dormant D. All six axes and twelve signed nearest-neighbor steps remain. The source's permissive packet incidence remains a candidate. No primitive stable force event or mechanical balance is asserted. Response total, normalized path weight, trial occupancy weight, physical mass/energy and physical time are distinct. Infinite statements concern exact mathematical continuations, not an empirically established universe.

## 1. Eliminating waiting without changing spatial jumps

Write L_X=rho P_X, 0<rho<1. The total readout of P_X has column sum one. At an empty Cell its twelve outgoing weights are 1/12. At a material Cell:

K(q,p)=1/3 for q=p; K(-p,p)=0; K(q,p)=1/15 on the ten other-axis ports.

U5 uses, for 0<epsilon<1,

F_(n+1)=rho P_X F_n+epsilon D_n,
D_(n+1)=(1-rho)F_n+(1-epsilon)D_n.

For FIXED X, look only at actual spatial jumps of a normalized positive response ray. An active ray either jumps with total weight rho, or becomes dormant at the SAME key. A dormant ray eventually awakens at that same key with total weight one. The complete waiting excursion has weight

(1-rho) * epsilon * sum_(k>=0)(1-epsilon)^k = 1-rho.

Consequently the weight of the next outgoing spatial edge q is

sum_(j>=0)(1-rho)^j * rho P_X(q,p) = P_X(q,p).

This is a positive path-series identity, not cancellation of signed response. The embedded spatial chain is EXACTLY P_X for every positive epsilon. Changing the release fraction changes delays; it does not change hitting/return weights at fixed layout. This quotient preserves spatial-path total weights, NOT timing, raw path counts, CWM dominant values, or arbitrary joint packet observations. Original waiting-word provenance remains in the augmented recurrence.

At each spatial visit the expected number of active-state observations before the next jump is 1/rho; expected dormant observations are (1-rho)/(rho*epsilon). A ray initially dormant has the additional initial dormant wait, but the same subsequent active exposure. Thus coordinatewise, as nonnegative extended sums,

SUM_(n>=0) F_n = (1/rho) SUM_(k>=0) P_X^k (F_0+D_0).             (1)

This is justified by summing the waiting words at each spatial visit; it does not assume a finite all-depth CWM count. For epsilon=0 the argument fails: permanently stored response is not reactivated. No interchange of epsilon->0 with infinite observation time is claimed.

For checking the complete waiting-word statement, its first-jump duration generating function is

T(t)=rho*t*(1-(1-epsilon)*t) /
     (1-(1-epsilon)*t-(1-rho)*epsilon*t*t).

It is represented by positive waiting words; the displayed rational denominator is not a signed physical carrier. T(1)=1. The implementation actually checks finite waiting words and spatial-port distributions, not a classical matrix-exponential solver.

## 2. A rational bulk escape comparison

For an integer displacement v define the AUXILIARY observer

f(v)=1/(1+S), where S=sum_(i=1..6) v_i^2.

This is only a proof bound on the declared graph. It is not a square-number shell, a material potential, an energy law, or a prescription for final position. No arithmetic integer N is classified by proximity to a square.

For the twelve equally weighted bulk edges,

(1/12) sum_(i,s) f(v+s e_i)
 <= (1/6) [5/(S+2)+(S+2)/(S^2+4)] < 1/(S+1).                (2)

Proof: put b=S+2 and t_i=v_i^2. The pair of signs contributes 2b/(b^2-4t_i). The function g(t)=1/(b^2-4t) is convex on [0,S]. For S>0 its secant bound gives sum_i g(t_i)<=5g(0)+g(S), because sum t_i=S. S=0 is immediate. Subtracting the upper bound in (2) from 1/(S+1) gives exactly

[(S-1)^2+11]/[3(S+1)(S+2)(S^2+4)] > 0.

All denominators are positive. This is an all-coordinate proof, not an inference from finite tests.

For a finite set B of Cells, Psi_B(z)=sum_(b in B) f(z-b). Outside B, bulk propagation cannot increase its positive weighted average; dormant waits leave its value unchanged. At any hit of B, Psi_B>=1. Stopping the positive branch tree at the first hit and inducting to any finite depth yields

weight(ever hit B | z outside B) <= min(1,Psi_B(z)).           (3)

Take increasing finite depths for the all-future statement. Only before the first hit is the exterior bulk rule used. We are not applying the bulk bound to a material's scattering column.

Random-walk transience, Green sums and first-return arguments are established methods, not claimed novel. Primary reference checked: Lawler and Limic, Random Walk: A Modern Introduction, author-hosted PDF, section4.1, Theorem4.1.1, printed p75 / PDF page74 (zero-based), and section4.2. URL: https://www.math.uchicago.edu/~lawler/srwbook.pdf . The present explicit rational certificate and its U5 interface consequences are proved here; the reference is not a new non-BRC numerical calculation.

## 3. Explicit escape certificates for the original specimens

For fixed X, let R_X be the positive first-return kernel on the finitely many material Cell/incoming-port states, AFTER at least one spatial jump. First-hit branches and still-outside branches are separately retained; hitting is not annihilation. A uniform escape lower bound delta gives column sums R_X<=1-delta and

SUM_(k>=0) ||R_X^k v||_1 <= ||v||_1/delta.                    (4)

The BRC one-state comparison with loop weight1-delta evaluates this bound exactly. It is a bound in number of material visits, not an exponential temporal-decay assertion.

Adjacent pair X={c,c+e1}: select a first jump on any of the ten transverse ports. Their total weight is at least2/3 for every incoming port. At its endpoint Psi_X=1/2+1/3=5/6. Hence delta>=1/9.

Gap pair X={c,c+2e1}: the same transverse selection has endpoint Psi_X=1/2+1/6=2/3. Hence delta>=2/9.

Original square221 X={c,c+e1,c+e1+e2,c+e2}: select one of the eight ports transverse to axes1,2; total weight at least8/15. Take a second jump in the same direction at its EMPTY neighbor, weight1/12. These paths cannot have returned to X. Their endpoints have

Psi_X=1/5+2/6+1/7=71/105.

Thus

delta >= (8/15)*(1/12)*(1-71/105)=68/4725.                   (5)

These path families are disjoint in their first edge. The bounds apply to every material and every incoming port. Escape does not destroy response; it means that a positive part of its normalized path weight no longer revisits these materials. Bounds are not exact escape probabilities.

With rho=1/4, initial total M=|X| and no initial dormant budget, (1),(4) give:

preparation       delta       total active exposure at material Cells, all n>=0
adjacent pair     1/9         <=72
gap pair          2/9         <=36
square221         68/4725     <=18900/17

The bounds deliberately include self-origin response and stage0. They are conservative, dimensionless RESPONSE-by-index sums, not physical energy or elapsed time. Every cross-source-only exposure is smaller. No return matrix numerical inverse is assumed.

Since these sums are finite, local active response tends to zero. Summing the dormant recurrence at those Cells gives epsilon*SUM D=(1-rho)*SUM F+D_0, so local dormant exposure is finite and dormant response also tends to zero. This holds for every 0<rho,epsilon<1, not just the test parameters. The GLOBAL active total may simultaneously tend to epsilon*M/(1-rho+epsilon), including U5's M/7.

## 4. Bounded moving layouts do not evade the escape mechanism

There is a stronger, though much looser, uniform statement. Fix ANY finite region B containing every material Cell throughout a schedule X_n subset B. The occupied set may change arbitrarily with n; a fixed embedded spatial kernel is no longer assumed.

Take integer R with B subset[-R,R]^6, put m=2R+|B|+1, and k=2m+1. From any active state in B choose an alternating sequence of +e1,+e2, length2m, choosing its first direction not to equal the forbidden opposite of the incoming port. Every later direction uses a different axis from the preceding jump. Every such edge has actual augmented weight at least rho/15 whether its current Cell is empty or material. The endpoint is z+m(e1+e2), and

Psi_B(endpoint) <= |B|/[1+2(m-2R)^2] < 1/2.

For an initially dormant state first release, weight epsilon. Therefore, uniformly over starting ports and ALL future schedules confined to B, there is weight at least

eta_B = (epsilon/2)*(rho/15)^(2m) > 0                         (6)

of making no visit to B after at most k further stages. Holds outside B do not affect (3). The alternate path is a proof event, not a forced material move or a added transition law.

Start an attempt at the first visit to B; start the next at the first visit at least k stages later. Each attempt has conditional probability at least eta_B of there being no next attempt. Its first k stages account for at most k local observations, with no local observations in the gap before the next attempt. Hence

SUM_n (||F_n|B||_1+||D_n|B||_1) <= C_B*M,
C_B=k/eta_B.                                                 (7)

This bound is uniform in the fixed schedule, including schedules subsequently realized by the existing occupancy selector. The constant is very loose, not a useful claimed physical timescale. Spatial branch probabilities here only represent normalized positive response.

Consequences:
(a) There is no nonzero finite-total positive stationary augmented response for a fixed finite material set on unbounded X6. A positive stationary mass at any Cell contradicts (7) in a finite B containing that Cell and the materials.
(b) If repeated U5 current-active queries use fixed wait kappa, sustained infinitely many moves WHILE REMAINING IN A FIXED FINITE REGION have trial measure zero. Until first exit from B, the conditional expected moved-actor count is bounded by local active exposure/kappa. Extend each pre-exit layout by an arbitrary in-B schedule to apply the uniform bound (7). Expected moves before exit are finite, ruling out positive-weight never-exit/infinite-motion histories. Taking the countable union of boxes rules out globally bounded infinite-motion histories of positive trial measure. This does not rule out an unbounded translating cluster, unbounded excursions, exceptional zero-measure histories or a different native law.
(c) No mechanical stability, physical dissipation or native force impossibility follows. The ruled-out mechanism is this exact finite-budget circuit with bulk spreading, positive constant release, finite material support and the inherited fresh/current-active query eligibility.

## 5. A corrected all-future approximation scope with storage

U5 correctly rejected comparing only F after D can reactivate. Let two states have common positions, but initial augmented total-readout contrast

delta=||F-G||_1+||D-E||_1.

For the existing position-query processes STOPPED upon first exit from a declared finite B, couple them until their first positional disagreement. While positions agree, the positive augmented operator sends absolute contrasts into a dominating positive response of mass delta. By (7) its summed local exposure is at most C_B*delta, even along the adaptive common schedule. The old wait/request normalization and shared conflict kernel have one-step TV at most the local active contrast/kappa. Summing first-disagreement probabilities gives

TV(stopped position-trajectory laws) <= min(1,C_B*delta/kappa). (8)

The stopped process is an observer of the existing law, not a reflecting boundary inserted into its dynamics. This bound repairs the missing-D error only in the stated bounded observation scope. It is often numerically weak. It does not give an unrestricted bound for all unbounded co-moving trajectories, direct hidden-state observation, path counts, native force measurements or unrecorded request rearming. No claim to new general coupling theory is made.

## 6. Execution and evidence

check_u6.py verifies the inherited lifecycle.py blob389bd51a2a71a62a4c533ef781920bef00783bc3 and then uses the unchanged U4/U3/U2/BRC import chain. Other pins: continue_field c2f0749382ad4a6997b3a951a60d20713200fb20; occupancy3d7860df3ec93507cf7217bcea47867d809692fb; packet_router7465f5aa16cbb8fba61ba4be80f8a6884b879c53; BRC3f205696709e847909958a153f8fe10d3f6b70f0. No existing scientific function/class AST is altered. Only the inherited unused-relative-import adapter is reused.

The final run passed17863 checks. Actual BRC calls: edge173201, propagate1539516, recoalesce3048978, one_state_recurrent42. These counts describe execution, not independent confirmations. Scope:210 nonnegative-coordinate representatives plus the all-coordinate symbolic proof; every input port/material for the three explicit escape certificates; first-return prefixes through4 spatial jumps for three representative ports per layout;36 waiting-clock inputs through32 stages; full U5 fields through6 stages at fixed gap-pair and square layouts; finite path checks for the uniform-region comparison. The uniform all-schedule and infinite-time results are proved, not inferred from enumerating those samples.

Full positive finite CWM field traces, waiting records and escape path records are serialized in evidence/full_trace.json.gz. The source script regenerates them; no claim that each raw microscopic word is individually listed. CWM key coalescence is used only for the declared unary total-response/clock scope with the pinned transition grammar retained. Comparison observers are not signed physical mass.

The source repository receives this proof, executable checker and exact checkpoint. The conversation package also contains pinned dependencies and the full generated trace. Same-author isolated replay is reported separately after it is actually checked; there is no independent review, formal Task claim, Result admission or P000/worldview modification.

## 7. Exact next frontier

For this finite-budget baseline, the important gap is not another release fraction: the unchanged spatial rule has a strictly leaking material return operator. An actual sustaining mechanism must alter the relevant spatial return/retention or source/action relation, rather than merely delay the same escaping paths. Its native signed incidence, indivisible-event/readout bridge, third-action provenance, reaction and source lifecycle must still be sourced and verified.

Keep two open scopes separate: true native force/occupancy closure; and possible localization relative to an unbounded moving material group in this trial circuit. Do not infer the latter is impossible from a fixed-region theorem. Do not repeat U1 budgets, U2 triple memory, U3 circulation, U4 return-history witness or U5 global-sector totals as new discoveries. No prime prediction or square-shell selection has been obtained.
