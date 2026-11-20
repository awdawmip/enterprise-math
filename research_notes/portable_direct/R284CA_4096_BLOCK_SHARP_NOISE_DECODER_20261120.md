# R284CA — Exact 4,096-block decoder for the 34-bit sharp-noise star-Port code

Date: 2026-11-20 (Asia/Shanghai). Scope: independent portable auxiliary finite algebra. Status: **AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED**. This is a continuation of the R284BZ frozen scientific input, not a native X6/BRC experiment, CLAIM, Result or Review.

## Scientific input and fixed parameters

For (C\in\{1,2\}^{4\times4}), retain the immutable R284BZ observation
[
F_C=\det(\operatorname{diag}(d_0,6,13,d_3)-C-\sum_{j=1}^3z_jE_{0j})\pmod p,
]
where
[
p=17179869143,\quad(d_0,d_3,z_1,z_2,z_3)=(1120832,1651128,390139,394465,1497639).
]
The row-major input has 16 binary-valued entries; a single cyclic residue is read with adversarial real circular error (0\le\rho<29.5). R284BZ had established the exact full-code minimum circular separation 59, using 65,536-entry nearest-center lookup. **This note changes the inverse/decoder representation only, not the scientific input.**

## The new theorem

There is an **exact lossless sorted index of only 4,096 entries** ((\beta_L,L)), where (L\in\{1,2\}^{12}) is the lower three rows and (eta_L) is the observation for the top row ((1,1,1,1)). Its four positive cofactor weights can be regenerated from (L), without storing 65,536 codewords.

For every circular real query (y\in\mathbb R/p\mathbb Z) and every radius (0\le\rho<29.5), the following two-stage decoder includes the correct lower block among its candidates and examines **at most 157 lower blocks** using a single global window. Filtering with the individual block span reduces this bound to **at most 128 lower blocks**, so at most **2,048 possible full matrices** require arithmetic evaluation and a final nearest-center test. If (y) is within the specified noise radius of one codeword, exactly one complete matrix is returned.

This is a certified *index-size / worst-case candidate-count* improvement, not a claim of lower CPU latency than binary search on a materialized 65,536-entry lookup table. The 4,096 index entries retain a 34-bit base residue and a 12-bit block ID; all four coefficients are computed on demand. Ignoring physical array/allocator overhead, this is 188,416 stored bits versus the naive full table's 65,536 × (34-bit residue + 16-bit matrix ID) = 3,276,800 bits. A conventional full table might also use other compression schemes.

## Algebraic proof of the inverse representation

For each fixed lower block write
[
L=(u_1,A_{11},x,y_0,u_2,w,A_{22},z,u_3,g,h,r),
\quad T=6-A_{11},\quad S=13-A_{22},\quad U=TS-xw.
]
Let
[
V=-rU-z(Th+xg)-y_0(wh+Sg),\quad
p_1=Su_1+xu_2,\quad p_2=Tu_2+wu_1,
]
[
q_1=-rp_1-u_1zh+xzu_3+y_0(u_2h+Su_3),
]
[
q_2=-rp_2+Tzu_3+u_1zg+y_0(wu_3-u_2g),
\quad q_3=Uu_3+p_1g+p_2h.
]
The four top-row cofactor weights are
[
k_0=Ud_3+V,\quad k_1=p_1d_3+q_1,\quad
k_2=p_2d_3+q_2,\quad k_3=q_3.
]
Writing (C_{0j}=1+e_j), (e_j\in\{0,1\}), the exact determinant identity is
[
\boxed{F_C\equiv\beta_L-\sum_{j=0}^3e_jk_j\pmod p},\qquad
\beta_L\equiv d_0k_0-z_1k_1-z_2k_2-z_3k_3-\sum_{j=0}^3k_j\pmod p.
]
This follows directly from multilinearity of the determinant in its first row; the displayed weights are its four signed cofactors. For the complete 4,096 lower blocks, exact integer enumeration establishes
[
k_0\in[66044964,97416474],k_1\in[19813523,46231612],k_2\in[8255634,23115806],k_3\in[59,196].
]
All are strictly positive. Thus with (s_L=\sum_jk_j), all 16 observations associated with (L) lie in the oriented circular arc ([\beta_L-s_L,\beta_L]). The exact span bounds are
[
\boxed{97416474\le s_L\le161810643=:s_{\max}}.
]
No cofactor approximation or floating-point algebra is involved.

## Query algorithm and global candidate bound

Keep pairs ((\beta_L,L)) sorted by the first coordinate on the circle. Use ordinary lower-bound / upper-bound binary searches on the sorted base residues and their (pm p) copies to find all (L) such that
[
\beta_L\in[y-29.5,\ y+s_{\max}+29.5]\pmod p.
]
Next retain only blocks obeying the sharper individual interval
[
\beta_L\in[y-29.5,\ y+s_L+29.5]\pmod p.
]
For each surviving (L), regenerate the four (k_j), evaluate the 16 top-row choices, and retain centers with circular distance less than 29.5 from the query. If the actual observation error is (\rho<29.5), the true block cannot be pruned: its codeword is of the form (\beta_L-\sum e_jk_j) and the sum is in ([0,s_L]). By the previously certified global separation 59, there is at most one such matrix. This establishes correct adversarial real-error decoding for the fixed witness.

To certify a **uniform** work bound over *every real query location*, independently of sampled decoded words, form the 4,096 closed circular intervals
[
I_L=[\beta_L-s_L-29.5,\ \beta_L+29.5]\pmod p.
]
Count the maximum number of intervals covering a point of the circle with an exact endpoint sweep. Multiply all endpoints by 2: each is an integer; duplicate arcs into the range ([-p,2p]), clip to ([0,p]), and sort entries before exits at coincident endpoints (closed-interval semantics). The sweep proves
[
\boxed{\max_y\#\{L:y\in I_L\}=128}.
]
With every (s_L) replaced by (s_{\max}), the identical sweep gives **157**. These are exact finite maxima with endpoint witnesses at doubled coordinates 9226782847 and 9191072381 respectively. They cover real queries, not only queries arising from one of the 65,536 codewords.

## Independent reproducibility and limits

Run the companion standard-library checker:
`python research_notes/portable_direct/R284CA_grouped_port_decoder_checker.py`.
It exhausts all 4,096 lower blocks, enumerates all 65,536 full codewords, verifies the 34-bit predecessor checksum `b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4`, rechecks minimum cyclic gap 59 (64 attaining gaps), performs both exact global sweeps, and tests prefilter inclusion for 196,608 integer-noise samples (all matrices at errors -29, 0, +29). It also explicitly enumerates surviving top rows in 4,797 selected decoder tests; correctness for all real errors follows from the algebraic interval proof and the exact gap certificate.

This is a *complete proof of the stated fixed-code representation and bounds*, accompanied by an exhaustive finite certificate. It does not prove a general 4,096-block decoder for other star-Port parameters, an improvement over all compressed lookup methods, or a native physical observation. Mathematical independent review: **NOT_REVIEWED**.

## Provenance, control, and next question

Predecessor: `research_notes/portable_direct/R284BZ_34BIT_GLOBAL_SHARP_GAP59_PORT_20261120.md`; fixed frozen input witnessed at Git blob `7e81f28d26be9dc6a5b0f4956f11e8e55fe84066`; checker at Git blob `3884f2d7a4b56a8e76855d0488ba16d64c52c29b`. Prior contributor lineage `EM-DIRECT-E6B1DD`; this portable note asserts no current inherited native SID, CLAIM or Activity authority. Source-save and formal Activity are distinct.

The next mathematical question is whether one can replace binary-search interval enumeration by a direct residue-to-lower-block inversion using the block cofactor structure, or find a 33-bit-or-less gap-59 witness under the original frozen controls. A fair runtime comparison must include 4,096-index construction, on-demand (k_j) reconstruction, worst-case candidate arithmetic, and full lookup construction.
