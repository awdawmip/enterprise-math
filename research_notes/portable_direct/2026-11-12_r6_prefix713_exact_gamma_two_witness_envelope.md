# PREFIX-713-R6 — Exact Gamma-clock witness improvement and four new symmetric fine-cell certificates

Date: 2026-11-12 (Asia/Shanghai).  
Scientific input pin: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.  
Parent target: PREFIX-675; immediate verified predecessor: PREFIX-712, with the corrected Gamma maximum kernel from PREFIX-710.  
Status: AUTHOR_RECOMPUTED / EXACT_INTEGER_GAMMA_KERNEL / UNREVIEWED / NOT_ADMITTED.  
Scope: the **auxiliary** two-coordinate statistical observer on (D=[0,1/2]^2), not a native X6 slice.

## 1. Definitions and exact kernel

The pinned 189-row integer recursion defines stopping-count survival probabilities (s_n(p)=P(N_p>n)), (0\le n\le188). Given (N_p=k), the completion clock (T_p) has a Gamma(k,1) law. For two independent clocks let (Y(p,z)=\max(T_p,T_z)), (\mu(p,z)=E[Y]), (W(p,z)=\operatorname{Var}(Y)), (V_q(p,z)=q^2W-q\mu).

The exact Gamma kernel is
[
c_{nm}=\binom{n+m}{n}2^{-(n+m+1)}.
]
The moments are
[
\mu(p,z)=\sum_n s_n(p)+\sum_m s_m(z)
-\sum_{n,m}c_{nm}s_n(p)s_m(z),
]
[
E[Y(p,z)^2]=2\sum_n(n+1)s_n(p)+2\sum_m(m+1)s_m(z)
-\sum_{n,m}(n+m+1)c_{nm}s_n(p)s_m(z).
]
Thus (W=E[Y^2]-\mu^2). All values at rational parameters are rational. The verifier rebuilds the 189 rows and their 9,529 nonzero count cells with integer arithmetic, retaining the historical width predicate exactly.

## 2. Theorem 713.1 — uniformly better exact rational witness

The old witness is (e_0=(0,3/20)). Define (e_A=(0,149/1000)) and (e_B=(0,146/1000)). The exact integer Gamma recursion yields
[
\boxed{W(e_A)-W(e_0)>5224/100000}
]
and
[
\boxed{\mu(e_0)-\mu(e_A)>5474/10000}.
]
Consequently, for every real (q\ge2) (indeed (q>0)),
[
\boxed{V_q(e_A)-V_q(e_0)>
  (5224/100000)q^2+(5474/10000)q>0.}
]
This improves the actual lower bound for the parent global optimum over **all** real (q\ge2), not merely over a finite sample. Every cell excluded by the old fixed-witness certificate remains excluded by the new witness, with an additional strict gap.

For (t=1/q\in[0,1/2]), define the stronger two-witness envelope
[
P(t)=\max\{W(e_A)-t\mu(e_A),\,W(e_B)-t\mu(e_B)\}.
]
Since (W(e_A)>W(e_B)) and (\mu(e_A)>\mu(e_B)), the two affine branches cross exactly at
[
t_*={W(e_A)-W(e_B)\over\mu(e_A)-\mu(e_B)},
\qquad \boxed{23/100<t_*<24/100}.
]
Use (e_A) when (0\le t\le t_*) and (e_B) when (t\ge t_*). The exact crossing is algebraic (in fact rational), with numerical locator (t_*\approx0.233105650365), equivalently (q_*\approx4.289900302427). The finite envelope (P(t)) is a rigorous, q-adaptive lower bound on (H(t)=\max_{x\in D}(W(x)-t\mu(x))).

## 3. Theorem 713.2 — eight more ordered 384-grid cells than PREFIX-712

Partition (D) into (384\times384) cells, whose coordinates have denominator 768. For a cell with lower-left corner (a) and upper-right corner (h), set
[
U(a,h)=E[Y(h)^2]-\mu(a)^2,\qquad
L_e(t)=W(e)-U(a,h)-t(\mu(e)-\mu(a)).
]
The previously established coordinatewise survival-tail order implies (W(x)\le U(a,h)) and (\mu(x)\ge\mu(a)) throughout the closed cell. Since (L_e(t)) is affine, the exact endpoint inequalities (L_e(0)>0) and (L_e(1/2)>0) exclude this entire cell for all real (q\ge2).

The newly checked cells, represented as their lower-left integer indices ((i,j)) with ((p,z)=(i/768,j/768)), are
[
(28,88),\quad(34,91),\quad(57,163),\quad(74,138).
]
For each, the former (e_0) endpoint certificate fails, while both exact endpoint tests with (e_A) pass. Here are **strict lower bounds** for the new margins, with unit (10^{-6}):

| Cell ((i,j)) | floor\((10^6L_{e_A}(0))\) | floor\((10^6L_{e_A}(1/2))\) |
|---|---:|---:|
| (28,88) | 8875814 | 40727 |
| (34,91) | 7784125 | 155041 |
| (57,163) | 33678 | 16482396 |
| (74,138) | 23837 | 9040883 |

The Gamma-clock distribution is symmetric under interchanging the two independent streams, hence the four transposed cells also pass. All eight ordered fine cells were absent from PREFIX-712's union because the original fine-cell tests failed; a certified coarse parent would imply certification of all its children.

PREFIX-712 already certified 137,168 of 147,456 ordered fine cells. The union of its old certificate with these eight newly proven disjoint cells therefore covers **at least**
[
\boxed{137176/147456=17147/18432\approx93.0284288194\%}
]
of the full auxiliary square, uniformly for all real (q\ge2). This is a **verified lower bound**, not a claim of exhaustive maximal coverage under the new witness; a complete fresh full-grid scan could find additional cells. The absolute improvement is eight fine cells (an additional (8/147456) of (D)). The mathematical increment is additionally the strict uniform witness domination and its q-adaptive two-branch envelope.

## 4. Actual checks, provenance and continuation

Local Python standard-library verifier A (`PREFIX713_R6_EXACT_TWO_WITNESSES.py`) rebuilt the frozen count rows, exactly evaluated the three rational Gamma witness moments and proved the two strict pointwise inequalities and crossing enclosure: `ALL_CHECKS_PASS PREFIX713-R6`.

Local exact cell checker B (`PREFIX713_R6_FINE_CELL_CERTIFICATES.py`) independently computed the Gamma kernel at eight distinct axes' required corner values and exactly checked the old failures/new endpoint successes for four cells: `ALL_CHECKS_PASS PREFIX713-FINE`. Its mirrored four cells follow from exchangeability. The machine-readable counts and finite tests are in `PREFIX713_R6_RESULTS.json`.

A broader uniform piecewise-witness exhaustive 192/384-grid attempt was not completed; no count is claimed from that attempt. The present certificate requires only the verified eight added cells and prior PREFIX-712 proof.

Next scientific unit: use the two-witness envelope (P(t)) with exact breakpoints to certify all remaining PREFIX-712 fine cells, then refine only truly unexcluded cells. Use the exact Gamma maximum kernel, not the invalid count-maximum substitution from PREFIX-709. Compare with interior stationary-point candidates to solve PREFIX-675's actual global optimizer problem. The result is author-checked research, not an independent Result/Review or promoted foundation.
