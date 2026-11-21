# R5 | Primitive sixth roots: exact all-threshold leading coefficient, vanishing class and period-60 extension

2026-11-21. Scientific status: AUTHOR_EXACT_RATIONAL_PROOF / EXACT_FINITE_CHECKED / NOT_REVIEWED. Independent portable research; no assertion of a current Task CLAIM/RUN, native PROGRESS, Result or Review.

## Frozen scientific problem

The model is R5's 256 labelled hypotheses, query prices P={214,...,314}, and the original frozen data EXACT_R5_ALL_101_BUDGETS.json, inherited SHA256 50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b. The historical 32,640-pair separation certificate is inherited without rerunning or changing the pinned input.

The five minimal separating sets are:
- S0={214,215,216,217,218}
- S1={214,216,217,218,219,220,221}
- S2={215,216,217,218,219,220,221}
- S3={223,...,290}
- S4={296,...,312}.

For integer m>=1, F_m(N) counts nonnegative query multiplicity vectors of weighted cost N for which at least one S_j has total multiplicity strictly less than m. Its rational generating function is the inclusion-exclusion sum of the finite local polynomials H_{I,m}(x) times products over free prices P\U_I of (1-x^p)^(-1), for nonempty I subset {0,...,4}, U_I=union S_j.

Previous exact fifth-root and minimum-modulus-60 frontier:
https://github.com/awdawmip/enterprise-math/blob/7723ab9d7a0bd2e5a9b541e85e5188456f36b328/research_notes/portable_direct/r5_primitive_fifth_carrier60_20261121/RESEARCH.md

This is a purely scalar rational-function calculation. No assertion of a native X6 physics interpretation or BRC/Shor realization is made.

## Theorem 1: exact leading primitive-sixth-root contribution for all m

Let q be a primitive sixth root, q^2-q+1=0, q=exp(pi i/3). Define
- P6 = product(222,228,...,312), 16 factors;
- A6 = 1/(6^32 P6);
- R(z) = sum_{j=1}^{19} r_j z^j.

All nonzero r_j are listed; every omitted r_j is 0.

| j | r_j in Q(q) |
|---:|:---|
| 1 | 7-4q |
| 2 | -2+8q |
| 3 | -2+4q |
| 4 | -4 |
| 6 | -2-4q |
| 7 | 15-8q |
| 8 | 8q |
| 9 | -4+8q |
| 10 | -4q |
| 12 | -4q |
| 13 | 9-4q |
| 14 | 2 |
| 15 | -2+4q |
| 16 | 4-4q |
| 18 | 2 |
| 19 | 1 |

For every positive integer threshold m define the exact Gaussian algebraic coefficient S_m(q) by

$$
\sum_{m\ge1}S_m(q)z^m=\frac{R(z)}{(1-z^{12})^2}.
$$

Then for fixed m and N tending to infinity, the sum of contributions from the two primitive sixth roots q and conjugate(q) to F_m(N) is

$$
F_m^{(6)}(N)=\frac{A_6N^{15}}{15!}\left(q^{-N}S_m(q)+q^{N}\overline{S_m(q)}\right)+O_m(N^{14}).
$$

This statement concerns only the two primitive sixth-root partial-fraction terms.

Explicitly, for m=12k+r with integer k>=0 and 1<=r<=12,

$$
S_{12k+r}(q)=r_r+k(r_r+r_{r+12}),\quad r_j=0\ \text{if absent}.
$$

**Sharp exception:** S_m(q)=0 if and only if m is congruent to 5 modulo 6. Thus the sixth-root pole is exactly order 16 and yields a nonzero degree-15 cost harmonic whenever m is not congruent to 5 modulo 6. In the exceptional class the degree-15 coefficient vanishes; the degree-14 coefficient is a separate open question.

Exact normalized residue vectors, indexed N mod 6 from 0 through 5:
- m=1: S_1=7-4q; pair trace = (10,-1,-11,-10,1,11).
- m=2: S_2=-2+8q; pair trace = (4,14,10,-4,-14,-10).
- m=5: S_5=0; degree-15 trace zero.

## Proof

### Pole accounting, including all seven intersecting bad events

For every nonempty I, the order at q of the inclusion-exclusion term is bounded by the number of multiples of 6 among P\U_I. Exhaustive enumeration of 31 subsets proves that exactly the seven nonempty I subset {0,1,2} retain all 16 multiples, while every I meeting {3,4} retains at most 14. Therefore **all seven** contributions, including pair and triple intersections, are required for the 16th-order principal part. Using only single events would be incorrect.

For S0 the free prices are 219..314, 16 complete residue cycles modulo 6. Its 16 multiples each have a linear pole; their Laurent leading factor is 1/(6^16 P6), while the 80 nonmultiples have product constant 6^(-16). Hence the common leading normalization is A6.

### One exact eight-price joint local problem

Set E*={222,...,314}, with the other eight prices T={214,...,221}. Put a=n_214, b=n_215, c=n_216+n_217+n_218, d=n_219+n_220+n_221. The three bad constraints are a+b+c<m, a+c+d<m, b+c+d<m. Let alpha=q^4 and beta=q^5, and define

$$
C(z)=\frac1{(1-z)(1-qz)(1-q^2z)},\qquad
D(t)=\frac1{(1-q^3t)(1-q^4t)(1-q^5t)}.
$$

For nonempty I subset {0,1,2}, let M_I(a,b,d) be the maximum of the selected pair sums (a+b), (a+d), (b+d). The exact threshold generating function of its local q-weighted count is

$$
G_I(z)=\frac{zC(z)}{1-z}B_I(z),\qquad
B_I(z)=\sum_{a,b,d\ge0}\alpha^a\beta^b[t^d]D(t)\,z^{M_I(a,b,d)}.
$$

This follows from summing z^m over m>c+M_I. Every term is kept as a joint-relation observer, preserving the triple overlap.

### Explicit rational expressions for all seven B_I

For any scalar u write D_u(z)=D(uz). Put

$$
W_b(z)=\frac{D_b(z)}{1-bz}+\frac{D_1(z)-D_b(z)}{1-b},
$$

$$
M_{a,b}(z)=\frac1{(1-az)(1-abz)}
+\frac{(1-bz)^{-1}-(1-abz)^{-1}}{1-a},
$$

$$
T_{a,b,c}(z)=\frac{1-abc\,z^3}{(1-abc\,z^2)(1-az)(1-bz)(1-cz)}.
$$

Then:

$$
\begin{aligned}
B_0&=\frac{D(1)}{(1-\alpha z)(1-\beta z)},\\
B_1&=\frac{D_1(z)}{(1-\alpha z)(1-\beta)},\\
B_2&=\frac{D_1(z)}{(1-\beta z)(1-\alpha)},\\
B_{01}&=\frac{W_\beta(z)}{1-\alpha z},\\
B_{02}&=\frac{W_\alpha(z)}{1-\beta z},\\
B_{12}&=D_1(z)M_{\alpha,\beta}(z),\\
B_{012}&=\frac{\sqrt{-3}}3 T_{\alpha,\beta,q^3}(z)
+T_{\alpha,\beta,q^4}(z)
-\frac{\sqrt{-3}}3 T_{\alpha,\beta,q^5}(z).
\end{aligned}
$$

The last identity uses the exact partial fractions

$$
[t^d]D(t)=\frac{\sqrt{-3}}3 q^{3d}+q^{4d}-\frac{\sqrt{-3}}3q^{5d}.
$$

The W and M formulas follow by partitioning pairs of nonnegative integers at their maxima. The T formula follows by partitioning the three coordinates by their minimum. These are algebraic decompositions, not asymptotic approximations.

Relative to E*, the free-price normalization is multiplied by

$$
\prod_{p=219}^{221}(1-q^p)=4q-2=2\sqrt{-3}.
$$

Thus the normalized sixth-root coefficient threshold generating function is exactly

$$
S(z)=(4q-2)\frac{zC(z)}{1-z}
(B_0+B_1+B_2-B_{01}-B_{02}-B_{12}+B_{012}).
$$

Performing rational-function operations in the quadratic field Q[q]/(q^2-q+1) yields the exact polynomial identity

$$
(1-z^{12})^2S(z)=R(z),
$$

with every coefficient r_j tabulated above. The accompanying exact verifier independently asserts this polynomial identity; it does not use floating-point arithmetic.

Finally, (1-z^12)^(-2)=sum_{k>=0}(k+1)z^(12k). Reading each residue class gives the all-m formula. For k>=0 and r=1,...,12, direct comparison of the two rational coordinates of r_r+k(r_r+r_{r+12}) proves zero only for r=5 or 11 (equivalently m=5 mod6). A pole of order 16 produces binomial(N+15,15)=N^15/15!+O(N^14). This proves the theorem.

## Theorem 2: exact minimum cost period stays 60 through O_m(N^14)

For every fixed integer m>=1 there exists a quasi-polynomial Q_{m,60}(N), whose coefficient functions depend only on N mod60, with

$$
F_m(N)=Q_{m,60}(N)+O_m(N^{14}).
$$

Moreover 60 is the *strictly minimal positive integer modulus* for this asymptotic accuracy. Indeed, among the 31 nonempty inclusion-exclusion subsets and all d>=7, the maximum number of free prices divisible by d is 13. All primitive d>=7 roots therefore contribute O_m(N^12), below the retained degree>=15 range. The only roots that can affect this accuracy have d in {1,2,3,4,5,6}; all their frequencies are represented by N mod60. Prior exact all-m proofs show nonzero primitive 2,3,4,5 root contributions, so any admissible modulus must be divisible by lcm(2,3,4,5)=60. Primitive sixth roots introduce no new modulus factor, even when their degree-15 coefficient is nonzero.

This is precision-scoped; the exact (untruncated) cost period may be larger.

## Verification, provenance, next open problem

The accompanying code evaluates the quadratic-field rational identity exactly; independently computes all seven local overlap counts with Gaussian-integer-pair DP for m=1,...,24; and checks all 31 intersection pole counts plus d>=7 divisor counts. The finite checks corroborate a separately stated symbolic proof for all m. Frozen input and preexisting pair separation certificates are inherited and not rerun. Independent research review remains NOT_REVIEWED; formal Claim/Result/Review authority was not exercised.

**Next independent scientific unit:** compute the primitive sixth-root Laurent coefficient at degree N^14 for exceptional m=6k+5 and decide whether that harmonic persists. Then determine primitive seventh-root nonzero orders, toward the first precision at which the minimal cost modulus would need the factor 7 (potentially 420). A future joint cost/threshold residual codec requires an observer- and operation-scoped preservation certificate.

Current rules and P000 remain distinct from the frozen scientific input. This finite rational model is not an assertion of a physical heartbeat, a native X6 coordinate or a BRC-native phase.
