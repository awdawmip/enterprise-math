# R32 — Direct Stern–Brocot / Farey bulk compiler of maximal affine risk runs

Date: 2026-11-10. Status: author-side mathematical proof and exact finite computation; independent review pending. Frozen scientific input: 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Predecessors: R31 (9bfccb2650cab28b88c21bc749295722e7134ad2), R27 (6cfd0bf078b3bd05fbd4c51508a868a4706a5823).

## Mathematical object and goal

This result concerns the **auxiliary irrational-circle observation model**, with 128 historical phase cuts \(x_t=\{t\theta\}\), \(0\le t<128\). It does not assert transfer to the native X6 heartbeat dynamics. For total cut count \(n\ge128\), let \(M_n(I)\) be the largest surviving phase subinterval within each original historical gap \(I\), and let
\[
R_n=1-\sum_I M_n(I).
\]
Fix the **open** enclosure
\[
L=\frac{262204504569236716045286}{10^{24}}
<\theta<
U=\frac{262204504569236716045287}{10^{24}}
\]
and the horizon \(N=10^{12}+128\). Construct the exact risk function over all integer \(128\le n\le N\), as maximal intervals of affine increments, without enumerating one trillion phase cuts or the 9,697 positive event rows in predecessor R27.

## Lemma 1: exact Stern–Brocot stage generation

Start at the Farey neighbors \(0/1<\theta<1/1\). For current adjacent fractions \(a/q<\theta<c/j\) with \(cq-aj=1\), test their mediant \((a+c)/(q+j)\) against the entire enclosure \(L<\theta<U\). If the mediant lies strictly below \(L\), replace the lower fraction; if it lies strictly above \(U\), replace the upper fraction. Every comparison in the finite run is unambiguous at both rational endpoints.

Exactly 11 comparisons reach
\[
\frac{27}{103}<\theta<\frac{16}{61},
\quad 103+61=164>128.
\]
At a current Farey pair, the stage ends at total cut count \(n=q+j\), truncated if \(n>N\). When the stage end is below \(N\), advance one mediant and start the next stage at \(q+j+1\) (using the updated pair). The remaining 77 comparisons generate a total of **78 stages** including the final truncated one. The finite exact program checks the determinant, all strict inequalities and stage continuity.

## Lemma 2: positive-event blocks from the near-return source template

The R31 directional-clearance theorem establishes for the fixed 128 historical cuts and suffix window \(H=164\):
\[
\rho_+(\theta)=164\theta-43,\qquad
\rho_-(\theta)=59-225\theta,
\]
and the last surviving long-gap source ages consist of
\[
\mathcal A=\{1,\ldots,61\}\cup\{98,\ldots,164\}.
\]
For all 75 Farey stages after the three short initial stages, exact rational-endpoint checks prove
\[
q\ge164,\quad j\ge292,\quad
0<v=c-j\theta<59-225\theta.
\]
Consequently, the R31 source-owner correspondence identifies for each historical interval the final long-gap source as \(t=j-r\) for exactly one \(r\in\mathcal A\). With \(u=q\theta-a>0\), the long gap \(w=u+v\) splits when total cut count reaches
\[
n=q+t+1=q+j-r+1,
\]
contributing exactly \(\min(u,v)\) to the risk increment. All other cuts in the same historical interval and stage contribute zero. The two continuous positive event blocks in each stage are thus
\[
[q+j-163,\ q+j-97],\qquad
[q+j-60,\ q+j],
\]
intersected with its actual valid cut range. At every event-bearing stage, the strict enclosure confirms **one common choice** of \(u\) or \(v\) for \(\min(u,v)\) over the full parameter interval.

Of the 75 eligible stages, 74 contain 128 events in two blocks; the last one is cut by the finite horizon before any positive event. In that last event-free stage, the comparison \(u\) versus \(v\) varies across the enclosure; no amplitude is selected or claimed for nonexistent events.

## Lemma 3: bounded prefix and maximal affine integration

For the finite initial prefix \(129\le n\le389\), insert only 261 cuts and directly compute maximum subgaps in each of 128 historical intervals by sorting exact phase residues for each rational endpoint. Both endpoints choose identical integer-affine gap expressions, so the corresponding risk increments are valid for the entire open enclosure. The maximal prefix increment blocks are:
\[
\begin{array}{c|c}
129\ldots164 & 16-61\theta\\
165\ldots292 & 164\theta-43\\
293\ldots328 & 0\\
329\ldots389 & 164\theta-43
\end{array}
\]
For every subsequent Farey stage, emit two positive contiguous blocks and their intervening zero blocks directly, merge adjacent blocks having equal affine increments, and integrate from \(R_{128}=0\) to the output intervals. Every final run is maximal because consecutive runs have distinct increment coefficients; boundaries and cumulative risk have explicit integer values.

## Exact finite result and verification scope

- 88 strict Stern–Brocot mediant comparisons (11 startup, 77 subsequent).
- 78 Farey stages across \(128\le n\le10^{12}+128\).
- 261 individually evaluated initial-prefix updates, thereafter **148 positive block emissions**, not 9,697 event rows.
- **298 maximal integer-affine runs** (150 positive-increment runs, 148 zero-increment runs).
- Final risk:
\[
\boxed{R_{10^{12}+128}
=-4017401528447+15321634290944\,\theta.}
\]

The standalone Python standard-library exact verifier in VERIFY_R32.py produces all 298 rows of AFFINE_RUNS_R32.tsv and checks their canonical SHA-256 against the independently preserved R27 reference:
2573a84999d53dfd1cce772c45a41abaff251da735171efe904c860f2b2294f6.

An expanded local verifier independently compared all 78 stage rows and all 298 output runs against R27's preserved exact sources, with byte-for-byte agreement. The source program uses exact integer arithmetic and only the given rational endpoints; floating point determines no ordering.

## Complexity and boundary

For the **fixed S23 input**, after the stated bounded prefix and Stern–Brocot generation, interval emission/integration takes \(O(S+K)\) exact arithmetic operations for \(S=78\) stages and \(K=298\) output runs. Bit costs depend on \(\log_2(10^{24}N)\) and the largest affine coefficient, and include strict comparison, intermediate arithmetic and result serialization. A general complexity claim for arbitrary irrational inputs also must account for rational enclosure generation and unbounded continued-fraction partial quotients. Naive mediant-by-mediant iteration is not universally logarithmic.

This is **author-side proof plus exact finite verification**. Independent mathematics review, task Result/Review admission and any native-X6 model transfer are outstanding. The research branch/Draft PR is not merged canonical mathematical authority; no shared Task CLAIM or P000 change is asserted.

## Next discriminating research unit

Replace the 261 prefix-cut reconstruction by exact rank/select or floor sums; accelerate Stern–Brocot continued-fraction partial quotients without a mediant-by-mediant loop. Prove a variable-\(m\), variable-enclosure output-sensitive **bit-complexity** statement and cross-check it on an independent irrational rotation / historical-cut count. Reuse immutable verified results and preserve the BRC source-owner identities.
