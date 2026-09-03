# Gregory–Machin continuation: primitive rational-turn completion, Todd compression threshold, and a 1.27055 five-generator circuit

Status: `FREE_RESEARCH / EXACT_GENERAL_RATIONAL_TURN EXTENSION + COMPLETION_COST THEOREM + PRIOR_ART VERIFICATION / NOT_FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-B2817C / FREE_AXIOM_DISCOVERY`
Issue: `#1160`
Checker: `research_notes/experiments/gregory_machin_general_rational_circuit_check_20260903.py`

## 1. Native extension is already inside the original carrier

The #1160 native rational-turn group was defined from the start as

\[
\mathcal T_{\mathbf Q}=\mathbf Q(i)^\times/\mathbf Q_{>0}^\times.
\]

Thus restricting attention to reciprocal integer generators

\[
U_D=[D+i]
\]

was a search specialization, not an ontology restriction.

For coprime integers

\[
b>|a|>0,
\]

define the primitive rational-slope generator

\[
\boxed{G_{b,a}=[b+ai].}
\]

Everything in the native layer remains integer arithmetic:

- composition is Gaussian pair multiplication;
- positive scale is quotiented;
- split-prime oriented valuations are integers;
- the `C8` torsion coordinate is unchanged;
- winding is a finite direction-sheet lift.

Hence the exact valuation-lattice decomposition and circuit endpoint theorem apply verbatim to general primitive direction pairs.

Freeze:

`GENERAL_RATIONAL_SLOPE != NEW_NATIVE_PRIMITIVE`.

It is the already-declared integer direction-pair carrier used at full strength.

## 2. Analytic completion for a primitive pair

Only after the native state is fixed, define on the principal small-turn branch

\[
\Theta(G_{b,a})=\operatorname{sgn}(a)\arctan\frac{|a|}{b}.
\]

Put

\[
\rho=\frac b{|a|}>1.
\]

The finite truncation is

\[
A_N(\rho)
=\sum_{n=0}^{N}\frac{(-1)^n}{(2n+1)\rho^{2n+1}}.
\]

Exactly as in the reciprocal-integer case, the completion residual is

\[
R_N(\rho)
=(-1)^{N+1}
\int_0^{1/\rho}\frac{t^{2N+2}}{1+t^2}\,dt,
\]

so

\[
\boxed{
\frac{\rho^2}{\rho^2+1}\frac1{(2N+3)\rho^{2N+3}}
\le |R_N(\rho)|
\le
\frac1{(2N+3)\rho^{2N+3}}.
}
\]

Thus the earlier fixed-total-work theorem extends with no change other than replacing integer `D_j` by rational ratios `rho_j=b_j/|a_j|`.

The generalized Lehmer measure is

\[
\boxed{
\mu=\sum_j\frac1{\log_{10}\rho_j}
}
\]

and the optimal large-budget completion exponent remains

\[
\boxed{
\Gamma=\frac{2\ln10}{\mu}.
}
\]

## 3. Todd expansion is compression/decompression between reciprocal and rational generators

For integer `x>=2`, set

\[
F(x)=\frac{x(x^2+3)}2.
\]

Whenever `F(x)` is integral, direct Gaussian multiplication gives

\[
\boxed{
G_{x,2}=U_x^2U_{F(x)}^{-1}.
}
\]

Indeed

\[
(x+i)^2(F-i)
\]

has direction `(x,2)` precisely when

\[
2F=x(x^2+3).
\]

At analytic completion this is the familiar Todd relation

\[
\arctan\frac2x
=2\arctan\frac1x
-\arctan\frac1{F(x)}.
\]

The native interpretation is stronger for the current program:

\[
\boxed{
\text{two reciprocal completion generators}
\leftrightarrow
\text{one primitive integer direction pair}.
}
\]

No real angle is needed to perform the compression.

## 4. Exact generalized-Lehmer threshold for Todd compression

Compare the uncompressed support cost

\[
C_{\rm raw}(x)
=\frac1{\log x}+\frac1{\log F(x)}
\]

with the compressed rational-generator cost

\[
C_{\rm comp}(x)
=\frac1{\log(x/2)}.
\]

(Base of logarithm is irrelevant to the inequality.)

The compression is beneficial iff

\[
\frac1{\log(x/2)}
<
\frac1{\log x}+\frac1{\log F(x)}.
\]

Elementary rearrangement gives the equivalent condition

\[
\boxed{
h(x):=(\log(x/2))^2-(\log2)\log(x^2+3)>0.
}
\]

Furthermore

\[
h'(x)
=\frac{2\log(x/2)}x
-\frac{2x\log2}{x^2+3}.
\]

For `x>4`,

\[
(x^2+3)\log(x/2)-x^2\log2
=x^2\log(x/4)+3\log(x/2)>0,
\]

so

\[
\boxed{h'(x)>0\qquad(x>4).}
\]

Direct evaluation gives

\[
h(13)<0<h(14).
\]

Therefore:

### Theorem 4.1 — exact integer threshold

\[
\boxed{
C_{\rm comp}(x)<C_{\rm raw}(x)
\iff x\ge14
}
\]

for integer `x>2` for which the displayed Todd tail is integral.

For a genuinely primitive half-integer argument `(x,2)` one takes odd `x`, so the first strict generalized compression improvement occurs at

\[
\boxed{x=15.}
\]

This turns a classical transformation into an explicit resource theorem: beyond the threshold, retaining the primitive rational direction is asymptotically better under the same fixed-series-work model than expanding it into two integer reciprocal generators.

## 5. Exact five-generator circuit with generalized Lehmer measure 1.27055

A 2010 paper by Amrik Singh Nimbran records the identity, in compressed notation,

\[
\boxed{
\begin{aligned}
\tau={}&
G_{107,1}^{83}
G_{1710,1}^{17}
G_{207385,2}^{-22}
G_{2513489,2}^{-12}
G_{3235259223,1}^{22}.
\end{aligned}
}
\]

The project independently verifies it entirely at the native integer-pair layer.

For free split primes ordered as

\[
(5,113,229,8861,42953),
\]

the valuation matrix is

\[
V=
\begin{pmatrix}
2&0&0&12&-1\\
0&-2&-1&-1&0\\
-1&-1&0&-1&4\\
0&0&1&0&1\\
0&0&1&0&1
\end{pmatrix}.
\]

It has rank four, and

\[
\boxed{
c=(83,17,-22,-12,22)}
\]

satisfies

\[
\boxed{Vc=0.}
\]

The `C8` coordinates of the five generators are

\[
(7,2,0,2,7),
\]

and

\[
\boxed{(7,2,0,2,7)\cdot c\equiv1\pmod8.}
\]

Thus this is an exact generalized valuation circuit for the diagonal target.

Direct primitive pair multiplication gives

\[
\boxed{\text{endpoint}=(1,1)}
\]

and the finite tangent-sheet lift gives

\[
\boxed{\text{sheet}=0,\qquad\text{crossings}=0.}
\]

Hence analytic completion is unambiguously the principal `pi/4` branch.

## 6. Completion efficiency

The five ratios are

\[
107,\quad1710,\quad\frac{207385}{2},\quad\frac{2513489}{2},\quad3235259223.
\]

Therefore

\[
\boxed{
\mu_{\rm gen}=1.2705512545505269\ldots
}
\]

and the fixed-total-work exponent is

\[
\boxed{
\Gamma_{\rm gen}
=\frac{2\ln10}{\mu_{\rm gen}}
=3.624544991392124\ldots
}
\]

For comparison, the previously certified all-integer six-term `1.489121...` formula has exponent about `3.09254`, while Hwang 1997 at `1.512439...` has exponent about `3.04486`.

Thus preserving the two rational direction pairs materially improves the asymptotic completion rate under the same resource model.

## 7. Pure integer-reciprocal expansion is still better than the commonly quoted Hwang benchmark

Using

\[
G_{x,2}=U_x^2U_{F(x)}^{-1}
\]

for `x=207385` and `x=2513489`, the same endpoint expands to seven reciprocal-integer generators:

\[
\boxed{
\begin{aligned}
\tau={}&
U_{107}^{83}
U_{1710}^{17}
U_{207385}^{-44}
U_{4459662850206890}^{22}\\
&\cdot
U_{2513489}^{-24}
U_{7939642926390344818}^{12}
U_{3235259223}^{22}.
\end{aligned}
}
\]

The checker verifies again

\[
\boxed{\text{endpoint}=(1,1),\quad\text{sheet}=0.}
\]

Its ordinary integer-reciprocal Lehmer measure is

\[
\boxed{
\mu_{\rm int}=1.3683628258403102\ldots
}
\]

which is also below both `1.489121...` and the widely reproduced Hwang `1.51244` benchmark.

This does **not** constitute a historical novelty claim.  Nimbran's paper explicitly gives the uncompressed measure `1.36836` and notes an effective `1.27055` measure after treating the two half-integer arguments as primitive terms.

The project-level contribution is the exact typing:

- the half-integer terms are not bookkeeping shortcuts;
- they are primitive integer direction-pair generators already native to `T_Q`;
- their endpoint and winding are exactly certifiable by the same valuation circuit calculus;
- their lower resource cost follows from the generalized completion theorem.

## 8. Consequence for the #1160 research program

The search space should no longer be treated as

\[
\{U_D=[D+i]\}.
\]

The mathematically natural finite carrier is

\[
\boxed{
\{G_{b,a}=[b+ai]:\gcd(a,b)=1,\ b>|a|>0\}.
}
\]

The reciprocal-integer formulas are only the `a=1` slice.

This produces a sharper separation of layers:

\[
\text{primitive integer direction pair}
\to
\text{Gaussian valuation circuit}
\to
\text{finite winding}
\to
\text{ratio }\rho=b/|a|
\to
\text{analytic completion / resource cost}.
\]

The next frontier is a bounded **rational-slope Pareto census** whose search coordinates are `(b,a)` and Gaussian prime supports, not a precompiled list of inverse-cotangent identities.
