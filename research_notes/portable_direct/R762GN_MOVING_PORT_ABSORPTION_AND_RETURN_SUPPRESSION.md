# R762GN — Absorbing named-Port orientation class and exponential return suppression

Date: 2026-11-20 (Asia/Shanghai). Task: \`RS-X6-TRIADIC-CLOSURE-DYNAMICS\`; frozen publication \`TP2-8B7E13C5904A2D6F1142\`; frozen P000 \`a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json\`. Immediate scientific predecessor: R762GM, \`961479945c690fd07277ce30fba01c1f8edbe552:research_notes/portable_direct/R762GM_MOVING_PORT_DEPTH_HOLONOMY.md\`. Historical contributor lineage: \`EM-X6-3050F6\`; this portable note asserts no current CLAIM or original private session capability.

Status: author-proved structural lemma plus complete finite exact orientation-graph certificate; author-side Python 3 standard-library verification **PASS**; independent review **NOT_REVIEWED**. This is the previously declared candidate signed STAR semidirect model, not the frozen native \`TRIADIC_CLOSURE_E\` permit rule.

## Exact model and question

Let tetrahedral vertices be \`V={0,1,2,3}\`, with six *native* signed spatial coordinates indexed by edge labels \`E=(01,02,03,12,13,23)\`. For each vertex v, \`H_v\` is the 0/1 incidence vector of its three incident edges and \`g_v\` cyclically permutes those three labels, fixing the remaining three. Candidate signed event \`T(v,s)=(sH_v,g_v^s)\`, where \`s=±1\`, acts by right multiplication in \`Z^6 ⋊ A6\`:

\`(x,p) -> (x+s p·H_v, p g_v^s)\`.

Initially \`(x,p)=(0,id)\`, and the registered initial Port is \`e0=01\`. At each step the visible named Port is \`e=p(01)\` and **only** v in the two endpoints of this current edge is permitted, with both signs. The observer is a full affine return to \`(kD,id)\`, \`D=(1,1,1,1,1,1)\`. The typed positive BRC counts ordered admitted signed words; future source-aware observers retain each vertex/sign/Port history.

**Question.** Does the moving Port allow all orientation states to return, and how does this constrain the depth-return distribution?

## Theorem A — An absorbing class in the orientation register

Write \`O={p in A6 : p(01)=23}\`.

1. \`|O|=60\`. For every \`p in O\` and every permitted signed next event, the updated orientation remains in \`O\`: \`p g_v^s(01)=23\`.
2. For the full finite 360-element orientation graph, shortest admissible distances to \`O\` have the exact histogram \`{0:60, 1:144, 2:144, 3:12}\`. Thus **every** A6 orientation has an admissible path into \`O\` of length at most 3.
3. From \`id\`, exactly 350 orientation permutations are reachable: 290 outside \`O\`, 60 inside; 10 others are unreachable. The reachable graph has exactly two strongly connected components, of sizes 290 and 60. The 60-state component \`O\` is closed; the 290-state component has edges into \`O\` and no path back.
4. Once a word enters \`O\`, it can never satisfy a later complete affine return \`(kD,id)\` for *any* integer k.

**Proof of structural parts.** If \`p(01)=23\`, the only permitted vertices are 2,3. Both \`g_2\` and \`g_3\` fix the edge-label 01 because their three-cycles act only on incident edges at vertices 2 and 3. Consequently \`p g_v^s(01)=p(01)=23\`. There are \`|A6|/6=360/6=60\` even permutations with a specified image for 01 (the action is transitive). Since the identity sends 01 to 01, it does not belong to \`O\`, proving point 4 by forward invariance.

**Complete finite certificate for parts 2–3.** The attached \`R762GN_VERIFY.py\` enumerates **all 720 permutations**, filters exactly the 360 even ones, builds **all 1,440 signed permitted orientation transitions**, performs forward and reverse breadth-first reachability, verifies both SCCs by bilateral reachability, and performs multi-source reverse BFS from all 60 members of \`O\`. The complete finite assertion yields \`360=60+144+144+12\`, \`350=290+60\`. These graph facts are finite exhaustive results at the *orientation* level, independent of path-length truncation.

## Theorem B — All-horizon exponential suppression

At each state choose uniformly among its four admitted signed letters, and let \`τ\` denote the first time that \`P_τ\` belongs to \`O\`. Then for every integer \`m>=0\`,

\[
\Pr(\tau>m)\le \left(\frac{63}{64}\right)^{\lfloor m/3\rfloor},
\quad
\Pr\big((X_m,P_m)=(kD,\mathrm{id})\big)
\le \left(\frac{63}{64}\right)^{\lfloor m/3\rfloor}
\quad (\forall k\in\mathbb Z).
\]

In particular \`Pr(τ<∞)=1\`, and the upper bound on any full affine return decays exponentially with the event count.

**Proof.** The exhaustive graph certificate gives from *every* nonabsorbed orientation an admissible path into \`O\` of length at most 3. A particular path of length d≤3 has conditional probability \`4^{-d}≥4^{-3}=1/64\`; once reached, the class remains absorbing. Hence, conditional on any nonabsorbed past, probability of remaining outside \`O\` for the next 3 events is at most \`63/64\`. Iterate this bound on disjoint three-event blocks. A full affine return requires \`P_m=id\`, which cannot occur after absorption by Theorem A. Taking m→∞ proves almost-sure eventual absorption. No independence of successive blocks is assumed.

This is a property of the **positive, history-counting BRC Markov observer** on the stated candidate dynamics. It does not assert signed quantum cancellation, a physics equilibrium, or an unbounded exact closed-form count.

## Exact survival BRC (orientation-only projection with certified terminal scope)

Define \`S_m\` as the number of length-m admitted signed histories, from \`(0,id)\`, that have **never** entered \`O\`. Each step has four branches, hence the denominator is \`4^m\`. The checker uses the exact integer recurrence \`N_{m+1}(q)=sum_{p outside O, p->q, q outside O} N_m(p)\`. Its tested values include:

| m | all signed histories \`4^m\` | never absorbed \`S_m\` | already absorbed |
|---:|---:|---:|---:|
| 0 | 1 | 1 | 0 |
| 3 | 64 | 60 | 4 |
| 6 | 4,096 | 2,900 | 1,196 |
| 9 | 262,144 | 137,728 | 124,416 |
| 12 | 16,777,216 | 6,534,252 | 10,242,964 |
| 16 | 4,294,967,296 | 1,118,196,052 | 3,176,771,244 |

At m=12, the R762GM previous full affine return paths to nonzero depths \`±6\` (8 paths each) belong necessarily to this nonabsorbed part. Orientation survival by itself cannot recover their Cell endpoints; \`x\` and named-source histories remain necessary for the full observer.

## Relevance, verification scope and next question

**New distinction.** The Port being *transported* permits nonzero Cell-depth loops, as in R762GM, but its own orientational dynamics contains a one-way loss of eventual return capability. Thus a moving Port is not synonymous with reversible Port kinetics. The absorbing orientation residue is a structural future-operation distinction, not a zero or negligible numerical error.

**Verification.** Python 3 standard library; exact 360-orientation graph, all transitions, two SCCs, all shortest hitting distances, survival recurrence through m=16, all listed integer assertions. All-horizon probability bound follows mathematically from the finite graph lemma. No independent mathematical reviewer has certified the result.

**Remaining work.** (i) Classify minimum signed-word length for full affine unit-depth return \`(±D,id)\` in this candidate, or prove an additional lattice obstruction; the bound above does not settle it. (ii) Determine how the real frozen native \`TRIADIC_CLOSURE_E\` Cell/Link/Port permission and time evolution transport the Port. (iii) Test whether retaining \`(x,p,e0)\` is sufficient for specific named Link/Port history-dependent future operations. Do not modify P000 or mark this candidate as native law.

Evidence files: \`R762GN_VERIFY.py\` and \`R762GN_EVIDENCE.json\` in this directory; source BRC carrier: exact typed signed-word multiplicity.