# R5 D14 — universal 0–4 error plateau for every 14-label paired augmentation

Date: 2026-11-20 (Asia/Shanghai). Status: **AUTHOR_EXACT_FINITE_CHECKED / PARTIAL_INDEPENDENT_IMPLEMENTATION_CHECK / NOT_REVIEWED**. Scientific object: the original **frozen scalar R5 minimax observation game**, not a native BRC/X6 theorem. No shared TASK CLAIM, Result or independent project Review is asserted.

## Frozen statement

Let (W=(0,16,32,48,1,64,17,80,18,24,34,82)). The label universe is (\{0,\ldots,255\}), and (τ=58182461585441404127941754879). There are 101 priced queries (k=214,\ldots,314), with physical cost (k) and the closed intervals ( |2y-2N_h(k)|\le\tau ). Centers are frozen in `EXACT_R5_ALL_101_BUDGETS.json`, SHA-256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`; science pin `awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551`.

**Theorem (finite exact computation).** For every unordered pair (\{u,v\}\subseteq\{0,\ldots,255\}\setminus W) of distinct labels, and for every integer (0\le f\le4) of unflagged adversarial errors,

[
\boxed{V_f(W\cup\{u,v\})=735+950f}.
]

There are exactly `C(244,2)=29,646` named pairs and `1,906` distinct **price-aware joint maximal-support** signatures; values for f=0,1,2,3,4 are respectively `735,1685,2635,3585,4535`. The result does not decide whether any unresolved pair has (V_8>8335); the pre-existing full 256-name bound remains `8335 <= C*_8 <= 8343`.

## Exact endpoint/Bellman reduction

For each query k and each of 14 labels, use doubled left endpoint `2*N_h(k)-tau`; the support at that endpoint is the bitmask of all labels j with `abs(2*N_j(k)-(2*N_h(k)-tau))<=tau`. For a finite family of closed intervals, every inclusion-maximal common support is attained at one of these endpoints. Remove proper-subset supports. For identical maximal-support families retain only the cheapest physical query. This step preserves the original joint 14-label observer, not 12+2 independent marginal observations.

For fixed f, cap mismatch counts e_i at f+1, and retain a label as live iff e_i<=f. Values are zero if at most one label is live. Otherwise

[
V_f(e)=\min_{k:\mathrm{nonstall}}\bigl[k+\max_{S\in\mathcal F_k} V_f(\min(f+1,e+1_{i\notin S}))\bigr].
]

An action is nonstalling when no maximal support contains all live labels. Because the physical cost is positive, an adversarial unchanged-live branch makes a stalling action useless. Each remaining transition strictly increases a live mismatch coordinate, so exact finite memoized Bellman recursion terminates. A branch with no live labels costs zero thereafter.

## Complete low-budget computation and stronger f4 certificate

For **each of all 1906 signatures**, exact integer DP was run separately at f=0,1,2,3, all giving `735+950*f`. Reproduction table: `D14_F0_F3_1906.csv` (67,914 bytes; SHA256 `0ab8429ec26cdffbf461527fc6185521acf83e43c9e4398fe8ea6419fb99beea`).

For f=4 we use the established price-aware static simulation preorder from predecessor `enterprise-math@6c23d330d900a6bf29451832fb0e05e4ad777a2f`, and the maximal order-basis theorem at `enterprise-math@a3595f6855c7ad94a1cc0a1b7219db2f160c305f`. Here (i\preceq_D j) means: for every priced query of j, i has a no-more-expensive query whose each maximal support is contained in some support of that query of j, allowing swap of the two added-label positions. Strategy simulation proves (V_f(i)\le V_f(j)) for every f.

The already certified plateau covers 1265 of the 1906 classes through 50 distinct original witness references and six later added references. The remaining 641 classes form 468 preorder equivalence components, with **278 maximal components**. Thus exactly 50+6+278=**334** distinct reference signatures provide a static-preorder covering set for *all* 1906 classes. The present round ran a **fresh f4 exact Bellman solve** on all 334 references, each giving `4535`. The root ledger `D14_F4_ROOTS_334.csv` has SHA256 `e1c075755e978829933f45b0f0dc97541ac0ab09858a15ec5ee171d69429d8d6`. The roots have priced-action counts: 221 with 7, 3 with 8 and 110 with 9; the 334 root solves visited 26,147,116 nonterminal states total (separately counted) and at most 210,514 in any one root. The independently rechecked pinned 1906×1906 preorder matrix has 38,127 directed entries and SHA256 `c5c7c38b678aa5e3830e05895fc59f781bf72f926e5b3c19ea9aeeb262776fa6`.

For each class i, matrix coverage gives an exact f4-certified root j with (i\preceq_D j). Hence (V_4(i)\le4535). The original 12-label W is a subproblem of each 14-label model and has the predecessor's exact (V_4(W)=4535), giving the reverse bound. Therefore (V_4(i)=4535) for all 1906 classes, without spending 1906 full f4 root solves. This is a **complete certificate in the frozen model**, conditional only on the predecessor matrix correctness and the previously validated W baseline; it is not an asserted direct per-class f4 DP.

## Cross-checks, scope and next question

Python code reconstructing all joint masks directly from frozen integer centers, without consuming the C++ adjacency table, independently checked ten selected (class,f) entries: three f4 roots (including one unresolved nine-action class), two f3, two f2, two f1 and one f0. The separate implementation is author-run, not third-party independent review. All reported DP operations use integer arithmetic; no numerical tolerance or floating-point Bellman choices occur.

**Not solved:** f=5 for the 641 previously f8-unresolved classes, any of the 278 maximal f8 roots, or a native BRC/X6 observer-preserving transfer. A useful next step is to solve f5 on the same preorder-maximal root basis (plus already certified references), then advance towards f8 by exact state compression or shared strategy simulation. Earlier f8 bound `8335..8343` is unchanged.

Researcher attribution: prior R5 lane `EM-DIRECT-4C3E47`; activity `RA-F2257922D00B2FE4C4818DBD` is historical provenance, not evidence of a new formal CLAIM/RUN. All evidence in the companion local reproduction ZIP is SHA-256 checked. GitHub Source publication, portable Activity and global journal are separate status scopes.
