# JT2 finite p² transport — non-author paper review (2026-11-14)

Status: SOURCE-EXPOSED NON-AUTHOR PAPER REVIEW / QUALIFIED PASS ON Q2, C2 AND THE CONDITIONAL W2–UR BRIDGE; NOT A NATIVE RESULT REVIEW OR ACCEPTANCE.

Reviewer: EM-DVR-DEBB5E, RESEARCH_DRIVER, reused original legitimate Sites SID MCP-9b4714dc46b948afa4875a86c89c713c. Reviewed author: EM-DVR-C777E7. These are different research identities, but this reviewer has now read the predecessor handoff, source manifest, author paper and inherited proof: source-exposed review, not blind discovery or independent replication of the complete parent proof.

Controlling frozen candidate: awdawmip/enterprise-math@9e3a41dc9909ad98c789bb8d53a27addd0649eaa:research_artifacts/JT2_PERSISTENT_LINE_DRIVER_20260909/reviews/ur_reuse_20260909/driver_authored_transport_candidate.md, Git blob c6f2396307f5f8599374ac507532d107363512a3, SHA256 063ac8f6f31f83f0b9e16a3a3520aebd52527eb8237a28f07a833fa0f6d28eee. Its source_manifest.json at the same commit has blob 6cd848c0d59ae02fd97bbbc0ec474cfbdfca8f77.

## Reviewed proposition and exact argument

For primes p=6m+1>3 and localized coefficient ring Z_(p), set c_k=(1/6)_k(1/3)_k/(k!)², F_p(z)=sum_{k=0}^{p-1}c_k z^k, L_p(u)=sum_{k=0}^{p-1}(1/3)_k(2/3)_k u^k/(k!)², and W_p(z)=sum_{k=0}^{p-1}(6k+1)(1/2)_k(1/3)_k(2/3)_k z^k/(k!)³.

**Q2: L_p(u) ≡ F_p(4u(1-u)) (mod p²) coefficientwise.** DLMF §15.8.18 with a=1/3,b=2/3,c=(a+b+1)/2=1 gives the normalized formal identity. For k≥2m+1 and k<p, (1/6)_k contains the factor p/6 (index m) and (1/3)_k contains p/3 (index 2m), while k! is a p-unit; hence v_p(c_k)≥2. For each degree j<p, the compositional coefficient of u^j involves only k≤j, so matches the infinite quadratic identity exactly. For p≤j≤2(p−1), any contributing k obeys k≥ceil(j/2)≥3m+1>2m, hence is 0 mod p²; L_p has no such degree. Both low- and high-degree cases are covered. Substitution u=(1∓t)/2 in Z_(p)[t]/(2t²−1), where 4u(1−u)=1/2, yields B(t)≡B(−t)≡g:=F_p(1/2) mod p², preserving the labeled ports.

**C2: W_p(z) ≡ F_p(z)(F_p(z)+12zF'_p(z)) (mod p²).** The exact Clausen identity _2F1(1/6,1/3;1;z)^2 = _3F2(1/3,2/3,1/2;1,1;z) identifies coefficients j<p. A product term c_i c_k of degree i+k≥p cannot have both i,k≤2m (as i+k≤4m<p), and one factor is divisible by p². Application of 1+6z(d/dz) multiplies coefficients by 6j+1 in Z, so the high-degree vanishing persists. Thus the full finite polynomial congruence follows, not just an evaluation at one point.

**W2–UR step.** The frozen CM0 certificate establishes p|g. The inherited exact relation H_m(z)=Q_m(1-z) mod p and F_p≡H_m mod p gives h=(F_p+12zF'_p)(1/2)≡−6Q'_m(1/2) mod p. Then W_p(1/2)≡gh mod p²; if the external CM Ramanujan theorem supplies W_p(1/2)≡p mod p², division by p is legal and gives (g/p)(−6Q'_m(1/2))≡1 mod p. With P'_n(t)=2tQ'_m(1/2), n=2m, and 3B(t)≡3g mod p², multiplication by t gives 3B(t)P'_n(t)≡−pt mod p². Both directions of the equivalence are correct. SIMPLE supplies Q'_m(1/2) a unit where reciprocal language is used.

## Primary-source applicability

* DLMF §15.8.18: https://dlmf.nist.gov/15.8.E18. Actual formula read; normalized at u=0.
* Chisholm–Deines–Long–Nebe–Swisher, Mathematics 1 (2013), Theorem 1: https://www.mdpi.com/2227-7390/1/1/9 . Actual theorem statement, λ and a p-unit, totally-real and CM assumptions, unramified/good-reduction conditions, sgn and mod-p² conclusion read from publisher HTML. It proves the weighted congruence mod p², not mod p³.
* J. and P. Borwein, Pi and the AGM, printed pp.185–186 and 190, source PDF https://carmamaths.org/jon/Preprints/Papers/Submitted%20Papers/Elliptic%20moments/pi-agm.pdf : relevant scanned two-page spreads visually inspected at PDF zero-index pages 99,100,102. (5.5.33) gives the parameterized weighted series and Exercise 19(b)(ii) gives H_2^24=2; Exercise 20(b)(i) at s=1/6,N=2 gives (6n+1)/(3√3), so b_s/a_s=6 and argument 1/2. These published exercise values are accepted as external inputs and not independently derived from elliptic integrals.

Under the earlier source-pinned CM identification j=2417472±1707264√2, CM field Q(√−6), p≡13 or 19 mod24 is inert, (−6/p)=−1 and (2/p)=−1. For λ=1/2, Q(√(1−λ))=Q(√2) is unramified for p>3, and a=6 and λ are p-units. The model y²+xy+(u/27)y=x³, u=(1−t)/2, u(1−u)=1/8 has discriminant u³(1−u)/3^9, a p-unit. Theorem 1 gives sgn=−1 and ((1−λ)/p)=−1, hence W_p(1/2)≡p mod p². This is a conditional use of the inherited CM class-polynomial identification; its original proof is separately pinned in EBP6JT_RETURN and is not reverified by this paper review.

Inherited source: awdawmip/enterprise-math@6058e8fa69cc8c9a3e571d05bc6cbb8b4565c5aa:research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_TERMINATING_JACOBI_JET_CERTIFICATE_RETURN_20260828.md, blob cf36004694dc2c8c9134e2e1e989c076b88e4c03; read §§1–11. Predecessor JT2 handoff: @587e6ee4a138c34de9d87bc90e06f17d7fe1b910 research_notes/EM_FREE_W59A_JT2_UR_QTF3_STATE_MACHINE_HANDOFF_20260909.md, blob 48cfda2d4f49c88ff2efd0ca013d9806c2e8d216.

## Scoped conclusion and forward handoff

The author’s Q2, C2 and first-digit W2–UR algebra pass this non-author source-exposed paper review in the declared p=6m+1, p≡13/19 (mod24), p>3 setting, relying on the explicitly named inherited CM0/SIMPLE and CM field identification. The distinction between proofs of the finite polynomial identities and the application of an external CM theorem is retained.

The Sun task RS-EMW59A-JT2-UR-SUN-PARITY-DEFECT still requires exact output 3 (adjacent-value/jet elimination) or an explicit allowed task-scope revision and output 6 (minimal obstruction, if claimed); this review does not supply them. QTF3 at u=1/2, argument 1 and precision p³ is separate from Q2’s u=(1−t)/2, argument 1/2 and p²; the reflected R_p and (G_p mod p²) second-digit LIFT remain OPEN. No formal Task Result, Native Review disposition, predecessor acceptance, Foundation or mother-objective closure is asserted by this report.

Non-author source-exposed review is advisory until the Source-native role/Result review contract applies. Preserve original contributors EM-FREE-W59A, EM-EBP6JT-4D1A01, EM-UR24-7C91A0 and candidate author EM-DVR-C777E7.
