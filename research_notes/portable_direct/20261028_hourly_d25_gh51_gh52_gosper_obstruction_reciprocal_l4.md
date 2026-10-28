# D25/LIFT GH-51/GH-52 — Uniform rational Gosper obstruction and homogeneous reciprocal hypergeometric carrier

Date: 2026-10-28. Author-side portable research; **AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING**. Parent `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION` remains OPEN. Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`. Frozen science Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` unchanged. Research logical conversation `chatgpt-research-hourly-enterprise-math-20260923` is separate from maintenance. **No native winning CLAIM, authorized OPEN, native checkpoint, or independent Driver admission is asserted.**

## Source and exact mathematics

Consume original GH-38/39 single-sum coefficients (not a projected Gauss-square total):
[
c_0=1,quad rac{c_{r+1}}{c_r}=rac{(4r+1)^3}{(4r+2)(4r+3)(4r+4)},qquad T_d(z)=sum_{r=0}^d(8r+1)c_rz^r.
]
This scalar finite-field port does not replace original W/S, six Hasse ports or native Heartbeat X6 observation.

### GH-51 — PROVED: no uniform first-order rational Gosper telescoper

For every nonzero rational (z), there is **no** (G(k)inmathbb Q(k)) satisfying identically
[
z(4k+1)^3G(k+1)-(4k+2)(4k+3)(4k+4)G(k)
=(8k+1)(4k+2)(4k+3)(4k+4). 	ag{51.1}
]
Equivalently ((8k+1)c_k z^k) has no indefinite antidifference of the form (G(k)c_k z^k) with rational (G).

**Proof.** Let (A(k)=z(4k+1)^3), (B(k)=(4k+2)(4k+3)(4k+4)). If (G) has poles, choose one (eta) with minimum real part. At (k=eta-1), only (G(k+1)) has a pole, so (A(eta-1)=0) and (eta=3/4). Choose a pole (alpha) of maximum real part. At (k=alpha), only (G(k)) has a pole, so (B(alpha)=0) and (alphain{-1,-3/4,-1/2}). This contradicts (operatorname{Re}etaleoperatorname{Re}alpha). Thus (G) is polynomial.

For (z
e1), the leading term of the left side is (64(z-1)g_Nk^{N+3}) against degree-four right side; (G(k)=ak+b). Comparing coefficients of (k^4,k^3) forces
[
a=rac8{z-1},qquad b=rac{5z-1}{(z-1)^2}.
]
The remaining (k^2,k^1) residuals are respectively
[
-rac{128z(2z+1)}{(z-1)^2},qquad-rac{4z(33z+59)}{(z-1)^2}.
]
For (z
e0) these cannot vanish simultaneously. In particular at (z=9), forced (G=k+11/16) gives (k^2) residual (-342). For (z=1), leading coefficient (64N-96
e0) forces (N=2). Coefficient matching forces (G(k)=16k^2-4k-1/6), but (k^1) residual is (-38/3). Contradiction. QED.

**Scope:** characteristic-zero uniform rational-antidifference obstruction only. It does *not* exclude (p)-dependent WZ certificates, finite-field arithmetic, Frobenius/CM or nonlocal cancellation.

### GH-52 — PROVED: reverse direct source gives homogeneous fourth-order carrier

Let (p=4d+3ge7) be prime, in (mathbb F_p). Set
[
ho_0=1,quadrac{ho_{r+1}}{ho_r}
=rac{(4r+3)(4r+4)(4r+5)}{(4r+6)^3};(0le r<d),quad
R_d(u)=sum_{r=0}^dho_r u^r.
]
All these denominators are units; (ho_r
e0) through (d). Reversing the **original** rank via (4d=p-3) proves
[
oxed{c_{d-r}=c_dho_r,quad
T_d(z)=-c_dz^d(8	heta_u+5)R_d(u)|_{u=z^{-1}}quad(zinmathbb F_p^	imes).}	ag{52.1}
]
Indeed (c_{d-r-1}/c_{d-r}=ho_{r+1}/ho_r) and (8(d-r)+1equiv-(8r+5)). Hence the still-open original target is equivalent to ((8	heta+5)R_d(1/9)=0).

With (	heta=u,d/du), define
[
mathscr L_4=	heta(	heta+	frac12)^3-
u(	heta+	frac34)(	heta+1)^2(	heta+	frac54).
]
Then the **whole polynomial** satisfies
[
oxed{mathscr L_4 R_d=0quad	ext{in }mathbb F_p[u].}	ag{52.2}
]
Proof: the coefficient of (u^n) for (1le nle d) is
(n(n+1/2)^3ho_n-(n-1/4)n^2(n+1/4)ho_{n-1}=0).
The constant term vanishes. At first omitted (n=d+1), the potential forcing is (-(d+3/4)(d+1)^2(d+5/4)ho_d=0) because (d+3/4=p/4=0). Above (d+1) both terms vanish. The leading coefficient of the recurrence is invertible for (1le nle d), so (R_d(0)=1) uniquely fixes the solution among polynomials of degree (le d). QED.

It is the degree-(d) reduction of the formal ({}_4F_3(3/4,1,1,5/4;3/2,3/2,3/2;u)) coefficient sequence. This *homogeneous reciprocal* carrier differs from GH-38's nonzero forward Picard–Fuchs truncation forcing. No equality of richer observer ports follows, and the unknown special-value zero has not been proved.

## Executed evidence / BRC / continuation

The Python standard-library checker `20261028_hourly_d25_gh51_gh52_gosper_reciprocal_check.py` passed for **338 primes** (7le p<5000,;pequiv3mod4), all ranks including the first omitted coefficient, reverse coefficients and exact (52.1) at (z=2,9,-1) for each prime. Rational coefficient no-go tested at (z=1/9,9,-1/2,2,1). Finite check is not a proof of the special value; the already-known observation (T_d(9)=0) was not counted as a new theorem.

BRC `COMPOSE_APPLIED`: exact rank, forward/reverse provenance, signed (mathbb F_p) coefficients, inversion map and differential/jet operations are retained. The compressed scalar is sufficient only for the declared (T_d(z)) observer with (52.1); original W/S, six Hasse ports, GH-20/GH-21 higher digits and P000 native X6 states remain independent.

**Next exact unit:** seek an *independent* finite-character/Frobenius connection certificate for ((8	heta+5)R_d(1/9)=0), using the homogeneous fourth-order operator, not a tautological reversal or GH-37 Laurent reassembly. If found, transport back using (52.1). GH-3 all-prime vanishing, p² source port relations, native p=373, Result/review and formal D25 task continuation remain OPEN.
