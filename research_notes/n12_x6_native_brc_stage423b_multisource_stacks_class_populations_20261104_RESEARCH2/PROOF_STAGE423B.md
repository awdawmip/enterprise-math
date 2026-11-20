# Stage423-B — Multisource deletion frontiers and direct 24-class populations

Date: 2026-11-04. Parent: Stage422-B, Draft PR #1736 at c7b7fbdaaadf8dea633d53f9a27d0b0aa9e793db. Author-side mathematical derivation plus executed finite exact checks; **UNREVIEWED / NOT_ADMITTED**.

**Immutable scientific inputs:** global \`bf84bd7c61a2444b59b1da96be57df0e9ae47e53\`; Enterprise Math \`2af3fc484eb11060b69e0afc1b562bcaf5ad1419\`; P000 blob \`bcc2590d3168a28f72e8b9f0f9b1f76faadcd488\`. Current normative rules are read separately. The substrate is an ordered path observer within native six-dimensional signed-X6 (\`D={±E1,...,±E6}\`), preserving both six-component endpoints, each full directed adjacency histogram J, absolute-position matching K, full original provenance and attempted action legality. No native physical time/rotation dynamics is claimed or computed here.

## Theorem 423.1: k-source asymmetric block deletion inequality

Fix k≥2 sources, numbered 0,...,k-1. Every source consists of a surviving prefix of its own original word followed by a surviving suffix of APP-generated labels. Each successful **common** APP appends exactly one label to *every* source. Source 0, the anchor, never receives an independent POP; other source j may have successful independent terminal POPs, counted by t_j. Besides APP and POP, each successful block-deletion event e removes exactly b_(e,j)≥0 terminal symbols from source j (possibly zero when j is not incident to e), with possibly different b-values for different sources. These events are allowed only when all required terminal blocks exist; inverse-pair constraints, if imposed, only restrict enabled events. No operation reorders original letters or inserts into their prefix.

Let d_j be the number of removed **original** labels, u_j the count of surviving **APP** labels, C_j=Σ_e b_(e,j), and a the common number of successful APPs. At every reachable step,

**d_j ≤ d_0 + t_j + Σ_e max(0,b_(e,j)-b_(e,0)),  1≤j<k.**

In the shared-arity case b_(e,j)=b_(e,0) for every event, this reduces to **d_j≤d_0+t_j**. For two sources, a joint inverse-CANCEL removing 2 from each and arbitrary signed-X6 common APP, it reproduces Stage422's coupled-stack estimate.

**Proof.** Word-length conservation gives u_j=a-t_j-C_j+d_j and u_0=a-C_0+d_0. Define G_j=Σ_e max(0,b_(e,0)-b_(e,j)). We first prove u_j-u_0≤G_j. Initially both sides are zero; common APP changes neither difference, and POP of j can only decrease u_j. A block deletion changes (u_j,u_0) to ((u_j-b_j)_+,(u_0-b_0)_+). For x,y,b,c≥0, (x-b)_+-(y-c)_+ ≤ (x-y)_+ +(c-b)_+. Thus its possible positive increase is at most (b_0-b_j)_+. This proves the gap inequality by induction on any legal attempted trace, with failed attempts leaving the state unchanged. Substituting into the conservation identity,

d_j-d_0=t_j+C_j-C_0+u_j-u_0
≤t_j+Σ_e(b_(e,j)-b_(e,0)+(b_(e,0)-b_(e,j))_+)
=t_j+Σ_e(b_(e,j)-b_(e,0))_+.

This proves the bound for all k, every sequence length and every permitted incidence/arity pattern. QED.

**Tight operator-arity counterexample.** Choose A=+E1 and B=-E1. Anchor original word P=AA, other original word Q=AB. Allow a Q-only inverse-CANCEL deleting its terminal AB pair, with no APP or POP. It gives d_P=0, d_Q=2, t_Q=0; hence the shared-arity formula would fail. The corrected formula gives 2≤0+0+2, with equality. This isolates the changed deletion-incidence hypothesis rather than changing spatial dimensions or observing only scalar displacement.

**One-B anchor corollary.** If P contains exactly one original B amid As and there are at most c *joint inverse-CANCEL* events, at most one CANCEL can remove two original P letters (such a pair must contain its only B); all other CANCELs remove at most one original P letter. Therefore d_P≤c+1. If P ends in at least c+1 original As, the B remains protected and d_P≤c. Hence for another source with p independent POPs, respectively d_Q≤p+c+1 and d_Q≤p+c. With p=3,c=2 these are the earlier 6 and 5 original-deletion bounds.

## Theorem 423.2: exact population multiset of Stage422's 24 classes

For n≥11 take the exact earlier fiber

P_i=A^(i-1) B A^(n-i),
Q_(r,s)=A^(r-1) B A^(s-r-1) B A^(n-s),
2≤r, r+2≤s≤n-1, i∈{r,s}.

Stage422 established an author-side 24-key full-future partition for three independent Q POPs, two joint inverse-CANCELs and arbitrary D×D paired APP, retaining both lengths/endpoints, complete directed J, absolute K and operation enabledness. **Conditional on that partition being correct**, the exact cardinalities of its 24 classes are the following multiset:

| Class size | Multiplicity |
|---|---:|
| (n-8)(n-9) | 1 |
| 2(n-8) | 1 |
| n-7 | 6 |
| n-8 | 2 |
| 1 | 14 |

The formula produces the populations directly from n without generating any of the (n-3)(n-4) ordered original pairs.

**Combinatorial proof.** Partition by the Stage422 class map:
- **B-capped:** s=n-5. Every r=2,...,s-2 and either i choice lies in one key, population 2(n-8).
- **R with s≤n-6:** one protected-tail key; 2Σ_(s=4)^(n-6)(s-3)=(n-8)(n-9) histories.
- **R, s=n-4:** two keys, each n-7 histories (i=r versus i=s).
- **R, s=n-3:** two keys of n-7 plus two singleton keys at r=n-5.
- **R, s=n-2 and i=r:** one key of n-7 plus two singletons.
- **R, s=n-1 and i=r:** one key of n-7 plus three singletons.
- **F, i=s=n-2:** one key of n-8 for r≤n-7, plus three singletons.
- **F, i=s=n-1:** one key of n-8 for r≤n-7, plus four singletons.

Here R keys retain P-last-6 and Q-last-6, while F keys fix P and retain Q-last-7; the B-capped class is the separate Stage422 all-future merge. The listed cases are disjoint, cover all permitted (r,s,i), and all their index intervals are valid for n≥11. They give 1+1+2+4+3+4+4+5=24 classes. The sum of the populations is
(n-8)(n-9)+2(n-8)+6(n-7)+2(n-8)+14=(n-3)(n-4),
matching |F_n|. The combinatorial **population** claim is proved independently; identifying the keys as *minimal all-future* states inherits the Stage422 all-horizon argument and its explicit separating traces. QED.

## General remaining-Euler/J/K transfer method

Let D be a fixed finite signed-direction alphabet. For given full directed edge counts J_P,J_Q and known initial endpoints/lengths, maintain integer dynamic-programming states (lastP,lastQ,R_P,R_Q,K,tailP,tailQ,z_P,z_Q), where R are the remaining directed edge multiplicities, tails are capped at sufficient lengths, z are chart-relative endpoint sums, and K is the current matched-absolute-position count. A joint next-letter transition (a,b) exists exactly when R_P[lastP,a]>0 and R_Q[lastQ,b]>0; decrement both entries, update endpoints and K by [a=b], and update tails. Give each *direction-type* choice weight 1, not the numerical multiplicity of indistinguishable copies of that edge. At terminal states require correct endpoints and K and map the original suffixes into the corresponding 24-class key (only under the declared F_n hypotheses).

The exact counting bijection follows by reading any ordered pair of source words from left to right: it determines one and only one sequence of typed transitions, and every completed valid path through the DP reconstructs one and only one pair. For the *special* defect fiber F_n, the above polynomial class formula bypasses this DP entirely. With binary-encoded n and the family contract already supplied, 24 O(log n)-bit integers cost a constant number of integer additions and multiplications; schoolbook arithmetic uses O((log n)^2) bit operations. Reading an explicitly supplied length-n pair of words, by contrast, costs Ω(n). For arbitrary dense J, the Euler/K DP is only potentially polynomial in numeric n at fixed |D|, with a very large alphabet-dependent state exponent; there is no claim of polynomiality in the input's binary encoding length or practical superiority to direct n² enumeration for this family.

## Actual exact validation and scope

\`REPRO_STAGE423B.js\` executed in JavaScript with an independent Python standard-library cross-check. It enumerated n=11..100 (304,080 original pairs), classified each by the exact Stage422 keys and checked all 24 formula sizes. An unrestricted *abstract* three-source stack exploration (original length 4 per source, common APP, POP permitted on sources 1 and 2, and every nonzero deletion arity vector in {0,1,2}³) examined 29,252 states and 175,678 transitions through depth 5, checking the theorem inequality after every transition. The finite test is a cross-check; the induction above supplies the unbounded claim. These are exact integer/formal path computations, not new native BRC physics, phase or physical-time calculations.

**Next Stage424-B:** implement and execute the generic remaining-Euler/J/K DP, verify its class populations against the direct formula for n=11..30, report preprocessing/state and encoded-bit costs, then examine sharper k-source bounds for fixed deletion-incidence hypergraphs. Independently audit Stage422 and the above results before any native Result/Driver admission.
