# D25: finite Clausen defect forced Picard–Fuchs equation and CM jet closure

Date: 2026-11-02. Status: AUTHOR-DERIVED / EXACT-PROVED / EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3.
Research logical ID: chatgpt-research-hourly-enterprise-math-20260923 (distinct from maintenance).

## New unit A: forced Picard–Fuchs equation

The preceding finite-Clausen proof at research_notes/portable_direct/20261102_hourly_r11_d25_clausen_truncation_defect_p3.md established coefficientwise integrality of the defect and the ordered high/low convolution formula. The predecessor arbitrary-Euler-observer proof at research_notes/portable_direct/20261102_hourly_r11_d25_clausen_all_euler_observers.md established all D_n as finite sums. We now relate these observers to the original CM base jet by an inhomogeneous differential equation. The original frozen R_p=D_0+6D_1 is prior research, not a new result.

For every prime p=6r+1 >= 7 work in Z_(p)[z]. Let theta=z d/dz,

    h_k=(1/6)_k(1/3)_k/(k!)^2,
    a_k=(1/2)_k(1/3)_k(2/3)_k/(k!)^3,
    G_p(z)=sum_{k=0}^{p-1}h_k z^k,
    F_p(z)=sum_{k=0}^{p-1}a_k z^k,
    E_p(z)=(G_p(z)^2-F_p(z))/p^2,
    P_r(z)=sum_{k=0}^r binom(r,k)binom(2r,k)z^k,
    L2=theta^2-z(theta+1/6)(theta+1/3),
    L3=theta^3-z(theta+1/2)(theta+1/3)(theta+2/3).

Earlier coefficientwise Clausen guarantees E_p is p-integral and G_p=P_r (mod p).

**Theorem (exact in F_p[z]):**

    L3 E_p(z) = -(1/3) z^p theta P_r(z).             (A)

**Proof.** For every polynomial f the symmetric-square identity is exactly

    L3(f^2) = 2 f theta(L2 f) + 6(theta f)(L2 f).    (B)

It follows either by expanding theta or by taking the symmetric square of the Gauss equation. The finite _2F1 and _3F2 recurrences give the *exact* boundary terms

    L2 G_p=-(p-5/6)(p-2/3)h_(p-1) z^p,
    L3 F_p=-(p-1/2)(p-2/3)(p-1/3)a_(p-1) z^p.

The p-valuations are v_p(h_(p-1))=2 and v_p(a_(p-1))=3. Wilson reflection, already established in the finite Clausen predecessor, gives

    h_(p-1)/p^2 = [18(r+1)(2r+1)]^-1 = 1/10 (mod p).

Thus (L2 G_p)/p^2 = -z^p/18 (mod p) and theta(L2 G_p)/p^2 = p(L2 G_p)/p^2 = 0 (mod p), while (L3 F_p)/p^2 =0 (mod p). Subtract L3 F_p from (B) with f=G_p, divide by p^2, and reduce G_p=P_r mod p: the one surviving source is 6(theta P_r)(-z^p/18), establishing (A). QED.

## New unit B: complete Euler-moment closure at a CM root

Set J_n=[theta^n P_r]_(z=1/2) (mod p) and D_n=[theta^n E_p]_(z=1/2) (mod p). Put Q(T)=(T+1/2)(T+1/3)(T+2/3).

For every n>=0, applying theta^n to (A) and using theta^n(zQ(theta)E)=z(theta+1)^nQ(theta)E, and 2^(-p)=1/2 (mod p), gives

    D_(n+3) - (1/2)[(T+1)^n Q(T)]_(T=theta) E_p |_(z=1/2)
              = -(1/6)J_(n+1) (mod p).             (C)

The coefficient of D_(n+3) in the left side is 1/2. Consequently (C) reconstructs every higher defect moment from earlier moments and J_(n+1). The terminating polynomial P_r is the mod-p Gauss solution (parameters -r,-2r), so L2 P_r=0 over F_p, and its J_n are determined by J_0,J_1. All finite Euler-polynomial observers therefore factor through D_0,D_1,D_2,J_0,J_1, with the boundary forcing (A) retained as provenance.

Expanding n=0,1 gives

    18D_3-27D_2-13D_1-2D_0+6J_1=0,                (D)
    18D_4-45D_3-40D_2-15D_1-2D_0+6J_2=0.        (E)

Since L2P_r(1/2)=0, J_2=J_1/2+J_0/18. Eliminate J_1:

    36D_4-108D_3-53D_2-17D_1-2D_0=-(2/3)J_0.   (F)

For the task's p mod24 in {13,19}, previously accepted CM0 gives J_0=0; this specializes to the new homogeneous relation

    36D_4-108D_3-53D_2-17D_1-2D_0=0.           (G)

Applying theta to L2P_r and using J_0=0 gives J_3=47 J_1/36. The n=2 instance of (C) and (D) then give

    648D_5-2268D_4-3906D_3-711D_2-D_1+22D_0=0. (H)

The full recurrences prove that D_0,D_1,D_2,D_3 **recover all D_n modulo p under the CM root**, for every finite Euler-polynomial operator at the declared point. Individual ordered coefficient branches remain preserved in the predecessor artifact when a future operation needs their provenance; the four-digit jet is sufficient only for the declared Euler readout interface. No X6-native embedding or native H0/B0 experiment is implied.

## Exact author-side verification

Companion Python checker computes D_0..D_8 from original G_p^2-F_p modulo p^3 and J_n independently from binomial polynomial P_r. All 207 primes 7<=p<=3000 with p=1 (mod 6) passed (C) for n=0..5 and (D)-(H) in their applicable domains. The checker separately compares every coefficient in (A) for every such prime p<=103. Selected exact certificates:

    p=13:  (D0,D1,D2,D3,D4,D5)=(6,12,12,12,12,12); (J0,J1,J2)=(0,7,10)
    p=19:  (D0,D1,D2,D3,D4,D5)=(18,18,0,2,6,14); (J0,J1,J2)=(0,1,10)
    p=373: (D0,D1,D2,D3,D4,D5)=(132,135,181,37,117,219); (J0,J1,J2)=(0,294,147)

BRC resolution COMPOSE_APPLIED: source carrier = ordered Clausen convolution, valuation tiers, original cutoff and CM polynomial; observer = finite Euler operators at z=1/2 mod p; repair coordinate = explicit forced source in (A). The CM four-port compression is proved for this observer and precision, not for all future source-sensitive operations.

Mother target remains Delta_p-R_p=0 mod p (p mod24 in {13,19}), or original signed S_p=p mod p^3. The next discriminating scientific unit is to test a source-preserving relation between the CM derivative J_1 (now tied to D_3 by (D)) and the independently defined Cauchy carry kernels K_0,K_1. Prior finite K_0=0 and K_1=-1/2 patterns retain conjectural status. Reuse existing R, CM0, Cauchy decomposition; do not recredit them.

Control/recovery at 2026-11-02: authenticated gateway version 0.6.11 says CODE_REVIEW_REQUIRED/UPSTREAM_CODE_REVIEW_REQUIRED, research_authority_granted=false, executor_binding_configured=false, native quota active_jobs=5/5. Same Research lane historical #6637 was a read-only recovery with no authorized run; #6638 terminal FAILED and unreplayed. No native CLAIM, OPEN, Source checkpoint, Result, independent review or admission for this author-side mathematical contribution. Issues enterprise-math#1558 (control) and #1559 (native p=373 benchmark) remain the support paths; registration pending.
