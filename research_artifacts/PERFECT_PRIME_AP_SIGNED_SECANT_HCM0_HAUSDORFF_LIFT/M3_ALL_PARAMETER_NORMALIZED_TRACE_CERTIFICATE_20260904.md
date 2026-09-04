# Perfect Prime AP HCM0 — m=3 all-parameter normalized trace certificate

Task: `RS-PERFECT-PRIME-AP-SIGNED-SECANT-HCM0-HAUSDORFF-LIFT`  
Publication: `TP2-7A2D91C5E40B836F19D2`  
Researcher: `EM-HCM0-HL-FB0860`  
Recovery claim: `CLM-HCM0HL-RECOVER-20260904T205700`  
Date: 2026-09-04  
Status: **EXACT ALL-PARAMETER m=3 THEOREM — ALL-m M6 / HCM0 REMAIN OPEN**

## 1. Statement

Set `m=3`, hence `n=2`.  Let the initial actual layer be `S=s0>=0`, and let the two consecutive positive block lengths be

\[
a\ge1,\qquad c\ge1.
\]

Put

\[
M=3a,\qquad N=3(a+c),\qquad r_0=3S.
\]

For the synchronized quotient forms define

\[
\mathcal H_a:=M^{-2}Q_{r_0,r_0+M},
\qquad
\mathcal H_{a+c}:=N^{-2}Q_{r_0,r_0+N}.
\]

Then the following strict inequality holds for every real `S>=0`, `a>0`, `c>0` (and therefore for every actual integer triple):

\[
\boxed{
\operatorname{tr}(\mathcal H_{a+c}^{-1}\mathcal H_a)>2.
}
\tag{1.1}
\]

Equivalently, in unnormalized form,

\[
\boxed{
\operatorname{tr}(Q_{r_0,r_0+N}^{-1}Q_{r_0,r_0+M})
>2\left(\frac{M}{N}\right)^2.
}
\tag{1.2}
\]

In particular the relevant extreme mixed determinant coefficient has the required strict sign for every `m=3` actual three-layer base slice.

## 2. Exact rational reduction

Use the exact frozen entry formula

\[
Q_{r_0,r}[u,v]
=\sum_{j=0}^{2}(-1)^j\binom2j\mu_{r+j}
 g_{M,u}(j)g_{M,v}(j),
\]

where

\[
\mu_k=\frac{2}{(3k+1)(3k+2)(3k+3)},
\qquad
g_{M,u}(j)=\binom{j+M}{u}-\binom ju,
\]

for `u,v in {1,2}`.

For a symmetric `2x2` pair `A,B`,

\[
\operatorname{tr}(B^{-1}A)
=\frac{B_{22}A_{11}+B_{11}A_{22}-2B_{12}A_{12}}
{\det B}.
\]

Substitution and exact rational simplification give

\[
\boxed{
\operatorname{tr}(\mathcal H_{a+c}^{-1}\mathcal H_a)-2
=\frac{c\,P(a,c,S)}{D(a,c,S)}.
}
\tag{2.1}
\]

The denominator factors completely as

\[
\begin{aligned}
D={}&3(a+S+1)(3a+3S+1)(3a+3S+2)\\
&\cdot(9a+9S+1)(9a+9S+2)(9a+9S+4)(9a+9S+5)\\
&\cdot(9a+9S+7)(9a+9S+8)(9a+9c+9S+5),
\end{aligned}
\tag{2.2}
\]

which is strictly positive for `S>=0`, `a,c>0`.

## 3. Exact positive polynomial certificate

After extracting the displayed factor `c`, the numerator polynomial `P(a,c,S)` has:

- total degree `9`;
- exactly `200` nonzero monomials;
- every coefficient a strictly positive integer;
- minimum coefficient `1,590,000`.

Ordering monomials lexicographically by exponent triple `(deg_a,deg_c,deg_S)` and serializing each row as

`deg_a,deg_c,deg_S|coefficient`

gives the canonical SHA-256 digest

`73b4667301eedfbfb6fa7097fa2cc16abc7aaee24ab31b915ff140bb5affc175`.

Therefore

\[
P(a,c,S)>0
\]

throughout the stated positive parameter region, and (1.1) follows.

## 4. Interpretation

At coalescence `c=0`, the two normalized forms are identical and the relative trace is exactly the dimension `n=2`.  Equation (2.1) proves that every positive second block produces a strict increase, globally in the first block and the initial layer.

This is stronger than merely proving positivity of the mixed coefficient: it verifies the all-m candidate lower-bound shape

\[
\operatorname{tr}(\mathcal H_{a+c}^{-1}\mathcal H_a)>n
\]

in the first nontrivial matrix dimension.

The proof is exact symbolic algebra, not bounded evaluation.  It does **not** establish the corresponding statement for arbitrary `m`.

## 5. Boundary

Proved here:

- full `m=3` M6 trace inequality for every initial layer and every two positive actual block lengths;
- explicit positive denominator and a positive-coefficient numerator certificate.

Still open:

- `M6_ACTUAL_TWO_BLOCK_NEWTON_TRACE_POSITIVITY` for every `m`;
- the remaining coefficients of the all-m three-support pencil;
- all-support layer sign regularity;
- HCM0 and parent determinant nonvanishing.
