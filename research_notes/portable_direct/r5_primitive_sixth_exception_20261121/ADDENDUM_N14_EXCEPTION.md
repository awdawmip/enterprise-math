# R5 addendum: first exceptional thresholds have a nonzero sixth-root degree-14 term

2026-11-21. AUTHOR_EXACT_FINITE_LEMMA / EXACT_RATIONAL_DP / NOT_REVIEWED.

This is a direct continuation of RESEARCH.md in this same directory, under its frozen 256-hypothesis, 101-price R5 input.

The all-threshold sixth-root leading coefficient S_m(q) vanishes exactly for m congruent to 5 modulo 6. The following further exact finite result shows that the exception at the first four such thresholds retains a **nonzero next-order sixth-root harmonic**.

Take q primitive sixth, q^2-q+1=0, and A6 = 1/(6^32 P6) as defined in RESEARCH.md. At each m in {5,11,17,23}, the primitive sixth roots give

$$
F_m^{(6)}(N)=\frac{A_6N^{14}}{14!}
\left(q^{-N}V_m(q)+q^N\overline{V_m(q)}\right)+O_m(N^{13}),
$$

where, in the exact basis (1,q):

| m | V_m(q) |
|---:|---|
| 5 | 1336+1726q |
| 11 | 7490+1688q |
| 17 | 16722+3366q |
| 23 | 30772+3280q |

For m=5 the associated six-residue trace vector is (4398,4788,390,-4398,-4788,-390), indexed N mod6=0,...,5. This proves the exceptional m=5 harmonic exists at degree 14. The same nonvanishing conclusion follows immediately from the tabulated coefficients for m=11,17,23.

## Exact derivation and independent computation

For each nonempty I subset {0,1,2}, put U_I=union of its separating sets, E_I=P\U_I, and H_{I,m}(x) equal to the finite exact local polynomial summing x^weighted_cost over locally admissible multiplicities. Let the baseline E_0=P\S0.

Set

$$
R_I(q)=\frac{\prod_{p\in E_0\setminus E_I}(1-q^p)}
{\prod_{p\in E_I\setminus E_0}(1-q^p)}.
$$

Define the first Laurent correction from its free prices as

$$
B_I(q)=\frac12\sum_{\substack{p\in E_I\\6\mid p}}(p-1)
-\sum_{\substack{p\in E_I\\6\nmid p}}\frac{p q^p}{1-q^p}.
$$

This follows by expanding at x=q(1-s): for a free p divisible by 6,
(1-x^p)^(-1)=(ps)^(-1)(1+(p-1)s/2+O(s²));
for the remaining p it equals
(1-q^p)^(-1)(1-pq^p s/(1-q^p)+O(s²)).

Writing sign(I)=(-1)^(|I|+1), the first two principal coefficients after dividing out common A6 are

$$
L_{16}(m)=\sum_{I}sign(I)R_I(q)H_{I,m}(q),
$$

$$
L_{15}(m)=\sum_{I}sign(I)R_I(q)
\bigl(B_I(q)H_{I,m}(q)-qH_{I,m}'(q)\bigr).
$$

The original proof establishes L16(m)=S_m(q); at these exceptional m it is zero. Therefore V_m(q)=L15(m). The exact checker independently accumulates both H(q) and its weighted-cost moment qH'(q) across each of the seven events in Q[q]/(q²-q+1), computes each R_I and B_I with rational arithmetic, and verifies L16=0 and the four tabulated nonzero values. No floating point and no use of previous closed-form numerator in this second-order calculation.

The values for other m=1,...,8 are also included as a regression record; they are the pole-order-15 coefficients and not by themselves the full degree-14 coefficients, since the degree-16 pole contributes an extra 8 L16 in degree 14. The included machine-readable result gives the corrected full degree-14 coefficient L15+8 L16 for each checked m.

**Remaining open problem:** classify the Laurent degree-14 coefficient for every m=6k+5, rather than the first four examples. A symbolic rational-generating-function attempt involving derivatives of seven overlap functions was interrupted before a valid identity was obtained; no unproved all-m formula is asserted. Next determine the primitive seventh-root leading nonzero class and the precision threshold at which the minimal cost residue modulus grows from 60.
