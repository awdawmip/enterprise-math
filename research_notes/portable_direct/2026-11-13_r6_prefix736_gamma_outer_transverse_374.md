# PREFIX-736-R6 — Certified outer Gamma transverse strip, 374 new whole cells

Date: 2026-11-13 (Asia/Shanghai). Parent research objective: PREFIX-675, exact global maximization of the frozen 189-row BRC stopped-count independent-Gamma auxiliary observer. Frozen scientific input: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.

**Scientific status:** AUTHOR_EXACT_FRACTION_CHECKED / SOURCE_FIELD_CROSSCHECK / UNREVIEWED / NOT_ADMITTED.

## 1. Exact new theorem

For the frozen model, let \(T_p,T_z\) be the independently sampled unit-rate Gamma clocks stopped according to its exact integer survivor kernel, \(Y=\max(T_p,T_z)\), \(\mu(p,z)=\mathbb E Y\), \(M_2(p,z)=\mathbb E Y^2\), \(W=M_2-\mu^2\), and \(V_q=q^2W-q\mu\).

Fix the comparison point \(e=(0,73/500)\). For **every real \(q\ge2\)**, every \((p,z)\) in any complete closed fine-grid cell
\[
[i/384,(i+1)/384]\times[j/384,(j+1)/384],
\quad 58\le i<70,\ 76\le j<96,
\]
and every point in the corresponding transposed cells, the strict inequality
\[
\boxed{V_q(e)-V_q(p,z)>\frac{q^2}{10}>0}
\]
holds. Consequently these 480 complete index cells (240 upper-strip cells and 240 distinct transposes) contain no global maximizer of the frozen two-parameter auxiliary Gamma objective for any real \(q\ge2\).

This is a complete **continuous-cell** inequality, not a discrete sample comparison.

## 2. Rigorous rational envelope

The stopped-survivor kernel provides coordinatewise monotonicity of \(\mu\) and \(M_2\), as verified in PREFIX-731. On a closed rectangle \(R=[a,c]\times[b,d]\), define
\[
L=\mu(a,b),\quad U=M_2(c,d)-L^2,\quad
\Delta=W(e)-U.
\]
Then \(\mu(p,z)\ge L\) and \(W(p,z)\le U\). Writing \(t=1/q\in(0,1/2]\),
\[
\frac{V_q(e)-V_q(p,z)}{q^2}
= W(e)-W(p,z)-t(\mu(e)-\mu(p,z))
\ge \Delta-t(\mu(e)-L)
\ge G(R),
\]
where
\[
G(R)=\min\{\Delta,\ \Delta-\tfrac12(\mu(e)-L)\}.
\]
This last inequality is exact because the lower envelope is affine in \(t\). The 189-row integer kernel and all comparisons use Python integer arithmetic and fractions.Fraction; no float enters a proof decision.

For each of the 240 fine-grid upper-strip cells, evaluate \(G\) on its entire closed cell; where that lower bound is at most \(1/10\), subdivide the cell into exactly four closed 768-grid subcells and take the minimum of the four bounds. The exact rational calculation verifies **all 240** with \(G>1/10\). Of them, 52 pass on the full cell and 188 on the four-subcell cover; none needs a further subdivision. The smallest verified lower-bound floor after multiplication by \(10^6\) is **110609** at cell \((67,88)\). Hence every certified lower bound is at least \(110609/10^6>1/10\). Symmetry of the Gamma pair transfers the inequality to the transposed cells.

For exact cell-by-cell lower-bound floors and the full selected subdivision map see PREFIX736_R6_OUTER_TRANSVERSE_374_RESULTS.json. PREFIX736_R6_OUTER_TRANSVERSE_374.py regenerates and checks these data from the frozen integer kernel.

## 3. Exact deduplicated union increment

The new strip sits outside PREFIX-733-A \([30,58)^2\), PREFIX-733-B \([50,70)^2\), and PREFIX-735's 70–75 transverse strip. All upper indices satisfy \(i<j\), so transposed cells are distinct.

For the older PREFIX-712 comparator \(e_0=(0,3/20)\), the exact full-cell affine endpoint criterion already certifies **53** of the 240 upper-strip cells; these and their transposes belong to the inherited prior certified union. The remaining **187** upper cells give **374** distinct new cells after reflection. The current original GitHub JSON source sets for PREFIX-713 coupled and multicompetitor, PREFIX-716, and PREFIX-718 were read and intersected with these proposed 374 cells; all four intersections are empty. Thus, relative to the inherited PREFIX-735 author union, the new exact index-set tally is
\[
140110+2(240-53)=\boxed{140484}.
\]
The resulting certified fraction is
\[
\frac{140484}{384^2}
=\boxed{\frac{11707}{12288}}
=95.2718098958333\ldots\%.
\]
There remain \(147456-140484=\boxed{6972}\) fine-grid cells outside the currently certified union. This is a certified *exclusion* count, not an assertion that the remaining cells contain the optimum.

## 4. Validation, source pins and reproducibility

- Independent local reconstruction of the 189-row stopped-count kernel gave exactly 9,529 nonzero survivor positions and reproduced all four PREFIX-731 SHA-256 numerator digests for the center and comparison mean/variance.
- Four disjoint local Python exact-Fraction 5-row scans (j=76..95) verified 240/240 complete cells, 52 full-cell plus 188 quarter-subcell covers, and the exact minimum floor 110609. Two separate exact old-witness scans gave 53 old PREFIX-712 overlaps.
- The current authorized GitHub connector read original PREFIX713_R6_RESULTS.json (blob 0a12cab85b186cda25df45591e50d7904836f7fa), PREFIX713_R6_MULTICOMPETITOR_RESULTS.json (4945aa30875a70ae047f7d9bef37aed48e1bfb7a), PREFIX716_R6_RESULTS.json (ea2e3df0da8c4713c531339ce735907ee607dac5) and PREFIX718_R6_RESULTS.json (af6a51b91e5bd1e3e5a884ad618e0c962c030674); source-defined sets had zero additional overlap with the 374 proposed new coordinates.
- The exact source-checking combined program is published alongside this note, but has **not yet been executed end-to-end on a complete checkout containing all four historical JSON dependencies**. Independent mathematical scans and source-field checks did execute. The recomputation and admission claims retain that distinction.
- The result is specific to the stated two-parameter **auxiliary Gamma observer**. An X6 Heartbeat-world native dynamics assertion would require an explicit embedding/readout and future-observer preservation bridge; this note makes no such transfer.

## 5. Next mathematical unit

Run the newly published combined program against all original checked-in JSON dependencies, compare its generated output byte-for-byte or semantically against the saved 240-cell evidence, then investigate the adjacent \(j\ge96\) strip and \(i<58\) boundary with adaptive rational envelopes. Deduplicate every proposed new coordinate against the whole inherited certificate union before publishing a further cumulative count. Formal shared CLAIM, Result and Review continue to depend on their current source-native authority receipts.
