# R708 — X6 Cell 三元覆盖的饱和轴判据与 BRC 隐藏来源律

Date: 2026-11-11 Asia/Shanghai. Mathematical scope: R707 equal-positive-rational-quantum candidate Cell-local triadic decomposition, six native X6 axes, three distinct axes per primitive triple, all tokens individually labeled and their signs/provenance retained. Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS / publication TP2-8B7E13C5904A2D6F1142. Frozen science: a72226e2430ffa4786321ac86e7f0c599d5f0389. R707 source: 877562f8f1affc12016fbd5c35f623d8a27f467b:research_notes/R707_TRIADIC_CELL_CLOSURE_PROOF_20261111.md. This candidate model does not identify its admission rule with the full native TRIADIC_CLOSURE_E.

## Domain and R707 reuse

Take a Cell c in the affine X6 torsor and 3m distinct tokens at c, all having common q>0, with six nonnegative axis multiplicities n=(n_0,...,n_5), sum n_i=3m, and arbitrary attached sign/provenance. A valid decomposition partitions all tokens into unordered triads, each containing three distinct axes. Let D(n) be its number, with D(0)=1. By R707, for H=sum_{i<j<k} x_i*x_j*x_k,

$$D(n)=(\prod_i n_i!/m!) [x^n]H^m.$$

We reuse its independent first-token integer recurrence and retain full source identity when reading signs, ports or a particular path.

## Theorem A — exact feasibility and constructive greedy proof

For all integers m>=0 with sum n_i=3m,

$$\boxed{D(n)>0 \iff \max_i n_i\le m.}$$

Necessary: one triad contains at most one token of each axis, so m triads can hold at most m tokens from any one axis.

Sufficient: induct on m. At m=0, use the empty cover. At m>0 and max n_i<=m, at least three axes are positive because their total is 3m. Choose the three axes with largest counts, select one labeled token on each, and remove that triple. Let S={i:n_i=m}. Since sum n_i=3m, there are at most three saturated axes; the chosen top three include every saturated axis. All unselected axes therefore have n_i<=m-1, and all selected axes after decrement also have n_i-1<=m-1. The remainder sums to 3(m-1), so the induction hypothesis constructs the rest. This greedy procedure outputs a valid labeled cover in m rounds. QED.

With six axes fixed, the number of arithmetic operations is O(m) and the explicit output has m triples; this is not a bit-complexity claim for binary-coded m.

## Theorem B — exact BRC branch weights and support

For any feasible nonzero n, fix two particular labeled visible tokens u,v with distinct axes i,j. Define the saturated set S(n)={a:n_a=m}; for each third axis k different from i,j let

$$W_{ij\to k}(n)=n_k\,D(n-e_i-e_j-e_k),$$

taking W=0 if n_k=0. W is the exact number of full labeled triadic partitions in which u,v are together and the third token has axis k: choose one of the n_k labeled third tokens and partition the remaining 3(m-1) tokens. Every such full partition is counted once. By Theorem A on the remainder,

$$\boxed{W_{ij\to k}(n)>0\iff n_k>0\text{ and }S(n)\subseteq\{i,j,k\}.}$$

Indeed a count equal to m must be decremented once in the first triple; all other axes already have <=m-1, so that condition is both necessary and sufficient. When D(n) equiprobable partitions are represented as positive-weight BRC sources,

$$\Pr(u,v\text{ together and third axis }k)=W_{ij\to k}(n)/D(n).$$

The local eight signed-axis lifts of R707 are thus filtered by the global token inventory, while their exact sign and provenance require the labeled carrier.

## Theorem C — two saturated axes imply branch-count rigidity

For m>=1, if n_a=n_b=m with a!=b then every triple contains one token of each saturated axis and one from their m-token complement. Anchor each triad by its distinct labeled a-token. Independently biject its m labels with the m labeled b-tokens and the m labeled complement tokens. Consequently,

$$\boxed{D(n)=(m!)^2},$$

irrespective of how the other m tokens distribute among the remaining axes. If u and v are chosen fixed tokens from a and b, fixing them together with a third token of axis k leaves two permutations of m-1 objects:

$$\boxed{W_{ab\to k}(n)=n_k((m-1)!)^2}.$$

Therefore

$$\boxed{\Pr(u,v\text{ together})=1/m,\qquad\Pr(k\mid u,v\text{ together})=n_k/m.}$$

These are exact positive-rational BRC kernels in the specified uniform-decomposition ensemble, not signed amplitude cancellation.

## Explicit information-residual counterexample

Let m=3. Compare nA=(3,3,3,0,0,0) and nB=(3,3,1,1,1,0). Both have D=36. Fix labeled visible tokens u on axis0 and v on axis1. Their chance of cohabiting one triad is 1/3 in both cases. In nA the only third-axis branch is k=2 with W=12 and conditional probability 1. In nB the k=2,3,4 branches have W=4 each and conditional probability 1/3 each. Thus (m,D,Pr(u,v together)) is insufficient for a future axis-addressed source query. For nB, a visible token pair on axes 2 and 3 has W=0 for every k: axes 0 and 1 both saturate m and must occupy every triad, leaving no triad containing both axes 2 and 3.

## Exact verification and next unit

The accompanying Python standard-library exact checker independently exercises the R707 first-token recurrence, Theorem A greedy existence, the saturated-axis source-support condition and Theorem C. It exhausts all 1366 six-tuples with 0<=n_i<=3 and sum divisible by 3, including 1135 feasible profiles, 10755 visible-axis pair checks and 390 two-saturated cases. All checks passed with arbitrary-precision integers and Fraction: R708_X6_TRIADIC_SATURATION_BRC_EXACT_PASS. The proof above is general for all m; exhaustive checks cover the stated finite domain.

Next: at the frozen task pin, inspect native V29 PASS/TRANSFER, V39 loop-flow j and the actual X6 Link/Port permitted event; test whether the two example inventories can occur with valid conserved primitive states. Extend the BRC carrier by precisely those Cell/Port/loop source coordinates that a native future update distinguishes. Formal claim, native event verification and independent Driver review remain tracked separately from this author-side proof.