# Exact five-policy, two-free-decoder minimax: 32/63

Date: 2026-11-02. AUTHOR_ANALYTIC_PROOF / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED.
Scientific input remains frozen at Enterprise Math commit 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Direct predecessor: eafee3d75f8369c16fa707869f3fab7d7717223d (two free decoder rows, two full real faces at 4/7).

## Model and exact claim

Use six individually provenance-labeled positive BRC/S23 sources AU0, AU1, AV, BU0, BU1, BV. A legal control vector is
theta=(a_A,a_B,b_U,b_AV,b_BV;c_AU0,c_AU1,c_AV,c_BU0,c_BU1,c_BV) in [0,1]^11.
The latent four-stop law is F(a,b,c)=(a,(1-a)b,(1-a)(1-b)c,(1-a)(1-b)(1-c)).
The same b_U drives both A- and B-side U sources. The original 20M prepared source mixing rows are
(10,10,0,0,0,0), (9,11,0,0,0,0), (0,0,20,0,0,0),
(0,0,0,10,10,0), (0,0,0,2,18,0), (0,0,0,0,0,20).
The deterministic four-group encoder sends the sources to AU,AU,AV,BU,BU,BV.
For any common decoder D (four stochastic rows, one per group), its prepared distribution is q_i(D)=sum_x M_ix D_group(x). Its loss on a behavior theta is
L_D(theta)=max_{i=1..6} TV(p_i(theta),q_i(D)), TV(p,q)=sum_t |p_t-q_t|/2.
Bank risk G(theta)=min_{d=1..10} L_d(theta).
Freeze the FIRST EIGHT decoder tables (group order AU AV BU BV, pair ij means masses 1/2 at i,j):
1: 34 24 34 24; 2: 34 23 34 34; 3: 34 34 34 23; 4: 24 24 12 12;
5: 12 12 24 34; 6: 12 13 23 24; 7: 23 34 12 13; 8: 24 34 12 14.
Let decoder 9 and decoder 10 range independently over ALL REAL stochastic 4x4 kernels.

Write O(s,t)=(s,t,0,0,0;0,1,1,1,0,1), N(s,t)=(s,t,0,0,0;1,0,0,0,0,0). Select five lawful policies:
W=(1,0,0,0,1;0,0,0,0,0,0);
J=(1,1/3,0,0,0;0,0,0,0,1,0);
A=O(1/7,1); B=O(1,1/7); C=N(1/7,1).

**Theorem.** On S5={W,J,A,B,C} the EXACT two-free-decoder minimax is
inf_{D9,D10} max_{theta in S5} G(theta) = 32/63.
Consequently, on S={W,H,J} union O([0,1]^2) union N([0,1]^2), the same two-free-decoder minimax lies in [32/63,4/7]. This strengthens the predecessor's lower bound 1/2 by exactly 1/126 while retaining its separately proved all-real two-face upper bound 4/7.

## Elementary event inequality and exact ten-triple certificate

For any event E contained in {1,2,3,4}, TV(p,q)>=p(E)-q(E).
If ONE common decoder is within r of each of THREE policies x,y,z on the SAME prepared row i, and E_x,E_y,E_z are pairwise disjoint events, then
3r >= p_i(x)(E_x)+p_i(y)(E_y)+p_i(z)(E_z)-[q_i(E_x)+q_i(E_y)+q_i(E_z)]
>= p_i(x)(E_x)+p_i(y)(E_y)+p_i(z)(E_z)-1.
This holds for every stochastic group decoder, regardless of mixture or other row entries.

The following is the COMPLETE ten-triple table (every 3-element subset of S5); row is the original 1-based prepared input, and each event string lists its stop atoms in the corresponding witness order.

| triple | input row | event atoms | target probability sum | forced radius |
|---|---:|---|---:|---:|
| W,J,A | 6 (pure BV) | 2 / 4 / 1 | 8/3 | 5/9 |
| W,J,B | 6 | 2 / 14 / 3 | 20/7 | 13/21 |
| W,J,C | 6 | 2 / 4 / 1 | 8/3 | 5/9 |
| W,A,B | 6 | 2 / 1 / 3 | 20/7 | 13/21 |
| W,A,C | 3 (pure AV) | 1 / 3 / 4 | 19/7 | 4/7 |
| W,B,C | 6 | 2 / 3 / 1 | 20/7 | 13/21 |
| J,A,B | 6 | 4 / 1 / 3 | 53/21 | 32/63 |
| J,A,C | 3 | 1 / 3 / 4 | 19/7 | 4/7 |
| J,B,C | 6 | 4 / 3 / 1 | 53/21 | 32/63 |
| A,B,C | 3 | 3 / 1 / 24 | 19/7 | 4/7 |

Every entry is checked with exact Fraction arithmetic against the original six-source law; each event triple is disjoint. Thus **any** decoder covering any three of the five at radius r must have r>=32/63. The first eight fixed decoders have exact minimum risks (W:1, J:2/3, A:4/7, B:4/7, C:4/7), each strictly larger than 32/63. At any proposed r<32/63 all five must therefore be assigned to the two new decoder labels. By pigeonhole one of those labels serves at least three, contradicting the ten-triple certificate. This proves the universal real-kernel lower bound.

## Two explicit rational common decoders attain 32/63

All entries below are nonnegative and each 4-stop row sums to exactly 1.

| decoder | encoded group | t1 | t2 | t3 | t4 |
|---|---|---:|---:|---:|---:|
| 9 | AU | 9/14 | 0 | 5/14 | 0 |
| 9 | AV | 9/14 | 0 | 0 | 5/14 |
| 9 | BU | 1/2 | 0 | 0 | 1/2 |
| 9 | BV | 1/2 | 1/2 | 0 | 0 |
| 10 | AU | 41/63 | 0 | 22/63 | 0 |
| 10 | AV | 41/63 | 0 | 22/63 | 0 |
| 10 | BU | 29/45 | 0 | 29/315 | 83/315 |
| 10 | BV | 31/63 | 0 | 22/63 | 10/63 |

Exact original six-preparation comparisons give:
- Decoder 9 on W: six row risks (5/14,5/14,5/14,1/2,1/2,1/2), hence L9(W)=1/2.
- Decoder 9 on C: six row risks (1/2,1/2,1/2,1/2,1/2,1/2), hence L9(C)=1/2.
- Decoder 10 on J: (22/63,22/63,22/63,14/45,32/63,32/63), hence L10(J)=32/63.
- Decoder 10 on A: (32/63,32/63,32/63,16/45,16/45,32/63), hence L10(A)=32/63.
- Decoder 10 on B: (22/63,22/63,22/63,158/315,32/63,32/63), hence L10(B)=32/63.

Thus G<=32/63 on all five, with equality for J,A,B. Combining with the exact lower bound proves the theorem.

## Executed validation and scope

VERIFY.py is a Python standard-library Fraction program actually executed locally with the full positive six-source mixture and four stops. It checks all ten disjoint-event dual certificates; all six prepared row losses for each of five witnesses; fixed-eight exact risk floors; and explicit stochastic normalization. RUN_EVIDENCE.json is the captured stdout of that execution. All-real decoder universality follows from the event and pigeonhole argument, not from finite sampling or floating-point LP. Initial candidate finding used SciPy numerical LP/MILP, but NO numerical optimizer is assumed in the theorem certificate.

P000's six native spatial axes, three-dimensional research slice and independent time are not statistical source labels; no native-fidelity transfer is claimed. The full eleven-real-control ten-label minimax remains bounded [1/2,2/3] for k=4,6. The present two-face restricted minimax is in [32/63,4/7]. Mathematical review/admission and native CLAIM/Result remain separate.
