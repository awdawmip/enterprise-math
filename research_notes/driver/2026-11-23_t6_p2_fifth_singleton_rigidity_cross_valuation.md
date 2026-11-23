# T6: exact-ν2(d)=5 singleton rigidity from two mixed valuation moments

Date: 2026-11-23 (Asia/Taipei). Independent scoped mathematical derivation by the existing RESEARCH_DRIVER **EM-DVR-DEBB5E**; original public session **MCP-9b4714dc46b948afa4875a86c89c713c**. Formal Native Review/Result not implied.

## Statement

Let A and B be finite multisets of positive integer exponents, with **each side separately satisfying** sum(e) <= 2331. Set d=e+1 and H_k(X)=sum_{e in X}(e/(e+1))^k. Suppose H_k(A)=H_k(B) for all k=0,...,6.

Assume the previously established exact cancellation of every d with v2(d)>=6, including [v2=6 three-tier proof](https://github.com/awdawmip/enterprise-math/blob/c577f07bcd434340c500b91e4b67a5402c82c514/research_notes/driver/2026-11-23_t6_p2_sixth_universal_cancellation_three_tier.md) and its prior v2>=7 references.

**Theorem.** If each of A and B contains *at most one* denominator having exactly v2(d)=5, then their entire exact-v2=5 denominator submultisets coincide. In particular, no difference consisting of a single exact-v2=5 atom on each side can extend to equality of the full seven H-moments, regardless of other lower-valuation denominators.

**Stronger arithmetic statement.** Without imposing the 2331 mass bound on the odd factors, equality of full moments plus exact-v2>=6 cancellation and precisely one exact-v2=5 denominator per side forces their odd factors to be congruent **modulo 256**.

## Proof with full mixed reciprocal moments

Binomial inversion of H_0,...,H_6 gives equality of the *complete* reciprocal moments S_k(X)=sum_d m_X(d)/d^k for 1<=k<=6. Subtract identical exact-v2>=6 multiplicities. Let delta_{v,j}=m_A(2^v j)-m_B(2^v j), j odd, and write

    D_{v,k} = sum_{j odd} delta_{v,j} j^{-k}  in Z_2.

The full equality, multiplied by 2^(5k) and reduced modulo 2^(2k), yields for k=1,...,6:

    D_{5,k} + 2^k D_{4,k} == 0  (mod 2^(2k)).

Every term from v<=3 has a factor 2^(2k), so is correctly eliminated *only at this modulus*. This implies

    D_{5,k} == 0 (mod 2^k),
    T_k := D_{5,k}/2^k == -D_{4,k} (mod 2^k).

For every odd j, j^{-4} == j^{-6} == 1 (mod 8). Therefore D_{4,4} == D_{4,6} (mod 8), giving the **cross-valuation necessary invariant**

    T_4 == T_6 (mod 8).                 (1)

This invariant applies to *arbitrary* exact-v2=5 signed profiles, including those with multiplicities.

For the at-most-one case, the k=1 congruence says the two singleton counts have the same parity; hence both counts are zero or both are one. In the latter case, write the odd factors as u,v. The k=5 first-tier congruence gives

    u^{-5} == v^{-5} (mod 32).

Exponentiation by 5 is an automorphism of the unit group modulo 32 (Euler exponent 16 is relatively prime to 5), so u==v (mod 32). Put v=u+32t for an integer t.

For any odd u, set x=32t/u in Z_2. The convergent 2-adic binomial expansion (1+x)^(-k) shows

    T_4 = [u^{-4} - (u+32t)^{-4}]/16 == 0 (mod 8),
    T_6 = [u^{-6} - (u+32t)^{-6}]/64 == 3 t u^{-7} (mod 8).

Indeed the leading terms are 4x and 6x; after division by 16 and 64, respectively, every quadratic/higher term is divisible by 8. Substituting into (1) gives 3 t u^{-7} == 0 (mod 8). Since 3u^{-7} is a unit, **8 divides t**, i.e. u==v (mod 256).

Under the T6 budget, 32j-1<=2331 and j is positive odd, so 1<=u,v<=71. Thus |u-v|<=70<256 forces u=v. This proves exact-v2=5 singleton rigidity. QED.

## Independent bounded verification

There are exactly 36 admissible odd factors j=1,3,...,71 (C(36,2)=630 distinct unordered singleton pairs). The modular fifth moment separates them into 16 classes: four triples and twelve pairs. It directly rejects 606 pairs. For the remaining 24 pairs, the exact k4/k6 cross-valuation invariant rejects all 24, with no lower-layer cost assumptions.

The standalone, integer-only checker `research_checks/T6_P2_FIFTH_SINGLETON_CONGRUENCE_EXACT_20261123.py` verifies all counts and 1,024 supplementary u/t congruence cases without invoking floats or assuming componentwise rational moment equality. Local execution: all assertions PASS.

## Scientific scope and next direction

This **closes the zero/one exact-v2=5 atom-per-side subfamily**, not the multi-atom v2=5 layer and not GLOBAL_T6=2332. For several v2=5 atoms the same general invariant (1) remains a reusable filter on their signed profile. Next useful route: combine the k5 first-tier signature and the k4/k6 invariant with independent side-mass budgets to classify remaining two-or-more-atom defects.

Contributions: this lemma/checker is the existing Driver's independent mathematical subunit. All older T6/p17/p19/q14 discoveries retain their own authorship and source pins. New scientific subunit=1; Native Review accepted=0; Result accepted=0; formal Task completed=0; mother objective completed=0. GitHub scientific publication is separate from formal Activity/Source and Review admission.
