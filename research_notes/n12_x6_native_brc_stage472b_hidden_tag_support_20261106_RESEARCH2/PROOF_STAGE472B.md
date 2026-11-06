# Stage472-B: polynomial exact BRC support for hidden repair tags (2026-11-06)

Status: **AUTHOR_SIDE_PROOF / EXACT_INTEGER_EXECUTED / UNREVIEWED**. Parent Stage471-B at commit `73ace4f732eee7a72c1f461d3a331a4e289c8093`. Frozen scientific input: global `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`, EM `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`, P000 blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Current norms independently read; no change to frozen science.

## Exact domain

Original P,Q histories have `4<=m=|P|<n=|Q|`, first direction A, and all original steps in `Sigma={A=+E1,B=+E2,C=+E3}` inside signed X6. The complete fixed initial observer Phi includes both lengths, signed 6D endpoints, both full 12x12 ordered adjacency matrices, and K, the position-match count. Keep each original history pair with positive integer branch mass 1. The labeled future language of Stage469-B is POP_P<=1, APPEND_P<=1, POP_Q<=h, APPEND_Q<=1 in legal interleavings, including popping appended directions and all twelve signed choices at APPEND. Let `t=max(1,n-h)`.

## Theorem 472.1: exact positive support, mass and rank for every m-1<=t<=n

On any complete initial fiber, define the repair word in this lexical order (1-based indices):
`V_t=(P_(m-1), [Q_m if t>m], [Q_(m+1) if t>m+1], Q_t,Q_(t+1),...,Q_n)`.
It has at most **three** original isolated ternary tags, independent of n. Every class population `M(v)=#{(P,Q) in Phi:V_t(P,Q)=v}`, support `#{v:M(v)>0}`, total mass and support-lexicographic rank/unrank can be calculated exactly, using **O(n^20) nonnegative integer operations** for fixed three-direction alphabet, without enumerating histories or emitting all supported keys. Integers have O(n) bits, yielding a conservative O(n^21) bit-addition bound for explicit n.

**Why this repair is the correct restriction of R469.** Stage469-B defines `R469=(Lambda_h,P_(m-1),Q_m if t>m,Q_(m+1) if t>m+1)`. For t>=m, `Lambda_h` includes only Q_t..Q_n. For t=m-1, it also includes P_m at the first visible pair (P_m,Q_m). But the complete original P adjacency determines the final direction uniquely by `out_P(x)-in_P(x)=[x=A]-[x=P_m]`. Thus on a fixed Phi the variable part of R469 is exactly V_t. Stage469's **future-equivalence semantic theorem remains a separately unreviewed author-side premise**; the new support and population theorem is independently proven for V_t.

**Constructive proof.** Let EP,EQ be the 9-entry original directed edge counts. Form a positive integer prefix table H_t by generating P and Q jointly through `min(m,t)` and then Q through t, tracking last directions, P and Q edge-use vectors, matched position count and the at-most-three tag symbols. Reject only counts exceeding EP,EQ,K. The final P direction `p*=P_m` is already fixed by EP. When `t=m-1`, append this forced P_m after the hidden prefix and check EP, but postpone its match with Q_m until the first visible Q symbol. For t>=m, the full P word and K contribution are already in H_t. Complete EP equality is checked in all cases.

Group the resulting prefix weights by `(tags,Q_t)`. Each group consists of triples `(e0,k0,w)`, where e0 is the prefix Q-edge vector, k0 the prefix match count, and w a positive integer count of hidden original histories. For each deterministic suffix word `s=Q_(t+1)..Q_n`, let es count its Q edges including the junction from Q_t; let ks be `[p*=Q_m]` if t=m-1, otherwise 0. Then

`M(tags,Q_t,s)=sum_(e0,k0,w in H_t(tags,Q_t)) w * [e0+es=EQ] * [k0+ks=K]`.

Every original pair has precisely one hidden-prefix and visible-suffix split, establishing necessity and exact original multiplicity. Conversely each counted prefix concatenates with its displayed suffix and satisfies all EP,EQ,K constraints. The original signed six-axis endpoints follow from these edge counts and fixed initial A. The displayed identity is therefore both necessary and sufficient for counting M(v).

Now memoize suffix states `(tags,position,last-Q,used-Q-edges,deferred-match)`, returning `(1,M)` at a terminal with M>0, otherwise `(0,0)`. Sum support counts across **distinct labeled** children and sum masses separately. Although states are merged, each visible word corresponds to one labeled root-to-leaf path; Boolean class support and positive raw population remain different quantities. Lexicographic rank subtracts the support of preceding children; inverse unrank descends into the unique child containing its index. Induction on suffix length proves both counts and the inverses.

The prefix state uses 18 bounded edge counters, one match counter, position and constantly many letter/tag fields. After P has closed, the suffix has only nine Q-edge counters plus position and constant fields. The direct terminal loop over feasible bounded prefix profiles remains polynomial; the conservative global O(n^20) operation bound includes this work. This is polynomial in explicit history length, not in the binary bit-length of compressed n.

## Actually executed verification

The self-contained Python 3 standard-library source `STAGE472B_REPRO.py` passed 14 small parameter configurations, 560 selected complete observer fibers and 2,556 exact class population plus rank/unrank checks. The raw histories were exhaustively enumerated *inside each selected fiber* and independently grouped by V_t. A larger locally executed audit harness checked 755 fibers and 3,021 classes across 14 configurations; it also compared complete legal 12-signed-direction future trees for 80 history pairs (12 same-repair, 68 differing-repair), visiting 10,593 comparison states. All assertions passed. These future tests audit Stage469 semantics on the stated finite inputs.

Large original complete-observer fiber: P=A^35, Q has `AA=3,AB=BA=14,AC=CA=12`, m=35,n=56,K=18. Exact *total* population is `11,154,643,500` for every t. Results:

| t | h=n-t | exact supported keys | prefix states | suffix cache states |
|---:|---:|---:|---:|---:|
| 34 | 22 | 281,600 | 53 | 2,649 |
| 35 | 21 | 168,960 | 30 | 1,928 |
| 36 | 20 | 168,960 | 48 | 2,989 |
| 37 | 19 | 168,960 | 102 | 5,846 |
| 56 | 0 | 5 | 5 | 5 |

No large-history enumeration was used. All five cases passed representative rank/unrank probes. The t=56 result also agrees with Stage470-B's five masses `531173500,858049500,735471000,4862280500,4167669000`.

**Research reuse:** EXTEND_EXISTING_TOOL — positive integer BRC prefix/signature and deterministic support DP from Stage471, with finite hidden tag repair. The result concerns ordered-history combinatorics and complete future observers; it asserts no physical phase or residual calibration.

## Next problem

Stage473-B: test P POP<=2, APPEND<=2 (Q POP<=h, APPEND<=1) under all signed-X6 append directions, locating any newly necessary original Q probes at m-1..m+2. Produce an explicit same-R469 pair with a distinguishing future operation word or a complete sufficient repair theorem, then extend the positive BRC support algorithm. Stage469's semantic proof is independently reviewable; formal native task acceptance is separately governed by actual CLAIM and Driver authority.
