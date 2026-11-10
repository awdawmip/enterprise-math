# D25/LIFT: two-way zero-set separation of the third-band tail and frozen reflected observer

Date 2026-11-10. TASK_RESEARCH author-side directed verification. **AUTHOR_EXACT_FINITE_COUNTEREXAMPLE_VERIFIED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CLAIM**.

Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Publication: TP2-B6F4FC938FF94941C1B7. Frozen science: awdawmip/enterprise-math@c47e13e4aba0e006366f989d6334d443f6333ae3.

## Precise claim and proof

For each prime p ≡ 13 or 19 (mod 24), put p=6m+1 and b=2m. All calculations are in the p-local rational ring or its exact finite-field reduction. Retain the separate source labels k versus (i,r).

**B recurrence:** B(0)=1 and B(k+1)/B(k)=(6k+1)(3k+1)/(36(k+1)^2), for 0≤k<p−1.

**Third-band scalar observer:** h=sum(k=0..p−1)(12k+1)B(k), S₂=sum(k=b+1..p−1)B(k), t_p = h · (S₂/p²) mod p. The third-band terms have valuation ≥2.

**Original frozen reflected observer:** C(r)=2^(r−1)((r−1)!)² / [18(5/6)_r(2/3)_r] in F_p for 1≤r≤m, and R_p=2 sum(i=1..m) B(i) sum(r=1..i)(1+6(i−r))C(r) mod p. This is copied from the original frozen finite-Clausen source rather than fitted to Delta.

The complete two-witness counterexample is:

| p | S₂/p² mod p | h mod p | t_p | frozen R_p | Delta_p | W_p mod p³ | Hesse odd phi | Hesse norm |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **13** | 8 | 6 | **9** | **0** | 0 | 13 | 11 | 3 |
| **157** | 0 | 80 | **0** | **82** | 82 | 157 | 109 | 112 |
| 373 (extra check) | 252 | 171 | 197 | 196 | 196 | 373 | 243 | 131 |

Here g=sum B(k), Delta=((g/p)h−1)/p mod p, and W is the weighted cubic hypergeometric sum with a₀=1, a(k+1)/a(k)=(2k+1)(3k+1)(3k+2)/(36(k+1)^3) and W=sum(k=0..p−1)(6k+1)a(k). These are original source observers. The *previously proved* frozen identity Delta−R=(W−p)/p² is checked, not recredited.

**Theorem (all-family unit-rescaling obstruction).** No family u_p∈F_p× can satisfy R_p=u_p t_p for every target prime, and no family v_p∈F_p× can satisfy t_p=v_p R_p for every target prime. Indeed units preserve zero: p=13 has R=0 and t=9, contradicting the first, while p=157 has t=0 and R=82, contradicting the second. Thus neither implication R=0 ⇒ t=0 nor t=0 ⇒ R=0 is valid across the family. This only rules out an observer reduction by nonzero scalar normalization. It is NOT a statement that all higher-dimensional, nonlinear or source-preserving relations are impossible.

For p=157, S₂ mod p⁴=286372082 and S₂/p³=74 mod p; aggregate valuation three, versus each individual high-band term's valuation two. The ordinary Hesse odd port remains 109 and norm 112, but is NOT native H0/B0/Frobenius/kappa.

## Reproduction, independent algorithms, retained provenance

Compute B(k) modulo p⁴ in two ways: the stated modular recurrence; independently exact integer numerator prefix N_k=∏(j<k)(6j+1)(3j+1) divided by p-unit D_k=36^k(k!)². The two coefficient vectors match at p=13,157,373. Compute R from its original nested factorial/rising-factor formula, independently by C₁=1/10, C_(r+1)=C_r 36r²/[(6r+5)(3r+2)] and running partial sums S_i=Σ(r≤i)C_r, J_i=Σ(r≤i)rC_r, R=2Σ(i≤m)B(i)[(1+6i)S_i−6J_i]. For each r≤m, independently check B(p−r)/p²=C_r mod p. Independently compute W by the a recurrence above and verify (g h−W) mod p³ = p²R mod p³. All exact integers; no floats or sampling.

Exact row detail from two-algorithm local certificate:
- p13: g mod p⁴=27352, h mod p²=149, G=g/p mod p²=76, S₂ mod p⁴=10140; odd Hesse alpha=(7,6).
- p157: g mod p⁴=454930265, h mod p²=13111, G=13712, S₂ mod p⁴=286372082; odd Hesse alpha=(20,145).
- p373: g mod p⁴=6096224345, h mod p²=62835, G=65672, S₂ mod p⁴=18354036809; odd Hesse alpha=(302,154).

This is an exposed-directed mathematical verification, not clean-blind review. The precise new unit is a **two-way zero-set counterexample by joining two already-sourced marginal observers**, NOT independent discovery of either observer or an all-prime proof of LIFT. BRC semantics: retain third-band k provenance and reflected (i,r) triangular provenance separately; the scalar t cannot be substituted for R by a unit.

## Prior work and next exact action

Frozen R source read at immutable science commit c47e13...:
- research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_FINITE_CLAUSEN_DERIVATIVE_BRIDGE_RETURN_20260827.md (blob c8c2423e8569a3da27b41bb7f602b4b781bb2a79);
- research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_REFLECTED_DERIVATIVE_PRODUCT_BRIDGE_RETURN_20260827.md (blob 3fedf7bef09b426037840721855f9a9d05558a0b).

Already published R streaming identity and 166-prime verification are explicitly reused without recredit: research_notes/portable_direct/20261107_hourly20_d25_frozen_Rp_restored_streaming.md (blob cad78a2cbb27489ccd15d462095701e54d842f5a). The 312-prime Hesse/tail author census is likewise reused without recredit: research_notes/portable_direct/2026-11-10_h40_d25_312prime_hesse_odd_scalar_tail_joint_author_portable.md (blob 5eac6b0e8b0e7248706e211c0e26460883aa9a16).

Executable local companion verified for p13,157,373: d25_two_port_nounit_exact_verify.py and d25_two_port_certificate.json, both author-side, no native Source writer. Next science: obtain a real uniform source-preserving proof/counterexample for W_p≡p (mod p³), or independently verify the native H0/B0 and [X]U, semilinear Frobenius orientation/eta and signed kappa for an original-class p; do not redo solved R lookup, UR, or prior bulk regressions. UR V2 original four-file bundle (94,687 bytes; SHA256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76) still unlocated: preserve writer/provenance debt, do not repeat mathematical proof.

**Scope:** author-side GitHub evidence only; native execution session/CLAIM/run/checkpoint, Driver review, formal Result and mathematical admission are all unverified/unperformed.