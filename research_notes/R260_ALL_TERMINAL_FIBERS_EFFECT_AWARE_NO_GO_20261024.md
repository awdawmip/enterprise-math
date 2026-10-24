# R260 — All-terminal source-mode saturation and an effect-aware deterministic lower bound

2026-10-24 | **AUTHOR-SIDE EXACT DRAFT, UNREVIEWED, NOT ADMITTED**. This is a formal six-axis positive BRC affine model, not a proved native P000 heartbeat law, accepted task Result, or independent review.

## Frozen sources, identity, and exact boundary

GLOBAL_KNOWLEDGE_V1 verified canonical main: 7b7bd052c42ed6aaa5641eea28b30435ed63c024 (bootstrap/manual, P000 original, P000 startup, ACTIVE worldview and domain policies read). P000 original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc agrees with the startup projection and is ACTIVE_LOCKED. Enterprise Math pinned main: 4f7169291a872467496de179666f456e67869749; inspected docs/PORTABLE_RESEARCH_PROTOCOL.md, src/enterprise_math/brc_transport.py and brc_control_port.py. Exact predecessor: R259 at immutable 2dbe9ba76cc1b431a0a75d3f5ba50930e92c76b5, research_notes/R259_UNIFORM_THREE_WAY_AFFINE_PROVENANCE_FIBERS_20261024.md. The q=2 base certificates and reset identities come from R259; they are not rediscovered here.

Current native em_session_start was denied STATIC_READONLY_SCOPE_DENIED (operation_sent=false); em_control_tasks returned CONTROL_QUOTA. Active owner and official CLAIM could not be checked. GitHub activity RA-EMR4-20261024-2037-R260ALLQ is owner-visible bookkeeping only; its Researcher-ID is local and not an authenticated native session, claim, or reviewer identity.

## 1. Model and observation

Nonspatial control q∈{0,1,2}; raw selector a∈{0,1}. Each outgoing branch has positive weight 1 and multiplicity 1. The edge triple (next q, eta, b) is:

| q | a=0 | a=1 |
|---|---|---|
| 0 | (2,-1,-1) | (2,+1,-1) |
| 1 | (0,-1,-1) | (0,+1,-1) |
| 2 | (1,+1,+1) | (2,+1,-1) |

The formal affine effect is F_(eps,k)(z)=diag(eps,eps,1,1,1,1)z+k e_1 on six coordinate slots, with chronological composition
\[
(\epsilon,k)\operatorname{then}(\eta,b)=(\eta\epsilon,\eta k+b).
\]
This keeps all six slots; selector, control q and monitor r are **not** extra spatial axes. It is only formal affine algebra, not an externally verified 120-degree triadic/primitive native update, a complete three-dimensional slice, a calibrated heartbeat step, or a final Cell address.

The DFA monitoring whether a raw source word contains 00 has states r=0 (not seen, last not 0), r=1 (not seen, last 0), r=2 (seen, absorbing). The transitions on selectors (0,1) are (1,0), (2,0), (2,2) respectively. Immediate query g(r)=1 iff r=2.

All words start from (q,r,eps,k)=(0,0,+1,0). At word-length m the *unmarked complete-effect* observer is O_m=(m,terminal q,weight 1,complete six-axis affine effect); it omits raw word and monitor mode. Full future query preservation asks for g at present and after all subsequent positive BRC packets, resolving final q and query mode/count.

The exact reachable joint control-mode set is
\[
S=\{(0,0),(0,2),(1,1),(1,2),(2,0),(2,1),(2,2)\}.
\]
It contains the initial pair, is closed under both selectors, and all its members have witnesses below. Therefore modes reachable with each terminal q are R_0={0,2}, R_1={1,2}, R_2={0,1,2}.

## 2. New exact base identities at every terminal q

Each table row consists of distinct raw words with the same terminal q, length, positive weight and complete affine (eps,k), yet exactly the indicated r modes.

| q | m | common (eps,k) | r=0 | r=1 | r=2 |
|---|---:|---|---|---|---|
| 0 | 6 | (+1,-2) | 101101 | — | 000000 |
| 0 | 7 | (-1,-3) | 0101101 | — | 0011101 |
| 0 | 8 | (-1,-4) | 01011101 | — | 00111101 |
| 1 | 5 | (+1,-1) | — | 10110 | 00010 |
| 1 | 6 | (-1,-2) | — | 010110 | 001110 |
| 1 | 7 | (-1,-3) | — | 0101110 | 0011110 |
| 2 | 7 | (-1,+1) | 1110101 | 1011010 | 0000000 |
| 2 | 8 | (-1,+2) | 11110101 | 10111010 | 00011010 |
| 2 | 9 | (-1,-1) | 101101011 | 010101010 | 000000011 |

The last three rows reuse R259; six q=0,1 rows are newly supplied. Every identity follows by literal use of the edge and DFA tables; exact Python and independently written C++17 verifiers both checked them.

## 3. Theorem: simultaneous saturation at every depth m>=7

**Theorem R260.** For each integer m>=7 and **each** terminal q∈{0,1,2}, there exists a single unmarked complete-effect fibre whose raw histories realize **every** reachable DFA mode R_q. Thus at *the same depth* there are q=0,1,2 fibres requiring respectively 2, 2 and 3 distinct provenance residual modes.

**Proof.** Define J_0={6,7,8}, J_1={5,6,7}, J_2={7,8,9}. Given m>=7 and q, each J_q contains exactly one j with m≡j (mod 3), j<=m. Put h=(m-j)/3.

The three-selector word p=101 returns joint (q,r)=(0,0) to itself and has formal affine effect (+1,-1). Hence p^h returns to (0,0) and has (+1,-h). Append **each** of the base words for q,j from §2. Those suffixes all have the same affine action (eps_j,k_j) and the same terminal q, but realize every mode in R_q. Chronological affine composition gives exactly
\[
(\epsilon_{\rm final},k_{\rm final})=(\epsilon_j,k_j-\epsilon_j h)
\]
for **every** suffix. Thus the resulting distinct raw words share all fields of O_m but have all the required monitor modes, for every q and m. QED.

**Sharp simultaneous threshold.** The first such simultaneous depth is exactly 7. For m=0..6, no q=2 complete-effect fibre has all three modes: the exact maxima of distinct r in any q=2 fibre are 0,1,1,1,2,2,2 respectively. This is a finite exhaustive certificate: altogether only 1+2+4+8+16+32+64=127 raw words exist at these depths, and exact dynamic programming agrees with explicit enumeration. The q=2 depth-7 row above achieves three.

## 4. Quantitative strengthening for all terminal controls

Two different raw seven-selector loops u=1011101, v=1101101 both return joint (q,r) to (0,0), both have affine effect (+1,-3). For fixed m,q,j as in §3 write h=7K+s, 0<=s<7. Construct a prefix from 3K independently chosen u/v blocks followed by s copies of p. The 2^(3K) distinct prefixes each have length 21K+3s, reset to (0,0), and carry the **same** affine (+1,-9K-s).

Append any of the |R_q| mode-distinguished base suffixes from §2. All |R_q|*2^(3K) raw histories then have the **same** O_m, while each mode appears at least 2^(3K) times. In particular
\[
M_{m,q}\ge |R_q|\,2^{3K},\qquad K=\left\lfloor\frac{m-j}{21}\right\rfloor.
\]
The constructed fibre alone requires at least 3K+1 extra bits to recover an individual history when q∈{0,1}, or 3K+2 bits at q=2. These are only constructive lower bounds, not maximum-fibre exact formulas or a stronger asymptotic claim than R254.

## 5. Effect-aware deterministic provenance compression cannot reduce seven q-labeled configurations

Fix a **per-history deterministic** provenance representation whose state exposes terminal q and an auxiliary tag. Its decoder may additionally read m and the *complete accumulated affine effect* F. The representation must preserve the current source query and every future two-branch BRC query **on that individual history**, resolving the original terminal q. It has no further stored hidden mixture/raw-word oracle; its state-update and decoding are deterministic.

At every depth m>=7, §3 supplies an effect fibre of fixed (m,q,F) for **each q**. The complete effect and length cannot distinguish the |R_q| histories inside that fibre. At q=0, modes 0 and 2 have different current g; at q=1, modes 1 and 2 differ currently. At q=2, mode 2 differs currently from 0 and 1. The remaining modes 0 and 1 are distinguished after one future positive packet: selector 0 reaches terminal q=1 while producing query mode 1 from r=0 and mode 2 from r=1; selector 1 reaches different terminal q=2, so target-q aggregation cannot hide the difference.

Therefore a correct effect-conditioned encoder needs at least 2 tags for q=0, 2 for q=1 and 3 for q=2. Because q remains an explicitly observed component of the state interface, at least 2+2+3=7 **reachable (q,tag) configurations** are necessary at every m>=7, despite access to accumulated complete effect. The reachable product representation S has precisely 7 and realizes the bound in this declared representation class.

**Boundary:** no seven-state lower bound for arbitrary nondeterministic/weighted linear realizations, shared provenance DAGs, signed amplitudes, or a different aggregate-observation contract is deduced. Seven q-tag configurations do **not** mean seven tag symbols globally: max tags needed at one q is 3 (two binary bits). This is a sharp lower bound for the q-retaining deterministic **per-history** monitor, not a universal memory-size theorem.

## 6. Verification and research status

Author-side Python exact code independently computes all nine base rows and reset loops; every positive-integer histogram depth 0..160 with total 2^m; exhaustive word enumeration for depths 0..13 (16,383 total raw words); all-q saturation at every computed depth m>=7; and 3,535 formula-constructed words from depths 7..511, including 24 distinct depth-28 histories in a single q=2 effect fibre.

An independent C++17 implementation (Boost multiprecision integers) verifies bases, loops, histogram totals through depth 128, exact first simultaneous saturation depth 7, 3,535 constructed words and depth-28 twenty-four-way collision. Both passed after local cold-start re-execution. The all-m statement is a proved symbolic construction, **not** extrapolation from depth 160 or 511.

BRC tool-reuse resolution: REUSE_APPLIED to the precise semantic contracts of native Affine.then, EffectHistogram.from_terms/then, ControlPacket.from_edges/then in pinned Source. Original Enterprise Math Python modules were **inspected, not imported/executed**; native conformance remains pending, not falsely reported as green. The source's EffectHistogram is a positive joint-effect histogram, **not** a complete ordered path-source record.

Native R193 actual labelled-source/query/time-port contract remains **not verified** in the documents located. No P000 native six-axis heartbeat dynamic, official owner/CLAIM, Result freeze, independent Driver review, or Foundation promotion is asserted. Formal model, source-model correspondence, implementation test, novel work and project admission are separate claims.

**R261 next:** obtain R193's real immutable observer and time-port record, prove an explicit observer-preserving map from (q,r,F) or give a minimal counterexample; then run pinned original ControlPacket/EffectHistogram modules in an authorized matching Python environment. Separately test if an **aggregate** effect-aware weighted realization may use fewer than seven q-labeled states—do not extend this per-history theorem without a fresh proof.

Global-Knowledge-Sync: main@7b7bd052 / GLOBAL_KNOWLEDGE_V1
