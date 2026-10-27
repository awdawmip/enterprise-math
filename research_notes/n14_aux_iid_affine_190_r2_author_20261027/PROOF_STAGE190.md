# Stage190 — exact all-real N14 auxiliary IID theorem

Status: author-level exact proof and finite rational computation, 2026-10-27. This is an external three-symbol IID optimal stopping model, NOT a native P000 six-dimensional X6 Cell theorem. Independently authorized mathematical admission and Source CLAIM remain pending.

## Source freeze
GLOBAL_KNOWLEDGE_V1 main@a4cb0f12f564f73b484c63bd589a69189bb67edb was read with the canonical bootstrap/manual, P000 startup projection (original P000 blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc matched), ACTIVE worldview, math/BRC/code/activity rules. Enterprise Math scientific input main@633decfc27bdbcb7abc4458c94f8c85db9a41698 supplied P000, AGENTS, native X6/time, joint observer preservation and docs/PORTABLE_RESEARCH_PROTOCOL.md. Stage189 predecessor is f9cf70be909a20de67bd763f581fb6201b49c464 and archive SHA256 eaa467157119fc07fe4ad849a2535b23dceb906b9ceaf44a78db3c74a37ece1b. BRC priority REUSE_EXECUTED: positive-rational branch mass with ordered P/Q histories, not signed/complex amplitude; count compression is proved sufficient only for this finite IID Bellman readout, while independent DFS retains full histories.

## Exact theorem
With horizon N=14 and independent observations under P=(1/8,1/24,5/6) and Q=(1/12,1/12,5/6), permit all randomized stopping/decisions conditioned on complete ordered histories. Let eP=P(decide Q), eQ=Q(decide P), tP=E_P T and tQ=E_Q T. V14(alpha)=min of max(tP,tQ) over eP,eQ<=alpha.

alpha189=28110010813253777166137/80134219991312171532288,
V189=3460429309624219796220367/320536879965248686129152.

For EVERY REAL delta between 0 and 10778682563979325/30915979934919819264,

  V14(alpha189+delta) = V189 - (435639953102168932/1293441907677519)*delta.

The exact endpoint is
  alpha190=28137949158459611576537/80134219991312171532288,
  V190=3422790017676192400495567/320536879965248686129152.

Beyond alpha190 the fixed Stage190 Bellman supporting line is strictly below the value; this is NOT a global post-Stage190 value formula.

## Universal exact dual proof
At count state s=(n,a,b), the Q/P likelihood ratio is ell(s)=2^(a+b)/3^a. Backward induction at n<=14 takes h(s)=min{K*ell(s), L, 1+sum_i P_i h(s+e_i)}, omitting continue at n=14. Exact rational constants are
K=219205722106707916/1293441907677519,
L=72144743665153672/431147302559173,
H=h(0,0,0)=27408936515658794949498678792123439/212566265355324633731370212917248.

The exact sweep checks all 680 finite count states and finds 1238 strictly positive nonminimizing gaps, none negative; minimum 8957179515094375931/362080953867613958784. Exactly two Bellman ties: X=(8,0,1) Q/continue and Y=(4,2,0) P/continue. Conditioning on arbitrary complete ordered histories and the iid continuation distribution proves tP+K*eQ+L*eP>=H for EVERY history-dependent randomized policy. Since K,L>0, V14(alpha)>=H-(K+L)*alpha.

## Exact primal equality family and ordered history verification
Let x=probability of decide Q at X (else continue), and y=probability of decide P at Y (else continue). All other states use their unique Bellman-minimizer. X cannot precede Y because its depth 8 exceeds 4, and Y cannot precede X because the first-outcome count cannot decrease from 2 to 0. Therefore the tie cones are disjoint and the mixed coefficient in O(x,y) is exactly zero. With O=(eP,eQ,tP,tQ), exact suffix DP yields O=B+x DX+y DY, where

B=(612777799304353049/1752976676930715648,112911152064569/320979616137216,2373868606529886935/219122084616339456,284015611027565/26748301344768);

DX=(84427421875/17832200896512,-58984375/15479341056,-326450234375/2229025112064,-26297890625/104485552128);

DY=(-4043233651675/6086724572676096,576511225/495338913792,-21834391874875/253613523861504,-17521482625/371504185344).

All four deterministic corners were ALSO evaluated by a separately implemented, unmerged ordered-path DFS carrying P and Q integer weights in denominator 24^14. The four-vector results agree exactly with suffix DP. Visited DFS nodes by corner 00/01/10/11: 196750,182350,195982,181582, total 756664; first-hit X=8 and Y=6 each corner, zero cross ancestry. Complete four-corner fractions, original executed Python and stdout exist in the local portable archive. This is not a generic unconditional proof that BRC counting state alone retains history.

Solve eP=eQ exactly:

x(y)=11602917512839349/44937930240000000
    +(1335288430137/6241379200000)*y, 0<=y<=1.

This is legal for every real y in [0,1]; x(0) is the precise Stage189 endpoint coin, and x(1)=21216994209825749/44937930240000000<1. Y saturates first. Exact affine observations along this family are

eP(y)=eQ(y)=alpha189+(10778682563979325/30915979934919819264)*y;
tP(y)=V189-(2722749706888555825/23186984951189864448)*y;
tP(y)-tQ(y)=233320042494497107567613/961610639895746058387456
            -(285468475404923075/17390238713392398336)*y.

The last expression remains strictly positive at y=1; alpha increases strictly, P time decreases strictly, and direct substitution gives tP+K*eQ+L*eP=H identically. The derivative ratio is -(dtP/dy)/(dalpha/dy)=K+L. These feasible policies therefore attain the universal lower bound for all real intermediate alpha. This proves the theorem, not a finite-grid conjecture.

## Strict right sharpness
Compactness of the finite behavioral stopping-strategy space ensures a feasible minimum is attained. If an optimizer for any alpha>alpha190 attained the fixed H-(K+L)*alpha line, positive multipliers force BOTH eP=eQ=alpha and all reached actions Bellman-minimal. Other actions have strict gaps, so only X and Y may randomize. Each ordered prefix reaching the same tie state has the same positive likelihood ratio and the same future iid distribution; averaging any history-specific tie probabilities by their first-hit P mass gives a single effective x or y and preserves all four observables. The two cones are disjoint. Consequently error equality forces the same x(y) and alpha=alpha(y)<=alpha190, contradiction. The fixed Stage190 line is therefore STRICTLY below V14(alpha) for every real alpha>alpha190.

## Evidence, limitations and continuation
Locally executed Fraction Bellman+suffix DP+full ordered integer DFS: STAGE190_AUTHOR_EXACT_FULL_REAL_PASS. Separately locally executed reference in REPRO_STAGE190_REFERENCE.py: STAGE190_REFERENCE_EXACT_PASS. Stage191 exact gap scan: STAGE191_DUAL_SCAN_PASS. Complete evidence with original code, logs, rational certificate, full-length proof and per-file hashes is in EM_STAGE190_AUTHOR_EXACT_PORTABLE_20261027.tar.xz (SHA256 4509e9bd5751f1b4844e380f030eac343ced52eb5d5c9373e11b97aa5b730b69).

Stage191 is DUAL-ONLY: K=610519409541/3646579780, L=30208318184/182328989, H=531209309176160736181221937/4161698766215586030551040, new tie Z=(10,5,2) P/continue alongside X Q/continue. Its primal theorem and native X6 transfer are open. GH connection identity awdawmip had push access; native task inventory returned CONTROL_QUOTA and session_start returned STATIC_READONLY_SCOPE_DENIED (operation_sent=false), so no current owner confirmation, no CLAIM and no independent Research Driver acceptance were obtained.
