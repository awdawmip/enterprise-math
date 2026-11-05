# D25 — exact 0/1/2-jet inhomogeneous terminating boundary for the original 216 bottom band

2026-11-06. TASK_RESEARCH author derivation and 80-prime exact integer verification; UNREVIEWED / NOT_ADMITTED. Source task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; immutable publication TP2-B6F4FC938FF94941C1B7; scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. Research lane chatgpt-research-onhour-enterprise-math-20260923, not maintenance.

## 1. Input, differentiable finite carrier, and exact telescoping

This directly continues the preceding author note 20261106_onhour_d25_bottom_216_parametric_two_jet_certificate.md, which reconstructs the previously unresolved bottom compensation D_p from original 216 parameter jets and original 2304 boundary.

For any integer m>=1, use rational polynomials
c_n(t) = (-3m+t/2)_n (-2m+t/3)_n (-4m+2t/3)_n / [2^n(n!)^3],
0<=n<=2m+1.

Let C_n=c_n(0); let L_n and S_n denote the exact two jets from the preceding note:
L_n=sum_{r<n}{1/[2(3m-r)]+1/[3(2m-r)]+2/[3(4m-r)]},
S_n=sum_{r<n}{1/[2(3m-r)]^2+1/[3(2m-r)]^2+4/[3(4m-r)]^2},
0<=n<=2m. Then
c_n'(0)=-C_n L_n, c_n''(0)=C_n(L_n^2-S_n).

Define
M(n,t)=(n-3m+t/2)(n-2m+t/3)(n-4m+2t/3)-2n^3.
The original hypergeometric ratio gives the **exact finite rational identity** for every t:
M(n,t)c_n(t) = 2(n+1)^3 c_{n+1}(t)-2n^3 c_n(t).
Summing from 0 through 2m gives
sum_{n=0}^{2m} M(n,t)c_n(t)=2(2m+1)^3 c_{2m+1}(t).   (1)

The right endpoint is zero at t=0 but has **nonzero derivatives**. Indeed, with C=C_{2m},
c_{2m+1}(t)=c_{2m}(t)*[(-m+t/2)(t/3)(-2m+2t/3)]/[2(2m+1)^3].
Its first derivative equals m^2 C/[3(2m+1)^3], and its second derivative equals
C[-10m/9-(4m^2/3)L_{2m}]/[2(2m+1)^3].

## 2. Three exact coupled boundary identities

Write M_i(n)=(d/dt)^i M(n,t) evaluated at t=0. Direct expansion gives:
M_0(n)=(n-3m)(n-2m)(n-4m)-2n^3
      = -n^3-9mn^2+26m^2n-24m^3.
M_1(n)=(3/2)n^2-(26/3)mn+12m^2.
M_2(n)=(13/9)n-4m.

Evaluate (1) and its first and second derivatives at t=0. This proves, **in Q, for every m>=1**:

(0) sum_{n=0}^{2m} M_0(n) C_n = 0.

(1) sum_{n=0}^{2m} [M_1(n)C_n - M_0(n)C_n L_n] = (2m^2/3) C_{2m}.

(2) sum_{n=0}^{2m} [M_2(n)C_n - 2M_1(n)C_n L_n
                      + M_0(n)C_n(L_n^2-S_n)]
    = C_{2m}[-10m/9-(4m^2/3)L_{2m}].

These are an exact **triangular 0/1/2-jet boundary system**, not just modulo-p observations. The first and second nonzero endpoint terms originate from the formerly terminating (-2m)_n factor, whose parameter derivative survives at n=2m+1. Dropping the endpoint when differentiating a terminating hypergeometric series produces false equations.

For p=6m+1>3 all denominators in these 0/1/2 jet sums are p-units, so the same equations may be read modulo p^r for any r>=1 after p-local reduction. In particular they are compatible with the p^3 digits required in the original third-digit D25 proof.

## 3. Actual exact checks

The companion verifier d25_216_bottom_jet_boundary_20261106.py independently checks all three identities with Python Fraction at p=13 (m=2) and p=19 (m=3), and with exact integer modular arithmetic modulo p^3 for all 80 primes p<=997 and p=1 mod6. All checks passed, failures 0.

Exact rational boundary values:
* p=13: first = 175, second = -25315/36.
* p=19: first = 14553/2, second = -2360771/80.

Modulo p^3, signed first/second boundary pairs:
* p=13 (mod 2197): (175, 1921).
* p=19 (mod 6859): (3847, 5557).
* p=67 (mod 300763): (235668, 56922).
* p=373 (mod 51895117): (49110461, 34631550).

The zero-jet cubic identity is exact; the two nonzero jet boundaries are rigorously determined, not fitted to modular outputs.

## 4. Direct role in the frozen residual problem and next action

Previous work proved: (i) one-seed complementary middle/upper-shell reduction; (ii) a 3D rational Gosper residual quotient for the middle shell; (iii) the original bottom D_p equals (A0-V_h)/p - A1+(p/2)A2 modulo p^2. The new three moment equations explicitly constrain the bottom triple (C_n, C_n L_n, C_n(L_n^2-S_n)) and its **nonzero derivative boundary**.

BRC composition = COMPOSE_APPLIED: population n=0..2m and three named parameter factors per n; carry the label (original 216, m, n, factor 1/2 vs 1/3 vs 2/3, derivative order 0/1/2, signed weight, n=2m+1 endpoint, original 2304 subtraction V_h). Permissible compression preserves the three differentiated channels and both nonzero endpoint corrections. This is ordinary external hypergeometric arithmetic, not a native X6 slice or original-class H0/B0 divided-power computation.

Next precise unit: compute the **common finite adjoint / polynomial reduction** for the original bottom weighted functional (1+6theta)F_m(1;p) against these three exact endpoint equations, and compare its residual three moments plus original V_h with the previously proved middle-shell cubic residual/boundary. The differentiations now fix the formerly unspecified bottom endpoint contributions. A valid all-prime cancellation remains the still-open mother target Delta_p-R_p=0 modulo p for all p=13,19 mod24.

Independent obligation: original p=373 native fixed H0/B0 divided-power [X]U mod139129, rank, semilinear Frobenius/eta/kappa, odd Green/Hesse and independent replication. Actual assigned native executor remains pending under GitHub issue #1559; no native run or Source Result is implied by this author's portable work.

Source-control read d25-onhour-20261106-0701-recovery-read was queued/running at last observation; retain its original request ID for receipt and reconciliation. This note is NOT canonical Source checkpoint, CLAiM, run, freeze, review or admission.
