# D25 — signed AF4 mirror-jet decomposition and finite Abel boundary

Date: 2026-11-09; task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; frozen science `c47e13e4aba0e006366f989d6334d443f6333ae3`; research conversation `chatgpt-research-onhour-enterprise-math-20260923`. **AUTHOR-PROVED ALGEBRA + EXACT FINITE CHECK; UNREVIEWED / NOT_ADMITTED / NOT_NATIVE.**

## Input and exact observation type

Consume, without reproving, the just-saved all-prime individual complementary first jets in `20261109_onhour_d25_WV_individual_mirror_firstjets_signed_AF4.md` at immutable commit `29efa1a4a745bab7ca1a079ed1331e5107ea94f9`. Original coefficients `A_n,C_n`, actual complete cutoffs `0<=n<p`, exact signed weights `6n+1,8n+1`, and p-adic unit provenance remain unchanged.

For every prime `p>3` let `I_A={q:p/3<q<p/2}`, `I_C={q:p/4<q<p/2}`, `a_q=A_q/p`, `c_q=C_q/p` in `Z/p²Z`, and

```text
  b_A(q) = (36 q³ a_q)^(-1) (mod p²),
  b_C(q) = (288 q³ c_q)^(-1) (mod p²).
```

The previous result supplies `J_A(q),J_C(q)` in `F_p`. Distinguish (i) the base `b`, (ii) first-jet harmonic/Fermat correction, and (iii) correction from the *original signed weights* at index `p-q`.

## Theorem: exact fourth-digit decomposition of both signed grade-two tails

For `X=A,C` use `w_A=6,w_C=8`, `I_X` as above, and `b_X,J_X`. In `Z/p²Z`, put

```text
  B_X  = sum_{q in I_X} (1-w_X q)b_X(q)               (mod p²),
  Z_X  = sum_{q in I_X} (1-w_X q)b_X(q)J_X(q)         (mod p),
  D_X  = w_X sum_{q in I_X} b_X(q)                    (mod p).
```

Then for the *original weighted* grade-two contribution `T2_X`,

```text
                  T2_X / p² ≡ B_X + p(Z_X+D_X)       (mod p²).
```

This follows by substituting the exact complement product
`X_{p-q}/p² = (d_X q³ (X_q/p))^{-1}(1+pJ_X(q)) mod p²`,
with `d_A=36,d_C=288`, into `(w_X(p-q)+1)X_{p-q}`. The multiplication retains `1-w_X q + w_X p` literally. In particular, `pD_X` is a true fourth-digit contribution that disappears if the original weight is prematurely reduced modulo `p`. The affine AF4 grade-two contribution is `(B_A-2B_C)+p[(Z_A-2Z_C)+(D_A-2D_C)] mod p²`.

## Theorem: rational first differences, exact Abel decomposition

For adjacent integers `q,q+1` *both inside* the applicable interval, the first-jet differences simplify to

```text
  J_A(q+1)-J_A(q)
    ≡ 2/(2q+1)+3/(3q+1)+3/(3q+2)-3/q        (mod p),

  J_C(q+1)-J_C(q)
    ≡ 4/(4q+1)+4/(4q+2)+4/(4q+3)-3/q        (mod p).
```

Proof: take successive harmonic differences in `J_A,J_C`; the respective Fermat quotients cancel, `2/(2q+2)=1/(q+1)`, `3/(3q+3)=1/(q+1)`, `4/(4q+4)=1/(q+1)`, and the remaining `q+1` fractions combine to `-3/q`. Every denominator is a `p`-unit on the stated internal adjacent ranges. Their difference also recovers the previously known ratio-jet kernel `-5(2q+1)/((3q+1)(3q+2)(4q+1)(4q+3))`, preserving its earlier provenance.

For either `X`, write the contiguous interval as `a<=q<=b`, set `g_X(q)=(1-w_X q)(b_X(q) mod p)` and `P_X(q)=sum_{r=a}^q g_X(r)` in `F_p`. Exact finite Abel summation gives

```text
  Z_X = P_X(b) J_X(b)
        - sum_{q=a}^{b-1} P_X(q)[J_X(q+1)-J_X(q)]     (mod p).
```

This is a *genuine signed boundary-plus-rational-kernel expression* for the first-jet portion of the actual AF4 grade-two tail; it is not yet a telescoping certificate for `W_p-2V_p+pχ` in full.

## Exact calculations and difference from prior work

All 46 primes `5<=p<=211` plus `373` pass the adjacent-index rational-difference and Abel identities using the independently executed original-coefficient data. The signed decomposition was separately checked on 8 primes `5,7,13,19,37,43,73,373`, with the full original grade-two tail as its target, not a synthetic target.

At `p=373`, the three components `(B_X,Z_X,D_X)` are
`A=(122610,61,168)` and `C=(96980,216,131)`, and
`T2_A/p²=68898, T2_C/p²=87282` modulo `139129`. The original affine signed tail is `33463` modulo `139129`. In the Abel split, `Z_A=193-132=61 mod373`, `Z_C=0-157=216 mod373`.

At `p=13`: `(B_A,Z_A,D_A)=(88,9,3)`, `(B_C,Z_C,D_C)=(117,3,4)`, affine grade-two unit `166 mod169`. At `p=19`: `(351,18,10)`, `(0,8,17)`, affine unit `294 mod361`.

This advances the direct AF4 additive target by isolating precisely the signed-operator boundary and rational first-jet prefix terms from one already-proved low-index mirror. It **does not** prove the all-prime zero/first-grade cancellation, universal AF4 or the frozen parent LIFT; the original same-class p373 H0/B0 `[X]U mod139129` and signed native `κ,Δ-R` remain unexecuted (#1559).

## Next exact research dependency

Compare these explicitly computed `B,Z,D` carriers to the original zero/first-grade contribution modulo `p^4` at `p=13,19,373`. Seek a common finite Abel/WZ boundary with the *same original cutoffs and weights*; a valid universal cancellation needs a proof of its remaining boundary equality in both frozen residue classes. Native evidence remains a distinct current support demand with no assigned executor.
