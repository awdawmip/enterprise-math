# R762GY — Perfect-matching phase dynamics and exact BRC return fibers of an oriented X6 triadic Port candidate

Date: 2026-11-20 (Asia/Shanghai).
Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS / TP2-8B7E13C5904A2D6F1142.
Research line: historical EM-X6-3050F6; source-side independent portable continuation.
Frozen taskbook: awdawmip/enterprise-math@857280d1012943290d141d1317179c40ec3cbdf8.
Frozen P000: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
Previous exact candidate: R762GX at awdawmip/enterprise-math@ffd6cdc5ee6ed64bb65490efd1e58fe9bce954f9.
Current rules are read separately from frozen scientific inputs.
Mathematical status: AUTHOR-PROVED candidate-model results; finite checker PASS; independent review NOT_REVIEWED.

## Scientific question

R762GX proves that a deterministic choice of a different edge incident to a selected K4 STAR vertex cannot preserve full S4 covariance unless one keeps two BRC branches or a one-bit orientation residual. It also counts the fixed-active-vertex six-event joint Cell/Port return.

The new question is what happens when the active endpoint is *reselected at each event*. This is a precisely specified positive-BRC extension rather than an assertion about the complete native TRIADIC_CLOSURE_E permission predicate. We seek exact unbounded-horizon invariants, finite source counts and an observer-loss witness.

## Candidate event and type declaration

Use four auxiliary incidence vertices V={0,1,2,3} to index the six *native* X6 signed spatial axes, namely the unordered edges 01,02,03,12,13,23 of K4. These four auxiliary vertices are not four extra spatial dimensions. Let H_v in Z^6 be the incidence vector of the three axes incident to v. A candidate signed STAR event at v has three coattached nonzero primitive force quanta on these axes and a declared Link/triad witness. Its composite chart displacement is s H_v, s in {+1,-1}. This is an explicit model update, not a derivation of motion from P000 force balance.

The current named Port e={u,v} is one K4 edge. Fix orientation chirality chi in {+1,-1} relative to the declared K4 reference order. At each time t choose either endpoint v in e as active and independently choose sign s. Let a=T_chi(v,u) be the unique remaining vertex a such that sign(v,u,a,b)=chi, with b the fourth vertex. The transition is

\[
 (x,e,\chi,t)\xrightarrow{(v,s)}
 (x+sH_v,\{v,T_\chi(v,u)\},\chi,t+1).
\]

Record the selected endpoint, sign, ordered triad witness, old/new named Port, Link and BRC source identity. There are exactly four equally weighted positive source branches per state (two endpoint choices times two signed events). The event ordinal t is separately typed relational order, not a seventh spatial axis or calibrated physical heartbeat time. Full provenance is kept even when the following projection forgets it.

Under pi in S4, act on six axes by edge relabeling and on chi by sign(pi)*chi. This is the covariant transport inherited from GX1/GX2.

## Theorem GY1 — a deterministic three-phase matching cycle

Partition the six named Ports into three perfect matchings:

\[
 M_0=\{01,23\},\qquad M_1=\{02,13\},\qquad M_2=\{03,12\}.
\]

Write j(e) in {0,1,2} for its matching index. For every admissible active endpoint and every sign, one step satisfies the **exact** law

\[
 \boxed{j(e_{t+1})\equiv j(e_t)+\chi\pmod3.}
\]

More strongly, from either edge in M_j the two endpoint selections lead to the *two distinct* edges of M_{j+chi}, exactly once each. Thus the directed six-Port graph at fixed chi consists of a cyclic chain of complete two-by-two bipartite links between consecutive matching layers (forward for chi=+1, reverse for chi=-1).

**Proof.** For chi=+1, direct substitution of the sign(v,u,a,b) rule gives 01 and 23 each leading to exactly 02 and 13; 02 and 13 each leading to exactly 03 and 12; 03 and 12 each leading to exactly 01 and 23. The chi=-1 rule reverses these three matching-layer transitions. The edge-unordered, sign-independent enumeration covers all six starting Ports, both endpoint choices and both chiralities; the signed event choice does not change the next Port. QED.

**Corollary (exact all-length Port return).** Start from any specified e0 and fixed chi. Let P_m be the number of length-m ordered signed BRC source words that return to e0, regardless of final Cell. Then

\[
 \boxed{P_0=1;\quad
 P_m=\begin{cases}4^m/2,&m>0,\ 3\mid m,\\0,&m>0,\ 3\nmid m.\end{cases}}
\]

With the four outgoing branches carrying equal probability 1/4, the Port-return probability for positive m is exactly 1/2 when 3 divides m and 0 otherwise.

**Proof.** For m>0, after each step the two endpoint choices select the two edges of the next matching layer bijectively. Consequently, for every m>0, the 2^m endpoint-choice words are evenly split between the two edges of the uniquely determined matching layer. The independent signed choices multiply every endpoint word by 2^m BRC histories. The initial edge lies in the current layer exactly if 3 divides m. QED.

This is stronger than a finite return table: it is valid for every nonnegative event count under the stated extension. It also gives an exact state projection onto three matching phases for the **phase-only future observer at fixed chi**.

## Theorem GY2 — complete X6 Cell plus Port return is supported exactly at multiples of six

Let Z_m count length-m signed BRC source words that return *both* to the initial named Port and to the original complete X6 chart Cell, while keeping fixed chi. Then

\[
 \boxed{Z_m>0 \iff 6\mid m\qquad(m\ge0).}
\]

The empty word at m=0 contributes Z_0=1. A nonempty joint return first appears at length six.

**Proof.** Given signed active-event counts z_v=sum_{t:active_t=v}s_t, the six-axis Cell difference equals sum_v z_v H_v and has coordinate y_{uv}=z_u+z_v. This incidence map Z^4 -> Z^6 is injective: y01=y02=y12=0 implies z0=z1=z2=0, and y03=0 then implies z3=0. Thus complete Cell return is equivalent to z_v=0 for each vertex, requiring every active vertex to occur equally often with positive and negative signs. In particular m must be even. Theorem GY1 requires m divisible by three for Port return. Therefore 6 divides m. Conversely, for every m divisible by six, choose one of the two initial Port endpoints as active in *all* events; its Port follows a 3-cycle, and choosing exactly m/2 positive and m/2 negative signs returns the full Cell. QED.

An exact general coefficient formula preserving *all ordered source multiplicities* is available. For indeterminates z0,z1,z2,z3, define the 6-by-6 Laurent-polynomial transfer matrix

\[
 M^\chi_{e,f}(\mathbf z)=
 \sum_{\substack{v\in e\\\{v,T_\chi(v,e\setminus\{v\})\}=f}}
 (z_v+z_v^{-1}).
\]

Here the notation T_chi(v,e\setminus{v}) uses the sole partner of v in e. Then for every m>=0,

\[
 \boxed{
 Z_m=[z_0^0z_1^0z_2^0z_3^0]\,
 (M^\chi(\mathbf z)^m)_{e_0,e_0}.}
\]

Each product term identifies the ordered endpoint and signed source choice, and taking the joint constant coefficient imposes all four signed activity balances. Since the four-to-six incidence map is injective, this is exactly the complete X6 zero-displacement condition.

## Theorem GY3 — six-step exact history fiber has 88 members

For any initial named Port and either chirality, Z_6=88. In contrast, fixing the active endpoint in all six events, as in GX3, gives 20 paths for a *given* active endpoint.

**Proof/certificate.** There are 2^(6-1)=32 endpoint-choice words that return the named Port at length six. Exactly two have the sole active vertex repeated six times, contributing 2*binom(6,3)=40 signed histories. Exactly six have three distinct active vertices each appearing twice, contributing 6*2^3=48 histories. Every other Port-return endpoint word has an odd active-vertex count and cannot yield zero signed Cell displacement. Thus Z_6=40+48=88. The six mixed balanced endpoint sequences for initial e0=01 and chi=+1, using digits for active vertices, are

\[
003311,\quad 021021,\quad 022330,\quad
112200,\quad130130,\quad133221.
\]

The checker enumerates the 32 Port-return endpoint words independently of the full signed recurrence and verifies this partition. QED.

At length twelve an exact dynamic program gives Z_12=61160. The six-step result means 88/4^6=11/512 of the equal-weight positive BRC histories return to the joint Cell/Port observer. At length twelve the corresponding probability is 61160/4^12.

## Observer fidelity and noncollapse witness

The quotient to j(e) is exact for future matching-phase observations with fixed chi, because j updates deterministically. It is **not** an exact quotient for the full X6 signed Cell or for named Port-gated operations.

For example, e=01 and e'=23 have the same phase j=0, but the possible next signed X6 increments from e are ±H0,±H1, whereas those from e' are ±H2,±H3. These sets are disjoint because the four H_v are distinct. The phase quotient therefore loses a one-step full-Cell observer distinction. Similarly, for fixed e=01 but different chi, the next matching phase is M1 versus M2; erasing chi is not safe even for future phase observations.

Keep the signed Cell, actual named Port/Link, chirality and ordered BRC witness when the future observer requires them. The valid three-phase compression is a *scope-typed observation result*, not a claim that the full physical or research state only has three states.

## Reproducible verification and evidence

R762GY_CHECK.js runs using an ordinary JavaScript/Node runtime with no dependencies. It checks 24 exact phase cases, all 1152 S4-covariant signed six-axis transition cases, both chiralities and the complete integer BRC state recursion at lengths 0 through 12, as well as the independent six-endpoint-word certificate. The author-side checker returned PASS, with Z_6=88, Z_12=61160 and Port-return totals P_3=32, P_6=2048, P_9=131072, P_12=8388608. All counts are exact integers below 2^53 over the verified range. The all-length assertions follow from the proofs, not from extrapolation of that finite run.

The companion R762GY_EVIDENCE.json provides exact counts by event length, the phase/covariance coverage, model assumptions, original scientific pins and review status. Independent review remains NOT_REVIEWED.

## Boundary and next research

These results hold for a **specified signed K4-STAR endpoint-choice candidate extension**. The frozen P000 establishes six native spatial axes, pairwise PERP_E and the triadic stable-force arity; it does not itself prescribe this exact endpoint-selection probability or composite Cell/Link transport. Native TRIADIC_CLOSURE_E legality, interleaved primitive timing and independent physical heartbeat calibration remain separate mathematical/physical questions.

Next: test whether the actual native event permission predicate admits all four candidate branches, whether existing Link/rotation records already carry chirality, and which of the matching-phase/Cell-fiber laws survive a restricted legal-language automaton. If native gates exclude some branches, derive the permitted graph and BRC constant-coefficient return count with full named source histories, preserving the counterexample to unsafe phase-only compression.

## Custody and control

Authorship/provenance continues the historical EM-X6-3050F6 line; the original public session is MCP-4b2d70a97f594366a7c94a0f8b45df38. A read-only native continuation at 2026-11-20T08:21:34Z recorded no current execution authorization. The earlier original continuation-preparation request emr3-20261120-1540-r762gx-own-cont-prepare-v1 ended FAILED with the exact error "CANONICAL_REJECTED: execution_branch_base must be a 40-hex commit SHA"; it was not replayed. GitHub scientific file publication and readback are portable Source custody, not a native PROGRESS, Result or independent review. Do not turn this note into a new claimant or a global foundation axiom.
