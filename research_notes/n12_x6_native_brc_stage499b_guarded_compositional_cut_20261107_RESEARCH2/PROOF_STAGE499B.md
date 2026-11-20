# Stage499-B — Guarded compositional cut signature for finite BRC futures
Date: 2026-11-07. Status: AUTHOR_PROVED / EXACT_EXECUTED / INDEPENDENT_REVIEW_PENDING.

## Provenance and scope
Frozen scientific input: global `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`, Enterprise Math `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`, P000 blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Direct Stage498-B frontier `187306e157d549cda1c91407f5638a59471fc481`. Current normative reads: global main `b1cec965d4cccd23cb004e4163ffee66d44b2ebc`; Enterprise Math main `948d2a02273b7b4db83372b760ff69c5cc3a7c0e`. GitHub author identity: `awdawmip`; native TASK owner/claim remains unresolved because backend returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH`, operation_sent=false. No theorem admission or physical BRC heartbeat claim.

## Exact typed state and observer
Let Σ={A,...,L} encode the 12 signed primitive directions along six X6 native spatial axes, with directions A-F = +e1,...,+e6 and G-L = -e1,...,-e6 in a chosen chart. Words are nonempty finite sequences of tokens (direction, source), with source O original or P publicly inserted. Define
(F(w)=(D(w),E(w))\in\mathbb Z^6\times\mathbb N^{12\times12}),
(D(w)=\sum_i v(w_i)), and (E_{ab}(w)=\#\{i:w_i=a,w_{i+1}=b\}).
F observes directional relations but not source labels directly. Every trace records the F observation after every action and action legality.

The five commands are precisely the Stage498-B grammar: POP last; SET_END_MINUS_2_C replaces the token at zero-based position n−3 with C keeping source (n≥3); INSERT_BEFORE_LAST2_C inserts public C before position n−2 (n≥2 and, in the original experimental variant, n<8); DELETE_END_MINUS_1 deletes position n−2 (n≥2); DELETE_LAST_PUBLIC deletes the rightmost P-source token, if any. We also consider the natural uncapped INSERT variant (n≥2) with the other commands unchanged.

For nonempty words u,v, concatenation satisfies (D(uv)=D(u)+D(v)) and
(E(uv)=E(u)+E(v)+[\operatorname{last}(u),\operatorname{first}(v)]).
The first/last direction of nonempty u is recoverable from F(u):
(v(first(u))=D(u)-\sum_{ab}E_{ab}(u)v(b)),
(v(last(u))=D(u)-\sum_{ab}E_{ab}(u)v(a)).
The summation of all E entries gives |u|−1.

## Theorem 499.1 — Sublinear exact future-preserving cut
For every h≥0 let L=h+3. On the domain of token histories (w=ct) with |c|≥1, |t|=L and **every source tag inside c equal to O**, define the compositional cut signature
[
\boxed{K_h(w)=(F(c),t)}.
]
Here the suffix t stores each direction and source label in order. For two histories x,y in this domain,
[
K_h(x)=K_h(y)\implies x\sim_h y
]
for **every** common legal action trace of length at most h under either the original capped Stage498 grammar or the uncapped insertion variant. The relation \(\sim_h\) includes legality and F after every prefix. Thus K_h is an exact sufficient finite-future quotient interface, computed in one left-to-right pass without enumerating S_h.

### Proof
Take any trace prefix of length j≤h. Maintain the invariant that the current state remains the original immutable c concatenated with a dynamically edited suffix t_j, and that |t_j|≥L−j. Initially this holds. Prior to an additional action, j<h implies |t_j|≥4. POP, SET at third-last, INSERT before last two and DELETE second-last each access or alter only t_j. They reduce its length by at most one. All source-P tokens are inside t_j because c began entirely O and the only operation creating P is the suffix-local INSERT. Hence DELETE_LAST_PUBLIC, when legal, also acts only on t_j. Every legality decision is determined from t_j and current total length; |c| is determined from F(c), so the capped n<8 test is also determined. Two states with the same K_h therefore have the same legal transitions and the same evolving tagged suffix after every common prefix. Their fixed core F is identical. The boundary-concatenation identity reconstructs F(c t_j) from F(c) and t_j at every prefix, so the complete observations agree. Induction over at most h operations proves the claim. QED.

## Storage and an exponential collapsed family
There are 150 integer counters in F(c), each with magnitude at most |c| (the six signed displacement counters may be negative). The tagged suffix has L=h+3 tokens over 24 possible direction/source pairs. A direct encoding uses (O(150\log_2(n+1)+(h+3)\log_2 24)) bits. For fixed h this is O(log n), and for h=o(n) it is o(n) bits.

Let U=AABA and V=ABAA, all labels O. They have identical F, first=A, last=A. Hence every concatenation of k independent choices from {U,V}, followed by the common O-tagged suffix C^(h+3), gives exactly the same K_h. This forms a concrete fiber of (2^k) distinct length-(4k+h+3) histories for each k≥1. As the theorem applies, all are h-future equivalent even though their ordered internal histories differ. This is a proved nontrivial compositional compression family, not a claim of K_h minimality.

## Proposition 499.2 — Source-tag guard matters
For h=1 consider x=AABACCCC and y=ABAACCCC. Label position 2 as P in each and all other positions O. The first four directions in both form different cores with the same F, and the final four are the same tagged suffix. A naive K_1 that ignores source labels within the core therefore agrees. DELETE_LAST_PUBLIC removes position 2. The resulting value histories are ABACCCC and AAACCCC, with different F (in particular different displacement), so these histories separate in one step. This is an exact counterexample to extending the formula indiscriminately to source-sensitive histories with P inside the compressed core.

## Execution certificate and BRC interpretation
The attached `REPRO_STAGE499B.js` is the exact executed standard JavaScript program. It checks the full five-action trace tree for every pair from the constructed gadget families h=0..3, k=1..5 under both insertion variants, plus exact boundary-reconstruction algebra and the source-tag counterexample. The generated `REPRO_STAGE499B_EXECUTED.json` reports 248 history comparisons, 496 trace-mode pairs, 11,346 compared action-tree prefixes, and 248 compositional reconstructions, all passing. This finite verification exercises the proof but the theorem is the independent induction above.

The BRC carrier is the ordered population of signed-X6 histories, retaining separate branches/multiplicity. This cut merges only branches whose declared F responses and legal future actions are identical through h steps, with source tags guarded. The independent Stage498 S_h quotient remains the unique coarsest such partition; K_h is a cheap, compositional sufficient representation. No time evolution beyond this explicit finite action grammar is inferred.

## External research reference
Bals, Pissis, Tinca, *Optimal Enumeration of Eulerian Trails in Directed Graphs*, ESA 2026, publication date 2026-08-25, DOI 10.4230/LIPIcs.ESA.2026.60. Their O(m+z_T) enumeration objective is distinct from random-access rank/unrank of one history; algorithmic comparison remains an independent exact-bit-cost task.

## Next unit
Stage500-B: extend the guarded interface to retain or dynamically summarize a bounded number of public-source tokens inside the core, with a rigorous last-public cursor/interface and worst-case access bound; search for a smallest counterexample where a bounded positional repair fails. Independently run exactly matched inventories on Stage494 recount and Stage495 one-solve Euler rank/unrank and report input preparation, support loss, big-integer bit arithmetic and memory.