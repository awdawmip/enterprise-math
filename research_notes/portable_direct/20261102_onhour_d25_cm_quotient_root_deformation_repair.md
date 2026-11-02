# D25 — CM quotient-square harmonic transport and necessary second-digit repairs

Date: 2026-11-02. Lane: chatgpt-research-onhour-enterprise-math-20260923 (different from maintenance and from the distinct hourly Research lane).

State: AUTHOR_DERIVED / ALGEBRAICALLY_PROVED / FINITE_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT. This author-side work is not a Source checkpoint/Result or a native H0/B0 execution.

Frozen D25: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7; immutable scientific input c47e13e4aba0e006366f989d6334d443f6333ae3. Consume rather than recredit predecessor ordinary Gauss second jet, Clausen/three-root bands and accepted D24.

## Theorem A: ordinary Gauss quotient-square first harmonic identity

For p=6m+1 prime >=7 in p-local rational arithmetic, put beta_r=binom(m,r)binom(2m,r)2^{-r},
Y(t)=sum_{r=0}^m beta_r t^r, epsilon=Y(1), J=sum r beta_r,
C=sum beta_r H_r, Ctheta=sum r beta_r H_r, and

Q(t)=(Y(t)-epsilon)/(1-t)=-sum_{j=0}^{m-1}(sum_{r=j+1}^m beta_r)t^j.

Q is an *exact polynomial*, Q(1)=-J, with no division by a CM zero. Set L(F)=sum_k(1+6k)H_k[t^k]F and I(F)=sum_k[t^k]F/(k+1). As degrees <=2m<p, all modular denominators are p-units. The following is an exact equality in rational arithmetic:

$$
\boxed{L(Y^2)=I((5+t)Q(t)^2)+2\epsilon(C+6C_\theta).}\tag{A}
$$

Proof: Write Y=epsilon+(1-t)Q; L(epsilon^2)=0 and L((1-t)Q)=L(Y)=C+6Ctheta. For F=(1-t)^2 Q^2 and G=(1+6t d/dt)F, G(1)=0. The finite harmonic integral H_k=int_0^1(1-t^k)/(1-t)dt implies L(F)=-int_0^1 G(t)/(1-t)dt. Differentiation gives G/(1-t)=(1-13t)Q^2+12t(1-t)QQ'. Integration by parts with vanishing t(1-t) boundary yields int_0^1(5+t)Q^2dt. QED.

## Theorem B: repair from ordinary to *original deformed* Clausen port

The frozen original Clausen source uses the terminating P(z)={}_2F_1(-m,-2m;1-p/2;z), not merely ordinary Y(t)=P0(t/2). Its coefficient expansion is P(t/2)=Y(t)+(p/2)Z(t) (mod p^2), where Z(t)=sum beta_r H_r t^r. Let Tdef=L(YZ) mod p and Hcal1_def=L(P(t/2)^2). Then

$$
\boxed{\mathcal H_{1}^{def}\equiv I((5+t)Q^2)+2\epsilon(C+6C_\theta)+pT_{def}\pmod{p^2}.}\tag{B}
$$

This follows by squaring the finite coefficient expansion, then applying Theorem A. Both the CM-root correction and parameter-deformation correction are required for the original divided second digit. An independent terminating-deformed-Gauss coefficient recurrence checks this correction.

## Theorem C: exact two-variable tail presentation for the second harmonic port

For any polynomial F of degree n<p, G=(1+6t d/dt)F=sum_{k=0}^n g_k t^k and T_j=sum_{k=j+1}^n g_k. Define polynomials

$$
K_{\square}(u,v)=\frac{G(1)-G(u)-G(v)+G(uv)}{(1-u)(1-v)},\quad
K_{\diamond}(u,v)=\frac{G(1)-G(uv)}{1-uv}.
$$

Their denominators divide exactly, and their square and diagonal coefficients preserve the original signed ordered-pair source. Expanding finite geometric series and integrating termwise proves:

$$
\boxed{\sum_k g_k(9H_k^2-5H_k^{(2)})
=9\iint K_{\square}-5\iint K_{\diamond}
=\sum_{j=0}^{n-1}T_j\left(\frac{18H_j}{j+1}+\frac4{(j+1)^2}\right).}\tag{C}
$$

Take F=Y^2. Since P=Y+O(p), it gives the original Hcal2 modulo p at precisely the D25 LIFT precision.

## Exact original LIFT re-expression and required precision

For target p≡13 or 19 (mod24), consume accepted CM0 (epsilon=0 mod p), D24 first-digit divisibility and the previously proven original-source identity:

$$
\Delta_p-R_p\equiv N/p+A^2+6AC_\theta+3JD_2/2+\mathcal H_2/8+A_2+B_2+C_2\pmod p,
$$
$$
A=\epsilon/p+C/2,\quad D_2=\sum_r\beta_r(H_r^2+H_r^{(2)}),\quad
N=12JA-3\mathcal H_1^{def}/2+A_1+B_1-1.
$$

The A_i,B_i,C2 here remain the previous *original* three-root source ports. Define Nflat=12JA-3I((5+t)Q^2)/2+A1+B1-1, c=epsilon/p mod p. Equations A/B show p|Nflat and yield a source-identical reduction:

$$
\boxed{\begin{aligned}
\Delta_p-R_p\equiv&
N_{\rm flat}/p-3c(C+6C_\theta)-3T_{\rm def}/2\\
&+A^2+6AC_\theta+3JD_2/2+
\mathcal H_2/8+A_2+B_2+C_2\pmod p .
\end{aligned}}\tag{D}
$$

Calculate epsilon to mod p^3 (not merely p^2) so that epsilon/p and A are known mod p^2 for Nflat/p. Compute Q,I,C and J at needed mod p^2; Tdef, D2 and Hcal2 at mod p. This is an exact reduction; universal all-prime cancellation remains an open obligation.

BRC use: original signed Cauchy pair population, p-adic units/valuations, Euler operation, and divided observer. Q alone loses two source coordinates: epsilon(C+6Ctheta) and Tdef, which repairs (B). The prior ordered-pair Xi is retained for further joint-observer operations. No assertion about native X6/H0/B0 follows from these algebraic ports.

## Executed exact evidence

A standard-library modular verifier, consuming unchanged d25_ordinary_second_jet_checker_20261102.py, checked Theorems A-C, an *independent* deformed Gauss recurrence, the signed mother formula (D), and the unchanged original source check for **all 107** target primes p<=3000. No mismatches. p=7 was separately used as a nonCM control of A-C; 13,19,37,373,1171 were independently crosschecked using the pre-existing original factorial W computation and exact ordered-pair Xi.

At p=373: ordinary H1=10417 (mod139129), quotient integral=52939, root correction=96607, deformed H1=83152 (mod139129), c=340 (mod373). The divided LIFT components are:

- Nflat/p = 361;
- root repair = 171;
- deformed repair = 267;
- ordinary second-jet quadratic = 194;
- Hcal2/8 = 366;
- original three-band sum = 133.

Their signed total 361+171+267+194+366+133=1492=4*373, while 361+171+267=799≡53 (mod373), exactly the old original N/p. At p13 the six components are (4,10,4,3,8,10), sum 39; at p19 (12,14,1,16,6,8), sum 57. The combined repair is nonzero on all 107 tested primes. Finite checks do not establish universal LIFT.

## Continuation / outstanding native evidence

Next smallest scientific unit: terminating contiguous/WZ identity involving Q-square integral, *both* root/deformation repairs, and Hcal2 pair-tail to cancel the original A2+B2+C2 and Wilson high-band C2 for both target classes; check 13,19,373 and nonCM control 7. Do not re-prove prior auxiliary Gauss lemmas.

Native fixed p373 H0/B0 divided-power [X]U mod139129, module rank, semilinear Frobenius, eta, odd signed Green/Hesse, kappa and independent replay remain pending under enterprise-math issue #1559 (OPEN/unassigned on 2026-11-02). This algebra is not that benchmark.

Control read 2026-11-02: private Sites gateway 0.6.11 reports research_authority_granted=false and write_relay_enabled=false; own checkpoint ACCESS_DENIED; original request research-onhour-20261031-0205-dispatch-r15 returned CONTROL_REQUEST_NOT_FOUND in current scope, historical bridge issue #6633 records terminal FAILED/UPSTREAM_CODE_REVIEW_REQUIRED. No reissue, no authenticated own Source session/CLAIM/run, no maintenance-lane identity, no formal checkpoint/Result/review. Role-bound restore requires approved Site backend Research client and credential. Old three staging items remain independent. Existing automation settings remain unchanged.
