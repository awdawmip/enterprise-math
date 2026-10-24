# D25 / SECOND-DIGIT-LIFT — direct p³ hard target: 575-prime dual-path finite certificate

2026-10-24 | on-hour TASK_RESEARCH author lane: chatgpt-research-onhour-enterprise-math-20260923. UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT; not a native benchmark, Result, Source run/checkpoint or independent review.

## Scope and source boundaries

Mother question: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Earlier author records identify canonical publication TP2-B6F4FC938FF94941C1B7; fresh canonical claim/session ownership has not been established here. The frozen mathematical Source pin remains c47e13e4aba0e006366f989d6334d443f6333ae3. This is a larger finite original-hard-target check, not re-credit for the WZ proof (c7fb90fd), same-prime five-tail p³ transport (7724e73f), odd/even LOW seed proofs (6f14c39f / 5404753a), or the p=211 certificate (767c51ef). Other research conversations retain their independent attribution.

The original object is, with p=6m+1 prime and p mod 24 in {13,19},

\[
 S_m=\sum_{n=0}^{4m}T_{m,n}
 \stackrel{?}{\equiv}p(4/3)^{p-1}\pmod{p^3},
\quad T_{m,n}=A_m(6n+12m+1)R_{m,n},
\]
\[
 A_m=\frac{(6m)!}{3^{6m}((2m)!)^3},\quad R_{m,0}=1,\quad
 \frac{R_{m,n+1}}{R_{m,n}}=
 \frac{(4m+2n+1)(3n+1)(3n+2)}
 {36(n+1)(2m+n+1)(4m+n+1)}.
\]

No truncated range, denominator or exceptional n is silently changed.

## Exact arithmetical foundation for the verifier

For all positive m and nonnegative n, an exact rational identity follows from equality at n=0 and equality of successive ratios:

\[
\boxed{R_{m,n}=\frac{(4m+2n)!\,((2m)!)^2\,(3n)!}
{216^n\,((2m+n)!)^2\,(4m+n)!\,(n!)^2}.}\tag{F}
\]

For 0<=n<=4m, every factorial index in (F) is at most 12m=2p-2, hence its p-valuation is either zero or one. In detail,

\[
v_p(R_{m,n})
=\mathbf1_{4m+2n\ge p}+\mathbf1_{3n\ge p}
-\mathbf1_{4m+n\ge p}
=\boxed{\mathbf1_{n\ge m+1}}.
\]

The prefactor A_m is a p-unit, and the linear weight 6n+12m+1 is a p-unit: its least nonnegative vanishing index modulo p is n=5m+1, outside this summation. Hence original term valuations are exactly 0 for 0<=n<=m and 1 for m+1<=n<=4m. The two p-factors that cancel at n=2m remain explicitly represented. This safeguard certifies that the computational paths never invert a p-divisible denominator; it is not by itself the full supercongruence.

## Actually executed finite result (not an infinite-prime proof)

The companion [original hard-target p³ dual-path verifier](20261024_onhour_d25_original_hard_target_p3_20k_dualpath_certificate.py) performed a deterministic exhaustive sieve and computed every p<=20000 in the two prescribed classes: 288 primes p≡13 mod24 and 287 primes p≡19 mod24, 575 total, including 530 previously unscanned p>1000 (relative to earlier author p<=1000 reports).

Path A accumulates the unmodified hypergeometric recurrence, preserving p-exponents and p-free units modulo p³. Path B independently accumulates (F), using its own p-free factorial/inverse factorial arrays (all factorial arguments <2p). For every prime it verifies the two original endpoint residues are equal, both agree with the independently computed target, and the exact valuation-support counts are m+1 zero-valuation terms and 3m valuation-one terms.

Execution outcome: 575/575 exact target congruences PASS, 575/575 recurrence-vs-factorial checks PASS, 575/575 valuation-support checks PASS; zero counterexamples in the stated finite domain.

The exact canonical-row projection (ascending p; ASCII lines p,m,S_recurrence,target,difference_mod_p3) has SHA-256:
4344fc9d4e30a26f97a6ba93575c7a99148c89e438330540fb411c1f5f01d91b.

Representative independently matched original residues: p=13, m=2, S=1872 mod 2197; p=19, m=3, S=2546 mod 6859; p=211, m=35, S=8904411 mod 9393931; p=19963, m=3327, S=145858841017 mod 19963³. A complete 575-row CSV was produced locally and is regenerated deterministically by the attached GitHub code (python filename.py 20000 output.csv). The local CSV SHA-256 is 77d740c6cea71164e7deaaf5706285b2a40485746e7caf2b8fdce4230b665211. The executed local code SHA-256 is 99c90a9214569d7885269e2e5e108de7da1c4e9ba0a2f5ebe4eb21bfb52cddb6.

## BRC observer, remaining mathematical target and exact continuation

BRC COMPOSE_APPLIED: the carrier is each labeled original n-term, its unit modulo p³, original low/high membership and p-valuation; the output observer is the signed full endpoint modulo p³. Reduction modulo p³ is sufficient only for this fixed arithmetic output and its allowed addition/multiplication. It does not discard branch/terminal provenance in the mathematical proof, and is not a native Heartbeat X6 or CM/divided-power experiment. P000 and the ACTIVE residual-faithful worldview are unchanged.

Hard target OPEN: the above finite sweep does not prove either infinite prime class. The minimum unfinished algebraic unit is the full same-prime modulo p² normalization of the odd H19 / even H13 exact LOW-seed jets combined with the five WZ upper-rank ports, preferably through a source-faithful same-class CM/divided-power bridge. Retain both exceptional original terminal contributions, correct p-units, and the unchanged frozen hypotheses. No additional already-completed HIGH/LOW auxiliary theorem substitutes for this identity.

Original native benchmark NOT RUN: the source-fixed experiment and its actual host/run/verification protocol are an independently outstanding requirement. The direct arithmetic sweep here is not that native object. The pre-existing control recovery case enterprise-math#1539 owns the Source/session permission path; the native execution owner is not independently verified (NATIVE_EXECUTOR_UNASSIGNED). The precise next operational acceptance is a legitimately owned Source continuation, original benchmark input and actual native execution receipt with checked outputs. Current Sites status reports static read-only scopes and research_authority_granted=false; no recovery_status callable is exposed here. No original unknown request is replayed. Do not use maintenance conversation chatgpt-hourly-enterprise-math-20260921, borrow another session, or claim Source registration/CLAIM/run/Result.

Durable status of this note and companion code: author GitHub evidence only, not formal Task checkpoint, accepted mathematics or final LIFT answer. The three earlier unrelated UR staging materials remain independent. No research scheduler, timing, notification, Source scientific pin or protected worldview was modified.
