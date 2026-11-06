# D25: Exact 216 weighted-prefix Green transfer for the signed Clausen boundary

2026-11-06. AUTHOR-PROVED exact finite theorem / FINITE-VERIFIED / UNREVIEWED / NOT_ADMITTED. Original SECOND-DIGIT-LIFT publication TP2-B6F4FC938FF94941C1B7 and frozen scientific Source c47e13e4aba0e006366f989d6334d443f6333ae3. Consumes (not re-crediting) the new finite 216 Clausen symmetric-square source identity in commit 42adace766ea6df565554dcc8a75d2c4394d2b77.

## Exact 216 weighted-prefix transfer theorem

For any integer m>=1 put p=6m+1 (primality is unnecessary for the exact identity). Define rational Gauss low coefficients
`d_0=1`, `d_(i+1)/d_i=(6i+1)(3i+1)/(36(i+1)^2)` (0<=i<m); complementary coefficients
`e_1=1/10`, `e_(r+1)/e_r=36r^2/((6r+5)(3r+2))` (1<=r<m).
Use original 216 model `a_0=1`, `a_t/a_(t-1)=(2t-1)(3t-2)(3t-1)/(36t^3)`.
Let `P_t=sum_(k=0)^(t-1)(6k+1)a_k` be the *original* finite 216 weighted prefix (t=1,...,m); `A=p(3m+1)d_m`.

**New exact Q identity** for the signed original triangular boundary
`J_m=sum_(1<=r<=i<=m)(1+6(i-r))d_i e_r`:

```
J_m = sum_(t=1)^m P_t/(36t^3 a_t) *
               [3t d_t + A(3t-2m-2)e_(m+1-t)].                 (T)
```

**Proof.** The exact finite 216-operator coefficient equation for `c_k=sum_(i-r=k)d_i e_r` (from the already-proved bilinear Clausen source identity) reads, for 1<=k<=m,
```
36k^3 c_k-(2k-1)(3k-2)(3k-1)c_(k-1)
 = -3k d_k-A(3k-2m-2)e_(m+1-k).
```
The complementary top source in the full Laurent equation is supported on k<=0; its absence here is **a support restriction**, not an erasure of the joint source. Divide by `36k^3 a_k`, using `36k^3 a_k=(2k-1)(3k-2)(3k-1)a_(k-1)`, to obtain
`c_k/a_k-c_(k-1)/a_(k-1)=[-3k d_k-A(3k-2m-2)e_(m+1-k)]/(36k^3 a_k)`.
As `c_m=0`, telescoping gives
`c_k/a_k=sum_(t=k+1)^m[3t d_t+A(3t-2m-2)e_(m+1-t)]/(36t^3 a_t)`.
Multiply by `(6k+1)a_k`, sum for k=0..m-1, interchange two finite sums, and observe that the inner sum is the original P_t. This proves (T) for every m>=1, without interpolation or a conjectural bridge.

This **source-to-original-216-prefix** formula is a direct combinatorial bridge between the signed Clausen correction and the original 216 weighted sum. It retains every original index/sign and separates a p-unit bulk term from the valuation-one p-adic low-endpoint source.

## Exact executed arithmetic

Independent standard-library code computes the same J twice, by the direct labeled pair sum and by (T). The tests run exact rational Fraction arithmetic for m=1..8 and modular arithmetic modulo p^2 for all **80** primes p≡1 mod6, p<=997, with zero failures. Representative [p,J modp²,bulk modp²,low endpoint modp²]:
[13,104,130,143]; [19,120,234,247]; [67,2121,446,1675]; [373,78428,135497,82060].
For p19, 234+247≡120 mod361; for p373, 135497+82060≡78428 mod139129. These bulk values also equal the preceding low-source ablation readouts, identifying precisely the removed contribution. The original frozen W_p modulo p^3 uses J only modp; this p² split is an exact transfer certificate, not completion of the full uniform supercongruence.

## Next exact research action and native benchmark separation

Combine (T) with original full 216 weighted W_p and the already derived Gauss parameter/moment correction, seek a finite WZ or hypergeometric cancellation proof of `Delta_p-R_p=0 modp` for all primes p≡13,19 mod24. The candidate must retain nonzero signed J19=6 and J373=98, and both source branches. The original *same original class* p373 divided-power H0/B0 [X]U mod139129, Frobenius rank/direction/eta, odd Green/Hesse, kappa/Delta-R and independent replication still require an authorized native evaluator: https://github.com/awdawmip/enterprise-math/issues/1559 (OPEN/PENDING_OWNER on current read). No Source CLAiM/run/Result/admission or independent review is asserted; old staging sources remain separate.
