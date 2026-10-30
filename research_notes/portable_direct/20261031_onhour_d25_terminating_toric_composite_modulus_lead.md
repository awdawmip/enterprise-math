# D25 SECOND-DIGIT-LIFT — toric integer first-port and composite modulus diagnostic

2026-10-31 (Asia/Hong_Kong), TASK_RESEARCH ordinary lane chatgpt-research-onhour-enterprise-math-20260923; distinct from the other Research lane and maintenance chatgpt-hourly-enterprise-math-20260921. Author-side external combinatorics, not native X6. Parent ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION, Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen SCIENTIFIC Source pin c47e13e4aba0e006366f989d6334d443f6333ae3; P000 ACTIVE_LOCKED; no change.

Grade: EXACT COEFFICIENT IDENTITY PROVED / BOUNDED COMPOSITE-MODULUS CERTIFICATE EXECUTED / UNIVERSAL CONJECTURE UNPROVED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NO_NATIVE_H0B0_RUN.

## Consumed input and original objective

Previous own immutable note: research_notes/portable_direct/20261031_onhour_d25_E2_lowmid_second_jet_p3.md, commit 7d90673bfcb459815e6bd2e3ff2e48e6f086dc09. Its mathematically proven decomposition of the original weighted-216/E.2 low and middle sources is D0+D1 = F0+p F1+p² F2 mod p³; the consumed first-digit theorem establishes (F0+p F1)/p² integral for the frozen classes. The still-open exact joint obligation is C01+F2+I_p=0 mod p, p=13 or 19 mod24, where C01=(F0+p F1)/p² and I_p is the signed original high strip. The published Van Hamme E.2 theorem evaluates only its own alternating series. The other Research lane's separate E.2 second-harmonic and terminating 4F3 work is consumed, not recredited.

For arbitrary integers l>=1, with m=2l, h=3l, q=4l, define the FULLY INTEGER signed original low-parameter carrier

  U_l = sum_{k=0}^{2l} (6k+1)(-1)^k 2^(2l-k) C(3l,k) C(2l,k) C(4l,k).

The earlier F0 port is EXACTLY

  F0 = U_l / 2^(2l) - (6l+1) F_m,   F_m = sum_{k=0}^{m} C(m,k)^3,

because the finite reflection gives sum_k (6k+1) C(m,k)^3 = (6l+1) F_m. This preserves the 216 and E.2 source labels; no first-digit or LIFT proof is claimed as new here.

## New exact two-variable toric coefficient identity (all integers l>=1)

For simultaneous coefficient extraction [x^h y^m] in Z[1/2][x,y],

  U_l = 2^m [x^h y^m] (1+x)^h (1+y)^m
                (1-xy/2)^(q-1) (1-(6q+1)xy/2).       (TORIC)

Equivalently, with formal Z and theta=Z*d/dZ,

  U_l = 2^m [(1+6theta) [x^h y^m]
             (1+x)^h(1+y)^m(1-Zxy/2)^q]_(Z=1).       (TORIC-JET)

PROOF: The coefficient [x^h y^m] of the product with exponent q is exactly
sum_k (-Z/2)^k C(h,k)C(m,k)C(q,k), since the three factor indices are forced equal. (1+6theta) multiplies the k-th term by (6k+1). Finite differentiation gives
(1+6theta)(1-Zxy/2)^q=(1-Zxy/2)^(q-1)(1-(6q+1)Zxy/2).
Alternatively the integer identity
C(q-1,k)+(6q+1)C(q-1,k-1)=(6k+1)C(q,k)
(with C(q-1,-1)=0) proves TORIC coefficientwise. No primality, infinite hypergeometric series or valuation inversion occurs. QED.

The toric representation is an exact finite *source-preserving* coefficient/WZ input, not a native original-class H0/B0 model or an infinite congruence proof.

## Bounded discovery, distinct negative controls

UNPROVED universal candidate:

  (6l+1) | U_l   for every integer l>=1.              (CONJECTURE C)

The accompanying PURE PYTHON STANDARD LIBRARY exact-integer checker actually executed for ALL 450 integers 1<=l<=450, with no modular division by nonunits. ALL 450 cases satisfy C; 259 of these moduli 6l+1 are COMPOSITE, including 25,49,121,169,2401. A second exact toric coefficient formula independently matched 36 lengths. The test has no coverage beyond 450 and does not prove C.

Integer witnesses (l, N=6l+1, U_l/N modulo N):
(2,13,11), (3,19,9), (4,25,24), (8,49,27), (20,121,74), (28,169,124), (50,301,280), (250,1501,579), (400,2401,196), (450,2701,2494).

**Sharp limit:** 448 of 450 tested lengths have U_l not divisible by (6l+1)^2. At l=2:
U_2=-23686=13*(-1822), and U_2 mod 169 =143 nonzero.

**Parameter controls** at l=1: replacing the denominator 2 by 3 produces scaled weighted sum -261=5 mod7; replacing weight 6k+1 by 4k+1 with denominator 2 produces -74=3 mod7. The original signed weight and argument are material; generic binomial-sum divisibility does not follow.

Actual stdout marker:
PASS_EXACT_TORIC_COMPOSITE_MODULUS_BOUND_20261031
and TESTED_L 450 COMPOSITE_MODULI 259, INDEPENDENT_TORIC_COEFFICIENT_CHECKS 36, SHARP_MOD_P2_NONZERO_CASES 448.
Executed code: research_notes/portable_direct/d25_toric_integer_port_guard_20261031.py.

## BRC / scientific next front / formal status

BRC COMPOSE_APPLIED: carrier (l,k,source=original216_lowparameter, three binomial indices, (-1)^k, 6k+1, 2^(2l-k), integer modulus N=6l+1). Toric readout retains variables (x,y,Z), coefficient port [x^h y^m], and signed theta. Permitted operations: integer exact recurrence, finite toric creative telescoping, CRT after prime-power validation, and the *separate* previously verified p-adic F0,F1,F2 and I_p reconstruction. The l=2 nonzero U_l/N modN witnesses that compressing to a Boolean first-digit divisibility readout erases information needed in the second digit.

Scientific next discriminating action: construct a symbolic integer-valued telescoping certificate U_l=(6l+1)V_l for EVERY l, or find the first counterexample; then derive the second-order JOINT source identity C01+F2+I_p for both frozen p mod24 classes, including the known p=19 and p=373 nonzero second-jet witnesses. Finite C is a research lead, not permission to skip the original second-digit proof.

Native independent benchmark remains EXACT same-original-class p373 H0/B0 divided-power [X]U modulo 139129, actual module rank, semilinear Frobenius direction/eta, signed odd Green/Hesse, kappa and independent replication: existing enterprise-math issue #1559, OPEN/PENDING_OWNER at observed read. No native algorithm, Source CLAIM, OPEN, checkpoint, Result or review was run. Current native gateway 0.6.11 Site read identity has research_authority_granted=false and control CODE_REVIEW_REQUIRED. Own research recovery issue awdawmip/kimi-query-bridge#6632 succeeded as a historical no-current-claim/no-run snapshot; own #6633 dispatch explicitly FAILED/UPSTREAM_CODE_REVIEW_REQUIRED, not NO_DISPATCH. No replay or maintenance identity borrowing. Neutral old staging remains independent. For future real Source work, honor current authentic session and receipt/continuation/ownership CAS. Research-Activity formal entry REGISTER_PENDING/SYNC_DEBT; author-side Git storage is not Source mathematical admission. User's recurring task schedule/notifications unchanged.
