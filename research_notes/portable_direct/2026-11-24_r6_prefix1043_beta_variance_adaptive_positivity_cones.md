# PREFIX-1043 — Exact Beta-variance positivity cones and pointwise finite-order certificates

Date: 2026-11-24 (Asia/Shanghai). Parent: PREFIX-1042. Status: AUTHOR_CONDITIONAL_ANALYTIC_PROOF / EXACT_RATIONAL_IMPLICATION_CHECKED / NOT_INDEPENDENTLY_REVIEWED.

## Provenance and frozen scope

Frozen scientific root: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json` (P000 V5). The original signed X6 Cell–terminal-port–grade observer retains branch, sign, multiplicity, provenance and residual information. Stage46's signed BRC candidate uses W=J12−6I12, incoming −e1, blocked bidirectional Link {0,e1}, and one outgoing negative step. This paper proves a theorem only about the inherited **auxiliary six-phase scalar signed spectral model**. The map back to native BRC remains NATIVE_ATTRIBUTION_PENDING_BRC_REVALIDATION; no BRC operation or classical physical comparison is performed here.

Precisely used inherited author-level inputs:
* PREFIX-1033 (`enterprise-math@fec5c00006e3693121ee18f6d0be661506e06410`): continuous real signed density g on [0,36] and exact normalized Hausdorff/Beta identity.
* PREFIX-1037 (`@928461a6f8c675b9a7bd38586cf47db9d25835e9`): g(4)>6371/60 and g(16)>919/90, conditional on its scalar representation and numerical certificate.
* PREFIX-1040 (`@58e35fe4a131729405107d736198cf555d53cc8a`): |g(y)-g(4)|<104400 sqrt(|y−4|) for |y−4|<=1/10000, and |g(y)-g(16)|<291700 sqrt(|y−16|) for |y−16|<=1/10000.
* PREFIX-1041 (`@7bcaa3dc08c01119b661f0f9ecc31ca7fa7ba806`): |g(y)|<=U=611856 on [0,36].
* PREFIX-1042 (`@cd31f2c70132c5f976e6540d8ebb85e6e3171d55`): earlier cones at n>=5×10^14 and 5×10^20 using the universal variance 1/(4(n+2)).

The new calculation improves the variance constant at each fixed center and uses a sharper admissible positivity margin. These inputs and their independent-review states are unchanged.

## Exact adaptive criterion

Let m,k be nonnegative integers, n=m+k+1, j=m+1 (so 1<=j<=n), s=j/n, and let T have Beta(j,n-j+1) distribution. Use exactly the inherited normalization
[
D_{m,k}=rac{(m+k+1){m+k\choose m}}{36^{m+k+1}}E_{m,k}=mathbb E[g(36T)].
]
The factor relating D to E is strictly positive.

For c in {4,16}, choose (a_c,L_c,H_c,C_c) as follows:

| c | a_c, in spectral y units | L_c | H_c, strict lower bound on g(c) | C_c |
|---|---|---:|---:|---:|
| 4 | 1/2000000 | 104400 | 6371/60 | 106 |
| 16 | 1/2000000000 | 291700 | 919/90 | 10 |

Put epsilon=1/10000 and
[
Q_{n,j;c}=
rac{1296j(n-j+1)}{(n+1)^2(n+2)}
+left(rac{36j}{n+1}-cight)^2.
]

**Proposition A (pointwise exact integer criterion).** If
[
nge8cdot10^{12},qquad |36j/n-c|le a_c,
qquad L_c^4Q_{n,j;c}<C_c^4,
]
then
[
D_{m,k}>H_c-C_c-rac1{100}.
]
In particular the right side is 13/75 for c=4, and 181/900 for c=16. Thus E_{m,k}>0.

This criterion is a finite exact-rational decision on (n,j) for either center, stronger than a uniform worst-case row bound. It does not require evaluating the enormous Hausdorff moments themselves.

## Uniform improved cones

Set p_c=c/36, b_c=a_c/36, and
[
Q_c^{\mathrm{unif}}(n)=
rac{1296}{n+2}left[p_c(1-p_c)+b_c+rac{p_c+b_c}{n}ight]
+left(a_c+rac{36}{n}ight)^2 .
]

**Theorem B.** For all integers m,k>=0 with n=m+k+1 and s=(m+1)/n:
[
oxed{nge160000000000000,quad |s-1/9|le 1/72000000
quad\Longrightarrowquad D_{m,k}>13/75, E_{m,k}>0.}
]
[
oxed{nge300000000000000000000,quad |s-4/9|le 1/72000000000
quad\Longrightarrowquad D_{m,k}>181/900, E_{m,k}>0.}
]

Both ratio bands retain exactly the PREFIX-1042 widths. Their order thresholds decrease by 25/8=3.125 and 5/3, respectively, compared with PREFIX-1042. Each eligible row contains an integer pair in its stated band.

Two stronger exact-center **pointwise** witnesses from Proposition A are:
* c=4: n=126000000000000, j=14000000000000, hence (m,k)=(13999999999999,112000000000000), and D>13/75.
* c=16: n=243000000000000000000, j=108000000000000000000, hence (m,k)=(107999999999999999999,135000000000000000000), and D>181/900.

These are conditional analytic certificates verified through rational inequalities, not direct numerical evaluations of E at those large indices.

## Proof of both statements

1. The Beta order-statistic representation gives mean mu=j/(n+1) and exact variance
[
\operatorname{Var}(T)=rac{j(n-j+1)}{(n+1)^2(n+2)}.
]
Thus Q_{n,j;c}=E[(36T-c)^2] exactly, and concavity/Hölder gives E sqrt(|36T-c|)<=Q_{n,j;c}^{1/4}.

2. Put A={|36T-c|<=epsilon} and q=Pr(A^c). If |36s-c|<=a_c<=epsilon/2, then A^c implies |T-s|>epsilon/72. The order-statistic/binomial identity followed by Hoeffding yields
[
qle2\exp(-n\epsilon^2/2592).
]
At every n>=8×10^12 the exponent exceeds 30; since e>2,
q<2^{-29}. By the inherited global bound, 2Uq<U/2^{28}<1/100.

3. On A the inherited local square-root modulus bounds g(36T)>g(c)-L_c sqrt(|36T-c|). On A^c one has g(36T)>=-U and g(c)<=U. Splitting the expectation gives
[
D_{m,k}ge g(c)-L_c E\sqrt{|36T-c|}-2Uq
>H_c-L_cQ_{n,j;c}^{1/4}-1/100.
]
The exact integer condition L_c^4Q_{n,j;c}<C_c^4 proves Proposition A.

4. For |s-p_c|<=b_c, one has s(1-s)<=p_c(1-p_c)+b_c (because x(1-x) is 1-Lipschitz on [0,1]) and s<=p_c+b_c. Directly from j=ns,
[
\operatorname{Var}(T)=rac{n^2s(1-s)+ns}{(n+1)^2(n+2)}
lerac{p_c(1-p_c)+b_c+(p_c+b_c)/n}{n+2}.
]
Also |36mu-c|<=a_c+36/n. Therefore Q_{n,j;c}<=Q_c^{unif}(n). The latter decreases in n>0.

5. Companion Python Fraction checks establish, at the stated minimum n values,
[
104400^4 Q_4^{unif}(160000000000000)<106^4,
]
[
291700^4 Q_{16}^{unif}(300000000000000000000)<10^4,
]
and exact tail, lower-margin and pointwise-sample inequalities. Theorem B follows by Step 3. For every admissible n the nearest integer j to np_c obeys |s-p_c|<=1/(2n), so |36s-c|<=18/n<=a_c; it lies between 1 and n. QED within the stated inherited scalar assumptions.

## Validation, limits and continuation

Reproducibility: `PREFIX1043_R6_BETA_VARIANCE_EXACT_CHECK.py` uses integer and `fractions.Fraction` arithmetic only and checks all displayed finite inequalities, the 2Uq cap, both nonempty cones, comparison ratios and both pointwise j values. This verifies the **new rational implications**. The analytic Beta/order-statistic and Jensen steps are written above, not delegated to the checker. No floating-point evaluation, native BRC run, new spectral integration or formal proof checker has been performed.

Next: use the exact adaptive criterion with improved local spectral estimates or a rigorous point/interval certificate away from c=4,16; target whole-interval sign certification or an exact negative witness. The full scalar g>=0 on [0,36], native X6–signed BRC observer correspondence, and mother question B_fix,odd(32) in {19,20} remain open. Keep historical contributors and NOT_REVIEWED; a GitHub science commit is not a formal CLAIM, PROGRESS, Result, Review or native mathematics acceptance.
