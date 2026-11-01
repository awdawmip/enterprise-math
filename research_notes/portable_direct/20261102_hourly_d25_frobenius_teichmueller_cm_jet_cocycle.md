# D25 — Frobenius/Teichmüller coordinate cocycle for the original 216↔2304 CM jets

Date: 2026-11-02 (UTC+08). **AUTHOR-DERIVED / EXACT ALGEBRA / EXACT-CHECKED ON 107 TARGET PRIMES / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.** This is portable classical arithmetic, **not** the original native H0/B0 experiment or a Source-authorized Task checkpoint.

Frozen Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Logical research lane `chatgpt-research-hourly-enterprise-math-20260923`, not maintenance `chatgpt-hourly-enterprise-math-20260921`. The frozen mother objective remains `Delta_p-R_p=0 (mod p)`, equivalently under the existing signed source-port reduction to the full original weighted 216 sum `W_p=p (mod p^3)` on p≡13,19 (mod 24).

## Question and input

Previous author-derived exact weighted-projective-jet identity (Enterprise Math `research_notes/portable_direct/20261102_hourly_d25_projective_jet_first_lift.md`) resolved the mod-p projective slope but exposed a nonzero first p-adic defect `D_p/p`. Another lane independently observed original 216/2304 fourth-digit correlation but a weighted first-jet mismatch (at p=373 the mismatch is 138), see `research_notes/portable_direct/20261102_onhour_d25_two_stream_fourth_digit_finite_certificate.md`. Neither datum proves a normalized non-scalar transport. The smallest new question is: which first-digit CM ports survive a change of the p-adic representative of the same mod-p observation point, and what exact correction must a proposed two-stream transport retain?

For prime p>3 let Z_(p) be rationals with p-unit denominators, `theta=z d/dz`, and let P in Z_(p)[z]. For a p-unit z define

`q_p(z)=(z^(p-1)-1)/p in Z_(p)`, `omega_p(z)=z^p (mod p^2)`.

This rational Fermat quotient is defined at the **actual observation point**, not a fitted constant.

## Theorem 1 — exact Frobenius jet transport and gauge-invariant first digit

For every nonnegative integer j, as polynomial evaluations in Z_(p)/p^2,

`theta^j P(omega_p(z)) = theta^j P(z) + p*q_p(z)*theta^(j+1) P(z) (mod p^2).`   (1)

Indeed `omega_p(z)=z[1+p q_p(z)]`; coefficientwise `(1+pq)^k=1+kpq (mod p^2)`. Also `omega_p(z)^p=omega_p(z) (mod p^2)` and `omega_p(z')=omega_p(z) (mod p^2)` for any z'=z (mod p); thus omega is the canonical mod-p^2 Teichmüller representative of the nonzero residue.

Suppose `P(z)=theta P(z)=0 (mod p)`. Put `f_j=(theta^jP)(z)`, with the quotient `f_j/p` interpreted in Z_(p)/p only when divisibility has been established. Then

`f_0(omega)/p = f_0/p (mod p)`,
`f_1(omega)/p = f_1/p + q_p(z)*f_2 (mod p)`.   (2)

The two coordinates `(f_0/p, f_1/p)` are therefore **not** both functions of the reduced point. The repaired coordinates

`V_0=f_0/p,  V_1=f_1/p+q_p(z)f_2,  V_2=f_2 (mod p)`   (3)

**are** invariant under replacing z by any z'=z(1+pt). Proof: `f_1(z')/p=f_1(z)/p+t f_2` and `q_p(z')=q_p(z)-t (mod p)`; `f_0/p` and `f_2 mod p` are unchanged. Equation (3) is thus a precisely scoped p-adic coordinate-gauge invariant; it does not assert a global analytic connection or a cross-model isomorphism.

For a weighted polynomial `Y=(1+c theta)P` with `P(z)=theta P(z)=0 (mod p)`, equation (1) also yields

`[Y(omega)-Y(z)]/p = q_p(z)*(theta Y)(z)=c*q_p(z)*f_2 (mod p)`.   (4)

A weighted total is **not** invariant under Teichmüller substitution unless the explicit right side vanishes. The zero of the unweighted double jet does not erase this weighted first-digit carry.

## Theorem 2 — source-preserving CM first-lift decomposition

Use the exact ORIGINAL truncated hypergeometrics

`F_A(z)=sum_(0<=k<p) (1/2)_k(1/3)_k(2/3)_k z^k/(k!)^3`,
`F_B(z)=sum_(0<=k<p) (1/4)_k(1/2)_k(3/4)_k z^k/(k!)^3`.

At z_A=1/2, z_B=1/9 set `f_j=(theta^jF_A)(z_A)`, `g_j=(theta^jF_B)(z_B)`; `Y_A=(1+6theta)F_A`, `Y_B=(1+8theta)F_B`; `a_j=(theta^jY_A)(z_A)`, `b_j=(theta^jY_B)(z_B)`. Let

`D_p=16 b_2 a_1-3 b_1 a_2`, `Q_A=q_p(1/2)`, `Q_B=q_p(1/9)`;
`U_A=f_1/p+Q_A f_2`, `U_B=g_1/p+Q_B g_2` (mod p).

Assume the **explicit CM double-zero hypotheses**
`f_0=f_1=g_0=g_1=0 (mod p)` and p>3. Then

`D_p/p = 6a_1 U_B+(3/2)a_1(g_0/p)-8b_1 U_A-2b_1(f_0/p)`
`          + a_1 b_1 [(4/3)Q_A-(3/4)Q_B] (mod p).`   (5)

All denominators 2,3,4 are p-units. In terms of integer Fermat quotients `q_p(n)=(n^(p-1)-1)/p`,
`Q_A=-q_p(2)`, `Q_B=-2q_p(3)` (mod p), so the **mandatory coordinate correction** is

`a_1 b_1 [-4 q_p(2)/3 +3 q_p(3)/2] (mod p).`   (6)

Proof: the preceding source's exact finite Picard–Fuchs endpoint identity gives

`D_p/p=6a_1(g_1/p)+(3/2)a_1(g_0/p)-8b_1(f_1/p)-2b_1(f_0/p) (mod p).`

Insert `g_1/p=U_B-Q_Bg_2`, `f_1/p=U_A-Q_Af_2`, then `a_1=6f_2`, `b_1=8g_2 (mod p)`. The difference is `8 b_1 Q_A f_2-6 a_1 Q_B g_2 = a_1 b_1[(4/3)Q_A-(3/4)Q_B]`. This is exact algebra; no missing matrix is smuggled in by changing coordinates.

## Consequence and sharp finite discriminator

For the **original** weighted sums `W_p=Y_A(1/2)` and `T_p=Y_B(1/9)`,

`[Y_A((1/2)^p)-W_p]/p=-q_p(2)a_1 (mod p)`,
`[Y_B((1/9)^p)-T_p]/p=-2q_p(3)b_1 (mod p)`.  (7)

Thus even if `W_p-2T_p+p=0 (mod p^4)` for a given p≡1 (mod3), applying independent Frobenius lifts to the two arguments changes that bridge by

`p*{[-q_p(2)a_1]+[4q_p(3)b_1]} (mod p^2)`.  (8)

**At p=373:** `Q_A=169,Q_B=144`; `a_1=292,b_1=77`; the two weighted shifts are respectively `112,271` (each divided by p, mod p); the signed bridge shift is `112-2*271=316 !=0 (mod 373)`. The previously observed original fourth-digit scalar relation therefore cannot simply be reused after changing to these canonical Teichmüller CM coordinates. This is a precise counterexample to the *uncompensated coordinate-substitution bridge*, **not** to the original frozen mother conjecture.

The original projective first-lift defect at p=373 remains `D_p/p=365`; the canonical slopes `U_A=81,U_B=34`, and the explicit source correction in (5) equals `18 (mod 373)`. The correction is not a free fitted parameter.

## Exact finite computation / limits

A standard-library-only modular recurrence checker was executed on **all 107 primes p<=3000 with p mod 24 in {13,19}**, checking (1) on four Euler jets, (2), (4), (5), (7), the original double-zero hypotheses and the exact modular arithmetic. Six representative primes (13,19,37,61,373,1171) also received independent original-binomial-summand checks. All tests PASS. In this finite domain only, the signed coordinate shift (8) was nonzero at all 107 primes; there is **no** universal nonvanishing claim.

```text
p,D/p,Q_A,Q_B,U_A,U_B,cocycle,weighted_shift_A,weighted_shift_B,bridge_shift
13,7,10,10,3,4,12,4,5,7
19,15,16,2,10,18,12,2,10,1
37,19,36,1,26,23,14,7,35,11
61,41,25,35,25,34,52,27,27,34
373,365,169,144,81,34,18,112,271,316
1171,950,873,614,311,229,617,694,660,545
```

Full ordered-row SHA256 of the actual 107-prime exact run:
`c1e090c983f697affec35d8c3c6b0afe00fbe43ded5193a5291e6eeda5a0c751`.
Companion portable checker and stdout are in the run's delivered evidence bundle, `d25_frobenius_cm_jet_20261102.py` and `d25_frobenius_cm_jet_20261102.runlog.txt`. No float, network, native H0/B0 execution, or Lean checker was used.

## BRC, dependencies and next action

**BRC: COMPOSE_APPLIED** to the original indexed signed, weighted A/B hypergeometric streams with p-adic precision horizon p^2 and future operations `Euler-jet -> rational representative change -> first-digit projective defect -> proposed cross-stream transport`. Carrier includes original index/weight, `(f_0/p,f_1/p,f_2)`, both rational observation points and their Fermat quotients; collapse to the first two unnormalized digits is not observer-safe. The exact repair coordinate is `q_p(z) f_2`; (1)–(3) certify fiber constancy of the repaired observer under z'=z (mod p), at the **stated horizon only**. This is an external finite-ring arithmetic model, not a claim of native P000 X6 or physical time dynamics.

**Do not repeat:** completed original full-sum/half-tail valuation results, 2019 published 2304 comparison, prior exact signed Clausen bridge, existing projective-jet first-lift identity, or the onhour lane's p^4 finite fourth-digit certificate. This turn proves a new coordinate-invariance law and its nontrivial correction, *not* the D25 mother congruence.

**Next exact science:** use the canonical jet ports `(f_0/p,U_A,f_2)`, `(g_0/p,U_B,g_2)` and the correction (5) to test (and if possible prove) a non-scalar signed cross-stream connection. Retain `p=373: 228:114` fourth-digit scalar readout, `theta Y_A-2 theta Y_B=138` original first-jet mismatch, `D/p=365`, and coordinate-substitution bridge shift `316` as separate observables. Any proposed connection must match *all* or specify which observer it preserves. Then prove the original `Delta_p-R_p=0 (mod p)`, including the original signed Clausen cutoff; finite correlations are not a general theorem.

**Control:** previously read own recovery Issue #6637 SUCCEEDED read-only (no winning claim, no Source authority), continuation #6638 terminal FAILED `UPSTREAM_CODE_REVIEW_REQUIRED`; fresh authenticated Gateway 0.6.11 still `research_authority_granted=false`, `executor_binding_configured=false`, control `CODE_REVIEW_REQUIRED`, and 5/5 new-job quota. Support owner remains Enterprise Math #1558; native fixed p=373 H0/B0 issue #1559 remains NOT_EXECUTED. No new session/CLAIM/OPEN, canonical checkpoint/Result/review or false identity was created. Actual project artifact publication is neutral author evidence, not native admission. Source pins and scheduler unchanged.
