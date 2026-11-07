# D25 — CM derivative Frobenius parity and one-port first-digit bridge

Date: 2026-11-07. **Author-side TASK_RESEARCH / PROVED conditional and unconditional statements as specified / FINITE EXACT CHECKED / UNREVIEWED / NOT_ADMITTED**. Mother task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, frozen science `c47e13e4aba0e006366f989d6334d443f6333ae3`. Logical Research lane `chatgpt-research-onhour-enterprise-math-20260923`; not the maintenance lane. This step consumes the prior uniform CM/Hasse-zero proof `c30aa207b5bb6d445c0291a9a31dbfca20743576` and the conditional first-digit fold `46ac1f6c7acc340241ae793feca4ec782ba31bb1`. No re-proof of Fricke 6:8, Clausen p³, or Hasse zero.

## Scientific unit 1 — discharge the B-model Frobenius unit unconditionally

Let p be a prime congruent to 13 or 19 modulo 24. In Z_(p), put
- A: m=(p-1)/6, Q_A(z)=sum_{i=0}^m binom(m,i)binom(2m,i)z^i; x_A=1/2; J_A=(z Q'_A)(x_A), and G_A(z) the p-term Gauss sum with parameters (1/6,1/3).
- B: p=8k+3 when p≡19 (mod24), or p=8k+5 when p≡13 (mod24); Q_B(w)=sum_{i=0}^k binom(k,i)binom(3k+1,i)w^i; x_B=1/9; J_B=(w Q'_B)(x_B). The p-term G_B has parameters (1/8,3/8) for the first class, (5/8,7/8) for the second class. Set ε=0 or 1, respectively; the second representation carries the Euler factor 1-w.
- Define g_A=G_A(x_A)/p mod p, g_B=G_B(x_B)/p mod p. These quotients exist because the previous uniform CM theorem proves Q_A(x_A)=Q_B(x_B)=0 modp and the finite Gauss sums reduce to Q.

The already established Clausen/Euler first-digit fold gives (in Fp)
  W_p/p=12 J_A g_A;
  V_p/p=c_B J_B g_B,
where c_B=16 for ε=0 and c_B=128/9 for ε=1. The same CM proof establishes J_A,J_B ≠0.

**New unconditional consumed consequence:** Guo–Zudilin, *A q-microscope for supercongruences*, Theorem 1.1 (arXiv:1803.01830), proves for all p>3
  V_p = p * (-3/p) (mod p³)
for precisely the original 2304^k weighted truncated sum. In both target classes p≡1 (mod3), hence (-3/p)=1. Combining the existing folded first digit and this published theorem gives
  **c_B J_B g_B = 1 (mod p), for every p≡13,19 (mod24)**.
This *discharges* the B-side first-digit unit. It is a rigorously sourced deduction from existing theorems, not a new proof of the Guo–Zudilin theorem, and it is not an assertion about the open A-side p³ target.

Primary source and exact denominator: https://arxiv.org/abs/1803.01830, equations (1),(2), Theorem 1.1. Here 2^(8k)*3^(2k)=2304^k, and the original coefficients are binom(4k,2k)binom(2k,k)^2(8k+1).

## Scientific unit 2 — exact Frobenius parity of two CM Hasse derivative ports

Work over Fp[s]/(s²-2), where s^p=-s for both target residue classes. Let
  x_+=(2+s)/4, y_+=(3+2s)/6,
so 4x_+(1-x_+)=1/2 and 4y_+(1-y_+)=1/9.
The prior CM/Hasse proof gives the exact polynomial maps
  R_A(t)=Q_A(4t(1-t)),
  R_B(t)=(1-2t)^ε Q_B(4t(1-t)) in Fp[t].
Both R_A(x_+) and R_B(y_+) vanish and J_A,J_B are nonzero.

Differentiate **before evaluation**. At each CM fiber,
  P_A := R'_A(x_+) = -2s Q'_A(1/2),
  P_B := R'_B(y_+) = 4(-2s/3)^(ε+1) Q'_B(1/9).
Thus P_A,P_B are nonzero and have exact Frobenius types
  P_A^p=-P_A; P_B^p=(-1)^(ε+1) P_B.
In particular B's Euler branch reverses its derivative parity: B is anti-invariant for p≡19 and invariant for p≡13. The two-model derivative ratio T=P_A/P_B is therefore
  **T=(3/4) Q'_A(1/2)/Q'_B(1/9) = (1/6) J_A/J_B in Fp**, p≡19;
  **T=-(9s/16) Q'_A(1/2)/Q'_B(1/9) = -(s/8) J_A/J_B in s Fp**, p≡13.
Consequently T^p=T when ε=0 and T^p=-T when ε=1. These are identities for every target prime, not experimental extrapolations.

## Scientific unit 3 — one Frobenius-eigenspace residual replaces two alleged open units

Set λ_A=12 J_Ag_A and λ_B=c_B J_Bg_B=1 (the latter was proved above). Define a source-typed paired residual
  C_p = T*g_A-(2/9)*g_B                                (ε=0),
  C_p = T*g_A+(4s/27)*g_B                               (ε=1).
An elementary substitution of the two exact expressions for T yields
  **C_p=(λ_A-λ_B)/(72 J_B)**                           (ε=0),
  **C_p=-s(λ_A-λ_B)/(96 J_B)**                         (ε=1).
The denominators are units for p>3. Hence the still-open first-digit A assertion is **exactly equivalent** to the single signed CM derivative-port condition
  **W_p≡p (mod p²) iff C_p=0**.
Furthermore C_p^p=C_p in the p≡19 branch; C_p^p=-C_p in the p≡13 branch. This pins the observer/eigenspace any proposed Cartier/Fricke/Frobenius transport must preserve; taking a norm or erasing the odd signed component is not an adequate proof operation.

The B side is now a proved input, not a second independent proof obligation. The A p² bridge C_p=0 remains open universally. The harder A p³ mother objective remains open and still needs the previously preserved signed four-port/T02/Hasse-tail correction.

## Finite independent integer checks and discrimination

A Python standard-library checker `d25_cm_frobenius_derivative_bridge_check_20261107.py` computes both original p-term Gauss streams modulo p², J_A/J_B, and the independent polynomial derivative values of R_A,R_B over Fp[s]/(s²-2), using dual-number Horner evaluation. It verifies the Frobenius eigencharacter, each T formula, proved B first-digit unit and the **conjectural** A bridge on all 77 target primes p≤2000. All checks PASS (the A observations are finite evidence only). Selected entries (P_A,P_B,T,C_p, with (a,b) meaning a+b*s):

| p | ε | P_A | P_B | T | C_p |
|---:|---:|---|---|---|---|
| 13 | 1 | (0,11) | (7,0) | (0,9) | (0,0) |
| 19 | 0 | (0,15) | (0,3) | (5,0) | (0,0) |
| 43 | 0 | (0,6) | (0,1) | (6,0) | (0,0) |
| 67 | 0 | (0,41) | (0,31) | (64,0) | (0,0) |
| 373 | 1 | (0,316) | (193,0) | (0,106) | (0,0) |

BRC/Enterprise-coordinate application: **COMPOSE_APPLIED**. Retain the two different Gauss coefficient streams, their p-adic lifts, Euler ε, CM conjugate fiber ±s, first derivative, semilinear Frobenius eigencharacter and *signed* scalar residual C_p before projecting. Fp versus sFp is a typed observer coordinate, not an extra native X6 axis. This precise source and operation declaration is required to compare later with the original-class native H0/B0 evaluator; the portable CM derivative is not that evaluator.

## Native and handoff

Native same-original-class p373 H0/B0 divided-power [X]U mod p², Frobenius direction/η, Hesse κ and independent replication remain pending at https://github.com/awdawmip/enterprise-math/issues/1559, with no executor assigned at this read. The distinct original Source request `onhour11-20261106-1400-exact-research-lane-continuation` is retained. Current Site diagnostic 2026-11-07 15:56 UTC reports `CONFIGURED_NOT_LIVE_VERIFIED` and `research_authority_granted=false`; `em_status` and `em_control_result` fail before upstream operation with `BACKEND_IDENTITY_OR_VERSION_MISMATCH / UPSTREAM_STATUS_TOOL_ERROR / STATUS_DATABASE_UNAVAILABLE / operation_sent=false`. Do not resubmit the old request or borrow the maintenance lane. This note is author-side only.

**Next exact action:** seek a Source-permitted identity-preserving Fricke/Cartier differential pullback relation proving C_p=0 for all p≡13,19 mod24. It must explicitly retain ε=1 anti-invariant odd branch and the native benchmark as distinct. Once C_p=0 is established, B's proved unit gives W_p≡p modp²; only then attack p³ four-port cancellation using prior exact formulas. No pending original mutation was repeated in this author-side publication.
