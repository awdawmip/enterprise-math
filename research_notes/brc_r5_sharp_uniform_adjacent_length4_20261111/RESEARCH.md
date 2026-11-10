# R5 — Sharp uniform four-circuit bound for every adjacent Blackwell transfer direction

Date: 2026-11-11 (Asia/Shanghai). Status: author-side exact mathematical proof with executed rational validation; independent review and formal Source Result pending.

Scientific pins remain frozen: GLOBAL `a01383f825ef9d43b4b754254303298c64041568`; EM `86149263e38c22292c9def1e0f69092efa1be77e`. Reused lineage: PR #2017 (six-arc residual dictionary), #2021 (observer coordinates), #2026 (vertex adjacency), #2034 (three-atom edge), #2038 (four-atom edge). Current behavioral controls were read separately. P000 remains unchanged.

## Sharp theorem — the entire frozen 30-arc Blackwell model

Let the seven pairwise distinct likelihood ratios be
$$
(r_0,\ldots,r_6)=(2,10,15,20,25,30,38)/20.
$$
The allowed arcs are all $(i,j)$ with $i=0,\ldots,6$ and $j\in J=\{1,2,3,5\}$, plus the singleton-source arcs $(0,0)$ and $(6,6)$: thirty arcs in total. The $21\times30$ matrix $C$ records seven target marginal masses, seven source marginal masses and seven source first likelihood-ratio moments.

For **any** $b\in\mathbb R^{21}$ with nonempty transport fiber
$$
F_b=\{E\in\mathbb R_{\ge0}^{30}: CE=b\},
$$
and **any distinct adjacent vertices** $V,W$ of this fiber, let $d=W-V$. Define $L(d)$ to be the minimum number of scaled signed six-arc $K_{2,3}$ residual atoms $H(j,k;a,b,c)$ whose sum is $d$; coefficients may be arbitrary real numbers. Then
$$
\boxed{L(d)\le4.}
$$
The constant is sharp. The exact physically lawful fiber and adjacent vertices from PR #2038 satisfy $L(W-V)=4$. Thus the **global maximum of the minimum six-arc residual word length over all adjacent vertex directions of this fixed physical fiber is exactly four**.

## Proof

**1. Forced source rows and per-row moment conservation.** For every $h\in\ker C$, singleton-source constraints give $h_{00}=h_{66}=0$. Each nonzero row $j\in J$ satisfies
$$
\sum_i h_{ij}=0,\qquad \sum_i r_i h_{ij}=0.
$$
Since the ratios are distinct, every nonzero source row has at least three nonzero targets. Let $k\in\{2,3,4\}$ denote the number of such rows.

**2. A polytope edge direction has circuit-minimal support.** Write $U=\operatorname{supp}(V)\cup\operatorname{supp}(W)$. Their midpoint is positive exactly on $U$; therefore the minimal face containing the edge has dimension
$$
|U|-\operatorname{rank}(C_U)=1.
$$
Hence $\dim\ker C_U=1$. As $d\ne0$ belongs to this kernel, no nonzero $h\in\ker C$ can be supported strictly inside $\operatorname{supp}(d)$. Thus $S=\operatorname{supp}(d)$ is an inclusion-minimal dependent column set. If $D_k$ is the full set of arcs on the $k$ active source rows, then
$$
|S|\le\operatorname{rank}(C_{D_k})+1.
$$

**3. Exact rank of the restricted observer.** On $k\ge2$ complete source rows and seven targets, there are $7+2k$ target/source moment functionals. Every dependency has coefficients $\alpha_i,\beta_j,\gamma_j$ satisfying
$$
\alpha_i+\beta_j+\gamma_jr_i=0
\qquad\text{for all }i,j.
$$
Subtracting the equations for any two source rows and using two distinct ratios forces the $\beta_j$ to be constant over $j$ and the $\gamma_j$ to be constant over $j$. The dependency space therefore has dimension exactly two. Consequently
$$
\operatorname{rank}(C_{D_k})=7+2k-2=2k+5,
\qquad |S|\le 2k+6.
$$

**4. Constructive decomposition using a reference source row.** Put $s_j=|\operatorname{supp}(d_{\bullet j})|\ge3$ for the active rows and choose a reference row $p$ maximizing $s_j$. In each other row $j\ne p$, choose two target anchors $a,b$ in its support. For every target $c$ outside these anchors, the coefficient $d_{cj}$ uniquely determines a three-target vector on $\{a,b,c\}$ with both zero total mass and zero first ratio moment. Summing these $s_j-2$ vectors recovers the entire row $d_{\bullet j}$.

For each such three-target vector, place its negative in the reference row $p$. Each pair is a scaled $K_{2,3}$ atom $H(j,p;a,b,c)$. The target marginal equalities force the remaining reference row to match exactly. Therefore
$$
L(d)\le \sum_{j\ne p}(s_j-2)
=|S|-s_p-2(k-1)
\le |S|-\left\lceil|S|/k\right\rceil-2(k-1).
$$
For $k=4$, $|S|\le14$ and $s_p\ge\lceil |S|/4\rceil$, so $L(d)\le14-4-6=4$. For $k=3$, $|S|\le12$, so $L(d)\le12-4-4=4$. For $k=2$, the two source rows are opposite by target conservation. Circuit minimality then forces exactly three targets in each, making $d$ one $K_{2,3}$ atom: $L(d)=1$. One active source row cannot carry a nonzero kernel vector. This proves the upper bound.

**5. Exact sharpness witness.** PR #2038 contains rational adjacent $15$-support endpoints $V,W$ with $14$-supported direction $d$, a $16$-arc support union of rank $15$, and an explicit four-atom decomposition. Its structural obstruction excludes any three-atom representation, even with arbitrary real coefficients: the only two possible three-atom source-pair arrangements leave five nonzero targets in a row that one remaining atom could cover on at most three targets. The accompanying checker reproduces the vertices, $C$-equalities, rank, four-atom identity and both obstruction cases. Thus $L(d)=4$, proving sharpness.

## Generalization (reusable independent lemma)

For a complete $k$-source, $n$-target mass-plus-first-moment observer with pairwise distinct target ratios, the same proof gives, for an edge direction with $k\ge3$ active source rows,
$$
L(d)\le n-1-\left\lceil\frac{n-1}{k}\right\rceil.
$$
Indeed the restricted observer rank is $n+2k-2$, the circuit support has size at most $n+2k-1$, and anchoring the other rows to the largest row gives the stated count. With two active source rows each edge direction is a single three-target $K_{2,3}$ atom. In the frozen $n=7$, $k\le4$ model the upper bound specializes to four.

## Validation, BRC scope, and continuation

The saved `VERIFY_SHARP_BOUND.py` (SymPy exact rationals) checks all eleven subsets of two, three, and four active source rows; all 210 signed port-labeled six-arc atoms; the sharpness witness's $15$-support endpoints; equality of observed values; the $16$-arc union and its rank $15$; and the two-case lower-bound obstruction. `EXACT_OUTPUT.txt` is the actual executed stdout transcript, byte-matched to the saved Git blob.

BRC is applied to the labeled transfer-branch mass carrier. The $K_{2,3}$ atoms retain the unobserved branch residual under fixed marginals and first moments; the nonnegative fiber identifies which composites occur as extreme transfer directions. This theorem concerns the pinned auxiliary Blackwell model.

**Next exact question:** classify which adjacent edges attain length four and count their incidence in the fixed physical fiber's vertex-adjacency graph. A search for length-five adjacent rays in this model is now closed by the sharp universal bound. The separate mother objective concerning low-support transport and richer BRC observers remains open.
