# D25 p=139: exact source-resolved signed third-digit witness

2026-11-04 Asia/Hong_Kong. TASK_RESEARCH / author-side exact finite certificate / UNREVIEWED / NOT_ADMITTED. Pinned mother Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; scientific input c47e13e4aba0e006366f989d6334d443f6333ae3. Reuses the previously published p² Sun square and p³ derivative-defect identity.

For p=139 and R=(Z/p³Z)[s]/(s²-2), let x_a=(2+s)/4, x_b=(3+2s)/6, T_a=-s/4, T_b=-s/24. The **full original** unweighted 216/2304 sums and weighted moments computed by integer binomial coefficients modulo p³ are:
A=1024013, B=1004692, M_A=1619767, M_B=881538.
W=A+6M_A=139 and V=B+8M_B=139 mod p³. The nonzero third-digit source terms are (A-B)/p²=1 and (6M_A-8M_B)/p²=138 mod p.

An independently executed direct p³ polynomial-convolution/derivative checker (using the actual truncated coefficients and differentiating *before* Frobenius evaluation) returns:

| typed observer (u,v)=u+v*s mod139 | original 216 | original 2304 |
| --- | --- | --- |
| U=F(x)/p | (82,0) | (69,0) |
| E(x) | (138,0) | (122,0) |
| E'(x) | (3,53) | (50,73) |
| full unweighted sum /p² | 53 | 52 |
| full first moment /p | 116 | 87 |

The **four original signed observer components** are:
1. U_a²-U_b²=(17,0);
2. -E_a(x_a)+E_b(x_b)=(123,0);
3. (6T_aF_aF'_a-8T_bF_bF'_b)/p²=(106,64);
4. -3T_aE'_a(x_a)+4T_bE'_b(x_b)=(32,75).

The unweighted pair totals (1,0), the weighted pair totals (138,0), because 64+75=139≡0. Their total is (0,0). Integer divisions by p and p² are performed only after exact divisibility checks in Z/p³Z.

This discriminates two mechanisms at **the same target-class prime** (139≡19 mod24). The separately proved scalar-map obstruction shows E216 and E2304 fail scalar proportionality here: the only candidate lambda=135 matches [X^(p+1)], [X^(p+2)] but misses [X^(p+3)] by 14. Yet the fully signed evaluation-plus-derivative observer vanishes. Preserving signs, quadratic-extension coordinates, degree provenance and the operation order is essential to the demonstrated cancellation. This p139 witness does not prove the universal p³ target or replace the p373 H0/B0 native benchmark (#1559).

The local exact Python check invoked the preceding d25_sun_third_digit_defect_checker_20261104.py at p=139 (original complete convolutions, F/F', E/E', both original sums); all assertions passed. Next action is to construct an evaluation-plus-derivative signed Green/WZ terminal transport across the full D25 target classes, test at p=139,13,19,373, and keep scalar simplification rejected for its proved coefficientwise scope. No Source CLAIM/run/Result is asserted by this author-side note.