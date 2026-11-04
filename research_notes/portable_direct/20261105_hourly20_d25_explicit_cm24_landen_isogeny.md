# D25 CM−24: constructed Landen 2-isogeny and exact differential scaling

2026-11-05. **AUTHOR-PROVED / FINITE EXACT CHECKED / UNREVIEWED / NOT_ADMITTED**. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, frozen science pin c47e13e4aba0e006366f989d6334d443f6333ae3. Extends the same-turn CM−24 Frobenius norm and Φ₂ certificate. Original native p=373 H0/B0 remains an independent unexecuted obligation.

## Theorem (explicit degree-two isogeny to a Frobenius-conjugate)

Let a²=2, b²=3 over Q, let e,d=±1, and define

    s(e,d) = 3+2e a+d(2b+e ab),    t(e,d)=s(e,d)².

The **exact** field identity

    (1+s(e,d))*s(−e,−d) = 1−s(e,d)

gives

    t(−e,−d) = ((1−s(e,d))/(1+s(e,d)))².

For a parameter λ=s², characteristic not 2, with s≠±1, consider the Legendre curve

    E_λ: y²=x(x−1)(x−λ)=x³+A x²+B x,
    A=−(1+λ), B=λ.

Define

    X=x+A+B/x=x−(1+λ)+λ/x,
    Y=y(1−B/x²).

This is the standard **separable cyclic degree-2 isogeny with kernel {O,(0,0)}** onto

    E': Y²=X³−2A X²+(A²−4B)X
          =X[X+(1+s)²][X+(1−s)²].

Put α=−(1+s)² and β=−(1−s)². Choose ρ²=α and rescale u=X/α, v=Y/ρ³. The target is the Legendre curve E_(β/α), where

    β/α=((1−s)/(1+s))²=t(−e,−d).

For invariant differentials ω=dx/(2y) and ω*=du/(2v), **the exact pullback is**

    φ*(ω*)=ρ ω.                              (†)

Proof: Set X=(x²+Ax+B)/x and Y=y(x²−B)/x². The polynomial identity

    (x²+Ax+B)²−2Ax(x²+Ax+B)+(A²−4B)x²=(x²−B)²

proves the E' equation. The kernel and separable degree-two follow from the displayed rational isogeny (in characteristic ≠2). Its quadratic factors have roots α and β, yielding the target and Legendre scaling. Since dX/dx=1−B/x², one has dX/(2Y)=dx/(2y), and then du/(2v)=ρ dX/(2Y); this proves (†). The four Landen identities follow by expanding in the basis 1,a,b,ab with a²=2,b²=3.

**Frobenius scope.** For every prime p≥5, p≡5 mod8, the preceding exact CM branch theorem gives s,t∈F_(p²). Also p≡1 mod4, so i=√(−1)∈Fp and ρ=i(1+s) is in F_(p²). Thus the entire isogeny and its differential factor are defined over F_(p²). The prior exact Frobenius law gives:

* p≡5 mod24: t(−e,−d)=t(e,d)^p. Thus φ explicitly gives E_t→E_(t^p) over F_(p²).
* p≡13 mod24: t(−e,−d)=1/t(e,d)^p. Since s^p∈F_(p²) is a square root of t^p, the Legendre coordinate change x↦x/t^p, y↦y/(s^p)^3 is an F_(p²)-isomorphism E_(t^p)→E_(1/t^p). Composing its inverse with φ gives E_t→E_(t^p) over F_(p²).

The exact differential factor ρ and the split/inert inversion are required source labels for subsequent Hasse first-jet work, not replaceable by an unlabelled scalar j equality.

## Exact verification

The Python 3 stdlib checker tests all four exact Landen identities and target factorisations in Z[a,b], 16 independent rational Vélu substitutions, and 2276 CM branch-target congruences over the 569 primes 5≤p≤20000 with p≡5,13 mod24 (281/288). All PASS. The universal statement is proved algebraically; the window is a finite check.

BRC carrier and operation: (e,d)→s→t→(X,Y)→(u,v), including chosen ρ and Frob/inversion labels. This is a CM isogeny source, not the task's original H0/B0 divided-power Frobenius, normalized eta/kappa or signed odd Hesse Green observable.

## Next scientific action

Transfer the Hasse invariant **first jet** through the explicit φ, with the factor ρ=i(1+s) and correct Frobenius/inversion choice, to prove or refute the still open split-class condition

    16t(1−t)(1+t) H_p'(t)+(1+2t−7t²)H_p(t)=0.

Then consume the existing short Jacobi Green–Wronskian mod p² bridge. The independent original-class p=373 [X]U, H0/B0 and Δp−Rp obligations remain open under their Source-persisted checkpoint. No native experiment or independent review is asserted.
