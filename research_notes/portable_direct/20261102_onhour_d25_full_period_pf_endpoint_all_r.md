# D25 — Full-period Picard–Fuchs truncation defect at every prime-power length (2026-11-02)

**Status:** AUTHOR-DERIVED / EXACT ALGEBRAIC PROOF / FINITE CHECK 12 CASES / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_EXPERIMENT. This research note is neutral evidence, NOT a formal Source checkpoint, execution, CLAIM, Result or review. Frozen scientific pin: c47e13e4aba0e006366f989d6334d443f6333ae3; publication TP2-B6F4FC938FF94941C1B7; Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Declared Research logical lane: chatgpt-research-onhour-enterprise-math-20260923, distinct from maintenance; no issued Source identity asserted.

## All-prime/all-r exact theorem

Let p>3 be prime, r>=1, N=p^r. Set theta=z*d/dz and, in the p-local rational polynomial ring,

a_k = C(2k,k)^2*C(3k,k)/108^k
    = (1/2)_k*(1/3)_k*(2/3)_k/(k!)^3,

b_k = C(4k,2k)*C(2k,k)^2/256^k
    = (1/4)_k*(1/2)_k*(3/4)_k/(k!)^3,

F_N(z) = SUM_{k=0}^{N-1} a_k*z^k,
H_N(z) = SUM_{k=0}^{N-1} b_k*z^k.

Here C(n,k) means the integer binomial coefficient, and (x)_k is the rising factorial. Define the independent differential operators

L_A = theta^3 - z*(theta+1/2)*(theta+1/3)*(theta+2/3),

L_B = theta^3 - z*(theta+1/4)*(theta+1/2)*(theta+3/4).

**Exactly over rational polynomials**, without limiting processes,

(1) L_A F_N(z) = -N^3*a_N*z^N;
    L_B H_N(z) = -N^3*b_N*z^N.

For **every p>3 and every r>=1**, the omitted coefficients satisfy

(2) a_N = 1/9 (mod p);  b_N = 3/32 (mod p),

and are p-adic units. Hence **the highest polynomial coefficients of both operator residuals have valuation exactly 3r**, so the full truncated series satisfy their respective homogeneous Picard–Fuchs equations modulo p^(3r), but no stronger:

(3) L_A F_N(z) = -(p^(3r)/9)*z^N (mod p^(3r+1));
    L_B H_N(z) = -(3*p^(3r)/32)*z^N (mod p^(3r+1)).

At the actual unweighted arguments of the two original weighted models,

W_p = [1+6*theta] F_p(z) evaluated at z=1/2,
S_p = [1+8*theta] H_p(z) evaluated at z=1/9,

these **different operator defects** obey for each r:

(4) [L_A F_N]_(z=1/2) = -p^(3r)/18 (mod p^(3r+1));
    [L_B H_N]_(z=1/9) = -p^(3r)/96 (mod p^(3r+1)).

Their leading digits have ratio 16/3 (mod p). This is a typed differential-operator defect ratio, NOT a proven p-adic period-transfer factor or native Frobenius gauge.

## Proof

The exact adjacent ratios imply

n^3*a_n = (n-1/2)*(n-2/3)*(n-1/3)*a_(n-1),
n^3*b_n = (n-3/4)*(n-1/2)*(n-1/4)*b_(n-1).

After applying L_A or L_B, all internal polynomial coefficients cancel, while the only missing n=N term leaves precisely the two expressions (1).

Because N=p^r, the integer Lucas congruences give C(2N,N)=2, C(3N,N)=3, C(4N,2N)=6 (mod p). Fermat gives 108^N=108 and 256^N=256 (mod p). Hence a_N=(2^2*3)/108=1/9 and b_N=(6*2^2)/256=3/32 (mod p). Both denominators are p-units for p>3, proving (2) and the sharp 3r valuation in (3). The same coefficient recurrence shows v_p(a_(N-1))=v_p(b_(N-1))=3r because all three factors (N-alpha) are units. Finally, (1/2)^N=1/2 and (1/9)^N=1/9 (mod p) yields (4). QED.

The source-typed full-period cutoff in (1) is **not the prior reflected 216 sub-tail C_m**. The latter has a distinct, nonzero mod-p endpoint forcing term; both facts coexist without cancellation-by-relabeling. Project BRC is applied as provenance/observer discipline; the classical polynomial ring is not native X6 space.

## Executed independent exact check

A standalone integer program calculated a_(N-1), a_N, b_(N-1), b_N independently using the two original binomial formulas, checked their term-recurrence boundary modulo p^(3r+1), and evaluated both actual operator defects. **12 of 12 tests PASSED:** (p,r)=(5,1),(5,2),(7,1),(7,2),(13,1),(13,2),(19,1),(19,2),(37,1),(37,2),(373,1),(1171,1).

At p=373, p^3=51895117 and p^4=19356878641, the defects modulo p^4 are 7524791965=145*p^3 and 12299142729=237*p^3; the modular digit ratio is 254. For p=1171 the leading digits are 65 and 1110. Numeric checks support but do not replace the algebraic all-prime proof.

The local author-side reproducible files were generated with names d25_full_period_picard_fuchs_defect_20261102.md, .py, .check.json, .continuation.json, and a bundled .zip. This plain-text note preserves the proof even when the original local bundle is unavailable.

## Mother target and exact unfinished work

The frozen D25 goal remains Delta_p-R_p=0 (mod p) for all p congruent to 13 or 19 (mod 24), equivalent under accepted UR and the original signed Clausen source cutoff to W_p=p (mod p^3). The present theorem **does not prove** W_p-S_p=0 or D25 LIFT. It says a full-period *unweighted* differential-equation transport modulo p^3 does not require a truncation-source correction; it does **not** identify either weighted solution or original Q, Hesse/Green signs, twisted Frobenius or normalized Gauss–Manin map. At p^4 the two distinct defects must be restored.

The next useful mathematical obligation is an explicit finite, weighted, source-preserving 216-to-2304 horizontal/Gauss–Manin or WZ transport at their CM points through p^2, yielding W_p-S_p=0 (mod p^3) or directly Delta_p-R_p=0. Do not repeat accepted D24 CM0/SIMPLE/UR, the original R=Q/p^2 identification, Wilson three-band reductions, second-digit gauge redundancy, or zero-fiber fourth-digit counterexamples. No universal congruence claim is made from finite checks.

**Native benchmark:** same-original-class fixed p=373 H0/B0 divided-power [X]U (mod 139129), module rank, true semilinear Frobenius eta, odd signed Hesse/Green, kappa and independent replica remain PENDING_OWNER / NOT_EXECUTED under awdawmip/enterprise-math#1559 (open/unassigned on readback). Ordinary Hesse candidate norm 122102 is not a native coefficient without rank-one and normalization evidence.

**Control:** Gateway 0.6.11 reported research_authority_granted=false, executor_binding_configured=false, UPSTREAM_CODE_REVIEW_REQUIRED, 5/5 active jobs. Prior research dispatch request research-onhour-20261031-0205-dispatch-r15 has a FAILED upstream-code-review receipt in awdawmip/kimi-query-bridge#6633; do not reissue it. No current own Source session, claim, run or role-bound checkpoint is asserted. This Git note is only neutral author-side persistence. Frozen scientific pin and original scheduling/notifications remain unchanged.
