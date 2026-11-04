# D25: exact reverse-shell 4F3 transport and homogeneous finite-field differential certificate

Date: 2026-11-05. Role: TASK_RESEARCH author-side portable proof only. Classification: EXACT SCOPED ALGEBRAIC PROOF / FINITE EXACT CHECKED / UNREVIEWED / NOT_ADMITTED / NATIVE_SYNC_DEBT.
Stable logical Research lane: chatgpt-research-onhour-enterprise-math-20260923. Maintenance conversation is excluded and no maintenance identity/session is reused.
Mother Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; immutable scientific source pin c47e13e4aba0e006366f989d6334d443f6333ae3.

## 1. Input already proved (consume, do not re-prove)

For every prime p=6n+1>=7, the original full minus half 216 weighted shell satisfies W_full-W_half=p^2 T_A (mod p^3), and the prior onhour shell theorem proves

T_A = 3 C_p (1+2 theta_z) H_n(2) (mod p),

where C_p=216^(2n)*((2n)!)^5/(4n+1)! is a nonzero F_p scalar,
h_r=(2/3)_r^3/[(7/6)_r(4/3)_r*r!], H_n(z)=sum_(r=0)^(n-1) h_r z^r, theta_z=z*d/dz.

The earlier nonzero forward endpoint is L H_n = (h_(n-1)/8) z^n in F_p[z], with L=theta(theta+1/6)(theta+1/3)-z(theta+2/3)^3. This remains true; the new homogeneous representation is a DIFFERENT operator and different finite polynomial, not a claim that the original source vanished.

## 2. New theorem: exact reversed coefficient transport

Let N=n-1 and define, in F_p,

g_k = (1)_k(5/6)_k(7/6)_k / (3/2)_k^3, for 0<=k<=n-1.

All denominators are p-units. Then for every such k,

h_(N-k) / h_N = g_k  (mod p).

Proof: reversing the three numerator/denominator Pochhammer products gives
h_(N-k)/h_N = ((5/6-n)_k (2/3-n)_k (1-n)_k)/(4/3-n)_k^3.
Since 6n+1=p, n=-1/6 in F_p, this becomes exactly g_k. Numerators and denominators in the original forward coefficients are p-units for 0<=r<n. In the reversed coefficients (3/2)_k stays a unit for 0<=k<=n; indeed n<(p-1)/2. Thus the reversal is lossless for the declared finite source index range, not a fit of a scalar total. QED.

Write G_n(t)=sum_(k=0)^(n-1) g_k t^k and U_p=C_p h_(n-1)2^(n-1), which is a p-unit and is exactly the LAST unweighted original upper-shell term in the source j=3n indexing. The original signed upper-shell sum has the new exact observer identity

T_A(p) = -2 U_p (3 theta_t+2)G_n(1/2)  (mod p).

Proof: replace r=n-1-k in 3C_p sum_r(2r+1)h_r2^r, reverse the coefficients, and use 3*(2n-1-2k)=-2*(3k+2) modulo 6n+1. The prefactor U_p retains the original last shell term and its sign; theta_t records the reversed index. QED.

## 3. New theorem: the reversed finite polynomial is a homogeneous order-four solution

G_n is a finite truncation of the very-well-typed generalized hypergeometric coefficient sequence
{}_4F_3(1,1,5/6,7/6;3/2,3/2,3/2;t).

Define
D = theta_t(theta_t+1/2)^3 - t(theta_t+1)^2(theta_t+5/6)(theta_t+7/6).

Then for every prime p=6n+1>=7,

D G_n(t) = 0 as an exact polynomial identity in F_p[t].

Proof: the coefficient ratio is
g_(k+1)/g_k = (2/9)(k+1)(6k+5)(6k+7)/(2k+3)^3,
which cancels all coefficients t^j of D G_n for 1<=j<n. The t^n coefficient is
-n^2(n-1/6)(n+1/6)g_(n-1)=0, because n+1/6=p/6=0 in F_p.
The constant coefficient also vanishes; higher coefficients are absent. The terminal zero is legitimate: (7/6)_n contains p/6, while (3/2)_n is a unit. Therefore g_n=0 is a genuine terminating numerator, not a suppressed denominator pole. QED.

The juxtaposition is the new diagnostic: the forward 3F2 carries a nonzero inhomogeneous boundary, whereas the exact REVERSED 4F3 is homogeneous. The nonzero boundary has NOT disappeared: it is explicitly preserved as the unit U_p and the weighted derivative observer (3 theta_t+2)G_n(1/2). A proposed WZ/Green certificate may operate on the homogeneous 4F3, but it must reproduce -2 U_p times that observer when returned to the original 216 shell.

## 4. Exact executable validation and source separation

Checker: research_notes/portable_direct/d25_reversed_terminal_4f3_checker_20261105.py.
It computes (i) original factorial 216 j-shell, (ii) the independent forward 3F2 coefficients, (iii) reverse 4F3 coefficients, (iv) every polynomial coefficient of the order-four differential equation, and (v) the nonzero original forward endpoint. Pure integers and F_p modular arithmetic, no floating-point approximation.
All 611 primes p=6n+1, 7<=p<=10000 passed; 0 mismatches. Representative (p,n,T_A,U_p,(3theta+2)G_n(1/2),forward-endpoint) are:
(7,1,5,4,2,1), (13,2,10,3,7,9), (19,3,9,2,12,16), (139,23,13,108,128,24), (373,62,266,83,295,251).
Finite tests support the arithmetic implementation but the theorem proof is the exact reversal and coefficient recurrence, not extrapolation from these 611 cases.

## 5. Scope, BRC and original benchmark

BRC result: COMPOSE_APPLIED. The carrier records original model=216, original j=2n+1+r, reversed k=n-1-r, valuation-two shell, nonzero terminal U_p, signed weight, derivative observer and p-local field. Reversal is a bijection on the declared indexed source, so no signed provenance is removed. Homogeneous D G_n=0 does not establish W_full=V_full (mod p^3), the frozen Delta_p-R_p=0 (mod p), or ANY native H0/B0 claim.

The frozen p=373 same-original-class divided-power H0/B0 benchmark remains unexecuted under support issue #1559: [X]U modulo 139129, actual module rank, semilinear Frobenius and eta, kappa, odd observer, and independent replication all PENDING_OWNER. No surrogate 4F3/CM computation replaces that benchmark. Old staging stays separately sourced.

Previous native Source read request onhour11-20261105-0103-current-cont had SUCCEEDED / execution_authorized=false. This author note does not assert a live session, claim, run, Source checkpoint or admitted Result.

## 6. Next exact test toward the frozen target

Apply finite homogeneous operator D to construct an honest terminating WZ/Green adjoint that evaluates the ORIGINAL observer (3theta_t+2)G_n(1/2), including the unit U_p. Connect its resulting signed boundary to the 216 HALF-sum correction
W_half = p + p^2 J_p, with J_p=-T_A on the target residue classes as the OPEN all-prime statement.
First discriminate at p=13,19,139,373, preserving J_p and T_A separately; no claim of completion before a uniform proof. Independent native H0/B0 p=373 remains a separate highest-priority admission gate.

Source: exact predecessor research_notes/portable_direct/20261105_onhour_d25_216_shell_pole_3f2_forcing.md and original source-port note 20261026_onhour_d25_native_lift_source_port_identity.md, plus Guo–Zudilin 2019 Adv. Math. 346 (2019), DOI 10.1016/j.aim.2019.02.008 for the separately proven 2304 comparison.
