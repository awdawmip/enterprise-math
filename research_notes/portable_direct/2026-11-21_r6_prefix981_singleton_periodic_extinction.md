# PREFIX-981 — Singleton-port periodic words: exact extinction and 19-bit triple census

2026-11-21 · Research6 · AUTHOR_PROOF / EXACT_INTEGER_CHECKED / NOT_REVIEWED.

Prior verified scientific frontier: PREFIX-980 at \`enterprise-math@2bb34f7293ee6e30277883f0025710a352bf4092:research_notes/portable_direct/2026-11-21_r6_prefix980_periodic_word_uniform_carrier.md\`.
Frozen scientific pin: \`enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json\` (Source V5), unchanged. Account P000/ACTIVE assumptions and current applicable research rules were read separately.
Historical provenance: EM-DIRECT-FBEA5D, Activity RA-3FB2D033BE6048D8712FF056; public identity bytes do not themselves attest to execution capability.

## Definitions

Fix p>=3. The residual dictionary is \`D_p={2^i-s*2^j:0<=i,j<p,s=+1 or -1}\`; each (i,j,s) is a distinct named source. State x is an odd integer modulo 2^p; enabled nonzero port j is flipped: \`x -> x XOR 2^j\`. A positive-sign source requires bit_j(x)=0, a negative-sign source requires bit_j(x)=1.

Write T_a for all allowed nonzero ports (j>=1) represented by residual a. Define the **singleton-port family** \`E_p={a in D_p:|T_a|=1}\`. For a in E_p denote its unique port by j(a).

**Lemma 981.0 — unique sign and named source.** Every a in E_p has exactly one enabled bit value b(a) in {0,1} at j(a), with exactly one corresponding named source. For fixed (a,j,s), exponent i is unique from \`2^i=a+s*2^j\`. If both signs existed at the same port j, then \`2^i-2^k=2^(j+1)\`, forcing i=j+2, k=j+1, a=3*2^j. But a also has a source \`(j,j+1,-1)\` on the distinct nonzero port j+1, contradicting singleton support.

Fix an ordered nonempty word \`w=(a_0,...,a_{L-1})\` with every a_t in E_p, repeated cyclically. At phase t there is either one valid named edge, at the predetermined port \`j_t=j(a_{t mod L})\`, or no edge.

## Exact initial-state/path counts

Let \`m_j(t)=#{u<t:j_u=j}\` and \`q_t=b(a_{t mod L}) XOR (m_{j_t}(t) mod 2)\`. Define \`Q_j(n)={q_t:0<=t<n,j_t=j}\` and \`U_n={j:Q_j(n) nonempty}\`. A valid path with this prescribed first n edges requires \`bit_j(x_0)=q_t\` at every occurrence. These constraints factor by port, giving exactly

\[
N_n(w;p)=\begin{cases}
0,&\exists j,\ |Q_j(n)|=2,\\
2^{p-1-|U_n|},&\text{otherwise}.
\end{cases}\tag{981.1}
\]

This counts pairs of odd initial state and **named** length-n path. Since the enabled source is unique at each phase, no source name or branch multiplicity is lost.

## Theorem 981.1 — exact two-period cutoff

For every p and every singleton-port word w of period L, a given odd state supports an infinite named path **iff** it supports the first 2L transitions. Any finite maximal path has length at most 2L-1.

Proof. Port j occurs d_j times during a complete word. After one period its bit has toggled by d_j mod 2. If d_j is even, the j-bit begins each next period unchanged; eligibility already checked in period one recurs indefinitely. If d_j is odd, its bit begins period two inverted; since the first occurrence of j always requires the same fixed b(a_t), it fails at that occurrence in period two (assuming the first period succeeded). Thus survival through period two forces every d_j even, after which the entire state and phase recur after one period. This is sufficient and necessary. QED.

**Corollary 981.2 — odd-period extinction.** For odd L, \`sum_j d_j=L\` is odd, so some d_j is odd. Hence every odd-period singleton-port word becomes extinct within 2L-1 edges. In particular, all three-phase singleton words die by step 6, improving PREFIX-980's unrestricted nonzero triple bound of 191 for this family.

**Corollary 981.3 — even-period exact criterion.** Infinite paths exist iff every d_j is even and the required bits b(a_t) at consecutive uses of port j alternate 0,1,0,1,..., within the period. If so, exactly \`2^(p-1-|U|)\` odd initial states support infinity, U being all used ports. This is an O(L) decision after the a -> (j,b) lookup.

## Sharpness and complete 19-bit singleton-triple arithmetic

At p>=4, take \`w=(-1,3,-4)\` and odd x=1. The unique sources are respectively \`(0,1,+1), (0,1,-1), (2,3,+1)\`, and the first five valid updates are \`1 -> 3 -> 1 -> 9 -> 11 -> 9\`. Step six at port 3 fails. Thus the five-step upper bound is sharp.

Let n_{j0},n_{j1} count singleton residuals with unique port j and required bit 0 or 1. Write \`N=sum_j(n_{j0}+n_{j1})\`.

**Proposition 981.4 — exact number of five-step-surviving triple words**

\[
F_5(p)=\sum_{j=1}^{p-1}2n_{j0}n_{j1}\bigl(N-n_{j0}-n_{j1}\bigr).\tag{981.2}
\]

Every such word supports exactly \`2^(p-3)\` initial odd states for its first five edges; total named state/path pairs are \`2^(p-3)*F_5(p)\`.

Proof. The first and fourth phase share residual a, and the second and fifth share residual b. For these respective pairs to remain enabled, the number of intervening flips on their ports must make the initial required bit recur. Inspecting the three predetermined ports, both requirements hold iff \`j(a)=j(b)!=j(c)\`. The consecutive a,b edges then require opposite initial-bit eligibility at their shared port, yielding \`2n_{j0}n_{j1}\` ordered choices and \`N-n_{j0}-n_{j1}\` choices for c. Two distinct input bits are forced; the other p-3 are free. QED.

At p=19, direct exact construction of the source dictionary gives \`|E_19|=312\`. Equations (981.1)–(981.2) give:

| Quantity | Exact value |
|---|---:|
| Single-port numerical residuals | 312 |
| Ordered single-port triple words | 30,371,328 |
| Triples allowing infinite paths | 0 |
| Triples permitting five valid edges | 192,544 |
| Five-edge named initial-state/path pairs | 12,618,563,584 |
| Maximum finite path length | 5 |

This is an algebraic census of 30,371,328 triple words, **not** an exhaustive listing of those words or their 19-bit state graphs.

## Verification and limitations

The independently executable \`PREFIX981_R6_SINGLE_PORT_PERIODIC_CHECK.py\` constructs all original (i,j,s) named sources, checks unique singleton signs, and cross-compares factorized counts with direct raw named-XOR simulation for every ordered triple of singleton residuals at p=3,4,5,6 and every n from 0 through 5. Counts of ordered triples are 512, 1,728, 5,832, 17,576, totaling 25,648 triples and 153,888 raw-comparison aggregates; every one passes. The six-edge extinction claim is checked for each triple. All 20,736 singleton four-phase words at p=4 are checked against raw eight-step survival; 1,168 have infinite paths. The 19-bit port-class arithmetic yields the table above. The matching JSON counts and raw code are preserved in adjacent scientific artifacts.

This is an auxiliary signed-source XOR observer. A typed BRC Cell/Link/Port or X6 TRIADIC_CLOSURE_E embedding has not been established. Independent scientific review is NOT_REVIEWED. No change to P000, formal task/CLAIM, shared PROGRESS, Result or Review.

## Next question

Extend the phase/bit-consistency method to **two-port branching residuals** and exact interleaving of port use, seeking sharper sustained-cycle criteria and better finite-path bounds. Preserve named-source identity and ordered joint correlations. Mother problem \`B_fix,odd(32) in {19,20}\` remains open.
