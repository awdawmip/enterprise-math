# D25/LIFT — Negative Ward left-boundary second p-jet and harmonic observer

Date 2026-10-26. **SOURCE-NEUTRAL AUTHOR EVIDENCE; UNREVIEWED; NOT_ADMITTED; NOT_NATIVE_TASK_CHECKPOINT; REGISTER_PENDING / NATIVE_SYNC_DEBT.** This is a new portable author derivation, not a native Researcher CLAIM, OPEN, Result, Source progress writer, independent review, or original-class CM/DP experiment. This work does not assume possession of the existing Researcher's private session or logical conversation identity. No frozen scientific source pin is changed.

Mother objective D25/LIFT/JT2; Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; immutable frozen science source c47e13e4aba0e006366f989d6334d443f6333ae3.

## Existing inputs, not newly credited

The inherited exact negative Ward adjoint is in research_notes/portable_direct/20261026_hourly_d25_ward_adjoint_two_digit_tangent_r11.md; the exact finite Gauss-sum closure and its first p-jet are in the same author's separate local note 20261026_offphase_d25_negative_ward_delta_hypergeometric_closure_LOCAL_UNPUBLISHED.md. The authentic corrected-Clausen Hasse terminal source and three-digit dual Ward are in research_notes/portable_direct/20261026_hourly_d25_third_digit_dual_ward_resonant_face_r11.md and its checker. Another already established result, research_notes/portable_direct/20261026_hourly_d25_green_all_order_cumulants_r11.md, treats Green transfer coefficients, not this delta scalar. Do not recredit prior p=733 delta first resonance, prior terminal jets, or other Research1 J1/J2 work.

For any prime p=6m+1≥7 put R=2m−1=(p−4)/3. The true oriented negative Ward adjoint yields
δ_0=1, δ_t=((p+2t)/(p+2t−1)) δ_{t−1}+2^{−t}
and δ_R=2^{−R}−(p+2R)λ_{−R}. The inherited *exact rational* Gauss product formula is

δ_R=A_R(p) Σ_{t=0}^R 2^{−t}/A_t(p),
A_s(X)=∏_{j=0}^{s−1}(X+2j+2)/(X+2j+1).

## Theorem — complete second p-jet modulo p³

Define in Z_(p):
P_s=4^s/binom(2s,s), b_t=binom(2t,t)/8^t,
D_s=H_s−H_{2s},
L_s=H_{2s}^{(2)}−H_s^{(2)}/2
    =Σ_{j=1}^s[(2j−1)^{−2}−(2j)^{−2}],
with D_0=L_0=0. All denominators are p-units because 2R<p. Then the universal congruence for all primes p=6m+1 is

δ_R ≡ P_R Σ_{t=0}^R b_t {1+p(D_R−D_t)
       +(p²/2)[(D_R−D_t)²+L_R−L_t]}   (mod p³).   (T)

**Proof.** All constants in A_s(X) are p-units, so A_s(X)/P_s is a formal series with coefficients in Z_(p). Direct logarithmic differentiation at zero gives (log A_s)'(0)=D_s and (log A_s)''(0)=L_s. Consequently for each t≤R,

A_R(X)/A_t(X) ≡ (P_R/P_t)[1+X(D_R−D_t)
       +(X²/2)((D_R−D_t)²+L_R−L_t)]   (mod X³).

Apply this formal identity to the exact *finite* Gauss formula, use 2^{−t}/P_t=b_t, and evaluate X=p. The remainder lies in p³ Z_(p). This is an algebraic all-prime proof; finite computation below is only author checking. □

This has a linear-length moment evaluator. Put S0=Σb, S_D=Σ bD_t, S_DD=Σ bD_t², S_L=Σ bL_t. Then

δ_R ≡ P_R[S0 + p(D_R S0−S_D)
   +(p²/2)(D_R² S0−2D_R S_D+S_DD+L_R S0−S_L)] (mod p³).

## Exact information-loss witness

At p=13,R=3 the original oriented recurrence, the unexpanded Gauss product and (T) all give δ_3=1906 (mod 13³=2197). If the L_R−L_t coordinate is simply dropped while every other second-jet term is preserved, the value becomes 385. The missing 1521=13²·9 is nonzero. Therefore coarsening the BRC-compatible p-adic observer to the first harmonic jet D alone is **not sound at the three-digit readout**. The carrier is labelled by signed Ward orientation, p-valuation, finite cutoff, Hasse port and weighted higher harmonic jet; this external p-adic bookkeeping is not a 6D native physical axis or a P000 theorem.

Author-side exact checks (Python stdlib, no floating point, no original-class native experiment): 330 primes p≡1 mod6 with 7≤p<5000, 257100 source recurrence cells, 660 prime-level independent modular comparisons of (T) with original δ recurrence and exact finite Gauss product, all PASS. Six independent rational identity spots and six independent exact Fraction second-jet divisibility spots, all PASS. The omitted L coordinate contributes a nonzero mod-p³ difference at 328/330 primes; two observed exceptional primes 673,2371 do not imply a universal exception classification.

## p=733: isolated next digit of true left boundary

At p=733,R=243, the second-jet identity independently confirms the previously seen δ≡7698699=733(241+14·733) (mod 733³); that already-known integer is not recredited as a new observation. The corrected-Clausen Hasse-endpoint recursion (not native crystalline CM) gives, modulo 733²:

u_{1,244}=220164, u_{2,732}=316513,
Y_L^{12}=−244 u_{1,244}u_{2,732}=268155=610+365·733.

For this **specific** labelled source, C12=δ Y_L^{12}, so the *new combined higher precision* readout is

C12/733 ≡ 500316=410+682·733 (mod 733²),
C12 ≡ 366731628 (mod 733³).

For the isolated old third-digit negative boundary port γ_p·(2p C12), γ_p=2^{−p}/18,

γ_733·(2·733 C12) ≡ 85692759899
 =733²·430+733³·217 (mod 733⁴).

The 217 is **only the next digit of this isolated negative left-face port**; it is NOT the fourth digit of full original Q_p/p². At that precision the other higher Hasse faces, positive/infinity J/E, high–high ordered population and changed source contractions remain outstanding. Mod 733³ the earlier valid face digit 430 is recovered.

## Minimal reproducibility algorithm (all integers)

For each p, modulus M=p³, compute the true delta recursively starting at 1 using the exact rational recurrence modulo M. Separately compute the Gauss product A_R(p) and sum 2^{−t}/A_t(p) modulo M. For (T), start P_0=b_0=1 and D_0=L_0=0, then for t=1..R update

P_t=P_{t−1}(2t)/(2t−1),
b_t=b_{t−1}(2t−1)/(4t),
D_t=D_{t−1}+1/(2t)−1/(2t−1),
L_t=L_{t−1}+1/(2t−1)²−1/(2t)²

inside Z/MZ (every inverse exists). Accumulate S0,S_D,S_DD,S_L. Evaluate the boxed linear formula and compare the three independently obtained residues. For p=733 independently generate only Hasse endpoint jets using u_0,0=1 and, for a≤2, n=1..p−1,

n(n−p/2)u_{a,n}
=(n−1−m)(n−1−2m)u_{a,n−1}
 +3n u_{a−1,n}−(3(n−1)−4m)u_{a−1,n−1}
 +2u_{a−2,n−1},

zero for negative labels and n<0; reduce modulo p². This recovers both endpoints and labelled C12 without reperforming entire original Q or any genuine CM experiment.

The complete runnable checker and full author numeric JSON for this run are available as the accompanying conversation artifacts:
d25_negative_ward_delta_second_jet_checker_20261026.py and
d25_negative_ward_delta_second_jet_author_check_20261026.json.
This neutral note alone contains the complete proof and verification semantics; it does not claim those two unmerged local artifacts were committed here.

## Native control and precise continuation

The *other actual historical Research conversation* had read-only recovery and Source continuation SUCCEEDED at 2026-10-26 ~13:39 +08 (enterprise-math Issue #1558). Its Source native checkpoint has two genuine completed predecessor units, HANDOFF_READY/NEEDS_DISPATCH/NO_LIVE_CLAIM, execution_authorized=false, a latest-claim versus previous-checkpoint predecessor mismatch and an older registered service session; none of that historical identity is this note's CLAIM or independent-review entitlement. This run's native Site is static_machine_readonly/write_relay_enabled=false and research_authority_granted=false; a new native control_continuation read returned CONTROL_QUOTA and checkpoint listing ACCESS_DENIED. No native write/role mutation was retried. Any local or neutral GitHub storage is distinct from native progress publication, Result and admissible checkpoint.

Control owner: existing enterprise-math Issue #1558. Preserve the immutable native Source frontier, archived staging and contributor IDs; resolve authenticated predecessor/ownership epoch and lawful same-real-conversation successor session; only real verified own typed continuation_prepare→winning CLAIM→OPEN→native checkpoint readback authorizes formal progression. No claimed native success here. The initial-input seed case, if surfaced, must first be fully read and carry frontier_notes.completed_units=[] instead of treating parent inputs as completed owner research. The original H0/B0, [X]U mod p², semilinear η/κ, native CM computation and full cross-sector WZ/Driver review remain OPEN.

Separate UR V2 four-file original 94,687 byte bundle, target SHA256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76, has still not been recovered with matching bytes. Two historical separate corrected V2 uploads (bridge #1121/#1224) are staged-only and not substitutes; their existing mathematical proofs are not redone. Existing scheduler, phase, notifications and user pause controls remain untouched.
