# T6 maximal-p17 order 7 split (3,4): complete exact global mixed-congruence exclusion

Date 2026-11-23 (Asia/Hong_Kong). Original TASK_RESEARCH logical lane: `chatgpt-research-onhour-enterprise-math-20260923`, source attribution `EM-X6-FB6990`, existing public SID `MCP-082892eb480e45dea6d4b9fcc0491034`. Evidence **AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED**. Mother `T6=2332`: OPEN. No current native T6 winning CLAIM, protected semantic PROGRESS, independent review or Result acceptance asserted.

## Frozen model

Input remains `research_tasks/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260909.md` @ `d84bd940cfb093cdc60e569f15cad58772a51dca`, blob `87b3a6f38e9350f7a3f56624b27bff2a7778a439`. Each side has exponent mass <=2331. Retain original full named denominator, sign, repetitions, two individual masses and all `H0,...,H6`.

After cancellation of common named atoms and the existing *author-level* p17-square valuation cancellation lemma, a maximal-p17 valuation-one denominator is `17(r+17q)`, `r=1,...,16`, `q>=0`, cost `289q+17r-1`. Use arbitrary p17-free lower-prime atoms. The global H-observer equalities imply six necessary mixed congruences

```
sum_(r=1..16) u_r * r^(-j)
 + sum_(q>=1,r=1..16) m_(q,r) * (r+17q)^(-j)
  == 0 (mod 17^j),  j=1,2,3,4,5,6.
```

All modular inverses exist. Do not replace these global necessary constraints by equality of the p17-only rational moments.

## Exhaustive computation and argument

Generate *all* vertical order-3 and order-4 named side rosters via positive integer partitions of q and complete nondecreasing residue multisets within repeated q. Discard side rosters exceeding exponent mass 2331. Exactly **1,088** order-three and **6,460** order-four rosters remain. Their Cartesian product is **7,028,480** oriented pairs. **2,398,208** share a named vertical atom across sides and reduce to a lower primitive vertical order. The remaining **4,630,272** primitive pairs are the entire split (3,4) domain.

The q0 signed completion vector is a full 16-dimensional integer vector, with weights `W=diag(16,33,...,271)` and its full saturated homogeneous lattice basis from pinned p17 source cert Git blob `d9ac014355a6a1058cc8a0cf2141a01082628881`. Its index is `17^21`; exact modular successive lifting supplies an affine representative, and all solutions are that representative plus an integral combination of the 16 basis rows.

For vertical mass `c_+` and `c_-`, the true two separate signed-side budgets imply the necessary weighted spherical inequality

```
||W*u||² <= (2331-c_+)²+(2331-c_-)² = R².
```

Here the maximum possible `R²=3,439,985`. The exact minimum squared Gram–Schmidt diagonal of the weighted lattice is the fraction

```
8350069911612335617606677214061177705401058080646556447012234889468081355909
/480650972868542992444263969893692042421717754534280313801217347854273
```

(about 17,372,418.62). Thus `R²<Dmin` uniformly. At every reverse GS coefficient, only exact floor and ceiling of its affine center are possible. The exact `Fraction` solver exhaustively traverses both, pruning only when the partial rational squared norm exceeds `R²`. A complete original-valid candidate must produce a complete leaf in this search, making zero-leaf exclusion rigorous.

The standalone Python/SymPy exact implementation actually executed the complete order-three side in **34 disjoint ranges of 32 states**, against the full order-four roster in each range. All 34 local result JSON files were created, their nonoverlapping ranges were checked to cover `[0,1088)`, and SHA-256 checksums of each appear in the attached published certificate. Consolidated counts:

| Exact statistic | Value |
| --- | ---: |
| Raw named side pairs | 7,028,480 |
| Shared vertical atom pairs | 2,398,208 |
| Primitive pairs after cancellation | 4,630,272 |
| Exact GS recursion nodes | 9,623,589 |
| Full necessary weighted-sphere leaves | **0** |
| Genuine two-side-budget q0 completions | **0** |

The compact GitHub checker `research_checks/T6_P17_Q7_SPLIT3_4_MIXED_AFFINE_CHECK_20261123_0500.py` uses the existing published pinned q5 saturated lattice and original parameters; it was **not separately executed** after publication. The standalone chunked computation was executed; this is author evidence rather than an independent mathematical review.

**Proposition (author exact finite, split scope).** There exists no primitive maximal-p17 valuation-one vertical-order-seven signed pair of split (3,4), with individual exponent mass <=2331 and all six globally necessary mixed 17-adic reciprocal congruences, regardless of the lower-prime completion.

## Coverage of order seven and continuation

Other three q7 split results are already preserved as independently authored exact units: (0,7), (1,6), and (2,5), each with zero full necessary weighted-sphere leaf. This unit completes **all four unordered q7 vertical split cases at author exact finite evidence strength**. It does **not** independently admit the proofs, eliminate every valuation assumption without the cited p17-square author lemma, or close the global T6 threshold.

The next minimal remaining maximal-p17 valuation-one case is vertical total order **8**. Start with split (0,8), then (1,7), etc, recomputing exact complete named rosters, respecting the frozen mass cap and any actual current owner/Source task route. Preserve the low-prime and H0-observer obligations. If a full modular lattice survivor appears, keep its signed named atoms and independently test original two budgets and lower-prime completion.

At last exact control read, original T6 Task request `onhour-20261123-0315-t6-current-task-read-v1` had SUCCEEDED/error=null, owner unassigned and `execution_authorized=false`. Portable GitHub evidence and Source Activity are not an authenticated winning CLAIM, run or Native PROGRESS.
