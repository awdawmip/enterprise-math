# D25 AF4 — explicit finite Gauss affine first-jet certificate in the p≡13 mod24 class

Date: 2026-11-09. Continuation of `20261109_onhour_d25_V_clausen_two_residue_cutoff_port.md`; frozen Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. AUTHOR-SIDE EXACT ALGEBRA / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE.

## 1. The new finite first-jet theorem

Fix any prime `p≡13 (mod24)`; write
`a=(5p-1)/8, b=(7p-3)/8, r=5/8, s=7/8, z=1/9`.
Then `0<a<b<p`, and the original Gauss scalar of the 2304 Clausen representation is

`M_p=sum_{k=0}^{p-1}(1/8)_k(3/8)_k z^k/(k!)^2.`

Introduce a **finite affine parameter deformation**, not a native spatial coordinate:

`F_p(X,z)=sum_{k=0}^{p-1}(-a+rX)_k(-b+sX)_k z^k/(k!)^2.`

Because `-a+rp=1/8` and `-b+sp=3/8`, exactly `M_p=F_p(p,1/9)`. Every denominator is a p-unit and a Hasse coefficient expansion yields

`M_p ≡ P_{a,b}(z)+p(L_{a,b}(z)+T_{a,b}(z)) (mod p^2).`

The THREE terms are explicitly:

`P_{a,b}(z)=sum_{k=0}^a binom(a,k)binom(b,k) z^k` (computed mod p²),

`L_{a,b}(z)=-sum_{k=0}^a binom(a,k)binom(b,k) z^k [r(H_a-H_{a-k})+s(H_b-H_{b-k})]` (mod p),

`T_{a,b}(z)=r sum_{k=a+1}^b (-1)^(a+k) a! b! (k-a-1)! z^k/[(b-k)!(k!)^2]` (mod p).

Here `H_n=sum_{j=1}^n 1/j`, `H_0=0`. All displayed factorials and harmonic denominators are below p.

**Proof.** For `k<=a`, both numerator Pochhammer products have no zero at `X=0`; differentiation gives the harmonic logarithmic derivative in L. For `a<k<=b`, the first product has precisely one zero at `j=a`, whose derivative is `r(-1)^a a!(k-a-1)!`; the second has value `(-1)^k b!/(b-k)!`, giving T. For `k>b`, both products contain a zero, so the coefficient is `O(X²)`. Inserting `X=p` and reducing modulo p² proves the identity. No assumed hypergeometric transformation or signed cutoff cancellation is used.

This is a **strictly finite certificate reduction** for the previously tested conjecture `M_p≡0 (mod p²)`. The new exact proposed field identity is

`P_{a,b}(1/9) ≡0 (mod p)` and
`boxed{ P_{a,b}(1/9)/p + L_{a,b}(1/9)+T_{a,b}(1/9) ≡0 (mod p) }.`

The quotient `P/p` is evaluated in `Z_(p)` from the exact integer/rational polynomial modulo p² before reduction. These two identities together are **equivalent** to the p² Gauss congruence for the original finite M, not its all-prime proof.

## 2. Original-coefficient exact checks and individual split observations

The companion integer-only Python script checks the three distinct pieces, the affine Hasse expansion and an independent original `(1/8,3/8)` recurrence modulo p². The equality was checked for **all 22 primes p<=1000 with p≡13 (mod24)**, and the proposed cancellation was observed in each. For p=13,37,61,109,157,181,373:

| p | a,b | P/p mod p | L mod p | T mod p | sum mod p |
|---:|:---|---:|---:|---:|---:|
| 13 | 8,11 | 8 | 6 | 12 | 0 |
| 37 | 23,32 | 15 | 34 | 25 | 0 |
| 61 | 38,53 | 53 | 2 | 6 | 0 |
| 109 | 68,95 | 17 | 91 | 1 | 0 |
| 157 | 98,137 | 108 | 31 | 18 | 0 |
| 181 | 113,158 | 170 | 49 | 143 | 0 |
| 373 | 233,326 | 75 | 66 | 232 | 0 |

The previous separate original Gauss-factor recurrence tested `M_p≡0 mod p²` for all **157 primes p<=10000 with p≡13 (mod24)** (zero exceptions; all 157 also had `H=M+16N` nonzero mod p). This extended evidence has its own coverage; it is not an all-prime proof or a native H0/B0 benchmark. The new full P/L/T first-jet test was run only for the 22 primes <=1000.

## 3. Direct continuation

The next proof obligation is the displayed *binomial-harmonic plus middle-band* cancellation with `a=(5p-1)/8,b=(7p-3)/8,z=1/9`. A finite Jacobi/Fricke transformation or WZ telescoper with explicit endpoint T is a promising test. This keeps the derivative and signed overflow information needed in the AF4 W/V cross-layer interface. For `p≡19 mod24` the preceding p²-termwise Q theorem remains a completed separate result.

The highest-priority original native gap is unaffected: issue #1559, p373 H0/B0 same-class divided-power module `[X]U mod139129`, rank, genuine Frobenius direction/eta, signed kappa/Delta-R and independent reproduction. No native Source CLAIM/run/checkpoint/Result is asserted by this author note.
