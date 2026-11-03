# BRC S23: sharp global inverse stability for the minimum two constant-overwrite probes

2026-11-03 (Asia/Shanghai). AUTHOR_ANALYTIC_PROOF / EXACT_BIGINT_EXECUTED / UNREVIEWED / NOT_ADMITTED.
Frozen scientific model: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Immediate verified predecessor: 8f44ac0f8981920f16ddaaa5f9a8414aec32e3db (two-probe complete classification and global inverse bound).

## Exact model

For every z in [0,1]^11 retain the six ordered gate triples:
A=(0,0,0,1,1,1), B=(2,2,3,2,2,4), C=(5,6,7,8,9,10).
A triple (a,b,c) gives four labeled outcomes
R(a,b,c)=(a,(1-a)b,(1-a)(1-b)c,(1-a)(1-b)(1-c)).
Mix the six raw source rows by M/20, with
M=((10,10,0,0,0,0),(9,11,0,0,0,0),(0,0,20,0,0,0),
(0,0,0,10,10,0),(0,0,0,2,18,0),(0,0,0,0,0,20)).

Let U_I^beta replace z_k by a common known beta for k in mask I, where I is a subset of the first five gate indices. For F one of
(3,31), (7,27), (11,23), (15,19), with five-bit mask encoding,
Phi_F,beta(z) consists of baseline P(z) and the two additional probes P(U_I^beta(z)).
Define d_F,beta(z,w) to be the largest total variation distance between corresponding labeled four-outcome observation rows across these three views. The input distance is eps=||z-w||_infinity.

## Theorem: exact all-state inverse modulus

For every one of the four F and all real beta in [0,1),

    inf_{z != w in [0,1]^11} d_F,beta(z,w)/||z-w||_infinity
       = (1-beta)^2/21.

The infimum is attained by the same explicit lawful pair for all beta and all F. Thus the best global inverse Lipschitz constant is exactly 21/(1-beta)^2, not merely an upper bound. In particular beta=1/2 gives the sharp coefficient 1/84 from the predecessor. In the allowed design interval [0,1), beta=0 uniquely maximizes the guaranteed separation, with coefficient 1/21. The beta=1 observer is noninjective.

## Proof over the complete real eleven-parameter cube

The predecessor established the lower inequality d_F,beta(z,w) >= (1-beta)^2 eps/21 for beta in (0,1). Its exact source-unmixing has maximal absolute coefficient row-sum 21; per-outcome difference is bounded by raw-source TV; recovery divides root differences by 1, middle differences by (1-beta), downstream differences by (1-beta)^2. The argument uses only 1-beta>0 and thus extends unchanged to beta=0, proving the lower inequality for every beta in [0,1).

For an equality witness take z0=...=z4=w0=...=w4=1. Set z5=1,w5=0,z6=0,w6=19/21; set z7=...=z10=w7=...=w10=0. Then eps=1. Only raw sources 0 and 1 depend on differing gate coordinates (third gates 5 and 6), and both use first gate 0 and second gate 2.

Every listed optimal two-mask pair has exactly one mask that contains {0,1,2}; its other mask omits 2. The original baseline hides these downstream differences because both upstream gates are 1. The probe omitting 2 likewise hides them because its second gate remains 1, even after overwriting the first gate. All other source rows have equal parameters in z,w.

In the sole revealing probe define alpha=(1-beta)^2. The raw source 0 and 1 third-outcome differences are alpha and -19 alpha/21; the fourth-outcome differences are opposite and the first two outcome differences vanish. Mixing with rows (10,10)/20 and (9,11)/20 gives observed third-outcome differences

    (10 alpha - 10 * 19 alpha /21)/20 =  alpha/21,
    ( 9 alpha - 11 * 19 alpha /21)/20 = -alpha/21.

Their fourth differences are opposite, so each of these two labeled-row TV distances equals alpha/21. Every other corresponding row TV is zero. Hence d_F,beta(z,w)=alpha/21, attaining the global lower bound. At beta=1 alpha=0, so the same distinct states become observationally identical. QED.

## Reuse and scope

The proof is an exact positive-weight BRC/S23 branch-observer statement with all six source labels, branch order, mixer and four output positions preserved. It uses specified algebraic future replacement operations. It does not modify P000 or claim native Heartbeat evolution or phase-cancellation semantics. The predecessor forward bound d<=3 eps remains valid; its sharpness is a separate question.

VERIFY.js is a dependency-free Node.js BigInt rational evaluator of the actual original source matrix, all three views and all four mask families. It checks beta values 0, 1/4, 1/2, 3/4, 9/10 and 1: 24 exact identities. RUN_EVIDENCE.json contains actual runtime results. The all-real theorem uses the analytic inverse and equality witness, rather than treating the finite beta check as a universal proof.
