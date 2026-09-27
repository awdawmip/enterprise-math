# RP9-B supplement: two exact dyadically balanced Gram blocks have condition number below two

Progress-Event-ID: RP9B-C971348E-GRAM-2544-PAIR
Status: AUTHOR_SYMBOLIC_DERIVATION_FROM_STORED_BRC_GRAM / UNREVIEWED / NOT_ADMITTED
Source continuation: https://github.com/awdawmip/enterprise-math/blob/660267a6fa8417451c6d9ed647a40e243e2644bd/research_notes/HEARTBEAT_RP9B_INVERSE_FREE_GRAM_C971348E_2544.md
Input: CURRENT conversation RP8_PACKED_CHECKPOINTS.json, file_000000000e88820b900184c4537001e9. Associated attachment package is identified by its delivery record as d680a1d633f32df579ee8fa27e3281b6a98d1cb72d82ad36a66ae4ab516d94a0. The distinct cloud a71213a7 version is not substituted.

No new program, BRC core call, eigenvalue computation, factorization or performance experiment was run. These are exact substitutions in stored complete BRC Gram identities and elementary quadratic-form inequalities. Their future native replay remains pending. P000 and all scientific state/gate semantics are unchanged.

## Lemma: an exact coefficient-space condition certificate

For a symmetric two-by-two block K=[[a,c],[c,b]], let

    l=min(a-|c|,b-|c|), u=max(a+|c|,b+|c|).

From 2|xy|<=x^2+y^2, for every coefficient vector v,

    l*(v_1^2+v_2^2) <= v^T K v <= u*(v_1^2+v_2^2).

If l>0, K is positive definite and its spectral condition number is at most u/l. Thus u<2l is a strictly rational certificate of condition number below2. This does not require a numerical eigenvalue or square root. The ordinary coefficient norm in the inequality is an algebraic diagnostic, not a redefinition of native geometry.

## N143: zero-based columns 1 and 7

First replace f_7 by h=f_7-f_1 as in the parent note. The exact two-column Gram is

    [[3298174993,3317500],
     [3317500,49408]].

Then use basis columns f_1 and 2^8 h. The second vector can be stored as the SAME small integer mantissa h plus exact exponent8; its coefficient is divided by2^8. No rounding occurs. The resulting Gram is

    K143 = [[3298174993,849280000],
            [849280000,3238002688]].

Indeed3317500*256=849280000 and49408*65536=3238002688. The lemma gives

    l143=2388722688,
    u143=4147454993,
    u143 < 4777445376 = 2*l143.

Therefore condition_2(K143) <= 4147454993/2388722688 < 2.

For an original coefficient pair (d_1,d_7), the exact replacement is (d_1+d_7,2^-8 d_7). Every other coefficient, work label, radial scale and escape record remains. In particular, this is not a new approximation of any full row. h has maximum mantissa magnitude171, but the materialized scaled column has a larger magnitude: mantissa length and true scale are not conflated.

## N253: zero-based columns 0 and 3

First use h=f_3+f_0. Its exact Gram with f_0 is

    [[1297951293,15146835],
     [15146835,30672681]].

Use columns f_0 and2^3 h. Then

    K253 = [[1297951293,121174680],
            [121174680,1963051584]].

The lemma gives

    l253=1176776613,
    u253=2084226264,
    u253 < 2353553226 = 2*l253.

Therefore condition_2(K253) <= 2084226264/1176776613 < 2.

Original coefficients (d_0,d_3) become (d_0-d_3,2^-3 d_3). The exact scale is retained; h's maximum mantissa magnitude5245 is not its scaled physical row magnitude.

## What this does and does not add

The parent note establishes smaller difference/sum mantissas. This supplement also establishes that the SELECTED two-dimensional coefficient blocks can be made well conditioned using exact integer column operations and powers-of-two scaling, with no fractional orthogonal basis or dense inverse.

It does NOT imply that the complete eight-by-eight or seven-by-seven Gram has condition number below2. Correlations with all remaining columns can still cause near-dependencies. A well-conditioned principal subblock is not a lower bound on the smallest eigenvalue of the full matrix. There is no executed statement about iteration counts, full payload, RSS, final-output law changes or time to a verified factor.

A tested solver may use such blocks as candidate preconditioners, but must preserve all couplings, exact label incidence and Q_K boundaries. All changed coefficients and exponents must be charged. The compact integer mantissa savings can be offset elsewhere. This is a small concrete algebraic entry point for the inverse-free residual method, not a generic complexity result.
