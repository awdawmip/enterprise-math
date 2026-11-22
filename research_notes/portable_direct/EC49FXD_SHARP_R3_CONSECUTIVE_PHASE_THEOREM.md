# EC49FXD — sharp fixed observer for one unknown channel-bit error across all consecutive relative phases

Date: 2026-11-23 (Asia/Shanghai). Frozen science: **BRC16943** (unchanged). Continues [EC49FXA–FXB](https://github.com/awdawmip/enterprise-math/pull/2968) and [EC49FXC](https://github.com/awdawmip/enterprise-math/pull/2970). Status: **AUTHOR_PROVED / EXACT_FINITE_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED**.

## Theorem and exact scope

Retain the frozen 110-periodic P10/one-hole Farey–CRT auxiliary observer, separately indexed left/right spectra and known reference. The relative phase lies in \(D_k=\{0,\ldots,k-1\}\subset\mathbb Z/110\), with \(1\le k\le55\). A physical activation at a chosen \(t\in\mathbb Z/110\) returns **two separate Boolean channel bits**. We require a sampled Hamming distance of at least \(r=3\) between all competing two-state spectral-fiber words, permitting correction of one unknown **channel-bit** error.

Then the exact minimum number of fixed physical activations is

\[
\boxed{N_{\mathrm{fixed}}(D_k;3)=15-\min\bigl(5,\max(0,\lfloor(46-k)/2\rfloor)\bigr).}
\]

| Relative-phase count \(k\) | 1–36 | 37–38 | 39–40 | 41–42 | 43–44 | 45–55 |
|---|---:|---:|---:|---:|---:|---:|
| Exact optimum | 10 | 11 | 12 | 13 | 14 | 15 |

## Elementary reduction inherited from frozen proof

For a probe set \(S\), offset \(d\in D_k\), block \(i\in\mathbb Z/5\), and absent mod-11 column \(j\in\mathbb Z/11\), define the exact two-channel disagreement count

\[
F_S(d,i,j)=\sum_{t\in S}\left(
\mathbf1_{t\bmod5=i,\ t\bmod11\ne j}+
\mathbf1_{(d-t)\bmod5=i,\ (d-t)\bmod11\ne j}
\right).
\]

The EC49FXA–FXC frozen, realized P10 one-pair witness (including \(U=299\)) and disjoint-block reduction establish that **all** \(F_S(d,i,j)\ge3\) is both necessary and sufficient for this auxiliary observer's fixed error-correcting requirement. We preserve that scientific input rather than re-fuzzing it or claiming a native X6 theorem.

Write \(m_i=|\{t\in S:t\bmod5=i\}|\). For fixed \(d,i\), put \(n=m_i+m_{d-i}\). Across the eleven choices of \(j\), the total deletions sum to \(n\), hence one deletion has at least \(\lceil n/11\rceil\) contributions. \(F\ge3\) therefore requires \(n-\lceil n/11\rceil\ge3\), so \(n\ge4\). Summing over \(i\) gives \(2|S|\ge20\), establishing **\(|S|\ge10\)** for every nonempty \(D_k\).

## Light-block lower bound

For \(k\ge5\), the self-reflection \(d=2i\bmod5\) occurs within \(D_k\) for every block \(i\). It forces \(m_i\ge2\), since a one-site block contributes at most two channel bits. Call a block **light** if \(m_i=2\), otherwise **heavy** with \(m_i\ge3\). If \(s\) blocks are light, then

\[
|S|\ge2s+3(5-s)=15-s. \tag{1}
\]

The two selected sites of a light block must be **distinct modulo 55**: if they share the mod-11 column, deleting that column in a self-reflection row erases at least two of its four contributions. Let \(x,y\) be their distinct mod-55 residues; \(x\equiv y\bmod5\). For **any** two sites from light blocks, including twice the same site, their sum modulo 55 must lie *outside* \(D_k\). Otherwise choose \(d=(x+y)\bmod55\) and the mod-11 deletion corresponding to the first site: both channel disagreements disappear and the four-contribution row drops to at most two.

Consequently every light block selects an unordered pair from the eleven residues of one mod-5 class satisfying

\[
(2x)\bmod55,\quad(x+y)\bmod55,\quad(2y)\bmod55\in[k,54].\tag{2}
\]

Two light pairs of distinct colors coexist only if all four cross-sums also lie in \([k,54]\). There are just \(5\binom{11}{2}=275\) candidate pairs before filtering. The complete decisive **finite obstruction** is:

| \(k\) | All pairs satisfying (2), written color:(x,y) | Maximum mutually compatible light colors |
|---:|---|---:|
| 37 | 0:(20,25); 1:(21,26),(46,51); 2:(22,27),(47,52); 3:(48,53); 4:(19,24),(49,54) | 4 |
| 39 | 0:(20,25); 1:(21,26); 2:(22,27),(47,52); 3:(48,53); 4:(49,54) | 3 |
| 41 | 1:(21,26); 2:(22,27); 3:(48,53); 4:(49,54) | 2 |
| 43 | 2:(22,27); 4:(49,54) | 1 |
| 45 | none | 0 |

The pair lists are obtained by the explicit integer tests in (2), not by a numerical optimization claim. Each compatible-set maximum is established by checking the at most eight listed pairs and their cross-sums. Short direct witnesses to impossibility: at \(k=37\), the sole color-0 and color-3 pairs conflict, so five light colors cannot coexist. At \(k=39\), color-0/1 low candidates conflict with color-3/4 high candidates, and either color-2 choice joins only one side: maximum three. At \(k=41\), the four pairs split into two internally compatible but mutually incompatible groups of two. At \(k=43\), the only two candidates conflict. At \(k=45\), no light pair survives. The program records all candidate pairs and exhaustive subset counts for independent inspection.

Monotonicity in \(k\) gives \(s\le\max(0,\lfloor(46-k)/2\rfloor)\) for \(k\ge37\). Combining with (1) and \(|S|\ge10\) proves the claimed lower bound.

## Explicit upper bound for every k

Set \(s=\min(5,\max(0,\lfloor(46-k)/2\rfloor))\). For every \(x=23-s,23-s+1,\ldots,22\), install the two sites \(x,x+5\) (one light block of each of \(s\) distinct mod-5 colors). In every remaining color \(i\), install the three sites \(i,i+5,i+10\). This yields exactly \(2s+3(5-s)=15-s\) distinct sites, all in \(0,\ldots,27\).

Every sum of two light sites lies in the **ordinary** integer interval \([2(23-s),54]=[46-2s,54]\), hence outside \(D_k\) by construction. Every light block has two distinct mod-11 columns and each heavy block has three. If both reflected blocks are light, four contributions lose at most one because two deletions would imply a forbidden light/light sum. If at least one is heavy, at least five contributions lose at most two, one per channel. In both cases \(F_S(d,i,j)\ge3\). Therefore this explicit construction attains the lower bound throughout all 55 intervals.

| k (last of plateau) | Selected sites | Count |
|---:|---|---:|
| 36 | 18–27 inclusive | 10 |
| 38 | 3,8,13,19,20,21,22,24,25,26,27 | 11 |
| 40 | 3,4,8,9,13,14,20,21,22,25,26,27 | 12 |
| 42 | 0,3,4,5,8,9,10,13,14,21,22,26,27 | 13 |
| 44 | 0,1,3,4,5,6,8,9,10,11,13,14,22,27 | 14 |
| 55 | 0–14 inclusive | 15 |

## Computation, scope and next scientific unit

The attached dependency-free JavaScript verifier (executed locally with Node 22.16.0) recalculates all \(\sum_{k=1}^{55}(k\cdot5\cdot11)=84{,}700\) exact integer \(F\) constraints, enumerates all 275 potential unordered light pairs at the five decisive thresholds and exhaustively checks compatible subsets. It emits a 55-row JSON with each layout and measured minimum. All assertions passed. The finite lower-bound checks are small, fully specified and reproducible; the analytic argument and construction explain their relevance.

This **closes the \(r=3\)** consecutive-offset optimization in the frozen **auxiliary Farey–CRT representation**, complementing EC49FXC for \(r=1\) and EC49FXB for \(r=2\). Corruption of an entire paired activation is a different error model. Keep Farey anchor/height, signed branch, phase/source, affine seed and causally relevant residual separate from an indexed Boolean readout; P000 and the protected ACTIVE six-axis/three-dimensional-slice worldview remain unchanged.

Open questions: exact \(N_{\rm fixed}(D_k;r)\) for \(r\ge4\); actual same-anchor Farey relative-offset reachability versus the auxiliary \(D_k\) families; and error correction when a whole physical activation, rather than one channel bit, is corrupted. No formal shared CLAIM, Result or independent Review is asserted by this scientific note.
