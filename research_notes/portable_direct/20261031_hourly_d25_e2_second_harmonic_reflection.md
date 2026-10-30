# D25/LIFT — published alternating E.2 and a signed second-harmonic Franel reflection

Date: 2026-10-31 Asia/Hong_Kong. Lane: TASK_RESEARCH, logical conversation \`chatgpt-research-hourly-enterprise-math-20260923\` (not maintenance). Scope: author-side external p-adic arithmetic. Status: AUTHOR-DERIVED COROLLARY OF PUBLISHED THEOREM / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.

Parent: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\`; P000 ACTIVE_LOCKED unchanged.

## 1. External theorem consumed: match the alternating sign and endpoint

For each prime p ≡ 1 (mod 6), m=(p−1)/3, the *original alternating* E.2 sum is

B_p = Σ_{n=0}^{m} (−1)^n (6n+1) (1/3)_n^3/(n!)^3.

The **published**, previously proved Van Hamme (E.2) supercongruence states B_p ≡ p (mod p³). It is not proved afresh here. Exact sign, weight, endpoint and precision are recorded in Guo–Schlosser, *New q-Analogues of Van Hamme's (E.2) Supercongruence and of a Supercongruence by Swisher* (2023), introduction and Theorem 1.1: https://pmc.ncbi.nlm.nih.gov/articles/PMC10027641/ . The distinct nonalternating result with p-adic gamma factor in Corollary 1.5 must not be substituted. This theorem evaluates the E.2 side only, not original 216 LIFT.

## 2. All-prime second-harmonic identity (new-to-project sourced corollary)

Set v_n=binom(m,n)^3, F_m=Σ_{n=0}^m v_n and, for 0≤n≤m,

δ_n = Σ_{r=m−n+1}^{m} 1/r,
δ_n^(2) = Σ_{r=m−n+1}^{m} 1/r².

All denominators are p-units. Retain two signed, precision-typed moments:

T_1 = Σ_{n=0}^m (6n+1)v_n δ_n  (mod p²),
T_2 = Σ_{n=0}^m (6n+1)v_n[δ_n²/2−δ_n^(2)/6]  (mod p).

**Theorem (deduced from the published E.2 theorem):**

   T_1 ≡ F_m − 1 + p T_2  (mod p²).                         (H2)

In particular the prior D25 four-port E.2 harmonic readout H_p^B ≡ T_1 ≡ F_m−1 (mod p), now evaluated for all p ≡1 (mod 6).

**Proof.** Since 1/3=−m+p/3, the following finite identity is exact over Q:

   (−1)^n (1/3)_n³/(n!)³
     = v_n ∏_{r=m−n+1}^{m}(1−p/(3r))³.

For each r a p-unit, logarithmic/formal finite-product expansion through order p² yields

   RHS ≡ v_n {1−pδ_n+p²[δ_n²/2−δ_n^(2)/6]} (mod p³).

The *exact integer* pairing n↔m−n gives Σ(6n+1)v_n = (3m+1)F_m=pF_m (pair weights sum to 2p). Summing gives B_p≡pF_m−pT_1+p²T_2 (mod p³). Insert the published congruence B_p≡p (mod p³), divide this p-divisible equality by p and obtain (H2). Modulus p² for T_1 and modulus p for T_2 are essential.

## 3. Second-order signed antisymmetric reflection

Define H_j=Σ_{r≤j}1/r and H_j^(2)=Σ_{r≤j}1/r² (mod p). Then for every p≡1 (mod 6),

 T_2 ≡ (1/4) Σ_{n=0}^m (6n+1)v_n
             (H_n−H_{m−n})(2H_m−H_n−H_{m−n})
       − (1/12) Σ_{n=0}^m (6n+1)v_n
             (H_n^(2)−H_{m−n}^(2))             (mod p).  (R2)

**Proof.** Reflection fixes v_n and maps weight w_n=6n+1 to w_{m−n}=2p−w_n ≡−w_n (mod p). Thus weighted sum of f_n=δ_n²/2−δ_n^(2)/6 only depends on (f_n−f_{m−n})/2. Substitute δ_n−δ_{m−n}=H_n−H_{m−n}, δ_n+δ_{m−n}=2H_m−H_n−H_{m−n} and their second-harmonic analogues. The two terms above follow algebraically. First-harmonic and second-harmonic antisymmetric ports are distinct; discard neither before the specified observer.

## 4. Exact reduction of the original 216/E.2 bridge

Consume prior author-side exact four-port decomposition at EM commit \`f53d9c10a841f1e09d27b4219127c517cbe9cbfb\` and no predecessor completed native units. Write p=6ℓ+1, m=2ℓ, and define

 S_t=Σ_{n=0}^{m}(6n+1)(−1)^n 2^(−n) binom(3ℓ,n)binom(2ℓ,n)binom(4ℓ,n).

The prior C_p=(S_t−pF_m)/p is legitimately defined for the frozen CM p mod24∈{13,19}. Prior identity:

 (D_0+D_1)/p ≡ C_p + H_p^A + H_p^B + U_p (mod p).

From (H2), H_p^B≡F_m−1 (mod p), and hence the *new source-aware reduction*

 (D_0+D_1)/p ≡ S_t/p + H_p^A + U_p − 1 (mod p).   (A1)

This is a reduction, not the all-prime zero theorem. Separately the original 216 a_n have v_p(a_n)≥2 for n>3ℓ, so E.2 implies

 D_0+D_1 ≡ A_p−p  (mod p²)                        (A2),

A_p = Σ_{n=0}^{p−1}(6n+1)binom(2n,n)^2 binom(3n,n)/216^n, with the exact D0,D1 from the previous bridge and all p≡1 mod6. This is the correct first-digit equivalence; a second-digit correction involving the signed intermediate I_p is still required. It is not permissible to infer LIFT from published E.2 alone.

**Next exact mathematical proof obligations:** establish S_t/p+H_p^A+U_p≡1 (mod p) simultaneously for the frozen classes p mod24∈{13,19}, or an actual original-class counterexample. Then, where divisibility is proved, establish (D0+D1)/p²+I_p≡0 (mod p). Native H0/B0 divided powers, [X]U mod p², semilinear Frobenius/η and p373 benchmark remain separately required.

## 5. Exact executed verification

Independent standard-library program \`d25_e2_harmonic_second_moment_20261031.py\` computes original alternating E.2 recurrence modulo p³ separately from binomial/harmonic expansion, evaluates (H2), and recomputes (R2) from independently accumulated harmonic tables. Executed 330 primes 7≤p≤5000 with p≡1 mod6, of which 166 are in the frozen p mod24 classes; no floats and no native H0/B0 substitution.

p=373,m=124: B_p mod p³=373; F_m mod p²=2421; T_1 mod p²=5031; T_2 mod p=7, with 2421−1+373·7=5031. p=19: F_m mod361=22, T_1 mod361=59, T_2=2, with 22−1+19·2=59. The reflection independently returns T_2=7 at p373. Program marker: \`PASS_SOURCED_E2_SECOND_HARMONIC_MOMENT_AND_RAW_RECURRENCE\`. Finite checks are implementation witnesses, while the published E.2 plus displayed derivation supply all-prime strength.

BRC COMPOSE_APPLIED to carrier (p,m,n,sign,original-source,binomial,δ,δ²,weight,valuation,precision,reflection), with observer signed E.2 modulo p³ and source-labelled moment readouts. This is an external arithmetic typed application and does not transfer to P000 native X6 geometry.

## 6. Formal authority and continuation

At the Gateway 0.6.11 read of 2026-10-31, research_authority_granted=false; executor_binding_configured=false; native active_jobs=5/5; CODE_REVIEW_REQUIRED/UPSTREAM_CODE_REVIEW_REQUIRED. Author-only Git publication and these exact arithmetic checks are **NOT** Source CLAIM/OPEN/checkpoint/Result/independent review. Historical service sessions, staging, request IDs and maintenance conversation are untouched; formal Research-Activity REGISTER_PENDING/SYNC_DEBT. Existing EM #1558 is the native control support path and #1559 the original native benchmark intake. Continue from (A1) and preserve frozen scientific pin unchanged.
