# Enterprise Math R5 — Exposed two-key simplex faces are a convex-hull veto in absorbing stop/continue models

Date: 2026-10-29 (Asia/Shanghai). Author-side **portable mathematical research**, not native Source task execution or an admitted theorem. Status: `AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING`.

## Frozen sources, question and observer typing

- Account-wide GLOBAL_KNOWLEDGE_V1 canonical `main@68642df618f0730b271f1e78fce3ce3ab10a5aad` (verified by remote branch read). Applicable `00_BOOTSTRAP.md`, `OPERATING_MANUAL.md`, P000-related worldview, `MATH_RESEARCH_POLICY.json`, BRC protocol and research activity protocol were read at this immutable account snapshot.
- Project Enterprise Math canonical `main@4ffdef264544aeea65b68be98a36ab5a829d9f12` (verified by remote branch read). Applied `AGENTS.md`, `p000_reality_foundation.json`, `definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json`, the joint-observer contract, `docs/AUTONOMOUS_RESEARCH_OPERATIONS.zh-CN.md`, and `docs/PORTABLE_RESEARCH_PROTOCOL.md` at this pin.
- Exact prior research frontier (unreviewed): `research_notes/brc_r5_facet_bellman_face_obstruction_20261029_t1837/RESEARCH.md` at immutable PR commit `65ff2d28290c39ef7e00ecaf86823046e825d36c`, especially its Theorem 2 and NEXT_TASK. The mother problem asks for equal **all-signed four-observer convex hulls** but unequal real behavioral observer images.
- Scoped external mathematical model: finite, two-probability-law, acyclic **absorbing stopping** decision tree, with perfect-recall FULL behavioral strategies and no-persistent-seed policies keyed by exact `(time, likelihood ratio)` (LR). `O=(e_P,e_Q,T_P,T_Q)`: errors of two terminal declarations and expectations of terminal time under P,Q. This is an *external finite statistical model*, not a native X6 embedding, physical-time calibration, or a claim about the truth of P000.
- BRC usage: `REUSE_APPLIED`, exact positive P and Q branch masses with origin/path labels; postpone LR quotient until all source-labeled continuation/bypass contributions are accounted for. The erased observer-relevant residue is precisely whether a later LR key was reached **through** an earlier continue choice or **around** it. No signed-amplitude interpretation of positive branch masses.

Native service read reported `research_authority_granted=false` / `UPSTREAM_CODE_REVIEW_REQUIRED`, and the bounded current-owner inventory request returned `CONTROL_QUOTA`. Hence current Source owner/CLAIM/Result could not be authenticated; this note does **not** purport to occupy or replace another researcher's Task.

## Theorem — four-corner exposed-simplex veto (all real policies)

Let a finite two-law stopping model have strictly absorbing stop actions (with a specified declaration) and continue actions, and let FULL observe the complete history, including whether an earlier decision point was visited. Consider two **different time-labelled LR decision keys** `k=(t,r)` and `l=(s,r')` with `t<s`. Fix the same deterministic actions at every other LR key. At each of `k,l`, let action 0 be a fixed stop-and-declare action and action 1 be continue. Let `D_ij` be the four resulting deterministic LR policies, and `V_ij=O(D_ij)`.

Suppose there is a signed `w in Q^4` (or R^4 for the qualitative assertion) and `h` such that the exposed face of the **complete** deterministic LR convex hull

`C_LR = conv{O(D) : D deterministic LR}`

satisfies

`F = {z in C_LR : w·z=h=min_{v in C_LR} w·v} = conv(V_00,V_10,V_01,V_11)`

and the four `V_ij` are affinely independent (a three-dimensional simplex). Other deterministic LR policies may map to points *inside* this face; only its four extreme vertices are stipulated. Then

**`C_FULL != C_LR`.** More precisely, the deterministic FULL observer

`H = V_00 + V_11 - V_01`

is legal, satisfies `w·H=h`, and is **outside** `C_LR`. Consequently the model cannot solve the R5 mother problem (which requires hull equality), even though the previous Theorem 2 also supplies an LR-actual-image nonmembership point under a related face hypothesis.

If every probability/cost is rational, a finite exact rational separating functional can be constructed without CAD or a full new facet enumeration.

### Proof (no independence or source-label shortcut)

**1. BRC branch partition.** Under the four policies, partition full trajectories by the historical occurrence of key `k`. A trajectory through `k` which takes action 0 stops and cannot reach later `l` (absorbing stopping). For action 1 at `k`, any later visit to `l` is in the **via-k** class. Other histories reaching `l` are the **bypass-k** class. Retain these disjoint origin/path labels, P and Q masses, and terminal error/time payloads. The fixed policies at all other keys make the four-observer map multi-affine in the two action probabilities. Since the action at `l` affects the bypass class even when action 0 is taken at `k`, and affects via-k only when action 1 is taken at `k`, there are (vector-valued) coefficients `C,U,B,A in R^4` with

`O_LR(x,y) = C + U*x + B*y + A*x*y`, where `x,y in [0,1]`.

Here `B` is the bypass-key `l` action contrast; `A` is the via-k contrast. This identity holds simultaneously for P and Q error/time coordinates, because each is linear in terminal path masses. It does not treat hidden positive source flows as signed amplitudes.

**2. Perfect-recall split policy.** FULL can make its later action at `l` depend on whether the history visited `k`. Keep `k=continue` and every other fixed action, choose `l=continue` on via-k histories but `l=stop` on bypass histories. This is a legal deterministic perfect-recall policy with

`H = C+U+A = V_00+V_11-V_01`.

This explicitly shows the signed *observer identity* comes from differences of legal positive-mass policy outputs; no negative trajectory probability has been assigned. The companion split (via-k stop, bypass-k continue) gives `H'=V_10+V_01-V_00`.

**3. Exposed-face contradiction.** Because `w·V_ij=h`, we have `w·H=h`. If `H` belonged to `C_LR`, it would have to belong to its exposed face `F`. Affine independence makes the barycentric coefficients of `H` in the simplex unique. They are `(1,0,-1,1)` relative to `(V_00,V_10,V_01,V_11)`, which contain a negative component. Thus `H notin F`, contradiction. Therefore `H notin C_LR`, proving the strict all-signed convex-hull gap. The argument covers *every real behavioral LR policy* because such policies' observer outputs lie in `C_LR` by finite multi-affine expansion.

**4. Exact Farkas separator.** In the rational case choose any rational affine functional `L_01(z)=a·z+c` extending the barycentric coordinate of `V_01` from the affine span of the four corners, so `L_01(V_01)=1` and `L_01(V_00)=L_01(V_10)=L_01(V_11)=0`. Such an extension exists by exact rational Gaussian elimination. For each deterministic LR output `d` off the face, put `delta_d=w·d-h>0` and

`M = max({0} union { -L_01(d)/delta_d : d is off-face })`.

There are finitely many outputs, so `M` is rational and nonnegative; if all deterministic outputs lie on the face, set `M=0`. Then

`Phi(z)=L_01(z)+M*(w·z-h)>=0` for **every** LR deterministic output, hence for all real LR outputs. For any on-face output, `L_01>=0` as it lies in the simplex. But `Phi(H)=-1`. Hence `Phi>=0` is a rational all-real support separator, and the sup-norm distance of `H` to every LR output is at least `1/||a+M*w||_1`, with nonzero normal forced by `Phi(H)=-1`. This is a direct Farkas-style certificate.

**5. Structural necessity.** If no trajectories reach `l` through `k`, then `A=0` and the four vectors have affine rank at most 2. If no trajectories reach `l` by bypassing `k`, then `B=0` and `V_00=V_01`. Therefore rank three requires both types of route to carry an observable contrast. This is the precise path residual destroyed by the LR quotient; the two FULL split actions are permitted by perfect recall and incompatible with a four-vertex simplex face under hull equality.

### What this changes about the previous R5 next-task proposal

The earlier Theorem 2 (`65ff2d28...`) correctly states an **LR actual-image nonmembership** criterion conditional on a four-corner exposed face. This new theorem establishes that, **in the absorbing stop/continue model with two time-ordered keys and unrestricted FULL perfect recall**, the same four-corner rank-three simplex *already forces unequal FULL/LR convex hulls*. Therefore the suggested strategy of (i) certify all-signed hull equality, then (ii) seek exactly this exposed four-corner simplex to solve the mother problem is **mathematically infeasible in this model**. This is a scope correction to the search strategy, **not** a retraction of the algebraic rank-one nonmembership proof in the old note. Avoid searching for a universal counterexample under simultaneously incompatible conditions.

The theorem does **not** eliminate possible mother examples with non-simplex exposed faces, additional exposed LR vertices accommodating the FULL split points, different nonabsorbing controls, or more complicated interactions. Those cases retain genuine unsolved status.

## Strictly-positive rational branch illustration and independent finite computation

Construct a finite **partially controlled DAG** (a forced bypass at time 1; this example is not claimed to satisfy every native mother topology requirement). Initially origins A and B each have P=Q mass `1/2`, so their LR at the source decision stage and the later merger is 1. At time 1, A alone has decision `x` (stop+declare P/Q or continue); B necessarily transits. At time 2 both reach the same LR key `y` if A continued; B arrives independently. At y each may stop+declare P/Q or continue. Continue yields two time-3 signals low/high with the **conditional** probability kernels:

- A: `P=(1/4,3/4)`, `Q=(3/4,1/4)`; terminal LR keys `(1/3,3)`.
- B: `P=(2/5,3/5)`, `Q=(3/5,2/5)`; terminal LR keys `(2/3,3/2)`.

Every conditional probability under both laws is strictly positive and exactly normalized. At time 3 declare Q for low LR and P for high LR. These four terminal LR values are distinct; hence all LR terminal decisions may be independently optimized. Under the fixed terminal declarations, the four rectangle outputs in order `V00,V01,V10,V11` are

`V00=(0,1,3/2,3/2)`,
`V01=(1/5,7/10,2,2)`,
`V10=(0,1,2,2)`,
`V11=(13/40,13/40,3,3)`.

The determinant of `(V10-V00,V01-V00,V11-V00)` in coordinates `(e_P,e_Q,T_P)` is `-3/160`, proving affine rank three. The legal FULL history-dependent split policy `x=continue`, `y_A=continue`, `y_B=stop+declare P` gives

`H=(1/8,5/8,5/2,5/2)=V00+V11-V01`.

For **all** LR deterministic policies of the *entire specified illustrative DAG*, including all 16 independent time-3 declarations and all 3x3 stop/declaration/continue choices at x,y, the exact signed objective

`100e_P+100e_Q+11T_P+11T_Q`

has minimum **131**; for FULL deterministic policies (3x3x3x16) its minimum is **130**, realized by H. Hence the integer inequality `100e_P+100e_Q+11T_P+11T_Q>=131` holds for *all real LR behavioral policies*, but H evaluates to 130, and the corresponding `L_infinity` distance is at least `1/222`. The finite complete enumeration is independently justified by multi-affinity and full perfect-recall vertex optimization. The example's four rectangle corners are **not** claimed to form an exposed simplex face for this signed objective: it illustrates the route-splitting algebra and a separate certified support gap, not an instance of an impossible combination of mother conditions.

`VERIFY.py` is a standalone, executed standard-library `Fraction` checker: 144 deterministic LR policies, 432 deterministic FULL policies, 4 corner vectors, nonzero affine determinant, the full split equality, true normalized positive kernels, four terminal LR keys and the exact signed gap. An additional symbolic-coordinate rational toy verifies the `M` separator mechanism (abstract only; not a stopping realization). `EXACT_OUTPUT.txt` is the actual successful stdout ending `PASS_EXACT_R5_BYPASS_RECTANGLE_FACET_VETO`. No Lean proof or independent reviewer was used.

## Literature and limits

- Kuhn (1953) perfect-recall mixed/behavioral realization equivalence, contextual textbook treatment: Maschler, Solan, Zamir, *Game Theory*, Cambridge University Press, 2013, chapter 6, DOI `10.1017/CBO9780511794216.007`, https://www.cambridge.org/core/books/abs/game-theory/behavior-strategies-and-kuhns-theorem/8CF3A6CC31B4607E24CB286D0E82ABB3 . The present explicit FULL path-flow argument does not depend on external novelty priority.
- Anderson and Montúfar, *The Value Function Semi-Algebraic Set in Partially Observable Markov Decision Processes*, ICML 2026, PMLR 306:2677–2715, https://proceedings.mlr.press/v306/anderson26a.html . Its setting is infinite-horizon memoryless POMDP policy value geometry, not this finite two-law four-observer theorem. This is background only; no claim of novelty priority or direct theorem transfer.

**Scope:** finite absorbing stopping, time-labelled two LR keys, fixed other deterministic actions, four-corner face exactly their rank-three simplex. This no-go proves nothing about physical X6, P000, all possible LR models, or any unexamined two-merger candidate. Native independent mathematical review and Source admission remain pending.

## Next exact question

After exact all-signed hull equality on a genuinely source-sensitive, interacting **two-merger** DAG, investigate an LR exposed face with *additional* vertices and determine whether each full-history bypass/via split vector lies in that LR face with exact rational primal combinations. If yes, test whether the genuine LR behavioral image still misses an interior FULL point using exact semialgebraic constraints (including zero-flow boundaries). If any split vector lies outside its face, output the rational Phi separator above and reject the candidate. Preserve source-labelled BRC P/Q weights and both exact LR collision equations throughout.
