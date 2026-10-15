# BRC Q=1,T=4：三体阈值轮廓计数与后置反馈盲区

Status: UNREVIEWED / NOT_ADMITTED / NO_NATIVE_CLAIM. Date: 2026-10-16.
Canonical input: GLOBAL_KNOWLEDGE_V1 0c09d7621f186b45301ccca304db9085d34d143b; Enterprise Math b193909b6f1797eb06bd3d29d3c4bcaa384ac8a7.
Previous exact source (unreviewed): e0dfb2103a49bafadaf641c4fad487846f70138a, research_notes/unreviewed/EM_BRC_HAMMING1_N_DELAY_AND_Q1T3_COLLISION_20261016_R3T11.md.
Current native dispatch CONTROL_QUOTA; session_start STATIC_READONLY_SCOPE_DENIED (operation_sent=false). This is an unclaimed, non-accepted mathematical draft, not a Source Result or RA registration.

## Exact scope

n>=2 labeled sources, nonnegative integer masses d_i; action G_j permits hidden reset of any i!=j, including an already-zero coordinate. A bit [sum remaining >= T] becomes public *after* each action; no initial feedback is revealed. Public strategies can branch and stop. The only strategy output is whether every hidden terminal trace has sum >= Q. No raw transcript is an output. This is a positive-integer BRC auxiliary observer, not a native X6 physical/signed-phase model.

For Q=1,T=4 define the complete subset threshold profile

Sigma_4(d) = ( [sum_(i in S) d_i>=1], [sum_(i in S) d_i>=4] )_(S subset I).

Clipping d_i to min(d_i,4) preserves Sigma_4. Equality of these full profiles implies equality of every terminal-safe output under every feedback-adaptive strategy: couple hidden index choices; after a history of resets R the surviving set S=I\R and both threshold bits come from Sigma_4(S). This is **sufficiency, not minimality**.

## Theorem 1: exact number of full subset profiles for arbitrary n

Let P_n(1,4) count distinct Sigma_4 profiles of all integer states, with source labels preserved. Define

f_m = 3^m - 2^m + 1 - m^2 - m(m-1)(m-2)/3.

For every n>=2,

**P_n(1,4) = SUM_(m=0)^n binom(n,m) 2^(n-m) f_m.**

For n>=4 this simplifies to

**P_n(1,4) = 5^n - 4^n + 3^n - n(n^2+6n+20)3^(n-4).**

Symbolic proof: a singleton profile separates zero-valued labels Z, capped-4 labels H, and intermediate labels M, where |M|=m and each mass is 1,2,3. Any subset meeting H has high bit; any M-subset with >=4 elements has high bit; intermediate singletons have low high-threshold bit. Inside M all information is the labeled pair-low graph L2={{i,j}:d_i+d_j<4} and triple-low hypergraph L3={{i,j,k}:d_i+d_j+d_k<4}.

Partition M=A union B union C with respective weights 1,2,3. L2 consists exactly of A-A and A-B edges. L3 consists exactly of all triples in A. Distinct signatures are disjointly classified and counted:

- empty L2 and empty L3: 1 signature;
- single labeled L2 edge: binom(m,2) signatures, regardless whether its endpoints are (1,1) or (1,2);
- triangle with no low triple: binom(m,3) signatures, realized by two 1s and one 2;
- star with one 1-center and at least two 2-leaves: m SUM_(b=2)^(m-1) binom(m-1,b);
- book graph with an adjacent pair of 1-spine vertices and at least two 2-leaves: binom(m,2) SUM_(b=2)^(m-2) binom(m-2,b);
- at least three 1s: SUM_(a=3)^m binom(m,a)2^(m-a). Its nonempty L3 uniquely recovers A and L2 then uniquely recovers B.

A star center and book spine are identified by degrees; the triangle with an all-1 triple is separated by L3. The displayed sum simplifies exactly to f_m; for m=0,1,2 direct boundary evaluation gives f_m=1,1,2. Independently choose M in binom(n,m) ways and assign each outside label 0 or 4 in 2^(n-m) ways, proving P_n. Binomial falling-factorial moments yield the second formula: SUM binom(n,m)2^(n-m)m^2 = n3^(n-1)+n(n-1)3^(n-2); SUM binom(n,m)2^(n-m)m(m-1)(m-2)=n(n-1)(n-2)3^(n-3).

Values P_n for n=2..7: 10, 41, 210, 1219, 7290, 42949. This is a symbolic all-n theorem, not a fit to these values.

## Theorem 2: post-action feedback blindness, arbitrary Q and T

For n>=2 and 1<=Q<T, let x,y have all coordinates >=Q and every proper-subset sum <T in **both** states. Then x and y give the same terminal Safe_Q under *every finite adaptive policy*. Each first allowed reset removes a positive coordinate; therefore every post-action threshold bit is low, even after arbitrarily many later actions. Consequently both policies follow the same all-low public decisions. Their terminal safety along the same hidden reset-index sequence is equivalent to retaining at least one positive source, because every original mass >=Q. Universal Boolean outputs coincide.

A strict full-profile discrepancy is possible whenever T>nQ: take
x=(Q,...,Q), y=(T-(n-1)Q,Q,...,Q).
The full-set sums are nQ<T versus T, so the complete subset threshold profiles differ. Yet all proper subsets have mass <T and these states are **permanently adaptive equivalent**. This is an exact structural information-loss witness: an initial-only threshold observation disappears because initial feedback is not exposed.

At Q=1,T=4,n=3, (1,1,1) and (1,1,2) have different full Sigma_4 but are forever adaptive equivalent. At n=2, (1,1) and (1,3) behave similarly.

## Exact small-n adaptive quotient (finite computer-assisted results)

Using exact clipped states in {0,1,2,3,4}^n, form one representative for every complete profile (valid by the sufficiency lemma). Test every distinct-profile pair by complete directed belief-pair search. For the orientation X universally safe, Y having an unsafe trace, a valid strategy may be pruned to one Y-unsafe feedback spine: every other feedback branch stops immediately, which preserves X-safety since masses never increase. At every action the algorithm enumerates all hidden reset choices, rejects any action that may leave an unsafe X successor, and follows any Y-compatible feedback bit. Breadth-first closure gives a shortest witness or a completeness certificate of nonseparation; test both orientations. No horizon cap is used for n<=4.

n=2: 10 profiles; 45 pairs checked; one different-profile pair unseparated; **A_2(1,4)=9**, maximum shortest distinguishing depth 2.
n=3: 41 profiles; 820 pairs checked; one different-profile pair unseparated; **A_3(1,4)=40**, maximum shortest distinguishing depth 3.
n=4: 210 profiles; all 21,945 pairs checked and separated; **A_4(1,4)=210**, maximum shortest distinguishing depth 4.

At n=4, pair counts by shortest depth 0,1,2,3,4 are exactly 209, 1404, 4401, 8759, 7172. An independent direct-policy evaluator verifies that for X=(1,1,1,0), Y=(1,1,2,0), the continuation-on-feedback sequence (excluded j, required bit) [(0,1),(0,0),(0,0),(1,0)] gives Safe_1(X)=true and Safe_1(Y)=false, stopping immediately at any off-spine bit.

The verifier also exhaustively counts middle profiles for m<=8, and all clipped full profiles n<=7 (up to 78,125 states at n=7), comparing against the symbolic formulas. For n=5, a fixed-seed sample of only 1000 distinct-profile pairs was separable within depth 5; **no all-n minimality is claimed**.

## New frontier and precise limits

For Q=1,T=4, the complete subset carrier is a pair-low graph plus triple-low hypergraph, with the closed class-count formula above. However, feedback is only accessible after an action: the full subset carrier is generally strictly finer than the adaptive observation quotient (Theorem 2). The finite n=4 equality is not yet a proof for n>=5.

Next: construct a uniform, labeled gate-and-reset adaptive separating policy for every two distinct Sigma_4 profiles when n>=4, or find its first counterexample; determine whether the sharp distinguishing horizon is n for all larger n. Preserve branching/provenance and the distinction between static subset thresholds and post-action observability.

Research code and complete symbolic proof produced locally in the same run; pending authorized project-admission path remains a separate task. No formal Research Activity registration, native CLAIM, frozen Result, independent Driver review, or Foundation/Working Truth acceptance is asserted.
