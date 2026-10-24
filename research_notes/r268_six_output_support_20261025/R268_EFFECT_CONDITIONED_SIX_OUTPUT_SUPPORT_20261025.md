# R268 | A common full-effect fiber with all six output channels: sharp depth 7 and an aggregate-state lower bound

Date: 2026-10-25
Status: AUTHOR_SIDE_PROOF / EXACT_FINITE_VALIDATION / NOT_DRIVER_REVIEWED / NOT_ADMITTED
GLOBAL_KNOWLEDGE_V1: main@ba426098a3731ac30822784c7f670f2a40416493
Enterprise Math Source: main@5e8c16777987ab8da4afbbc90450a56f6e145945
P000: ACTIVE_LOCKED; global source blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc (matches projection).

## Provenance and exact scope

Inherited, not re-proved: R263 author evidence at ecce6d55b4c2b1f58769dc40d306f594f7d29b9a (seven internal memories share one effect from depth 8); R265 at b6d858eacbd5482b6a4bb7bcf847bdee2a9932fa (seven-state minimum for *fixed* output decoder); R266 at 5ab2fcd0a980c728560b2a10b3657f0413ba1dd1 (homomorphic effect-conditioned quotient obstruction); R267 at 950c0d72c33132540a5762d73ef6990ef1079c14 (finite-window coefficient-decoder dimension). Their mathematical admission status is not upgraded.

This is a formal positive BRC with an affine action on six FORMAL slots, not an established native X6 operator, native heartbeat trajectory, or R193 source/time-port representation. The index m counts serial branches, not physical time. Positive branch weight/count never stands for signed amplitude.

## 1. Typed BRC and observer

Formal effect g=(epsilon,k), epsilon in {+1,-1}, k integer. Its action on six formal slots is
 F_g(z1,z2,z3,z4,z5,z6)=(epsilon*z1+k,epsilon*z2,z3,z4,z5,z6).
Chronological composition is
 (epsilon,k) THEN (eta,b)=(eta*epsilon,eta*k+b).

There are two ordered unit-positive outgoing branches a=0,1 per control state q:
 q=0: a=0 -> (q'=2,eta=-1,b=-1); a=1 -> (2,+1,-1).
 q=1: a=0 -> (0,-1,-1); a=1 -> (0,+1,-1).
 q=2: a=0 -> (1,+1,+1); a=1 -> (2,+1,-1).

The provenance monitor has states r=0 ("00" not seen; previous is not zero), r=1 ("00" not seen; last is zero), r=2 ("00" already seen). Transitions, ordered by a=(0,1), are
 r=0 -> (1,0), r=1 -> (2,0), r=2 -> (2,2).
The initial full state is (q,r,epsilon,k)=(0,0,+1,0). Full positive count propagation is
 P_(m+1)(q',r',eta*epsilon,eta*k+b) += P_m(q,r,epsilon,k),
for both outgoing branches, with integer path multiplicities and no cancellation.

The *terminal observer* discards the distinction r=0 versus r=1 but retains (q,h), h=1 iff r=2. Its six channels in fixed order are
 C=((0,0),(0,1),(1,0),(1,1),(2,0),(2,1)).
Let H_m(c,g) be the number of ordered selector words of length m with observer c and *exact* cumulative affine effect g.

## 2. Theorem A: first shared six-output fiber occurs at 7, persists forever

Let S_m=max_g #{c in C: H_m(c,g)>0}. Then

 (S_0,S_1,S_2,S_3,S_4,S_5,S_6,S_7)=(1,1,1,3,4,4,5,6),

and S_m=6 for every integer m>=7.

For m<=7 the exact support statement is certified by exhaustive traversal of all 2^m binary source words, independently checked against the positive BRC integer-count recurrence above (finite exhaustive lemma; full source code supplied). In particular no depth m<=6 has six channels at a common effect.

At depth 7 the genuine common effect g_7=(+1,-3) supports all six channels and its exact count vector in channel order C is

 H_7(C,g_7)=(2,2,3,1,1,9).

Six exact, distinct source-word witnesses are:

| channel c | length-7 selector word | effect |
|---|---|---|
| (0,0) | 1011101 | (+1,-3) |
| (0,1) | 0001101 | (+1,-3) |
| (1,0) | 1011110 | (+1,-3) |
| (1,1) | 0001110 | (+1,-3) |
| (2,0) | 1011011 | (+1,-3) |
| (2,1) | 0000001 | (+1,-3) |

Two further *complete* bases occur at j=8,9. At j=8 the effect is (+1,0), count vector (1,6,1,9,2,16), and witnesses for C in order are
 01010101, 00001100, 01010110, 00000100, 01101011, 00001010.
At j=9 the effect is (-1,-1), count vector (1,19,2,20,4,28), and witnesses are
 110101101, 000001000, 101010110, 000001110, 010101010, 000000011.
All 18 words are individually checked by their original transition equations, including provenance status and full effect. These are not merely sampled fibers.

For the universal extension, let p=101. Starting from (q,r)=(0,0), p returns to (0,0), and its genuine chronological affine effect is (+1,-1). By the composition law p^h is again such a reset with effect (+1,-h). Any integer m>=7 uniquely has
 m=j+3h, j in {7,8,9}, h>=0.
Prefix p^h to each of the six base witness words at length j. Every prefixed word has the *same* terminal channel as its base because p^h resets the entire control/source monitor, and all six have the exactly common effect
 g_m=(epsilon_j,k_j-epsilon_j*h).
Thus S_m>=6 for all m>=7, and the six-channel observer gives S_m<=6. This proves the infinite-depth assertion independently of any depth cutoff.

This output-channel onset at m=7 is **not** the same question as R263's seven *internal-state* common effect (first at m=8).

## 3. Theorem B: even arbitrary positive aggregate BRC needs at least SIX states

Define comparison class D(d) as follows. A candidate has d internal control states, arbitrarily many positively weighted rational BRC edges per state, authentic effects from the same affine group, and any time-dependent edge/weight packet; no source-word-to-source-word homomorphism is required. Candidate mass mu_m(v,g)>=0 is accumulated under the real affine composition law. Final readout is an *arbitrary deterministic single-valued function*
 D(v,m,epsilon,k) -> (q,h) in C.
It may inspect the full effect and step number and may change with them. The only representation obligation is **exact equality** of all six-channel joint histograms at every c and g in the target horizon:
 Hhat_m(c,g) = sum_{v: D(v,m,g)=c} mu_m(v,g) = H_m(c,g).
In particular, a single state at a single effect and depth cannot be fractionalized into several *different output labels* by D; such a stochastic/mass-splitting readout would be a different comparison class.

Then D(d) reproducing the target distribution already at (m,g)=(7,(+1,-3)) entails
 d>=6.
The bound also holds *separately* at every m>=7 for the same unrestricted class.

Proof: Fix such an m and its exact g_m from Theorem A. For each of the six channels c, H_m(c,g_m)>0. Exact equality and nonnegative mass require some internal v with mu_m(v,g_m)>0 and D(v,m,g_m)=c. Since D is single-valued, different c require distinct v. Consequently d>=6. No pathwise source homomorphism, fixed decoder, linear coefficient assumption, or stationary transition assumption is used. QED.

The known original seven-state construction is a realizable upper bound. Hence the **currently unresolved** minimum in this larger class obeys
 6 <= d_min(D) <= 7.
This result must NOT be misreported as proving seven-state minimality for arbitrary aggregate effect/time-dependent decoders. R265's fixed-linear-decoder Hankel factorization does not apply to arbitrary D without a further proof.

## 4. A local quantitative information-loss bound

At m=7 and effect g_7=(+1,-3), six positive channel masses are (2,2,3,1,1,9), sorted (1,1,2,2,3,9). Any single-valued decoder using d<6 internal states yields positive output for at most d channels at this one (m,g). If s_t is the sum of the t smallest counts in the sorted list, its local unnormalized L1 discrepancy obeys
 sum_{c in C}|H_7(c,g_7)-Hhat_7(c,g_7)| >= s_(6-d).
If in addition the candidate matches the unmarked effect marginal at g_7 exactly, namely 18, missing positive mass must be compensated by excess mass on other channels, and
 L1 >= 2*s_(6-d).
For d=5, marginal-preserving L1>=2; normalization by all 2^7=128 source paths yields >=2/128. This is a finite-fiber mathematical error floor, not a uniform time/physical error bound.

## 5. Executed evidence, honest boundaries, and next exact unit

The supplied Python script R268_six_output_support.py implements the typed positive BRC recurrence through depth 96, exhaustively checks 4095 source words for depths 0..11, verifies all six-channel common-effect fibers through depth 96 and universal reset-witness construction through depth 219. R268_independent.cpp is an independently written C++17 exact integer implementation checking depths 0..20, exhaustive raw-word agreement through depth 11 and all three base count vectors. All author-side checks passed. Full 18 witnesses and raw exact coverage appear in R268_AUTHOR_EXACT_REPORT.json. The all-depth result itself follows the reset proof; it is not inferred from finite computation.

Reuse status: R263 original BRC witness/effect checker REUSE_EXECUTED; R265 formal affine THEN rule REUSE_APPLIED. This work changes observer and comparison class within the existing BRC family; it neither introduces a new BRC-native physics module nor claims execution of enterprise_math ControlPacket.from_edges/then/EffectHistogram.

Native authority: authenticated GitHub user awdawmip; em_status version 0.6.11; native em_control_tasks returned CONTROL_QUOTA, and em_session_start(RESEARCHER) returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false. Thus this turn did not verify the live owner, acquire a CLAIM, create a native RA/Result or obtain independent Driver review. A GitHub draft is durable **author-side evidence**, not Source-native admission. P000 and the ACTIVE worldview are untouched.

NEXT (R269): In precisely the comparison class D(d), resolve the 6-versus-7 remaining gap with either a *genuine positive six-control aggregate affine BRC* reproducing the full terminal joint effect histogram at all depths, or a *non-homomorphic obstruction*. Check simultaneous constraints across several effect fibers and depths, unmarked effect-marginal consistency and transition compatibility; do not silently reuse a fixed-decoder Hankel bound for the variable-effect readout. Independently establish the R193 true path/query/time-port and P000 X6 bridge before any native-transfer claim.
