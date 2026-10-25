# C297 — Uniform outward-interval width, dyadic-grid termination, and 125 exact 512-bit brackets

**Status: AUTHOR EXACT / NOT ADMITTED / NO NATIVE CLAIM / 2026-10-25**

Model: C195/H168, the frozen **79-positive-rational-branch auxiliary** function `f(v)=F(v)/2^128`. This is not a theorem about native signed GF(2)-BRC, X6, the P000 three-dimensional research slice or physical dynamics. Primary source: C296 author commit `7832b54d97f363994ac00e65634ce5a49024b719` (unmerged research branch), including C275 original function, C288 125-path selection, C293 24-bit brackets, C296 256-bit brackets and its positive dyadic evaluator. Global knowledge read snapshot: `a7abbde1de0afbc58b533c89fef98140302c1196`; EM control main read snapshot: `60d41cbd0c1c9b219bc2d78ff10e4f664aab4cb7`. Control identity cannot register: native `CONTROL_QUOTA` on dispatch and `STATIC_READONLY_SCOPE_DENIED`, `operation_sent=false`, on session start. Hence no verified active owner, CLAIM or Driver acceptance.

## Theorem A: uniform a priori *width* for all precisions

The 125 C293 intervals are closed rational segments
`I_i=[k_i/2^24,(k_i+1)/2^24]`, with affine four-coordinate paths `v_i(t)=w_i+td_i`. On each interval, all relevant coordinate gaps, fixed-node gaps and positive numerators remain strictly signed: every such inequality is affine and holds at the two frozen endpoints. This guarantees no pole or absolute-value sign flip inside the interval.

For every positive rational factor `r=n/d>0`, C296 starts with integer interval
`[floor(2^P c),ceil(2^P c)]` for its positive branch coefficient `c`, and multiplies by `r` using
`[L,H] -> [floor(Ln/d),ceil(Hn/d)]`.
The starting integer width is at most 1. If the previous interval has integer width at most `E`, the new width is strictly below `r E+2`. Each factor in this model is a quotient of affine functions whose denominator has fixed sign, so its maximum on `I_i` is attained at one endpoint. Denote this *exact rational* maximum by `R_{i,j,l}`. Define the integer recurrence
`E_0=1, E_l=ceil(R_{i,j,l} E_{l-1})+2` for every factor of branch `j`. Sum the 79 final branch widths: `B_i=sum_j E_{i,j,last}`.

An exhaustive *exact-rational* check across all 125 strips gives
`max_i B_i = 16375417622426291165720915401788739733159 < 2^134`.
Consequently, for **every real** `t in I_i` and **every integer P>=0**, the 79-term outward integer evaluator satisfies
`0 <= H_P(v_i(t))-L_P(v_i(t)) < 2^134`.
This is a statement about the evaluator's error envelope, not merely 250 sampled points, and does not rely on any C285/C290/C292 derivative certificate.

Thus, for any endpoint with exact nonzero margin `mu=|f(v_i(t))-1|`, choosing `P` such that `2^(134-P)<=mu` (strict if needed) certifies the correct strict side. A fixed `P=b+192` does **not** follow universally from width alone: arbitrary dyadic endpoints can approach a root closer than `2^(-b-192+134)`, and an endpoint exactly equal to a root has no strict sign.

## Theorem B: explicit termination for nonroot dyadic inputs

Along each fixed path, the 75 fixed-node summands each have a rational-polynomial representation `N_j(t)/D_j(t)` with integer coefficient polynomials, positive denominator on the C293 strip, and denominator degree at most 4. Each of the four moving-node summands has base denominator `((2-p(t)^2)(3-p(t)^2))^3` of degree at most 12, 75 fixed-node pole factors and three moving-node pole factors, for denominator degree at most `12+75+3=90`. Every numerator degree is no larger than its corresponding denominator degree. After taking the product of these 79 denominators and summing the numerators, the *normalized* `f(v_i(t))=A_i(t)/D_i(t)` has integer polynomials `A_i,D_i`, with `D_i>0` and `deg(A_i-D_i)<=75*4+4*90=660`.

For each rational coefficient factor, clear denominators in the numerator and positive denominator polynomial *by the same positive integer*. Define `M_i` as the product of the resulting denominator coefficient 1-norms, across all factors in all 79 terms. Since polynomial coefficient 1-norm is submultiplicative and `0<=t<=1`, `0<D_i(t)<=M_i`. Summing the exact integer bit lengths of these factor norms yields `H_i` with `M_i<2^H_i`. An exhaustive certificate establishes `max_i H_i=73527`.

For `t=k/2^b in I_i`, if `f(v_i(t)) !=1`, the nonzero integer polynomial `A_i-D_i` of degree at most 660 obeys
`|(A_i-D_i)(k/2^b)|>=2^(-660b)`.
Therefore
`|f(v_i(t))-1|>2^(-660b-H_i)`.
Combining with Theorem A, the explicit, conservative choice
`P=660b+H_i+134`, or uniformly `P=660b+73527+134`, *always* certifies the strict sign of **every nonroot dyadic point** in these frozen strips. This is a termination theorem, not a claim that this large precision is practical. Exact equality to the threshold must be handled as an equality, not called a failed nonzero sign certificate.

The fixed 79-term straight-line circuit has bounded length. If its input rational coefficient heights are bounded by the frozen constant `L`, evaluating a dyadic point of precision `b` at `P=O(b+L)` has integer operand bit widths `O(b+L)` (factor construction included) and costs `O((b+L)^2)` bit operations with schoolbook integer arithmetic for this *fixed circuit*, up to constants depending on its 79 labels and 125 fixed paths. It does not establish bounded resource requirements for varying node populations.

## Theorem C: new finite, exact 512-bit root certificate

The previous 125 C296 certified root brackets at width `2^-256` are extended to width `2^-512`. The compact suffix certificate stores for each path a 256-bit nonnegative integer `s_i`; reconstruct
`K_{i,512} = 2^256*K_{i,256}+s_i`.
At the two endpoints `K/2^512` and `(K+1)/2^512`, exact positive *integer* outward rounding at `P=704` proves **250/250** strict inequalities:
`f(v_i(K/2^512))<1<f(v_i((K+1)/2^512))`.
Their normalized strict margins are all greater than `2^-528`; all candidate corrections were zero. A separate direct full-`Fraction` computation checks 32 prespecified endpoints (path indices 0,8,16,...,120; both endpoints), without using the interval evaluator for their signs. All 512-bit intervals nest inside their corresponding C296 256-bit intervals. Existence follows by IVT. Uniqueness/simplicity and pairwise root-box separation are *upstream author-level dependencies* C285/C288, not newly established by finite signs.

The compact evidence is a zlib/base64 encoding of 125 unsigned, big-endian 32-byte suffixes (4000 decoded bytes). Verify `C297_COMPACT_CERT_METADATA.json` and use `C297_REPLAY_512_EXACT.py` to reproduce all 250 strict signs with stdlib Python and the frozen upstream modules. Run `C297_UNIFORM_WIDTH_AND_HEIGHT_EXACT.py` for the two uniform theorems; original local package also includes the candidate proposer and 32-endpoint independent check. Approximate `mpmath` arithmetic selected integers only, never established signs.

## Research limits and next question

The measured `2^134` guard bound is a conservative all-strip forward-error envelope; `73527` is a very conservative coefficient-denominator height and `660` is a degree cap, not minimal algebraic degree. Neither automatically proves `P=b+192` for every future dyadic refinement. Next: exploit shared denominators and cancellation-safe exact remainders to reduce the *proved* separation slope and denominator-height constant; separately investigate the missing native GF(2)-BRC phase/port/provenance-to-auxiliary-map.

**Reuse resolution:** C296 positive dyadic evaluator and frozen C275/C288/C293/C296 source are `REUSE_APPLIED`; existing functionality was executed unchanged for 512-bit sign verification. The added width/height certificate is a problem-specific proof around that existing tool, not a new top-level BRC family.

**Research outcome:** author-level exact derivation plus finite certificates, **not** Source Result, independent Driver review, Foundation or P000 admission.
