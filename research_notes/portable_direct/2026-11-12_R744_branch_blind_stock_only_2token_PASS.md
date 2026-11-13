# R744 — Branch-blind stock-only PASS compensation for rooted BRC triads

Date: 2026-11-12, Asia/Shanghai. Author-side exact conditional construction; independent mathematical review pending.

Parent: RS-X6-TRIADIC-CLOSURE-DYNAMICS / TP2-8B7E13C5904A2D6F1142.
Frozen scientific P000: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
Dependencies: R739@d0d37ca56ef32c5772cd7566c0826ff060d45f25, R741@e3b3e7ec3685ac97f0e3a923c75abc3ad61e49c6, R743@85b01f8ed38672488645601454a4559473189a89 and V29@30fb16d39465708fd1b54c70a58d06ad20f310f8. Each research claim has the precise declared-model scope, not native admission.

## Question

R743 needs the immediately selected next arc to choose one early helper. Can a two-stock, four-PASS generator instead be scheduled **without knowing the next branch**, from a current intermediate triad and observable port inventory alone?

Fix the three rooted three-arc BRC loops for each carrier:

| Carrier | I | P | Q |
|---|---|---|---|
| A | 012→014→013→012 | 012→023→013→012 | 012→023→123→012 |
| B | 012→123→124→012 | 012→023→013→012 | 012→123→013→012 |

The named V17 holonomies of I,P,Q are those proved at R739/R741: I is identity, P and Q are different transpositions, and their products generate S3. They use seven distinct directed arcs per carrier. As in R741, every arc emits one real **offdiagonal V29 PASS count** and is source-decodable; the two local ports are not two X6 spatial axes.

For the *conditional stock-refinement* retain b=(b0,b1), b0+b1=2, 0≤b0,b1≤2. The optional tagged helper event is holonomy identity and preserves active triad, all three nonzero attached force sources, their TRIADIC_CLOSURE_E incidence certificate and V17 slots. F=PASS(C;0→1) changes b by (-1,+1); R=PASS(C;1→0) changes b by (+1,-1). This stock movement and the triad coupling are **declared candidate event semantics**; original V29 PASS only increments a nonnegative counter M.

## Theorem 1: zero future-branch lookahead is sufficient

Use the following source-injective codebooks:

| A directed arc | PASS | B directed arc | PASS |
|---|---|---|---|
| 012→014 | R | 012→123 | F |
| 012→023 | F | 012→023 | R |
| 014→013 | F | 123→124 | F |
| 023→013 | F | 123→013 | R |
| 023→123 | R | 023→013 | R |
| 013→012 | R | 013→012 | F |
| 123→012 | F | 124→012 | R |

**Scheduler:** immediately after the first arc leaving root 012, issue exactly one helper PASS inverse to that *observed first pulse*. This operation occurs before selecting the second arc. It restores b=(1,1) and depends only on current stock (0,2) or (2,0). On the given subgraph, the first-hop triad itself is an equivalent static guard: for A, at 014 emit F, at 023 emit R; for B, at 123 emit R, at 023 emit F. There is no future-branch lookup.

| Carrier | I four PASS | P four PASS | Q four PASS |
|---|---|---|---|
| A | RFFR | FRFR | FRRF |
| B | FRFR | RFRF | FRRF |

Every word has two F and two R. The intermediate stocks are:

- RFFR: (1,1)→(2,0)→(1,1)→(0,2)→(1,1)
- FRFR: (1,1)→(0,2)→(1,1)→(0,2)→(1,1)
- FRRF: (1,1)→(0,2)→(1,1)→(2,0)→(1,1)
- RFRF: (1,1)→(2,0)→(1,1)→(2,0)→(1,1)

The second and third **arc** pulses are opposite, after the helper has cancelled the first. Hence every generator is capacity-legal and resets the stock. Root-incoming predecessor vertices {013,123} (A) / {124,013} (B) are disjoint from the root-outgoing first-hop vertices {014,023} (A) / {123,023} (B). Thus arbitrary generator concatenations remain nonbacktracking.

For every integer k≥0 and word w∈{I,P,Q}^k, exact induction gives 4k PASS events and

\[
M(w)=\begin{pmatrix}0&2k\\2k&0\end{pmatrix},\quad
R_{\rm in}=R_{\rm out}=0,\quad
\Omega=0,\quad u=0,\quad \Gamma=4k,\quad b=(1,1).
\]

The helper preserves the BRC holonomy and all ordered transition provenance. At k=3, six words III,IIP,IIQ,IPQ,IQP,PQP have this same M=[[0,6],[6,0]] and b=(1,1), yet the named relations are respectively:

- Carrier A: 012,021,102,201,120,210;
- Carrier B: 012,021,210,120,201,102.

Consequently the terminal count-stock observer has a six-state relation fiber. A six-value S3 register is sufficient and sharp for recovery on this fiber. The R743 lower bounds of two stock units and four PASS per generator remain attained, now with **no next-edge lookahead**.

## Theorem 2: exactly four branch-blind first-hop codebooks per carrier

In the stated seven-arc grammar, require (i) one binary offdiagonal PASS label per arc, (ii) outgoing labels source-injective, (iii) a single inverse-of-first PASS helper immediately after arc one, (iv) stock restoration to (1,1) after every generator. There are exactly **four** satisfying arc codebooks out of **32** locally source-injective binary codebooks.

Proof. Each carrier has exactly two branching source vertices of outdegree two; each has exactly two choices of its F/R assignment. Its other three source vertices have outdegree one and arbitrary labels: there are 2²·2³=32 source-injective codebooks.

After the first arc and its inverse helper, stock equals (1,1). The two remaining arc pulses must be opposite: if they agree, one source stock is depleted; if opposite, the stock returns (1,1) with each prefix valid. In each carrier two loops share the same final arc 013→012, forcing the labels of their preceding arcs to be equal, which uniquely determines that shared final label. The third loop's final arc is then determined by its second arc. Thus for each of the 2² branching assignments the three nonbranching arc labels are uniquely fixed. Every resulting assignment obeys the same opposite-pair rule and works. QED.

The four assignments for each carrier are listed exhaustively in the companion JSON. Source-level symmetry under F↔R and the two independent branching assignments accounts for the fourfold codebook family. The classification is for the three-generator seven-arc carrier; coding the entire fifteen-arc network is a different interface (R741).

## Typed X6 interface, symmetry and next question

For σ∈S6 of the declared native-axis-permutation skeleton, transport the signed-axis force-source labels, five candidate closure certificates, active triad/frame, current source and arc codebook. Keep local port F/R labels fixed. The inverse-first helper is stock-defined and commutes with this transported action; the *conditional decorated scheduler* is therefore S6-covariant. The sixth spatial axis remains in the X6 ambient space; local ports are not a two-dimensional native plane.

The actual V29 source grammar defines PASS as M[a,b] += 1; it does not by itself grant a physical token-transfer law, nontrivial triad transition, or identity-holonomy helper event. The exact next native test is now small: after a certified first-hop arc, can a permitted X6 Cell/Link/Port rule emit the reverse helper while keeping TRIADIC_CLOSURE_E, attached nonzero source tokens, dependency order and signed-axis provenance? A legal event refinement would realize R744; a specific denied event guard would identify the missing interface. No P000 change is proposed.

## Exact reproducibility and status

The accompanying standalone Python checker enumerates all 2^7=128 binary codebooks per carrier, certifies 32 source-injective and exactly four branch-blind stock-return codebooks, and exhaustively executes all 1+3+...+3^8=9,841 generator histories for each of the eight valid codebooks (**78,728 histories total**). Each simulation checks every stock prefix, the final cumulative matrix and S3 relation; six twelve-PASS witness relations are separately checked. All arithmetic is exact integers. The associated JSON was generated by actual local Python execution with result PASS. The all-k construction follows the induction proof, not the finite test alone.

**Review:** author-side proof and code completed; independent Source scientific review and native event permission still open. **Next:** native guarded-PASS-plus-closure interface certificate, or an exact failing guard/counterexample.
