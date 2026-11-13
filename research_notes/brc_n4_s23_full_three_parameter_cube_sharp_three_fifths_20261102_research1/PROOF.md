# BRC N=4 S23: exact 3/5 radius on a full three-parameter real cube

2026-11-02 · Author analytic and executed exact-integer certificate · Independent review pending. Scientific inputs remain pinned at `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.

## Exact statement

Use the original six separately labeled positive-weight sources `AU0,AU1,AV,BU0,BU1,BV`, their original source mixing matrix and common encoder, shared causal parameter `b_U`, and the four-stop observation alphabet. Preserve the seven original fixed decoders `D1,D2,D3,D4,D6,D7,D8`. Optimize three arbitrary real stochastic 4x4 decoding kernels.

Let `S18` denote the exact eighteen strategies from the previously verified research frontier. Let
$$
J(t)=(1,t,0,0,0;0,0,0,0,1,0),\quad 0\le t\le 1,
$$
and the full three-parameter continuum
$$
F(s,t,u)=(s,t,u,0,0;1,0,0,0,0,0),\quad (s,t,u)\in[0,1]^3.
$$
With `L_D(z)` the maximum, across all six original prepared observations, of the total-variation distance between the prepared probability law and decoder D, write `D(K1,K2,K3)` for the ten-decoder bank. Then
$$
\boxed{\inf_{K_1,K_2,K_3}\sup_{z\in S_{18}\cup J([0,1])\cup F([0,1]^3)}\min_{D\in D(K_1,K_2,K_3)}L_D(z)=\frac35.}
$$
This is a model-internal exact result over the displayed parameter family, with all three stochastic kernels allowed arbitrary real entries in the infimum.

## Explicit upper construction

Retain the previous `K2`, `K3` and all seven fixed decoders. Replace only `K1` by the stochastic kernel whose four rows are
$$
K_1^*=\begin{pmatrix}
2/5&0&2/5&1/5\\
2/5&2/5&0&1/5\\
3/5&0&0&2/5\\
2/5&2/5&0&1/5
\end{pmatrix}.
$$
Each row is nonnegative and sums to one. This new bank covers all 20 explicitly listed old policies (including the 18 witnesses and two face points) at radius at most `3/5`. It covers `J([0,2/5])` using `K2` and `J([2/5,1])` using `K1*`; all four segment endpoint risks are at most `3/5`.

The principal new construction is a **single-decoder certificate per small three-dimensional cube**. Partition `[0,1]^3` into the one thousand closed boxes
$$
C_{abc}=[a/10,(a+1)/10]\times[b/10,(b+1)/10]\times[c/10,(c+1)/10],\quad a,b,c\in\{0,\ldots,9\}.
$$
For each box choose one of the ten fixed-bank decoders minimizing its worst risk among that box's eight vertices. The exact verifier tests all `1000*10*8` decoder-corner combinations and proves that **each of the 1000 boxes has at least one common decoder with worst corner risk at most `3/5`**. The selected decoder indices, ordered lexicographically by `(a,b,c)` with `c` changing fastest, are stored in `RUN_EVIDENCE.json` as a 1000-digit string. Index `0..9` corresponds to `D1,D2,D3,D4,D6,D7,D8,K1_new,K2,K3`.

The original causal source laws have the form `(x,(1-x)b,(1-x)(1-b)c,(1-x)(1-b)(1-c))` with `x\in\{s,t\}`, `b\in\{u,0\}` and fixed source-specific `c\in\{0,1\}`. Thus every source row, and consequently every six-source observation row after the **unchanged** mixture matrix, is separately affine in `s,t,u`. At every point inside one box, the six prepared observation rows are the same nonnegative tensor-product convex combination of that box's eight vertex observation rows. For a fixed decoder Q, each observation's TV distance to Q is convex in the prepared row; taking the maximum across six sources preserves the upper estimate by the maximum of eight vertex risks. Therefore the decoder selected for `C_{abc}` covers **every real-valued interior point** of that box. The cubes cover the full closed `[0,1]^3`.

As an independent compact subcertificate, on the full causal edge
$$
E(u)=F(3/5,3/10,u),\quad 0\le u\le1,
$$
`K1*` has risk exactly `1/2` at `u=0,5/7`, while fixed `D6` has risk exactly `1/2` at `u=5/7,1`. Affinity in `u` and TV convexity imply the edge is covered at `1/2`. At `u=0`, the bank's minimum risk equals `1/2`, so for this explicit ten-decoder bank,
$$
\boxed{\sup_{u\in[0,1]}\min_D L_D(E(u))=\frac12.}
$$
The previous specific bank had a unique `13/20` worst point on this edge. This is an explicit decoder repair, rather than changing the scientific inputs.

## Exact lower certificate

Reuse the ten legal strategies `W,X,Y,Z,T5,U,V,H(1/5),J(1),J(1/5)`, all contained in the displayed union. Each of these has risk at least `3/5` against each of the seven fixed decoders. For any three of those strategies assigned to a single free decoder Q, and one prepared observation row `i`, the elementary inequality
$$
\sum_{k=1}^{3}\mathrm{TV}(p_i^{(k)},Q_i)\ge\sum_{j=1}^{4}\max_{k=1,2,3}p_{ij}^{(k)}-1
$$
holds, as `max_k p_{ij}^{(k)}\le Q_{ij}+\sum_k(p_{ij}^{(k)}-Q_{ij})_+`. There are 84 out of 120 triples for which some `i` makes the right side at least `9/5`, hence no such triple can share a decoder with all three errors strictly below `3/5`. A complete exact check of all `3^10=59049` assignments of the ten strategies to three free decoder labels shows every assignment contains one of these 84 forbidden monochromatic triples (the minimum count is one). Thus every three-free-kernel bank has worst-case risk `>=3/5`; the explicit upper construction gives equality.

## Verification and scope

Run `node VERIFY.js` in the directory containing this note; it prints the exact test evidence. The program uses safe integer operations only, with probability scale `N=3360000` and total-variation denominator `2N`. It reconstitutes all six original source laws and their exact 6x6 source-mixture matrix; verifies stochastic kernel rows, source normalization, the 20 prior finite strategies, the two J intervals, 25 older face cells, 1331 new grid vertices, all 1000 three-dimensional cells, an interior multi-affinity identity, the causal-edge certificate, all 84 lower-bound triples, and every one of the 59049 labelings. The code verifies the finitely enumerated certificates; the algebraic multi-affinity and TV-convexity argument proves the entire real cube. Author proof and computation are awaiting independent review and canonical mathematical admission.

Relative to the previous frontier `e13c15cf7eeaef19789813a78b32ff1abd0ba39c` (single causal-edge obstruction) and `7a6494f5cefe177458bcdd7d2caf33d21c6f93f4` (full two-parameter face `3/5`), this advances the joint upper/lower result to an entire three-parameter real cube. The full eleven-real-parameter ten-label mother problem retains its previously established `[1/2,2/3]` interval, and requires separate continuation.
