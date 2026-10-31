# D25: exact two-zone p² certificate for the 2304 clipped Clausen boundary

2026-10-31. **Status: AUTHOR-SIDE / ALGEBRAIC THEOREM PROVED / FINITE CHECK EXECUTED / UNREVIEWED / NOT_ADMITTED.** No Researcher session, CLAIM, Research-Activity, Result, native Frobenius computation or independent review is implied.

**Parent:** RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; immutable scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3. Consume the earlier exact two-sided Clausen source split from Enterprise Math commit 9619ea46d8db39f496e85737b69ae9f3ba222dd9; do not replace its original 216 model or six original-series ports.

Define beta_k=(1/8)_k(3/8)_k / (9^k(k!)²), and the **signed clipped double boundary**

T_beta,p = Σ_{0≤i,j<p; i+j≥p} [8(i+j)+1] beta_i beta_j.

The preceding exact Clausen identity is B_p=g_beta h_beta−T_beta,p, where B_p=Σ_{k<p}(8k+1)binom(4k,2k)binom(2k,k)²/2304^k, g_beta=Σ beta_k, h_beta=Σ(16k+1)beta_k.

## Proved finite two-zone theorem (all primes p≡5 or 7 mod 8)

Set (n,m)=((5p−1)/8,(7p−3)/8) for p≡5 mod8, or ((5p−3)/8,(7p−1)/8) for p≡7 mod8. Put lambda=5/8, mu=7/8, in Z_(p). Then p/2<n<m<p and {1/8,3/8}={−n+lambda*p,−m+mu*p} as unordered parameters.

For 0≤k≤n define
C_k=binom(n,k)binom(m,k)9^(−k),
E_k=lambda*(H_n−H_(n−k))+mu*(H_m−H_(m−k)),
where H_r=Σ_{j=1}^r 1/j. For n<k≤m define

D_k=lambda*(−1)^(n+k)*n!*(k−n−1)!*m! / ((m−k)!*(k!)²*9^k) mod p.

**Exact coefficient law**, all k<p, in Z_(p)/p²:

beta_k ≡ C_k*(1−p E_k) if k≤n;
beta_k ≡ p D_k if n<k≤m;
beta_k ≡ 0 if k>m.

Define signed weights w(i,j)=8(i+j)+1 and three source-labelled ports:

LL0 = Σ_{i,j≤n;i+j≥p} w(i,j)*C_i*C_j,
LL1 = −2p Σ_{i,j≤n;i+j≥p} w(i,j)*C_i*E_i*C_j,
LM = 2p Σ_{0≤i≤n<j≤m;i+j≥p} w(i,j)*C_i*D_j.

**Theorem:** T_beta,p ≡ LL0+LL1+LM (mod p²), universally for this prime class. LL0 is computed mod p²; the inner sums of LL1, LM need only mod p.

**Proof:** Since beta_k=(-n+lambda*p)_k(-m+mu*p)_k/(9^k(k!)²), for k≤n expand each product term 1−lambda*p/(n−j), 1−mu*p/(m−j); cross terms vanish mod p² and the sums are the stated harmonics. For n<k≤m only the first Pochhammer hits the zero-index j=n, with isolated factor lambda*p. The remaining factors modulo p give lambda*p*(−1)^(n+k)*n!*(k−n−1)!*m!/(m−k)!; divide by the unit factorial/9 denominator to obtain D_k. For k>m both factors hit p, so beta_k vanishes mod p². Substitute into the original clipped two-index sum and keep low/low leading, low/low first-order corrections (factor 2 from symmetry) and low/middle (factor 2 from orientation). Every other contribution has ≥2 powers of p. QED.

Each port has an O(p) terminal-scalar evaluation through separate suffix sums for C_k,k*C_k and D_k,k*D_k. **Observer scope**: this p² terminal scalar does not license quotienting away the signed pair population or higher p³/p⁴, operator or native H0/B0 information.

## Proved complement using published external theorem

If p≡1 or 3 mod8, the two beta valuation jumps occur at ((p−1)/8,(3p−3)/8) or ((p−3)/8,(3p−1)/8), respectively. The second jump index m satisfies 2m<p. Thus any i+j≥p contains at least one beta factor with valuation ≥2, giving **T_beta,p≡0 mod p² termwise**.

Guo and Zudilin, *A q-microscope for supercongruences*, Advances in Mathematics 346 (2019), 329–358, DOI 10.1016/j.aim.2019.02.008, independently proved B_p≡p chi_{−3}(p) (mod p³) for all primes p>3. Combining that published theorem with exact Clausen gives the proved corollary:

**g_beta*h_beta≡p chi_{−3}(p) (mod p²), universally for p≡1 or 3 mod8.**

This is a sourced corollary, **not** an independent proof of Guo–Zudilin.

## Sharper complementary character law: NEW CONJECTURE, NOT PROVED

Finite arithmetic suggests T_beta,p ≡ −p chi_{−3}(p) (mod p²) for p≡5 or 7 mod8. If proved, Guo–Zudilin yields g_beta*h_beta≡0 (mod p²) in those classes. The unproved condition is an explicit signed finite WZ/CM target: LL0+LL1+LM≡−p chi_{−3}(p) (mod p²). Do not erase the unit/unit low port LL0: its individual summands are not p-divisible even though terminal cancellation is observed.

The executed standalone Python file d25_beta_cutoff_p2_harmonic_20261031.py verified the **proved coefficient and three-port identities**, independently of the above conjecture, for all **100 primes p≤1200, p≡5 or7 mod8**, checking every coefficient, the complete signed boundary, and direct numerator/factorial definitions for designated primes. It additionally found the **conjecture held 100/100**, a finite experiment only.

Exact examples (LL0, LL1, LM, total mod p²):
- p=7: (0,7,35,42); conjecture 42.
- p=13: (130,156,39,156); conjecture −13=156 mod169.
- p=23: (92,506,483,23); conjecture 23.
- p=37: (925,185,222,1332); conjecture −37=1332 mod1369.
- p=373: (105186,96980,75719,138756); conjecture −373=138756 mod139129.

## Unfinished parent and Source continuation

The original target A_p≡p (mod p³), p≡13,19 (mod24), is **OPEN**; stronger A_p−2B_p+p chi_{−3}(p)≡0 (mod p⁴) is **UNPROVED**. This new p² beta transfer does not prove either. For p≡13 mod24 it supplies an exact three-port finite target for the outstanding beta-tail character claim; for p≡19 mod24 termwise vanishing was already proved. Next: find a class-aware finite WZ/CM certificate for LL0+LL1+LM and then integrate the original 216 I0–I2 with completed I3–I5 and both signed two-sided tails, **without** claiming a substitute native experiment.

Native support #1559 fixed p=373 same-original-class H0/B0 divided power, [X]U mod139129, rank, semilinear Frobenius, odd signed Green/Hesse, kappa and independent reproduction remains NOT_EXECUTED/PENDING_OWNER; rightful owner/authorized native executor or designated maintainer must run the unchanged input and validate exact outputs.

Research lane historical recovery at awdawmip/kimi-query-bridge#6632 does not establish a current winning CLAIM/run. Original request research-onhour-20261031-0205-dispatch-r15 at #6633 is terminal FAILED UPSTREAM_CODE_REVIEW_REQUIRED; gateway v0.6.11 on 2026-10-31 had research_authority_granted=false, executor_binding_configured=false, control CODE_REVIEW_REQUIRED. Do not replay rejected operations or borrow maintenance lane. Author-side evidence publication is distinct from Source checkpoint, registration, independent review or Result admission. P000/ACTIVE worldview and frozen scientific Source pin unchanged; no scheduler changes.