# D25: universal Gauss terminal source and CM third-digit coordinate jet

2026-11-01 16:24 Asia/Hong_Kong · TASK_RESEARCH logical lane `chatgpt-research-hourly-enterprise-math-20260923` · Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT` · publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific pin `c47e13e4aba0e006366f989d6333ae3` unchanged.

**Scope:** AUTHOR-DERIVED / EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING / NATIVE_NOT_RUN. This consumes, without re-crediting, the previously proved beta CM mod-p selector (on-hour lane, `2e52f3dfc171e3b0621084a3eb88a48377c3b000`), this lane's adjacent Legendre derivative (`15009ebc884193a7713c4e81e2ad9f007068bd74`), and the already-known rational/Frobenius Taylor formula. The genuinely new claims are the universal normalized terminal coefficient and the explicit third-digit observer with its necessary derivative-carry port.

## Theorem I: all-prime terminal source at p³

Let p=8t+5≥13 be prime, F_p(z)=Σ_(k=0)^(p-1)c_k z^k, c_k=(1/8)_k(3/8)_k/(k!)², and L=z(1-z)∂²+[1-(3/2)z]∂-3/64. All coefficients belong to Z_(p). Then

```text
c_(p-1) = p² (mod p³), and v_p(c_(p-1)) = 2;
L F_p(z) = -(35/64) p² z^(p-1) (mod p³), coefficientwise.
```

**Proof.** The exact numerator of c_(p-1) is ∏_(j=0)^(p-2)(8j+1)(8j+3), with denominator 64^(p-1)((p-1)!)². The only p-multiples occur at a=(5p-1)/8, where 8a+1=5p, and b=(7p-3)/8, where 8b+3=7p; both indices are in [0,p-2]. The affine residue maps j↦8j+1 and j↦8j+3 permute F_p. By Wilson, omitting the zero and the j=p-1 terms gives products (-1)/(-7)=1/7 and (-1)/(-5)=1/5 modulo p. Their p-adic unit product multiplied by 5·7=35 is 1; 64^(p-1) and ((p-1)!)² also reduce to 1. Therefore c_(p-1)/p²=1 (mod p), exactly two p-factors. The hypergeometric coefficient recurrence (k+1)²c_(k+1)=(k+1/8)(k+3/8)c_k cancels all nonterminal coefficients of L F_p, giving the **exact identity**

```text
L F_p(z) = -[(p-1)+1/8][(p-1)+3/8] c_(p-1) z^(p-1).
```

Reduction modulo p³ proves the formula. Consequently the homogeneous differential equation holds modulo p² but fails modulo p³ as a polynomial and at any p-unit z: normalized terminal source is -35 z^(p-1)/64, which is a unit modulo p. QED.

## Theorem II: CM Frobenius coordinate difference modulo p³

Assume p≡13 (mod 24), n=(p-1)/4, s²=2, x=2s/3, λ=1/9, and B_p=P_(n-1)(x), classical Legendre polynomial. n-1 is even so B_p is a p-integral rational scalar, independent of s-sign. Let the **integer** q=(9^(p-1)-1)/p and define d_p=(F'_p(λ)+(9/8)B_p)/p in Z_(p), integral by the previously proved CM-neighbor derivative law.

Then the following holds for *every* such prime, without assuming conjectural F_p(λ)=0 (mod p²):

```text
F_p(λ^p) - F_p(λ)
 = (p q/8) B_p - p² [(q/9)d_p + (17q²/256)B_p] (mod p³).
```

**Proof.** The proved beta selector gives F_p(λ)=0 (mod p). Theorem I implies L F_p=0 (mod p), so at λ=1/9, (8/81)F''_p(λ)+(5/6)F'_p(λ)=0 (mod p), and F''_p(λ)=-135 F'_p(λ)/16=1215 B_p/128 (mod p). Since λ^p=λ/(1+pq) exactly, Taylor yields

```text
F_p(λ^p)-F_p(λ)
 = -pλqF'_p(λ)+p²q²[λF'_p(λ)+(λ²/2)F''_p(λ)] (mod p³).
```

Use F'_p(λ)=-(9/8)B_p+p d_p, λ=1/9. The p² bracket is -B_p/8+15B_p/256= -17 B_p/256. Substitute to finish. QED.

**Precision/observer lease:** q modulo p², B_p modulo p² and d_p modulo p suffice *for this coordinate-difference observer modulo p³*. The two p² sources -q d_p/9 and -17q²B_p/256 remain distinguishable. Absolute F_p(λ^p), signed quadratic high-index provenance, and the original native H0/B0 operator are outside this quotient: preserve F_p(λ) and the original source/branch data for those future operations. In BRC terminology this is a proved observer-specific jet descent, not a positive-mass or X6-state collapse.

## Reproducible exact arithmetic

Companion `research_notes/portable_direct/d25_cm_third_digit_jet_20261101.py` was executed with Python standard library integers. It constructs every original Pochhammer coefficient modulo p³, independently calculates P_(n-1) in the quadratic coefficient ring modulo p², evaluates F,F',F'' by Horner, checks L F at λ and z=2 and checks the full third-digit identity. Results: **109/109** primes p≤3000, p≡5 (mod 8), pass the universal terminal theorem; **53/53** primes p≤3000, p≡13 (mod 24), pass the coordinate formula. No floating-point or native scientific runtime was invoked.

| p | B_p mod p² | d_p mod p | normalized third carry | derivative port | quadratic port |
|---:|---:|---:|---:|---:|---:|
|13|29|6|12|11|1|
|37|534|22|15|23|29|
|61|2441|29|43|45|59|
|109|5091|88|107|108|108|
|373|38379|213|300|51|249|

Here normalized third carry = [F_p(λ^p)-F_p(λ)-(pq/8)B_p]/p² mod p. Terminal source ratio L F_p(λ)/p² equals -35/64 mod p, respectively 9,22,29,25,320 in these samples. The equality 51+249=300 (mod 373) exhibits retention of both third-digit sources.

**Next smallest science unit:** express d_p (mod p) using the already separated Jacobi/Frobenius ports and signed high-index contribution, then seek an all-prime CM p² cancellation certificate or a precise counterexample. Include the universal -35/64 terminal source in any p³ Gauss lift. Frozen mother goal A_p=p (mod p³) for p mod24 in {13,19} remains OPEN.

**Control provenance at 2026-11-01 ~16:20 +08:** native recovery #6637 identifies own ACTIVE Researcher service session `MCP-06f7ad61a8d841d9ba1ba1ef4d088d94` but no execution authority. Exact continuation #6638 definitively FAILED with `UPSTREAM_CODE_REVIEW_REQUIRED`; support #1558 owns running-backend effective config/code reconciliation. Native original-class p373 H0/B0 remains #1559 PENDING. Neither this portable note nor Git storage is a SOURCE checkpoint, formal Research-Activity registration, Result, or independent review. P000 ACTIVE, source pins and separate maintenance identity are preserved.
