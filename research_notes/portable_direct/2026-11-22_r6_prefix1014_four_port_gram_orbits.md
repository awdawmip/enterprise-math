# PREFIX-1014 — Four exact port-Gram classes from eleven shared marked-collision signatures

2026-11-22 (+08). Status: **AUTHOR_EXACT_LAURENT_PROOF / SIGNED_BRC_INTEGER_CHECK_N5_TO_N8 / NOT_REVIEWED**. This is a model-internal result for the frozen Stage46 **candidate** signed BRC, not a Foundation promotion.

## Frozen source and observation
Continue PREFIX-1013 at enterprise-math@2148ee631e6db1425e0df0c7cd802d64ac4b1592. The scientific premise remains P000 V5 pinned at enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json. Use six-axis chart-relative X6 Cells, twelve native steps, incoming-neighbour ports h, integer transition numerator w(h,d)=1-6[ h=d ], next port -d, and double-direction absorption of the selected Link {0,e1}. The initial packet is (chosen Cell 0,h=-e1). Grade k=1 counts **exactly one negative native-axis step**. Coherent signed amplitudes are assembled within a joint Cell–terminal-port fibre *before* squaring; no renormalization or physical-time claim.

Define the four **squared numerator** masses at length n:
- Q^+_{n,1}: final actual step +e1, i.e. incoming port -e1.
- Q^+_{n,*}: final actual step +ej, for each fixed j=2,...,6.
- Q^-_{n,1}: final step -e1, i.e. incoming port +e1.
- Q^-_{n,*}: final step -ej, for each fixed j=2,...,6.

The S5 symmetry of the frozen input and Link proves equality inside each starred class, *without summing away terminal ports*. Probability masses are Q/36^n.

## Theorem — common eleven-collision exact formula for all n>=5
Work in the six-variable Laurent ring over Z, with S=sum_i z_i and U=sum_i z_i^(-1), m=n-4. Define
A_{n,j}=(n-1) S U -36(n-3) -6S/z_1 -6S/z_j,
B^+_{n,j}=z_j [ S A_{n,j} - z_1 A_{n-1,j} +25 z_1 ],
B^-_{n,j}=z_j^(-1) S (S-6z_j)(S-z_1).

The previously proved PREFIX-1004 full-port Laurent identities imply
F^L_{n,j}=S^m B^+_{n,j},  N^L_{n,j}=S^m B^-_{n,j}.
For a homogeneous degree-two Laurent polynomial B, write B=sum_alpha b_alpha z^alpha. Let
H_m(delta)=sum_{|a|=m} Mult(m;a) Mult(m;a+delta),
with out-of-range multinomial coefficients interpreted as zero.

**Exact four-class identity:** for j=1 or any fixed j>=2,
Q^{±}_{n,j} = sum_{alpha,beta} b_alpha b_beta H_m(alpha-beta)
= sum_{sigma in Sigma} K^{±}_{j,sigma}(n) H_m(sigma),
where H_m(sigma) means H_m(delta) for *any* zero-sum signed delta whose sorted absolute coordinate values equal sigma, and
K^{±}_{j,sigma}(n) = sum_{alpha,beta: sort(|alpha-beta|)=sigma} b_alpha b_beta.
This defines four explicit integer polynomials (degree <=2) per sigma, with *no growing Cell–port propagation state*. In this exact model all four share precisely the following eleven allowed signatures:

| sigma (ascending) | K+ 1 | K+ * | K- 1 | K- * |
|---|---|---|---:|---:|
| 000000 | 5(722n²−4834n+9139) | 3610n²−22826n+37907 | 1390 | 1006 |
| 000011 | 10(378n²−2503n+7519) | 2(1890n²−11723n+24029) | 8220 | 6348 |
| 000022 | −10(57n²−139n−233) | −2(285n²−1271n+1253) | 330 | −246 |
| 000033 | 10(2n²−3n−11) | 2(10n²−39n−1) | 20 | −28 |
| 000112 | −80(63n²−316n+352) | −16(315n²−1724n+2342) | 240 | −912 |
| 000123 | 240(2n²−7n−3) | 48(10n²−47n+27) | 0 | −576 |
| 001111 | −120(69n²−505n+961) | −24(345n²−2201n+3515) | −2520 | 72 |
| 001113 | 240(2n²−9n+1) | 48(n−1)(10n−41) | −240 | −528 |
| 001122 | 1080(n−5)(2n−1) | 1080(2n²−11n+11) | −2160 | −2160 |
| 011112 | 1440(2n²−13n+9) | 288(10n²−59n+69) | −4320 | −2592 |
| 111111 | 240(n−1)(2n−13) | 48(10n²−63n+83) | −960 | −384 |

Here 000112 means (0,0,0,1,1,2), etc. Coefficients refer to the numerator mass *of one terminal port*, not the S5-multiplied total. The all-port k=1 mass is exactly
M^L_{n,1}=[Q^+_{n,1}+5Q^+_{n,*}+Q^-_{n,1}+5Q^-_{n,*}]/36^n.

### Proof
1. The quoted PREFIX-1004 identities are equalities in the full Laurent Cell–incoming-port signed carrier; factor out S^(n-4) without summing over ports. The negative packet factorization follows from N^L=z_j^(-1) S^(n-3)(S-6z_j)(S-z_1).
2. The Laurent coefficientwise square norm of S^m B is the constant term of S(z)^m B(z) S(z^(-1))^m B(z^(-1)). Expanding the two multinomial factors yields exactly H_m(alpha-beta). This retains all same-fibre interference and no different-port interference.
3. Each B^+ has coefficients affine in n; each B^- is independent of n. Consequently each K is a polynomial of degree <=2. Exact multiplication of their at most 96 (positive) or 55 (negative) Laurent monomials gives the eleven signatures and table. Since affine coefficients have support contained in the union of their support at n=5 and n=6, two-point support enumeration captures every possible monomial at all n; the K table follows from a quadratic coefficient comparison at n=5,6,7. It is **not** a numerical interpolation assumption.
4. The PREFIX-1007 formal-series identity
sum_m H_m(delta)t^m/(m!)² = t^p prod_i sum_{r>=0}t^r/[r!(r+|delta_i|)!], p=sum_i |delta_i|/2,
proves that H_m(delta) depends only on the sorted absolute values of delta when sum delta=0. Every B term has total Laurent degree 2, so alpha-beta has zero sum. Thus the eleven-signature substitution is exact at all lengths.
5. S5 permutations of axes 2,...,6 preserve the initial port, the blocked Link, the signed BRC kernel and the squared joint-port observer. Hence the four port classes are exhaustive. QED.

## Exact integer evidence and numerical scope
The independent direct signed twelve-port Cell BRC recursion agrees with the eleven-signature formula at each individual terminal port for n=5,6,7,8. Four-class results (all are integer numerators, normalized only by 36^n):

| n | Q+ 1 | Q+ * | Q- 1 | Q- * |
|---:|---:|---:|---:|---:|
| 5 | 135110 | 109490 | 16560 | 12384 |
| 6 | 2918820 | 2532792 | 246870 | 191574 |
| 7 | 66735540 | 59610948 | 4299380 | 3455060 |
| 8 | 1607486710 | 1458235054 | 83992020 | 69575892 |
| 10 | 1064532083910 | 982562886810 | 40858323910 | 35414546374 |
| 20 | 546603450641366641962015310 | 523608038144842202757757750 | 9309183293108914043121660 | 8743165099121150271132924 |
| 30 | 677651055203849923631964793135399800872160 | 658391304488465309605671701221623098765040 | 7437065117530900694116692027052316442360 | 7141777762708534050771165046847302176504 |

The marked collisions are computed by the exact 6-axis binomial DP in PREFIX-1006, now restricted to eleven shared signatures. Its integer arithmetic cost for the fixed family through degree m is O(m²) per signature with O(m) working storage, excluding big-integer bit complexity. The local independent Python implementation agrees with all four BRC classes n=5..8, and evaluates the four formulas at n=10,12,16,20,30. n>=5 is proved from the Laurent identities; no universal inequality between distinguished and undistinguished port masses is asserted by those finite checks.

This upgrades PREFIX-1013's fixed-source n=5 class contrast to **all-length exact per-port formulas**, and sharply distinguishes it from PREFIX-1012's one-Green *signed total* observer. The full Cell–port carrier is required if it will undergo further propagation; the eleven-signature quotient is certified for the declared **terminal Gram/squared** observer only.

### Source attribution, control and next question
Historical contributor EM-DIRECT-FBEA5D / RA-3FB2D033BE6048D8712FF056 is provenance, not a present CLAIM. The original researcher SID recovery reports execution_authorized=false; do not infer Activity write authority. No formal PROGRESS, Result, review or Foundation admission is claimed.

Next: determine whether the two positive and two negative port-class contrasts admit a uniform sign theorem, or an even smaller A6-shift identity; compare future-horizon Gram propagation of two packets with equal current four-class readout. Original mother objective B_fix,odd(32) in {19,20} remains open.
