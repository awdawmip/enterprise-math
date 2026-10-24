# R271 — Sharp Fibonacci exponent of common-effect provenance collisions in positive affine BRC

Date: 2026-10-25. Status: AUTHOR-SIDE HAND PROOF + EXACT INTEGER COMPUTATION. NOT FORMAL RESULT, NOT INDEPENDENT DRIVER REVIEWED, NOT P000-NATIVE X6 DYNAMICS.

## Frozen source and research scope

Global-Knowledge-V1 canonical main: c9c3e48d3aeb4e53b6bc8c66e299c7e6b7060036. Enterprise Math control source main: b347e6454442154a80f599cdaebe8d174f33ccdd. P000 startup verified canonical blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc, ACTIVE_LOCKED, unchanged. ACTIVE worldview and current docs/PORTABLE_RESEARCH_PROTOCOL.md read without changes.

Input lineage: R268 six-channel common-effect witnesses and R270 author-side exact paper at immutable commit ae394b2d4846e14763af593a49c1129fa1f9a25e, research_notes/r270_six_channel_mass_20261025/R270_BLOCK_AMPLIFICATION_LOWER_BOUND_20261025.md (blob 0701f04eec22050da58346ac30bed53262887809). R270 proved one fixed 30-step reset coefficient 16482 and its resulting exponential lower bound. This R271 contribution establishes the SHARP growth exponent of reset-effect fibers and six-channel common-effect bottlenecks.

The assertions are about an explicitly defined FORMAL positive unit-weight BRC model on ordered binary selector words, not a native P000 heartbeat update or an actual R193 time-port theorem. Word length is not physical elapsed time.

## Definitions

Control state q in {0,1,2} starts at 0. Selecting a in {0,1} gives (q',eta,b) as follows:

| q | a=0 | a=1 |
|---|---|---|
| 0 | (2,-1,-1) | (2,+1,-1) |
| 1 | (0,-1,-1) | (0,+1,-1) |
| 2 | (1,+1,+1) | (2,+1,-1) |

The accumulated affine effect g=(epsilon,k) acts on SIX FORMAL SLOTS by F_g(z1,...,z6)=(epsilon*z1+k,epsilon*z2,z3,z4,z5,z6). Composition in chronological order is (epsilon,k) THEN (eta,b)=(eta*epsilon,eta*k+b). The ordered provenance automaton starts r=0, with r=0 when no 00 has occurred and the last symbol is 1 (also at the empty word), r=1 when no 00 has occurred and the last symbol is 0, and absorbing r=2 after 00 occurs.

P_n(q,r,g) counts length-n ordered selector words of exact terminal control, provenance and effect, with positive integer multiplicity. Let h=1 if r=2 and h=0 otherwise. The six terminal channels, in this order, are C=((0,0),(0,1),(1,0),(1,1),(2,0),(2,1)). Let H_n(c,g) be the exact positive-integer count in terminal channel c at complete effect g.

For n>=1 define M_n=max_g P_n(0,0,g), the strongest effect fiber among FULL resets of q=r=0. For n>=7 define B_n=max_g min_(c in C) H_n(c,g), the largest bottleneck mass across all six channels sharing one and the same complete effect.

Fibonacci conventions: F_0=0,F_1=1,F_(t+2)=F_(t+1)+F_t; phi=(1+sqrt(5))/2.

## Lemma R271.1 (common synchronizing suffix, all effects have polynomial support)

The 4-symbol suffix sigma=1101 takes every starting q=0,1,2 to q=0. Proof: after the two leading selectors 1 all three possible q are at 2, then selector 0 takes q to 1 and the last selector 1 to 0. Because sigma begins/ends with 1 and contains no 00, appending it to a 00-free word ending in 1 creates a 00-free word ending in 1, hence terminal r=0. Appending a fixed suffix is injective on words.

After n steps, the recurrence k'=eta*k+b with eta,b in {+1,-1} gives |k|<=n and k congruent to n modulo 2. Therefore at any fixed length n, at most 2(n+1) distinct complete effects (epsilon,k) can arise: n+1 parity-admissible translations times 2 signs. This bound counts FORMAL COMPLETE effects, not a coarser projection.

## Theorem R271.A (exact reset-fiber growth rate)

For EVERY integer n>=5,

  ceil(F_(n-3)/(2(n+1))) <= M_n <= F_(n+1).    (A1)

Consequently,

  lim_(n->infinity) (M_n)^(1/n) = phi.           (A2)

Proof. The number of length-(n-4) binary words with no substring 00 and ending in 1 is exactly F_(n-3). Append sigma=1101 to each. By Lemma R271.1, we obtain F_(n-3) DISTINCT length-n words all ending in (q,r)=(0,0). The at-most-2(n+1) possible complete effects partition these words, so one exact effect fiber has size at least the ceiling in (A1). Conversely, every length-n word ending in r=0 avoids 00 and ends in 1, of which exactly F_(n+1) exist, proving the upper bound. Fibonacci's elementary nth-root limit is phi; fixed shifts and polynomial factors have nth roots tending to 1. Thus the lower and upper bounds yield (A2). QED.

A2 is a proven infinite-depth statement, not a finite-range numerical extrapolation. It gives the OPTIMAL EXPONENTIAL RATE for exact-effect full-reset multiplicities, not an explicit maximizing effect formula.

## Lemma R271.2 (three existing six-channel base fibers)

Exact integer recurrence, also verified by direct word enumeration at these depths, yields the following positive vectors H_j(.,g_j), in the fixed C order:

j=7, g_7=(+1,-3): b_7=(2,2,3,1,1,9).
j=8, g_8=(+1,0):  b_8=(1,6,1,9,2,16).
j=9, g_9=(-1,-1): b_9=(1,19,2,20,4,28).

All 18 base entries are >=1. Separately p=101 returns (q,r)=(0,0) to itself with complete effect g_p=(+1,-1), as is checked directly from the control/effect table. The effect is reused by chronological composition rather than treating a six-component formal slot expression as native physical motion.

## Theorem R271.B (sharp six-channel common-effect collision exponent)

For the EXACT six terminal channels and complete formal effects defined above,

  lim_(n->infinity) (B_n)^(1/n) = phi.           (B1)

Proof of lower bound. Fix ANY integer block length L>=5. Select a complete effect g_L that attains M_L. There are exactly M_L distinct length-L words which reset (q,r)=(0,0) and have IDENTICAL complete effect g_L. For arbitrary n>=7 put K=floor((n-7)/L), t=n-KL, j=7+((t-7) mod 3), h=(t-j)/3. Thus j belongs to {7,8,9}, h>=0, and n=KL+3h+j. Concatenate (i) K independently selected words from the length-L reset fiber, (ii) h copies of p=101, (iii) any length-j base word in any chosen channel c at effect g_j.

This is an INJECTION: fixed block boundaries distinguish the choices, and each block returns to the same starting q,r. Chronological affine composition proves ALL these words, regardless of channel c, have the SAME effect g_L^K THEN g_p^h THEN g_j. Therefore for every c,

  H_n(c,g_L^K THEN g_p^h THEN g_j) >= (M_L)^K b_j(c) >= (M_L)^K,

so B_n >= (M_L)^floor((n-7)/L). For fixed L, K/n tends to 1/L as n tends to infinity, hence liminf B_n^(1/n) >= M_L^(1/L). This holds for every L. Letting L tend to infinity and using Theorem A gives liminf >=phi. The sign of g_L causes no difficulty: its group power is the same across all block choices and all channels.

Proof of upper bound. Any one of the six channels with h=0 consists ONLY of words avoiding 00. The number of ALL length-n words avoiding 00 is F_(n+2). For every effect g, the minimum of its six terminal channel counts is at most F_(n+2), hence B_n<=F_(n+2). Therefore limsup B_n^(1/n)<=phi. Combine the bounds. QED.

## Corollary R271.C: quantitative positive decoder obstruction, explicitly excluding d=6

Let D(d) be the R268/R270 comparison class: a positive rational weighted BRC aggregator with d internal states, arbitrary time-dependent transitions and authentic affine effect labels, and a SINGLE-VALUED deterministic terminal decoder depending arbitrarily on (internal state v, depth n, full effect g). A state v at fixed (n,g) can contribute to at most one of the six channels. For d<=5 choose effect g maximizing B_n. At least 6-d original channels cannot receive any modeled mass; each has at least B_n original mass. Thus

  sum_(c in C) |H_n(c,g)-Hhat_n(c,g)| >= (6-d)B_n.   (C1)

If, additionally, the candidate preserves the exact UNMARKED marginal mass at this same g, the absolute error lower bound DOUBLES, as each omitted unit must reappear as surplus in represented channels. By (B1), the guaranteed one-effect lower bound has sharp base phi in its exponent. But B_n/2^n ->0 because phi<2: NO uniform positive normalized error floor follows.

This does not rule out d=6. The broad class retains the actual unresolved interval 6<=d_min<=7, even with Theorems A/B. Signed amplitudes, nondeterministic readouts, effect-dependent untyped transitions, and native physical claims are outside the stated scope.

## Executed verification and reproduction

The accompanying R271_verify.py uses only Python exact integers. It independently checks:
- all 4,095 ordered binary words of depths 0..11 against a full recurrence;
- the complete six-channel formal-affine histogram through depth 38;
- the three depth-7/8/9 base vectors, all-six support first appearing at depth 7, and 30-step amplification for depths 7..38;
- the no-00 reset sector and parity/Fibonacci invariants through depth 160;
- the synchronizing suffix, integer counts, and R270's reference P_30(0,0,+1,-4)=16482.

A SEPARATELY IMPLEMENTED C++17 Boost.Multiprecision verification (R271_independent.cpp) computes the no-00 reset recursion and independent exact coefficients through depth 160; its output is R271_INDEPENDENT_OUTPUT.txt. Both executed locally and PASSED. Full programs and reports are evidence, not a formal proof checker. Computed maxima M_n:
n=30: 16506 at effect (-1,-4), versus R270's 16482 at (+1,-4);
n=60: 21010024205 at (-1,-4);
n=80: 273055000503388 at (-1,-4);
n=120: 50619832248140702252095 at (+1,-4);
n=160: 9992479752177812645565616065526 at (+1,-4).

The numerical samples establish no asymptotic fact on their own. (A2)/(B1) rest on the complete mathematical constructions, Fibonacci counts and polynomial effect-support bound. Data code uses exact integer counts; displayed nth roots are approximations only.

## Authority, preservation and next mathematical unit

GitHub connector identity was verified as awdawmip with repository push permission. Source-native em_status read returned version 0.6.11, but em_control_tasks and em_control_dispatch returned CONTROL_QUOTA. Native em_session_start was rejected before sending the operation: STATIC_READONLY_SCOPE_DENIED (static_machine_readonly; operation_sent=false). No owner, CLAIM, native execution session, Result, independent Driver review, or Foundation acceptance is inferred. This is AUTHOR-SIDE research and its publication is a durable draft only. Native ControlPacket.from_edges/then/EffectHistogram was not run; actual R193 provenance/time-port rules were not resolved.

Next genuinely discriminating question: determine whether an exact d=6 positively weighted effect-conditioned aggregate with authentic composition and deterministic decoder exists at EVERY depth and effect, or construct a cross-depth/time-port no-go certificate that survives n,g-dependent decoding. Theorems A/B sharply quantify the necessary six-channel mass but do NOT settle that exact 6-vs-7 representability question.

Researcher-ID: EM-CHAT-R4-20261025-LOCAL / TASK_RESEARCH
