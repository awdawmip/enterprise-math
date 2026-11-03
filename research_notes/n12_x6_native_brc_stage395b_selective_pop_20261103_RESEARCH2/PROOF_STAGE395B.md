# Stage395-B — Exact future-memory quotient with selective undo and typed signed/positive BRC branch weights

2026-11-03, Research2 portable author-side continuation of Stage394-B (PR #1736, preceding commit `6612b2b0284e6be0d06d1b1e7af66ac354b82b5f`). This document is a new combinatorial proof in the declared **Path-formal** model. It does not posit a physical undo action, a seventh spatial coordinate, or mathematical admission.

## Frozen science and live method

- Frozen EM scientific source `awdawmip/enterprise-math@2af3fc484eb11060b69e0afc1b562bcaf5ad1419`, global science `awdawmip/chatgpt-global-knowledge@bf84bd7c61a2444b59b1da96be57df0e9ae47e53`, exact P000 V5 blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`.
- Reused frozen native derivation `research_notes/X6_SIGNED_PATH_BRC_AND_PRIMITIVE_LINE_V17_20260905.md` (blob `aa005cd62c45d7f4105632257db9186b115c5b29`) and `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md` (blob `e266c103cae02550c8bbaa794958f3423b41d151`).
- Current normative context was separately read via `docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context`; role, claim, review and Source authority remain distinct from a GitHub author's proof.

## Objects, observations and allowed future language

Fix an arbitrary chart Cell anchor in the native affine X6 torsor. Let `A={+E_i,-E_i:1<=i<=6}` with twelve distinct signed displacement letters. For ordered path `w=d_1 ... d_m in A*`, define endpoint `z(w)=sum_j delta(d_j) in Z^6` and turn count `tau(w)=sum_{j=2}^m 1[d_j != d_{j-1}]`. The first three components of each of the **20** selected 3-axis observations are retained as `R_S(z)=(z_i-min_S(z),z_j-min_S(z),z_k-min_S(z))`; the integer common depth `h(z)=min_i z_i` repairs the joint relative observation to the full signed X6 endpoint. Source tag `sigma` remains attached. Let `N_m(z)` denote the source's exact all-length signed-path count (not a spatial distance).

Take arbitrary positive rational native weights `p_d in Q_{>0}` and retain the native source Weighted-BRC endpoint mass

`B_m^p(z)=sum_{w': |w'|=m,z(w')=z} prod_j p_{d_j}`.

This is the exact source multinomial/opposite-pair formula, depending only on `(m,z,p)`; a change in the order of a particular branch word does not change the *endpoint aggregate*. Independently fix nonzero rational signed branch factors `omega_d in Q^x` and give an **individual branch** its multiplicative trace `Omega(w)=prod_j omega_{d_j}`. This latter trace is a typed signed algebraic extension, not a claim that positive Weighted-BRC implements cancellations or physical amplitudes. Nonzeroness is used exactly for POP division; no logarithms or ordinary trigonometric functions are needed.

The observer is

`O(w,sigma)=(sigma, (R_S(z))_{|S|=3}, h(z), m, N_m(z), B_m^p(z), tau(w), Omega(w))`.

Fix an arbitrary **permitted undo-label subset** `D subseteq A` and total undo budget `H>=0`. A future step may APPEND any `d in A`. POP is defined only when the current word is nonempty, its terminal label is in `D`, and the remaining budget is positive. At most `H` POP operations are permitted in the complete future, interleaved with arbitrarily many APPEND operations. The observer is readable after every operation. This partial-operation language treats whether POP is defined as operational information. All claims below hold for every chosen `D`, including the empty and full sets, every initial source, and all finite words.

## Theorem 395.1 — Exact minimal selective-POP memory

Define the **barrier-limited suffix** `K_{D,H}(w)` by scanning `w` right-to-left, taking at most `min(m,H+1)` letters and **stopping immediately after taking the first letter outside D**, if encountered. Return the scanned letters in their original order. The empty word has empty signature. For any two words `w,v` in the same current O-fiber, the following are equivalent:

1. Every admissible finite future APPEND/selected-POP operation sequence produces identical observations (and the same definedness of each proposed operation).
2. `K_{D,H}(w)=K_{D,H}(v)`.

Consequently for the fixed current observer fiber `F_o=O^{-1}(o)`, the **sharp** number of required additional future-memory states is

`q_{D,H}(o)=|{K_{D,H}(w): w in F_o}|`, with `ceil(log2 q_{D,H}(o))` fixed-width bits. This is an equality for each fiber; it does not assert uniform attainment of `12^(H+1)`.

**Sufficiency.** Represent the compressed state by current `O`, the remaining undo budget `r`, and `K_{D,r}`. The O fields reconstruct the full endpoint z and m. APPEND(d) updates z by signed native unit displacement, m by +1, tau by `1[m>0 and last != d]`, Omega by multiplication by omega_d, and recomputes the two endpoint BRC masses from `(z,m)` using the original formulas. Its signature is the last `r+1` letters of the former signature followed by d, truncated at the first non-D barrier from the right. If `d outside D`, the new signature is simply `(d)`: this new unpoppable barrier hides the earlier word. For permitted POP, the terminal d is known from the signature, and when m>1 the penultimate letter is also known since r>=1. Update z by `-delta(d)`, m by -1, tau by `-1[m>1 and penultimate!=d]`, Omega by division by the nonzero omega_d, and r by -1. Remove d from the signature; it is precisely `K_{D,r-1}` of the shortened word, because at most r further original letters could be reached before the decrement. APPEND and POP agree for any two equal compressed states and preserve equal compressed successor states. Induction over arbitrary finite operation sequences proves sufficient future fidelity.

**Necessity.** Suppose two words in the same O-fiber have unequal signatures. The common terminal letters preceding their first mismatch, counted from the right, all belong to D: otherwise both signatures would already have stopped identically at a common barrier. Let the first differing terminal letter have rightward distance j. It satisfies `1<=j<=H+1` and, since both initial m are equal, both such letters exist. Apply `j-1` permitted POPs to the identical terminal D letters, using no more than H undos. Their remaining final letters now differ, say d and e. APPEND(d) yields turn increment zero in the first word and one in the second, because m-(j-1)>=1 and d!=e. The new observed tau distinguishes the histories. Thus unequal signatures are distinguishable. The minimum-state formula follows from the equivalence classes themselves. QED.

The proof uses the full native alphabet, all twenty three-component coordinate readouts and common-depth reconstruction; it does not identify source or internal branch relation with an extra spatial coordinate. Weights appear only as typed observations and valid exact multiplicative update laws.

## Corollary 395.2 — Strict quotient refinement lattice

For D empty, the signature is just the terminal label (or empty for the empty word), recovering the APPEND-only result. For D=A it is the last `min(m,H+1)` labels, recovering Stage394-B. If `D subseteq E`, then equality of `K_{E,H}` implies equality of `K_{D,H}`. Hence on every shared O-fiber `q_{D,H}(o) <= q_{E,H}(o)`. Increasing H can only refine/preserve the future equivalence partition. This is a monotonicity law for **declared future operations**, not a universal law that path history is discardable.

**Exact strict compression witness.** Set `D={+E_1}`, H=3 and define two six-step native paths:

`w=(-E_1,+E_2,-E_2,+E_4,-E_4,+E_1)`,

`v=(-E_1,+E_3,-E_3,+E_4,-E_4,+E_1)`.

Both have z=0, m=6, tau=5, `N_6(0)=19920` and the same entire twenty-triple/depth observation, same source and same `B_6^p(0)` for any given common positive native weights. Choose nonzero signed factors `omega(+E_i)=i+1`, `omega(-E_i)=-1/(i+1)`; both branch products are equal to `-1`. Hence the richer current O is identical. The two full 4-letter suffixes differ, so the unrestricted H=3 POP model distinguishes them, but the selective signature is **identically** `(-E_4,+E_1)` because `-E_4` is an unpoppable barrier. By Theorem 395.1 no legal future can distinguish them under `D={+E_1}`. This supplies a concrete strict separation between two observer-operation quotients.

The obstruction scales: insert an arbitrary number of cancelling `(+E_i,-E_i)` blocks before the fixed barrier `(-E_4,+E_1)` while fixing path length and source. Each such family shares endpoint, all twenty projections, depth, length, maximum turn count and common signed product of the reciprocal-weight type, yet the inaccessible earlier signed labels can vary exponentially. Safe selective-POP compression is therefore a structural operation-specific quotient, not a numerical approximation.

## Source-compatible BRC and actual exact execution

The source's full six-axis recurrence is

`N_{m+1}(z)=sum_{d in A} N_m(z-delta(d))`, and

`B^p_{m+1}(z)=sum_{d in A} p_d B^p_m(z-delta(d))`,

with initial unit mass at `m=0,z=0`. Independently evaluate the source's multinomial/opposite-pair closed formulas. The Python 3 standard-library checker in `REPRO_STAGE395B_RESTRICTED_POP.py` performs **1,375 exact endpoint comparisons** over all six native axes for lengths m=0..4 for both counts and positive weighted mass. It also enumerates all 341 words over `{+E_1,-E_1,+E_2,-E_2}` with length <=4, forms the complete O-fibers, and checks 14,736 same-fiber word pairs across D=empty, `{+E_1}`, `{+E_1,-E_1}`, and the four-letter test alphabet with H=0,1,2. Behavior is evaluated over all operations of length <=H+1 with POP-definedness and remaining budget; this finite witness horizon is sufficient for the necessity direction. Finally 4,432 exact signed branch multiplication/division checks and the strict six-letter witness pass. These checks corroborate the universal proof but do not replace it. All arithmetic is integer/Fraction; no floating point.

The source's `D=A` case is a theorem over the *full twelve-letter alphabet*; the finite checker takes four test directions for tractable exhaustive crosschecks. `REPRO_STAGE395B_EXECUTED_STDOUT.txt` is an actual execution result of the companion code.

## Status and next discriminating question

**New proved author-side theorem:** exact and sharp selective-undo per-fiber memory quotient for full signed-X6 Path-formal branches with nonzero rational signed trace and source-positive Weighted-BRC endpoint aggregation; strict compression counterexample; monotonicity in the allowed undo label set. The model's POP remains a syntactic stack operation and is not a physical Cell inverse or time reversal. The algebraic signed trace is a labeled branch extension, not a claim of signed-mass native Foundation acceptance. Formal native Task CLAIM/Result/independent Driver acceptance remain separate.

**Stage396-B question:** add one precise provenance-conditioned inverse or paired cancellation operator that can cross the `-E_4` barrier in the six-letter witness, and determine the new minimal future quotient or produce an exact counterexample to the barrier signature. Classify its effect when the observer additionally retains a joint branch-label correlation or exact rational finite-weight histogram rather than a single product. Preserve frozen pins, full six-dimensional signed directions, original source identity and physical/Path-formal typing.
