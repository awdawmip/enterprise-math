# D25 AF4 — original 2304 finite Clausen cutoff splits the two frozen prime classes

Date: 2026-11-09. Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Logical Research lane `chatgpt-research-onhour-enterprise-math-20260923` distinct from maintenance. AUTHOR-SIDE / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE.

## 1. Exact paired Clausen scalar interface for the original 2304 model

Let `p>3` be prime, `d_n=(1/8)_n(3/8)_n/(9^n(n!)^2)`, `0<=n<p`, and

`M=sum d_n, N=sum n d_n, H=M+16N,`

`Q=sum_{0<=i,j<p, i+j>=p}(1+8(i+j))d_i d_j.`

All expressions are in `Z_(p)`; retain the ordered pair indices, coefficient signs, and full cutoff. The classical Clausen identity, applied coefficientwise at `z=1/9`, is

`(_2F1(1/8,3/8;1;z))^2 = _3F2(1/4,1/2,3/4;1,1;z).`

For every `0<=n<p`, convolution `sum_{i+j=n}d_i d_j` is precisely the original 2304 coefficient `binom(4n,2n)binom(2n,n)^2/2304^n`. Consequently the **exact rational finite-cutoff identity** is

`V_p = M(M+16N)-Q = M H-Q.`

The overflow Q must remain a separately typed signed observer; this is the 2304 counterpart of the *already known* 216 source Clausen port. The formula is a new application to the frozen two-model AF4 bridge, not a new derivation of Clausen.

## 2. Proved, all-prime p≡19 (mod24) strong valuation lemma

For `n<p` the p-adic valuation is

`v_p(d_n) = 1_{n>a_1}+1_{n>a_3}`

with the unique roots `a_1,a_3 in [0,p-1]` satisfying `8a_1+1=0, 8a_3+3=0 (mod p)`. For `p≡19 mod24` (therefore `p≡3 mod8`),

`a_1=(3p-1)/8,  a_3=(p-3)/8,`

both strictly smaller than `(p+1)/2`. Every term in the triangle `i+j>=p` has `max(i,j)>=(p+1)/2`, hence at least one factor d is divisible by `p^2`. Thus **term by term**, with no cancellation assumption,

`Q≡0 (mod p^2),  p≡19 (mod24).`

Use Guo--Zudilin, *A q-microscope for supercongruences*, Advances in Mathematics **346** (2019), 329–358, doi:10.1016/j.aim.2019.02.008: for `p>3`, the ORIGINAL `V_p≡p(-3/p) (mod p^3)`. Here `(-3/p)=1`. Combining with the exact finite Clausen identity yields the **all-prime original-carrier theorem**

`boxed{ M(M+16N)≡p (mod p^2), p≡19 (mod24). }`

This is an explicit first-digit scalar port in the second frozen residue class. It says the product has valuation exactly one, without silently selecting which factor supplies the p.

## 3. Complementary p≡13 (mod24): a concrete different proof obligation

For `p≡13 mod24` (`p≡5 mod8`), the roots instead are

`a_1=(5p-1)/8,  a_3=(7p-3)/8,`

both greater than `(p+1)/2`. The triangle term `i=(p-1)/2, j=(p+1)/2` has `v_p(d_i d_j)=0` and weight `1+8p`, a p-unit. Therefore the p^2 **termwise** argument of the other residue class is genuinely unavailable here. The total Q exhibits nontrivial signed cancellation.

New precise **CONJECTURE** for this class:

`M≡0 (mod p^2),  Q≡-p (mod p^2), p≡13 (mod24).`

The first congruence implies the second through `V_p≡p (mod p^3)` and `V_p=MH-Q`. Conversely, if the further hypothesis `H mod p !=0` holds, the second implies the first, but no uniform H-unit theorem is claimed here. This is an exact Gauss-factor certificate candidate rather than a substitution for the native H0/B0 experiment.

## 4. Executed exact finite evidence, original coefficient crosscheck

The companion Python 3 script uses only integer arithmetic and modular inversion at p-unit denominators. It independently implements (A) the Gauss d-recursion and ordered-pair overflow and (B) the original 2304 binomial factorial recurrence, all modulo `p^3`. On **all 45 primes p<=1000 with p≡13 or19 (mod24)** it verified Clausen reconstruction, the published `V_p≡p mod p^3`, and:
- `p≡19`: 23/23, `Q mod p^2=0` (consistent with the proved lemma);
- `p≡13`: 22/22, `M mod p^2=0`, `Q mod p^2=-p` (finite evidence for the conjecture).

| p | residue mod24 | M mod p² | H mod p | Q mod p² | V mod p³ |
|---:|---:|---:|---:|---:|---:|
| 13 | 13 | 0 | 7 | 156 | 13 |
| 19 | 19 | 171 | 17 | 0 | 19 |
| 37 | 13 | 0 | 5 | 1332 | 37 |
| 43 | 19 | 860 | 28 | 0 | 43 |
| 61 | 13 | 0 | 59 | 3660 | 61 |
| 67 | 19 | 938 | 24 | 0 | 67 |
| 373 | 13 | 0 | 80 | 138756 | 373 |

For the key p373 original native benchmark, this remains an *ordinary finite hypergeometric computation*, **not** its H0/B0 divided-power [X]U modulo 139129. It introduces no H0/B0 rank, semilinear Frobenius direction, eta, odd kappa or Delta-R readout. Support issue #1559 remains PENDING_OWNER until an actual executor provides the original module and independent reproduction.

## 5. Value and next smallest exact action

The original W-side finite Clausen overflow Q_W is already Source-aligned; this new V-side identity exposes a **different** cutoff mechanism between the two frozen residue classes, which must not be erased in an AF4 WZ/Fricke certificate. Next: derive an exact p-adic Gauss two-factor deformation or finite WZ identity proving `M≡0 (mod p^2)` for p≡13 mod24, or find an exact counterexample, while keeping the proven p≡19 first-digit product port. Then insert the V-side Q carrier into the existing low/high fourth-digit carry with W, without recasting that as the native H0/B0 benchmark.

Source native CLAIM/run/Result are not asserted. Authored under the existing noncanonical `research_notes/portable_direct` surface; provenance and published theorem strength remain separate. No scheduler mutation.
