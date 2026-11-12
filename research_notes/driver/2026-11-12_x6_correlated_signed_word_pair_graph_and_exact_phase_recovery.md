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
that is, precisely the two different words \((+,+)\) and \((-,-)\). Conversely, these two words really do collide: choose their initial depths to differ by \(+1\); both stage gaps then equal \(+1\). These collision witnesses are statements about the signed raw Cell chart \(\mathbb Z^6\). Coordinatewise nonnegativity through every intermediate signed rotation is **not** asserted; registered nonnegative final-address serialization is a distinct interface contract.

**Sharp language theorem.** For every fixed initial relative chart, the map \((h,w)\mapsto(y_1,y_2)\) is injective over \(h\in\mathbb Z,w\in L\) if and only if \(L\) does **not** contain both \((+,+)\) and \((-,-)\). This is an exact classification of all \(2^4=16\) possible two-stage languages; it has no independent physical-law claim.

Consequently the largest recoverable language retains **three of the four** words (75%, rather than the 50% retained by strict alternation). The two maximum-cardinality choices are
\[
L_+=\{(+,+),(+,-),(-,+)\},\quad
L_-=\{(+,-),(-,+),(-,-)\}.
\]
Each still permits both signs independently *as stage-wise marginals* at both stages. For example \(L_+\) can be implemented by carrying the first sign: after \(s_1=-1\), require \(s_2=+1\); after \(s_1=+1\), allow either sign. A two-state one-bit memory is sufficient. Under a stage-indexed, **one-state**, position/depth-independent word automaton, preserving both signs as each stage's marginal necessarily permits the full Cartesian product of four words and hence the alias. Thus two distinguishable boundary states are also necessary in this explicit automaton class.

An exact integer audit enumerated all four sign words and all 16 candidate sublanguages. Over initial depths \(-5,\ldots,5\), the only colliding distinct-word pair was \((-,-)\) versus \((+,+)\) (with their corresponding depths offset by one); the only three-word injective languages preserving both stage marginals were \(L_+\) and \(L_-\). The unrestricted integer argument above, not this finite test, establishes the universal theorem.

**Scientific contribution and boundary:** This strengthens the prior one-bit existence example into a sharp maximum-admissible-language and minimal-state classification. It does not assert that a physical Heartbeat/triadic law enforces either language. An X6 Researcher can test the actual registered law's accepted words against the single forbidden-pair criterion before invoking a larger pair-state graph. The original note's sections 1–5, their attribution, and the separation from Native Result/review remain unchanged.

## 7. Sharp m-stage sign-language recovery, block memory and rolling-window memory

**Scope.** This extends the two-stage example of §6, rather than asserting a physical Heartbeat law. For any integer (m\ge 1), let the registered stage map be the *same* signed coordinate permutation (R\in B_6) with (R e_1=e_2, R e_2=e_3, R e_3=-e_1), the remaining axes fixed, so (R D=D-2e_1). At each of the (m) consecutive observed stages, use one unknown signed-native step (s_i e_1), (s_i\in\{-1,+1\}). The observer knows (r=q(z_0)), all stage maps, and **every** stage relative readout (y_i=q(z_i)), where (z_i=R z_{i-1}+s_i e_1) and (z_0=r+hD), (h\in\mathbb Z). A registered admissible block language is (L\subseteq\{-,+\}^m), independent of (h).

**Exact all-length alias theorem.** For two histories yielding all the same observed (y_1,\ldots,y_m), write (z_i-z'_i=d_iD) (including (d_0=h-h')). Subtracting their stage updates gives

\[
d_iD=d_{i-1}(D-2e_1)+(s_i-s'_i)e_1.
\]

The five coordinates other than 1 force (d_i=d_{i-1}=d_0), while coordinate 1 forces (s_i-s'_i=2d_0), **for every** (i\). If (d_0=0), the signs are identical. If (d_0\ne0), since (s_i,s'_i\in\{-1,+1\}), necessarily (d_0=\pm1), and one complete word is (+^m) while the other is (-^m). Conversely, those two words with initial depths differing by 1 satisfy the same recurrence at every stage, so all registered relative observations agree. Thus

\[
(h,w)\longmapsto(y_1,\ldots,y_m)\quad\text{is injective on }\mathbb Z\times L
\quad\Longleftrightarrow\quad\{+^m,-^m\}\nsubseteq L.
\]

The maximum possible admissible language is therefore (2^m-1) words: omitting *either* one of the two constant-sign words suffices. This is sharp for every (m\ge1); for (m\ge2), all signs remain available in **each separate stage marginal**. The fraction (1-2^{-m}) retained by a fixed-length block increases with (m). This recovery is of the initial integer depth and entire signed word (hence net signed displacement at every stage); the stronger native BRC ordered-branch semantics, non-backtracking, nonnegative final codec and physical state update remain separately typed.

**Two different memory contracts.** For a stage-indexed length-(m\) **terminal block** with (m\ge2), the language (L=\{-,+\}^m\setminus\{-^m\}\) is realized by a two-state finite automaton recording whether a (+\) has appeared. At the block boundary, accept exactly when it has. A one-state, depth-independent stage-indexed transition automaton with both signs in each stage marginal accepts the full Cartesian product, including both forbidden words, so one bit is minimal in that class.

If instead **every rolling window of length (m\)** in an indefinitely continuing stream must be recoverable while retaining the all-plus path, the shift-invariant sufficient safety rule is *never emit (m\) consecutive minus signs*. Its deterministic on-line monitor has precisely (m\) non-failing states, storing the current run length (0,\ldots,m-1) of trailing minus signs (plus a rejecting sink if a complete-language recognizer is wanted). Distinct trailing-run states are distinguishable by a future minus suffix, so (m\) non-failing states are minimal for this exact rolling-window language. This is a different requirement from the one-bit terminal block; it uses \(\lceil\log_2 m\rceil\) bits of persistent memory for its non-failing state, not one bit for general (m\).

For exact finite-window inventory let (A_N^{(m)}\) count length-(N\) sign streams without (m\) consecutive minuses. It satisfies (A_N^{(m)}=2^N\) for (0\le N<m\), (A_m^{(m)}=2^m-1\), and

\[
A_N^{(m)}=\sum_{j=1}^{m} A_{N-j}^{(m)}\qquad(N>m),
\]

by partitioning by the last plus and its preceding trailing minus run. This provides an exact throughput/cost account for repeated safe windows, distinct from the single-block cardinality.

**Independent exact check.** For each (m=2,3,4,5,6,7), enumerated all (2^m\) signed words, depths (-2,\ldots,2), and the registered relative readouts starting from (r=(0,2,4,1,3,2)) under the displayed (R). In each enumeration the **only** different-word collision pair was ((+^m,-^m)), matching the unrestricted integer proof. This is a candidate spatial observer theorem and an executable finite-language filter for a future Source-registered Heartbeat/triadic transition law; it is not an independent Native Result, a physical-law registration or a closed X6 Task.
## 8. Mixed-sign arbitrary phase and moving exceptional-axis theorem

**Question and precise scope.** Sections 6–7 kept the same signed permutation \(R\) and the same step axis at every phase. Here fix any dimension \(n\geq3\), an arbitrary registered sequence of signed permutations \(g_1,\ldots,g_m\), and one signed native step \(s_i e_{a_i}\) at each observed phase, with \(s_i\in\{-1,+1\}\) and a registered but potentially moving axis \(a_i\). Require each direction vector \(\varepsilon_i=g_iD\) to be **mixed-sign** (at least one positive and one negative entry). Use the same signed raw state and full sequence of relative readouts as before:

\[
 z_0=r+hD,\qquad z_i=g_i z_{i-1}+s_i e_{a_i},
 \qquad y_i=q(z_i),\quad q(z)=z-\min_jz_j\,D.
\]

Here \(r=q(z_0)\) is known, \(h\in\mathbb Z\) is unknown, and all \(y_1,\ldots,y_m\) are registered. The legal sign language \(L\subseteq\{-1,+1\}^m\) does not depend on the hidden depth. No nonnegative intermediate-coordinate restriction or physical Heartbeat law is silently added.

Call phase \(i\) **singleton-aligned** if \(\varepsilon_i\) has one exceptional sign at coordinate \(a_i\), with the other \(n-1\) signs all equal to \(t_i\in\{-1,+1\}\) and \((\varepsilon_i)_{a_i}=-t_i\). This includes both one negative sign and \(n-1\) negative signs; \(t_i\) denotes the *majority* sign.

**Sharp moving-axis theorem.**

1. If **any** phase is not singleton-aligned, then \((h,s_1,\ldots,s_m)\mapsto (y_1,\ldots,y_m)\) is injective on the **entire** \( \mathbb Z\times\{-1,+1\}^m\). No sign-memory restriction is required.
2. If **every** phase is singleton-aligned, define \(p_0=1\) and \(p_i=\prod_{\ell=1}^{i}t_\ell\). Define the two phase-twisted words
   \[
   w^+=(p_1,\ldots,p_m),\qquad w^-=(-p_1,\ldots,-p_m).
   \]
   The **only** distinct-parameter collision is \(w^+\) against \(w^-\), with initial depths differing by exactly one in the corresponding orientation. The map restricted to \(\mathbb Z\times L\) is therefore injective if and only if \(L\) excludes at least one of those two words. Its maximum allowed language size is \(2^m-1\), and this bound is attained.
3. More generally, if the admissible initial depth set is \(H\subseteq\mathbb Z\), the sole potential collision in case (2) survives precisely when **both** twisted words are legal and \(H\) contains two consecutive integers. An explicit absolute-depth or position-dependent dynamical constraint may remove the witness; it must be checked separately.

**Proof.** Compare two legal histories with the same \(r\) and all the same \(y_i\). Since \(q(z)=q(z')\) exactly when \(z-z'=dD\) for an integer \(d\), introduce integer gaps \(d_i\), with \(d_0=h-h'\). The exact recurrence is
\[
 d_iD=d_{i-1}\varepsilon_i+(s_i-s_i')e_{a_i}. \tag{8.1}
\]
On every coordinate \(j\ne a_i\), this requires \(d_i=d_{i-1}(\varepsilon_i)_j\). If those \(n-1\) signs disagree, \(d_{i-1}=d_i=0\). If they agree and the phase is mixed, their common sign is \(t_i\), the exceptional coordinate has \(-t_i\), and (8.1) becomes
\[
 d_i=t_i d_{i-1},\qquad s_i-s_i'=2t_i d_{i-1}. \tag{8.2}
\]
If any \(d_{i-1}=0\) or \(d_i=0\), the nonexceptional coordinates and (8.1) force the other gap and sign difference to vanish. This propagates in both directions through every mixed-sign phase. Thus a nonsingleton-aligned stage forces all gaps and all sign differences to vanish, proving (1).

If every stage is singleton-aligned, (8.2) gives \(d_i=p_i d_0\). A nonzero gap demands \(2t_id_{i-1}=s_i-s_i'\in\{-2,0,2\}\), so \(d_0\in\{-1,+1\}\), and necessarily \(s_i=p_i d_0,\ s_i'=-p_i d_0\) for **each** stage. These are exactly the two twisted words. Conversely, they satisfy (8.1) with \(d_0=1\) (or the reversed ordering with \(-1\)), so the entire registered observation sequence coincides for every \(r\). Restricting the start depths to \(H\) gives the consecutive-integer criterion. QED.

**Concrete X6 mixed-majority collision.** For \(n=6\), take three diagonal signed-permutation phases with
\[
\varepsilon_1=(-1,+1,+1,+1,+1,+1),\ a_1=1;\quad
\varepsilon_2=(-1,-1,+1,-1,-1,-1),\ a_2=3;\quad
\varepsilon_3=(+1,-1,+1,+1,+1,+1),\ a_3=2.
\]
The majority signs are \((+1,-1,+1)\), so the exceptional-axis steps have the two and only two colliding sign words \((+,-,-)\) and \((-,+,+)\). For \(r=(0,3,2,1,4,2)\), initial depths \(h=1\) and \(h'=0\) respectively, the three min-zero readouts **in both histories** are
\[
(0,4,3,2,5,3),\quad(5,1,7,3,0,2),\quad(5,8,7,3,0,2).
\]
Changing **any one** stage step axis away from its sole exceptional-sign coordinate instead makes the full sign language injective, by part (1).

**Independent finite check.** As a consistency check separate from the universal proof, a deterministic exact-integer enumeration with pseudorandom seed 234 tested \(n=3,4,5,6\), phase counts \(m=1,2,3,4\), and 200 mixed-sign signed-permutation/axis configurations per \((n,m)\): 3,200 configurations in total. For each it enumerated all \(2^m\) sign words and initial depths \(-2,-1,0,1,2\) from a fixed randomly generated registered min-zero chart, compared the full tuple of normalized phase observations, and found **zero mismatches** with the theorem's predicted collisions and depth offsets. This is a sample check only; (8.1)–(8.2) prove the unrestricted-integer classification.

**Scientific impact and remaining boundary.** The all-\(R\) words \((+^m,-^m)\) of §7 are the special case \(t_i=+1\) at every stage. This generalization handles moving exceptional axes, alternating phase parity, and majority-negative frames without erasing the exact sequence of observations. It also identifies an admissible **zero-memory** route for fully varied signed step alphabets when even one registered stage is nonaligned. A real BRC/Heartbeat trajectory must still specify its physical \(\text{model\_law\_id}\), signed-step admissibility, branch/force correlation, position guards, and future observer equivalence; this theorem is an exact candidate-model filter and not a Native Result, independent review, Task closure, or new physical-law registration.
