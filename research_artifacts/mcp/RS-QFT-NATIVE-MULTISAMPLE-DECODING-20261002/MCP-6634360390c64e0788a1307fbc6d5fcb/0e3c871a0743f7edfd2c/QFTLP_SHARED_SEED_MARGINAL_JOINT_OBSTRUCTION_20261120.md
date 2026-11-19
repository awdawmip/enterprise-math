# QFT-LP | Exact shared-seed marginal-to-joint obstruction (author finite witness)

Task: RS-QFT-NATIVE-MULTISAMPLE-DECODING-20261002
Author: EM-X6-C7A253. Symbolic probability witness, **not** a native BRC trajectory or independent mathematical review.

Fix an order r and distinguishable idealized peak labels z_k indexed by residues k in Z/rZ. Give every sample the SAME hidden random index K uniform on Z/rZ, Y_1=...=Y_m=z_K, m>=2. Each single-register marginal is exactly uniform: Pr(Y_i=z_k)=1/r for all i,k. The joint law is concentrated on the diagonal, not a product measure.

For ideal peak-to-reduced-denominator reconstruction, d_i=r/gcd(k_i,r), and lcm(d_1,...,d_m)=r/gcd(r,k_1,...,k_m). In this shared-index construction, the probability that the LCM equals r is

   Pr(gcd(K,r)=1)=phi(r)/r=product_{p|r}(1-1/p).

If m samples instead used *independent* uniform residue indices, the corresponding probability would be

   product_{p|r}(1-p^(-m)).

Concrete exact finite witness: r=6, m=2. Shared K gives 2/6=1/3 exact-order LCM success; independent K1,K2 gives (1-1/4)(1-1/9)=2/3. All four one-register marginals (two experiments times two positions) are identical, uniform on six peak labels. Thus even exact agreement of ALL individual peak marginals cannot justify an independence-based two-sample success guarantee.

For r with more distinct prime factors, phi(r)/r can shrink; the multishot benefit from independent reinitialization is material. This witness is an abstract correlated-output law with genuine elementary counting and does NOT show the frozen native BRC model can produce this exact law. It motivates using the actual native joint law or a condition on every conditional sampling kernel. The companion conditional peak-floor note proves a joint lower bound without assuming sample independence but leaves its native hypothesis unverified.

Evidence class: AUTHOR_SYMBOLIC_EXACT_COUNT / UNREVIEWED / NOT_ADMITTED.
