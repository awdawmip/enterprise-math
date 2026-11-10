# R5 — Sharp uniform four-circuit bound for every adjacent Blackwell transfer direction

Date: 2026-11-11 (Asia/Shanghai). Status: author-side exact mathematical proof and executable rational verification; formal Source Result and independent mathematical review pending.

Frozen scientific inputs (not rebased): GLOBAL `a01383f825ef9d43b4b754254303298c64041568`; EM `86149263e38c22292c9def1e0f69092efa1be77e`. Source lineage: PRs #2017 (210 six-arc circuits), #2021 (observer coordinates), #2026 (vertex adjacency), #2034 (length-three edge), #2038 (exact length-four edge). Current governing behavior read separately from canonical main; P000 is unchanged.

## Theorem (sharp, entire frozen model)

Let (r_i=(2,10,15,20,25,30,38)_i/20), (i=0,...,6), and let (D) consist of the 28 arcs ((i,j)) for (j\in J=\{1,2,3,5\}), (i=0,...,6), and the forced arcs ((0,0),(6,6)). Let (C\in\mathbb Q^{21\times30}) observe target marginals (sum_j E_{ij}), source marginals (sum_iE_{ij}), and source first likelihood-ratio moments (sum_i r_iE_{ij}). Fix **any** (b\in\mathbb R^{21}) for which the Blackwell transfer fiber (F_b=\{E\ge0:CE=b\}) is nonempty.

For any distinct adjacent vertices (V,W\in F_b), put (d=W-V). Let (L(d)) be the least number of scaled signed six-arc (K_{2,3}) residual atoms (H(j,k;a,b,c)) required to represent (d), with arbitrary real coefficients. Then

[
\boxed{L(d)\le4.}
]

The constant four is attained by the rational, physically valid fixed-fiber adjacent pair from PR #2038, reproduced in the exact checker below. In particular, **the maximum minimum (K_{2,3}) word length among all adjacent vertex directions in that pinned physical fiber equals four.** This closes the proposed search for an adjacent ray of length at least five in this model.

## Proof

**(1) Two forced rows vanish from every residual.** For every (h\in\ker C), the source marginal constraints on singleton rows (j=0,6) give (h_{00}=h_{66}=0). Every nonzero residual is carried by the four complete source rows (J). In each active row (j\in J),

[
\sum_i h_{ij}=0,\qquad \sum_i r_i h_{ij}=0.
]

The ratios are pairwise distinct, so a nonzero row has at least three nonzero targets.

**(2) Each polytope edge direction has inclusion-minimal dependent column support.** Let (U=\operatorname{supp}(V)\cup\operatorname{supp}(W)). The midpoint of the two endpoints is positive on precisely (U), so the minimal face of (F_b) containing the edge has dimension (|U|-\operatorname{rank}(C_U)=1). In particular, \(\ker C_U\) is one-dimensional. Any kernel vector supported strictly inside \(\operatorname{supp}(d)\subseteq U\) would contradict that one-dimensionality. Thus (d) has circuit-minimal support (S), and (|S|\le\operatorname{rank}(C_{D_k})+1), where (D_k) is the set of all arcs on the (k) source rows active in (d).

**(3) Exact rank of a (k)-row observer.** For (k\ge2) complete source rows and seven distinct target ratios, the observer consists of seven target marginals plus two source moment functionals per row, with exactly two dependencies. Indeed any row-relation has the form (α_i+β_j+γ_jr_i=0) for all targets (i) and active sources (j); subtraction between two source rows forces all β values equal and all γ values equal, because the ratios are distinct. Hence

[
\operatorname{rank}(C_{D_k})=7+2k-2=2k+5,
\qquad |S|\le 2k+6.
]

**(4) Explicit recovery by a star of six-arc atoms.** Write (s_j=|\operatorname{supp}(d_{\bullet j})|\ge3) for each active source row. Select a reference row (p) with maximum (s_p). For every other row (j\ne p), choose two distinct target anchors (a,b) in its support. Each of the remaining (s_j-2) target coordinates determines a unique three-target zero-sum/zero-first-moment vector; these vectors sum to the original row (d_{\bullet j}). Pair each such vector in source row (j) with its negative in source row (p). These are precisely scaled (H(j,p;a,b,c)) atoms. Target marginal conservation fixes row (p) automatically. Consequently

[
L(d)\le \sum_{j\ne p}(s_j-2)
=|S|-s_p-2(k-1)
\le |S|-\lceil |S|/k\rceil-2(k-1).
]

If (k=4), use (|S|\le14) to obtain (L(d)\le14-4-6=4). If (k=3), use (|S|\le12) to obtain (L(d)\le12-4-4=4). If (k=2), circuit minimality forces exactly three target positions in the two opposite rows, so (d) itself is one (K_{2,3}) atom and (L(d)=1). No nonzero kernel vector can have (k=1). This proves the uniform bound.

**(5) Sharpness.** PR #2038 supplies rational adjacent endpoints (V,W) with a fourteen-supported direction (d) and an exact four-atom identity. Its structural two-case proof excludes every three-atom representation (arbitrary real coefficients); the attached checker rebuilds the same endpoint, atom identity, and exhaustive two-case residual-support obstruction. Hence (L(d)=4).

## More general reusable statement

For the complete (k\)-source, (n\)-target mass-plus-first-moment observer with pairwise distinct target ratios, each edge direction admits the bound

[
L(d)\le n-1-\left\lceil\frac{n-1}{k}\right\rceil
]

when (k\ge3) active source rows and (n\ge3). This follows from rank (n+2k-2), circuit-size bound (n+2k-1), and the same anchored row decomposition; for (k=2) every edge direction is one atom. The specific (n=7,k\le4) restriction gives the sharp constant four.

## Verification, semantics, and next work

`VERIFY_SHARP_BOUND.py` uses exact SymPy rationals; it checks all eleven choices of two, three or four active source rows, the 210 dictionary atoms, the fourteen-supported previous sharpness witness, its positive neighboring endpoints and union support rank, plus the three-atom obstruction. `EXACT_OUTPUT.txt` is the actual local execution transcript. Finite checks support the exact input/witness, while the proof of the universal upper bound is the mathematical rank/circuit/decomposition argument above.

BRC reuse: the thirty branch-labeled transfer masses retain the hidden residual fiber; the (K_{2,3}) dictionary is the exact branch-residual carrier, and the nonnegative edge relation selects its extreme observable-invariant motions. This is a statement about the frozen auxiliary Blackwell observer, not a promotion or alteration of the native X6/P000 foundation.

Next research question: determine the exact incidence and frequency of length-four edges in the global vertex adjacency graph of this physical fiber, and characterize which support profiles realize four. Searching for length-five edges is now resolved in the negative by the proof above. The independent mother question of optimum low-support transmission and its BRC observer consequences remains open.
