# PREFIX-1010 — Three-Green-series reconstruction of all rooted signed BRC Link loops

Date: 2026-11-22 (+08). Status: **AUTHOR_FORMAL_LAURENT_PROOF / EXACT_INTEGER_CROSS_CHECKED / NOT_REVIEWED**.

## Exact model, provenance and result

Retain the frozen scientific input at awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json (P000 V5), the Heartbeat World native six-axis signed X6 Cell torsor, a chart-relative chosen Cell 0, initial incoming-neighbour port h=-e1, and the Stage46 *candidate* BRC multiplier w(h,d)=1−6[h=d], equal to 1 or −5. Each named direction d moves x to x+d and updates its incoming port to −d. Both orientations of the one Link {0,e1} are blocked without renormalization.

Write L_k for the integer signed-weight sum of all 2k-step Link-avoiding paths from Cell 0 back to Cell 0, with named incoming ports retained until the final sum. This is the rooted-loop coefficient in PREFIX-1009. Let \(\mathcal L(z)=\sum_{k\ge0}L_kz^{2k}\). The goal is an exact all-grade formula, not a physical-time or squared-probability statement.

**Theorem 1010.1 (all-grade three-series formula).** Introduce six formal native-axis Laurent symbols \(X_i\), with \(X^{e_i}=X_i\), and
\[
S(X)=\sum_{i=1}^{6}(X_i+X_i^{-1}),\quad
D(X,z)=1-zS(X)+36z^2,\quad
G_j(z)=[X_1^jX_2^0\cdots X_6^0]D(X,z)^{-1}\quad(j=0,1,2).
\]
In the ring of integer formal power series, define
\[
\begin{aligned}
H&=1-36z^2,\\
a&=(G_0-12zG_1+36z^2G_2)/H,\\
b&=((1+36z^2)G_1-6z(G_0+G_2))/H,\\
A&=((1+36z^2)G_1-12zG_0+36z)/H,\\
B&=((1+36z^2)G_0-12zG_1-6)/H,\\
c&=G_1-6zG_0,\qquad d=G_0-6zG_1,\\
p&=1+zA,\qquad q=zB,\qquad \Delta=p^2-q^2.
\end{aligned}
\]
Then \(\Delta(0)=1\), and for **all** \(k\ge0\),
\[
\boxed{\mathcal L(z)=d-\frac{z}{\Delta}\left[a(pc-qd)+b(pd-qc)\right].}\tag{1010.1}
\]
Only three scalar native-X6 Green series are needed for the complete final rooted-return observer. The source Cell, ordered path and port are not replaced for more detailed future observers.

## Derivation from the original signed BRC kernel

Work coefficientwise in \(\mathbb Z[X_1^{\pm1},\ldots,X_6^{\pm1}][[z]]\). Index the twelve named incoming ports h,h' by signed axes. The actual free BRC transfer is
\[
T_{h,h'}=(1-6\mathbf1_{h=-h'})X^{-h'}.
\]
Put \(u_h=1\), \(v_h=X^{-h}\), and \(P_{h,h'}=\mathbf1_{h=-h'}X^{-h'}\). Thus \(T=uv^t-6P\) and \(P^2=I\). Finite-dimensional algebra gives
\[
[(I-zT)^{-1}u]_h=\frac{1-6zX^h}{D}.\tag{1010.2}
\]
For a distinguished named outgoing direction d, put \(b_d(h)=1-6\mathbf1_{h=d}\). Exactly the same algebra gives
\[
[(I-zT)^{-1}b_d]_h
=\frac{(1-6zX^h)(1-6zX^{-d})}{(1-36z^2)D}
-\frac{6\mathbf1_{h=d}-36zX^h\mathbf1_{h=-d}}{1-36z^2}.\tag{1010.3}
\]
Both are identities of the original signed BRC paths: the formal variable z marks one discrete native step.

For the full spatial/port operator \(\mathsf T\), the two deleted directed transitions form a rank-two operator \(UV\). The first component evaluates the original outgoing signed weight at Cell 0 in direction +e1, then lands at (e1,−e1); the second evaluates at Cell e1 in direction −e1, then lands at (0,+e1). The exact masked transfer is \(\mathsf T_L=\mathsf T-UV\). Formal inversion yields
\[
(I-z\mathsf T_L)^{-1}=(I-z\mathsf T)^{-1}
-z(I-z\mathsf T)^{-1}U
\bigl(I_2+zV(I-z\mathsf T)^{-1}U\bigr)^{-1}
V(I-z\mathsf T)^{-1}.\tag{1010.4}
\]
Extracting the Cell displacements 0,e1,2e1 in (1010.2)–(1010.3) gives free rooted return d, starting-to-deleted-row vector (a,b), deleted-row-to-rooted-return vector (c,d)^t, and
\[
V(I-z\mathsf T)^{-1}U=\begin{pmatrix}A&B\\B&A\end{pmatrix}.
\]
Its feedback inverse is \(\Delta^{-1}\begin{pmatrix}p&-q\\-q&p\end{pmatrix}\). Insertion into (1010.4) proves (1010.1). Every coefficient is finite and the proof holds at arbitrary path length. A path returning in the signed X6 torsor has equal positive and negative uses of each axis; therefore all odd coefficients vanish, while coefficient \(z^{2k}\) is precisely L_k. QED.

## Theorem 1010.2 — quadratic-cost exact coefficient algorithm

For j=0,1,2, define factorial-denominator **combinatorial counting** series \(g_j(u)=\sum_{a\ge0}u^a/[a!(a+j)!]\). Let \(W_{r,j}\) count *unweighted* length-r signed six-axis words ending at j e1. Separating positive and negative axis occurrences gives the exact formula
\[
W_{r,j}=
\begin{cases}
r![u^{(r-j)/2}]g_j(u)g_0(u)^5,&r\ge j,\quad r\equiv j\pmod2,\\
0,&\text{otherwise}.
\end{cases}\tag{1010.5}
\]
From the formal expansion of D,
\[
\boxed{G_j(z)=\sum_{r\ge0}W_{r,j}\frac{z^r}{(1+36z^2)^{r+1}}.}\tag{1010.6}
\]
The factorial generating series are exact counting identities for the native paths, not an alternate physical propagation mechanism. For fixed six-axis dimension, a bounded set of polynomial convolutions and unit-series inversions computes L_0 through L_K with O(K²) arithmetic operations and O(K) coefficient storage (excluding the bit cost of growing integers). This substantially improves scalar coefficient computation over the expanding Cell–port DP in PREFIX-1009. The independently executed checker still uses the full named BRC signed transition.

## Exact checks and new coefficients

The prior PREFIX-1009 integer coefficients through k=6 are 1, −25, 390, −2365, −49550, 1645010, −22026080. The new Laurent method reproduces these and computes through k=20. An independently written native twelve-port, six-coordinate, signed integer BRC DP (excluding the two forbidden directed Link crossings) verifies **every k=0,…,10**, including:

| k | Exact L_k | independent named BRC |
|---:|---:|---|
| 7 | 78,710,035 | equal |
| 8 | 4,076,647,030 | equal |
| 9 | −215,329,002,630 | equal |
| 10 | 7,724,818,416,180 | equal |
| 11 | −146,088,496,994,110 | scalar certificate only |
| 12 | −815,898,004,254,020 | scalar certificate only |
| 20 | 2,654,805,287,682,237,859,503,700,820 | scalar certificate only |

The independent dynamic program prunes a partial path only if its native L1 distance from the root exceeds its remaining step count; this cannot discard a closed loop. All executed integer assertions pass, and every odd formal coefficient to degree 40 is zero.

By PREFIX-1009, these also yield stabilized grade-resolved **signed totals** \(S_{n,k}=-L_k/6^{2k+1}\) for k≥1 and n≥2k+1; for example \(S_{n,7}=-78710035/470184984576\) for every n≥15. This is not a squared norm.

Reproduce with standard-library Python script PREFIX1010_R6_RANK_TWO_GREEN_CHECK.py; it generates PREFIX1010_R6_EXACT_RESULTS.json. The script uses exact integers and rational counting coefficients; no floating point, external trigonometry, π expansion, classical comparison, or matrix exponential. The full 0…20 coefficient list is in the attached JSON.

## Scope, references, provenance and next scientific unit

The original frozen P000 and candidate Stage46 BRC assumptions remain in force. This theorem gives an exact **final rooted-return scalar** reduction; a later terminal-port or paired-history observer needs its named states or a separately proved repair. Independent mathematical Review and physical calibration remain open.

Source: prior [PREFIX-1009](https://github.com/awdawmip/enterprise-math/blob/2c73ee6b36f323301c8d673784613888f3f46424/research_notes/portable_direct/2026-11-22_r6_prefix1009_all_grade_rooted_link_renewal.md). Historical contribution reference R6 EM-DIRECT-FBEA5D / RA-3FB2D033BE6048D8712FF056 identifies earlier provenance, not this conversation's execution capability.

Next question: is there a one- or two-series closed scalar observer, and which irreducible joint-state corrections appear for the **squared** first-internal-layer probability? The mother question B_fix,odd(32)∈{19,20} stays open.

Status: AUTHOR_FORMAL_LAURENT_PROOF / EXACT_INTEGER_CROSS_CHECKED / NOT_REVIEWED; standalone portable Source research only, no CLAIM, PROGRESS, formal Result or independent Review.