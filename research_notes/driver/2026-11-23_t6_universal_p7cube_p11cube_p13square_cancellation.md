# T6: unconditional cancellation of 7³, 11³ and 13² denominator layers from H₀–H₄

Date: 2026-11-23 Asia/Taipei. Research contribution: RESEARCH_DRIVER **EM-DVR-DEBB5E**, original own session `MCP-9b4714dc46b948afa4875a86c89c713c`. This is new mathematics with direct finite integer verification, **not** a formal Native Review or accepted Result. Earlier p17² and p19² author/reviewer scopes are unchanged.

## Exact theorem (original T6 model)

Let A and B be *finite multisets* of positive integers `e>=1`. On **each** side the sum of all exponents is at most 2331. Put
`H_k(X)=sum_{e in X} (e/(e+1))^k`.
If `H_k(A)=H_k(B)` for **k=0,1,2,3,4**, then, for every integer denominator `d>=2`, the multiplicity of `e=d-1` is identical in A and B whenever

- `7^3 | d` (all six denominators `343*j`, `1<=j<=6`);
- `11^3 | d` (the sole denominator 1331);
- `13^2 | d` (all thirteen denominators `169*j`, `1<=j<=13`).

No maximal-prime, p-primary moment-isolation, distinctness, single-atom, or sign restriction is assumed. Thus the conclusion applies to original T6 equality of H₀,...,H₆. This *removes specific high-valuation denominator layers*, not all maximal-p=13,11,7 cases or the global T6 obstruction.

## Common  p-adic reduction

Define `S_k(X)=sum_{e in X}(e+1)^(-k)`. The triangular binomial identity
`H_k=sum_{i=0}^k (-1)^i binom(k,i)S_i`, with `S_0=H_0`, implies equality `S_k(A)=S_k(B)` for `0<=k<=4`.

For a prime p and highest remaining exact denominator valuation v, multiply `S_k(A)-S_k(B)=0` by `p^(vk)` and reduce modulo p in the localization `Z_(p)`. Any denominator with valuation strictly less than v disappears. Exact-valuation-v denominators `p^v*j`, with `p∤j`, contribute
`sum_j (m_A(p^v*j)-m_B(p^v*j))*j^(-k) = 0 mod p`.
Every per-side vector `m=(m_j)` lies in the finite nonnegative profile set
`sum_j (p^v*j-1)*m_j <=2331`.

### 7³: three modular moments are injective

Since `7^4=2401>2332`, the only denominators with 7-adic valuation at least three are `343*j`, j=1,...,6. Exact recursion gives **30** feasible per-side profiles. A separate generating-function coefficient DP returns the same 30.

For signatures `(sum_j m_j*j^(-k) mod 7)_{1<=k<=K}`, the exact enumeration yields:

| K | distinct signatures | unordered colliding distinct profile pairs |
|---|---:|---:|
| 1 | 7 | 52 |
| 2 | 29 | 1 |
| 3 | **30** | **0** |

Thus `S_1,S_2,S_3` force equality of all six multiplicities. It suffices to assume H₀–H₃ for this subclaim.

### 11³ and 13³: a single maximal-valuation atom cancels

The *only* admissible denominator divisible by 11³ is 1331, and by 13³ is 2197: twice either exponent `d-1` exceeds 2331. Thus each side can contain at most one such atom. Multiply S₁ equality by `p^3` and reduce modulo p: its signed multiplicity is 0 mod p and lies in `{-1,0,1}`, so it is exactly zero. These two cancellations already follow from H₀ and H₁ alone.

### 13²: the sole modular collision is ruled out by exact S₂

Having removed denominator 2197 equally from A and B, the remaining denominators divisible by 13² are precisely `169*j`, `1<=j<=12`. Their per-side weights are `169*j-1` under the **original full-side mass budget**. Complete recursive enumeration gives **372** profiles, independently agreeing with the coefficient sum of
`prod_{j=1}^{12}(1-z^(169*j-1))^(-1)` through degree 2331.

The `F_13` signature `(sum_j m_j*j^(-k))_{1<=k<=K}` has:

| K | distinct signatures | unordered colliding distinct profile pairs |
|---|---:|---:|
| 1 | 13 | 5152 |
| 2 | 161 | 319 |
| 3 | 355 | 17 |
| 4 | **371** | **1** |

The *unique* collision at K=4 is the empty profile versus **13 copies of denominator 169**. Hence equality of `S_1,...,S_4` implies either exact profile equality, or a signed discrepancy of `±13` copies at d=169 and zero discrepancy at all other 13² denominators.

The latter cannot satisfy exact S₂ equality: its contribution to `S_2(A)-S_2(B)` is
`±13/169² = ±1/13³`. After cancellation of the 13³ atom and all other 13² profiles, **all remaining denominators have 13-adic valuation at most one**, so their reciprocal-square contributions have valuation at least -2. Multiplying exact S₂ equality by 13³ and reducing modulo 13 gives `±1=0 mod 13`, impossible. Thus the profiles coincide and *all* 13² denominators cancel, including the already handled 2197.

## Reproducible finite arithmetic and provenance

A short standard-library Python checker independently uses two different counting mechanisms—complete multiplicity recursion and generating-function DP—then enumerates every signature fiber and checks the exact unique 13-collision. All arithmetic is integer or finite-field modular inverse, with **no floating-point thresholds**.

Checker: `research_checks/T6_P7_CUBE_P13_SQUARE_EXACT_PROFILE_20261123.py`. In the original Driver research turn its exact local execution printed the expected 30 / 372 profiles and all stated signature counts, ending `PASS`. The arithmetic proof and program must be retained together; repository publication/readback is separate from local execution.

A repository keyword check found no same-title p13-square cancellation record before this publication; this is **not** a claim that all earlier research is exhaustively absent.

This extends, without rewriting, the prior universal 17² cancellation result (Driver r499) and independent p19² audit (original contributor EM-X6-FB6990). The remaining valuation-one and lower-prime cross-residue interactions still require their actual mixed-moment and mass-budget proof. This publication is **one new theorem family / one completed research subunit**; Native Review acceptance 0, Result acceptance 0, formal Task completion 0, mother objective completion 0.
