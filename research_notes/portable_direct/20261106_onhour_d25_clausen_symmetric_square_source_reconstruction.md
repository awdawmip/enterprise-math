# D25: Exact finite Clausen symmetric-square with source-resolved signed cutoff

2026-11-06. AUTHOR-PROVED exact algebra / FINITE-VERIFIED / UNREVIEWED / NOT_ADMITTED. SECOND-DIGIT-LIFT publication TP2-B6F4FC938FF94941C1B7, frozen Source c47e13e4aba0e006366f989d6334d443f6333ae3. Consumes existing exact Gauss finite endpoints at commit 19b484a9449ef9e01b630d89123dba943be80ce0, and this run's coupled Green concomitant at 7c61f348f08d5f2ee41231d153b02be269654b3d.

## Exact finite 216-operator source theorem

For every integer m>=1, p=6m+1 (primality not needed for the exact identity), define rational
`d_0=1; d_(i+1)/d_i=(6i+1)(3i+1)/(36(i+1)^2)` for 0<=i<m,
`e_1=1/10; e_(r+1)/e_r=36r^2/((6r+5)(3r+2))` for 1<=r<m.
Put D(z)=sum_(i=0)^m d_i z^i, V(z)=sum_(r=1)^m e_r z^(-r), H(z)=D(z)V(z), theta=z d/dz, and

`L2=36theta^2-z(6theta+1)(3theta+1)`,
`L3=36theta^3-z(2theta+1)(3theta+1)(3theta+2)`.

The input equations are `L2 D=-A z^(m+1)` with `A=p(3m+1)d_m` and `L2 V=-1+B z^(-m)` with `B=36m^2 e_m`.

**New exact theorem in Q[z,z^-1]**:

```
L3 H=-3 theta D+B z^(-m)(3theta-m)D
      -A z^(m+1)(m+1+3theta)V.                           (C1)
```

Proof: for any Laurent polynomials f,g, by expansion on monomials `z^i,z^j`, the exact bilinear Clausen symmetric-square product rule is
```
L3(fg)=theta((L2 f)g+(L2 g)f)
       +2*((L2 f)theta(g)+(L2 g)theta(f)).
```
The z^(i+j) coefficient matches 36(i+j)^3 by the binomial identity. The z^(i+j+1) coefficient matches by
`(i+j+2j+1)(6i+1)(3i+1)+(i+j+2i+1)(6j+1)(3j+1)=(2(i+j)+1)(3(i+j)+1)(3(i+j)+2)`.
Bilinearity proves the operator rule, and substituting the two *already-proved* finite endpoint equations yields (C1). L3 is precisely the original 216 factorial-coefficient recurrence operator, for `a_n=(2n)!(3n)!/[216^n(n!)^5]`; thus the complementary cross-product belongs to the same original third-order operator family, with explicit inhomogeneous source.

Define `c_k=sum_(i-r=k)d_i e_r` with d,e zero-extended outside their finite ranges. The coefficient recurrence **for every integer k** is
```
36k^3 c_k-(2k-1)(3k-2)(3k-1)c_(k-1)
=-3k d_k+B(3k+2m)d_(k+m)
 -A(3k-2m-2)e_(m+1-k).                                  (C2)
```
Its three source populations remain distinct: low `-3k d_k`, complementary top `B` and low cutoff `A=p(3m+1)d_m`, including the latter's p-adic valuation one.

## Exact source-to-signed-observer reconstruction

Because `c_m=0`, for k=m,m-1,...,1 compute
```
c_(k-1)=[36k^3 c_k-source_k]/[(2k-1)(3k-2)(3k-1)].
```
This is one-dimensional, has no undefined k=0 division, and recovers the **original signed triangular observer**
`J_m=sum_(k=0)^(m-1)(1+6k)c_k`.
For primes p=6m+1, each denominator (2k-1)(3k-2)(3k-1) is a p-unit for 1<=k<=m; recurrence is valid mod p^2. This is the completed source-certified second-port relation required after the earlier concomitant: the whole signed J is recovered from original-class 216 operator sources, without replacing the triangle by a square or erasing odd/paired information.

## Executed checks and source ablation

Self-contained standard-library script directly forms all labeled pairs (i,r), independently derives c_k backwards from (C2), and compares **every coefficient** exactly for rational m=1..8 and modulo p^2 for **all 80** primes p=6m+1<=997. All checks pass. Signed J residues: p13=0, p19=6, p67=44, p373=98 mod p.

A controlled diagnostic drops *only* the valuation-one A source while keeping all other terms fixed, and reconstructs J mod p^2. At p19, full J=120, ablated=234 (true-minus-ablated divided by p is 13 mod19). At p373, full J=78428, ablated=135497 (discrepancy/p=220 mod373). Thus homogeneous low-cutoff simplification discards a genuine second digit. Since frozen W_p mod p^3 uses J only modulo p, these ablations demonstrate the **scope-specific transport information loss**, not a proof or refutation of the frozen full-prime supercongruence.

## Unfinished mother target and independent native benchmark

The frozen mother condition remains `Delta_p-R_p=0 modp` for p≡13,19 mod24, equivalently the already proved scalar interface
`24(S_p/p)M_(2,p)-(p/3)(S_p/p)^2=1+2pJ_p (mod p^2)`.
Next precise research unit: compare the source terms in (C2) with the original *full* 216 weighted W_p and Gauss moment/parameter-jet sources, preserving the nonzero signed p19/p373 cutoffs; prove uniform cancellation or establish a genuine input-scoped counterexample. Original p373 same-class divided-power H0/B0 [X]U, Frobenius direction/eta, rank, original odd Green/Hesse, kappa and independent replication are NOT_EXECUTED/PENDING_OWNER in https://github.com/awdawmip/enterprise-math/issues/1559. This portable author result is not a Source-native CLAIM/run/Result or independent review; old staging sources remain separate.
