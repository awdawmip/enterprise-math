# R284DR — 八骨架与带标签事件包络的零逐弧调用最小间隔见证构造

Date: 2026-11-22 (Asia/Shanghai)  
Status: **AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED**  
Scope: frozen 34-bit Port auxiliary finite observer. This statement concerns the explicitly pinned integer source and its defined readout, not native X6 dynamics or a BRC theorem.

## Frozen source and exact inherited facts

The input is `awdawmip/enterprise-math@acba2d8667903434aaa2a10720f43637fcc2421b:research_notes/portable_direct/R284CO_spectral_witness_checker.py`, Git blob `b46e0f682b58e47c27094b4bea6fa4e55119a3ee`; 65,536 source residues have ordered SHA-256 `b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4`. The circle modulus is P=17,179,869,143, with 64 original labeled oriented integer circular arcs.

For source index i, let f(i) be the maximum exact circular distance from its residue g(i) to the 64 arcs. Set

`U(i)=(f(i), f(i xor 1), f(i xor 64), f(i xor 65))`.

The following already-established results are consumed with their original mathematical scope:

- **R284DN**: on all 65,536 source states, the minimum pairwise Chebyshev distance among U values is exactly 60; precisely 256 unordered source-state pairs attain it, with SHA-256 pair digest `7c05864095ba5cde368002e67764bc772ca1bfe3fabbcf26af4fb090b7d0996a`.
- **R284DO**: toggling the fourth upper bit, index XOR 4096, changes the corresponding residue by `-q3` modulo P, with `q3=(ts-xw)u3+(su1+xu2)g+(tu2+wu1)h`, `t=6-a`, `s=13-b`.
- **R284DQ**: for canonical lower indices `ell & 65=0`, the condition `max(q3(ell),q3(ell xor 64))<=60` is equivalent to `a=b=2; u1=u2=u3=g=h=1`, leaving exactly the three free variables x,y,z. Thus the lower skeleton indices are exactly `ell=1056+512X+256Y+16Z` for X,Y,Z in {0,1}.
- **R284DD**: for a finite labeled family of integer circular arcs, a labeled two-slope event envelope computes the exact farthest distance **and the complete set of winning arc labels** via event-predecessor lookup, without evaluating each site against all arcs.

## Theorem — direct attributed-envelope construction of all sharp witnesses

Build the exact original 64 arcs once and the R284DD fully labeled event envelope. For the frozen arcs the envelope has **194 event positions and 193 event slabs**. Generate the eight Boolean lower skeletons from R284DQ. For each of the eight lower skeletons choose eight even upper lexicographic indices `h in {0,2,4,6,8,10,12,14}`, giving 64 upper/lower group representatives. For each representative and `v in G={0,1,64,65}`, set

`i=((h << 12) | ell) xor v`, `j=i xor 4096`, `d=q3(i & 4095)`.

Compute the first residue `x=g(i)` with the pinned determinant, and compute the second **without another determinant** as `y=(x-d) mod P`. Query the labeled event envelope once at x and once at y to obtain the two scalar farthest distances and their full winning-label sets. No direct point-to-arc distance call is needed in this construction.

**Exact finite conclusion.** All 256 constructed unordered pairs are different and satisfy

`|f(i xor v')-f(j xor v')| in {59,60}` for every `v' in G`, with at least one difference 60. Their four-read Chebyshev distance is therefore exactly 60. Each endpoint has the same single winning arc label as its paired endpoint under the corresponding translation. Since R284DN already proves that **the entire 65,536-state population contains precisely 256 pairs at distance 60**, this construction generates *every* minimum-distance pair.

The resulting list, in ascending order of both 16-bit endpoint indices with each pair serialized as two unsigned two-byte big-endian integers, has SHA-256

`7c05864095ba5cde368002e67764bc772ca1bfe3fabbcf26af4fb090b7d0996a`.

Among the 64 canonical orbit representatives the gap patterns are `(60,60,60,60)`: 32 and `(60,60,59,59)`: 32. Across 256 pair comparisons the unique winning arc-label histogram is `21:45, 32:21, 44:37, 45:19, 55:64, 56:43, 63:27`, consistent with the earlier complete witness classification.

**Argument.** R284DQ identifies all lower candidates as a symbolic eight-element Boolean family. The upper fourth-bit identity from R284DO yields the partner residue exactly; G-shifts preserve the pair relation. The R284DD envelope theorem establishes that its two value/label queries are identical to evaluating the full set of circular distances, including tied labels. The R284DR checker performs these two queries for each candidate pair, checks the exact observed scalar gap, the unique common winner, and the maximum across all four shifted coordinates. It checks pair distinctness, the exact pattern counts and the reference 256-pair digest. R284DN's independent full-universe minimum and exact count then establish global completeness. QED.

## Reproducible computation and cost

Project checker: `research_notes/portable_direct/R284DR_boolean_event_envelope_checker.py`, importing the original R284DP/R284DM determinant helper and original R284DD event-envelope helper from the same directory. Certificate: `R284DR_boolean_event_envelope_certificate.json`.

The author-controlled local execution confirmed all assertions; a separate local direct-distance validation on the same **512 generated candidate sites** checked all 64 arcs for each site (32,768 direct checks) and agreed with the event-envelope value and winning arc label. This validation cost is separate from construction. The published GitHub source was read back in full, not executed separately in remote CI. The R284DN global finite search is reused, not recomputed.

| Operation | R284DR construction | R284DP construction | R284DN global scan |
|---|---:|---:|---:|
| Source determinant calculations for candidate residues | 256 base + 256 partners via exact modular increment | 512 full residues | 65,536 residues |
| Direct point-to-arc distance evaluations | **0** | 32,768 | 4,194,304 |
| Exact envelope predecessor lookups | **512** | 0 | 0 |
| Constructed minimum-distance pairs | 256 | 256 | 256 |

The event envelope has separate upfront construction costs: forming the original 64 arc parameters requires the pinned determinant operations, and the supplied simple reference sweeps active candidate branches at each of 193 slabs (O(m²) preprocessing in m arcs). In a local instrumented run the preprocessing visited **24,114 active branch keys**. Each of the 512 attributed-envelope queries uses a predecessor search over 194 events plus a constant-size two-slope evaluation. The operation counts describe this exact algorithm and source; they are not wall-clock benchmark measurements. This is a structural elimination of 64-way per-site distance scans for the selected pair-witness generation problem, with explicit preprocessing trade-offs.

The complete source space, observations, pair count and universal δ=60 continue to rely on the pinned earlier exact full-universe theorem. The new computational certificate is a complete check of the 256 construction pairs, not a re-execution of the earlier 65,536-state universe. Independent mathematical review is **NOT_REVIEWED**.

## Future questions

1. Derive a direct symbolic event-slab prediction from the eight Boolean skeletons and upper bits, avoiding even the 512 binary event lookups in this frozen family; compare the real encoding and initialization cost.
2. Replace the reference O(m²) envelope preprocessing with a balanced active-branch sweep O(m log m) while retaining complete tie-label provenance, and measure the break-even point against direct 64-arc evaluation.
3. Investigate which families of other circle-arc inputs share the same algebraic lower-skeleton reduction without assuming transfer of this special finite instance.

## Control and attribution

This is independent portable TASK research, preserving the real frozen science and prior author provenance. Current gateway status did not establish Researcher execution authority. A read-only current owner request `r1-20261122-0201-owner-leased-scope-v1` terminated `FAILED / SOURCE_TREE_TRUNCATED`, so no current live-LEASED inventory was verified. This round did not acquire a shared CLAIM, write native PROGRESS, create Result/Review, impersonate historical researcher `EM-DIRECT-20B766`, or rebind historical Activity `RA-617F40704F37299B15489DCA`. The new Activity association awaits a legitimately authenticated original-session/CAS source write.