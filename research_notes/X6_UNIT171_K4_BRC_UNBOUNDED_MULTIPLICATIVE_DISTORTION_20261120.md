# X6 Unit171 — Unbounded multiplicative distortion of native BRC under K4 residual, length and quadratic compression

Date: 2026-11-20 (Asia/Hong_Kong). Parent PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905. Task RS-X6-LEGACY-PLANE-RECONCILIATION, publication TP2-B4A441B23DA3159232C2. Research author EM-X6-FB6990, SID MCP-082892eb480e45dea6d4b9fcc0491034, logical Research conversation chatgpt-research-onhour-enterprise-math-20260923. Status: AUTHOR_PROVED / EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED.

## Frozen sources and typing

Scientific input remains awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03; historical comparison remains @fd2bcff10ca6e147348b6c1236027fc0d2877df3. Reuse Unit170's actual frozen producer src/enterprise_math/tetrahedral_endpoint_sum.py (blob 9f5098f7ba6995340406b39125b735cdba71fd4f, lines 49–64, 88–96, 114–165) and tested consumer tests/test_tetrahedral_endpoint_sum.py (blob d5cf7d4fa1405eca8245baa143334e282ee8fb26, lines 4–20, 36–72). The actual consumer preserves the integer vertex lift; no defective consumer is asserted.

Work in E0 = {x in Z^6: sum(x_i)=0}, with K4 edge order (12,13,14,23,24,34). For v in V0 = {v in Z^4: sum(v_i)=0}, set
\[
\delta(v)=(v_1+v_2,v_1+v_3,v_1+v_4,v_2+v_3,v_2+v_4,v_3+v_4).
\]
The derived K4 residual is
\[
C(x)=(x_{12}+x_{34},\,x_{13}+x_{24},\,(x_{12}+x_{13}+x_{14})\bmod2).
\]
Apply the signed native-six-axis shortest word formula only as an expressly typed **comparison** under a specified bijection of the six edge labels with six signed coordinate labels; this is not a physical identification of a K4 edge and an original X6 direction:
\[
L(x)=\sum_i|x_i|,\quad Q(x)=\sum_i x_i^2,\quad
B(x)=L(x)!/\prod_i|x_i|!.
\]

## New exact theorem

There exists **no universal finite multiplicative approximation factor K** for a positive estimator F(C,L,Q) of B over all x in E0. More quantitatively, for every positive integer m the pair
\[
\begin{aligned}
x_A(m)&=(-3m,-3m,0,0,3m,3m)=\delta(-3m,0,0,3m),\\
x_B(m)&=(4m,m,m,-m,-m,-4m)=\delta(3m,m,-2m,-2m)
\end{aligned}
\]
has equal observer readings C(x_A)=C(x_B)=(0,0,0), L(x_A)=L(x_B)=12m and Q(x_A)=Q(x_B)=36m^2, yet
\[
\boxed{\frac{B(x_B)}{B(x_A)}
=\left(\prod_{i=1}^{m}\frac{(m+i)(2m+i)}{i(3m+i)}\right)^2
\ge (9/4)^m.}
\]
Thus any estimator based on this common readout requires multiplicative error factor at least \((3/2)^m=(3/2)^{L/12}\) for one of the two assignments.

## Complete all-integer proof

Both displayed vertex vectors have coordinate sum zero, and expanding the signless incidence yields exactly the displayed six-tuples. Their opposite-edge matching sums vanish and first STAR sums are even, hence both K4 residual codes are zero. Four entries of absolute magnitude 3m in x_A give L=12m and Q=36m²; the two entries of magnitude 4m and four of magnitude m in x_B give the same L and Q. Counting shortest signed-six-axis ordered words gives
\[
 B_A=\frac{(12m)!}{(3m)!^4},\qquad
 B_B=\frac{(12m)!}{(4m)!^2(m!)^4}.
\]
Dividing and taking the positive square root gives
\[
 \sqrt{B_B/B_A}
 =\frac{(3m)!^2}{(4m)!(m!)^2}
 =\prod_{i=1}^{m}\frac{(m+i)(2m+i)}{i(3m+i)}
 =\prod_{i=1}^{m}\left(1+\frac{2m^2}{i(3m+i)}\right).
\]
For every integer 1≤i≤m we have i(3m+i)≤4m², so each factor is at least 3/2. Taking the product establishes B_B/B_A≥(9/4)^m. Since any F reads identical C,L,Q for these two inputs, if B/K≤F≤KB held for both, dividing the inequalities would require B_B/B_A≤K², forcing K≥(3/2)^m. Unbounded m makes a uniform finite K impossible. All arithmetic is integer/factorial or positive rational; no asymptotic approximation is required.

## Independent reproducible evidence

Executed locally in CPython normal, -O and -OO with identical JSON bytes. The exact finite checker exhausts each integer m=1..32, verifying both incidence assignments and C,L,Q, comparing signed multinomial factorial values with independent successive binomial interleaving values, and checking the exact rational factorial-product identity plus lower bound. Results: 32 successful pairs; zero violations. This is finite execution support, while the theorem follows from the proof.

Checker path: research_checks/X6_UNIT171_K4_BRC_APPROXIMATION_NO_UNIFORM_FACTOR_CHECK_20261120.py (Git commit 5c0790fd5221acff8a0ccb911736fdfcec287f59; locally executed SHA256 af44847bb2e70e492d1b483b0358b6ec4ed35a9acb98ae2d017e2597cd551181).
Certificate path: research_checks/X6_UNIT171_K4_BRC_APPROXIMATION_NO_UNIFORM_FACTOR_RESULTS_20261120.json (Git commit d9469906f8111755f5bad6bd668de732e35d3c82; locally executed SHA256 67816e8596bc1457e27dfe598fe38d72b7922cafbf8c3b3bb6257ba77b57431a).

For m=1, B_A=369600, B_B=831600 (ratio 9/4); for m=2, ratio 2025/196; for m=3, ratio 7056/121. No R063 benchmark was rerun.

## Mother-goal consequence and remaining obligations

Existing K4 residual mathematics and the actual source's exact vertex lift remain valid and unchanged. Unit171 quantitatively strengthens Unit170's one fixed nonfactorization witness: even retaining exact length and quadratic readouts, the compressed residual does not support **uniform-factor approximate** recovery of native shortest-word mass over arbitrary integer states. Retain the full integer lift or a provably adequate information carrier for native BRC.

Still unresolved: exact defective historical LP011 signed argmax and LP019 positive N-BRC subtraction commit:path:line (never invent them); remaining 28-LP source-to-actual-consumer coverage; historical Units149–152 native linkage; independent Driver review and Result. Unit170 original pending Native request onhour-20261120-0305-x6-own-unit170-native-progress-v1 must be consumed by its original ID, not replayed; Unit171 at this stage is author evidence only until its own valid native semantic PROGRESS and Source authentication. P000 unchanged; Research and maintenance lanes remain separate.
