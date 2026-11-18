# R749SUF — Exact Farey-tree enumeration and even jump spectrum of the late two-Port BRC feedback staircase

Date: 2026-11-18 (Asia/Shanghai). Scientific status: **AUTHOR_EXACT_NOT_REVIEWED**.
Predecessor: R749SUE, paper at \`awdawmip/enterprise-math@1ede7d0d30f127e3ad679a7bce3981cc4b3476e4:research_notes/portable_direct/2026-11-18_R749SUE_UNIMODULAR_LATE_FEEDBACK_TAIL.md\`.
Frozen scientific model: \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`; WBRC-T30–T32, positive rational stable two-Port feedback; P000 remains untouched. This is an auxiliary contextual observation model, not licensed native X6 triadic dynamics.

## Problem and symbols

The preceding exact result expresses the saturated-minus-observed signature count for integer feedback grid K>M>=1 in the **late regime** 2K>M^3 as

\[
D_M(K)=N_\infty(M)-N(2,K,M)
=\#\{(a,d,u,v)\in[1,M]^4:\ ad-uv=1,\ K\leq \max(u,v)ad\}.
\]

All four entries are positive integers; ports and ordered coordinates stay labeled. Equality \`K=t\` is missing because stability is a strict inequality. This paper characterizes every jump of this finite staircase without an M^3 multi-sum or floating approximation.

## Theorem A — Positive unimodular matrices form a uniquely generated binary tree

Let \(\mathcal U_M\) consist of integer matrices
\[
A=\begin{pmatrix}a&u\\v&d\end{pmatrix},
\quad 1\le a,u,v,d\le M,\quad ad-uv=1.
\]
Set
\[
L=\begin{pmatrix}1&1\\0&1\end{pmatrix},\quad
R=\begin{pmatrix}1&0\\1&1\end{pmatrix}.
\]
Every determinant-one nonnegative integer 2×2 matrix is uniquely a word in right multiplications by L and R starting from I. Thus \(\mathcal U_M\) is exactly the bounded subtree nodes having all four entries positive. From \((a,u,v,d)\), right multiplication gives
\[
AL=(a,\ a+u,\ v,\ v+d),\qquad
AR=(a+u,\ u,\ v+d,\ d),
\]
where tuple order is always (a,u,v,d). A child is pruned if any entry exceeds M.

**Proof.** For a nonidentity nonnegative determinant-one matrix, one column dominates the other componentwise. Otherwise, the only possible nonnegative determinant-one incomparable pair is the two coordinate unit columns forming I; for positive crossing columns, the inequality \((u+p)(v+q)-uv=uq+vp+pq\ge3\) for p,q,u,v>=1 excludes determinant one, while the opposite crossing makes the determinant negative. If column 1 dominates, subtract column 2 and undo a unique right R; if column 2 dominates, subtract column 1 and undo a unique right L. Both retain nonnegative integral entries and determinant one; entry sum strictly decreases. Induct to I. Dominance uniquely selects the predecessor, proving unique factorization. Right multiplication never decreases any entry, so a bound violation has no valid descendants. QED.

There are exactly 2M+1 nonpositive-entry boundary nodes within the bound: I, L^j and R^j for 1<=j<=M. Every other visited node has all entries positive. Hence total visited nodes are
\[
|\mathcal U_M|+2M+1=H_M+2M+1,\quad
H_M=4\sum_{n=1}^{M}\varphi(n)-2M-2,
\]
using the previously established R749SUE totient identity. This is O(M²) arithmetic operations for the entire bounded tree, output-optimal when listing its H_M positive matrices. Histogram sorting, if needed, costs an additional O(H_M log H_M) comparisons. This is a unit-cost arithmetic bound for integers of O(log M) bits, not a bit-complexity or general native-X6 speedup claim.

## Theorem B — Exact late staircase and even jumps

Define the finite *labeled unimodular threshold polynomial*
\[
P_M(z)=\sum_{A\in\mathcal U_M}z^{\tau(A)},\qquad
\tau(A):=\max(u,v)ad.
\]
Let \(g_M(t)=[z^t]P_M(z)\). Then for every K>M satisfying 2K>M³,
\[
\boxed{D_M(K)=\sum_{t\ge K}g_M(t)}
\quad\text{and}\quad
\boxed{D_M(K)-D_M(K+1)=g_M(K).}
\]
Thus the tree enumerator generates **all** late-grid breakpoints and their exact jumps simultaneously; no re-evaluation for each K is needed.

For every M and integer t,
\[
\boxed{g_M(t)\equiv0\pmod 2}.
\]
Consequently the late deficit D_M(K) is always even; all nonzero jumps have an even number of ordered, labeled signatures.

**Proof.** The first identities substitute the R749SUE determinant-one missing-signature characterization and group the finite set by integer threshold. For parity, the commuting involutions (a,d,u,v)->(d,a,u,v) and (a,d,u,v)->(a,d,v,u) preserve positivity, upper bounds, determinant and tau. Their orbits have size 4 when a!=d and u!=v, otherwise size 2. An orbit of size 1 would require a=d and u=v; then a²-u²=1 with a,u>=1, impossible since (a-u)(a+u)=1. Every threshold fiber therefore splits into even-sized orbits. QED.

Note: evenness is proved for the unimodular **late regime**. The theorem does not assert parity for earlier grid resolutions where determinant >=2 classes can contribute.

## Theorem C — Exact finite certificate and reproducibility

The accompanying JS program implements the tree and an independent loop over (a,d,u) reconstructing v=(ad-1)/u. For every M=1,...,64 it compares complete integer threshold histograms, counts all visited nodes, checks the totient identity and verifies coefficient parity. For M<=16 it also independently checks selected late-grid deficits through the full (a,d,u,v) inequality, without assuming determinant one in that oracle.

All tests executed with exact integers in the JS Number safe range in this finite domain; no floating-point tolerance is used. The general statements follow from proofs A–B, not test extrapolation. The source file itself can be run by \`node R749SUF_FAREY_TREE_STAIRCASE_CERT.js\`. See the JSON record for checked parameters and sample breakpoint spectra.

Representative late spectra:
- M=10: late thresholds (810:2), (576:2); D_10(501)=4.
- M=16: (3600:2), (2940:2), (2366:2); D_16(2049)=6.
- M=32: D_32(16385)=32 across 11 distinct late thresholds; top thresholds are 30752:2, 27900:2, 25230:2, 22736:2.
- M=64: D_64(131073)=90 across 29 late thresholds, with 4910 positive bounded matrices.

These counts match the independently recomputed finite enumeration, and provide the full late-regime staircase by the exact histogram.

## Information-preservation and status

The two independent port-swap/diagonal-swap involutions are **counting symmetries**, not permission to erase port labels. BRC source/port provenance is preserved in each integer tuple. If a future observer distinguishes ordered ports, a quotient by these symmetries would be lossy.

**Novel contribution relative to R749SUE:** the complete unique-generator-tree proof, a direct O(M²) all-breakpoint histogram algorithm, and the global parity theorem for every late-resolution jump. R749SUE already gave modular-inverse enumeration and the final two-class jump; those are reused, not relabeled as new.

**Not established:** physical/native X6 Cell/Link/Port event authorization, resource or temporal closure, independent peer review, an external algorithmic speed benchmark, or a theorem for K outside the declared late regime.

## Recovery point / next scientific question

Study how many initial largest late thresholds follow the diagonal family \((a,d,u,v)=(M-j,M-j,M-j+1,M-j-1)\), and locate the first intrusion from a non-diagonal Farey-tree branch. The computed spectra show such intrusions in moderate M. Prove or refute a uniform asymptotic law for that crossover; then test whether the unimodular adjacency and label-sensitive Port observer survive actual admissible triadic X6 resource/time/event constraints. Keep current shared X6 CLAIM ownership separate; this is independent portable research.
