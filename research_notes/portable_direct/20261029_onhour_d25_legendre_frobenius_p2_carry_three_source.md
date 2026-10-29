# D25 / SECOND-DIGIT-LIFT — all-prime p² Legendre Frobenius carry and three-source CM residue

**2026-10-29 · AUTHOR-SIDE / EXACT FORMAL-COEFFICIENT PROOF / 14 EXECUTED INTEGER CHECKS / UNREVIEWED / NOT_ADMITTED / NATIVE_H0_B0_NOT_EXECUTED.**

Mother ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. Research lane chatgpt-research-onhour-enterprise-math-20260923, not maintenance. Prior finite Legendre parameter-jet proof: Enterprise Math commit 8e61fa5c5a03e8826147089ea4ffde7624534c77.

## Theorem: every prime p>3, all 0<=e<p

Use the formal variable T, an indeterminate x, k=(p-1)/2, and

\[
A(T)=1-2xT+T^2,\qquad B(T)=A(T)^k,\qquad B_e=[T^e]B(T).
\]

Define the **integral** polynomial

\[
Q_p(T)=\frac{A(T)^p-(1-2x^pT^p+T^{2p})}{p}\in\mathbf Z[x,T]
\]

and let \(C_j=[T^j](B Q_p)\). The numerator of Q_p is coefficientwise divisible by p: Freshman's dream in characteristic p, and \((-2)^p+2\) is divisible by p by Fermat. Then as a **polynomial in x, modulo p²**,

\[
\boxed{P_{p+e}(x)\equiv x^p B_e-\frac p2\bigl(C_{p+e}+3x^pC_e\bigr)\pmod{p^2}.}
\]

This is a complete all-prime formal-power-series theorem, not a finite numerical conjecture. The definition of Q preserves all cross-term Frobenius coefficients, rather than replacing x^p by x or deleting a p-carry.

**Proof.** The exact classical Legendre generating function is

\[
\sum_{n\ge0}P_n(x)T^n=(1-2xT+T^2)^{-1/2}=A(T)^{-1/2}.
\]

Since k=(p-1)/2, the identity \(A^{-1/2}=B(A^p)^{-1/2}\) is exact. Put \(A_0(T)=1-2x^pT^p+T^{2p}\), so \(A^p=A_0+pQ_p\). All binomial coefficients for exponents -1/2 and -3/2 are p-integral for odd p. Consequently

\[
(A_0+pQ_p)^{-1/2}\equiv A_0^{-1/2}-\frac p2 Q_p A_0^{-3/2}\pmod{p^2}.
\]

The degree of B is p-1. Hence at degree p+e (<2p), its product with \(A_0^{-1/2}\) contributes exactly \(x^pB_e\). Meanwhile \(A_0^{-3/2}=1+3x^pT^p+O(T^{2p})\); multiplying by B Q_p produces exactly \(C_{p+e}+3x^pC_e\). This proves the boxed polynomial identity coefficientwise. No infinite series is evaluated at a p-adic unit: all operations extract one finite formal coefficient. Reduction mod p recovers the known Lucas-like \(P_{p+e}(x)\equiv x^pP_e(x)\pmod p\); the displayed Q correction is its exact second digit.

## Combine with the original K_b at unchanged z=1/9

For p≡5,7 mod8 let e=floor((p-1)/4) (odd). The previous verified numerator-hit formula gives \(2r=p+e\), \(\lambda=5\) and the original b. In the quadratic coefficient ring with \(x^2=8/9\), define \(G_{r,b}\) from the **finite parameter derivative** of \((a)_n(1/2-a)_n/(n!)^2\) at a=-r. Combining the previous finite-p² Legendre transport with the new theorem yields

\[
\boxed{
K_b(1/9)\equiv
\underbrace{x^p B_e}_{\text{finite binomial port}}
-\underbrace{\frac p2\bigl(C_{p+e}+3x^p C_e\bigr)}_{\text{Frobenius defect/carry}}
+\underbrace{\frac{5p}{8}G_{r,b}(1/9)}_{\text{parameter derivative port}}
\pmod{p^2}.
}
\]

All three summands retain their original source, sign, valuation, and operator order. Here e is odd, so B_e is odd in x, x^p is odd, and their product is scalar; the full result is scalar at the fixed quadratic point without a premature branch quotient. The auxiliary \(B_e\) **has not been identified** with the earlier external elliptic Hasse polynomial \(H_p(t)\); that correspondence requires a separate derivation. The formula is valid for p≡5,7 mod8, not by this e+p construction for the p≡19 mod24 branch, which has 2r=e.

## Reproducible exact certificates

The standard-library program d25_legendre_p2_frobenius_carry_guard_20261029.py was actually run for 14 primes: 5,7,13,23,29,31,37,47,61,71,109,157,229,373. It constructs B=A^k and A^p in the original two-component (Z/p²)[x]/(x²-8/9) ring, verifies Q's componentwise p divisibility, evaluates both C coefficients, and independently computes the ordinary even Legendre polynomial using the integer binomial formula. All 14 checks passed; code commit 7638017feec1a8d8a4ac533ead9eed21deab0ac9, exact verified code blob 2675fe4a21bd225f3734cc174b67898fa4754825.

| p | x^pB_e | signed Q carry | (5p/8)G source | original K_b |
|---:|---:|---:|---:|---:|
| 13 | 65=5p | 52=4p | 52=4p | 0 mod p² |
| 23 | 138=6p | 23=p | 368=16p | 0 mod p² |
| 37 | 222=6p | 851=23p | 296=8p | 0 mod p² |
| 373 | 125328=336p | 105932=284p | 46998=126p | 0 mod p² |

At 373, 336+284+126=746=2p, so the original companion is zero modulo p² through **three-source signed cancellation**, not because any one port is zero. At 23 the corresponding coefficients are 6+1+16=23.

## BRC scope, science next step, native obligation

**BRC COMPOSE_APPLIED.** Keep typed \((B_e,Q_p,C_e,C_{p+e},x^p,G_{r,b},K_b,\text{Frobenius-before-observer order},v_p,\text{branch label})\); total-only mod-p reduction would erase the Q carry which survives at the second digit. x and T are external algebraic/series variables, not an assertion of a P000-native two-dimensional spatial plane. P000, ACTIVE worldview and the frozen scientific pin remain unchanged.

**New proven result** is the all-prime p² Legendre Frobenius defect formula and its exact fixed-observation three-source composition. **Next scientific unit**: prove or falsify the three-source cancellation for all p≡13 mod24, not another finite Root2 survey; separately analyze the p≡23 branch with opposite parameter-jet forcing, and identify the genuine relation (if any) between the finite B_e, Q_p source and the earlier external Jacobi/Hasse first-order correction. No all-prime Root2/216–2304 p³ bridge or native experiment is claimed here.

**Native top-priority support Issue #1559**, read OPEN/PENDING_OWNER on 2026-10-29, retains the exact p=373 H0/B0 divided-power [X]U mod139129, module rank, genuine semilinear Frobenius/eta, full signed Green/Hesse and κ, Delta_p−R_p. It requires a real authorized native executor and independent validation. Site 0.6.11 read shows research_authority_granted=false and write_relay_enabled=false; no own Source session/CLAIM/run/target_request_id is confirmed and the available tool did not expose a callable recovery_status. No Source checkpoint, CLAIM, dispatch, Result, freeze or independent review was asserted. Original periodic Research lane settings were not modified.
