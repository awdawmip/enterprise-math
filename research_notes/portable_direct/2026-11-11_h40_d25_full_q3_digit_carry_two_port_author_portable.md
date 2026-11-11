# D25/LIFT: full finite Clausen two-port reconstruction modulo q³ by factorial-unit digit carries

**Date:** 2026-11-11. **Classification:** AUTHOR-PROVED / EXACT-INTEGER-VERIFIED / UNREVIEWED / NOT_ADMITTED. This is portable author mathematical evidence, not a native Source Task checkpoint or Result.

**Parent:** RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT (TP2-B6F4FC938FF94941C1B7). Frozen science pin c47e13e4aba0e006366f989d6334d443f6333ae3. This work completes the auxiliary q³ reconstruction left after the prior q² Lucas carry jet and q³ joint-borrow proof. It does not claim priority over classical generalized Lucas/Granville-style congruences.

## Theorem 1: all-digit binomial reconstruction modulo q³

Let q≥5 be prime; n≥k≥0 and s=n−k. Set M=q³ and E_q(x)=Σ_{j≥1}⌊x/q^j⌋. Write x_j=⌊x/q^j⌋ and a_j(x)=x_j mod q. Let H_a=Σ_{i=1}^{a}i⁻¹, H_a^(2)=Σ_{i=1}^{a}i⁻², H_0=H_0^(2)=0 (these fractions have unit denominators modulo M). Define

J_a(t)=1+qtH_a+q²t²(H_a²−H_a^(2))/2 (mod M),

V_q(x)=((q−1)!)^{E_q(x)} ∏_{j≥0} (a_j(x)! J_{a_j(x)}(x_{j+1})) (mod M).

The product is finite, and V_q(x) is a unit. For e=E_q(n)−E_q(k)−E_q(n−k), the **exact universal congruence** is

**binom(n,k) ≡ q^e V_q(n) V_q(k)⁻¹ V_q(n−k)⁻¹ (mod q³).**

For e≥3 the right side is zero. The valuation e records total base-q carries, not just a one-digit borrow.

**Proof.** Set U_q(x!)=x!/q^{E_q(x)}. For x=qN+a with 0≤a<q, partition the integer factorial exactly into multiples of q, N full blocks of q−1 units, and the terminal a units:

U_q((qN+a)!)=U_q(N!) ∏_{r=0}^{N−1}∏_{i=1}^{q−1}(qr+i) ∏_{i=1}^{a}(qN+i).

For q≥5 the finite-field square-sum identity implies Σ_{i=1}^{q−1} i⁻²≡0 (mod q). Pairing i with q−i then gives Σ_{i=1}^{q−1}i⁻¹≡0 (mod q²). Expanding elementary symmetric functions to degree two proves

∏_{i=1}^{q−1}(qr+i) ≡ (q−1)! [1+qrH_{q−1}+(qr)²(H_{q−1}²−H_{q−1}^(2))/2] ≡ (q−1)! (mod q³).

The terminal partial block is a!J_a(N) modulo q³. Hence

U_q((qN+a)!) ≡ U_q(N!) ((q−1)!)^N a! J_a(N) (mod q³).

Iterate down all base-q digits. The summed exponent Σ N at successive levels is E_q(x), yielding U_q(x!)≡V_q(x) (mod q³). Applying this unit congruence to the exact factorial quotient for binom(n,k) proves the theorem. QED.

## Theorem 2: two source-distinct Clausen ports

For every m≥0, ε∈{0,1}, let

F(X)=Σ_{k=0}^m binom(m,k)binom(2m+ε,k) X^k,
A=F(1/2), B=(1−6ε)F(1/2)+6F'(1/2).

For each k set n₁=m, n₂=2m+ε, eᵢ=E_q(nᵢ)−E_q(k)−E_q(nᵢ−k), and uᵢ=V_q(nᵢ)/[V_q(k)V_q(nᵢ−k)] modulo q³. Then

**A ≡ Σ_{k≤m, e₁+e₂<3} q^{e₁+e₂} 2^(−k) u₁u₂ (mod q³),**

**B ≡ Σ_{k≤m, e₁+e₂<3} (1−6ε+12k) q^{e₁+e₂} 2^(−k)u₁u₂ (mod q³).**

These identities follow termwise from Theorem 1, with all inverses taken on units. They simultaneously supply previously missing second-order no-borrow corrections, first-order single-borrow refinements and the earlier joint-borrow sector. The valuation classes are e₁+e₂=0 (full unit q³), =1 (unit q²), =2 (unit q), and ≥3 (zero). At valuation two retain (2,0), (1,1), and (0,2) as different source sectors.

The provenance-aware BRC observation state is (ε,k,e₁,e₂,u₁,u₂,2^(−k),1−6ε+12k); reducing it to (A,B) is valid for the declared auxiliary q³ observer, with the graded source state retained for later precision changes.

## Exact integer witnesses

At (q,m,ε)=(7,8,0), source sectors (e₁,e₂)=(0,0),(1,0),(1,1) yield (A,B)=(88,315),(154,77),(49,147) respectively modulo 343. Their sum is (291,196) modulo 343. Its q² projection is (46,0) modulo 49. The joint-borrow row reproduces the previous independently recorded (49,147).

At (13,28,0), sectors (0,0),(1,0),(1,1) contribute (650,481),(1898,1079),(1183,507) modulo 2197, total (1534,2067). At (5,26,1), sector (2,0) contributes (100,50), while (1,1) contributes (0,75), modulo 125; total (5,91).

## Verification and frontiers

An independent local Python verifier compared the above q-adic unit-jet construction against Python's exact integer binomial coefficients across **149,188** exhaustively enumerated pairs (n,k), 0≤k≤n≤150, for q in {5,7,11,13,17,19,23,29,31,37,41,43,47}. This included **68,473** nonzero q-adic valuation cases, including **830** with valuation≥3. Another **336** two-port comparisons across both ε branches and digit boundaries passed, including the displayed carry-sector witnesses. The complete executed verifier and machine-readable certificate are in the separately supplied portable bundle.

**Exact next original-objective dependency:** recover authenticated original-class H0/B0 divided-power data, [X]U mod p², and source-native Frobenius direction/normalization; explicitly connect the auxiliary ports to kappa and Δ_p−R_p at the frozen scientific pin. The missing UR V2 bundle has historical target size 94,687 bytes and SHA-256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76; do not redo already-completed UR mathematics.

No CLAIM, Result freeze, independent review, native experiment or canonical mathematical admission is asserted by this note.
