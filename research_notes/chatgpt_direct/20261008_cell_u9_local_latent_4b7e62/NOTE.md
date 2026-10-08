# U9 — local trail updates realizing the U8 stationary marginal

Event: EM-20261008-CELL-U9-LOCAL-LATENT-4B7E62
Status: CONDITIONAL_AUXILIARY_MODEL / ACTUAL_TYPED_BRC / UNREVIEWED / NOT_NATIVE_FORCE
Researcher: EM-DIRECT-0F8A19; activity RA-AF060260FAC823CCDD529366.
Own public session: MCP-95152fe1680a412b9029254fd2077d11.
Logical conversation: chatgpt-heartbeat-cell-attraction-20261006-8b74f0 (not platform-attested).
Global read: ea414f16dfebfb651fcef8ebd4152d8ef6c33471.
EM intake: 49e906174c388a5567501da555e6a4c789f16d75.
Own registration observed at 221eb28ec4abfbcd2223c3bfcfc72f1487675e2a, blob ca653dcd7b3e23fd29e78966bdefaecb6065e29e.

## 0. New question and retained limits

Consume U8 at e06109fd37624b833e3f5dfdd1f8d46e0b527dea, directory research_notes/chatgpt_direct/20261008_cell_u8_connected_retention_5e91c4. It supplied K(r)=sum_z G(z)G(z-r) and W_N(X)=sum_T product_edges K, with finite relative excluded partition Z. Its global-score Barker motion was explicitly engineered, not derived force. U7 remains an excluded different circuit. The parallel residual-selector note is consumed at TEST_ONLY strength; it does not supply the missing native force lift.

Here we replace evaluation of the summed score at every move by a declared auxiliary-state algorithm. Its stationary positional marginal is EXACTLY U8, without a finite path cutoff. Its projected trajectories are NOT asserted to equal the U8 memoryless Barker dynamics. Material updates are local one-edge moves; complete trail editing, tree reassociation and their scheduling still have computational communication requirements. No autonomous finite-speed physical event implementation or reaction law is supplied.

P000, six spatial axes/twelve ports and separate time are retained. A path record is not an indivisible force quantum; a three-identity graph slide is not TRIADIC_CLOSURE_E. Scores, normalized trial weights, BRC counts, record length, physical response/energy and time remain distinct. No U5 field is reset, transported with a source, or claimed to be the new auxiliary configuration.

## 1. Expand the state instead of recomputing the sum

For N labelled, distinct material Cells X, let T be a labelled spanning tree. For every edge e={i,j} retain two finite ordered native words gamma_(e,i), gamma_(e,j) whose endpoints agree:

  x_i + displacement(gamma_(e,i)) = x_j + displacement(gamma_(e,j)) = z_e.

The meeting z_e is determined by these records and is not separately overcounted. Words can backtrack, cross or visit materials; only material positions have exclusion. Define L as the sum of all leg lengths, and the positive microstate weight m(sigma)=lambda^L, 0<lambda<1/12. The empty word is permitted. Quotient all locations by a common translation; choosing x_0=0 is only a chart convention.

**Marginal identity.** For fixed X, summing m over all its tree/meeting/word states gives W_N(X). For a fixed tree, independent sums over the two words on each edge give its K factor. Positive summation over trees then gives W_N. This is the exact expansion used by U8, now retained as state; it does not declare all those relations simultaneously present in one sampled microstate. The positive branch law retains all alternatives.

Consequently the augmented partition equals U8's finite Z, and m/Z defines a probability measure on the countable relative microstate space. Forgetting auxiliary state is valid for this stationary position observation. It is NOT thereby valid for future transition queries.

## 2. A precise four-channel proposal grammar

Choose four channels with weight 1/4 each. All invalid proposals stay put; no postselection renormalization is used. Let E=N(N-1)/2. Edge selection always ranges over all E unordered identity pairs, not just currently present edges. Missing edges give waits. This makes forward/reverse proposal weights equal.

**M: material update.** Choose actor a, port p and grow/shrink equally. Propose x_a'=x_a+d(p); collisions wait. In grow mode prepend -p to EVERY incident leg starting at a. Those paths now start at x_a' and first traverse back to x_a; their old tails and meeting Cells stay unchanged. This increases L by deg_T(a). Shrink requires EVERY incident leg to start with +p, removes this first edge, and decreases L by deg_T(a). Its new starting Cell is also x_a+d(p). Reverse (a,p,grow) by (a,-p,shrink). No remote source or meeting is moved. Data needed are vacancy, incident-link identities and their first ports, not K,W or Z.

**J: meeting update.** Choose pair e, port p and grow/shrink equally. Grow appends p to BOTH legs and moves that meeting one native edge. Shrink requires both last letters p and removes them. Reverse uses the same e,p and opposite mode. Delta L is +2 or -2. This moves a path meeting, not a material.

**W: word edit.** Choose e and one of its two legs; choose equally detour or commute. Choose word index j>=0 with weight 2^(-j-1), independently of current word length. A detour additionally selects p and grow/shrink equally: insert (p,-p) at index j, or remove exactly that pair there. Delta L is +/-2; reverse labels have the SAME j,p. A commute swaps two adjacent different-axis letters at j; it is its own inverse and has Delta L=0. Undefined edits wait. The infinite index tail is part of the proposal grammar, not a truncation. Its mean index is one. Uniformly selecting currently available indices instead would need a length-dependent Hastings correction and is NOT the defined rule.

**S: witnessed tree slide.** Choose ordered distinct identities (a,b,c) equally; for N=2 this channel waits. Require tree edges ab,bc and identical words from b on these edges. The two meetings then coincide. Replace ab by ac, retaining its a leg and using the c leg of bc; keep bc. A tree remains a tree: after removing ab, b and c are in the same component, and ac joins the two components. There was no ac edge, since that would have formed a cycle. Reverse uses (a,c,b); the removed b leg is recovered from retained bc. Delta L=len(gamma_bc,c)-len(gamma_bc,b). This is an invertible relation-record operation, not a force-balancing event. Equality of long trails can require traversal or a verified shared-record handle; no constant-time physical equality oracle is claimed.

For each valid label ell with result sigma', accept with

  alpha(sigma,ell)=lambda^(L'-L)/(1+lambda^(L'-L)).

The implementation evaluates only NONNEGATIVE powers: for Delta>=0 normalize (lambda^Delta,1); otherwise normalize (1,lambda^(-Delta)). All accept/reject weights, changed-word weights and composition use the unchanged weighted BRC. A negative exponent in the displayed ratio is not a negative path or signed mass. Unaffected factors cancel only in the acceptance observer; their records remain in the microstate.

## 3. Detailed balance and reachability, without a global score oracle

Each label has the stated reverse with the same proposal weight q. Thus

  m(sigma) q alpha = q m(sigma)m(sigma')/[m(sigma)+m(sigma')]
                  = m(sigma') q alpha_reverse.

Sum over paired labels, including multiplicity and invalid waits. This proves invariance of m/Z. It never calls W_N(X), enumerates all trees at each update, evaluates an infinite Green sum, or enforces a path-length cap.

For 2<=N<=6 this relative chain is irreducible and aperiodic:

1. Any two words with the same start/end can be connected by the permitted detour and commute edits. Commute distinct-axis letters to group axes, cancel adjacent opposite pairs within each group, and obtain the ordered coordinate word; reverse edits build any other word. These are REAL transitions between distinct states, not equivalence classes deleting future-relevant histories.
2. Move any meeting to a chosen Cell by repeated joint append operations, then edit its individual words as in 1. Thus, at fixed X,T, all meeting/word configurations communicate.
3. With all meetings at one Cell and a common chosen word from each actor to that Cell, any abstract tree slide is witnessed. Slides connect labelled trees: slide edges of vertices at depth>=2 along the next edge toward a root, decreasing the sum of tree depths until a star is reached. The reverse moves reach any target tree.
4. Z6 minus at most N-1<=5 occupied sites is connected. From a free point at least one of its six coordinate lines contains no obstacle. Follow it to a coordinate value absent from all obstacles; that hyperplane has no obstacles. Use fresh remaining coordinates to reach a shared remote parking location. Applying this construction one actor at a time permits arbitrary labelled distinct layouts via remote parking sites chosen outside both endpoint layouts. Each step can use grow mode and has strictly positive acceptance. Subsequently adjust the auxiliary records by 1-3.
5. Positive Barker rejection supplies a self-loop at every state. The geometric invalid-index tail does too.

Therefore the countable relative chain has the unique invariant probability m/Z and converges to it from each microstate (no mixing-time bound is supplied). Its invariant position marginal is U8's pi_N. For larger N, invariance and finite normalization still hold; this note does not extend the above bounded-obstacle irreducibility proof without justification.

These are algorithmic statements. Graph slots/trails may be distributed, but selecting an indexed event, traversing a trail, comparing words, updating remote endpoint handles and serializing concurrent operations have costs. Only M's geometric support is strictly one-edge local in this implementation. No synchronous arbitrary-speed global communication is promoted to a physical law.

## 4. Exact original-four marginal certificate

Use the original four positions (0,e1,e1+e2,e2). Enumerate ALL augmented states with total L<=5. Each of the three tree links has length at least one, so each link needs length at most three. Enumerating native words through three edges and ALL their split positions is therefore a complete cover for this bounded joint question, not an unproved numerical truncation.

The counts are

  L=3:32; L=4:192; L=5:6624; total6848 distinct microstates.

Their exact BRC sum is 32 lambda^3 +192 lambda^4 +6624 lambda^5. A separately composed expression using the inherited U8 endpoint BRC recurrence and all sixteen trees agrees in count,total AND dominant weight. This checks the NEW joint-state marginal implementation; it does not rerun the whole U8 study or infer the infinite identity from finite samples.

## 5. Same position, tree, meetings, length and score, different next motion

Use tree T={01,12,23}, meeting each edge at its higher-index endpoint. On edge01 let the leg starting at actor0 be

  P: (+e3,+e1,-e3),     Q: (-e3,+e1,+e3),

and let its actor1 leg be empty. Other legs follow their one-edge paths. Both states have the original four positions, the same T and all meetings, L=5 and CWM=(1,lambda^5,lambda^5). At lambda=1/48 that weight is 1/254803968.

In M, actor0 is a leaf. Its +e3 shrink is permitted in P with acceptance 48/49, but is ineligible in Q. The +e3 grow is allowed in both with acceptance1/49. Including the declared channel, actor, port and mode selection, the exact next-position weights of moving actor0 to +e3 are

  P:1/384, Q:1/18816.

The -e3 weights are reversed. All other position weights agree; internal channels do not change positions. Hence the entire one-query position laws have EXACT TV=1/392. The two inputs can be prepared from the same base microstate by one signed detour insertion followed by one adjacent different-axis commute. Their chosen preparation paths have positive, explicitly computed weights. They are controlled candidate-algorithm histories, not empirically observed native states.

Thus no position-only transition kernel represents all these microstates. Even current tree, meetings, scalar path length and score together omit necessary information. Equality of stationary positional laws does not imply equality of trajectories or of conditional responses. This note does not assert that every conceivable equilibrium-only projection fails every weaker Markov property; the proved obstruction is the explicit lack of a universal fibre-constant position update.

## 6. Storage and physical-source limits

The total number of path records is 2(N-1), but their lengths are not uniformly bounded. With Z(lambda) the relative partition,

  E[L]=lambda Z'(lambda)/Z(lambda)<infinity.

A positive upper bound follows by allowing collisions and summing all tree increments: their total is t_N(1-rho)^(-2(N-1)), rho=12lambda. Differentiating positive coefficients yields

  sum_sigma L lambda^L <= 2(N-1)rho t_N(1-rho)^(-(2N-1)).

Divide by any verified positive lower bound on Z. This proves finite expected record length, not a sharp resource estimate, bounded physical energy or a fixed finite memory guarantee. Each realized finite word can be processed in finite work, but access/acceptance and mixing costs still matter.

A useful obstruction: imposing a fixed count B of indivisible path-edge tokens with one token per recorded edge forces L<=B. The full target gives positive weight to arbitrary added backtracks, hence to L>B. Such a capped inventory cannot realize the exact target; it would define a NEW truncated model. Either path records are not material quanta, or an additional sourced mechanism/representation is needed. A finite mean is not a conservation law.

Nor does a stationary marginal determine force or time. For any 0<eta<1, (1-eta)I+eta Q preserves the same invariant law but changes every nontrivial one-step probability. Without an independent event/clock law, fitting the static law cannot choose eta or establish a mechanical reaction. Native signed triad certificates, third-action provenance and reaction remain OPEN. Three labels in a slide do not fill those obligations.

## 7. Execution and literature boundaries

check_u9.py actually uses local_latent.py -> unchanged connected_retention.py (Git blob569e6171d0052fbfd41cf007b09a8327b339228b) -> unchanged packet_router.py (7465f5aa16cbb8fba61ba4be80f8a6884b879c53) -> brc_weighted.py (3f205696709e847909958a153f8fe10d3f6b70f0). The original adapter's two unused relative imports are the only inherited loading adjustment. No function bodies of existing scientific kernels are changed. Geometric index tails use actual positive recurrent BRC; no infinity of proposal labels is falsely represented as a finite raw count.

The checker covers every local label in its declared finite inputs, three parameters, all6848 bounded joint states, complete96-label material queries, positive controlled preparation paths, and all tree slides for N=3,4,5. It checks exact inverses and CWM balance, not just decimal tolerances. Native physics, long sampled trajectories and independent review are not claimed. The first development check caught a factor-two mistake in a hand-written expected one-query fraction; the actual law and TV were correct. Expected fractions were corrected before final replay; this is not a structural residual.

General expanded-state path sampling and reversible auxiliary-variable updates have prior art. Official abstracts checked: Prokof'ev/Svistunov, Worm algorithms for classical statistical models, arXiv:cond-mat/0103146; Andrieu/Lee/Livingstone, A general perspective on the Metropolis-Hastings kernel, arXiv:2012.14881. Only metadata/abstracts were read; neither supplies this native mechanics nor this model-specific certificate. No general MCMC invention claim is made. The dedicated query attempt in this turn was blocked by platform safety checks and was NOT retried by another route. Official public sources are distinct from that uncompleted provider request.

## 8. Durable next frontier

The computational global-score oracle is no longer required for this conditional stationary candidate: an explicit enlarged-state kernel has the desired marginal, with finite per-state exact acceptance calculations. A future physical bridge must realize/update these records through admissible local action events, with finite communication, inventory interpretation and reaction, or falsify this particular candidate. It must not assume a tree slide is primitive triadic balance, a Gibbs weight is energy, or an algorithmic step is heartbeat time. Consume U1-U8 and this exact marginal/non-lumpability result, not repeat release-parameter sweeps. No prime formula or unique landing has been obtained.
