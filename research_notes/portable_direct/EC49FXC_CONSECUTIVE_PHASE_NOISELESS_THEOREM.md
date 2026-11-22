# EC49FXC — Exact noiseless fixed activation cost for consecutive relative-phase uncertainty

Date: 2026-11-23 (Asia/Shanghai). Frozen science: \`BRC16943\`, unchanged. Inherits [EC49FXA](https://github.com/awdawmip/enterprise-math/pull/2968) and its elementary CRT constraint, and [EC49FXB](https://github.com/awdawmip/enterprise-math/blob/bd76c61ba399baa727ffa99bf16dea112ce98dc5/research_notes/portable_direct/EC49FXB_SHORT_INTERVAL_ERASURE_THEOREM.md). Status: AUTHOR_PROVED / EXACT_INTEGER_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED.

## Proposition

Retain the 110-periodic frozen P10/one-hole auxiliary Farey–CRT observer. Full indexed spectra and the reference are supplied, while the relative offset lies in \`D_k={0,1,...,k-1}\` in Z/110, with \`1<=k<=55\`. A fixed physical activation at \`t\` reads both Boolean channels separately. For noiseless identification of every compatible two-state spectral fiber, require sampled Hamming distance at least \`r=1\`.

**The exact fixed-activation optimum for all 55 nonempty consecutive antipodal-free intervals is**

\[
\boxed{N_{\mathrm{fixed}}(D_k;1)=\max\!\left(5,\ 10-\left\lceil\frac{55-k}{2}\right\rceil\right),\quad 1\le k\le55.}
\]

Equivalently, the optimum is **5** for \`1<=k<=46\`; then **6** for 47–48, **7** for 49–50, **8** for 51–52, **9** for 53–54, and **10** at 55. The last value agrees with the full antipodal-transversal EC49FWZ optimum.

## Elementary distance invariant (reused exact frozen result)

For \`S subset Z/110\`, \`d in D_k\`, \`i in Z/5\`, and an absent column \`j in Z/11\`, the distinguishing channel-bit count for the frozen elementary one-pair witness is

\[
F_S(d,i,j)=\sum_{t\in S}\left(
  {\bf1}_{t\bmod5=i,\ t\bmod11\ne j}
 +{\bf1}_{(d-t)\bmod5=i,\ (d-t)\bmod11\ne j}
\right).
\]

The inherited P10 realization and disjoint-block reduction state that \`F_S(d,i,j)>=1\` for every \`d,i,j\` is both necessary and sufficient for this *auxiliary observer's* noiseless fixed-layout problem. This statement is conditional on that documented frozen realization, not a new direct X6 dynamical theorem.

Define \`m_i=#\{t in S:t mod5=i\}\`. For one \`d\`, every \`i\` must have \`m_i+m_(d-i)>=2\`: with 0 or 1 contributions, selecting the single missing mod11 column that deletes the contribution would make \`F_S=0\`. Summing over all five \`i\` yields \`2|S|>=10\`; hence \`|S|>=5\` for every nonempty \`D_k\`.

## Strong lower bound at k>=46

As \`D_k\` contains the representatives \`0,1,2,3,4\`, the self-reflection row \`d=2i (mod5)\` forces \`m_i>=1\` for every \`i in Z/5\`. Call a block *singleton* if \`m_i=1\`, and write its physical site as \`t_i\`. Let \`s\` be the number of singleton blocks, so \`|S|>=s+2(5-s)=10-s\`.

For a singleton, the self-reflection row has two channel contributions and both are deleted exactly when \`d=2t_i (mod55)\`. The unique representative \`a_i=(2t_i mod55)\` in \`{0,...,54}\` must therefore lie in \`[k,54]\`. For two singleton blocks \`i,l\`, their cross-reflection row is fully deleted when \`d=(t_i+t_l mod55)\`. This residue satisfies
\[
2d\equiv a_i+a_l\pmod{55}.
\]

Suppose \`a_i,a_l\` have **different parity**. Because \`k>=46\`, their sum is odd and lies in \`[2k,107]\`. The representative of their modular half-sum is then exactly
\[
d=\frac{a_i+a_l-55}{2}\in[18,26]\subseteq D_k,
\]
contradicting \`F_S>=1\`. Thus every singleton's \`a_i\` has the **same parity**. The interval \`[k,54]\` contains \`55-k<=9\` integers, with at most \`\lceil(55-k)/2\rceil\` of either parity. Moreover distinct singleton blocks have distinct \`a_i\bmod5=2i\`; hence
\[
s\le\left\lceil\frac{55-k}{2}\right\rceil,\qquad |S|\ge10-\left\lceil\frac{55-k}{2}\right\rceil.
\]
Together with \`|S|>=5\` this proves the lower bound. The argument covers arbitrary physical sites in Z/110, including sites above 54 and repeated CRT residue types; no layout symmetry was assumed.

## Uniform explicit attainment

For \`1<=k<=46\`, install \`S_k={23,24,25,26,27}\`. There is one site in each mod5 block; any two chosen sites sum to an integer in \`[46,54]\`, outside \`D_k\`. The two deletion columns of every elementary row therefore never coincide, giving \`F_S>=1\`.

For \`47<=k<=55\`, put \`a=ceil(k/2)\` and take singleton sites
\[
T_k=\{a,a+1,\ldots,27\}.
\]
Their mod5 classes are distinct, and every pairwise sum lies in \`[k,54]\`. For each mod5 class \`i\` missing from \`T_k\`, add the two physical sites \`i\` and \`i+5\`. These occupy two distinct mod11 columns. If a row joins two singleton blocks, their sum avoids the forbidden \`D_k\`, so one channel bit survives every deletion. If a row involves a doubled block, at least three channel positions are counted; the one-hole deletion can erase at most one from each channel, leaving at least one. Consequently all elementary rows have distance >=1. The cardinality is
\[
|S_k|=|T_k|+2(5-|T_k|)=10-\lceil(55-k)/2\rceil.
\]

Representative layouts:
| k | selected physical sites | optimum |
|---:|---|---:|
| 46 | 23,24,25,26,27 | 5 |
| 48 | 3,8,24,25,26,27 | 6 |
| 50 | 3,4,8,9,25,26,27 | 7 |
| 52 | 0,3,4,5,8,9,26,27 | 8 |
| 54 | 0,1,3,4,5,6,8,9,27 | 9 |
| 55 | 0,1,2,3,4,5,6,7,8,9 | 10 |

The attached dependency-free JavaScript checker evaluates every \`k,d,i,j\` (84,700 exact inequalities), independently computing each site's channel contributions and inspecting the claimed size. Its JSON output gives all 55 optima, layouts and minimum distances. The proof is analytic; this finite check cross-validates rather than replaces the parity lower bound.

## Scientific interpretation, scope and next question

Noiseless detection is extremely resilient to consecutive offset uncertainty: 5 fixed activations suffice until 46 different relative phases are admitted; then the cost increases at every second new offset. Compare with the distinct \`r=2\` result EC49FXB: 8, 9, or 10 activations, with transitions at k=3 and k=5. Thus the two error models have qualitatively different threshold structures.

**Still open:** exact \`N_fixed(D_k;3)\` for one unknown **channel-bit** error, and feasibility restrictions on relative offsets for an actual shared Farey anchor. The present r=1 result preserves the reference, branch, phase, signed/source relation and three-dimensional-slice/native-X6 transfer questions as separately typed provenance; it makes no claim to reconstruct the full native dynamical state. P000 and ACTIVE worldview are unchanged. Formal Task CLAIM, Result, and independent Review have not been performed by this mathematical note.

This work is independent portable research under previously recorded EC49 research provenance. Published exact PR/commit and Activity association are tracked separately from the science file.
