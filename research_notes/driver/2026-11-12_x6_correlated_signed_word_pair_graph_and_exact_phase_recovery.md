# X6 signed-word recovery with correlated finite-state path memory

Status: DRIVER-AUTHORED MATHEMATICAL AUDIT / EXACT THEOREM IN EXPLICIT CANDIDATE MODEL / NOT A NATIVE RESULT OR INDEPENDENT REVIEW
Date: 2026-11-12 (+08)
Line: RS-X6-NATIVE-ROTATION-DYNAMICS; RS-X6-NATIVE-TIME-DYNAMICS
Source basis: `p000_reality_foundation.json` (signed primitive directions), `definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json`, `definitions/HEARTBEAT_SELF_CONSISTENT_INSTANT_V0_1.json`, and `definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json`.
Direct mathematical predecessors: `research_notes/driver/2026-11-12_x6_serial_signed_word_two_phase_injectivity_and_gap_graph.md` and `research_notes/driver/2026-11-12_x6_coherent_serial_phase_depth_alias_sharp_observation_box.md`.

## 1. Distinct question and model boundary

Earlier sharp signed-word criteria allowed **all** exact-length signed-axis words independently at each observed phase. A real ordered BRC/Heartbeat process may retain a finite branch, force, phase, or history state that correlates words across phases. Replacing such a correlated language with its independent per-phase projections can create fictitious aliases. We give an exact finite-state test that does not discard the correlation.

Fix `n>=2`, `D=(1,...,1)`, and `q(z)=z-(min_j z_j)D` on `Z^n`. The observer knows `r=q(z_0)`, while `z_0=r+hD` for unknown `h in Z`. At stage `i=1,...,m`, a *known* signed coordinate permutation `g_i` is applied and followed by an ordered signed-native word of fixed length `M_i`. Its net displacement is `b_i`, and

`z_i=g_i z_{i-1}+b_i,    y_i=q(z_i),    epsilon_i=g_i D.`

The legal words are accepted by a declared finite-state path device: a finite set `S`, admitted initial states `S_0`, and a stage-indexed finite directed transition system whose edges are labelled by `+e_j` or `-e_j`. Stage boundaries preserve the actual machine state. An optional registered, deterministic phase/frame update can be incorporated in the finite state. **Assumption for this theorem:** admissibility depends only on this registered machine state and word labels, not on the unknown absolute raw depth `h`. A position-dependent rule requires adding its position guard to the exact state model before applying the theorem.

Write `E_i(s,t)` for the set of net vectors realized by *accepted ordered words of length `M_i`* that take state `s` to state `t` at stage `i`. These are finite exact sets, but must be computed from the word machine, not from the unrestricted signed-word envelope `W_{M_i}`. Distinct accepted words with the same net vector may have different states and future behavior. The recovery target here is the parameter tuple `(h,b_1,...,b_m)`; it is **not** the entire ordered-word or branch identity.

## 2. Exact correlated pair-state theorem

For paired histories write `d_i in Z` for their raw common-diagonal difference at each registered observation. Construct a layered graph with vertices `(i,s,s',d_i)`. Draw a stage-`i` edge from `(i-1,s,s',d)` to `(i,t,t',e)` if and only if there exist

`b in E_i(s,t),    b' in E_i(s',t')`

such that

`b-b'=e D-d epsilon_i.                         (1)`

Start with `s,s' in S_0` and any integer `d_0`; preserve both machine states along the *same* registered stage sequence.

**Correlated-path recovery theorem.** Two admissible complete histories with the same initial relative chart have identical registered readouts `y_1,...,y_m` if and only if their machine-state pair and diagonal-gap sequence form a path in this graph. Their parameter tuples `(h,b_1,...,b_m)` differ if and only if at least one `d_i` on this path is nonzero. Hence the declared observer recovers the full parameter tuple precisely when there is **no feasible path with a nonzero depth-gap vertex**.

Proof: If `q(z_i)=q(z'_i)`, then `z_i-z'_i=d_iD` for an integer `d_i`. Subtract the two serial update equations to obtain (1). The machine traces provide the two `E_i` entries. Conversely, choose the exact legal words witnessing each graph edge, and start at `z_0=r+hD`, `z'_0=r+h'D` with `h-h'=d_0`. Induction using (1) gives `z_i-z'_i=d_iD` and therefore equal `q` readouts. Finally, if every `d_i=0`, (1) forces `b_i=b'_i` at each stage and `h=h'`; if some `d_i` is nonzero, either the initial depths or an intermediate net displacement differs. This proves the equivalence.

This graph also admits an *ordered-word* implementation: run two copies of the actual native finite-state machine in lockstep for `M_i` microsteps, accumulating `v=sum(a-a')`, and retain a boundary edge only when `v=eD-d epsilon_i`. A stage-by-stage union of projected legal words without carrying `(s,s')` is not equivalent in general.

### Finite gap domain / exact algorithm

Let `k_i` be the number of negative entries of `epsilon_i`; define `u_i=min(k_i,n-k_i)` for mixed-sign phases (`0<k_i<n`). Because `||b_i-b'_i||_1<=2M_i`, any pair-edge gap obeys

`C_{n,k_i}(d,e):=(n-k_i)|e-d|+k_i|e+d| <=2M_i.`

For a mixed phase, `C_{n,k_i}(d,e)/2 >= u_i max(|d|,|e|)`; thus both adjacent gaps have absolute value at most `floor(M_i/u_i)`. For a pure-sign phase, `k_i=0` or `k_i=n`, `|e-(+/-)d|<=floor(2M_i/n)`. Consequently **if at least one stage is mixed-sign**, every gap on any complete path lies in the finite interval `[-K,K]` for the safe bound

`K=max_{i:0<k_i<n} floor(M_i/u_i) + sum_{i:k_i in {0,n}} floor(2M_i/n).`

Build `E_i` by exact finite-state dynamic programming over the fixed word lengths, then test the finite layered pair graph for nonzero-gap reachability. No floating-point tolerance or heuristic truncation is involved. If every stage is pure-sign, the assumed depth-independent language makes the observer unable to distinguish different unrestricted initial depths; those cases need not be bounded artificially. If the initial depth belongs to `H subset Z`, restrict graph initial gaps to `H-H` with actual feasible pairs.

The simpler unrestricted gap graph remains a valid **necessary-envelope test**: if that graph excludes collisions, every correlated sublanguage also excludes them. A collision in the unrestricted envelope is not a valid witness for a correlated law until both entire words pass the same actual path-state machine.

## 3. Sharp X6 example: phase memory destroys a spurious alias

Use the previously declared six-axis candidate

`R(z_1,...,z_6)=(-z_3,z_1,z_2,z_4,z_5,z_6)`,

so `epsilon=RD=(-1,+1,+1,+1,+1,+1)`. Perform two serial `R` stages with `M_1=M_2=1`, each followed by one signed step on axis 1. Each **individual** stage permits both `+e_1` and `-e_1`; thus the independent per-stage marginals are identical.

Give the two-stage word machine one persistent sign bit `s in {-1,+1}`:

`b_1=s e_1,      b_2=-s e_1.`              (2)

The bit is chosen at stage 1 and retained through stage 2. It is a **declared candidate correlation example**, not an asserted physical force/triadic law.

With independent per-stage sign choices, the histories `h=1,(b_1,b_2)=(+e_1,+e_1)` and `h'=0,(b'_1,b'_2)=(-e_1,-e_1)` have equal `q` readouts at both stages (the earlier unrestricted signed-word collision at `(1,1)`). Under (2), both of those two-stage words are illegal.

More strongly, (2) makes the map `(h,s)->(y_1,y_2)` injective for **every** initial relative chart `r` and every integer `h`. Proof: compare bits `s,s'`. On coordinates 2 through 6, the first boundary equation forces `d_1=d_0`; on coordinate 1 it gives `d_1+d_0=s-s'`. If `s=s'`, both gaps vanish. If `s!=s'`, then `d_1=d_0=(s-s')/2`, a nonzero integer. The second boundary equation forces `d_2=d_1` from coordinates 2 through 6 and `d_2+d_1=-(s-s')` from coordinate 1. But its left side is `s-s'`, contradiction. Therefore no nonzero-gap pair exists. QED.

The example distinguishes (i) a mathematically valid collision in the **independent signed-word envelope** from (ii) a mathematically valid recovery guarantee in a **correlated two-stage sublanguage** whose per-stage marginal step sets have not changed. It is a strict information effect of preserving a one-bit cross-stage relation, not of replacing the signed alphabet by positive-only words.

## 4. Exact finite check and limits

A separate direct-integer check used four arbitrary registered min-zero initial charts, all depths `h=-10,...,10`, and both signs `s=+1,-1`, for `4*21*2=168` correlated two-stage histories. Within each fixed initial chart, no duplicate pair of readouts occurred; all four charts had 42 distinct paired readouts. The check is illustrative; the unrestricted-integer proof in §3 does the universal work. For `r=(0,...,0)` and `h=-4,...,4`, allowing independent signs at both stages gave 36 parameter histories but only 28 distinct paired readouts (8 collisions); the correlated model gave 18 histories and 18 distinct readouts.

No fixed `model_law_id` or complete triadic-force transition is installed by `definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json` (its `fixed_heartbeat_program` is null). `definitions/HEARTBEAT_SELF_CONSISTENT_INSTANT_V0_1.json` requires declared scope, source/boundary response, field/momentum state, branch provenance, `model_law_id`, and consistency status. Accordingly, the finite-state correlation above is a **research example** of a typed update component. It does not assert that Heartbeat dynamics physically implement sign alternation, nor that triadic closure has been proved for it. A physical claim needs a separately specified, Source-pinned model law and actual registered admissible force/branch transitions.

Even when the parameter tuple is recovered, the complete BRC word and internal branch state need not be recovered. Any further observer collapse must carry its own exact future-operation fiber-constancy/bisimulation certificate under the joint-observer preservation contract. If admissibility depends on absolute Cell position, fields, or unbounded history, one must enlarge the actual state or prove a finite quotient before using the finite graph.

## 5. Actionable audited frontier

For an existing X6 Time/Rotation Researcher with lawful owner CLAIM, the smallest next test is to supply a concrete proposed `model_law_id` with (a) exact per-microstep signed-axis admissibility, (b) triadic-force/field and boundary state updates, (c) registered phase/frame action, (d) the carried branch/correlation state and (e) the exact observer sequence. Compile its finite part to `E_i(s,t)` and run the pair graph; if the physical state is not finite, use a sound declared abstraction and classify the remaining proof obligation. Compare its verdict with the unrestricted gap envelope to quantify exactly which hypothetical aliases disappear by enforcing coherent provenance.

This note is an authored auxiliary model theorem, not independent mathematical review of the preceding Driver-authored notes. No Native Result accepted, no CLAIM/Task completion, no objective closure and no Foundation/P000 promotion are asserted.
## 6. Sharp maximal-permissiveness refinement for the two-stage X6 sign language

The alternating-bit language in section 3 is **sufficient but not maximally permissive**. At the exact same two-stage, one-microstep-per-stage, axis-1-only candidate, we can classify every admissible subset of the four signed words and quantify the smallest restriction required to preserve recovery.

Let a word be its two sign choices \((s_1,s_2)\in\{+1,-1\}^2\), and let \(L\) be any fixed, depth-independent subset of these four words. Comparing two histories with the same initial relative chart and equal readouts gives from stage 1 (coordinates 2 through 6, then coordinate 1)
\[
d_1=d_0,\qquad s_1-s'_1=2d_0.
\]
Stage 2 similarly gives
\[
d_2=d_1,\qquad s_2-s'_2=2d_1.
\]
Therefore a *nontrivial* alias is possible exactly when
\[
s_1-s'_1=s_2-s'_2\in\{-2,+2\},
\]
that is, precisely the two different words \((+,+)\) and \((-,-)\). Conversely, these two words really do collide: choose their initial depths to differ by \(+1\); both stage gaps then equal \(+1\). With sufficiently large shared baseline both histories may be kept in the nonnegative Cell orthant, if desired.

**Sharp language theorem.** For every fixed initial relative chart, the map \((h,w)\mapsto(y_1,y_2)\) is injective over \(h\in\mathbb Z,w\in L\) if and only if \(L\) does **not** contain both \((+,+)\) and \((-,-)\). This is an exact classification of all \(2^4=16\) possible two-stage languages; it has no independent physical-law claim.

Consequently the largest recoverable language retains **three of the four** words (75%, rather than the 50% retained by strict alternation). The two maximum-cardinality choices are
\[
L_+=\{(+,+),(+,-),(-,+)\},\quad
L_-=\{(+,-),(-,+),(-,-)\}.
\]
Each still permits both signs independently *as stage-wise marginals* at both stages. For example \(L_+\) can be implemented by carrying the first sign: after \(s_1=-1\), require \(s_2=+1\); after \(s_1=+1\), allow either sign. A two-state one-bit memory is sufficient. Under a stage-indexed, **one-state**, position/depth-independent word automaton, preserving both signs as each stage's marginal necessarily permits the full Cartesian product of four words and hence the alias. Thus two distinguishable boundary states are also necessary in this explicit automaton class.

An exact integer audit enumerated all four sign words and all 16 candidate sublanguages. Over initial depths \(-5,\ldots,5\), the only colliding distinct-word pair was \((-,-)\) versus \((+,+)\) (with their corresponding depths offset by one); the only three-word injective languages preserving both stage marginals were \(L_+\) and \(L_-\). The unrestricted integer argument above, not this finite test, establishes the universal theorem.

**Scientific contribution and boundary:** This strengthens the prior one-bit existence example into a sharp maximum-admissible-language and minimal-state classification. It does not assert that a physical Heartbeat/triadic law enforces either language. An X6 Researcher can test the actual registered law's accepted words against the single forbidden-pair criterion before invoking a larger pair-state graph. The original note's sections 1–5, their attribution, and the separation from Native Result/review remain unchanged.
