# D25 / LIFT: same-source Jacobi parameter-jet / reflected-corner bridge
Date 2026-10-25; author-checked portable mathematics, UNREVIEWED / NOT_ADMITTED. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged.

Let p=6m+1>=7 be prime, N=p-1=6m, and b_n(x)=(-x)_n(-2x)_n/(n!)^2. Let Phi(x,z)=sum_{n=0}^N b_n(x)z^n; F_i(z)=partial_x^i Phi(m,z) (i=0,1,2), and u_n=b_n(m), v_n=b_n'(m), w_n=b_n''(m)/2. Put theta=z d/dz, A_i=F_i(1/2), H_i=[(1+12theta)F_i](1/2). Original signed source r_n=2^(-n)b_n(-1/6), g=sum r_n, d=sum nr_n, h=g+12d, Q=sum_{0<=j,k<p;j+k>=p}(6(j+k)+1)r_jr_k.

**Theorem A (all p=1 mod6).** For 0<=n<p,
b_n(-1/6)=u_n-(p/6)v_n+(p^2/36)w_n mod p^3. Hence
g=A_0-(p/6)A_1+(p^2/72)A_2 mod p^3,
h=H_0-(p/6)H_1+(p^2/72)H_2 mod p^3.
Furthermore u_n=0 for n>m, v_n=0 for n>2m and the valuations of r_n in the three rank layers n<=m, m<n<=2m, 2m<n<p are exactly 0,1,2.

Proof: -1/6=m-p/6 over Q. Every b_n(x) is a polynomial over Z_(p) for n<p, so its Taylor expansion around m, truncated at quadratic order, has error divisible by p^3. Each of (-m)_n, (-2m)_n acquires its distinct simple zero on crossing its index threshold; all remaining nonzero factors are p-units. Weighted summation gives the g/h identities.

**Theorem B (all p=1 mod6).** The original signed ordered cutoff corner satisfies
Q/p^2 = T_jet mod p,
T_jet := (1/18) sum_{j=1}^m sum_{ell=1}^j (6(j-ell)+1)u_j w_{p-ell}/2^(j+p-ell) mod p.
Proof: only low/extreme ordered pairs have combined valuation 2 and can cross j+k>=p. In the reflected port r_{p-ell}/p^2=w_{p-ell}/(36*2^(p-ell)) mod p, while r_j=u_j/2^j mod p. Reversing the two indices produces 2/36=1/18 and signed weight 6(j-ell)+1 mod p. Other cutoff terms vanish mod p^3.

**Theorem C (hard target exact reduction, not its all-prime solution).** For p=13,19 mod24, consume the independently accepted first-digit certificate p|g and gh=p mod p^2. Write
g_01=A_0-(p/6)A_1, h_01=H_0-(p/6)H_1,
B_01=(g_01 h_01-p)/p^2 mod p (integral by the first-digit condition).
With Delta=(gh-p)/p^2 and R_ref=Q/p^2 mod p,
Delta-R_ref = B_01 + A_2 H_0/72 - T_jet mod p.
Proof: multiply Theorem A, use g_01=0 mod p so its product with p^2 H_2/72 disappears mod p^3, divide by p^2 and invoke B. The original target is therefore equivalent to the explicit Jacobi-only finite-field equation B_01+A_2 H_0/72=T_jet. It is NOT proved for all p here.

**Exact witness.** For p=13, the three residues (B_01, second-jet correction, T_jet) are (4,9,0); p=19 gives (1,11,12); p=373 gives (184,12,196). The missing second jet is genuinely nonzero for p=13 and 19 even though T_13=0, so dropping the entire second-jet branch loses the declared next observer. It can vanish for some primes (p=43), so no uniform nonvanishing is claimed.

Author checker used an independent original-source recurrence, terminating Taylor-jet recurrence and the full signed ordered Q double sum. All 35 p=1 mod6 primes <=373 passed the identities; among these, all 19 p=13 or 19 mod24 cases passed the hard-target bridge. Finite zeros are NOT a uniform proof. Local reproducer: d25_jacobi_translation_bridge_check.py, available with the present run; remote script publication pending. BRC COMPOSE_APPLIED to the rank/derivative/valuation/ordered-sign carrier; no native BRC or original CM/Frobenius experiment performed.

**Next:** apply the inherited genuine terminating second-Jacobi-jet differential equation with its nonzero cutoff forcing to B_01+A_2 H_0/72-T_jet, aiming at a uniform signed telescoper; alternatively obtain authenticated same-original-class H0/B0, [X]U mod p^2 and Frobenius/kappa map. Preserve existing Source checkpoint (SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED), do-not-repeat, contributor history, frozen pin. This note is NOT a native checkpoint. Existing cross-epoch continuation predecessor mismatch is tracked in issue #1558; no winning claim/open in this run.