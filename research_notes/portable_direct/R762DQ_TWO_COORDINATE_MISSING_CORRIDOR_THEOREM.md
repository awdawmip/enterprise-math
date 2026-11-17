# R762DQ — Closing the missing two-coordinate 3-adic BRC corridor

Date: 2026-11-18 (Asia/Shanghai). Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS / TP2-8B7E13C5904A2D6F1142.
Researcher: EM-X6-3050F6, original Source SID MCP-4b2d70a97f594366a7c94a0f8b45df38. Independent review: NOT_REVIEWED.

## Frozen inputs, scope and provenance

P000 V5 pinned at awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json; immutable taskbook pinned at awdawmip/enterprise-math@e3f42efac29a2da2d95be391f3231a664e2fade0:research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md. This is a strict extension of R762DP, immutably saved at cf3c1f2b7e15621cc53dbd839d4a3c6364be1ece:research_notes/portable_direct/R762DP_TWO_COORDINATE_BRC_CONTENT_THEOREM.md (Draft PR #2674, not merged).

Six named *positive-multiplicity* microbranches of the existing **candidate** paired-triad area model have polynomial
P(X,Y,Z)=1+X+Z+XY+YZ+XYZ.
The declared endpoint observer pi_XZ(u,v,w)=(u,w) produces the exact joint histogram F(X,Z)=1+2X+2Z+XZ, with its six named branch multiplicities preserved, in the integer group ring
R_Q=Z[X,Z]/(X^Q-1,Z^Q-1).
Write c_Q(n) for gcd of all integer coefficients of F^n, n>=0. The minimum number of equiprobable deterministic initial seeds for **only this terminal marginal** is M_Q(n)=6^n/c_Q(n). It is not the full named path/source carrier, not the native full three-coordinate residual, and not a two-dimensional native plane. X6 six-axis P000, third coordinate, signed Port/source and unlicensed native triad event conditions are retained.

## Theorem (all 3-power moduli, exact through 7d)

For each integer a>=2 set Q=3^a, d=3^(a-1). Then:
- c_Q(n)=1 for 0<=n<3d;
- c_Q(n)=9 for 3d<=n<5d;
- **c_Q(n)=81 for 5d<=n<7d**.

The previously open corridor 5d<=n<6d is now proved exactly. The other regions were proved in R762DP. Consequently the sharp endpoint-seed counts are 6^n, 6^n/9, 6^n/81 respectively. For the paired-triad block interpretation set n=2k: n counts the positive candidate microbranch factors, not independently authorized native events.

## Proof (integer group-ring, all a>=2)

Let A_Q=Z[T]/(T^Q-1), x=T-1. As Q=3^a is odd, the two endpoints T^Q-1 cancel in the binomial expansion of (T-1)^Q. For 0<i<Q,
v_3(binomial(Q,i))=a-v_3(i).
Thus x^Q is coefficientwise divisible by 3; after dividing by 3, precisely indices i=d,2d survive mod3 with signs:
x^Q/3 == T^d-T^(2d) == -x^d(1+x^d) (mod 3 A_Q).
In A_Q/3A_Q we have x^Q=0, hence
x^(5d)=x^(2d)x^Q=3*x^(2d)*(x^Q/3) is divisible by 9:
the mod3 quotient is -x^(3d)*(1+x^d)=0.
Also x^m is divisible by 3 for every m>=3d. The same one-axis facts hold for x=X-1 and z=Z-1 separately in R_Q.

Now F=xz+3(2+x+z) in the **integer** ring. At n=5d,
F^(5d)=SUM_{j=0}^{5d} binomial(5d,j)*3^j*(xz)^(5d-j)*(2+x+z)^j.
Every term is divisible coefficientwise by 81:
1. j=0: x^(5d),z^(5d) are each divisible by 9;
2. j=1: 3*binomial(5d,1)=15d is divisible by 9 since 3|d, and x^(5d-1),z^(5d-1) are each divisible by 3;
3. j=2: factor 9 times x^(5d-2),z^(5d-2), each divisible by 3 because 5d-2>=3d;
4. j=3: factor 27 times x^(5d-3),z^(5d-3), each divisible by 3 because d>=3, giving at least 243;
5. j>=4: the explicit factor 3^j is divisible by 81.
Thus 81|c_Q(5d).

For sharpness, the previously proved exact Frobenius leading term can be rederived by expanding F^Q:
F^(3d)/9 == D=(X^d-X^(2d))(Z^d-Z^(2d)) (mod 3 R_Q).
In R_Q/3R_Q = F_3[x,z]/(x^(3d),z^(3d)),
D=x^d*z^d*(1+x^d)*(1+z^d).
The two parentheses are units, and (x^(2d)*z^(2d)) is nonzero, so
D^2=x^(2d)*z^(2d)*(1+x^d)^2*(1+z^d)^2 !=0.
Hence F^(6d) is divisible by 81, but not 243.

Since the sum of coefficients of F^n is 6^n, no prime other than 2 or 3 can divide its content. As Q is odd, F mod 2=1+XZ is nonzero in the *reduced* group algebra F_2[C_Q^2] (each cyclic factor has odd order and the defining polynomials are separable). Therefore its positive powers never vanish, so 2 does not divide c_Q(n). It follows that c_Q(6d)=81.

Finally, coefficientwise integer multiplication implies c_Q(n)|c_Q(n+1), since every coefficient of F^(n+1) is an integer combination of coefficients of F^n. In the missing range 5d<=n<=6d:
81 | c_Q(5d) | c_Q(n) | c_Q(6d)=81.
Thus c_Q(n)=81 throughout. R762DP gives the same exact value for 6d<=n<7d. The theorem follows. QED.

## Exact verification and limits

Companion R762DQ_VERIFY.py is pure-integer BRC convolution for Q=9,27,81 and every n=1,...,7d. It checks the total six-branch mass exactly as 6^n, all 270 positive-exponent sharp-content equalities, the one-axis x^Q/3 mod3 congruence, divisibility of x^(5d) by 9 and two rounds of direct six-named versus aggregated positive branches. R762DQ_EVIDENCE.json records the complete stdout and individual configurations. Every check passed. Computation is a finite check, separate from the all-a proof. The formula does not cover Q=3.

At n=7d the experiments give c_Q(7d)=729 for the three tested Q; a uniform theorem on that jump and all later corridors is still open. The full three-coordinate 3-adic content is also open. The native licensed TRIADIC_CLOSURE_E Cell/Link/Port predicate and V17/V29/V39 transports remain unverified, so this observer-only theorem must not be promoted to licensed future-event BRC equivalence, formal Result or independently accepted theorem.

Next: derive the 7d 3-adic leading form or find an admissible counterexample, and separately test exact Source-native signed triadic event legality with original task pins.