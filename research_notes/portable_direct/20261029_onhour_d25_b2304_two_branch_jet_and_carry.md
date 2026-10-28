# D25 / SECOND-DIGIT-LIFT: B2304 双目标类 companion jet 及条件性高位进位定理

Research date 2026-10-29 Asia/Hong_Kong. AUTHOR-SIDE / EXACT PRIOR-THEOREM COROLLARY + CONDITIONAL DERIVATION / 166 EXECUTED PRIME CHECKS / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING / NATIVE_H0_B0_NOT_EXECUTED.
Mother objective ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION; task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen science Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged). Research conversation chatgpt-research-onhour-enterprise-math-20260923; not maintenance chatgpt-hourly-enterprise-math-20260921.

## Input identities, source and proof strength

Let p be prime congruent 13 or 19 (mod 24). Define beta_n=(1/8)_n(3/8)_n/(n!)² and gamma_n=(1/4)_n(1/2)_n(3/4)_n/(n!)³; the complete original B2304 sum is

B_p=sum_{n=0}^{p-1}(8n+1)gamma_n/9^n
   =sum_{n=0}^{p-1}(8n+1)binom(2n,n)²binom(4n,2n)/2304^n.

For p≡13 (mod24), set (a,b)=((5p−1)/8,(7p−3)/8); for p≡19 (mod24), (a,b)=((p−3)/8,(3p−1)/8). Let K_b(z)=sum_{n=0}^b beta_n z^n, theta=z d/dz, w=1/9, K=K_b(w), D=(theta K_b)(w). Let Pi_<p retain original degrees <p; Q_a(z)=sum_{i=0}^a (beta_i mod p)z^i; J(z)=sum_{j=b+1}^{p-1}(beta_j/p² modp)z^j, the exact quotient having p-local denominators. Keep distinct

R_B=[(1+8theta)Pi_<p(Q_a J)](w) mod p;
H_B=[(1+8theta)(1−Pi_<p)(K_b²)](w) mod p³.

Previously proved AUTHOR-SIDE p³ truncated Clausen theorem (research_notes/portable_direct/20261029_onhour_d25_b2304_p3_sharp_carry_crosskernel_certificate.md, commit 3fe386d2578dbf2825a76a7f9a7ef360e85ada80) is

(1)  B_p ≡ K(K+16D) − H_B + 2p²R_B (mod p³).

The p≡19 branch has 2b<p and H_B=0 *identically*. The p≡13 branch has genuine low×low, low×middle and middle×middle over-cutoff source contributions, as derived in 20261029_onhour_d25_b2304_harmonic_three_source_carry.md (commit 4dcbb8960f9f04f6acc46f8d9faa24c91dc319d9).

Published prior art: V.J.W. Guo and W. Zudilin, A q-microscope for supercongruences, Advances in Mathematics 346 (2019) 329–358, DOI 10.1016/j.aim.2019.02.008, https://arxiv.org/abs/1803.01830. They proved B_p ≡ p*(-3/p) (modp³) for all primes p>3. The character is +1 in both target residue classes, hence B_p ≡ p (modp³).

## NEW strict corollary — all p≡19 (mod24)

Combining (1), H_B=0 and the published theorem gives, **unconditionally for every prime p≡19 mod24**:

(2)  K(K+16D) ≡ p−2p²R_B (modp³).

In particular v_p(K(K+16D))=1 and exactly one of K,K+16D has valuation 1, the other 0. Under the *additional* hypothesis K≡0 modp, write k1=K/p modp. Then

(3) 16k1(D modp) ≡1 (modp).

The finite checks below verify the extra root in sampled primes, but do not establish a universal CM/Hasse-root theorem. The universal theorem here is (2), which does not need the extra root.

## NEW conditional theorem — p≡13 high carry

For every prime p≡13 mod24 satisfying the explicitly conditional **Root2** hypothesis

(4) K_b(1/9) ≡ 0 (modp²),

set k2=K/p² modp and d0=D modp. Then K²≡0 modp³ and K(K+16D)≡16p²k2d0 modp³. From (1) and the published B theorem,

(5)  H_B ≡ −p+p²(16k2d0+2R_B) (modp³).

Thus H_B ≡−p modp² under Root2. For p≡13, this first p-adic digit resides in the original high-degree cut, whereas for p≡19 there is no high cut and the digit resides in the companion square. This is an observer-scoped BRC provenance result: (5) does not erase the tagged original (i,j) sources for other future operations.

Root2 for *all* primes p≡13 mod24 remains CONJECTURAL. This is a conditional theorem and not a proof of the cross-kernel A216/B2304 congruence or original native LIFT/JT2.

## Reproducible executed exact certificate

Actual standard-library Python checker: research_notes/portable_direct/d25_b2304_branch_jet_20261029.py. It computes beta_n w^n via t_(n+1)/t_n=(8n+1)(8n+3)/(576(n+1)²) for 0≤n<b<p, using p-unit modular inverses; no floats.

ALL 83 primes p≡13 mod24 and p<5000: K≡0 modp² (zero exceptions).
ALL 83 primes p≡19 mod24 and p<5000: K≡0 modp and 16(K/p)D≡1 modp (zero exceptions).
Eight selected primes 13,19,37,43,109,139,373,379 had independent factorial-product beta checks modp³ and independently calculated original binomial B sums. For 13,37,109,373,19,43, separately enumerated original ordered pairs with i+j≥p and computed exact R_B to verify (1) and (2)/(5). Terminal result:

TARGET p<5000: p=13 mod24 83, p=19 mod24 83
BRANCH_13_K_MOD_P2_NONZERO: []
BRANCH_19_16_K_OVER_P_D_MOD_P_NOT_ONE: []
PASS_D25_B2304_BRANCH_JET_OBSERVER p<5000 exact modular samples=8 source_checks=6

At p=373 (p³=51,895,117): K=20,730,221=149p² modp³, D=5 modp, R_B=246 modp. U_B=K(K+16D)=49,669,053=357p² modp³; direct source-pair enumeration gives H_B=14,329,914. Identity (5) predicts -373 + 373²*(16*149*5+2*246 mod373)=14,329,914, equal to the previous three-source carry 10,219,454+9,814,749+46,190,828 modp³. U_B−H_B+2p²R_B≡373, matching independent B373.
At p=19: K=171=9p modp², D=7 modp; 16*9*7≡1 mod19; U_B=3990 mod6859, H_B=0, R_B=4, original B19=19.

## Carrier, scope, next scientific action and control status

BRC resolution COMPOSE_APPLIED: carrier is (p,i,j) with original coefficient source low/middle, degree i+j, valuation, signed weight 1+8(i+j), original Pi_<p BEFORE differentiation and point evaluation w=1/9. The compressed two-branch jets preserve only this declared observer modulo p³; neither a full generic source quotient nor a native X6/H0/B0 evaluation is proven. P000 remains ACTIVE_LOCKED unchanged, no reinterpretation of the native 6D spatial/3D slice.

Smallest mathematical next unit: prove or falsify universal Root2 (4) for p≡13 mod24 through a faithful finite CM/Dwork/WZ certificate, or retain and transport a nonzero Root2 defect. Then derive the needed original A216/B2304 p³ cancellation for both target classes with the frozen Delta_p−R_p source alignment (20261026_onhour_d25_native_lift_source_port_identity.md). Do not recycle Clausen or prior 373 scalar checks as new discovery. D25/LIFT/JT2 OPEN.

Original native benchmark is separate and highest-priority: https://github.com/awdawmip/enterprise-math/issues/1559 (read 2026-10-29: OPEN/PENDING_OWNER/NATIVE_NOT_EXECUTED). Actual same-original-class p373 H0/B0 divided-power [X]U mod 139129, module rank, semilinear Frobenius direction/eta, signed odd Green/Hesse, original kappa/Delta−R, native reproducible code and independent review still require a lawful executor; scalar B2304 is no substitute.

Read-only Site gateway version 0.6.11 returned research_authority_granted=false, executor_binding_configured=false, active control quota 5/5 and code-review-required. The original Research-lane request IDs research-onhour-20261027-0501-recovery-r13 and research-onhour-20261027-0507-dispatch-r13 returned CONTROL_REQUEST_NOT_FOUND to this Site's receipt read, and new exact Source continuation read returned CONTROL_QUOTA. Historical requests are preserved, not replayed. No Researcher Source session, winning claim, run, Source checkpoint, Result, freeze or independent review is asserted; no maintenance-lane authority borrowed. This GitHub note is author-side evidence only, UNREVIEWED/NOT_ADMITTED/REGISTER_PENDING/SOURCE_SYNC_DEBT. Next authorized operator: reconcile the old exact request receipts, read current exact canonical continuation, and only then decide own session/claim/open; do not hop selector or alter frozen pin. No schedule, notifications, scheduler or Actions changes.
