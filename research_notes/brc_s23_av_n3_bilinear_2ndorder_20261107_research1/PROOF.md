# S23 conditional AV (n=3): second-order grid-to-continuum certificate

Date: 2026-11-07. Classification: AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_EXECUTED / REVIEW_PENDING.

## Frozen scope and verified inputs

Scientific input pin: 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Fixed 8x27 rational kernel K: research_notes/brc_s23_av_n3_uniform_quarter_upper_20261107_research1/KERNEL.json (blob 564acd9574876059c505fd8a40d14f2f6e0e3736).
Prior 8192-grid exact evidence: research_notes/brc_s23_av_n3_dense_grid_8192_exact_20261107_research1/RUN_EVIDENCE.txt at commit 3d1cced9d8b5b9a8a17a1064f3a01bc7a48ae267.
The 8192 enumeration is REUSED, not re-executed in this iteration; the 256-grid exhaustive integer check is independently executed.

For a,c in the entire real square [1/2,7/8]^2, let z=(1-a)c, p=(a,z,(1-a)(1-c)), b=(z,1-z). Three ordered conditionally IID full outputs have law p^tensor3; the compressed-input reconstruction has law (b^tensor3)K. Put F(a,c)=p^tensor3-(b^tensor3)K in R^27 and E_K(a,c)=||F(a,c)||_1/2. Delta_3 is infimum over parameter-independent stochastic kernels of supremum E_K.

## Lemma: quadratic bilinear interval enclosure

For every vector-valued C^2 F on a rectangle of side lengths h_a,h_c, write A=sup||F_aa||_1 and C=sup||F_cc||_1. Then

sup_rectangle TV(F) <= max_four_corners TV(F) + (h_a^2 A + h_c^2 C)/16,

where TV(F)=||F||_1/2.

Proof. Let I_a,I_c be endpoint-linear interpolation. The Banach-valued linear interpolation Peano kernel has nonnegative weight and total integral (x-u)(v-x)/2<=h^2/8. Hence ||F-I_a F||_1<=h_a^2 A/8 and ||F-I_c F||_1<=h_c^2 C/8. Decompose F-I_a I_c F=(F-I_a F)+I_a(F-I_c F). The I_a coefficients are nonnegative and sum to one, so ||F-I_a I_c F||_1<=(h_a^2 A+h_c^2 C)/8. The bilinear interpolant is a convex combination of corner vectors. Triangle inequality and division by two prove the result. No mixed derivative is needed: bilinear interpolation retains all affine mixed terms. QED.

## Uniform derivative estimates on the lawful AV square

p_a=(1,-c,-(1-c)), ||p_a||_1=2; p_c=(0,1-a,-(1-a)), ||p_c||_1=2(1-a)<=1. Both pure second derivatives p_aa and p_cc are zero. Likewise b_a=(-c,c) has norm <=7/4, b_c=(1-a,-(1-a)) has norm <=1, and b_aa=b_cc=0.

For threefold tensors, the pure second derivative sums over six ordered distinct pairs of positions. Tensor products multiply l1 norms. Row-stochastic K contracts the signed l1 norm. Therefore

||F_aa||_1 <= 6*(2^2+(7/4)^2)=339/8;
||F_cc||_1 <= 6*(1^2+1^2)=12.

The sum is 435/8. For the uniform square grid step h=3/(8N), the new uniform extension is

SUP_REAL E_K <= MAX_GRID_N E_K + 3915/(8192 N^2).  (1)

For general n>=1, the corresponding extension valid for any fixed stochastic 2^n x 3^n kernel on this same box is 1305*n*(n-1)/(16384*N^2). For n=1 bilinear interpolation is exact.

## New certified bounds

The supplied VERIFY.py independently enumerates the N=256 grid of 66,049 rational pairs, all 27 ordered outcomes, and reproduces the previous maximum at (i,j)=(141,256):

MAX_GRID_256 E_K = 1046025373084480007/4398046511104000000.

Using (1) gives the wholly rerun, all-real bound

DELTA_3 <= 1046057444764480007/4398046511104000000
         = 0.23784592594085552... < 0.237846.

Reuse the existing N=8192 exact-grid proof certificate:

MAX_GRID_8192 E_K = 21422604982162266373/90071992547409920000.

The identical proved analytic enclosure now yields

DELTA_3 <= 21422605623595866373/90071992547409920000
         = 0.23783870010780492... < 0.237839.  (2)

The previous lower bound 5211/21952 <= DELTA_3 remains unchanged; the author's present interval gap is 0.00045714034104106... . Formula (2) improves the earlier continuous extension 27/(16N) to O(N^-2) without a new 8192 enumeration or a new kernel.

## BRC and scientific boundaries

Observer: stop3 maps to Y, stop1 and stop4 map to N; ordered branch identities and the single shared hidden (a,c) are retained in the full tensor law. BRC reuse resolution: REUSE_APPLIED (positive-rational branch probabilities; retained provenance and no hidden-state quotient). This result concerns the conditional AV auxiliary experiment. Transfer to the lawful six-source, ten-label mother R_beh(k,10) requires a separately verified encoder/decoder/source map.

This is an author-side analytical proof with exact arithmetic validation; independent mathematical review and admission remain open. The current native service identity/version mismatch prevents confirmation of formal CLAIM and active owner.

## Next discriminating mathematical unit

Find whether the fixed K attains its true continuous supremum on c=7/8 via exact polynomial sign/derivative regions, particularly near a~0.7064. Alternatively construct a rational primal/dual kernel witness approaching the known lower certificate, and separately check lawful ten-label transfer.
