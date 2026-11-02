# D25 — exact ordered-pair / quotient-square observer bridge (author-side)
Date: 2026-11-02. Lane provenance: `chatgpt-research-onhour-enterprise-math-20260923` (historical logical lane, not a newly authenticated service identity). This is not the maintenance lane. State: AUTHOR_DERIVED / ALGEBRAICALLY_PROVED / EXACT_FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT.

Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; original frozen science pin `c47e13e4aba0e006366f989d6334d443f6333ae3` unchanged. Parent goal: prove/disprove `Delta_p-R_p=0 mod p` for every prime p=13 or 19 (mod24); separately execute authentic native p373 H0/B0. Consume, do not recredit, preceding onhour CM quotient repair at `20261102_onhour_d25_cm_quotient_root_deformation_repair.md`, D24 and other-lane research.

## Theorem A: an exact rational joint-observer / quotient-square identity

Let m>=1, beta_r=binom(m,r)binom(2m,r)/2^r (0<=r<=m), Y(t)=sum beta_r*t^r, epsilon=Y(1), J=sum r*beta_r, C=sum beta_r*H_r and Q(t)=(Y(t)-epsilon)/(1-t). Define the original *ordered-pair* observation

```
Xi=sum_{i,j=0}^m beta_i beta_j (1+6(i+j)) (H_{i+j}-H_i-H_j)
I=integral_0^1 (5+t) Q(t)^2 dt.
```

Then, **exactly over the rational numbers**,

```
                       Xi = I - 12 J C.                  (A)
```

This identity is for all positive integers m, with no CM hypothesis. In particular, for p=6m+1 prime >=7, all harmonic and integral denominators through 2m+1 are p-units, so (A) remains true mod p^2.

**Independent proof from ordered-pair source.** The exact finite-harmonic kernel is

```
H_{i+j}-H_i-H_j = -integral_0^1 (1-t^i)(1-t^j)/(1-t) dt.
```

Set D(t)=epsilon-Y(t), K(t)=J-tY'(t). Summing the *original signed ordered pairs*, without erasing their indexes or their factor (1+6(i+j)), gives

```
Xi=-integral_0^1 [D(t)^2+12D(t)K(t)]/(1-t) dt.
```

Use D=-(1-t)Q, Y'=-Q+(1-t)Q', K=J+tQ-t(1-t)Q'. Thus

```
Xi=integral_0^1 [(-1+13t)Q^2+12JQ-12t(1-t)QQ']dt.
```

Integrating -6t(1-t)(Q^2)' by parts produces +(6-12t)Q^2, while integral Q=-sum beta_r H_r=-C (finite coefficientwise integration). Therefore Xi=integral(5+t)Q^2 -12JC, proving (A).

For positive m, beta_i>0, and every pair i,j>=1 has H_{i+j}-H_i-H_j<0. Consequently Xi<0 in the rationals and I>0, hence 0<I<12JC *as rational inequalities*. This does NOT assert Xi(mod p) nonzero for all primes and does not transfer a rational order to a residue field.

## Theorem B: exact same-source second digit of the *original deformed* Gauss port

For p=6m+1 prime >=7 set Z(t)=sum beta_r H_r t^r and Ctheta=sum r beta_r H_r. The original frozen deformed polynomial has coefficients

```
P(t/2)=sum_{r=0}^m beta_r t^r / prod_{a=1}^r (1-p/(2a)).
```

Let L(F)=sum_k (1+6k)H_k[t^k]F, Hcal1=L(P(t/2)^2), and Tdef=L(YZ). The prior correctly sourced expansion P(t/2)=Y+(p/2)Z (mod p^2), combined with (A) and the previously proved ordinary quotient-square formula, yields the **new joint-source synthesis**

```
Hcal1 = Xi + 12JC + 2epsilon(C+6Ctheta) + p*Tdef   (mod p^2).  (B)
```

This keeps original ordered-pair, CM-root, and parameter-deformation sources separate. To apply (B) inside a numerator subsequently divided by p, `Xi` must be computed **mod p^2**, not merely mod p; use epsilon mod p^3 when epsilon/p must be known mod p^2.

By substitution into the *existing* original-source D25 reduction (predecessor note), on target CM classes:

```
Delta_p-R_p =
  [12J A -(3/2)*(Xi+12JC+2epsilon(C+6Ctheta)+p*Tdef)+A1+B1-1]/p
  + A^2+6A*Ctheta+(3/2)J*D2+Hcal2/8+A2+B2+C2   (mod p),
A=epsilon/p+C/2.
```

Divisibility of the numerator is inherited from the pre-existing CM0/D24 source and its reduction; the new expression does not prove unconditional cancellation. A local equality for this scalar observer is **not** evidence that arbitrary future ordered-pair, Frobenius or native H0/B0 observations can discard pair provenance.

## Executed integer certificates

The independent program `d25_joint_quotient_exact_bridge_20261102.py` computes Xi by all original (i,j), computes I by a separate quotient polynomial convolution, and computes Hcal1 from an independently generated deformed Gauss coefficient recurrence in Z/p^2 Z. It verified equations (A) and (B) for all 107 primes <=3000 in classes 13,19 (mod24), plus controls p=7,31, without floats or division by p.

| p | Xi mod p^2 | I mod p^2 | 12JC mod p^2 | original Hcal1 mod p^2 | root repair | p*Tdef |
|---:|---:|---:|---:|---:|---:|---:|
| 13 | 41 | 59 | 18 | 163 | 26 | 78 |
| 19 | 188 | 183 | 356 | 354 | 304 | 228 |
| 373 | 20055 | 52939 | 32884 | 83152 | 96607 | 72735 |

At p=373, 20055+32884=52939; 52939+96607+72735=222281=83152 (mod139129). Thus the joint rank-one correction has value 12JC=60 (mod373), Xi=286 (mod373), and I=346 (mod373). Omitting 12JC is a concrete precision/error witness. These check the previous I=52939 and Hcal1=83152 using independent routes. Finite verification is not a universal proof of the original D25 cancellation.

**Exact next science action:** seek a terminating contiguous/WZ certificate for the *original parent signed combination* expressed with Xi lifted mod p^2, the 12JC factor, CM-root and parameter repairs, and A2+B2+C2 (or a valid prime counterexample). Test p13,p19,p373 and nonCM p7. Do not rederive this bridge or confuse a scalar check with native H0/B0.

Native original p373 divided-power [X]U mod139129, module rank, semilinear Frobenius, eta, signed Green/Hesse/kappa and independent replay remain NOT_EXECUTED, owner PENDING under issue #1559. Current gateway read: 0.6.11, research authority=false and write relay=false; own checkpoint ACCESS_DENIED; exact live Source continuation CONTROL_QUOTA; old request research-onhour-20261031-0205-dispatch-r15 CONTROL_REQUEST_NOT_FOUND in client and historically FAILED / UPSTREAM_CODE_REVIEW_REQUIRED in bridge issue #6633. That request was not resent. No own authenticated session/claim/run, Source checkpoint or Result is claimed. Old staging retains independent provenance. Scheduler and notification settings untouched.
