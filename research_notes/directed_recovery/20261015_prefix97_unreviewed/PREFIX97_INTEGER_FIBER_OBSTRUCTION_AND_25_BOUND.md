# PREFIX-97 — integer score-fiber obstruction (UNREVIEWED / NOT_ADMITTED)

Research note, 2026-10-15. Auxiliary **positive unit-weight 0/1 edge-labeled BRC** with two roots; this is **not** a P000-native X6 dynamics claim, formal Result, Research Activity, CLAIM, Driver review, or mathematical admission.

## Frozen task instance

For each root r=s,t, integer path-score multiplicity histograms are F(0)=1, F(1)=2, F(2)=4, F(3)=4+4z, F(4)=8+8z², F(5)=3+13z+16z³, F(6)=1+6z+25z²+32z⁴. At all n≥7, F_s(n)=1+55z²+64z⁵, F_t(n)=14z+50z³+56z⁴. Each reachable hidden vertex has 1 or 2 outgoing edge occurrences of unit positive multiplicity, labeled 0 or 1; all path counts retain branching multiplicity and provenance.

## New unconditional within-instance local obstruction

**Every root at depth 4 reaches ≥3 distinct score-zero hidden states, and ≥4 hidden states in total.**

Proof: eight score-zero path occurrences at depth 4, each at a two-outdegree state, create exactly three score-zero occurrences at depth 5. If only one endpoint state, 8*d0=3 is impossible. If there are two states of multiplicities a,b≥1, a+b=8, and zero-edge outdegrees c,d∈{0,1,2}, solve a*c+b*d=3: only (a,b;c,d)=(3,5;1,0), up to swapping. All three depth-5 score-zero paths then end at the *same* state (the single zero edge from the multiplicity-three vertex). Any score-zero depth-6 contribution is a multiple of three, contradicting the target coefficient 1. Also depth-4 score-zero and score-two paths cannot share a state: from score-two the forced three-bit suffix through depth 7 is 111 for root s and 110 for root t; the same suffix starting from score-zero yields respectively 3 or 2 at depth 7, both outside the respective prescribed support. Since score-two paths are present, total depth-four states ≥4. Zero-edge flow from score-zero depth four is odd 3, forcing a mixed 0/1 state; 3<8 forces a distinct pure-one state.

## Divisibility, early-state and total-resource bound

Let m_r(n,u,k) count length-n paths from root r reaching hidden vertex u with integer cumulative label k. The transition update is a nonnegative integer sum over actual edges. Therefore any common divisor of all positive m_r(n,u,k) divides all subsequent integer multiplicities. As F_r(5) has coefficient 3, root r cannot have merged both length-one paths into one state or all four length-two paths into one state. At depth 3 score-zero mass 4 must have at least two **odd-visitation** states (otherwise its descendants' score-zero coefficient at depth 5 is even); score-one states at depth 3 are separate because score-zero states have both edges labeled 0 and score-one states have both edges labeled 1. Thus each root needs at least 1+2+2+3=8 state slots over depths 0..3. Using previously derived **unreviewed** PREFIX-94/96 sharing-rigidity lemmas (no cross-root same-depth sharing through depth 3, no inter-depth reuse before the 3→4 boundary), the union at depths 0..3 has size at least 16.

A further **conditional** chained lower bound is **N≥25 reachable states**, using the preceding local argument and the unreviewed PREFIX-93–96 structural lemmas:
- Put a=number of root-s depth-3 score-zero states (≥2), b=number of root-t depth-3 score-one states (≥1); early union ≥16+(a−2)+(b−1).
- Let S and T be respectively root-s and root-t depth-4 score-zero state sets (≥3 each). They are disjoint by the exact root-to-root suffix-support table. Across depth 3→4, an earlier E state in S must be root-s depth-3 score-zero; an earlier E state in T must be root-t depth-3 score-one. Earlier depths 0..2 cannot be reused. For S, required mixed/pure-one vertices are new, yielding (a−2)+|S\\E|≥3 if a≥3. If a=2, the visitation multiplicities are {1,3}. The PREFIX-94 unary-capacity 8*m(3,u)≤8 excludes reuse of the 3-visited state, and 2*m(4,u)≤3 constrains reuse of the 1-visited state to one incoming path. That would require its 0-self-loop (no other predecessor has multiplicity 1), contradicting unary-only states by depth 7; thus S wholly new, still cost≥3.
- For T, only b earlier root-t score-one states could be reused, and their depth-three multiplicities would each need to be 1 by the same PREFIX-94 capacity. Their total path mass is four. At most b−1 such states are singleton if b≤3, hence (b−1)+|T\\E|≥3; if b≥4 the left term b−1 already ≥3. Therefore union through depth 4 ≥16+3+3=22.
- At root-s depth 5, score-one mass 13 has **exactly one** zero-edge continuation, because root-s score-zero depth-five mass 3 emits one zero and five ones, while F_s(6) has score-one coefficient 6. At least two distinct score-one depth-five states are needed. Exact PREFIX-96 shifted suffix support excludes these from all depth-four states, and PREFIX-94 excludes depths 0..3. Hence union through depth five≥24.
- Total paths time six=64 and time seven=120, so exactly eight unary **path occurrences** at depth six; every state appearing at earlier depths 0..5 is binary. Thus a fresh unary state makes total N≥25.

The 25 bound is a proof **dependent on P93–P96 premises not independently accepted** and is NOT a certified 33-state UNSAT. The local depth-4 bound does **not** depend on those prior lemmas.

## Exact local verification

Local Python standard-library replay (not performed on this server): independent zero-flow pair enumeration and shifted suffix-support word check; exact integer forward paths for lengths 0..12 on two previous 34-state witnesses: PREFIX-80 34 states/67 edges, cumulative union depth 0..3/4/5/6 = 18/25/32/34; PREFIX-86 34 states/66 edges, corresponding 18/25/31/34. Both pass checks; original witnesses and full exact script/certificate are retained in the attached conversation ZIP `em_research6_prefix97_20261015_local_handoff.zip`. Remote Source does not yet contain or independently verify the script.

Frozen source pins: GLOBAL_KNOWLEDGE_V1 main `654a4f1ad3ccf435132b5a9e6b4a9f8f528206b8`, original P000 blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`; Enterprise Math main `1c2913ac2c3b0412b3aedca30dfa9cf16ac8bee7`. All P000/native X6/observer-preservation obligations preserved.

## Next PREFIX-98

Strengthen exact integer score-fiber & crossroot state-budget cuts, or construct a sound integer-flow SAT encoding that accepts both known 34-state witnesses before searching 33-state UNSAT with an independently checkable proof. Publish the scientific evidence via the current role-authorized Task/Source protocol and arrange genuinely independent adversarial review. Native interface currently rejects this client's session start: `STATIC_READONLY_SCOPE_DENIED`, `operation_sent=false`; hence this note is **branch-only unreviewed evidence**, not a canonical result or Owner/CLAIM evidence.
