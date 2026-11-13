# D25/LIFT target-class sharpening: the natural weighted j first jet is one sufficient source scalar

Date: 2026-10-27. Status: AUTHOR_DERIVED / AUTHOR_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED. This is a portable auxiliary modular-curve proof, not canonical Source checkpoint, original native H0/B0 experiment, independent review, or LIFT/JT2 theorem.

Parent ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION; Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific source c47e13e4aba0e006366f989d6334d443f6333ae3; frozen taskbook Git blob 53a3ef039325534e3715add837f0eee332289984. This material does not change those pins, P000 or the ACTIVE worldview.

For any prime p congruent to 13 or 19 modulo 24, let O_p=Z_p[s]/(s^2−2), x_0^±=3±2s, B_±=x_0^±+pO_p, t=x/[27(1+x)^2], J=27(1+x)(1+9x)^3/x, T=1/216+pO_p. Reciprocal x↦1/x preserves t and exchanges B_±. On each ball t is bijective onto T by the previously proved simple-root Hensel argument. The entire source population here consists of these two labelled balls, not an asserted native P000 embedding.

**Theorem.** For every x∈B_+ and y=1/x∈B_- at equal t, the *unmodified* natural first-jet scalar H=(1+6t d/dt)J obeys

    H(x) − H(y) ≡ −77704704 s  (mod p)
    77704704 = 2^9 · 3^3 · 7 · 11 · 73.

None of the prime factors 7,11,73 is congruent to 13 or 19 modulo 24 (their residues are 7,11,1), so the difference is a p-adic unit for **every target-class prime**. Thus (exact t, H modulo p) separates source balls and uses only one *natural* auxiliary weighted scalar besides the shared t. A separate J readout, branch tag or modified M=(9+6θ_t)J is unnecessary for this declared target family and same-t recovery operation. H mod p by itself cannot reconstruct the full t value; the claim is not global injectivity.

**Proof.** Reuse the previously proved exact sheet-difference identity D(t)=J(x_+(t))−J(x_-(t))=A(t)d(t), where A(t)=27(t^(−1)−64)(t^(−1)−8), d=x_+−x_- and S=x_++x_-=1/(27t)−2. From d^2=S^2−4, d'/d=SS'/(S^2−4). Hence H_+−H_-=C_1(t)d(t) with

    C_1=A+6tA'+6tA·SS'/(S²−4).

At t_0=1/216, exact algebra gives d=4s, A=853632, A'=−453496320, d'/d=−324, 6t_0=1/36. Therefore

    C_1(t_0)=(1−9)853632−453496320/36
            =−19426176=−2^7·3^3·7·11·73,

and d(t_0)C_1(t_0)=−77704704s. All denominators are p-adic units on T for target p>3. For t≡t_0(mod p), C_1(t)≡C_1(t_0), d(t)≡4s. This proves the universal target-class identity without sampling. Directly at the two fixed points, H(x_0^±)=−54917568∓38852352s, giving the same difference.

The earlier first-jet checks at exceptional p=13 and 19 give residues s and 14s, recovered here from the universal signed integer coefficient. The contrast *does* vanish at p=73, which is outside the frozen target prime classes. Consequently the previously published alternative M=(9+6θ_t)J remains stronger when expanding the scope to all p≥7; this result is specifically a simplification for the present D25 target.

**Observer audit.** BRC_COMPOSE_APPLIED: retain two labelled CM source balls, exact same-t involution, signed difference, prime-valuation information and Hensel inverse sections. The observer quotient (t,J,H)→(t,H) is source-faithful for the stated future operation and target primes. It has not been transferred to original H0/B0, to signed Gauss–Manin/Frobenius, or to the original Δ_p−R_p observer. Matching the coefficient 6 does not prove such a transfer.

Reproducibility: companion standard-library Python checker imports the existing author quadratic-ring helper in this PR, evaluates J and J' directly modulo p³ in Z[s]/(s²−2) for all 166 target primes p<5000, 4 same-t reciprocal deformations per prime (664 cases), and tests p=73 as a negative out-of-scope control. All author checks PASS; that finite regression is not the all-prime proof or independent review.

Unfinished gate: authentic original-class p=373 H0/B0 [X]U mod139129 with true semilinear Frobenius, rank, signed odd Green/Hesse, κ and Δ−R; existing support Issue #1559 remains an intake awaiting an actually authorized native executor. Native winning claim/open/Source checkpoint have not been verified: previous exact read requests returned CONTROL_REQUEST_NOT_FOUND and current 2026-10-27 read r40_20261027_1436_exact_cont_read_v1 returned CONTROL_QUOTA. Keep predecessor completed_units=[] absent Source authentication. UR V2 original four-file hash recovery (historical 94687 bytes, SHA256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76) remains separate and pending; this proof does not repeat UR mathematics or claim missing bytes persisted.
