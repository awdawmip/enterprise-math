# R730 — Explicit uniform BRC named-holonomy mixing from exact 90-state projective diameters

Date: 2026-11-12 (Asia/Shanghai). Derived author-side continuation of R728/R729. Parent task `RS-X6-TRIADIC-CLOSURE-DYNAMICS`; frozen task-science pin `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. Predecessor source: R729 commit `5f1010b9142c297f59419ed544adb5bf397b76d5`. The five-accessible-label carrier is a derived subcarrier within P000's six native spatial axes. It preserves positive source-distinct BRC path multiplicities, V17 slot transport and cyclic nonbacktracking (including the seam).

## Proposition: a quantitative all-length mixing certificate

Use the R725/R729 optimal 15-arc representatives, with original 60-arc lexicographic masks A=`211733226574` and B=`5363347296468`. Let `L_X` be the 90-by-90 nonnegative integer lifted directed-edge × ordered-frame transfer of R728/R729. The standalone verifier reconstructs `L_X` from the exact arcs and slot law, and proves by integer multiplication and exhaustive rational cross-product comparisons that `M_X=L_X^9` is entrywise positive and its **exact maximal matrix cross ratio** is

\[
K_X=\max_{i,j,k,\ell}\frac{(M_X)_{ik}(M_X)_{j\ell}}{(M_X)_{i\ell}(M_X)_{jk}},\qquad
\boxed{K_A=25,\quad K_B=21}.
\]

The checker examines all 4005 unordered pairs of 90 rows, maximizing/minimizing their 90 exact column ratios; reversing a row pair does not change the maximal cross ratio. Exact attaining witnesses (0-based row/column indices of `L^9`):

- A: rows 12,14 and columns 66,68 have entries `5,1,1,5`, yielding ratio 25.
- B: rows 30,44 and columns 29,48 have entries `6,2,1,7`, yielding ratio 21.

The entire ninth powers each contain 8100 positive entries, with minimum 1 and maximum 18. Their integer entry sums are 58764 (A) and 61080 (B); `L^8` still contains 108 (A) and 72 (B) zero entries. The cross-ratio calculation improves substantially upon the crude common entry bound `K<=18^2=324`.

For positive 90-vectors define Hilbert's projective metric

\[
d_H(u,v)=\log\max_i(u_i/v_i)-\log\min_i(u_i/v_i).
\]

The classical Birkhoff–Hopf contraction theorem for positive matrices with projective diameter `log(K)` gives, for **row-vector** multiplication by `M_X`, the contraction factor
\[
q_X=\tanh\!\left({\log K_X\over4}\right)
={\sqrt{K_X}-1\over\sqrt{K_X}+1};
\qquad
\boxed{q_A=2/3,\quad q_B={\sqrt{21}-1\over\sqrt{21}+1}<2/3}.
\]
Here transposing the matrix to use the usual column-vector theorem preserves its cross-ratio maximum. The elementary diameter bound gives `d_H(uM_X,vM_X)<=log K_X` even for arbitrary nonzero *nonnegative* row vectors `u,v`; subsequent blocks contract by `q_X`.

### Rooted closed histories and six named final frames

Let `a_m^X(h)` count positive rooted cyclic-nonbacktracking closed histories of length `m`, rooted at triad 012 and ending in the named slot frame `h in S3`, as in R729. Let `T_m^X=sum_h a_m^X(h)`. For `m>=10`, set `k=floor((m-10)/9)`. Then **for both X=A,B and all six named h**,

\[
\boxed{\left|\frac{6a_m^X(h)}{T_m^X}-1\right|
\le \exp\!\left((\log K_X)q_X^k\right)-1.}
\]

**Proof of projection step.** Fix one initial permitted arc `f` leaving root 012. Its initial 90-vector is a basis vector `u_f` at the resulting V17 frame. Let `\bar u_f` be its average over the six right deck permutations (all six frame variants on the same arc). The lift commutes with this deck action because each transition applies its slot permutation on the *left*. Thus `\bar u_fL_X^{m-1}` is uniform across all six final frames for every last arc. For `m-1>=9`, both evolved vectors are strictly positive. Birkhoff's diameter and contraction estimates yield
\[
d_H(u_f L_X^{m-1},\bar u_f L_X^{m-1})\le(\log K_X)q_X^{\lfloor(m-10)/9\rfloor}.
\]
Nonnegative intermediate `L^r`, `0<=r<9`, cannot expand Hilbert distance: the verifier checks that no row or column of `L` is identically zero.

The two evolved vectors have equal total mass on **each last-arc fiber** when summed over all six frames, because `\bar u_f` is exactly the deck average. Hence their coordinatewise ratios straddle 1, and projective distance at most `d` implies all coordinate ratios lie in `[e^{-d},e^{d}]`. The seam restriction selects last arcs only by their triad endpoints, independent of the slot permutation. For the averaged vector each named-frame count equals one-sixth of its seam-legal total; summing over root-first arcs `f` preserves the same bound and total. This proves the displayed inequality. It is a uniform, explicit exponential rate rather than only an existence statement about a spectral gap.

### Concrete fully certified milestones

For every named frame, the relative discrepancy `|6 a_m(h)/T_m -1|` is strictly less than 10% for all `m>=91` (A) and `m>=82` (B); it is strictly less than 1% for all `m>=145` (A) and `m>=127` (B). These are conservative *sufficient* thresholds, not claimed optimal.

The inequalities can be certified without floating point: use `log 25 < 13/4`, `log 21 < 61/20`, `q_B < 9/14` (because `sqrt(21)<23/5`), and `log(1+epsilon)>epsilon/(1+epsilon)`. The required exact rational checks are
`(13/4)(2/3)^9 < 1/11`,
`(13/4)(2/3)^15 < 1/101`,
`(61/20)(9/14)^8 < 1/11`,
`(61/20)(9/14)^13 < 1/101`.
Monotonicity extends each check to all longer lengths.

The derivation invokes the standard positive-matrix Birkhoff formula, not a numerical theorem fit: J. E. Carroll, *Birkhoff's contraction coefficient*, Linear Algebra and its Applications **389** (2004), 227–234, DOI: https://doi.org/10.1016/j.laa.2004.02.039. See also Lawson and Lim, *A Birkhoff Contraction Formula with Applications to Riccati Equations*, SIAM J. Control Optim. **46** (2007), DOI: https://doi.org/10.1137/050637637.

## Reproduction, scope and next scientific unit

Execute `node R730_BRC_PROJECTIVE_MIXING_VERIFY.js > R730_BRC_PROJECTIVE_MIXING_RESULTS.json`. Node with standard BigInt support is sufficient; the largest ninth-power entry is 18 and every exact cross-product comparison fits safe integers. The code reconstructs the 60 original arcs, filters both actual masks, rebuilds all 90 lifted states and the 8th/9th powers, checks positivity and exact extremal ratios, and serializes the complete finite witness summary. The accompanying JSON is a reproducible finite certificate; the infinite-length conclusion uses the explicitly cited Birkhoff theorem and the symmetry/terminal-projection argument above.

This calculation is for the derived positive BRC 15-arc model with uniform counting of source-distinct histories. It establishes an effective quantitative mixing law for that precise observer, not an assertion of physical event probabilities. The frozen P000 ontology and original task science remain unchanged. Author-side publication is distinct from Source CLAIM/Result and independent mathematical review.

**Next discriminating unit:** seek a real typed V29 Link/Port, Cell, signed-axis and event-time witness (or an exact obstruction) for a selected abstract 15-arc carrier, and then test whether its executable transfer retains strict block positivity and what projective cross ratio applies. A model whose actual event permissions differ must recompute its own transition matrix and bound.
