# D25 | Exact LIFT-to-half-cutoff repair and Wilson-reflected W216 B2 port (2026-11-02)

**Author-derived exact argument; integer regression; UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT. Not a Source checkpoint or a native H0/B0 experiment.**

Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; scientific input frozen at `c47e13e4aba0e006366f989d6334d443f6333ae3`. Logical Research lane `chatgpt-research-onhour-enterprise-math-20260923` is distinct from maintenance. Already accepted D24 UR/JT0 first-digit is consumed rather than redone.

## 1. Exact original observer

For a target prime `p≡13,19(mod24)`, write `p=6m+1`, `H=(p−1)/2=3m`, and set

```text
B_0=1, B_(k+1)/B_k=(6k+1)(3k+1)/(36(k+1)^2),
g=Σ_(k=0)^(p−1) B_k, h=Σ_(k=0)^(p−1)(12k+1)B_k,
G=g/p, Δ_p=(G*h−1)/p mod p.
w_k=(6k+1)α_W(k), α_W(k)=(2k)!(3k)!/[216^k(k!)^5],
W(n)=Σ_(k=0)^n w_k.
```

The frozen finite Clausen result
`research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_FINITE_CLAUSEN_DERIVATIVE_BRIDGE_RETURN_20260827.md`
defines the original correction

```text
C_r=2^(r−1)((r−1)!)²/[18(5/6)_r(2/3)_r] mod p,
R_p=2 Σ_(i=1)^m B_i Σ_(r=1)^i(1+6(i−r))C_r mod p.
```

It proves the exact rational finite convolution identity `W(p−1)=g*h−T_p` and `T_p≡p²R_p(mod p³)`. The **accepted D24 first-digit** proves `W(p−1)≡p(mod p²)` and `G*h≡1(mod p)`. Consequently, in the precise original scalar observer,

```text
                   Δ_p−R_p ≡ [W(p−1)−p]/p² (mod p).     (1)
```

The divided operations require genuine `G,h mod p²` and `W mod p³`; first-digit mod-p compression alone loses the intended observer.

## 2. Theorem A: exact all-target half-cutoff repair

Put `E=floor((2p−1)/3)=4m`. For `H<k≤E`, let `U_p(k)=p^(−2)α_W(k)∈Z_p^×`, and define the labeled tail port

```text
B2_W(p)=Σ_(k=H+1)^E(6k+1)U_p(k) mod p,
J_H(p)=[W(H)−p]/p² mod p.
```

**Proof:** Legendre's valuation gives `v_p(α_W(k))=floor(2k/p)+floor(3k/p)` for `0≤k<p`. It equals two on `H<k≤E`, and is at least three on `E<k<p`. Thus `W(p−1)−W(H)≡p²B2_W(p)(mod p³)`; the accepted first digit also yields `p² | W(H)−p`. Combining with (1) proves the exact all-target identity

```text
                 Δ_p−R_p ≡ J_H(p)+B2_W(p) (mod p).      (2)
```

Hence the mother target is equivalent, for **both** classes, to a *specific* finite half-truncation certificate:

```text
                 W(H) ≡ p−p²B2_W(p) (mod p³).          (3)
```

The original 2304 stream `s_k=(8k+1)(4k)!/[2304^k(k!)^4]`, `S(n)=Σ_(k=0)^n s_k`, satisfies by Guo–Zudilin, *A q-microscope for supercongruences*, Adv. Math. 346 (2019), Theorem 1.1, `S(H)≡p(−3/p)(mod p³)`. In both target classes `(−3/p)=+1`; therefore (2) can equivalently be written

```text
          Δ_p−R_p ≡ [W(H)−2S(H)+p]/p²+B2_W(p) (mod p). (4)
```

The published result also gives `B2_S=0` (the previously completed source consequence), but **the W216 B2 port is retained**. No auxiliary full-stream equality is silently promoted to the original D25 observer.

## 3. Theorem B: exact Wilson reflection of the W216 B2 port

This statement applies to **every prime p≡1(mod6), p>3**, with `p=6m+1`; it is not contingent on the D24 CM signs. For `1≤r≤m`, put `k=3m+r`, `U_r=p^(−2)α_W(k) mod p`. As `p≤2k,3k<2p`, Wilson's theorem yields

```text
(2k)!/p≡−(2r−1)! (mod p), (3k)!/p≡−(3m+3r−1)! (mod p),
U_r ≡ (2r−1)!(3m+3r−1)!/[216^(3m+r)((3m+r)!)^5] (mod p). (5)
```

Set `ε_p=(6/p)` (Legendre symbol). With `H=(p−1)/2`, Wilson's half-factorial identity `(H!)²≡(−1)^(H+1)(mod p)` and `216^H≡ε_p(mod p)` reduce the initial term to

```text
                         U_1 ≡ ε_p/9 (mod p).          (6)
```

The consecutive factorial ratios in (5), using `3m≡−1/2(mod p)`, simplify to

```text
            U_(r+1)=U_r * r(6r−1)(6r+1)/[9(2r+1)^3] mod p,
                                1≤r<m.              (7)
```

All denominators are units in the stated range. Restoring the *original* weight `6k+1≡6r−2(mod p)`, the exact low-index reflected tail is

```text
     B2_W(p) ≡ Σ_(r=1)^m(6r−2)U_r (mod p), U_1=ε_p/9. (8)
```

This reduces the source-tagged high-valuation W tail to `m=(p−1)/6` finite-field steps and exposes its exact character, valuation and signed weight. As an applied BRC/Enterprise-coordinate observer audit, the source coordinate `k=3m+r` is carried to `r` with model W216, branch `ε_p`, interval, valuation two, and the required divided-digit port retained; dropping B2 before the final observer would not preserve `Δ_p−R_p`.

Together (2)+(8) constitute a **genuinely source-connected equivalent finite certificate**, not a proof of the remaining all-prime cancellation.

## 4. Exact checks (2026-11-02)

An original-coefficient p-adic recurrence checker independently evaluates `g,h,R_p,W(p−1),W(H),S(p−1),S(H),B2_W,J_H`, retaining original denominators and integer p-adic divisions. Across **107 target primes p≤3000**, zero mismatches arose in (1)–(4), (8), and every target `Δ_p−R_p` computed as zero (finite observation only). A second original tail-unit recurrence checked (8) across **all 207 primes p≡1(mod6), p≤3000**. At p=13,19,37,43,373 the 216 and 2304 full/half sums were also recomputed directly using independent integer binomial coefficients instead of the recurrence. All five cross-checks agreed.

| p | R_p | Δ_p | B2_W | J_H | W(H) mod p³ |
|---:|---:|---:|---:|---:|---:|
| 13 | 0 | 0 | 10 | 3 | 520 |
| 19 | 12 | 12 | 9 | 10 | 3629 |
| 37 | 11 | 11 | 20 | 17 | 23310 |
| 43 | 15 | 15 | 35 | 8 | 14835 |
| **373** | **196** | **196** | **266** | **107** | **14887176** |
| 1171 | 0 | 0 | 1048 | 123 | 168663814 |

At p373, `p²=139129`, `G mod p²=65672`, `h mod p²=62835`. Thus `Δ=R=196`, `W(H)=373+107·139129=14887176(mod373³)`, and `J+B2=107+266=373≡0(mod373)`.

**Proof strength:** Theorems A/B are direct exact algebraic identities under the explicitly consumed frozen parents and the cited 2019 theorem. Enumeration is finite regression, not a uniform proof of `J_H+B2_W=0`; the **hard D25 all-prime LIFT remains OPEN**.

## 5. Next unit, native debt and control

Next exact scientific action: derive the divided second digit `J_H` from a *terminating finite* transformation and prove or refute its cancellation with the Wilson-reflected recurrence (7) in both target classes. Preserve original `Δ,R` identity, branch signs, finite cutoff and p-adic valuation. This is more directly tied to the mother goal than enlarging an auxiliary scalar scan.

The **separate original native p373 H0/B0 divided-power experiment** ([support issue #1559](https://github.com/awdawmip/enterprise-math/issues/1559)) remains pending: actual `[X]U mod139129`, module rank, genuine semilinear Frobenius, eta, odd signed Green/Hesse/kappa and independent validation. This note is not that experiment. Gateway 0.6.11 was read-only on this Research client (Site research write grant and executor binding absent). No Source session/claim/run/admission or checkpoint is claimed, no maintenance identity used, no old failed request replayed. Original on-hour research schedule and notifications untouched.

**Source attribution:** Frozen publication/taskbook and frozen Clausen return at `enterprise-math@c47e13e4aba0e006366f989d6334d443f6333ae3`; Guo–Zudilin 2019 above. Author-derived deductions and exact regression are distinct from external theorem and future independent Source acceptance.
