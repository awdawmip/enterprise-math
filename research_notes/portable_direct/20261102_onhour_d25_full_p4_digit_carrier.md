# D25: Full two-digit p^4 carry transport and low-digit ordinary-source certificate (2026-11-02)

**AUTHOR-DERIVED / ALGEBRAIC PROOF / FINITE EXACT CHECK / UNREVIEWED / NOT_ADMITTED / NOT_SOURCE_CHECKPOINT / NOT_NATIVE_H0_B0.**

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific pin `c47e13e4aba0e006366f989d6333ae3`. This is a neutral author-side research record, not a session/CLAIM, official checkpoint or independently admitted theorem. Consumes prior author theorem `research_notes/portable_direct/20261102_onhour_d25_carry_boundary_first_lift.md` (blob `84bd78c59dd68f67600fb8318d9a0a8a30601ded`). The research logical lane is `chatgpt-research-onhour-enterprise-math-20260923`, distinct from the maintenance lane.

## Objective and added scientific content

Mother problem remains the original, signed `Delta_p-R_p=0 mod p` for every prime `p=13,19 mod 24`, or a genuine source-faithful counterexample/strict equivalent. The predecessor first-lift carry formula supplied p^2 precision for unit parts, enough for valuation-two/three anomalous terms modulo p^4 but insufficient for valuation-zero ordinary terms. The new theorem supplies a fully explicit **p^4 unit precision** carry formula, so both anomalous and ordinary pieces can be calculated with low-digit source/valuation records. It is **not** a proof of the mother conjecture or a universal W-2S supercongruence.

## Exact digit factorization, valid for every prime p >= 5

Let `k=ap+b`, `0<=a,b<p`. Write `u_p(n)=n/p^{v_p(n)}` (for n>0) and `F_p(n)=prod_{t=1}^n u_p(t)`. For any `n=qp+r`, `0<=r<p`, define
```
A_p(q)  = prod_(i=0..q-1) prod_(t=1..p-1) (1+p*i/t),
B_p(q,r)= prod_(t=1..r) (1+p*q/t).
F_p(qp+r) = F_p(q) * ((p-1)!)^q * r! * A_p(q)*B_p(q,r).
```
The last equality is an **exact rational identity**, obtained by separating multiples of p and the complete/remainder nonmultiple blocks.

For a source model with numerator factorial indices `J`, `d0=sum_(j in J)j`, denominator base `d`, let
```
C_J(n) = (prod_(j in J)(jn)!)/((n!)^d0*d^n);
v_J(n)=v_p(C_J(n)); U_J(n)=p^{-v_J(n)} C_J(n).
c_j=floor(j*b/p); r_j=jb-p*c_j; q_j=j*a+c_j;
delta_j=floor(q_j/p)-floor(j*a/p);
Gamma_j=F_p(j*a+c_j)/(F_p(j*a)*c_j!)
       =prod_(t=1..c_j)u_p(j*a+t)/c_j!.
```
All Gamma divisions are by p-units; the numerator is a p-free product. Direct substitution of the exact F_p factorization gives
```
v_J(ap+b) = v_J(a)+v_J(b)+sum_(j in J) delta_j;

U_J(ap+b)/(U_J(a)*U_J(b))
 = (prod_j Gamma_j)
   * (prod_j A_p(q_j)/A_p(c_j))/A_p(a)^d0
   * (prod_j B_p(q_j,r_j)/B_p(c_j,r_j))/B_p(a,b)^d0
   * d^{-a*(p-1)}.
```
For the original weighted 216 stream `J={2,3},d0=5,d=216,weight=6k+1`; for the original 2304 stream `J={4},d0=4,d=2304,weight=8k+1`. Reconstruct each original term by multiplying the *exact* weight and `p^{v_J(ap+b)}` after the p-free unit calculation. A vanishing weight mod p must never be divided out. The source, sign, p-adic valuation, low/high digits, carry flags and observer are retained.

## Closed p^4 harmonic expansion

Set `H_n^(t)=sum_(m=1..n)m^{-t}` in Z/p^4, `S1(q)=q(q-1)/2`, `S2(q)=q(q-1)(2q-1)/6`, and the Fermat quotient `q_p(d)=(d^{p-1}-1)/p` modulo p^3. Standard harmonic congruences for primes p>=5 give `H_(p-1)^(1)=0 modp^2` and `H_(p-1)^(2)=H_(p-1)^(3)=0 modp`. Therefore
```
log A_p(q)=p*H_(p-1)^(1)*S1(q)
            -(p^2/2)*H_(p-1)^(2)*S2(q)   (mod p^4).

E_j = p*H_(p-1)^(1)*[S1(q_j)-S1(c_j)-j*S1(a)]
      -(p^2/2)*H_(p-1)^(2)*[S2(q_j)-S2(c_j)-j*S2(a)];
D_j = sum_(t=1..3) (-1)^(t+1)*p^t/t
      *[(q_j^t-c_j^t)*H_(r_j)^(t)-j*a^t*H_b^(t)];
D_d = -a*sum_(t=1..3)(-1)^(t+1)*(p*q_p(d))^t/t;
L_J = D_d + sum_(j in J)(E_j+D_j);

U_J(ap+b) =
 U_J(a)*U_J(b)*(prod_j Gamma_j)
   *[1+L_J+L_J^2/2+L_J^3/6]    (mod p^4).
```
All denominators 2,3,6 are p-units, and p>=5. This is a **general algebraic identity** derived from the exact factorial split and p-adic log/exp truncated through p^3, not numerical fitting. The scope of p-adic logarithms is 1+pZ_p.

Each `E_j` is divisible by p^3. In the valuation-zero stratum the carry data satisfy `c_j=delta_j=0`; hence `E_j` depends on high digit a alone. Modulo p^4 the complete-block E contribution to a weighted full sum factors into
```
p^3 * [sum_a U_J(a)*e_J(a)]
    * [sum_b (lambda*b+1)*U_J(b)].
```
Thus **if the original one-digit weighted sum vanishes mod p**, the complete-block correction cancels in aggregate, even though its individual terms can be nonzero. This is a conditional factorization; it does not independently prove the antecedent for all primes.

## Executed exact verification and p=373 discriminator

An independent Python verifier implemented the digit/harmonic expression and compared against a separately coded direct original coefficient p-adic recurrence. Every original weighted term for p=5,7,13,19,37,43,61 matched: **15,086/15,086 source-index term comparisons**, no discrepancy. At p=373 the digit method independently rebuilt both full p^2 cutoffs, 139,129 index positions per source, using only low-digit factorial/harmonic state; source components matched the **previously executed, independent full-index recurrence certificate**:

```
p=373; p^2=139129; p^4=19356878641
W_(p^2)=139129 ; S_(p^2)=139129 (mod p^4)
W anomaly  =  2087908903 ; S anomaly  =  2782162613
W ordinary = 17269108867 ; S ordinary = 16574855157
signed anomaly (W-2S):         15880462318 = p^2*(4+306p)
signed ordinary+baseline:       3476416323 = p^2*(369+66p)
signed total mod p^4 = 0.
```
The BRC observer is the tuple (W/S source, high/low digit, carry, valuation, p-free unit, signed weight, modulus); no positive-mass substitution or native X6 identification was made. For p=373 at a=b=1, the per-term E corrections are **14,426,842,526** (W) and **9,496,806,411** (S) modulo p^4, so they cannot be discarded termwise. In all eight tested primes the aggregated E corrections vanish for both models.

The finite 373 identity and seven other examples do **not** establish the universal W/S relation. This unit closes the previous **ordinary-source precision bottleneck**, not the still-unproved finite summation identity or full mother objective. Verification source and detailed raw JSON are supplied in the same-turn author-side reproducible evidence archive: `d25_full_p4_digit_lift_20261102.py`, `d25_full_p4_digit_lift_20261102.check.json`. They are not native execution certificates.

## Immediate next mathematical and native acceptance steps

Sum over the high digit a in the **ordinary** strata, separately for classes 13 and 19 mod24, using the explicit L_J and Gamma data to search for/defeat an exact signed finite telescope (WZ / summation by parts) cancelling the anomaly. Then attach any resulting identity back to the **original** Delta-R readout and signed Clausen cutoff, not just a surrogate p^2 scalar congruence.

Native fixed-373 H0/B0 divided-power `[X]U mod139129`, original CM class, module rank, semilinear Frobenius direction and eta, signed odd Green/Hesse, kappa, and independent verification remain **PENDING_OWNER / NOT_EXECUTED** in Enterprise Math issue #1559. Ordinary scalar arithmetic here does not replace them.

The onhour original control dispatch `research-onhour-20261031-0205-dispatch-r15` has terminal FAILED / UPSTREAM_CODE_REVIEW_REQUIRED receipt in `awdawmip/kimi-query-bridge#6633`; no repeat was made. There is **no** authenticated Researcher session, CLAIM, run, formal Source checkpoint or Research Activity registration claimed for this record. The same real research lane is preserved; no maintenance identity or scheduler was touched. Status remains **AUTHOR-DERIVED / UNREVIEWED / NOT_ADMITTED**.
