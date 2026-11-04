# D25 — A forced Green operator for the complete third-digit Sun defect
2026-11-04 · TASK_RESEARCH author-side portable result · UNREVIEWED / NOT_ADMITTED
Research conversation: `chatgpt-research-onhour-enterprise-math-20260923` (maintenance lane excluded).
Frozen scientific pin: `c47e13e4aba0e006366f989d6334d443f6333ae3`.
Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`.

## Theorem: inhomogeneous symmetric-square differential equation

For any prime p>=5 and d=3,4, let C=(d-1)/d², c_k=(1/d)_k(1-1/d)_k/(k!)², F(X)=sum_{k=0}^{p-1}c_k X^k and H(t)=sum_{k=0}^{p-1}binom(2k,k)c_k t^k. All rational expressions are interpreted in Z_(p). Write u=X(1-X), v=1-2X, and the Sun defect E=(F²-H(u))/p² mod p. The prior all-coefficient proof established E=C X^p Q with Q(0)=0 and degree Q<=J<=p-2.

Define the third-order Green operator (D=d/dX)
```
T_C = u² D³ + 3uv D² + (v²-(2+4C)u)D - 2Cv.
```
Then in F_p[X] the complete polynomial Q satisfies
```
                      T_C Q = 2F - 6(1-X)F'.             (A)
```
This determines the complete defect from the original low-valuation period using an inhomogeneous differential equation, prior to the D25 signed two-model observer.

**Proof.** The exact contiguous recurrence (k+1)² c_(k+1)=[k(k+1)+C]c_k gives
```
(u D²+vD-C) F = S = -p² c_p X^(p-1).                   (1)
```
Here c_p is p-integral and c_p=C (mod p). Direct calculation of the symmetric square yields
```
T_C(F²)=6u S F' +2(uS'+vS)F.                           (2)
```
Classical Clausen supplies the differential equation for the untruncated H. Its truncated version obeys exactly
```
[θ³-4t(θ+1/2)(θ+1/d)(θ+1-1/d)] H = -p³ h_p t^p,
θ=t d/dt, h_p=binom(2p,p)c_p.
```
Under t=u(X), the same differential expression is transformed by T_C H(u)=(v/u)L_3 H(u), so
```
T_C H(u) = -p³ h_p v u^(p-1).                          (3)
```
The coefficientwise p² division defining E is valid by the previously established Sun congruence. Combining (1)–(3) gives T_C E=C X^p[2F-6(1-X)F'] mod p. In characteristic p, D(X^p)=0; as E=C X^p Q, cancel C X^p and obtain (A). This holds polynomially with every source preserved. QED.

## Explicit finite three-term transport

For j>=0,
```
T_C(X^j) = j³X^(j-1) - (2j+1)[j(j+1)+2C]X^j
                    + (j+1)[j(j+2)+4C]X^(j+1).
```
Writing Q=sum_{j>=1}q_jX^j with q_0=q_(-1)=0, 0<=n<J, and f_n=(2-6C/(n+1))c_n modulo p, we derive
```
(n+1)³ q_(n+1) = f_n +(2n+1)[n(n+1)+2C]q_n
                     -n[n²-1+4C]q_(n-1)    (mod p).   (B)
```
Every divisor n+1 is a p-unit in the declared range. The coefficient at X^(j-1) of T_C(X^j) equals j³, so this is the unique solution with q_0=0 and degree <=p-2. In particular q_1=2-6C, as in the earlier first-boundary result.

(B) computes the full defect in O(J) finite-field operations after F's coefficients are generated. It replaces a p³ full polynomial convolution and explicit rational z² coefficient calculation on the **defect construction path**, retaining original d=3/d=4 labels and the derivative-before-Frobenius operation. This is a finite, exact Green recurrence; the cross-model weighted equality is the open mother dependency.

## Independent exact verification and interpretation

The accompanying Python standard-library checker independently constructs both complete original polynomials F² and H(X(1-X)) modulo p³, divides by p² coefficientwise, builds Q, and verifies T_C Q directly. A second path generates Q solely by (B), and compares all coefficients. All 70 model-prime instances (each p from 5 to 151 plus p=373, both d=3 and 4) passed.

(p,d,deg Q,deg RHS) include (13,3,3,3), (13,4,5,3), (19,3,5,5), (19,4,9,4), (139,3,45,45), (139,4,69,34), (373,3,123,123), (373,4,185,93). These finite checks independently support the all-prime algebraic proof.

**Exact next scientific action:** compute T_C's Lagrange adjoint and the finite Green boundary form, then pair the two original CM evaluation-and-derivative observers (x_3=(2+s)/4, x_4=(3+2s)/6, s²=2) with the forced periods, testing a candidate signed cross-model intertwiner first at 13,19,139,373. Preserve the odd Green/Hesse observer and native original coefficient provenance.

The frozen parent is Δ_p-R_p=0 mod p for p≡13,19 mod24. Native original-class p=373 H0/B0 [X]U modulo 139129, rank, semilinear Frobenius and independent replication remain NOT_EXECUTED, issue #1559 (PENDING_OWNER); no surrogate benchmark is claimed. Service 0.6.11 observed research_authority_granted=false, control.state=CODE_UPGRADE_AVAILABLE; no native CLAIM/run/checkpoint/Result in this lane. Original failed continuation request `onhour-d25-20261104-1702-continuation-read` retained without reissue.

Source input: frozen D25 pin, earlier `20261104_onhour_d25_sun_global_support_and_full_boundary_jet.md`, Zhi-Hong Sun (2015) truncated-square congruence, classical Clausen equation. Status: EXACT ALGEBRAIC THEOREM / FINITE EXACT CHECKED / AUTHOR-SIDE PUBLISHED / UNREVIEWED / NOT_ADMITTED.
