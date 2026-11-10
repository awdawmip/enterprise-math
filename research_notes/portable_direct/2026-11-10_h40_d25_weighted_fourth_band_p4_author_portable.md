# D25/LIFT: fourth p-adic source band of the weighted W observer

**Date:** 2026-11-10. **Scope:** TASK_RESEARCH, author-side portable exact mathematical evidence; `AUTHOR_PROVED / FINITE_EXACT_VERIFIED / UNREVIEWED / NOT_ADMITTED`. Original science is pinned at `awdawmip/enterprise-math@c47e13e4aba0e006366f989d6334d443f6333ae3`.

**Task:** `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; parent `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`. Reuses the previously published weighted-W mod-p³ three-band result without recrediting it.

## Theorem: fourth band and exact finite-field repair coordinate

Let p>=13 be prime, p mod 24 in {13,19}, and m=(p-1)/6. Preserve the full k-labeled original weighted cubic observer

```text
a_0=1
a_(k+1)/a_k = (2k+1)(3k+1)(3k+2) / [36(k+1)^3],  0<=k<p-1
W_p = sum_(k=0)^(p-1) (6k+1)a_k .
```

Let L, M, N and T be the four *exact p-local rational sums* over k in 0..2m, 2m+1..3m, 3m+1..4m, and 4m+1..6m, respectively. Then for **every** such p

```text
W_p = L_p + M_p + N_p + p^3 F_p                 (mod p^4)

F_p = -2 sum_(k=4m+1)^(6m)
    [(6k+1)(2k-p)!(3k-2p)!]/[216^k (k!)^5]     (mod p)

    = -2 sum_(j=1)^(2m)
    [(6j-3)(2m+2j-1)!(3j-2)!]/
    [216^(4m+j) ((4m+j)!)^5]                    (mod p).
```

Every factorial in the right-hand side has argument below p, and every denominator is a p-unit. Thus F_p is an exact finite-field observer repairing the loss of the highest labeled band when the output precision changes from p³ to p⁴.

**Proof.** The original recurrence gives a_k=(2k)!(3k)!/[216^k(k!)^5]. Since k<p, Legendre gives v_p(a_k)=floor(2k/p)+floor(3k/p), which is 0,1,2,3 on the four intervals. For k>4m we have p<=2k<2p and 2p<=3k<3p. Wilson yields (2k)!/p = -(2k-p)! mod p and (3k)!/p² = 2(3k-2p)! mod p. The latter factors into two complete blocks (p-1)! and a factor 2, giving +2. Multiplication gives -2 and hence the first expression for F. Setting k=4m+j and p=6m+1 yields 6k+1=6j-3 modulo p and the second expression. As T is divisible by p³, the four-band congruence follows, with no assumption on the global W supercongruence.

## Exact finite verification

A complete sieve enumerated all **312** primes 13<=p<=10000 in the stated two congruence classes. A modular original recurrence modulo p⁴ computed both W and T; an algebraically distinct method computed F from the displayed factorial expression using factorial/inverse-factorial tables modulo p. Both F values agreed in all 312 cases, and **F was nonzero in all 312**. Each modular recurrence also satisfied W=p mod p³ in this finite range; defining Q_p=(W_p-p)/p³ mod p, **Q was nonzero in all 312**. These are bounded exact computations, not infinite-family nonvanishing theorems.

| p | F_p = T_p/p³ mod p | Q_p=(W_p-p)/p³ mod p | Q_p-F_p mod p |
| ---: | ---: | ---: | ---: |
| 13 | 5 | 9 | 4 |
| 19 | 4 | 12 | 8 |
| 157 | **96** | **151** | **55** |
| 373 | 278 | 228 | 323 |

At p=157 the exact residues modulo 157⁴=607573201 are W=584354000, L+M+N=212844272 and T=371509728=96*157³. A third calculation, with the independent factorial numerator formula modulo p⁴, reconfirmed W and T for p=13,19,157,373.

This distinguishes the new fourth band F_157=96 at p⁴ precision from the *previously established* weighted third-band H_157=98 at p³ precision, and from the ordinary scalar third-band tail t_157=0, frozen reflected R_157=82 and odd Hesse observer. The exact BRC compression interface depends on the declared operation and p-adic precision; total-only reduction at p³ loses a detectable source coordinate at p⁴.

## Reproducibility, provenance and next step

Portable verification files (author-side, not native execution) were prepared as a 3-file package: `2026-11-10_h40_d25_weighted_fourth_band_p4_author_portable.md`, `d25_fourth_band_exact_20261110.py`, `d25_weighted_fourth_band_certificate.json` (all 312 rows). The verifier uses only Python standard-library integers, sieves all eligible primes and checks both independent F calculations by exact equality. The four listed p also passed a third exact factorial-numerator calculation.

Next scientific problem: relate the new Q_p and repair coordinate F_p to a source-preserving finite WZ/telescoping route for W_p=p (mod p³) or the original-class H0/B0 representation, without conflating separate observers. Uniform W congruence proof and native Frobenius operation are not asserted here.

Original UR V2 four-file provenance/writer debt remains separate: exact original target 94687 bytes, SHA256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`; no bundle reconstruction or replacement hash is asserted. This note is GitHub author evidence, not Source task checkpoint, formal Result or independent review.
