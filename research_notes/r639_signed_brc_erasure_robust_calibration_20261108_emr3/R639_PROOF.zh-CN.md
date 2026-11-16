# R639｜六轴 BRC 背景校准的 Smith 精度定理与单参照失效容错

Date: 2026-11-08. Status: AUTHOR_SIDE_EXACT_DERIVATION / UNREVIEWED / NOT_ADMITTED.
Scientific source: frozen R462 @ 18783e01e3646c72b7aab3b16d3f565e83e6446f; signed K generation reused exactly from R638. Predecessor R638 @ 496a84ba9e00089d443d560cc8e3da1863b422e5. P000 and ACTIVE worldview unchanged.

## Exact question and model

Six original native X6 axes serve as **indices** of a static auxiliary observer. Their fixed calibration abscissae, **not native coordinate directions**, are \`c=(0,5,1,2,3,4)\`. Let \`1<=q<=6\` and for each axis \`x\` define an integer-polynomial nuisance
\[
H_x(t)=\sum_{k=0}^{q-1}c_x^k H_k(t),\qquad H_k\in\mathbb Z[t].
\]
The signed frozen branches satisfy \`P_j=K_(2j-1)=t^(2j-2)U_j\`, \`M_j=K_(2j)=t^(2j-1)V_j\` with positive-side initial coefficients \`(2,-8,6,106,83,9)\`, all units mod 5. As in R638, \`Y_x^+=A_x^+P_j+H_x\`, \`Y_x^-=A_x^-M_j+H_x\`, with unknown assignment \`j\` a permutation, \`nu_t(A_x^+ mod 5)=a>=1\`, \`nu_t(A_x^- mod5)>=a-1\`. A matched background-only reference at axis x is \`R_x=H_x\`. All available coefficients are read modulo \`5^N\` through degree d.

**Two different problems are distinguished:** (i) recover every unknown background coefficient \`H_k mod5\` uniformly, and (ii) recover all six BRC directions once that background is known. Optimality claims about (i) are not silently promoted to necessity for (ii).

## Theorem 1 — exact p-adic information threshold for general integer calibration

Let \`C\in Z^{m×q}\` be of full column rank over \`Q\` and let \`p\` be a prime. Write a Smith normal form \`U C V=diag(s_1,...,s_q)\` padded with zero rows, with integer unimodular U,V, and let \`e=max_i v_p(s_i)\`. From \`C h (mod p^N)\` one can recover \`h (mod p)\` for **every integer vector h** if and only if
\[
\boxed{N\ge 1+\max_i v_p(s_i).}
\]

Proof: U,V are automorphisms over Z/p^N and modulo p. In diagonal coordinates, equality of two observed vectors requires \`s_i \Delta z_i =0 (mod p^N)\`; this forces \`\Delta z_i=0 (mod p)\` for every i exactly when \`N>v_p(s_i)\` for all i. If \`N<=e\`, alter only a diagonal coordinate corresponding to \`e\` by 1; the observation remains equal modulo p^N while the underlying vector changes modulo p. This proves necessity as well as sufficiency. The same proof applies coefficientwise to arbitrary integer polynomials.

**Useful scope refinement:** The determinant valuation \`v_p(det C)\` of a square matrix is a sufficient digit tax, but in general need not be the *minimum*. For example at p=5 the nodes 0,5,10 give \`C=((1,0,0),(1,5,25),(1,10,100))\`, \`det C=250\` with valuation 3, whereas Smith valuations are \`(0,1,2)\`; the minimum is \`N=3\`, not 4.

## Theorem 2 — all 63 nonempty subsets of the R638 axes

For a calibration set S of exactly q distinct selected axes, let \`C_S=(c_x^k)_{x\in S,0<=k<q}\`. Then
\[
\boxed{N_{\min}(S)=
\begin{cases}2,&\{1,2\}\subseteq S,\\1,&\text{otherwise},\end{cases}}
\]
where axes are one-based and correspond to \`c_1=0,c_2=5\`. This is an **if and only if** statement for recovering all \`H_k mod5\` from q references.

Proof: \`det C_S=\prod_{x<y\in S}(c_y-c_x)\` with the rows taken in selected axis order. Among the six numbers the **only** pair congruent modulo5 is (0,5), and its difference has valuation exactly 1. All other pairwise differences are units modulo5. Thus \`v_5(det C_S)\` is either zero or one. The Smith exponents are nonnegative and sum to that valuation, so the largest exponent is the same, proving the formula by Theorem 1.

For every exceptional S containing axes 1 and 2 the lack of a mod5 inverse has an explicit certificate: the nonzero polynomial
\[
f_S(z)=z\prod_{x\in S\setminus\{1,2\}}(z-c_x)
\]
has degree q−1 and leading coefficient one, but \`f_S(c_x)=0 (mod5)\` for **every** selected axis. Taking the q coefficients of \`f_S\` as a difference in \`(H_0,...,H_{q-1})\` changes the background modulo5 and leaves all references modulo5 unchanged. Conversely \`N=2\` suffices by the Smith argument or exact adjugate division. For nonexceptional sets \`det C_S\` is a unit modulo5.

Enumeration of all \`C(6,q)\` sets:

| q | #sets | N=1 (mod5) | N=2 (mod25) |
|---:|---:|---:|---:|
| 1 | 6 | 6 | 0 |
| 2 | 15 | 14 | 1 |
| 3 | 20 | 16 | 4 |
| 4 | 15 | 9 | 6 |
| 5 | 6 | 2 | 4 |
| 6 | 1 | 0 | 1 |
| **total** | **63** | **47** | **16** |

## Theorem 3 — one-erasure calibration with q+1 references

Choose a set S of q+1 axes; any ONE reference may be lost without advance notice. After its loss, reconstruct all q background coefficients mod5 from the remaining q references. For \`1<=q<=5\`, define the worst-case minimum digits
\[
N_{\rm erase}(S)=\max_{x\in S}N_{\min}(S\setminus\{x\}).
\]
For q=1 every pair works at N=1. For \`2<=q<=4\`, \`N_{\rm erase}=1\` iff the selected set does **not** contain both axes 1 and 2. For q=5 the only six-axis selection has \`N_{\rm erase}=2\`, which is achieved.

Proof: if q>=2 and both 1,2 are selected, removing one of the remaining q−1 axes leaves an exceptional q-set and requires N=2. Otherwise every surviving q-set contains at most one member of {1,2}, and N=1 by Theorem 2. The q=1 case is immediate. All q+1 choices are exhausted because there are only six axes.

| q | q+1 selected references | robust N=1 sets | robust N=2 sets |
|---:|---:|---:|---:|
| 1 | 2 | 15 | 0 |
| 2 | 3 | 16 | 4 |
| 3 | 4 | 9 | 6 |
| 4 | 5 | 2 | 4 |
| 5 | 6 | 0 | 1 |

For instance, when q=4, the **only** mod5 single-erasure-robust sets of size 5 are axes {1,3,4,5,6} and {2,3,4,5,6}. When q=5, all six references and mod25 precision tolerate any single loss.

## Signed BRC consequence and evidence scope

If a selected reference subset has its stated sufficient N, use the recovered \`H_k mod5\` to subtract each \`H_x mod5\` from \`Y_x^+\`. The signed BRC positive orders are exactly \`a,a+2,a+4,a+6,a+8,a+10\`; their initial coefficients are 5-units. Hence \`d=a+8\` identifies the first five labels and the permutation determines the sixth, uniformly for all 720 assignments and all legal backgrounds/gains.

This **proves a sufficient orientation-recovery protocol** using the exact minimum digits for full background recovery. It does not assert that the same digits are necessary for orientation with arbitrary use of all \`Y^\pm\`; this is a distinct question.

Verification: \`R639_REPRODUCE.py\` reconstructs the frozen signed K leading branches from the exact inherited binomial formula and uses integer Bareiss determinants/adjugates, modular arithmetic, all 63 subsets, 16 explicit coefficient-kernel certificates, all 186 single-erasure survivor cases, 2,112 integer coefficient recovery checks and 136,080 permutations/parameter triples. Marker: \`R639_VANDERMONDE_ERASURE_EXACT_PASS\`. All tests are exact integers; the theorems are supplied by the arguments above.

**BRC: REUSE_APPLIED** — signed branch provenance and observation model from R462/R638. This is a static auxiliary observation theorem with X6 labels, not an assertion that the current native X6 field operator implements the polynomial nuisance or supplies matched undisturbing references.

## Exact next scientific question

Extract one *registered actual* PF10/triadic-field/native X6 operation, its source/branch/path-preserving field update and its observer. Test whether its nuisance coefficient map factors through a finite-rank integer matrix C and whether matched background-only references exist before/after one legal update. Calculate the actual Smith invariants if an integer map is established; otherwise give a small typed operator-level obstruction/counterexample without fitting artificial c-values.