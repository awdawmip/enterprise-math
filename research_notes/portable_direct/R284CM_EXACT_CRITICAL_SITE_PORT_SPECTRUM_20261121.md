# R284CM — Critical-site reduction for all 64 finite Port covering thresholds

Date: 2026-11-21 (Asia/Shanghai). Scientific status: **AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED**. Independent portable continuation of R284CL; no native Task CLAIM, Result, Driver Review, BRC theorem admission, or P000 change is asserted.

## Frozen question and inputs

R284CL determines the 64 sharp finite-codeword support thresholds

[
U_k=\max_{x\in X} d_{(k)}(x),\quad k=1,\ldots,64,
]

where (X) is the set of the 65,536 frozen 34-bit Port codewords, (d_{(k)}(x)) is the (k)-th smallest circular distance from (x) to the 64 closed coarse-fiber arcs (A_j), and the circular modulus is (p=17,179,869,143). The original program uses (65,536\times64=4,194,304) exact point-to-arc distance evaluations.

Frozen Port parameters: (D=(1120832,6,13,1651128)), (Z=(0,390139,394465,1497639)), lower-coordinate selector ((0,1,2,4,5,6)). Ordered 8-byte codeword stream SHA-256:

`b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4`.

The original determinant encoder, complete codeword enumeration, and exact arc reconstruction remain those of the immutable R284CL checker; **no scientific input is rebased**.

## Theorem — finite-site critical-neighbor principle

Let (X\subset \mathbb{R}/p\mathbb{Z}) be any finite set and (A_1,\ldots,A_m) any closed circular arcs of lengths strictly between 0 and (p). Let (f_k(y)) be the (k)-th ordered value of the (m) functions (d(y,A_i)). Form the critical set (B) from:

1. the individual distance-function kinks (each arc's two endpoints and the midpoint of its complementary gap);
2. all isolated equalities (d(y,A_i)=d(y,A_j)) within intervals where both distances are affine;
3. one chosen circular cut, included at both ends of a linearized period.

For every critical position, retain its predecessor and successor in the ordered finite population (X), whenever present, including a site exactly at the critical position. Denote the resulting subset by (X_B). Then, **simultaneously for every** (k=1,\ldots,m),

[
\boxed{\max_{x\in X}f_k(x)=\max_{x\in X_B}f_k(x).}
]

A flat coincidence of two distance functions over an interval does not require extra critical positions; the tied ordered values remain affine on the entire interval.

### Proof

For any closed circular arc (A=[a,a+w]) oriented positively, the distance (d(y,A)) is zero on the arc, grows with slope (+1) from its exit endpoint to the midpoint of the complementary gap, and falls with slope (-1) until the next entry endpoint. It is therefore affine between the three indicated kinks.

Take the common refinement of all kink positions and all isolated pairwise equalities on these affine pieces. Inside each resulting open interval, every distance is affine and their weak ordering is unchanged. Identically equal affine functions remain tied; any change of a strict order would require an equality that has already been inserted as a boundary. Consequently each ordered statistic (f_k) is itself affine on that interval, for every (k).

An affine function attains its maximum on the finite (X)-points in one such interval at its leftmost or rightmost point. These are, respectively, the successor of the left boundary and predecessor of the right boundary in the sorted population. Points exactly on a boundary are themselves selected as a predecessor/successor. The period cut handles the first and last intervals. Taking the union over all intervals proves the equality for every (k) using the same selected set. QED.

This reduction depends only on exact distances and their order, not on an assumed uniform codeword distribution; it retains the original codeword value and original matrix-enumeration index for each witness.

## Exact critical-position arithmetic

Use the scaled coordinate (q=4y). On each piece (F_i(q)=4d(q/4,A_i)) is affine with slope in ({-1,0,+1}), taking integer values at the individual kink positions. For two affine pieces on ([l,r]), write their slopes (s_i,s_j) and left endpoint values (F_i(l),F_j(l)). Any isolated crossing satisfies

[
q=l-\frac{F_i(l)-F_j(l)}{s_i-s_j}.
]

Since (s_i-s_j\in\{-2,-1,1,2\}), every crossing has **integer (2q=8y)**. All breakpoints can therefore be represented without floating point as integer multiples of one eighth of the Port residue unit. An exact adjacent-pair segment scan generates the complete set; one does not need to sample real circle points.

## Exact frozen-model results

| Metric | Value |
|---|---:|
| Source codewords / distinct Port values | 65,536 / 65,536 |
| Coarse fiber arcs | 64 |
| Individual arc kink sites, excluding the period cut | 192 |
| Arc pairs inspected | 2,016 |
| Isolated crossing hits across pairwise segments | 4,105 |
| Distinct pairwise crossing locations | 4,055 |
| Flat pair-tie segments | 75 |
| **Distinct union breakpoints, including both cut endpoints** | **4,149** |
| **Distinct neighboring candidate codewords** | **6,007** |
| Reduced point-to-arc distance predicates | **384,448** |
| Full-population baseline predicates | 4,194,304 |

The reduced candidate set is (6007/65536\approx9.166\%\) of the finite population. The 64-level spectrum and **all 64 sharp radii match** the independent original exhaustive computation, not just the selected levels below.

| k | Exact (U_k) | Reduced-set witness: original matrix index / Port |
|---:|---:|---|
| 1 | 0 | 32745 / 41705 |
| 2 | 539127606 | 51531 / 3431128591 |
| 4 | 765801463 | 30792 / 3613932823 |
| 8 | 1236647378 | 50145 / 6612239517 |
| 16 | 2474503698 | 1616 / 5366504683 |
| 32 | 4633230194 | 10331 / 3566289776 |
| 54 | 7642302204 | 33760 / 6683583072 |
| 64 | 8436072374 | 19081 / 16943358802 |

Exact output SHA-256 digests (decimal values each followed by newline, sorted):
- (8y) critical positions: `b357e713c8eec3c072b904188b05cba9f6dc9e3e45f134e711d1481a92687a42`
- selected codeword values: `158738b19275f2b6d8dcc16797070ef28d678bbfc1705c6831e83b2a3c48a6a7`.

### Verification and interpretation

The companion Python checker reconstructs arcs from the original frozen R284CL source, recomputes the entire frozen codeword SHA-256, verifies the 65,536 Port residues are distinct, generates all critical locations using arbitrary-precision integers, selects the 6,007 neighboring sites, and computes all 64 levels and witnesses on those sites. It separately performs the original complete (65,536\times64) distance enumeration and asserts 64/64 exact equality. This is a finite exhaustive certificate plus a general analytic reduction theorem; no independent mathematical Review or external native execution is claimed.

**Cost boundary:** the 10.91-fold reduction applies to the count of point-to-arc distance evaluations **inside the threshold computation**. It does not include generating and sorting the original codewords, forming the 2,016 pairwise critical arrangements, locating candidate sites, or memory and implementation overhead. Thus it is not yet an end-to-end runtime speedup. The reduction also does not alter the 34-bit code, the original minimum distance 59, or the full matrix ±29 integer correction guarantee.

**Worldview and provenance boundary:** this is a frozen Port observer's exact finite residual calculation. Its circular coordinate is an auxiliary readout, not an assertion that a one-dimensional circle is an Enterprise native spatial plane or a complete X6 Cell state. No path/branch provenance or BRC claim is eliminated by this observer-level index. P000 and ACTIVE residual-fidelity rules remain unchanged.

## Reproduction, evidence and remaining question

- Parent frozen theorem: [R284CL](https://github.com/awdawmip/enterprise-math/blob/6679d7946e01549192ac113ab6b5c49074558a7b/research_notes/portable_direct/R284CL_FINITE_CODEWORD_SUPPORT_SPECTRUM_20261121.md).
- Frozen dependency: [R284CL exact checker](https://github.com/awdawmip/enterprise-math/blob/ff96f1dd28b5c64172706da8cb3236a23ae9d1aa/research_notes/portable_direct/R284CL_finite_codeword_support_checker.py).
- New checker: `research_notes/portable_direct/R284CM_critical_site_port_spectrum_checker.py`.
- New machine certificate: `research_notes/portable_direct/R284CM_critical_site_port_spectrum_certificate.json`.

Run from the research_notes/portable_direct folder with Python 3.8+:
`python R284CM_critical_site_port_spectrum_checker.py R284CM_critical_site_port_spectrum_certificate.json`.

The scientific frontier now permits three further independent questions: (i) reduce the number of pairwise breakpoints with k-specific envelope structure; (ii) explain the previously determined minimal doubled-radius full-circle/finite-population slack 786 at k=54 using the actual neighboring forbidden Port gaps; (iii) measure total initialization, sorting, pairwise arrangement, storage, and repeated-query cost against the 4,194,304-predicate baseline.

Historical Port lineage: EM-DIRECT-20B766; Activity RA-617F40704F37299B15489DCA. These are attribution references, not evidence that the present execution possesses the historical session's private native authority. Activity association and independent review are separate, currently pending.
