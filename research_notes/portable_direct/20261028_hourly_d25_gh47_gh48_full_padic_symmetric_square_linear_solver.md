# D25/LIFT GH-47–GH-48: full p² symmetric-square coefficient solver and boundary-notch classification

Date: 2026-10-28. TASK_RESEARCH author-derived portable arithmetic, **UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING**. These two units compose existing GH-41–GH-46 exact rational formulas into a new full-range p-adic algorithm and a classified forcing defect; they do **not** prove the original GH-3 congruence or create a native CLAIM/OPEN/Source checkpoint.

Parent: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION (OPEN); Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; immutable publication TP2-B6F4FC938FF94941C1B7. Research routing label `chatgpt-research-hourly-enterprise-math-20260923`, distinct from maintenance `chatgpt-hourly-enterprise-math-20260921`; no currently verified service session/claim/run is asserted. Preserve frozen scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3`, P000 and ACTIVE worldview.

## Carrier, source and domain

Let `p=4d+3 >= 7` be a prime and `R=Z_(p)`. Let `beta_r`, `a_r` and `c_r` retain the precise GH-38–GH-45 rational recurrences. Define beta_r for `0<=r<=d` by beta_0=1 and

`beta_(r+1)/beta_r = 16(r+1)(4r+3)/(8r+13)^2`.

Set `V(u)=sum_(r=0)^d beta_r u^r`, `v_n=[u^n]V^2`, with beta_n=0 outside [0,d], v_n=0 outside [0,2d]. Let `gamma_r=a_(d-r)/a_d` be the **actual** reversed forward Gauss coefficient:

`gamma_0=1; gamma_(r+1)/gamma_r=4(4r+4-p)(4r+3-p)/(8r+13-2p)^2`,

and `Gamma(u)=sum_(r=0)^d gamma_r u^r`, `g_n=[u^n]Gamma^2` (extended by zero). These are rational functions of the integer parameter p, with all needed denominators p-units. Retain ordered source pairs `(i,j)`, their index sum, coefficients and future differentiated/evaluated observer; a scalar residue is **not** the original W/S, six Hasse ports, nor a native X6 state.

## GH-47: complete rational and p² boundary-forced recursion (PROVED)

For **every** integer `d>=1` with formal parameter `p=4d+3`, and every `0<=n<=2d+1`, the following is an exact identity in rational numbers:

```text
(4n+5)^3 v_n =
  8(n+1)(2n+1)(4n+3) v_(n-1)
  + 25(6n+5) beta_n
  - 16p(d+1) beta_d (6n-4d+1) beta_(n-d-1).       (47.1)
```

In particular this is valid over `R/p²`, with no lost upper-boundary source. Proof: expand GH-44's **exact** symmetric-square affine equation

```text
S_0(V²) = -(25/64)(6D+5)V
        + [p(d+1)beta_d/4] u^(d+1)(6D+2d+7)V,
S_0=u(D+2)(D+3/2)(D+7/4)-(D+5/4)^3, D=u d/du.
```

At coefficient n, the left side equals
`(n+1)(n+1/2)(n+3/4)v_(n-1)-(n+5/4)^3v_n`.
The source at n>=d+1 is
`[p(d+1)beta_d/4](6(n-d-1)+2d+7)beta_(n-d-1)`.
Multiplying by 64, moving terms and simplifying gives (47.1), including n=0 and n=2d+1. All nontrivial denominators `4n+5` for 0<=n<=2d are p-units: a multiple of p among p,2p,3p cannot equal 4n+5 in this range (first two fail mod 4, third is too large). Hence beta_n and v_n are recoverable using **O(d) arithmetic operations modulo p²**, once beta_d has been calculated. Omitting the final source would silently replace the p² equation by its mod-p truncation.

## GH-48: exact deformed-square solver, first jets and a unique source notch (PROVED)

GH-45's exact parameter-deformed affine square equation yields the equally explicit rational recurrence, for `0<=n<=2d+1`:

```text
(4n+5-2p)^3 g_n =
  4(2n+2-p)(2n+1-p)(4n+3-2p) g_(n-1)
  + (5-2p)^2(6n+5-2p) gamma_n.                    (48.1)
```

Indeed, extract coefficient n from
`S_(p/4)(Gamma²)=-(5/8-p/4)^2(6D+5-2p)Gamma`, using the exact GH-45 operator
`S_h=u(D+2-2h)(D+3/2-2h)(D+7/4-2h)-(D+5/4-2h)^3`, and clear denominators by 64. As before `4n+5-2p` is a p-unit, so gamma and g can be computed to precision p² in O(d) field/ring operations without convolution.

GH-42 established `gamma_r ≡ beta_r(1+pH_r) mod p²`, where
`H_r=sum_(j<r)(4/(8j+13)-1/(4j+4)-1/(4j+3)) mod p`.
Consequently `g_n-v_n` is **provably divisible by p** in R. Define the well-typed first jet

```text
j_n := (g_n-v_n)/p mod p
     = sum_(i+j=n) beta_i beta_j (H_i+H_j) mod p.  (48.2)
```

This is not arbitrary division of two independent residues: use canonical mod-p² representatives after proving the divisibility. For `u=1/9`, recover **all three separate GH-42 observers** via linear-time coefficient passes:

```text
M(u)=sum_(n<d) v_n u^n              mod p²,
W(u)=sum_(n<d) (8n+11)v_n u^n     mod p²,
J(u)=sum_(n<d) (8n+11)j_n u^n    mod p.            (48.3)
```

Using GH-42's already-established full-tail relation, the original `T_d(9) mod p²` is then computable in O(d) arithmetic operations, including forward a/c coefficient passes, without O(d²) pair enumeration:

```text
T_d(9) = B_d(9)Q_d(9) +
 a_d²/9 [W + p(q_p(3)W-4M+J)]    mod p²,
q_p(3)=(3^(p-1)-1)/p.                              (48.4)
```

This is a **new computational implementation** of previously proved source identities, not a new independent evaluation of `W(1/9)`, and not a proof that `T_d(9)=0`.

**Exact p-adic boundary-notch theorem.** For n=d+1,...,2d+1 the entire last term in (47.1) has p-adic valuation exactly 1 except in the following unique case:

```text
p ≡ 11 (mod 12), n=(p-2)/3:
v_p[-16p(d+1)beta_d(6n-4d+1)beta_(n-d-1)] = 2.   (48.5)
```

For `p≡7 mod12`, every such forcing coefficient has valuation 1. Proof: beta_r and d+1 are p-units; in this n interval `2d+7 <= 6n-4d+1 <= 8d+7=2p+1`. The only possible multiple of p is exactly p: `6n-4d+1=p iff n=(p-2)/3`. This is integral and inside the range precisely when p≡2 mod3, i.e. p≡11 mod12 within primes p≡3 mod4. At the exceptional rank the linear factor is exactly p, not p²; hence the valuation is 2. This residue-class-sensitive **single-rank defect** distinguishes p≡11 mod24 from p≡19 mod24 but does not itself prove any special-value congruence.

## Executed exact evidence and honest boundary

Local Python standard-library exact-rational checker verified (47.1) and (48.1), **including terminal n=2d+1**, for every integer d=1..12 (composite p allowed). A separate finite-ring checker ran over all **154 primes** 7<=p<2000, p≡3 mod4, comparing (47.1)/(48.1) coefficient-by-coefficient against independent O(d²) ordered-pair convolutions; verifying every j_n against the harmonic pair sum; checking all n>=d+1 boundary-notch positions; and recovering `T_d(9)` through (48.4) against direct forward c_r summation. All tests passed. Among these 154 primes, exactly 76 are p≡11 mod12 and exhibit the predicted single notch.

Selected exact p² residues `(p; M,W,J,T_d(9), first upper forcing mod p², notch)`:
`(11;0,3,7,11,0,n=3)`, `(19;17,5,15,342,114,none)`, `(23;7,8,0,69,391,n=7)`, `(43;7,11,5,1634,989,none)`, `(67;36,6,39,201,804,none)`. Here M/W/J are reduced mod p as displayed; full W/M are computed mod p² in the checker. The finite tests support the derivation; they are not a formal Lean proof, proof review, native p=373 experiment, or Source admission.

**BRC COMPOSE_APPLIED:** ordered-pair provenance, signed mod-p² weights, precision/valuation, gamma-vs-beta deformation, rank threshold and observer `M/W/J` are preserved. The p-adic notch is an operator/source-specific effect; it is not automatically a native X6/third-slice physical law.

**OPEN next discriminator:** use this linear-time evaluator to search for an **independently proved** finite-field character-sum, CM/Frobenius or nonlocal WZ certificate at u=1/9 yielding a special-value law for W versus BQ. Do not pass GH-39/GH-42 reconstruction `T=T` off as an independent proof of GH-3. Separately type-match the new tangent and notch with GH-20/GH-21's next-digit sources, without merging original W/S or six Hasse ports. Mother D25/LIFT/JT2 OPEN; frozen Source unchanged. No Result, accepted review, authorized run or task closure.
