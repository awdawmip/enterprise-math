# D25 — all residue classes of the p³ Gauss terminal coefficient

Date: 2026-11-01. Author-side portable follow-up in TASK_RESEARCH lane `chatgpt-research-hourly-enterprise-math-20260923` to the source-backed D25 project note `20261101_hourly_d25_universal_terminal_cm_thirddigit.md` at commit `aa651c4deafb50206eb34dab26be052717b4a654`. Scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3`, P000/ACTIVE unchanged. **AUTHOR-DERIVED / EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NATIVE_NOT_RUN**.

## General theorem

For every prime p≥11, define

```text
F_p(z) = sum_{k=0}^{p-1} c_k z^k,
c_k=(1/8)_k(3/8)_k/(k!)²,
L=z(1-z)d²/dz²+(1-3z/2)d/dz-3/64.
```

Let alpha_p,beta_p ∈ {1,3,5,7} be uniquely determined by alpha_p*p=1 (mod8), beta_p*p=3 (mod8). Then the **whole polynomial** obeys

```text
v_p(c_{p-1})=2,
c_{p-1}/p² = alpha_p beta_p / 35 (mod p),
L F_p(z) = -alpha_p beta_p p² z^(p-1)/64 (mod p³).
```

The congruences are coefficientwise in Z_(p)[z]. The residue-class dichotomy:

| p mod8 | alpha_p | beta_p | alpha_p beta_p | normalized terminal source |
|---:|---:|---:|---:|---|
|1|1|3|3|-3/64|
|3|3|1|3|-3/64|
|5|5|7|35|-35/64|
|7|7|5|35|-35/64|

In particular, the **two original 216-sum mother-goal prime classes have different universal p³ forcing**:

```text
p=13 (mod24): L F_p(z) = -35 p² z^(p-1)/64 (mod p³)
p=19 (mod24): L F_p(z) = - 3 p² z^(p-1)/64 (mod p³).
```

A cross-class p³ Frobenius/Green or Hesse comparison must retain the residue-class tag and corresponding forcing. These are ordinary finite-Gauss boundary values, not the native H0/B0 or the original 216 coefficients.

**Proof.** With k=p-1, the numerator products have unique p-divisible factors 8*j_a+1=alpha_p*p, 8*j_b+3=beta_p*p, where j_a=(alpha_p*p-1)/8, j_b=(beta_p*p-3)/8. Since p≥11 these lie in [0,p-2], and no other factors are divisible by p. For each linear residue permutation, the product of nonzero residues as j runs from 0 to p-1 is -1 (Wilson). The j=p-1 excluded factors are -7 and -5, so the remaining unit products are 1/7 and 1/5 modulo p. As 64^(p-1)=1 and ((p-1)!)²=1 modulo p, the normalized top coefficient is alpha_p*beta_p/(7*5)=alpha_p*beta_p/35. The exact hypergeometric recurrence cancels all internal coefficients of L F_p, leaving

```text
L F_p(z) = -[(p-1)+1/8][(p-1)+3/8] c_(p-1) z^(p-1).
```

The endpoint factor reduces to 35/64 modulo p; multiply by alpha*beta/35 to get -alpha*beta/64. QED.

**Exact tests.** The separate standard-library integer checker computes original Pochhammer coefficients modulo p³ and independently evaluates F,F',F'' at z=2 and z=1/9. All **426 primes** 11≤p≤3000 pass the coefficient and ODE checks, partitioned by p mod8 = 1,3,5,7 into **101,108,109,108**. Certificates: p=13 top normalized 1, source ratio 9 mod13; p=19 top normalized 18, source ratio 5 mod19; p=373 normalized 1, source ratio 320 mod373. Generality follows from the algebraic proof, not finite testing.

**BRC/observer scope.** For the future operation of modulo-p³ truncated Gauss Green response across both target prime classes, a total-only observer dropping p mod8 or terminal coefficient is not certified lossless. Retain distinct source ports -35/64 and -3/64. This is a finite valuation/residue-class carrier, not a primitive positive-branch-weight assertion or native X6 collapse.

**Next:** Investigate whether this normalized source dichotomy survives the exact signed quadratic cutoff and original216 mapping. First prove the class-specific normalization/port map for both residue classes. Current Source/control #1558 and native p373 H0/B0 #1559 remain pending. There was no native CLAIM, OPEN, Source checkpoint, Result or independent acceptance.
