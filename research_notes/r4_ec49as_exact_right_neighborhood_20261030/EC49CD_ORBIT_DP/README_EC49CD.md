# EC49CD — Exact K-orbit quotient of signed-X6 BRC sparse DP

2026-10-31. Scope: author-side finite combinatorial BRC model, not native physical dynamics. Classification: **AUTHOR-DERIVED / EXACT INTEGER AUDIT PASS / PORTABLE DRAFT / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING**. This note is a continuation of EC49CC at immutable `0cc382d5162456adf31710191b488e049b278a5d`. Native positive signed-X6 BRC source: `EC49CA_CRT/native_signed_brc.py`, Git blob `300a96e3dc24bf6fff73743037a0347a8bc83176`.

Frozen research/control reads: GLOBAL_KNOWLEDGE_V1 `main@d1e02ddc52af58fc1512d5675ea38d7ada187a8a`; Enterprise Math `main@dae896eec630511ed988677bd6b4f134e02a45c7`. P000 ACTIVE_LOCKED and ACTIVE worldview were read and left unchanged. Portable protocol: `docs/PORTABLE_RESEARCH_PROTOCOL.md` and `docs/AUTONOMOUS_RESEARCH_OPERATIONS.zh-CN.md` at the stated EM pin.

## Exact model

Each ordered length-n word uses the twelve native signed directions ±E1,...,±E6, preserves branch order/multiplicity and has a six-component signed displacement z. The two positive BRC weight instruments are `w0+=(2,3,3,2,1,1)` and `w1+=(3,2,3,2,1,1)`, all negative-direction weights equal one, and a third channel counts words. Observe whether the ordered signed patterns `A=(+E1,+E2)` and `B=(+E2,+E1)` have occurred. A product nine-state DFA `q=(qA,qB)∈{0,1,2}²` records each 2-letter pattern's state (0 reset, 1 matched the first letter as the current suffix, 2 permanently matched). The terminal readout comprises all 4 Boolean atoms 00/01/10/11 × 3 weighted/count channels, after selecting **zero displacement**.

Let `K=<s,t>` have commuting generators `s=(E1 E2)`, `t=(E5 E6)`. The group relabels both signs and all six displacement coordinates. Under s the two DFA pattern states and instrument channels 0/1 must be exchanged, whereas the count remains unchanged; t acts trivially on both DFA and channels. Denote this vector representation by `T_g`. The declared future operation is extension by one typed native signed step with its DFA update; arbitrary unrepresented suffix observables are not covered.

## Theorem 1: all-layer lossless quotient

For fixed even n, let `D_j` be the *actually reachable* prefix states `(z,q)` at depth j satisfying the return-cone bound `||z||_1≤n-j`. Let `f_j(x)∈ℤ_{≥0}³` count and weight all admissible ordered prefixes reaching x. Then for all j≤n, x∈D_j and g∈K,

`f_j(gx)=T_g f_j(x)`.

Choose one canonical representative from each K-orbit. Keep only its three-coordinate vector. To advance one step, expand each **distinct actual source** in each orbit with the appropriate T_g channel permutation, apply the twelve native signed BRC steps, prune if the resulting displacement cannot return, and accumulate **only canonical destination** states. This reduced dynamic program reproduces all 12 exact terminal coordinates and, more strongly, the entire full state map after group reconstruction at **every intermediate depth** for every even n.

**Proof.** Applying g letterwise is a bijection of ordered prefixes, preserves branch multiplicity and return-cone admissibility, and commutes with native displacement and the product-DFA transition. By the stated instrument choice, the word's weighted vector transforms by T_g. This proves the equivariance formula. Assume the reduced state values at depth j equal the full ones at canonical sources. Expanding distinct group images reconstructs every actual source once, including stabilizer-fixed sources; each edge into a canonical destination then occurs exactly once with its correct source weight. Every omitted target is determined by the equivariance equation. This gives the induction step, with the empty prefix as base. On returning to displacement zero, expand terminal q-orbits and sum each of the four labelled Boolean atoms separately. QED.

**Stabilizers.** If s fixes (z,q), equivariance forces equal instrument-channel weights; if t fixes it, it is one actual source, not two. Canonicalization here is exactly `z5≤z6` and `(z1<z2) or (z1=z2 and q≤swap(q))`. Source orbit images are deduplicated before transitions. This construction uses exact nonnegative integers, with no division, averaging or scalar cancellation.

## Theorem 2: Burnside count and bit-cost boundary

At each layer, with the full state set D_j and quotient representative count R_j,

`R_j=(|D_j|+|Fix_Dj(s)|+|Fix_Dj(t)|+|Fix_Dj(st)|)/4.`

This follows directly from the Burnside orbit-count theorem for the *joint* displacement/DFA state. In the positive integer-weight model a prefix weighted coordinate is bounded above by `12^j·3^j=36^j`, hence needs O(j) bits. Consequently the three-integer payload per stored representative costs O(j) bits. A six-dimensional ℓ1 return ball has O(n^6) lattice points; with the fixed nine-state DFA, the coarse memory bound is O(n^7) payload bits and schoolbook bit-time bound is O(n^8). The quotient reduces the exact state-key and payload **constants**, not these polynomial exponents. Runtime depends on orbit handling and is measured independently.

## Executed exact certificate

`VERIFY_EC49CD_MIN.py` is the actually executed compact checker. The expanded checker and longer execution archive are retained as companion author evidence. For each even n∈{0,2,4,6,8,10,12}, the compact checker compares the *entire* full and lifted-quotient state dictionaries at every depth, verifies all Burnside fixed-point terms, verifies the 4×3 terminal vector, and compares unfiltered totals with the pinned native `endpoint_weight`/`endpoint_multiplicity`. The expanded checker additionally directly enumerates all signed words at n=0,2,4 and tests the closed-path obstruction. All comparisons use exact Python integers.

| n | native weighted return | native closed-word count | full peak states | quotient peak reps | full peak channel bits | quotient peak channel bits |
|--:|--:|--:|--:|--:|--:|--:|
| 0 | 1 | 1 | 1 | 1 | 3 | 3 |
| 2 | 24 | 12 | 12 | 8 | 44 | 30 |
| 4 | 1,560 | 396 | 94 | 47 | 572 | 297 |
| 6 | 152,640 | 19,920 | 480 | 203 | 4,838 | 2,152 |
| 8 | 18,921,000 | 1,281,420 | 1,874 | 721 | 30,848 | 12,038 |
| 10 | 2,737,312,704 | 96,807,312 | **5,932** | **2,115** | **140,721** | **50,409** |
| 12 | 441,121,650,816 | 8,175,770,064 | **16,022** | **5,418** | **502,696** | **169,844** |

Peak channel bits mean the sum of the actual three Python integer bit lengths at one layer, with minimum one bit per zero coordinate; dictionary/key/allocator overhead is excluded. For n=12 the maximum number of held state keys is about 66.2% smaller, and the peak integer-payload bits are about 66.2% smaller. In one local run, unquotiented vs quotient n=12 took about 0.42 s vs 0.34 s; wall-clock is illustrative, not a theorem.

The n=12 ordered terminal atom rows (weight0,weight1,count) are:

```
00 (356739909456,356739909456,7033558224)
01 (39309550560,39309550560,542082240)
10 (39309550560,39309550560,542082240)
11 (5762640240,5762640240,58047360)
```

These sum to the native 441121650816 weighted output (in *each* weight channel) and 8175770064 closed words. The exact machine report and regenerating code are in this directory.

## Closed-path counterexample: scalar quotient loses an observation

Let `p=(+E1,+E2,-E1,-E2)` and `sp=(+E2,+E1,-E2,-E1)`. Both are length-four **closed** signed-X6 words in the same K orbit, and each has current unfiltered `(weight0,weight1,count)=(6,6,1)`. The fixed A-filter gives 6 on p but 0 on sp, while B does the opposite. Thus identifying them as one *untyped scalar* discards a permitted observation. The typed quotient keeps the A/B transformation and both instrument channels, avoiding this loss.

## Reproduction, status and next research unit

Run `python VERIFY_EC49CD_MIN.py` from this folder with Python 3.11+; the code imports the unchanged sibling `../EC49CA_CRT/native_signed_brc.py`. Expected terminal marker: `PASS_EC49CD_MIN 7`. Actually executed source SHA256: `48480ac798c33fbcdbecd07a626dae606ef1b1a6c54bcedf997e4cbf2ed8de23`; report SHA256: `79bab1436c991bc775e99cc13141c860daabd2de60e0af45d0a0ff83c9f4fa4e`. Expanded original checker SHA256: `7f5e89fcbd6721f01ba8bf6303d4e1c77ada722ce4a1729f4bde063aa6ff077f`; expanded deterministic report SHA256: `fd7d93466f649879de872a0cb001942aa4070832c6ce8271c96ada889ac99cbc`, identical across two executions.

The native control service 0.6.11 read gave `research_authority_granted=false`, `executor_binding_configured=false`; owner inventory request returned `CONTROL_QUOTA` with active jobs 5/5. Thus current Source owner is **unknown**, and this is neither a native CLAIM/Result nor an independently reviewed/admitted theorem. No protected P000/worldview/other lane files were changed.

**Next EC49CE:** compile stabilizer-aware orbit-to-orbit transition coefficients directly, avoiding explicit source-orbit expansion while preserving the typed two-instrument and A/B fibre. Derive integral edge coefficients or a provable fractional-cancellation construction, compare full, EC49CD and compiled quotient at n=10,12,14, and report actual time, peak state memory, bit complexity and counterexamples to illegal scalar folding.