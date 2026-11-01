# D25 — 2304 Clausen source split at the 13/19 boundary and a proved comparator

Date 2026-11-02 +08:00. TASK_RESEARCH portable author-side mathematics. D25 Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged; Research lane chatgpt-research-hourly-enterprise-math-20260923 separate from maintenance. AUTHOR-DERIVED / EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING.

## 1. Exact Clausen cutoff

Define the formal rational series F(z)=2F1(1/8,3/8;1;z)=sum f_k z^k and V(z)=3F2(1/4,1/2,3/4;1,1;z)=sum v_k z^k. By the classical Clausen identity, F(z)^2=V(z). Let F_{<p}, V_{<p} truncate at k=p-1 for each prime p>=5. The signed finite-square cutoff K_p=F_{<p}²-V_{<p} has support exactly among degrees p,...,2p-2 (some coefficients possibly vanish). Its first omitted coefficient has the exact rational identity

    [z^p]K_p = v_p - 2 f_p.                              (1)

Here v_p is a hypergeometric coefficient, not the p-adic valuation notation.

**Theorem (first-boundary residue).** For every prime p>=5,

    [z^p]K_p ≡ 0   (mod p), p mod8 = 1 or 3;
    [z^p]K_p ≡ -1  (mod p), p mod8 = 5 or 7.

**Proof.** For 1<=a<=d with p∤d, choose the unique integer α in [1,d] satisfying αp≡a mod d. In the rising factorial (a/d)_p exactly one factor has numerator αp; the other p-1 numerators permute F_p^×. Wilson plus Fermat gives

    (a/d)_p / p! ≡ α/d (mod p).                          (2)

For 1/4,1/2,3/4, the three α factors multiply to 3 in either class p mod4, hence v_p≡3/32 modp. For 1/8,3/8, the two α factors multiply to 3 for p mod8=1,3 and to 35 for p mod8=5,7, hence f_p≡3/64 or 35/64. Substitution into (1) yields 0 or (3-35)/32=-1, as required. The divisions by p in (2) are genuine integer p-factor cancellations. QED.

**Stronger p mod8 =3 theorem.** For every prime p=8r+3>=11, the entire signed cutoff satisfies

    K_p(z) belongs to p² Z_(p)[z].                      (3)

Proof: the exact coefficient recurrence for F gives v_p(f_k)=0 for k<=r, =1 for r<k<=3r+1, =2 for k>3r+1, all k<p. The first p-multiple in 8j+3 is at j=r and in 8j+1 at j=3r+1. For i+j>=p, it is impossible for both i,j<=3r+1 since 2(3r+1)=6r+2<8r+3=p. Thus every convolution term f_i f_j at degrees >=p is p²-divisible; QED.

For the frozen target p mod24=13, p mod8=5: [z^p]K_p=-1 (modp) is a p-unit and the high cutoff CANNOT be discarded even at modp precision. For p mod24=19, p mod8=3: the entire K_p is divisible by p², although it can contribute at p³ precision. This is a new exact provenance and observer-sensitive split across the target classes; it is an external number-theoretic auxiliary claim, not a native X6 transfer.

## 2. Proven literature comparator reduces the original arithmetic question

Victor J. W. Guo and Wadim Zudilin, A q-microscope for supercongruences, Adv. Math. 346 (2019), 329–358, arXiv:1803.01830v6, prove the following p³ supercongruence for all primes p>3:

    T_p ≡ p * (-3/p) (mod p³),
    T_p = sum_(k=0)^(p-1) (8k+1)*binom(4k,2k)*binom(2k,k)^2 / 2304^k.

The published denominator 2^(8k)3^(2k) equals 2304^k. Its terms are exactly (8k+1) times the V-coefficient at z=1/9 (ratio (4k+1)(2k+1)(4k+3)/(288(k+1)^3)). Thus T_p=[(8θ+1)V_{<p}](1/9) with θ=z d/dz.

The frozen mother target concerns original S_p=sum_(k=0)^(p-1)(6k+1)*binom(2k,k)^2*binom(3k,k)/216^k. For all p mod24 in {13,19}, quadratic character (-3/p)=+1, so the published theorem proves the exact equivalence

    S_p ≡ p (mod p³)   iff   S_p - T_p ≡ 0 (mod p³).      (4)

Equation (4) is a **proved reduction**, not a proof of the right-hand modular bridge. A useful BRC fidelity identity preserving all signed source channels is

    T_p=[(8θ+1)F_{<p}²](1/9) - [(8θ+1)K_p](1/9).

In the p13 class, the first omitted coefficient is already a p-unit, so a transfer replacing T_p by the uncorrected square is mathematically invalid. In the p19 class, the cutoff is p²-small but remains a possible second-digit term.

This exact literature comparator plus class-dependent cutoff gives a focused alternative to attempting the universal 216 congruence from scratch. It does not replace the same-original-class native H0/B0 experiment.

## 3. Executed exact checks, scope and next scientific unit

The local standard-library checker d25_2304_clausen_boundary_20261102.py verified the first-boundary theorem for all 428 primes 5<=p<=3000; it also checked the entire high tail modp² for p mod8=3, p<=200. Examples: p13 cutoff first coefficient -1 mod13, p19 0 mod19, p37 -1 mod37, p43 0 mod43, p373 -1 mod373. A second exact modular script compared the *two weighted sums* at all 166 primes 5<=p<=997; every case obeyed S_p=T_p=(-3/p)p modp³. The p4 difference is nonzero: (S_13-T_13)/13³=11 mod13, (S_19-T_19)/19³=6 mod19, and (S_373-T_373)/373³=114 mod373. These computations validate only finite inputs.

**Next precise open math:** prove the bridge S_p-T_p≡0 modp³ for p mod24=13,19, retaining the proved p13/p19 cutoff distinction, potential CM-isogeny trace and/or WZ summation. A complementary route is the existing 216 first-digit Green criterion 9E_pH_p=2J_p+3 modp and its second-digit signed Clausen tail C_p with real integer carry. Do not reprove previous full Green/Legendre/CM selector units. No all-primes S_p conclusion has yet been admitted.

Original control evidence (2026-11-02): native gateway 0.6.11 research_authority_granted=false, executor_binding_configured=false, CODE_REVIEW_REQUIRED / UPSTREAM_CODE_REVIEW_REQUIRED. Historical Research recovery awdawmip/kimi-query-bridge#6637 read-only; exact continuation #6638 terminal FAILED and not replayed; owner issue awdawmip/enterprise-math#1558; native p373 H0/B0 capability issue #1559. No new CLAIM/open/Source checkpoint/Result/review, nor new Research-Activity registration, is claimed. Frozen P000, ACTIVE worldview, mathematical Source pin and existing timer and notification behavior unchanged.