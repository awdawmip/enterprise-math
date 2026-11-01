# D25 SECOND-DIGIT-LIFT: exact signed beta / CM-Wronskian lift duality with universal −2

2026-11-01 Asia/Hong_Kong. **AUTHOR-SIDE CONDITIONAL COMPOSITION OF EXPLICIT EARLIER LEMMAS + NEW PROVED TRANSFER LAW / EXECUTED EXACT FINITE CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NATIVE_NOT_RUN.**

Mother `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` unchanged. This ordinary Research lane is `chatgpt-research-onhour-enterprise-math-20260923`, not any hourly/maintenance owner. The Wronskian/Frobenius moment premise below comes from **another author-side research lane**, GLOBAL_KNOWLEDGE journal commit `6ba6e88d79fdf8bd631f1d127e35774fc7b83a9d` (2026-11-01 12:20+08); its separate affine-fiber note is `59047e95917578f32bf5f56061663514733436da`. Reused and attributed, never presented as independently reviewed or newly owned here. Our preceding original signed LL two-port is in project commit `50c53dd6f57d8beccc8c18794d24ad7c7f3edf37`.

## New cross-observer theorem (exact arithmetic, conditional on named source premises)

Let prime p≡13 (mod24), p>=13, h=(p−1)/2, t=(p−5)/8, a=(5p−1)/8, and rational `lambda=1/9 in Z_(p)`. Put

`F_p(z)=sum_{k=0}^{p−1} ((1/8)_k(3/8)_k)/(k!)² z^k`, `H_p(z)=F_p(z)+16z F'_p(z)`.

Retain the *actual original* 2304 model at general argument z:

`B_p(z)=sum_{k=0}^{p−1} (8k+1)((1/4)_k(1/2)_k(3/4)_k)/(k!)³ z^k`;

`gamma_k(z)=((1/8)_k(3/8)_k)/(k!)² z^k`;

`T_p(z)=sum_{0<=i,j<p; i+j>=p} (8(i+j)+1) gamma_i(z)gamma_j(z)`.

The weighted Clausen coefficient identity gives the **exact polynomial equality** `B_p(z)+T_p(z)=F_p(z)H_p(z)`, retaining the original signed clipping and both orientations.

For the finite-field Jacobi reduction define

`Q_p(z)=sum_{j=0}^t (-1)^j binom(t,j)binom(a+j,j)z^j`,
`V_p(0)=0`, `V'_p(z)=−(1+3z)(1−z)^h Q_p(z)^2/4` in `F_p[z]`.
The denominator `4(j+1)` in the coefficient-by-coefficient primitive is a p-unit because `deg V_p< p`. Denote `lambda_bar=lambda mod p`. Consume the earlier **author-side / unreviewed** CM selector and simple-root claims:
`Q_p(lambda_bar)=0`, `Q'_p(lambda_bar) != 0`,
`F_p(z)=(1−z)^(h+1)Q_p(z) (mod p)`.
For every `z in Z_(p)` satisfying `z≡lambda_bar (mod p)`, define the retained Wronskian observer

```text
M_p(z) = 8 lambda_bar (1−lambda_bar)^(h+2)
         Q'_p(lambda_bar) [Q_p(z)/p]
         − V_p(lambda_bar) + 5 lambda_bar      (mod p).
```

The bracket `[Q_p(z)/p]` is division in Z_(p) **before** reducing modulo p, and is defined by the stated simple-root condition. The earlier author's Wronskian theorem, with its essential nonzero Frobenius coefficient **−5 z^p**, gives the precise input interface

```text
M_p(z) = 8 lambda_bar (1−lambda_bar) Q'_p(lambda_bar)
         [F_p(z)/p]            (mod p).
```

**New exact bridge and nonzero affine covariance**, for each such p and every p-adic lift z:

```text
D_p(z):=[B_p(z)+T_p(z)]/p    (mod p)
      = −2 M_p(z)            (mod p),

D_p(z+pδ)−D_p(z)
      = −16 δ lambda_bar (1−lambda_bar)^(h+2)
         Q'_p(lambda_bar)^2  (mod p),       δ in F_p.
```

The affine coefficient is **nonzero**, as both lambda_bar, 1−lambda_bar, and Q' are p-units. These formulas are genuinely p-adic *lift-sensitive*, not zero-only matches. The −2 is uniform over the full target prime class and does not depend on p.

**Proof of the −2 factor.** For all lifts of the same root, `p|F_p(z)` and the exact Clausen polynomial identity makes `D_p(z)=H_p(z)[F_p(z)/p]`. Differentiate the mod-p Jacobi factorization at its simple root to get

`H_p(z)≡16 lambda_bar(1−lambda_bar)^(h+1)Q'_p(lambda_bar) (mod p)`.

Compare to the earlier Wronskian interface to obtain
`D_p(z)=2(1−lambda_bar)^h M_p(z)`. As `1−lambda_bar=8/9` and `p≡13(mod24)` implies Legendre (2/p)=−1, Euler's criterion gives `(8/9)^h=−1 (mod p)`; hence `D_p=−2M_p`. Differentiating the exact first-order `Q_p(z+pδ)/p=Q_p(z)/p+δQ'_p(lambda_bar)` proves the affine law and nonvanishing. QED.

## Connection to the original fixed rational 2304 input, retaining each source

At the *distinguished rational lift* `z=lambda=1/9`, the published Guo–Zudilin congruence gives `B_p(lambda)≡p χ_(−3)(p) (mod p²)` with `χ_(−3)(p)=+1`. The previously proved valuation bands give `T_p(lambda)≡T_LL+T_LM (mod p²)`. The new source-preserving LL theorem gives
`T_LL/p = L_p(C²)/p+2L_p(C E) (mod p)`; the previous LM theorem supplies `C_LM=T_LM/p (mod p)`.
Consequently the *identical original signed first-carry obstruction* has an entirely different CM-moment readout:

```text
L_p(C²)/p + 2 L_p(C E) + C_LM + 1
       = −2 M_p(1/9)           (mod p),  p≡13 (mod24).
```

The **universal zero** of either side is OPEN. A proof of `M_p(1/9)=0` in the actual rational p-adic coordinate, with its `Q_p(1/9)/p` and −5λ ports, would prove the 13-class signed beta first-carry cancellation. It would **not alone** prove the mother weighted216 `A_p≡p(modp³)`; that still requires original 216 `Delta_p−R_p` integration. When z is moved to z+pδ, keep **B_p(z) and T_p(z) both changed**; substituting the fixed `pχ` for `B_p(z)` outside z=1/9 is invalid.

## Independent, discriminating integer execution

Executed `research_notes/portable_direct/d25_ll_cm_moment_bridge_20261101.py` with standard-library exact modular integers. For each of p=13,37,61,109,373 and each lift `z=1/9+pδ mod p²` for δ∈{0,1,2,7}, it constructs Q,V by independent integer binomial polynomial algebra, reconstructs the **original** Gauss and 3F2 coefficient recurrences, directly evaluates **both** the original weighted B(z) and **signed clipped T(z)** using an independent all-indices suffix sum, checks exact `B+T=FH modp²`, nonzero H, Wronskian M, and `D=−2M`. **20/20** exact cases passed.

Nonzero witnesses (δ=1):
- p=13: `B=156`, `T=65` modulo 169, `D=(B+T)/13=4`, `M=11`, and `−2·11=4 mod13`.
- p=37: `B=740`, `T=37` modulo 1369, `D=21`, `M=8`, `−16=21 mod37`.
- p=373: `B=119733`, `T=110035` modulo 139129, `D=243`, `M=65`, `−130=243 mod373`.

At δ=0 the same cases have `D=M=0` as observed in finite tests; the **nonzero shifted witnesses** check an informative coefficient rather than a vacuous 0=0. Neither finite check proves `M_p(1/9)=0` for all target primes.

**BRC COMPOSE_APPLIED:** retain original low/low, low/middle, complete clipped coefficient indices, sign/orientation, B(z), H(z), and rational-lift CM moment with independent observer/operation labels. The proven −2 scalar transport is valid for this designated `D=[B+T]/p` readout only. In particular there is **no** permission to discard the separate B/T or native H0/B0 ports.

**Next smallest proof action:** seek a source-justified finite CM/adjoint or Frobenius normalization that proves `M_p(1/9)=0` for every p≡13(mod24), respecting `Q_p(1/9)/p`, `V_p(1/9)`, the **−5λ boundary**, and the rational rather than arbitrary residue lift. Then return to original 216 `Delta−R`. Native p=373 original-class H0/B0 divided-power, rank, semilinear Frobenius and odd Green/Hesse, kappa and independent replication remain NOT_RUN / PENDING_OWNER (issue #1559). This calculation does not replace them.

Formal Source client remains read-only (Gateway 0.6.11 `research_authority_granted=false`); original request `research-onhour-20261031-0205-dispatch-r15` still scoped `CONTROL_REQUEST_NOT_FOUND`, and no new own CLAIM/open/checkpoint/Result was asserted. Existing private staging remains independent; P000/ACTIVE worldview, frozen source pin and scheduled task settings remain unchanged.
