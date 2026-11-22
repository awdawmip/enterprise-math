# EC49FXE — Exact r=4 fixed observer for all 55 consecutive relative-phase intervals

Date: 2026-11-23 (Asia/Shanghai). Frozen input: **BRC16943** (unchanged). Follows EC49FXD ([Draft PR #2973](https://github.com/awdawmip/enterprise-math/pull/2973)), and EC49FXA–FXC. Research state: **AUTHOR_PROVED / EXACT_INTEGER_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED**.

## Exact result

In the frozen 110-periodic two-channel P10/one-hole auxiliary Farey–CRT observation model, assume complete indexed reflection-defect spectra and known reference. A fixed activation at site \(t\in\mathbb Z/110\) returns **two separately counted Boolean channel bits**. Unknown relative offset belongs to \(D_k=\{0,\ldots,k-1\}\subset\mathbb Z/110\), \(1\le k\le55\). Requiring minimum sampled Hamming distance \(r=4\) yields the exact optimum

\[
\boxed{N_{\mathrm{fixed}}(D_k;4)=
\begin{cases}
13,&k=1,2,\\
14,&k=3,4,\\
15,&5\le k\le55.
\end{cases}}
\]

A distance of four tolerates three known channel-bit erasures, or one unknown channel-bit error plus one known channel-bit erasure. Corruption or erasure of an entire two-bit physical activation is a separate coding model.

## Lower bounds

The already frozen P10 single-pair witness/disjoint-block reduction makes the following elementary inequality necessary and sufficient for this auxiliary representation:

\[
F_S(d,i,j)=\sum_{t\in S}\left(
\mathbf1_{t\bmod5=i,\ t\bmod11\ne j}+
\mathbf1_{(d-t)\bmod5=i,\ (d-t)\bmod11\ne j}
\right)\ge4
\]
for every \(d\in D_k\), \(i\in\mathbb Z/5\) and deleted column \(j\in\mathbb Z/11\). Let \(m_i\) be the number of installed sites with residue \(i\bmod5\); put \(n=m_i+m_{d-i}\). Over the eleven deleted columns, a total of \(n\) contributions are deleted, so the maximum deletion is at least \(\lceil n/11\rceil\). Requiring distance four forces \(n-\lceil n/11\rceil\ge4\), hence \(n\ge5\). Summing over the five \(i\) for one \(d\) gives \(2|S|\ge25\), or \(|S|\ge13\) for any nonempty \(D_k\).

For \(k\ge3\), the self-reflection rows \((d,i)=(0,0),(1,3),(2,1)\) force \(m_0,m_3,m_1\ge3\): a block with two sites has only four contributions, some erased by a possible mod-11 column. For \(d=1,i=2\), the \(n\ge5\) inequality yields \(m_2+m_4\ge5\). Thus \(|S|\ge3+3+3+5=14\).

For \(k\ge5\), the five phases \(0,\ldots,4\) supply a self-reflection for **every** \(i\), forcing all \(m_i\ge3\) and \(|S|\ge15\). These are analytic exact integer lower bounds.

## Sharp finite constructions

For \(k=1,2\), choose 13 sites
\[
S_{13}=\{56,58,63,65,75,81,89,92,94,97,98,104,105\}.
\]
For \(k=3,4\), choose 14 sites
\[
S_{14}=\{64,65,66,71,73,76,79,82,90,98,103,104,105,107\}.
\]
For every \(5\le k\le55\), choose \(S_{15}=\{0,1,\ldots,14\}\). In \(S_{15}\), every mod-5 class has three distinct mod-11 columns. After the one-hole deletion, each of the two channels retains at least two distinguishing bits, so \(F_S\ge4\) for **all** offsets.

For the two finite short-interval witnesses, the following are exact minima of \(F_S(d,i,j)\) over the eleven \(j\), with five entries per row indexed by \(i=0,\ldots,4\):

| Witness, d | i=0 | i=1 | i=2 | i=3 | i=4 |
|---|---:|---:|---:|---:|---:|
| S13, d=0 | 5 | 4 | 4 | 4 | 4 |
| S13, d=1 | 4 | 4 | 4 | 5 | 4 |
| S14, d=0 | 5 | 5 | 4 | 4 | 5 |
| S14, d=1 | 4 | 4 | 4 | 5 | 4 |
| S14, d=2 | 4 | 5 | 4 | 4 | 4 |
| S14, d=3 | 4 | 4 | 4 | 4 | 4 |

The accompanying standalone JavaScript verifier independently checks all 84,700 exact \(F_S(d,i,j)\) constraints over the 55 intervals, validates the two small tables and records all 55 minimizing layouts in JSON. It requires no optimization solver or external library. The calculation was crosschecked locally under Node.js 22.16.0.

## Scope and continuation

This closes **r=4** for the frozen auxiliary CRT observer. Along with EC49FXB, FXC and FXD, exact r=1,2,3,4 interval classifications are now available. The proof preserves original Farey anchor/height, signed branch, affine source phase and causal residue as typed context. P000, six native spatial axes and three-dimensional native slice remain unchanged. This auxiliary representation result is not a new native dynamical theorem. No formal Task CLAIM, Result or independent Review is asserted.

Next investigate the precise \(r\ge5\) phase thresholds and determine which relative-offset families arise from **actual same-anchor Farey evolution**.
