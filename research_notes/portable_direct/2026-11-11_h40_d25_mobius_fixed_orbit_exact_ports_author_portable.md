# D25/LIFT — Explicit Möbius fixed-orbit ports and moving-orbit cancellation

Date: 2026-11-11. Status: AUTHOR-PROVED / EXACT-INTEGER-VERIFIED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CM.

Parent objective ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION remains OPEN. Canonical task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, frozen scientific input awdawmip/enterprise-math@c47e13e4aba0e006366f989d6334d443f6333ae3. This is original author-side portable work, not a Source-native CLAIM, experiment or checkpoint. Antecedent results are cited below, not recredited.

## Universal finite-field theorem

For any prime p>5, uniquely let p=6m+1+4epsilon where epsilon=0 for p≡1 mod6 and epsilon=1 for p≡5 mod6; m>=1. Work in F_p. Let D=F_p minus {0,-1,-2} and define

U(t)=(t+1)(t+2)^2/t,
V(t)=U(t)^m (t+2)^epsilon,
w(t)=[2-12epsilon-(3+10epsilon)t]/(t+2),
T(t)=-2(t+1)/(t+2),
N=-2^{-(2m+epsilon)}.

The earlier two-branch moment theorem gives A=N sum_D V and B=N sum_D Vw, where A=K(1/2), B=(1-6epsilon)K(1/2)+6K'(1/2), and K(X)=sum_{k=0}^m binom(m,k)binom(2m+epsilon,k)X^k. Here A_fix and B_fix denote the same sums restricted to fixed points T(t)=t.

Let chi_2=(2/p) and n=m+epsilon. Define S_j=0 if chi_2=-1. When chi_2=+1, define S_j=0 for j odd and S_j=2*2^(j/2) in F_p for j even. Then for **every p>5**:

A_fix=N (-1)^m S_n,
B_fix=N (-1)^m [(4+4epsilon)S_(n+1)-(3+10epsilon)S_n].

In particular:

A_fix != 0 iff chi_2=+1 and n is even;
B_fix != 0 iff chi_2=+1.

Thus the weighted fixed-fiber contribution is always nonzero when the two fixed points exist. A globally vanishing B must then be compensated exactly by the moving-orbit contribution B_moving=-B_fix. It is not observer-safe to discard the fixed fibers when reconstructing this port.

## Proof

The equation T(t)=t becomes t^2+4t+2=0; thus t=-2+r with r^2=2. For such an r, t+2=r, t+1=r-1, r^2=2, and direct rational simplification yields

U(-2+r)=2(r-1)/(r-2)=-r
w(-2+r)=(8+8epsilon)/r-(3+10epsilon)
       =(4+4epsilon)r-(3+10epsilon).

Consequently V(-2+r)=(-1)^m r^(m+epsilon). The sum of r^j over r^2=2 in F_p equals S_j: if 2 is nonsquare there are no roots, whereas for square 2 the two roots are r and -r, so odd powers cancel and even powers give 2*2^(j/2). Substitution proves both exact port formulas, including the empty-root case.

For chi_2=+1 and n even, S_n is nonzero and S_(n+1)=0, so B_fix has a nonzero coefficient -(3+10epsilon). If epsilon=0 this coefficient is -3, a unit for p>5. If epsilon=1 it is -13, also a unit because 13≡1 mod6 and epsilon=1 requires p≡5 mod6. For n odd, S_n=0 and S_(n+1) is nonzero, while 4+4epsilon equals 4 or 8 and is invertible for all p>5. This proves the nonzero classifications. QED.

## Exact BRC compensation witnesses

At p=7, m=1,epsilon=0, the fixed roots have t=1,2 and:
(A,B)=(2,0); (A_fix,B_fix)=(0,4); (A_moving,B_moving)=(2,3) in F_7.
Here B=0 exactly because 4+3=0, despite its nonzero fixed component.

At p=23, m=3,epsilon=1:
(A,B)=(0,6); (A_fix,B_fix)=(13,15); (A_moving,B_moving)=(10,14) in F_23.
The different zero-port patterns cannot be represented by a scalar which erases fixed/moving provenance.

## Verification

Two independent exact routes were executed. Formula and nonzero-classification tests passed for all 3242 primes 7<=p<=30000: 1613 with chi_2=+1, 1629 with chi_2=-1. For all 364 primes 7<=p<=2500, a separate direct enumeration of r^2=2 evaluated the fixed moments and checked the full binomial K ports against original field moments, with moving/fixed decompositions matching. A local four-file portable ZIP also contains the full 364-record JSON certificate and the exact verification program. The repository verifier here deterministically regenerates that certificate. Finite checks corroborate the universal algebraic proof; no independent review has occurred.

## Boundary and continuation

This quotient explicitly retains the quadratic splitting bit chi_2, n parity, epsilon branch and fixed-versus-moving contribution for A and B. The previously established Lucas quotient already counts fixed fibers by nu=(1+Legendre(Delta))/2; these formulas unpack that component rather than adding it again. The all-prime Legendre(-6/p) vanishing-port selector remains only previously finite-verified (3243-prime test) and is not proved here. Next seek a Cartier/character sum identity giving full moving-orbit cancellation, and an explicit bridge back to the frozen second-digit Delta_p-R_p observation.

Native original-class divided-power H0/B0, [X]U mod p^2, Frobenius eta and kappa are NOT_RUN for this author-side work. The original UR V2 four-file bundle remains missing pending exact 94687-byte/SHA256 verification (4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76); old UR mathematics is not repeated. No Source execution session, winning CLAIM, admission or independent scientific review is claimed.

Antecedent author's two-branch moments:
https://github.com/awdawmip/enterprise-math/blob/021b06753d070d2b69aa5f51a8eb5b73f805972e/research_notes/portable_direct/2026-11-11_h40_d25_both_branch_twisted_mobius_ports_author_portable.md
Antecedent Lucas orbit quotient:
https://github.com/awdawmip/enterprise-math/blob/b38713e73b2052ac15933ca3529e6e7afc983fc9/research_notes/portable_direct/2026-11-11_h40_d25_mobius_orbit_quotient_lucas_two_port_author_portable.md
