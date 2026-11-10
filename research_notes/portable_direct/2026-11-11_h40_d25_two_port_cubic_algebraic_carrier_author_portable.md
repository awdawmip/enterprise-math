# D25/LIFT — Common cubic algebraic carrier for the two finite Clausen observation ports

Date: 2026-11-11. **AUTHOR-PROVED formal-power-series identity; EXACT-RATIONAL VERIFIED; UNREVIEWED / NOT_ADMITTED.** This is author-side portable evidence, not a Source CLAIM, Result, native H0/B0 calculation, checkpoint, or independent review.

Mother objective: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION (OPEN). Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific inputs: `awdawmip/enterprise-math@c47e13e4aba0e006366f989d6334d443f6333ae3`. The preceding finite Clausen square-root normal form and Legendre `(-6/p)` 3243-prime certificate are reused, not recredited.

## Theorem (exact in Q[[z]], every m>=0)

Fix e in {0,1}; for integers m>=0 put

```text
K_m^(e)(x) = sum_{k=0}^m binom(m,k) binom(2m+e,k) x^k,
A_m^(e) = K_m^(e)(1/2),
B_m^(e) = (1-6e)K_m^(e)(1/2) + 6 [d/dx K_m^(e)(x)]_{x=1/2}.
```

There is a unique s=s(z) in z Q[[z]] with
`2s=z(1+2s)(1+s)^2`. Write `d=1-s-4s^2`, `theta=z(d/dz)`. Then the ordinary generating series of both observation ports are rational functions of **the same cubic algebraic state** s:

```text
F_e(z)=sum_{m>=0} A_m^(e) z^m = (1+2s)(1+s)^(e+1)/d,
C_e(z)=s(1+2s)(1+s)^e/d,
H_e(z)=sum_{m>=0} B_m^(e) z^m = (1-6e) F_e + 12(2 theta+e) C_e,
theta |_Q(s) = [s(1+2s)(1+s)/d] (d/ds).
```

In explicit derivative-free form:

```text
H_0(z) = (1+s)(1+2s)(1+22s+89s^2+56s^3+16s^4)/d^3,
H_1(z) = (1+s)^2(1+2s)(-5+46s+119s^2-40s^3-80s^4)/d^3.
```

The extension Q(z,s)/Q(z) has degree **at most 3**, since `s` obeys this cubic equation. The branch coordinate e must be preserved to distinguish the two ports; collapsing to a product alone discards the vanishing-port identity.

## Proof

The exact binomial coefficient extraction is

```text
K_m^(e)(x)=[t^m](1+t)^m(1+xt)^(2m+e)
          =[t^m] U_x(t)^m V_e,x(t),
U_x(t)=(1+t)(1+xt)^2,  V_e,x(t)=(1+xt)^e.
```

Formal Lagrange-Bürmann residues imply, for unique T=z U_x(T),

```text
sum_{m>=0} [t^m] U_x(t)^m V_e,x(t) z^m
    = V_e,x(T)/(1-z U'_x(T)).
```

Set `x=1/2` and `T=2s`. The fixed-point equation becomes `2s=z(1+2s)(1+s)^2`; direct differentiation gives

```text
1-z U'_(1/2)(2s) = d/[(1+2s)(1+s)].
```

Consequently the first displayed formula for F_e follows. Differentiating **the original coefficient expression** in x yields

```text
K_m^(e)'(1/2)
=(2m+e)[t^m] U_(1/2)(t)^m V_e,1/2(t) t/(1+t/2).
```

Apply the same residue identity to the marked factor `t/(1+t/2)`. Evaluated at T=2s, it is `2s/(1+s)`, hence its generating function is `2C_e). The factor `2m+e` becomes `(2theta+e)`, proving

```text
sum_m K_m^(e)'(1/2) z^m=2(2theta+e)C_e.
```

Combine with the definition of B, proving the H formula. Log-differentiating the cubic gives `theta=s(1+2s)(1+s)/d * d/ds`; rational simplification gives the two H closed forms. Every denominator has nonzero constant term, so every step is formal and exact, with no convergence assumption.

## Exact author-side checks and BRC observer

The accompanying portable Python verifier, independently of the binomial expressions, recursively builds s and the rational F_e,C_e in Q[[z]] using exact Fraction arithmetic. It checks both A and B against direct binomial sums for e=0,1 and every m=0..50: **204 exact-rational comparisons PASS**. Ten prime examples 5,7,11,13,17,19,23,29,157,373 were additionally evaluated modulo p. In particular the previously reported observations p=157: (A,B)=(0,80), and p=373: (0,171), agree.

Initial coefficients:

```text
F_0 = 1+2z+13z^2/2+95z^3/4+731z^4/8+...
H_0 = 1+14z+181z^2/2+1967z^3/4+20075z^4/8+...
F_1 = 1+5z/2+17z^2/2+253z^3/8+983z^4/8+...
H_1 = -5+11z/2+155z^2/2+4027z^3/8+22301z^4/8+...
```

BRC reuse: the common branch-indexed algebraic carrier (e,s) preserves two distinct rational observer functions. Its reduction at prime p uses the original index `m=floor(p/6)` and e=(p-1-6m)/4, rather than asserting a native crystalline Frobenius. The prior finite `p<=30000` observation that `(-6/p)` selects the vanishing A/B port is not yet a universal theorem. A discriminating next unit is to study the `p`-Cartier coefficient extraction of these two algebraic series under the original prime-index restriction and prove or refute the Legendre selector. The prime hypothesis is substantive: for composite n=65, m=10,e=1, both `2^m A` and `2^m B` are nonzero mod 65 (26 and 5 respectively).

Source continuation `h40-20261111-0440-d25-exact-continuation` was read SUCCEEDED on 2026-11-11 (Asia/Hong_Kong), but `execution_authorized=false`; own `recovery_status` returned `SITE_CONTROL_OWN_ISSUED_SESSION_REQUIRED`. The original Source frontier retains its own 2026-10 Hesse/Green and conditional rank-one contributions; this author-side work is not their completed_units. Native original-class H0/B0, Frobenius direction and normalization remain pending. The historical UR V2 four-file original is still sought at 94,687 bytes with SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`; do not repeat UR mathematics.

Prior author records: `research_notes/portable_direct/2026-11-11_h40_d25_clausen_square_root_normal_form_author_portable.md` and `2026-11-11_h40_d25_chi_minus6_two_port_finite_certificate_author_portable.md`. No prior-art novelty or formal theorem admission is asserted.
