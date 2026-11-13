# PREFIX-609-R2 — Paired controlled positive BRC probes recover all gates with one fixed phase sensor

Date: 2026-11-09 (Asia/Shanghai). Status: AUTHOR-SIDE EXACT PROOF AND EXECUTED CERTIFICATES; independent Driver review pending.
Frozen scientific input: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Continuity: PREFIX-602 exact 16-dimensional two-step image; PREFIX-604 12+4 invariant split; PREFIX-607 known-input four phase sensors; PREFIX-608 unknown-input first-gate gauge (PR #1836, immutable commit 6fb57c9ed6d130dc056eb25b439a3ad6f0be42a6).

## 1. Exact setup and mother-objective relation

Use the frozen native X6-BRC STAR source with 48 phases, 96 original bit ports and 576 tagged branch actions. Fix six axis weights (1,1,1,1,0,0), unknown nonnegative gate word q_1,...,q_n, and the known two-step transient D=Q(0)Q(1). The unknown native-derived nonnegative phase-sum source v is common to two controlled experiments. In the first prepare source v; in the second prepare v+u, where u=ones(48) is a known, nonnegative phase-sum increment. Apply the *same* unknown gate word independently to both experiments. At each t>=1 read only raw phase index 3 in each output. Original tagged 96-port history remains a separate native source carrier; any nonnegative phase-sum preparation can be implemented by assigning its mass to one designated port per phase.

Write
  a_t=Q(q_t)...Q(q_1)D v,
  b_t=Q(q_t)...Q(q_1)D(v+u).
Their exact contrast d_t=b_t-a_t=Q(q_t)...Q(q_1)Du is known-input propagation, independent of v. Linearity here is the exact phase-sum observer theorem, not an identification of the full original tagged histories.

## 2. Theorem 609.1 — fixed single-phase differential sensor is sufficient

For arbitrary n>=1, arbitrary v>=0 and arbitrary real q_t>=0 common to the two probes, the n contrasts
  s_t=b_t[3]-a_t[3] (t=1,...,n)
uniquely determine the full ordered gate word. This requires two raw scalar readings per step (one per probe) and one fixed zero-based phase sensor 3, or n scalar contrast values if subtraction is performed by the sensor.

The exact PREFIX-602/604 native-derived coordinates for the known increment Du are:
  c_0=(9/2, 4, 3/2, 3/4)^T, f_0=(I-P)KDu,
  B(q)=[[0,0,0,4(q+3)],[1,0,0,0],[0,1,0,0],[0,0,1,0]]
and the exact original phase-3 reconstruction row obeys
  (EW)[3,:]=(2,0,0,0),
  (E T^t f_0)[3]=12*2^t for all nonnegative integer t.
The latter follows from its four initial exact values and T^4=16I on the 12D complement. Thus with c_t=B(q_t)c_(t-1),
  s_t=12*2^t + 2 c_(t,0)
     =12*2^t + 8(q_t+3)c_(t-1,3).
Therefore the sequential decoder is
  q_t=(s_t-12*2^t)/(8c_(t-1,3))-3;
  c_t=B(q_t)c_(t-1).
Every initial c_0 component is strictly positive; q_t+3>=3 implies all four c_t components stay strictly positive at every step, so this decoder always has a nonzero denominator. By induction all n gates are recovered uniquely. The algorithm uses O(n) four-coordinate exact updates after one known input increment calibration; integer/rational bit length grows with exact products and must be included in concrete resource comparisons.

## 3. Sharp n-contrast smooth-observation rank

For strictly positive gate words, the map q=(q_1,...,q_n) -> (s_1,...,s_n) is differentiable and lower triangular in its time dependence, with
  partial s_t / partial q_t = 8 c_(t-1,3) > 0.
Hence its n by n Jacobian has nonzero determinant and exact rank n. Any differentiable scheme whose k real scalar observations can be differentiably decoded to *all* n free positive gates requires k>=n (chain-rule rank of decoder composed with encoder). The constructed n differential scalars attain this bound within that precise observation class. This lower bound counts contrasts, not physical raw readings, experimental runs or exact bit cost: our implementation reads 2n raw scalars from two synchronized probes.

## 4. An exact witness separating the PREFIX-608 blind gauge

The preceding unknown-source blind witness has v=ones(48) with first gate 1; alternate v' differs only by v'[28]=2501/2500 and v'[32]=2499/2500, with first gate 7503/7499. The first full 48-phase outputs of the single uncalibrated probe coincide exactly. Repeat each with the *same known increment u=ones(48)* and its corresponding gate. The controlled first-step phase-3 contrasts differ by
  s'_1-s_1=24/7499.
Thus the two-probe measurement distinguishes the explicitly verified strictly positive unknown-source gauge pair. The general theorem covers all v>=0, not just this witness.

## 5. Executed exact verification and scope

The standalone Python/SymPy checker constructs the original 48 STAR phase basis and the frozen native-derived Q(q), then reconstructs E,K,T,H,W,L and the four-cycle algebra. It checks the gate-sensitive phase-3 row and gate-free complement at eight exact times. Across 3 unknown nonnegative source vectors and 3 independent nonnegative integer/rational/zero gate words, it decodes 114 gates exactly; compares 5472 native-derived phase contrast coordinates; checks 228 nonnegative complete phase states; and checks the rational blind-witness controlled contrast 24/7499. All executed assertions passed on 2026-11-09. The universal result follows from the exact matrix identities and induction, with finite tests verifying the implementation.

BRC source/operation: original STAR Q(q), fixed weights, tagged branch provenance retained; 48-phase linear readout only. Observer/future scope: full nonnegative gate words with identical controls on paired inputs and the known D transient; fixed phase-3 sensor per run. The two experimental trajectories need the same unknown gate word and an exactly controlled additive native phase-sum increment. These are conditions of the theorem, not properties inferred of arbitrary physical preparations. The symbols q_t are operator gates, not calibrated heartbeat times.

## 6. Concrete next discriminating units

1. Replace the known two-step transient D by an unknown but shared transient: quantify the residual gauge of the differential initial tail and derive the minimum known calibration needed for one fixed sensor.
2. Test whether a single mixed source with a bounded scheduled positive input injection can replace two synchronized full runs without assuming unobserved state reset; specify exactly how additive control enters native ports.
3. Compare the 2n raw readings, exact rational bit lengths, native 96-port source preparation and differential measurement cost against the PREFIX-607 known-state one-probe n-reading method, rather than counting contrasts alone.

Governance: continuation is an independent author-side scientific note, not an accepted Result, claim, review or Foundation change. Native researcher registration and current owner are separately recorded based on actual Source receipts; an unknown session outcome is not a usable prior role.
