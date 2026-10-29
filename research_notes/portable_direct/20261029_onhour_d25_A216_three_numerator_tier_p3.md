# D25/LIFT: original A216 three-numerator p^3 tier theorem and six signed observer ports

2026-10-29. AUTHOR-SIDE / EXACT COEFFICIENTWISE PROOF / EXECUTED INTEGER CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING / NATIVE_H0_B0_NOT_EXECUTED.

Mother ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3, not rebased. Research conversation chatgpt-research-onhour-enterprise-math-20260923, not the maintenance lane.

## Exact original 216 model

For every prime p=6m+1>=7, set

a_n = ((1/2)_n (1/3)_n (2/3)_n)/(2^n(n!)^3)
    = binom(2n,n)^2 binom(3n,n)/216^n,
A_p = sum_{n=0}^{p-1} (6n+1) a_n.

Use distinct numerator sources I={(r,c,label)}={(3m,1/2,"1/2"),(2m,1/3,"1/3"),(4m,2/3,"2/3")}. The identities 1/2=-3m+p/2, 1/3=-2m+p/3, 2/3=-4m+2p/3 are exact in the localization Z_(p). For each n<p, define

h_n = # {(r,c,s) in I : r<n},
C_n = product_{(r,c,s) in I:r<n} c,
U_n = (2^n (n!)^3)^(-1) product_{(r,c,s) in I} product_{0<=j<n,j!=r} (j-r),
S1_n = sum_{(r,c,s) in I} sum_{0<=j<n,j!=r} c/(j-r),
S2_n = sum_{(r,c,s) in I} sum_{0<=j<n,j!=r} c^2/(j-r)^2.

All denominators are p-units. Exact factor extraction gives

a_n = p^{h_n} C_n U_n * product_{(r,c,s) in I} product_{0<=j<n,j!=r} (1+pc/(j-r)).

Using the second elementary symmetric function of the unit factors yields the **all-prime coefficientwise theorem**

(**) a_n == p^{h_n} C_n U_n [1+p S1_n+(p^2/2)(S1_n^2-S2_n)] (mod p^3),

valid for EVERY 0<=n<p and p=6m+1>=7. The hit counts are exactly 0 for n<=2m, 1 for 2m<n<=3m, 2 for 3m<n<=4m, 3 for 4m<n<p; moreover v_p(a_n)=h_n. The **signed observer** 6n+1 adds an independent valuation exactly at n=m, since 6m+1=p; this distinction must be retained.

Therefore A_p == T00+T01+T02+T10+T11+T20 (mod p^3), where

T00 = sum_{n=0}^{2m} (6n+1) U_n,
T01 = p sum_{n=0}^{2m} (6n+1) U_n S1_n,
T02 = (p^2/2) sum_{n=0}^{2m} (6n+1) U_n (S1_n^2-S2_n),
T10 = p sum_{n=2m+1}^{3m} (6n+1) C_n U_n,
T11 = p^2 sum_{n=2m+1}^{3m} (6n+1) C_n U_n S1_n,
T20 = p^2 sum_{n=3m+1}^{4m} (6n+1) C_n U_n.

All n>4m terms vanish coefficientwise mod p^3. The zero-hit unit is a terminating SIGNED binomial factor

U_n = (-1)^n * 2^(-n) * binom(2m,n) binom(3m,n) binom(4m,n), 0<=n<=2m.

This turns the original unmodified 216 problem into a finite signed-binomial / first-and-second harmonic / two p-hit boundary certificate. It differs from previously authored two-factor companion spectral jets because it computes the original 3F2 numerator streams without invoking Clausen or redefining its weighted n-cut. The original LIFT/Sun supercongruence is **not proved**; the precise remaining obligation for p=13,19 mod24 is to establish this six-port sum == p (mod p^3) uniformly. Inherited CM0/UR/source reflection are not new contributions.

## Actually executed integer evidence

A standalone stdlib exact verifier (same-run executable artifact named d25_a216_three_numerator_p3_guard_20261029.py) checked each individual coefficient and all six ports for all 115 primes p=1(mod6), 7<=p<1500. Among them 31 p=13(mod24) and 29 p=19(mod24). It also independently evaluated original INTEGER binomial coefficients for the 35 primes p<=373; the original direct 3F2 recurrence is checked for every n in all 115. All assertions pass. All 60 tested target primes satisfy A_p==p(mod p^3): finite observation ONLY, not all-prime proof.

At the original p=373, p²=139129, p³=51895117, m=62, in order (T00,T01,T02,T10,T11,T20) the exact modular residues are
(15521276,1164506,11408578,16705551,21982382,37008314).
Recombining by source hit count:
tier0=28094360, tier1=38687933, tier2=37008314=266*p², tier3=0.
Their sum equals **A_373==373 mod 51895117**. At n=m=62 the unweighted a_m ==122(mod373), a unit, while (6m+1)a_m=373*a_m has valuation one. The nonzero tier2 is a source-preserving falsifier of dropping the second numerator hit at p³. Hit boundaries for p373: 124/125, 186/187, 248/249 (n is original coefficient index).

Algorithm and proof obligations can be checked directly with modular unit inversions; for each original n the program independently computes a_n from its hypergeometric ratio a_{n+1}/a_n=(2n+1)(3n+1)(3n+2)/(36(n+1)^3), and separately computes original integer binomial terms when p<=373. No floating-point or unexecuted claim.

## Typed reuse and remaining native requirement

BRC COMPOSE_APPLIED only as arithmetic provenance preservation: carry source labels 1/2,1/3,2/3, original degree n, hit count, signed observer, and all six first/second parameter-jet ports through mod p³. No assertion that this auxiliary finite-ring equation is a native six-axis or three-dimensional-slice theorem; P000 and the ACTIVE residual-faithful worldview remain unchanged.

Independent native issue awdawmip/enterprise-math#1559 was read OPEN/PENDING_OWNER at this run. Real same-original-class p373 H0/B0 divided-power [X]U(mod139129), module rank, semilinear Frobenius direction/eta, signed odd Hesse/Green observer, kappa and Delta-R remain native NOT_EXECUTED here; this scalar check is NOT a substitute.

The Site MCP gateway 0.6.11 read has research_authority_granted=false, write_relay_enabled=false, active quota 5/5. Direct recovery_status action unavailable to the present Site; historical session/claim/run/target_request IDs remain UNKNOWN, not empty. No Service session, CLAIM, open, native checkpoint, Result, review or maintenance-lane role usage is asserted. GitHub author-side storage is not Source acceptance.

Next precise action: obtain terminating WZ/character-sum or reflection evaluation for the six signed finite-binomial/harmonic ports, preserving both 13 and 19 mod24; separately assign an AUTHORIZED NATIVE executor to #1559 and capture exact genuine H0/B0 proof-of-execution, then independently review. On authorized original Research-lane Source recover original request/continuation before any new dispatch, preserve current frozen scientific pin, and bind this author-side material only under actual lawful checkpoint/admission.

Proof is elementary factor extraction plus e2=(S1²-S2)/2 and finite hit intervals. No theorem acceptance, formal Lean check, original CM native execution, or independent Driver review is claimed.


## Same-run inherited-source reconciliation (2026-10-29)

After the initial author-side publication, the *existing* original-source benchmark intake #1559 was read including its comments, and the exact prior result was recovered: `20261028_onhour_d25_original216_p3_middle_tail_reflection.md` at commit `321f9240503f7c462a2f722b1da1ff96b950abcb` (prior blob `fe2c24e8ed71a2b4e9ee47dbc7d8ddcc6d8a4e03`). That **previous author** had ALREADY proven the four original weighted-216 p-adic valuation bands and the complete n=3m+1..4m tail reflection, `Theta_p`, including `Theta_373=266` and `T20=266p²`. The original numerator band decomposition and the 373 tail value in this note are **reused earlier facts, not fresh mathematical novelty**. Claiming a new tail theorem here would repeat completed work. These observations remain useful regression tests of source conservation.

The **distinct new scope** here is strictly the algebraic **six-port first/second numerator parameter-jet** (T00,T01,T02,T10,T11,T20) at the *original A216 summand*, its terminating signed triple-binomial first tier, and its p-sensitive finite WZ/harmonic proof obligation; no new claim about the known T20/Theta itself. In exact original degree labels n=4m-r, the pre-existing reflection theorem says `(6n+1)a_n/p² == tau_{p,r} mod p`; hence `T20/p² == Theta_p`. The updated executable at the SAME original path, commit `70c955f67578249b60f3a970020201aa0257c2cf`, verified blob `8739d732df7a12d106412501d450e31258bc0688`, now reuses that prior **independent factorial-reflection formula** and checks each tau digit and the sum against the new numerator-hit evaluator for ALL 115 primes p=1 mod6 below 1500, besides all original 3F2 recurrence and 35 independent integer-binomial checks. This is a composition/cross-source validation, not a rediscovery of the frozen tail.

The narrowed exact unsolved proof dependency is: establish the **five-port bulk** identity `T00+T01+T02+T10+T11 == p-p²Theta_p (modp³)` for *all* target p=13,19 mod24 using a genuine finite WZ/CM/character-sum argument, consuming the already proved Theta reflection and prior accepted CM0/UR. It is the same frozen LIFT target, not a new task or a completed proof. The real native #1559 execution remains a separate pending-owner scientific requirement. Formal Source state stays unverified; this is only a GitHub author-side correction and source provenance alignment.
