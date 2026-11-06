# D25 — A p-adic anti-diagonal first integral joining the original-216 middle and second shells

Date: 2026-11-06. TASK_RESEARCH author-side portable proof. Frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3, publication TP2-B6F4FC938FF94941C1B7. Logical lane chatgpt-research-onhour-enterprise-math-20260923; maintenance lane excluded. Status: AUTHOR-PROVED / FINITE-VERIFIED / UNREVIEWED / NOT_ADMITTED. Native p373 H0/B0 original experiment #1559 remains NOT_EXECUTED/PENDING_OWNER.

## Exact input and new theorem

For every prime p=6m+1>3, let a_n=(2n)!(3n)!/[216^n(n!)^5] and W_p=sum_(n=0)^(p-1)(6n+1)a_n. Consume the existing original 216 three-shell theorem, commit eec361046d7677ee6b53bf85786af97e616e325d. Its independent rational sequences, for 1<=j<m, are

q_0=g_0=1,
q_j/q_(j-1) = 3j(6j+1)(3j+1)/[4(3j+2)^3],
g_j/g_(j-1) = j(6j-1)(6j+1)/[9(2j+1)^3].

NEW THEOREM (anti-diagonal first integral): for every 1<=j<=m in F_p,

(3j-1)^3 q_(j-1) g_(m-j) = -27 q_(m-1)/8.                  (A)

Every denominator and q/g factor in this statement is a p-unit on the stated range.

Proof: Put T_j=(3j-1)^3 q_(j-1)g_(m-j). For 1<=j<m, t=m-j, the product of the three successive ratios is

T_(j+1)/T_j = [(3j+2)/(3j-1)]^3 *
              [3j(6j+1)(3j+1)/(4(3j+2)^3)] *
              [9(2t+1)^3/{t(6t-1)(6t+1)}].

Since t=m-j=-j-1/6 (mod p), the last factor equals
4(3j-1)^3/[3j(6j+1)(3j+1)] (mod p).
The product is 1. Evaluate T_m at g_0=1; 3m-1=(p-3)/2=-3/2 (mod p), so T_m=-27q_(m-1)/8. QED.

## Signed prefix preservation and one-kernel scalar reduction

For every 0<=r<m, the exact *signed-prefix* reflected observation is

sum_(t=0)^r (6t+4)g_t
 = (81/8) q_(m-1) sum_(j=m-r)^m (2j-1)/[(3j-1)^3q_(j-1)]   (mod p).  (B)

Proof: substitute t=m-j in (A) and use 6t+4=p+3-6j=-3(2j-1) (mod p). In particular define

D_m = sum_(j=1)^m (2j-1)/[(3j-1)^3q_(j-1)] (mod p);
G_0 = sum_(t=0)^(m-1) (6t+4)g_t.

Then G_0 = 81 q_(m-1)D_m/8 (mod p). The earlier proved first second-shell coefficient a_(3m+1)/p²=-a_(2m)q_(m-1)/576 (mod p) and g-ratio give a new termwise reversed-216-shell formula, for 1<=j<=m:

C_j := a_(4m+1-j)/p²
 = 3a_(2m)q_(m-1)^2/[512(3j-1)^3q_(j-1)] (mod p).       (C)

At j=1 this yields an endpoint square:

C_1 = 3 a_(2m) q_(m-1)^2/4096 (mod p).                  (D)

The nonzero original valuation-two weighted shell is therefore

sum_(n=3m+1)^(4m) (6n+1)a_n
 = -9p²a_(2m)q_(m-1)^2 D_m/512 (mod p³).                (E)

Finally, combining (E) with the ALREADY PROVED original middle-jet reduction yields the exact all-prime one-kernel identity

W_p = P_(2m+1) + p*a_(2m)*(Q_0+pQ_1)/32
      -9p²*a_(2m)*q_(m-1)^2*D_m/512 (mod p³),            (F)

where P, Q_0, Q_1 have precisely the definitions and precision in the cited three-shell theorem. Formula (F) removes the separately evaluated g-sequence but retains every original p² contribution, the signed index information, and the first-order middle jet. This is a representation theorem; the all-prime target W_p=p (mod p³) for p mod24 in {13,19} still requires a finite cancellation certificate.

## Executed exact verification

The companion standard-library integer-only program d25_qg_reflection_dual_kernel_check_20261106.py was executed for all 148 primes p=1(mod 6) with 7<=p<=1999 and separately p=5113: 149 primes, 23,804 termwise reflected pairs, ZERO failures. It independently forms the original a_n modulo p³, checks (A), (C), (D) for every j, checks the signed sums (B)/(E), and reconstructs the full W_p using the old middle jet and NEW one-q observer (F).

Nonzero witnesses:
- p19: (m,q_(m-1),C1,G0,D_m)=(3,8,2,5,1); shell/p²=9; W_p=19 mod 6859.
- p373: (62,7,181,217,132); shell/p²=266; W_p=373 mod 51895117.
- p5113: (852,3577,72,1135,1675); shell/p²=4671; W_p=5113 mod 5113³.

All operations use integers and modular inverses of certified units. The finite run verifies these inputs, while the recurrence proof establishes (A)-(F) under their hypotheses. The p5113 witness does not enlarge the immutable target prime class.

## BRC observer, remaining unit and Source boundary

BRC-style typed carrier: (p,m,j,reflected_original_n=4m+1-j, original valuation=2, p-unit C_j, q_(j-1), q_(m-1), original weight 3-6j). The map retains individual coefficients and signed prefixes, not just a collapsed total. This is an external arithmetic representation, not a claim about native X6/H0/B0 execution.

Next smallest mathematical unit: insert (F) into the already proved E.2/Franel two-jet, seek a finite nonlocal signed-boundary adjoint for W_p-V_p mod p³, testing against nonzero signed J19=6, J373=98 and valuation-two shell9/266, then p5113. A failing candidate should return its minimal exact typed counterexample. Do not reprove the q/g reflection, prior shells or the E.2 p4 signed-tail involution.

Canonical Source original request: onhour11-20261106-1400-exact-research-lane-continuation; 2026-11-06 23:xx +0800 read WAITING_RESOURCE/EVENT_COLLECTION_IO, same-ID reconcile QUEUED. Source winning claim/session/run not verified. Client checkpoint revision22 is historical SERVER_SQLITE_COMMITTED and was not updated by this author-side report. No native Result/admission or independent review is claimed. Three historical staging items remain separate; #1559 original p373 native rank/Frobenius/Green/kappa and independent replica remain pending.
