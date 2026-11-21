# R5: all-threshold primitive seventh-root residual and sharp 420 carrier

Date: 2026-11-21. Evidence: **AUTHOR_EXACT_DERIVATION / EXACT_RATIONAL_CHECKED / NOT_REVIEWED**. Independent portable science only; no formal CLAIM/RUN/Result/Review. Frozen scalar nonadaptive R5 model: 256 labeled hypotheses, integer query prices 214–314, and the original 32,640-pair separation certificate, SHA-256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`, retained without recomputation.

Previous immutable seventh-root science: [m=1 theorem](https://github.com/awdawmip/enterprise-math/blob/370b02668a89384269aab77ac304eef0c485d981/research_notes/portable_direct/r5_seventh_root_m1_420_20261121/RESEARCH.md). The sets are
\[
S_0=\{214,\ldots,218\},\quad S_1=\{214,216,217,218,219,220,221\},
\quad S_2=\{215,\ldots,221\},\quad
S_3=\{223,\ldots,290\},\quad S_4=\{296,\ldots,312\}.
\]
For every fixed threshold \(m\ge1\), \(F_m(N)\) counts price-multiplicity vectors of total cost \(N\) for which some set \(S_i\) has multiplicity sum strictly below \(m\).

## Theorem

Let \(z\) be a primitive seventh root of unity, \(\Phi_7(z)=0\), \(P_7=\prod_{j=0}^{12}(224+7j)\), and \(A_7=(7^{14}P_7)^{-1}\). For **every** fixed positive integer \(m\), all primitive seventh roots are genuine order-13 poles, with normalized leading coefficient \(A_7T_m(z)\) at \((1-x/z)^{-13}\). Define

\[
\mathcal C(t,z)=\frac1{(1-t)^2(1-zt)(1-z^6t)},\qquad
c_j(z)=\prod_{\ell\in\{2,3,4\}\setminus\{j\}}(1-z^{\ell-j})^{-1}.
\]

Put
\[
\begin{aligned}
\mathcal F(X,Y,Z;t)
&=\sum_{a,b,u\ge0}X^aY^bZ^u\,t^{a+b+u-\max(a,b,u)}\\
&=\frac{1+(1-t)\left[
\frac X{1-X}+\frac Y{1-Y}+\frac Z{1-Z}
-\frac{tXY}{1-tXY}-\frac{tXZ}{1-tXZ}-\frac{tYZ}{1-tYZ}
+\frac{t^2XYZ}{1-t^2XYZ}\right]}
{(1-Xt)(1-Yt)(1-Zt)} .
\end{aligned}
\]

Then the **all-threshold exact rational generating function** in \(\mathbb Q[z]/(\Phi_7(z))\) is

\[
\boxed{
\mathcal T(t,z):=\sum_{m\ge1}T_m(z)t^{m-1}
=\frac{7\mathcal C(t,z)}{(1-z^5)(1-z^6)}
\sum_{j=2}^{4}c_j(z)\mathcal F(z^4,z^5,z^j;t).
}
\]

It is strictly proper in \(t\), and its denominator divides \((1-t^{14})^2\). Accordingly,

\[
\boxed{T_{m+28}-2T_{m+14}+T_m=0\ (m\ge1),\qquad T_{r+14k}=C_r+kB_r.}
\]

The threshold coefficient has **minimal quasi-polynomial period exactly 14**: at \(t=-z^5\), only the \(j=2\) term has a vanishing triple denominator \(1-t^2z^4\), with nonzero residue. All other terms are regular there. This is a primitive 14th root and cannot be canceled by any period-7 quasi-polynomial.

## Global nonvanishing: finite exact witness plus recurrence

In the unique canonical basis \(1,z,z^2,z^3,z^4,z^5\), let \(a_{m,1}\) denote the coefficient of \(z\) in \(T_m\). For \(m=r+14k\), \(1\le r\le14\), \(k\ge0\), exact cyclotomic arithmetic gives \(a_{m,1}=c_r+b_rk\):

| r | c_r | b_r |
|---:|---:|---:|
|1|3|5|
|2|8|16|
|3|9|16|
|4|15|26|
|5|7|11|
|6|-6|-8|
|7|-8|-10|
|8|4|5|
|9|15|16|
|10|16|16|
|11|26|26|
|12|11|11|
|13|-8|-8|
|14|-10|-10|

Every \(c_r\) is nonzero and \(b_r\) has the same weak sign. Hence \(T_m(z)\ne0\) for **all** positive integer thresholds, not just the twelve finite cases checked previously. Only 28 exact coefficients are needed to establish the fourteen affine rows because \((1-t^{14})^2\mathcal T\) is polynomial of degree below 28.

Thus
\[
\boxed{
F_m^{(7)}(N)=\frac{A_7N^{12}}{12!}\sum_{a=1}^6T_m(\zeta^a)\zeta^{-aN}
+O_m(N^{11})
}
\]
is nonzero for every fixed \(m\). Combining with the previously established all-threshold primitive 2/3/4/5 harmonics (minimal lcm 60), and the 31-intersection bound that each order \(d\ge8\) leaves at most 12 free prices divisible by \(d\), gives

\[
\boxed{F_m(N)=Q_{m,60}(N)+O_m(N^{12}),\quad
F_m(N)=Q_{m,420}(N)+O_m(N^{11})}.
\]

For every fixed positive \(m\), **60 and 420 are the respective least positive quasi-polynomial cost periods**. The previous 420 result was only proved at \(m=1\). These are approximation periods at the stated precision, not a claim about the exact full-period count.

## Derivation and scope

Only the seven nonempty subsets of \(\{S_0,S_1,S_2\}\) leave the same 13 free multiples of 7, namely 224,231,...,308; any inclusion-exclusion subset containing \(S_3\) or \(S_4\) has pole order at most 12. Their shared local prices are 216,217,218. Write \(a=n_{214}\), \(b=n_{215}\), \(u=n_{219}+n_{220}+n_{221}\), and \(v=n_{216}+n_{217}+n_{218}\). The three event loads are \(v+a+b\), \(v+a+u\), and \(v+b+u\). The union's minimum load is \(v+a+b+u-\max(a,b,u)\). Summing over thresholds \(m\ge1\) contributes \(t^{\min\text{load}}/(1-t)\). Equivalently the inclusion-exclusion identity \(\sum_{I\ne\varnothing}(-1)^{|I|+1}t^{\max_{i\in I}s_i}=t^{\min_i s_i}\) preserves all event overlaps.

The common group 216–218 contributes \(1/((1-z^6t)(1-t)(1-zt))\), including the threshold factor yields \(\mathcal C\). The group 219–221 contributes \(1/((1-z^2w)(1-z^3w)(1-z^4w))=\sum_{j=2}^4 c_j/(1-z^jw)\). The rest of the local prices supply \(X=z^4,Y=z^5\). Prices 222–314 outside the local union contribute the nonmultiple constant \(1/[7^{13}(1-z^5)(1-z^6)]\); the 13 free multiples contribute \(1/P_7\). Multiplication by \(7^{14}P_7\) gives the displayed normalization. The identity for \(\mathcal F\) follows by separating triples by their maximum \(h\) and telescoping consecutive boxes \([0,h]^3\setminus[0,h-1]^3\). These geometric sums are rational identities evaluated at primitive seventh roots, not an unsupported convergence assumption.

Pole analysis: at \(t=1\), \(\mathcal C\) has order two and the factor \(1-t\) in \(\mathcal F\) cancels any extra pole. At other seventh roots, the base factors and each single pair/triple fraction in \(\mathcal F\) produce at most two coincident simple factors. At negative seventh roots, only one quadratic denominator can vanish, giving at most a simple pole. All poles are 14th roots and order at most two. Also \(\mathcal C=O(t^{-4})\) and \(\mathcal F=O(t^{-2})\) at infinity, proving strict properness and the claimed recurrence. The primitive-14 pole \(t=-z^5\) has a unique uncanceled \(j=2\) contribution.

## Reproduction and boundaries

Run `python VERIFY_GENERATOR.py` and `python VERIFY_DP.py 12` (standard-library Python). Generator: 84 exact coefficients, 56 second-difference regression checks, 14 sign certificates, predecessor m=1,2 Fourier trace checks, and `RESULT.json`. Independent enumerator: all seven intersection-local bounded multiplicity DPs for each m=1–12, compared with the rational generator; it does **not** reuse its coefficient-generation algorithm. Both pass locally. The infinite theorem rests on the rational identity, denominator and 28 exact initial coefficients, not on numerical extrapolation. No independent scientific review, formal Foundation admission, or native X6/BRC phase transport is asserted. The latter would require a separate observer-preservation mapping under P000.

Next: classify degree-11 terms from order-12 roots at all thresholds, and ask at what precision the minimal cost modulus first requires a new factor outside 420. Preserve frozen R5 pins, independent source contributions and review status.
