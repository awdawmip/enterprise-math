# D25 — Exact invertible weighted Picard–Fuchs gauges for both original models (2026-11-02)

**AUTHOR-DERIVED / EXACT ALGEBRAIC PROOF / 26 FINITE EXACT CHECKS / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_EXECUTED.** Neutral GitHub research proof, not role-bound Source checkpoint/CLAIM/run/Result/review.

Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; immutable scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. This is a **constructive correction/continuation** of the preceding same-day weighted CM PF-forcing result, not a reproof of accepted CM0/SIMPLE/UR or old Clausen/Wilson reductions.

## 1. General exact finite weighted gauge

For p>3, theta=z*d/dz, let f_p(z)=sum(k=0..p-1)c_k z^k and

L f_p=[theta^3-z(theta^3+e2 theta^2+e1 theta+e0)]f_p = -p^3 c_p z^p.

Let Y=(1+w theta)f_p, X=(f_p,theta f_p,theta²f_p)^T and r=-p³c_p z^p/(1-z). An **exact rational-function equality** is

(Y,theta Y,theta²Y)^T = T_w(z) X + (0,0,w*r)^T,

T_w(z)=[[1,w,0],[0,1,w],
        [w*z*e0/(1-z), w*z*e1/(1-z),1+w*z*e2/(1-z)]].

The determinant is D_w=1+(w*z*e2-w²*z*e1+w³*z*e0)/(1-z). When D_w and 1-z are units, all three original unweighted jets are recoverable from weighted jets with the explicit endpoint source.

The homogeneous companion connection of X is A=[[0,1,0],[0,0,1],
[z*e0/(1-z),z*e1/(1-z),z*e2/(1-z)]].
The correct *weighted* scalar operator is obtained from the rational gauge
A_w=(theta T_w+T_w A)*T_w^-1, with theta³Y=(A_w)[last row]*[Y,theta Y,theta²Y] plus a **known p³ source**. This is a constructive weighted operator, avoiding the failure of applying the unchanged unweighted scalar PF operator directly to Y.

## 2. Original weighted-216 exact operator and CM endpoint

For a_k=(1/2)_k(1/3)_k(2/3)_k/(k!)³, F_p=sum a_k z^k, Y_p=(1+6theta)F_p, set (e0,e1,e2,w)=(1/9,13/18,3/2,6).

D_A(z)=(1+6z)/(1-z).
The last row of A_w, in order of columns 0,1,2, is

alpha_A0=z(6z+7)/[9(1-z)(1+6z)],
alpha_A1=z(78z+19)/[18(1-z)(1+6z)],
alpha_A2=z(18z+17)/[2(1-z)(1+6z)].

Thus L_A^w=theta³-alpha_A2 theta²-alpha_A1 theta-alpha_A0 satisfies the **exact** finite identity

**L_A^w Y_p = -p³ a_p z^p/(1-z) * [6p-(30z-1)/(1+6z)].**

At original z_A=1/2, D_A=8, alpha_A=(5/18,29/36,13/4), and
T_A=[[1,6,0],[0,1,6],[2/3,13/3,10]]. The weighted third-jet endpoint correction T_A X-(Y,thetaY,theta²Y)^T is (0,0,delta_A)^T, with

**delta_A=6p³ a_p 2^(1-p) = (2/3)p³ (mod p⁴).**

In particular, for all primes p>3,

**[theta³ - 13/4 theta² - 29/36 theta - 5/18] Y_p |_(z=1/2) = (7/18)p³ (mod p⁴).**

The bracket denotes operator application *before* evaluation. For the original D25 target primes p≡13,19 (mod24), the weighted scalar residual has **exact** p-valuation 3.

Modulo p³, the original unweighted 3-jet has the **explicit inverse** in terms of y_j=(theta^jY_p)(1/2):

f_0=(-y_0-15y_1+9y_2)/2,
f_1=(2y_0+5y_1-3y_2)/4,
f_2=(3y_2-2y_0-y_1)/24.

Modulo p⁴ use y_2+delta_A in all three inverses.

## 3. Original weighted-2304 exact operator and CM endpoint

For b_k=(1/4)_k(1/2)_k(3/4)_k/(k!)³, H_p=sum b_k z^k, Z_p=(1+8theta)H_p, set (e0,e1,e2,w)=(3/32,11/16,3/2,8).

D_B(z)=(1+15z)/(1-z). The last row of its correct weighted companion connection is

alpha_B0=9z(5z+3)/[32(1-z)(1+15z)],
alpha_B1=3z(55z+1)/[16(1-z)(1+15z)],
alpha_B2=5z(9z+7)/[2(1-z)(1+15z)].

Thus L_B^w=theta³-alpha_B2 theta²-alpha_B1 theta-alpha_B0 satisfies exactly

**L_B^w Z_p = -p³ b_p z^p/(1-z) * [8p-(105z-1)/(1+15z)].**

At original z_B=1/9, D_B=3 and alpha_B=(3/64,1/16,15/16). The weighted third-jet matrix there has rows
[1,8,0], [0,1,8], [3/32,11/16,5/2]. The finite correction to its third weighted jet is

**delta_B=8p³ b_p (1/9)^p/(1-1/9)=(3/32)p³ (mod p⁴).**

Consequently, for every prime p>3,

**[theta³ - 15/16 theta² - 1/16 theta - 3/64] Z_p |_(z=1/9) = (3/64)p³ (mod p⁴).**

The weighted scalar residual has exact p-valuation 3 for all p>3.

These first p³ digits use the already-proved Lucas/Fermat congruences a_p=1/9, b_p=3/32 (modp). The 216 first digit 7/18 vanishes modulo p only at p=7; this is outside the D25 target.

## 4. Exact finite independent checks (not universal proof)

Executed standalone Python standard-library original-binomial modular sums at p in
5,7,13,19,37,43,61,67,109,139,211,373,1171,
for both original weighted models. All **26/26** cases passed modulo p⁴, testing both the **new weighted scalar operator** and the **third-jet p³ correction**. For p=373:

- 216: weighted scalar PF defect digit **104** (=7/18 mod373); third-jet correction digit **125** (=2/3 mod373).
- 2304: weighted scalar PF defect digit **239** (=3/64 mod373); third-jet correction digit **105** (=3/32 mod373).

All-prime proof is the exact finite gauge derivation, not this finite regression. The full independent executable/check-result files are saved as author-side d25_weighted_gauged_pf_endpoint_20261102.py and d25_weighted_gauged_pf_endpoint_20261102.check.json in this run.

## 5. Research consequence and remaining exact obligations

**Positive new route:** Both original weighted models have invertible source-preserving jet gauges at the two true CM arguments, with determinant 8 and 3 respectively (units for p>3). Their *correct transformed* scalar operators are homogeneous mod p³, unlike the naive attempt to apply the unchanged unweighted operators to the weighted sums. The exact p⁴ endpoint carries separate known residues for the two models. None of this establishes a cross-model horizontal/Gauss–Manin or WZ transformation, a normalized same-class Frobenius, or W_p=S_p mod p³.

Next scientific unit: test a genuine finite **cross-model 3x3 jet transport** respecting these transformed connections, original weights, CM twist, normalization and original signed Clausen R=Q/p²; at p373 check the full weighted jets before claiming an all-target identity. The mother Delta_p-R_p=0 (modp) remains OPEN.

Native fixed p373 original H0/B0 divided-power [X]U mod139129, module rank, true semilinear Frobenius/eta, signed odd Green/Hesse, kappa and independent reproduction remain PENDING_OWNER/NOT_EXECUTED under the *existing* support awdawmip/enterprise-math#1559. Auxiliary gauged PF coefficients do not replace native evidence.

Old Research dispatch research-onhour-20261031-0205-dispatch-r15 ended FAILED / UPSTREAM_CODE_REVIEW_REQUIRED in awdawmip/kimi-query-bridge#6633. No retry, Source CLAIМ, session, run, Result, checkpoint or independent review is asserted. Only neutral author-side GitHub evidence is preserved (REGISTER_PENDING / SYNC_DEBT). Historical Research lane chatgpt-research-onhour-enterprise-math-20260923 is distinct from maintenance chatgpt-hourly-enterprise-math-20260921; no role identity is borrowed. Frozen scientific source pin, P000 and original task schedule/notifications unchanged.
