# EC49FXG — Exact r=6 fixed paired-bit observer across all consecutive relative phases

Date: 2026-11-23 (Asia/Shanghai). Frozen input: **BRC16943** (unchanged). Direct predecessor: [EC49FXF](https://github.com/awdawmip/enterprise-math/pull/2976), [EC49FXE](https://github.com/awdawmip/enterprise-math/pull/2974). Status: **AUTHOR_PROVED / EXACT_INTEGER_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED**.

## Sharp theorem

In the same frozen 110-periodic P10/one-hole **auxiliary Farey–CRT two-channel** observer, suppose an activation at physical site (t\in\mathbb Z/110) returns two separately counted Boolean channel bits. Assume complete separately indexed reflection-defect spectra and known reference. Unknown relative offset is in (D_k=\{0,1,\ldots,k-1\}\) with (1\le k\le55). Requiring minimum sampled channel-bit Hamming distance (r=6) gives

[
\boxed{N_{\mathrm{fixed}}(D_k;6)=
\begin{cases}
18,&1\le k\le2,\\
19,&3\le k\le4,\\
20,&5\le k\le55.
\end{cases}}
]

This corrects up to two unknown channel-bit errors together with one known channel-bit erasure; whole-activation corruption is not the same metric. Compare r=5 [EC49FXF](https://github.com/awdawmip/enterprise-math/pull/2976): its first cost transition occurs at k=27, whereas r=6 saturates by k=5.

## Analytic lower bounds

Use the established exact necessary-and-sufficient CRT reduction (frozen EC49FWT–FXF): for every (d\in D_k,i\in\mathbb Z/5,j\in\mathbb Z/11),
[
F_S(d,i,j)=\sum_{t\in S}\big[
\mathbf1_{t\bmod5=i,\;t\bmod11\ne j}
+\mathbf1_{(d-t)\bmod5=i,\;(d-t)\bmod11\ne j}
\big]\ge6.
]
Let (m_i=|S\cap(i\bmod5)|\). The ((d,i)) row has (n=m_i+m_{d-i}) potential contributions. Their deletions sum to (n) over the 11 choices of (j). At least one deletion occurs for (n>0), so (F\ge6) requires **(n\ge7)**. Summing over the five (i) for any one (d) yields (2|S|\ge35), hence (|S|\ge18).

For (k\ge3), the self-reflections ((d,i)=(0,0),(1,3),(2,1)) force (m_0,m_3,m_1\ge4), since their total (n=2m_i\ge7). The row ((d,i)=(1,2)) gives (m_2+m_4\ge7). Consequently (|S|\ge4+4+4+7=19).

For (k\ge5), phases (d=0,1,2,3,4) give a self-reflection in each mod-5 color, so **all** (m_i\ge4) and (|S|\ge20).

## Attaining constructions

- For (k=1,2), use 18 consecutive sites (S_{18}=\{3,4,\ldots,20\}\).
- For (k=3,4), use 19 consecutive sites (S_{19}=\{3,4,\ldots,21\}\).
- For (5\le k\le55), use (S_{20}=\{0,1,\ldots,19\}\). Each mod-5 color has exactly four sites in four distinct mod-11 columns, so each of the two channels retains at least three differences after deletion: (F\ge6), uniformly for all permitted phases.

The short finite witnesses were checked by direct exact integer enumeration for every admissible phase/block/deleted column. The attached dependency-free JavaScript program verifies all 55 intervals (84,700 individual (F_S(d,i,j)) evaluations) and emits all 55 optimal layout sets in JSON. The complete local verification returned `all_pass=true`.

The closed claim is **within the frozen auxiliary observer's exact equivalence to these CRT constraints**. The original Farey anchor, branch, height, signed source, phase, affine seed and causal residual remain separately typed; Boolean words are not complete native X6 states. P000 and the ACTIVE six-axis / three-dimensional slice research worldview are unchanged. Neither independent Review nor formal Task CLAIM/Result is asserted.

Next scientific questions: exact (r\ge7) intervals; effects of corruption of a full two-bit activation; actual same-anchor Farey relative-phase reachability compared with the auxiliary permissible sets.
