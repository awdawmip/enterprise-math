# PREFIX-1161: selective raw-moment refinement and scale-adaptive exclusion

Date: 2026-11-28. TASK_RESEARCH, historical own registration EM-DIRECT-780BBE / RA-0ABD84561C86E53067DB0322 recovered from original session-start receipt r6-20261123-2358-session-start-own-v1 (SUCCEEDED, managed custody not revoked, no execution claim). Auxiliary parameter arithmetic, not a native Heartbeat computation. AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_AUXILIARY_COMPUTATION / AFFINE_OUTER_MODEL_WITNESSES / CONDITIONAL_STAGE46_APPLICATION / NOT_REVIEWED.

## Frozen inputs and authority

Continue PREFIX-1160 e484595611c07fb3add6448fe7cc1d95efc78bb9:research_notes/portable_direct/2026-11-28_r6_prefix1160_raw_resolution_bottleneck.md. Its execution archive SHA256 76bae51dabf7c61fd8902c34f9cea0474f8d95bb13daf4c000a7201d5186e0af; all 421 manifest entries passed. Frozen P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d and its joint-observer, Heartbeat and residual-fidelity companions read; account rules at 945479e4b9b3c6f6caef5c962bd1016b073afb43, current control Source at 1090b2b3029964ae13dbab383b07e910de1da16b. Owner inventory request r6-20261128-2348-owner-check SUCCEEDED; snapshot INV-c93e7b1e290303e271d4cd341f3c9d42 at 2026-11-28T15:48:47.828819Z, 547 tasks, LEASED filtered list empty, unchanged Source and event guard at completion 15:50:04Z. No new CLAIM, no shared task-state write. Original Stage46 asymptotic, anchor exit, affine transfer and primitive-relation reduction hypotheses remain load-bearing.

## 1. Actual targeted raw and integration-grid refinement

Retain the six-component shared anchor, twelve shared columns, two point rows, and eight lower-order moment rows. Refine exactly the five highest-order moment rows (zero-based 10--14): (k,j)=(14400,0),(16000,0),(20000,0),(14400,1),(14400,2). Raw grid Hraw=10^165 rather than 10^150; integration arithmetic J=10^170 rather than 10^155; final observation grid G=10^170 rather than 10^155. Original 9600 anchor and Frobenius N=300 are unchanged.

The five raw floors were actually recomputed by the inherited GMP exact integer recurrence in moments1148.cpp, changing only mpz_ui_pow_ui(H.get_mpz_t(),10,150) to mpz_ui_pow_ui(H.get_mpz_t(),10,165). All recurrence divisions and binomial divisions are checked exact before integer division; the final signed sum is divided by its positive exact denominator with floor rounding. Thus if v is the output integer, v/Hraw <= raw moment < (v+1)/Hraw. All five satisfy floor(v/10^15)=the previous integer floor. The recomputed five integers are published at 41da53a26293c950edaf78f33fb1138a67cad5cd:research_notes/portable_direct/2026-11-28_r6_prefix1161_moments.txt (Git blob a99b1195294f15cdeb89e814fe9bfda5ebf770a0, SHA256 7cda76c062af18052532cca74b843f3a503d4d6488ab1b36376d4ba89b1a7331).

For each refined row use the inherited outward-grid interval integration of the four Frobenius branches and two integration coordinates. Every integrated summand is rounded down at J only when both rational interval endpoints imply the same floor. Independently restore each old J=10^155 row exactly before accepting the new row. The basis tail sum is verified below 10^-180, and every shared anchor coefficient absolute value is bounded by one. At most 4*(N+1)+1=1205 summands contribute to the integration rounding budget. For the inherited channel-tail coefficient c_j=1 for j=0 and 6^(j+1)/(j+1) otherwise, the complete error is
delta = c_j*(35/36)^k + 1/(2*Hraw) + 10^-180 + 1205/J.
The second term comes from using the midpoint (2*v+1)/(2*Hraw). With exact rational center M and twelve shared coefficients B_l, store m=floor(G*M), C_l=floor(G*B_l), e=ceil(G*delta)+13, which pays at most one grid unit for each of the center and twelve shared coefficient roundings. Other rows are rescaled exactly; no prior error is silently dropped. All five refined radii equal 51219/G, and each old/new normalized radius ratio equals exactly 10^15. No new anchor or point calculation.

## 2. Old minimum exclusion and new section

Keep U=[C,diag(e)], A,B the original observation map rescaled to G. A candidate (q,p,h) has offset v=A(p/q-r)+B(h/q-u)-m. For an oriented functional n, separation is certified by
n.v > sum_j |n.U_j| + max(0,-n.A)*K/L^2 + max(0,n.B)*H/L.
The right side is nonincreasing for positive L. Exact rational max-volume pivot and sparse cofactor supports exclude the old qstar=1809754881531112186904694767481139172491414761359983491189786084567209150450511632496318670 at all L>=10^142. Independently evaluated oriented ratio at L=10^142 is 35.8118756767 (strictly >1); zero-scale ratio 158795878.5441, centered full-scale ratio 70.62373565 have different centers. Neither floating LP nor a changed error budget alone is needed for this separation.

Intersect old 16-vertex ratio section with 15 inverse-pivot and eight cofactor observation strips, retaining the support payments for all 27 generators. The eight cofactor directions use the seven-element subsets of {0,1,9,10,11,12,13,14}, and exactly cancel the first six columns on the new integer observation grid. Iterative clipping and all pairwise boundary intersections produce the same 16 vertices. New outer widths: rho 2.0048382800122707e-133, c 9.615337233311515e-133; previous widths improve by factors 1.00441309494 and 1.00441352447. These are outer-section widths; the large row precision gain is not a comparable gain in marginal widths.

## 3. Complete finite searches, monotone bounds

For L>=L0, the ratio domain is contained in P+[-K/L0^2,0]x[0,H/L0]. Use the maximum-area triangle observer metric and rational LLL with unimodular integer coordinates V,W (VW=I). A complete integer coordinate box follows from affine extrema at the polygon vertices and both denominator endpoints q0,Q. Exact interval elimination of the third integer coordinate and independent complete box enumeration in original-coordinate inequalities agree, including gcd(q,p)=1 under the inherited primitive reduction.

| L0 | Q | Complete box | Feasible | Primitive | q minimum |
|---|---|---:|---:|---:|---:|
| 10^142 | 3*10^91 | 45 | 2 | 1 | 1.6073455535e91 |
| 10^144 | 10^93 | 9240 | 1294 | 779 | 6.1110675725e91 |
| 10^146 | 10^94 | 98022 | 13011 | 7905 | 2.1685232978e92 |

Exact minima, in order:
16073455535007586418515856907980369971420624533773806841684237214267633166615711357693195931
61110675724865000272090069090060010536059594770586885717064088064213580235041701932613181493
216852329778244406868370584860521101728151521982456628993043813329465750319327160378889219902

Under the inherited hypotheses b-a>=q>=the respective minimum for every L>=L0, not merely the sampled L. The last bound is 119.8241441 times the preceding large-scale bound. Its scope is L>=10^146; at L>=10^142 the new minimum improves the old bound by about 8.88. The attempted larger search (L=10^148) was interrupted by execution timeout; no result is claimed for it or later scheduled loop entries.

## 4. Full fiber diagnosis

For each of the three minima the zero-scale full affine model is strictly separated (respective certified support ratios approximately 2974912.2151, 4372.4194, 255.9433). Each is feasible in the corresponding centered full-scale 29-generator model, with rational coefficient witnesses verified exactly in all 15 rows; slacks respectively >0.0516, >0.1972, >0.3671. This is an outer-model obstruction, not actual abnormal pairs. Further precision refinement alone need not address it; use the existing signed-scale critical inequality and joint scale relation to eliminate these candidate families at higher L. At zero scale there remains information to extract beyond the current sparse-section widths.

## 5. Stitched dyadic windows

With inherited triple necessary q^2<4E L/dlo, E=400000, and near-pair gap<=sqrt(L), the earlier verified dyadic coverage already exceeds 10^146. Stitch at that scale using the last exact minimum. Starting at L=10^8*2^j, the first not excluded triple and near-pair starts are approximately 3.8645375230172583e179 and 5.065326622169181e184; relative to PREFIX-1160 the exact factors are 16384 and 8192 respectively. These are exclusion endpoints, not found anomalies. Continuous integer endpoint remains 4.72478e43; anchor exit confirmation, unbounded final separation and B_fix,odd(32) remain open.

## 6. Reproduction

Extract PREFIX-1160 execution evidence (pinned SHA256 above). Recompute moments1161.txt using the single-source change in section 1:
sed 's/mpz_ui_pow_ui(H.get_mpz_t(),10,150)/mpz_ui_pow_ui(H.get_mpz_t(),10,165)/' moments1148.cpp > moments1161.cpp
g++ -O3 moments1161.cpp -lgmpxx -lgmp -o moments1161
./moments1161 14400 16000 20000 > moments1161.txt
The executed new C++ SHA256 is 360a069da6dfbeeab555947e09733f2547e97386e3177639597394cf38a31ba4. The actual Python refinement source is saved at 046d5869a2eb6002abcf2244bb265a0c8c54c0e8:research_notes/portable_direct/2026-11-28_r6_prefix1161_refine.py (SHA256 d442a4a4bbc86b74b2923e7f6a7024494deec0a348783ab83970bc0e006dae11; Git blob dc1734815c87b5d51f2a57a823042f4994e40a37). Run from the extracted directory with the saved raw file. It writes each completed run incrementally; stop after the third completed search to reproduce the claimed scope without the timed-out larger search. New grid SHA256 8fd5d21036ab2c19ebd1c5f05708255c9ba5d76b6930a56ed0bb451184bef1e5; completed section/run record SHA256 b91283fe603bc0cf4266f9e99ed3ae3d9f4eb50528742f0b0d1b8c789b2bc939; executed log SHA256 15d58543734142812ced7bfa2b586531465247c0645e4e6d5036f985b1aaf4d7. Full local evidence includes exact matrices, candidate lists, fiber witnesses, signed support normals and timeout log. The old archive is an exact prerequisite, not a newly revalidated analytic Stage46 proof. Next: exploit signed-scale critical thresholds and more informative observer normals before increasing raw moment precision again.
