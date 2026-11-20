# R5: exact nonadaptive low-excess spectrum (0–212), sharp threshold

Date: 2026-11-20. Author-side mathematical proof + exact frozen finite certificate; NOT_REVIEWED. Lane R5, scalar closed-interval fixed-query observer, NOT native X6/BRC admission.

## Frozen inputs and validated predecessor

Science pin: `awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551`. Integer-center input: `EXACT_R5_ALL_101_BUDGETS.json`, SHA-256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`; tau=58182461585441404127941754879. Use 256 named hypotheses, prices k=214..314, at most f arbitrary unflagged replacements and e visibly flagged erasures on paid observation slots. All queries are chosen before any reading. Set m=2f+e+1>=1.

The prior finite checker, re-run against unchanged SHA-matched input, exhaustively enumerates 32,640 hypothesis pairs, 101 budgets, 53 separation masks and five inclusion-minimal masks:

- S1={214,215,216,217,218}
- S2={214,216,217,218,219,220,221}
- S3={215,216,217,218,219,220,221}
- S4={223,...,290}
- S5={296,...,312}.

Pairwise robustness is equivalent to at least m occurrences in each separating set, hence precisely the five inequalities A_i>=m; no pairwise constraints are discarded. Previous optimum is C=735m uniquely at m copies of each 216, 223, 296. The current result extends its rigidity theorem; it does not independently accept that previous theorem.

## Theorem — exact near-optimal combinatorial spectrum

For every f,e>=0 and integer D between 0 and 212, all uniquely decodable **unordered** nonadaptive query multisets of cost 735m+D have exactly:

* m occurrences from E0={216,217,218};
* m occurrences from M={223,224,...,290};
* m occurrences from L={296,297,...,312};
* no other query prices.

Conversely every such multiset satisfies the 256-hypothesis mixed-fault decoding requirements. Their exact number is the coefficient

`a_m(D) = [q^D] [m+2 choose 2]_q [m+67 choose 67]_q [m+16 choose 16]_q`,

where [n choose r]_q is the Gaussian binomial polynomial. The equality applies coefficientwise for 0<=D<=212, not to the whole higher-degree polynomial.

The threshold is **sharp**: at D=213, replacing one 216 with BOTH 214 and 215 (leaving all other m copies unchanged) yields a valid design outside the three listed blocks. Its cost increases by 214+215-216=213. Thus 212 is the maximal uniform interval in which the three-block characterization holds, for every m>=1.

## Complete proof

The five constraints split by physical query prices into early E={214,...,221} (S1,S2,S3), middle M={223,...,290} (S4), and late L={296,...,312} (S5). All prices outside E∪M∪L occur in none of these five minimal separating sets; their least price is 222. Removing one such query preserves feasibility, and the remainder costs >=735m by the predecessor lower bound. Any feasible schedule using an outside query thus costs >=735m+222 and is excluded by D<=212.

The middle and late counts must be >=m. Their component costs are >=223m and >=296m. Having more than m middle occurrences adds >=223 above their base; having more than m late occurrences adds >=296 above base. We next prove every feasible early schedule costs >=216m, so for D<=212 both middle and late counts are exactly m.

Let c be the number of early queries in T={216,217,218}, a the number of 214, b the number of 215, d the combined number of 219,220,221. The three early constraints read a+b+c>=m, a+c+d>=m, b+c+d>=m. Early cost is >=216c+214a+215b+219d.

If c>m, excess relative to 216m is >=216. If c=m and any partial-incidence query occurs, excess is >=214. Suppose c<m and put r=m-c>=1. Then a+b>=r, a+d>=r, b+d>=r. For r=1, at least two distinct types must occur, and their cheapest possible combination is a=b=1 with cost 214+215=429; excess over one 216 is 213. For r=2, a+b+d>=3. If exactly 3, all three pairwise inequalities force a=b=d=1, costing 214+215+219=648, excess 648−2·216=216. If at least 4 partial queries, excess >=4·214−2·216=424. For r>=3, the sum of inequalities yields a+b+d>=ceil(3r/2), and excess is >=214·ceil(3r/2)−216r >=105r>=315. Consequently any early multiset other than exactly m occurrences of T has excess >=213. In all cases early component cost >=216m.

Therefore total costs at most 735m+212 force exactly m queries in each T,M,L and none elsewhere. In each block, subtract the base query price. The increments are respectively 0..2, 0..67, 0..16. A multiset of size m from increments 0..r has generating polynomial [m+r choose r]_q. The three independent blocks multiply, giving the claimed exact coefficient formula.

Finally, the advertised 214+215 replacement has early A1=m+1, A2=A3=m and does not change A4,A5, so is valid at D=213. This proves maximality. QED.

## Small-excess consequences

a_m(0)=1 and a_m(1)=3 for every m>=1. At D=2, a_1(2)=6 and a_m(2)=9 for m>=2: three single price+2 substitutions, three cross-block pairs of +1 substitutions and (when m>=2) three same-block pairs of +1 substitutions. These are counts of **unordered** multisets, not query sequences.

This is a precisely typed, nonadaptive observation-preserving quotient of query *supports*: equality of the three full-incidence blocks is used only for the declared fixed-query decoder and fault horizon. No path/provenance loss is certified for later native X6 operations.

## Evidence and residual question

Source checker `VERIFY_R5_MIXED_ERASURE_RIGIDITY.py` was re-run on the archived source and passed frozen SHA, 32,640 pair masks, five minimal patterns and all 101 dual slacks. Independent author program `VERIFY_R5_LOW_EXCESS_212.py` recomputes dual incidence, r=1,2 early minima, DP Gaussian coefficients and small-excess direct enumeration for m=1,2,3,17. Every operation is exact integer arithmetic; all-m proof is symbolic. The scientific input is a previously retained byte-for-byte frozen input, not a live newly repinned GitHub science source. Review remains NOT_REVIEWED; no CLAIM, Result, admission or native X6/BRC transfer is claimed.

Next questions: classify beyond D=212 including partial early masks and redundant paid queries, with complete rational generating functions; separately return to the original adaptive f=8 gap (reported prior bound 8335<=C8*<=8343) using an actual decision-tree or Bellman certificate. This theorem does not alter that adaptive interval.
