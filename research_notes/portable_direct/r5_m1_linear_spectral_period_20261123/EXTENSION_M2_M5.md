# R5 degree>=1 coefficient period: exact extension to thresholds 2, 3, 4, 5

Date: 2026-11-23 (Asia/Shanghai).
Status: **AUTHOR_EXACT_FINITE_FIELD_CERTIFIED / NOT_REVIEWED**.
Scope: unchanged frozen five-event scalar cost observer @75d986aa23b68a7ecf9b29dc1006f0e322b35a15.

## Result

The m=1 full linear-term coefficient period proved in `RESEARCH.md` persists at the next four positive thresholds:

\[
\boxed{M_m^{(\ge1)}=814202665467037976682352800
\quad \text{for each }m\in\{1,2,3,4,5\}.}
\]

The upper bound for all \(m\ge1\) is the denominator-root lcm \(\Lambda_1\), already proved in `RESEARCH.md` independently of all-threshold numerator cancellations. For the lower bound, the 18 selected primitive orders from that note all remain nonzero at each of \(m=2,3,4,5\), now with the **genuine simultaneous inequalities** and the **correct complete-homogeneous total-count numerator**. The same 18 orders have lcm \(\Lambda_1\), completing the exact-period conclusion for five individual thresholds.

## Exact inclusion/exclusion and disjoint-block calculation

Let \(A_m\) be the signed numerator for the union of the first three overlapping failure events \(E_0,E_1,E_2\), and \(B_m,C_m\) the separate numerators of the other two long-block failures \(E_3,E_4\). Because the three groups of price variables are pairwise disjoint, the full numerator of the union of all five events obeys the **polynomial identity**

\[
R_m(q)=1-(1-A_m(q))(1-B_m(q))(1-C_m(q)).
\]

For every nonempty mask \(I\subseteq\{0,1,2\}\), put \(U_I=\cup_{i\in I}S_i\) and
\[
P_{I,m}(q)=
\sum_{\substack{(a_p)_{p\in U_I}\in\mathbb Z_{\ge0}^{U_I}\\
\sum_{p\in S_i}a_p<m\text{ for every }i\in I}}
q^{\sum_{p\in U_I}pa_p}.
\]
Every \(a_p\) in \(U_I\) is bounded by \(m-1\), so this is a finite exact integer polynomial. Then
\[
A_m(q)=\sum_{\emptyset\ne I\subseteq\{0,1,2\}}
(-1)^{|I|+1}P_{I,m}(q)\prod_{p\in U_I}(1-q^p).
\]

The correct separate-block formula for \(T=S_3,S_4\) is
\[
H_{T,m}(q)=\Bigl(\prod_{p\in T}(1-q^p)\Bigr)
\sum_{j=0}^{m-1}h_j((q^p)_{p\in T}),
\]
where \(h_j\) is the complete homogeneous polynomial. Set \(B_m=H_{S_3,m}\), \(C_m=H_{S_4,m}\). To compute the prefix \(\sum h_j\) in a finite field, initialize \(h_0=1,h_{j>0}=0\); for each variable \(x=q^p\), update \(h_j\leftarrow h_j+x h_{j-1}\) in **ascending** \(j\), which permits arbitrarily many copies of each item and is exactly the product \(\prod_{p\in T}(1-x_pt)^{-1}\) truncated at degree \(m-1\). No invalid replacement by \(\prod_p(1-q^{mp})\) is made.

These formulas are exact in \(\mathbb Z[q]\), hence evaluating modulo any prime produces actual reductions of the frozen integer polynomial.

## Finite characteristic-zero obstruction certificates

Take the fixed 18 order/primality/primitive-root triples \((d,p,z)\) printed in `RESEARCH.md`. The companion code `VERIFY_M2_M5_LINEAR_PERIOD.py` calculates each \(R_m(z)\in\mathbb F_p\) by the formulas above. All \(4\times18=72\) exact values are nonzero; the table records them by row, with orders in increasing report order (the same order as `VERIFY_M1_LINEAR_PERIOD.py`):

| d | m=2 | m=3 | m=4 | m=5 |
|---:|---:|---:|---:|---:|
|32|5|93|53|79|
|54|105|29|66|92|
|25|73|96|93|90|
|49|187|28|25|80|
|11|9|5|15|12|
|13|35|12|9|44|
|17|15|13|12|95|
|19|124|25|149|3|
|23|22|4|20|8|
|29|7|5|11|40|
|62|75|171|117|57|
|37|138|127|38|121|
|41|74|47|52|1|
|43|140|62|128|90|
|47|127|244|202|136|
|59|507|240|594|350|
|61|351|324|10|115|
|73|231|26|104|206|

For each \(m\in\{2,3,4,5\}\) and each selected \(d\), nonzero \(R_m(z)\bmod p\) at a verified primitive root implies \(\Phi_d(q)\nmid R_m(q)\) over \(\mathbb Z[q]\), since polynomial division by the monic \(\Phi_d\) commutes with reduction modulo \(p\). Therefore \(F_m=R_m/D\) retains a pole of order \(n_d\ge2\) at that primitive complex root, so its degree-\(\ge1\) coefficient period is divisible by \(d\). Taking the lcm of 18 orders gives \(\Lambda_1\) for each \(m\), and the known universal upper bound proves equality.

This is a **finite exact proof for the four specified thresholds**, not an interpolation or claim about arbitrary future \(m\). All \(N\) are covered by the rational generating function and root-of-unity argument.

## Reproduction

Place `VERIFY_M1_LINEAR_PERIOD.py` and `VERIFY_M2_M5_LINEAR_PERIOD.py` in the same directory and run:
```
python3 VERIFY_M2_M5_LINEAR_PERIOD.py
```
The base module first certifies the primitive orders and m=1 values; the extension then enumerates all finite overlapping loads for m=2..5, computes the two disjoint complete-homogeneous blocks, and asserts the 72 tabulated residues and nonvanishing. Pure standard-library modular integers, no floating point. Author execution returned `PASS: m=1..5 attain Lambda_1=814202665467037976682352800` (local duration approximately 17 seconds).

## Next question and status

Determine the **first positive m** (if any) at which one of the new primitive orders ceases to contribute its degree-\(\ge1\) term, and formulate a residue-class / recurrence classification for all m without brute-force enumeration of \(m^8\) assignments. Extend the existing corrected six-cone rational threshold series and first-jet methods, respecting their true pole degree and the five event constraints. The existing all-m primitive-43 first-jet result remains reusable at its proved scope.

These are scalar quasipolynomial results only. Preserve P000/ACTIVE X6 semantics, do not collapse signed cyclotomic phases to positive BRC mass, and do not infer formal shared Task Result/Review/CLAIM from independent portable publication. Independent mathematics review remains `NOT_REVIEWED`.
