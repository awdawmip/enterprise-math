# R762DP — Exact BRC content corridors for a two-coordinate endpoint observer over all 3-power moduli

Date: 2026-11-18 (Asia/Shanghai). Task: `RS-X6-TRIADIC-CLOSURE-DYNAMICS` / `TP2-8B7E13C5904A2D6F1142`.
Researcher: `EM-X6-3050F6`, own previous Source session `MCP-4b2d70a97f594366a7c94a0f8b45df38`; independent review: `NOT_REVIEWED`.

## Immutable sources, observation scope, and provenance

Frozen P000 V5 `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json`; taskbook `research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md@e3f42efac29a2da2d95be391f3231a664e2fade0`; prior R762DN full three-coordinate theorem `4e9001fe28f8bc19ce93e5a1f87d842a241d7756`, R762DO diagonal theorem `39be21e5f4f3cc245f71ef5fa4e013d4ffaa6020`.

Start from six *named positive-weight BRC microbranches* of the R762DI–DO candidate additive area model:

`(0,0,0), (1,0,0), (0,0,1), (1,1,0), (0,1,1), (1,1,1)`.

Their complete three-coordinate group-ring polynomial is
`P(X,Y,Z)=1+X+Z+XY+YZ+XYZ`.
Declare the endpoint observer `pi_XZ(u,v,w)=(u,w)` and only the resulting endpoint joint distribution under common additive branch updates. In its target group ring `R_Q = Z[X,Z]/(X^Q-1,Z^Q-1)`, the *projected positive histogram*, including all six multiplicities, is

`F(X,Z)=P(X,1,Z)=1+2X+2Z+XZ`.

Here `X,Z` denote **two retained area observation coordinates of a three-coordinate residual carrier**, never a two-dimensional native spatial plane. The ambient X6 six-axis ontology, third area coordinate, signed Port/source and full named history remain in the full state. No primitive `TRIADIC_CLOSURE_E` event is inferred from this candidate observer. For a physical q-area paired-triad return, the normalized Q=q/gcd(q,2), and the algebraic exponent n counts individual microbranch factors; a complete paired block has n=2k.

For n≥0 let `C_Q(n;u,w)=[X^u Z^w]F^n`, nonnegative integers summing to `6^n`, and
`c_Q^{XZ}(n)=gcd_{u,w in C_Q} C_Q(n;u,w)`. Exactly reproducing **only** this endpoint probability distribution with equiprobable deterministic initial seeds requires
`M_Q^{XZ}(n)=6^n/c_Q^{XZ}(n)`.

## Theorem: two full and one partial sharp 3-adic corridor

For every a≥2, Q=3^a, d=Q/3 and n≥0:

1. **Initial corridor:** if `0≤n<3d`, then `c_Q^{XZ}(n)=1`.
2. **First nontrivial corridor:** if `3d≤n<5d`, then `c_Q^{XZ}(n)=9`.
3. **Second exact corridor:** if `6d≤n<7d`, then `c_Q^{XZ}(n)=81`.

Thus `M_Q^{XZ}(n)=6^n`, `6^n/9`, or `6^n/81`, respectively, on these exact parameter ranges. In particular, on the interval `3d≤n<4d`, R762DN gives **full** three-coordinate `c_Q^{full}(n)=3`, whereas this two-coordinate observer gives `c_Q^{XZ}(n)=9`. This is a sharp additional factor-three endpoint seed reduction for the declared observer.

The as-yet-unproved intervals `5d≤n<6d` and `n≥7d` are deliberately not covered by the theorem. Experiments below report some values in those ranges as experiments only. The case Q=3 is excluded from this statement.

### Proof A: exact characteristic-three filtration before n=Q

Put `x=X-1`, `z=Z-1`. In the *integer* cyclic group ring
`F=6+3x+3z+xz=xz+3(2+x+z)`.
Reducing modulo 3 gives
`A=F_3[x,z]/(x^Q,z^Q)`, with `F mod 3=xz`, since
`(1+x)^Q-1=x^Q` in characteristic three.

Therefore `F^n mod 3 = x^n z^n`, which is nonzero for `0≤n<Q`. The content of `F^n` has no factor 3 in this interval.

### Proof B: one exact Frobenius leading term at n=Q

For `Q=3^a`, a≥2, expand `F^Q=(xz+3(2+x+z))^Q`. The terms with j≥1 copies of the factor 3 have 3-adic coefficient valuation at least 3:
- j=1: `v_3(binomial(Q,1)·3)=a+1≥3`.
- j=2: `v_3(binomial(Q,2)·3^2)=a+2≥4` (Q odd).
- j≥3: the explicit `3^j` suffices.

Consequently `F^Q ≡ x^Q z^Q (mod 27 R_Q)`.

In the one-variable cyclic integer ring `Z[T]/(T^Q-1)`, the congruence
`(T-1)^Q/3 ≡ T^d-T^{2d} (mod 3)`
holds because the terms j=0 and j=Q cancel by `T^Q=1`; the only binomial terms with valuation exactly one have indices j=d,2d, with respective coefficients +1,-1 after dividing by 3 and reducing mod 3. More precisely `v_3(binomial(3^a,j))=a-v_3(j)` for `0<j<3^a`, and the extremal coefficients reduce by Lucas congruences.

It follows that `F^Q` is coefficientwise divisible by 9 and

`F^Q/9 ≡ D:=(X^d-X^{2d})(Z^d-Z^{2d}) (mod 3)`.  (★)

In `A=F_3[x,z]/(x^{3d},z^{3d})`,
`X^d-X^{2d}=-x^d(1+x^d)`; hence
`D=x^d z^d (1+x^d)(1+z^d)`.
Both factors `1+x^d` and `1+z^d` are units (they have constant term 1). The identity (★) therefore contains a nonzero leading source-residual, not just divisibility.

### Proof C: two sharp corridors

For 0≤r<2d, multiply (★) by F^r and reduce modulo 3:
`F^{Q+r}/9 ≡ x^{d+r}z^{d+r}(1+x^d)(1+z^d) (mod 3)`.
This is nonzero precisely for `d+r<3d`, so its coefficientwise 3-adic order is *exactly two* throughout `Q≤n<Q+2d=5d`.

Similarly, squaring the exact identity `F^Q=9(D+3W)` and multiplying by F^r gives, for 0≤r<d,
`F^{2Q+r}/81 ≡ D^2 x^r z^r = x^{2d+r}z^{2d+r}(1+x^d)^2(1+z^d)^2 (mod 3)`.
It is nonzero as `2d+r<3d`. This proves *exactly four* 3-adic powers for `2Q≤n<2Q+d=7d`.

### Proof D: the gcd has no hidden factor 2

All coefficient sums are `F(1,1)^n=6^n`, so every prime divisor of the coefficient gcd divides 6. For odd Q, the finite group algebra `F_2[C_Q^2]` is semisimple and reduced (group order odd; equivalently `X^Q-1`, `Z^Q-1` are separable). Modulo 2, `F=1+XZ`, a nonzero group-algebra element for Q≥9. It has no nilpotent power, so `F^n` is not identically zero modulo 2 for any n≥1. Thus 2 never divides the content. Combine with Proofs A–C. QED.

## Exact author verification and known limits

Companion `R762DP_VERIFY.py` uses exact integer positive BRC convolution with four *aggregated multiplicity groups* `[(0,0,1),(1,0,2),(0,1,2),(1,1,1)]`, corresponding exactly to the original six named branches. It checks:
- all n=1..21 for Q=9, n=1..63 for Q=27, n=1..189 for Q=81;
- coefficient sum equals exactly 6^n at every step;
- the theorem across 17, 53 and 161 covered nonzero exponents respectively (231 theorem checks);
- the full `F^Q/9 mod 3` table equals the four-term D in each Q.

All checks PASS. Observed outside the theorem: at `n=7d` the gcd is `729` for Q=9,27,81; this is a finite experimental lead, not an all-a theorem. Independent mathematical review: `NOT_REVIEWED`. No proof formalization or native triad-event licence is claimed.

## Next exact research

1. Analyze the `5d≤n<6d` corridor, where the first leading term D vanishes, by obtaining the next 3-adic graded piece of F^Q.
2. Extend the `n=7d` experimental content `729` to a universal theorem or construct a counterexample.
3. Compare diagonal (R762DO), two-coordinate (this note), full three-coordinate (R762DN) exact seed costs while preserving the full joint histogram and source/Port provenance for any future operations that can observe them.
4. Obtain authenticated original `TRIADIC_CLOSURE_E` Cell/Link/Port event predicates and the V17/V29/V39 native signed transports before claiming any safe native compression.

The source proof and tests are author-produced and retain their exact stated scope.