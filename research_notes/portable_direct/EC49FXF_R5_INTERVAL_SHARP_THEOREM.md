# EC49FXF — Sharp r=5 fixed two-channel observation for every consecutive relative-phase interval

Date: 2026-11-23 (Asia/Shanghai). Scientific source pin: **BRC16943** (unchanged). Direct scientific predecessor: EC49FXE, [PR #2974](https://github.com/awdawmip/enterprise-math/pull/2974), exact theorem at `f3b99d00dca976daec00e47e63935125fb177c46:research_notes/portable_direct/EC49FXE_R4_INTERVAL_SHARP_THEOREM.md`. Status: **AUTHOR_PROVED / EXACT_FINITE_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED**.

## Theorem: fifth channel-bit Hamming distance

Use the inherited frozen 110-periodic two-channel, P10/one-hole CRT **auxiliary Farey observer**, full separately indexed reflection spectra and known reference. One physical activation at (t\in\mathbb Z/110) returns two separately counted Boolean bits. The admissible relative phase is (D_k=\{0,1,\ldots,k-1\}\), (1\le k\le55). Require minimum **channel-bit** Hamming distance (r=5), sufficient to correct two arbitrary unknown bit errors in the sampled two-channel word.

Then the exact minimum number of *fixed physical activation sites* is
[
\boxed{N_{\rm fixed}(D_k;5)
 =20-\min\!\left(5,\max\!\left(0,\left\lfloor\frac{36-k}{2}\right\rfloor\right)\right).}
]
In particular:

| k | 1–26 | 27–28 | 29–30 | 31–32 | 33–34 | 35–55 |
|---|---:|---:|---:|---:|---:|---:|
| Exact minimum | 15 | 16 | 17 | 18 | 19 | 20 |

The first cost increase occurs at **27** possible consecutive phases; five successive two-phase thresholds occur before saturation at 35. The dependence on (k) is a property of this frozen auxiliary sensor model, not a time-evolution or native-heartbeat theorem.

## Exact inherited observer reduction

For a physical probe set (S\subseteq\mathbb Z/110), phase (d), mod-5 residue (i), and deleted mod-11 column (j), the inherited actual P10 single-pair witness/disjoint-block reduction says the fixed observer requirement is equivalent to **all** the inequalities
[
F_S(d,i,j)=\sum_{t\in S}\left[
\mathbf 1_{t\bmod5=i,\ t\bmod11\ne j}
+\mathbf 1_{(d-t)\bmod5=i,\ (d-t)\bmod11\ne j}
\right]\ge5
]
for every (d\in D_k, i\in\mathbb Z/5, j\in\mathbb Z/11). This equivalence is a dependency on the frozen EC49FWT–FXE chain; no new claim is made about the native X6 dynamics or arbitrary observed data.

Write (m_i=|\{t\in S:t\bmod5=i\}|). At any fixed ((d,i)), there are (n=m_i+m_{d-i}) potential contributions, and, across the 11 deleted columns, a total of (n) deletions. Some deleted column therefore removes at least one contribution whenever (n>0). Since (F\ge5), necessarily (n\ge6). Summing over all five (i) for a single (d\) gives (2|S|\ge30): **every nonempty phase set needs at least 15 activations**.

For (k\ge5), the self-reflection phase (d\equiv2i\pmod5) occurs for every (i). Then (2m_i\ge6), so **each mod-5 color contains at least three sites**. Call a color *light* if (m_i=3), otherwise *heavy* with (m_i\ge4). If (s) colors are light, (|S|\ge3s+4(5-s)=20-s).

For a light color, the three selected sites must have distinct mod-11 residues: otherwise choosing its self-reflection phase and the repeated deleted column removes at least two from (n=6), giving (F\le4). Hence each light color corresponds to a three-element set of distinct residues in one mod-5 color of \(\mathbb Z/55\). Moreover, for **any two selected light residues** (x,y), even in the same color and allowing (x=y), we require
[
\boxed{(x+y)\bmod55\notin D_k.}\tag{L}
]
Indeed if (d=(x+y)\bmod55\in D_k), at the corresponding (i=x\bmod5), choosing (j=x\bmod11) deletes the left contribution of (x) and right contribution of (y). The two participating colors are light, so the row has six potential contributions and at most four survivors. The case (x=y) deletes both channel contributions of that one site. Thus (L) is *necessary* for every light/light pair.

## Finite upper bound on the number of light colors

At each of the decisive thresholds (k=27,29,31,33,35), enumerate all three-element subsets of each color in \(\mathbb Z/55\): precisely \(5\binom{11}{3}=825\) candidates before filtering. Keep a triple (T) only when ((x+y)\bmod55\ge k) for all (x,y\in T) including equal residues. Two triples of different colors are compatible precisely when this holds for all their cross-pairs as well. A depth-five exact enumeration choosing zero or one compatible triple per color gives:

| k | surviving triples per colors 0,1,2,3,4 | max mutually compatible light colors |
|---|---|---:|
| 27 | (1,2,2,1,2) | 4 |
| 29 | (1,1,2,1,1) | 3 |
| 31 | (0,1,1,1,1) | 2 |
| 33 | (0,0,1,0,1) | 1 |
| 35 | (0,0,0,0,0) | 0 |

The attached dependency-free program contains the complete 825-candidate generation and compatible-family recursion, including all surviving actual triples and maximal witnesses; this is a finite, transparently specified obstruction, not an unverified integer-programming bound. By monotonicity in (k), for every (k\ge27) we obtain
[
s\le\max\!\left(0,\left\lfloor\frac{36-k}{2}\right\rfloor\right).
]
Combining with (|S|\ge20-s) and the universal (|S|\ge15) proves the stated lower bound for all 55 intervals.

## Uniform attaining constructions

Let
[
s=\min\!\left(5,\max\!\left(0,\left\lfloor\frac{36-k}{2}\right\rfloor\right)\right).
]
Create (s) *light* colors by taking, for every integer (x=18-s,\ldots,17), exactly the sites ({x,x+5,x+10}). In every remaining mod-5 color (i), take the four *heavy* sites ({i,i+5,i+10,i+15}). The two families use different mod-5 colors; their union (S_k) has precisely (3s+4(5-s)=20-s) distinct positions modulo 110, and every color's selected mod-11 columns are distinct.

All light sites lie in the ordinary interval ([18-s,27]), so every sum of two light sites is between (36-2s) and (54), inclusive. By the choice of (s), (k\le36-2s); therefore no light/light pair sum lies in (D_k) modulo 55. For a light/light reflection row, six potential contributions have at most one deletion, hence (F\ge5). For a light/heavy row there are at least seven contributions and at most two deletions (one per channel); for heavy/heavy there are eight and at most two. Thus (F_S(d,i,j)\ge5) for every (d,i,j). The lower bound is attained.

The endpoint witnesses are (S_{26}=\{13,\ldots,27\}) (15 sites), (S_{28}) (16 sites, light bases 14–17), (S_{30}) (17 sites, light bases 15–17), (S_{32}) (18 sites, light bases 16–17), (S_{34}) (19 sites, light base 17) and (S_{55}=\{0,\ldots,19\}) (20 sites). All 55 exact sets are emitted in the verification output.

## Reproducible evidence and research boundary

The attached standalone JavaScript program uses only integer modular arithmetic. It directly checks all (sum_{k=1}^{55}55k=84,700) inequalities for the constructed sets; independently enumerates the 825 potential light triples at the five decisive values of (k); and exhaustively checks all compatible color selections. Its output includes every phase interval, set, minimum sampled distance, candidate family and maximizing family. Local run: `node EC49FXF_R5_INTERVAL_VERIFY.js > EC49FXF_R5_INTERVAL_OUTPUT.json`; all 84,700 inequalities passed and all five light-color maxima matched. The certificate is a finite exact program/argument, not a formal Lean verification or independent mathematical review.

This is the next new result after (r=1,2,3,4) classifications in EC49FXB–FXE, with the original scientific pin **BRC16943** unchanged. Farey anchor and height, signed side, affine seed, relative phase, missing-column source and causally relevant residual remain typed state; a Boolean sensor word is not a lossless original-world coordinate. P000 and the protected six-native-axis / three-dimensional-slice worldview are unchanged.

**Open next questions:** exact consecutive-phase functions for (r\ge6); classification under *whole-activation* errors rather than channel-bit Hamming errors; and genuine same-anchor Farey relative-phase reachability versus arbitrary auxiliary \(D_k\). Formal Task CLAIM/Result/Review not established; retain real Researcher/Activity provenance separately.
