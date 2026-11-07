# D25 — Third-digit Clausen/Euler cutoff-overflow theorem for 216 and 2304

2026-11-07 · TASK_RESEARCH author-side. **PROVED POLYNOMIAL ALGEBRA / FINITE EXACT CHECKED / UNREVIEWED / NOT_ADMITTED.**

Parent task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; scientific input pin c47e13e4aba0e006366f989d6334d443f6333ae3. Logical lane chatgpt-research-onhour-enterprise-math-20260923; maintenance lane excluded. Previous same-lane author frontier 3918433058fe75f0e46bf1f18d58998d5bf79a71. Independently consumed, without adopting other actor's identity, the p² Clausen/Euler result of the hourly20 lane at 6cb6a01eccee001775e3aacadcb34961048157e5. This note advances the fold to p³ while retaining the true finite-index projection.

## Definitions

For prime p>3 set D=z d/dz and Π_p(f)=sum of coefficients of degree <p. Work in Z_(p)[z]/(p³,z^p). Define U(z)=3F2(1/2,1/3,2/3;1,1;z), B(z)=3F2(1/4,1/2,3/4;1,1;z), W_p=[(1+6D)Π_p U](1/2), V_p=[(1+8D)Π_p B](1/9). These equal the frozen 216 and 2304 integer-binomial weighted sums.

For p=6m+1, put f_n=(1/6)_n(1/3)_n/(n!)², Q_A=Σ_(0≤n≤2m)f_n z^n, R_A=Σ_(2m+1≤n<p)(f_n/p²)z^n, P_A=Π_p(Q_A R_A).

For p=8k+3 or p=8k+5, select (a,b)=(1/8,3/8) or (5/8,7/8), respectively. Put g_n=(a)_n(b)_n/(n!)², Q_B=Σ_(0≤n≤3k+1)g_n z^n, R_B=Σ_(3k+2≤n<p)(g_n/p²)z^n, C(z)=1 (8k+3) or 1-z (8k+5), P_B=Π_p(C Q_B R_B). All normalized tail coefficients are in Z_(p): by these indices two numerator p-factors have occurred while n! is a p-unit.

## Theorem 1 — unconditional polynomial fold through the third p-adic digit

For p=6m+1>3, coefficientwise modulo (p³,z^p):

    Π_p U = Q_A² + 2p² P_A.

For p=8k+3 or 8k+5>3, coefficientwise modulo (p³,z^p):

    Π_p B = C Q_B² + 2p² P_B.

**Proof.** Clausen supplies U=[2F1(1/6,1/3;1;z)]² and B=[2F1(1/8,3/8;1;z)]². Euler supplies the equivalent B=(1-z)[2F1(5/8,7/8;1;z)]². In the A Gauss stream the first numerator p-factor appears at coefficient index m+1 and the second by 2m+1. In both B representations the second p-factor appears by coefficient index 3k+2. Therefore, through degree p-1, the Gauss series is Q+p²R, and its square modulo p³ is Q²+2p²QR. The low-square degrees are 4m<p, 6k+2<p, and in the Euler case 6k+3<p. Only the tail cross-product requires Π_p. No degree ≥p source can affect a coefficient of degree <p. QED.

## Theorem 2 — weighted short-jet versus Frobenius-overflow ports

Let α=1/2 and β=1/9. Differentiating the exact coefficientwise theorem yields:

    W_p ≡ Q_A(α)² + 12Q_A(α) DQ_A(α)
             + 2p²[P_A(α)+6DP_A(α)]                 (mod p³).

For p=8k+3:

    V_p ≡ Q_B(β)² + 16Q_B(β) DQ_B(β)
             + 2p²[P_B(β)+8DP_B(β)]                 (mod p³).

For p=8k+5:

    V_p ≡ (128/9) Q_B(β) DQ_B(β)
             + 2p²[P_B(β)+8DP_B(β)]                 (mod p³).

The last formula uses (1-9β)=0 in the exact derivative of (1-z)Q_B². Define G_A and G_B as the displayed Gauss terms excluding 2p² and E_A=2(P_A+6DP_A) mod p, E_B=2(P_B+8DP_B) mod p. Thus

    W_p-V_p ≡ (G_A-G_B)+p²(E_A-E_B)                (mod p³).

If G_A-G_B is divisible by p², the target equality W_p=V_p (mod p³) is *equivalent* to the explicit finite-field condition

    (G_A-G_B)/p² + E_A-E_B = 0                    (mod p).

For target classes p≡13,19 (mod24), Guo–Zudilin's established weighted 2304 theorem supplies V_p≡p (mod p³). The displayed finite-field condition is the new exact reduction for the still-open W_p≡p (mod p³); the general cancellation remains unproved.

**Cutoff warning intrinsic to the formula:** Π_p(QR) is not Q(α)R(α). For A set H_A=(1-Π_p)(Q_A R_A). At a CM root Q_A(α)=0 mod p, P_A(α)=-H_A(α) mod p and DP_A(α)=DQ_A(α)R_A(α)-DH_A(α) mod p. This makes the higher-degree Frobenius overflow a concrete nonzero readout, not a dispensable term. On B retain C=1 or 1-z as a separate Euler source flag.

## Exact executed checks and examples

The companion stdlib checker independently builds the original 3F2 coefficients and Gauss coefficients with modular ratio recurrences; a separate integer-binomial path checks raw W and V at five primes. The full p³ coefficient vectors were checked for A at p=7,13,19,31,37,43,67,73,97,139,373 and B at p=13,19,37,43,67,139,373. For all 94 primes <2500 with p≡13,19 mod24, both projected formulas, the finite CM-root values and W_p=V_p=p mod p³ were checked exactly. Finite checks do not establish a universal supercongruence.

|p|E_A|E_B|(E_A-E_B) mod p|(G_A-G_B)/p² mod p|
|--:|--:|--:|--:|--:|
|13|9|0|9|4|
|19|13|8|5|14|
|43|31|33|41|2|
|67|30|46|51|16|
|373|1|220|154|219|

The last two columns sum to zero mod p. At p=373, original separate normalized Gauss registers are (Q_A,DQ_A,P_A,DP_A)=(41330265,50195277,307,353) and (Q_B,DQ_B,P_B,DP_B)=(22533676,20823512,118,372), with Q and DQ computed mod 373³ and P/DP mod 373. The nonzero overflow readouts (E_A,E_B)=(1,220) are needed for the observed cancellation.

**BRC use:** COMPOSE_APPLIED with separate original 216/2304 coefficient ports, Gauss index and factor valuations, Euler flag, Q,DQ,R,P,DP, Π_p and the signed cancellation readout. The projection and original origin of each coefficient must survive interpretation.

## Continuation and Source

Hard next unit: use the established Fricke common maps and Hasse p-th boundary to prove the source-preserving finite-field cancellation for both target classes or derive a verified obstruction to a candidate mechanism. Do not duplicate the earlier p² square fold, full-series 301-prime scans, or original-class p373 H0/B0 experiment. Native same-original-class divided-power [X]U, Frobenius, Hesse κ and independent check still require execution at issue #1559; the finite modular program is not that native benchmark.

Native source request onhour11-20261106-1400-exact-research-lane-continuation was previously QUEUED/EVENT_COLLECTION_IO/Error. On 2026-11-07 12:08 UTC em_status and em_control_result returned BACKEND_IDENTITY_OR_VERSION_MISMATCH, operation_sent=false. Sites gateway phase CONFIGURED_NOT_LIVE_VERIFIED, research_authority_granted=false. No original operation was resent. Source session/claim/run/checkpoint, Result, independent review and admission remain unverified; material here is GitHub author-side evidence only.
